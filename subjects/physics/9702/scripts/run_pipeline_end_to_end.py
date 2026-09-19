#!/usr/bin/env python3
"""
End-to-End Cambridge Physics P2 Paper Processor
Runs the full pipeline on any Cambridge Physics P2 paper:
1. Deterministic Question Paper Dual Slicing (Compact PNGs, Printable PNGs, Compiled PDFs)
2. Deterministic Mark Scheme Slicing (Question by Question MS PNGs, Compiled MS PDF)
3. AI Pass 1: Question & Mark Scheme OCR (Meta Muse Spark)
4. AI Pass 2: Pedagogical Enrichment (Meta Muse Spark)
5. Metric Consolidation (Tokens, Latency, Cost USD)
"""

import argparse
import base64
import json
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path
import pymupdf

# Import our slicers
from p2_dual_parser import detect_questions, make_compact_sanitized_copy, render_compact_question, render_printable_question
from slice_mark_scheme import slice_mark_scheme

MODEL_ID = "meta/muse-spark-1.3-contributor"
PRICING_PROMPT = 0.10 / 1_000_000
PRICING_COMPL = 0.20 / 1_000_000

def get_api_key():
    cmd = ["security", "find-generic-password", "-s", "kognitiv-openrouter-api-key", "-w"]
    return subprocess.check_output(cmd).decode("utf-8").strip()

# --- PROMPTS ---

OCR_SYSTEM_PROMPT = """You are an expert Cambridge Physics (9702) past paper digitizer.
Your goal is to transcribe the question image and the official mark scheme image with 100% fidelity into a structured JSON object.

OUTPUT JSON SCHEMA:
{
  "question_num": int,
  "total_marks": int,
  "title": "Short descriptive topic title (e.g. Kinematics, Dynamics, Waves, D.C. circuits)",
  "main_stem": "Initial narrative text introducing the question before any parts. Math strictly in $...$ or $$...$$.",
  "parts": [
    {
      "label": "(a)(i)",
      "part_stem": "Introductory text shared across child subparts or null",
      "text": "The prompt text. All math strictly in $...$ or $$...$$.",
      "marks": int,
      "answer_prompt": "Prompt preceding answer line (e.g. 'speed =', 'T =') or null",
      "unit": "SI unit (e.g. 'm s^{-1}', 'N m', 'J') or null"
    }
  ],
  "markscheme": [
    {
      "label": "(a)(i)",
      "marks": int,
      "marking_points": [
        {"tag": "B1", "text": "..."},
        {"tag": "C1", "text": "..."}
      ]
    }
  ]
}

STRICT RULES:
1. Verbatim accuracy: Transcribe every word and condition from the question and mark scheme images.
2. Math in LaTeX: Enclose all variables, formulas, and units in $...$ or $$...$$.
3. Output strictly valid JSON with no markdown wrapping if possible.
"""

ENRICHMENT_SYSTEM_PROMPT = """You are an expert Cambridge International AS-Level Physics (9702) teacher and curriculum author.
Your task is to generate clean pedagogical learning enrichment for the provided digitized past paper question.

You are provided with:
1. Digitized Question Stem and Parts text (with mark counts).
2. Official Cambridge Mark Scheme text and marking codes.
3. Cropped question image (for visual reference if diagrams exist).

OUTPUT JSON SCHEMA:
{
  "question_num": int,
  "difficulty": 2,
  "question_patterns": ["graph_interpretation", "direct_calculation"],
  "parts": [
    {
      "part": "(a)(i)",
      "difficulty": 1,
      "question_patterns": ["property_identification"],
      "target_time_minutes": int,
      "formulas_used": ["F = kx", "k = \\frac{F}{x}"],
      "hints": [
        "Hint 1..."
      ],
      "teacher_walkthrough": [
        "Step 1...",
        "Step 2..."
      ],
      "walkthrough": [
        "Mark scheme step 1..."
      ],
      "common_pitfalls": [
        "Trap 1..."
      ]
    }
  ]
}

STRICT PEDAGOGICAL STANDARDS:
1. Mark-Proportional Tiered Hints (`hints`):
   - Exactly 1 hint per mark (1 mark = 1 hint, 2 marks = 2 hints, 3 marks = 3 hints).
   - Hint 1: core concept or diagram reading. Hint 2: formula setup or unit conversion. Hint 3: algebraic resolution.
   - NEVER give away the final numerical value.
2. Humane Teacher Walkthrough (`teacher_walkthrough`):
   - NO conversational fluff ("Hello", "Lovely", "Great", "Now for the calculation").
   - Start immediately with the physical law, principle, or governing formula.
   - Show ALL intermediate arithmetic and algebraic calculations explicitly, line by line (substitutions, powers of 10, intermediate arithmetic products, unit conversions).
   - Formats math with LaTeX ($$...$$ for display, $...$ for inline).
   - STRICT: Zero em dashes ("—") and zero en dashes ("–").
3. Common Pitfalls (`common_pitfalls`):
   - 2 to 3 real examiner-reported traps.
4. Formulas Used (`formulas_used`):
   - Clean LaTeX equations used in this part (no database IDs).
5. Target Time (`target_time_minutes`):
   - Equal to round(1.25 * marks), min 1.
"""

def extract_json(raw_text):
    if not raw_text:
        return None
    m = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", raw_text)
    candidate = m.group(1) if m else raw_text.strip()
    try:
        return json.loads(candidate)
    except Exception:
        start = candidate.find("{")
        end = candidate.rfind("}")
        if start != -1 and end != -1:
            try:
                return json.loads(candidate[start:end+1])
            except Exception:
                return None
    return None

def call_muse_spark(api_key, system_prompt, user_content, max_tokens=5000):
    req_body = {
        "model": MODEL_ID,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ],
        "reasoning": {"effort": "low"},
        "max_tokens": max_tokens,
        "temperature": 0.2
    }
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://kognitiv.io",
        "X-Title": "Kognitiv Master Pipeline"
    }
    
    start_time = time.time()
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(req_body).encode("utf-8"),
        headers=headers
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        elapsed = time.time() - start_time
        data = json.loads(resp.read().decode("utf-8"))
        
        choice = data["choices"][0]
        raw_content = choice["message"].get("content") or ""
        usage = data.get("usage", {})
        
        prompt_tokens = usage.get("prompt_tokens", 0)
        completion_tokens = usage.get("completion_tokens", 0)
        reasoning_tokens = usage.get("completion_tokens_details", {}).get("reasoning_tokens", 0)
        
        cost = usage.get("cost")
        if cost is None:
            cost = (prompt_tokens * PRICING_PROMPT) + (completion_tokens * PRICING_COMPL)
            
        parsed_json = extract_json(raw_content)
        
        return {
            "elapsed_sec": round(elapsed, 2),
            "tokens": {
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "reasoning_tokens": reasoning_tokens,
                "total_tokens": prompt_tokens + completion_tokens
            },
            "cost_usd": round(cost, 6),
            "valid_json": parsed_json is not None,
            "parsed_json": parsed_json,
            "raw_content": raw_content
        }

def run_pipeline_for_paper(qp_pdf: Path, ms_pdf: Path, output_dir: Path):
    api_key = get_api_key()
    output_dir.mkdir(parents=True, exist_ok=True)
    paper_code = qp_pdf.stem.replace("_qp_", "_")
    
    print("=" * 70)
    print(f"STARTING END-TO-END PIPELINE FOR: {paper_code}")
    print(f"QP Source: {qp_pdf}")
    print(f"MS Source: {ms_pdf}")
    print(f"Output Directory: {output_dir}")
    print("=" * 70)
    
    pipeline_start = time.time()
    total_cost = 0.0
    total_prompt_tokens = 0
    total_completion_tokens = 0
    total_reasoning_tokens = 0
    
    # -------------------------------------------------------------
    # PHASE 1: Deterministic Question Paper Slicing
    # -------------------------------------------------------------
    print("\n[PHASE 1] Slicing Question Paper (Compact & Printable)...")
    qp_doc = pymupdf.open(qp_pdf)
    questions = detect_questions(qp_doc)
    print(f"  Detected {len(questions)} questions in {qp_pdf.name}")
    
    sanitized_qp_doc = make_compact_sanitized_copy(qp_doc)
    compact_pngs = []
    printable_pngs = []
    
    compiled_compact_doc = pymupdf.open()
    compiled_printable_doc = pymupdf.open()
    
    for q in questions:
        compact_png = render_compact_question(sanitized_qp_doc, q, output_dir, dpi=150)
        printable_png = render_printable_question(qp_doc, q, output_dir, dpi=150)
        compact_pngs.append(compact_png)
        printable_pngs.append(printable_png)
        
        # Add to compiled docs
        with pymupdf.open(output_dir / f"question_{q.number:02d}_printable.pdf") as qpdf:
            compiled_printable_doc.insert_pdf(qpdf)
            
    sanitized_qp_doc.close()
    qp_doc.close()
    
    # Compile paper_compact.pdf
    for cpng in compact_pngs:
        with pymupdf.open(cpng) as img_doc:
            pdf_bytes = img_doc.convert_to_pdf()
            with pymupdf.open("pdf", pdf_bytes) as qpdf:
                compiled_compact_doc.insert_pdf(qpdf)
                
    paper_compact_pdf = output_dir / "paper_compact.pdf"
    paper_printable_pdf = output_dir / "paper_printable.pdf"
    compiled_compact_doc.save(paper_compact_pdf)
    compiled_printable_doc.save(paper_printable_pdf)
    compiled_compact_doc.close()
    compiled_printable_doc.close()
    print(f"  ✓ Saved {len(compact_pngs)} compact & printable question pairs")
    print(f"  ✓ Compiled {paper_compact_pdf.name} and {paper_printable_pdf.name}")
    
    # -------------------------------------------------------------
    # PHASE 2: Deterministic Mark Scheme Slicing
    # -------------------------------------------------------------
    print("\n[PHASE 2] Slicing Mark Scheme Question-by-Question...")
    ms_dir = output_dir / "mark_scheme"
    ms_pngs = slice_mark_scheme(ms_pdf, ms_dir, dpi=150)
    print(f"  ✓ Sliced {len(ms_pngs)} question mark scheme images")
    
    # -------------------------------------------------------------
    # PHASE 3: AI Pass 1 - Question & Mark Scheme OCR
    # -------------------------------------------------------------
    print("\n[PHASE 3] AI Pass 1: Question & Mark Scheme OCR (Meta Muse Spark)...")
    ocr_results = {}
    
    for i, q in enumerate(questions, start=1):
        compact_png = output_dir / f"question_{q.number:02d}_compact.png"
        ms_png = ms_dir / f"ms_q{q.number:02d}.png"
        
        with open(compact_png, "rb") as f1, open(ms_png, "rb") as f2:
            b64_q = base64.b64encode(f1.read()).decode()
            b64_ms = base64.b64encode(f2.read()).decode()
            
        user_content = [
            {"type": "text", "text": f"Digitize Question {q.number} and its Mark Scheme with 100% fidelity."},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64_q}"}},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64_ms}"}}
        ]
        
        res = call_muse_spark(api_key, OCR_SYSTEM_PROMPT, user_content, max_tokens=4000)
        cost = res.get("cost_usd", 0.0)
        total_cost += cost
        t = res.get("tokens", {})
        total_prompt_tokens += t.get("prompt_tokens", 0)
        total_completion_tokens += t.get("completion_tokens", 0)
        total_reasoning_tokens += t.get("reasoning_tokens", 0)
        
        ocr_file = output_dir / f"question_{q.number:02d}_ocr.json"
        with open(ocr_file, "w", encoding="utf-8") as out_f:
            json.dump(res.get("parsed_json") or {"raw": res.get("raw_content")}, out_f, indent=2, ensure_ascii=False)
            
        ocr_results[q.number] = res.get("parsed_json")
        print(f"  Q{q.number:02d} OCR: {res['elapsed_sec']}s | Cost: ${cost:.6f} | Valid JSON: {res['valid_json']}")
        time.sleep(1.0)
        
    # -------------------------------------------------------------
    # PHASE 4: AI Pass 2 - Pedagogical Enrichment
    # -------------------------------------------------------------
    print("\n[PHASE 4] AI Pass 2: Pedagogical Enrichment (Meta Muse Spark)...")
    enrichment_results = {}
    
    for i, q in enumerate(questions, start=1):
        ocr_data = ocr_results.get(q.number) or {}
        compact_png = output_dir / f"question_{q.number:02d}_compact.png"
        with open(compact_png, "rb") as f1:
            b64_q = base64.b64encode(f1.read()).decode()
            
        prompt_text = f"### Question Information:\n{json.dumps(ocr_data, indent=2)}\n\nNow generate the complete pedagogical enrichment following the specified standards and schema."
        
        user_content = [
            {"type": "text", "text": prompt_text},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64_q}"}}
        ]
        
        res = call_muse_spark(api_key, ENRICHMENT_SYSTEM_PROMPT, user_content, max_tokens=5000)
        cost = res.get("cost_usd", 0.0)
        total_cost += cost
        t = res.get("tokens", {})
        total_prompt_tokens += t.get("prompt_tokens", 0)
        total_completion_tokens += t.get("completion_tokens", 0)
        total_reasoning_tokens += t.get("reasoning_tokens", 0)
        
        enrichment_file = output_dir / f"question_{q.number:02d}_enrichment.json"
        with open(enrichment_file, "w", encoding="utf-8") as out_f:
            json.dump(res.get("parsed_json") or {"raw": res.get("raw_content")}, out_f, indent=2, ensure_ascii=False)
            
        enrichment_results[q.number] = res.get("parsed_json")
        print(f"  Q{q.number:02d} Enrichment: {res['elapsed_sec']}s | Cost: ${cost:.6f} | Valid JSON: {res['valid_json']}")
        time.sleep(1.0)
        
    # -------------------------------------------------------------
    # PHASE 5: Consolidation & Performance Summary
    # -------------------------------------------------------------
    total_elapsed = time.time() - pipeline_start
    summary = {
        "paper_code": paper_code,
        "total_questions": len(questions),
        "total_elapsed_seconds": round(total_elapsed, 2),
        "total_cost_usd": round(total_cost, 6),
        "projected_cost_70_papers_usd": round(total_cost * 70, 4),
        "token_usage": {
            "prompt_tokens": total_prompt_tokens,
            "completion_tokens": total_completion_tokens,
            "reasoning_tokens": total_reasoning_tokens,
            "grand_total_tokens": total_prompt_tokens + total_completion_tokens
        },
        "artifacts_generated": {
            "compact_pdf": str(paper_compact_pdf),
            "printable_pdf": str(paper_printable_pdf),
            "markscheme_pdf": str(ms_dir / "paper_markscheme.pdf"),
            "question_compact_pngs": [str(p) for p in compact_pngs],
            "question_printable_pngs": [str(p) for p in printable_pngs],
            "mark_scheme_pngs": [str(p) for p in ms_pngs],
            "ocr_jsons": [str(output_dir / f"question_{q.number:02d}_ocr.json") for q in questions],
            "enrichment_jsons": [str(output_dir / f"question_{q.number:02d}_enrichment.json") for q in questions]
        }
    }
    
    summary_file = output_dir / "end_to_end_paper_summary.json"
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
        
    print("\n" + "=" * 70)
    print(f"END-TO-END PIPELINE COMPLETE FOR {paper_code}!")
    print(f"Total Questions Processed: {len(questions)}")
    print(f"Total Time: {total_elapsed:.2f}s (Average {total_elapsed/len(questions):.2f}s per question)")
    print(f"Total Prompt Tokens: {total_prompt_tokens:,}")
    print(f"Total Completion Tokens: {total_completion_tokens:,} (Reasoning: {total_reasoning_tokens:,})")
    print(f"TOTAL END-TO-END PAPER COST: ${total_cost:.6f}")
    print(f"PROJECTED COST FOR ALL 70 PAPERS: ${total_cost * 70:.2f}")
    print(f"Master Summary File: {summary_file}")
    print("=" * 70)
    return summary

def main():
    parser = argparse.ArgumentParser(description="End-to-End Cambridge Physics P2 Pipeline")
    parser.add_argument("qp_pdf", type=Path, help="Path to Question Paper PDF")
    parser.add_argument("ms_pdf", type=Path, help="Path to Mark Scheme PDF")
    parser.add_argument("--output-dir", type=Path, default=Path("output_pipeline"), help="Output directory")
    args = parser.parse_args()
    
    run_pipeline_for_paper(args.qp_pdf, args.ms_pdf, args.output_dir)

if __name__ == "__main__":
    main()
