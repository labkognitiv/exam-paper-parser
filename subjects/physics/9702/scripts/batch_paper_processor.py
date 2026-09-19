#!/usr/bin/env python3
"""
Batch Cambridge Physics P2 End-to-End Pipeline Processor
Automates full-paper processing for any or all Cambridge Physics Paper 2 exams:

1. Deterministic Question Paper Slicing:
   - Compact PNGs (answer spaces and dots masked)
   - Printable PNGs (authentic answer spaces preserved)
   - Compiled PDFs: paper_compact.pdf & paper_printable.pdf
2. Deterministic Mark Scheme Slicing:
   - Question-by-question MS PNGs (ms_q01.png ... ms_q08.png)
   - Compiled PDF: paper_markscheme.pdf
3. AI Pass 1: Question & Mark Scheme OCR (Meta Muse Spark 1.3 Contributor)
4. AI Pass 2: Pedagogical Enrichment (Progressive Hints, Teacher Walkthrough with explicit arithmetic, Pitfalls, Formulas, Pacing)
5. Metric & Cost Tracking across all papers

Modes:
- Single paper: ./batch_paper_processor.py --paper 9702_s23_21
- Multiple papers: ./batch_paper_processor.py --papers 9702_s23_21 9702_s23_22
- Filter by year: ./batch_paper_processor.py --years 2023 2024
- Batch limit: ./batch_paper_processor.py --all --limit 5
- All 100+ papers: ./batch_paper_processor.py --all
"""

import argparse
import base64
import json
import re
import subprocess
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import pymupdf

# Ensure script directory is in sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Import slicers
from p2_dual_parser import (
    detect_questions,
    make_compact_sanitized_copy,
    render_compact_question,
    render_printable_question,
    extract_question_figures,
)
from slice_mark_scheme import slice_mark_scheme

ROOT_DIR = Path(__file__).resolve().parent.parent
PAPERS_BASE = ROOT_DIR / "9702/past papers/p2"

MODEL_ID = "meta/muse-spark-1.3-contributor"
PRICING_PROMPT = 0.10 / 1_000_000
PRICING_COMPL = 0.20 / 1_000_000

def get_api_key():
    cmd = ["security", "find-generic-password", "-s", "kognitiv-openrouter-api-key", "-w"]
    return subprocess.check_output(cmd).decode("utf-8").strip()

OCR_SYSTEM_PROMPT = """You are an expert Cambridge Physics (9702) past paper digitizer.
Your goal is to transcribe the question image and official mark scheme image with 100% verbatim fidelity into a structured JSON object.

OUTPUT JSON SCHEMA:
{
  "question_num": int,
  "total_marks": int,
  "title": "Topic title (e.g. Kinematics, Dynamics, Waves, D.C. circuits)",
  "main_stem": "Initial narrative text introducing the question before any parts. If Fig. X.Y is referenced, insert {{figure:fig_X_Y}} right after the sentence. Math strictly in $...$ or $$...$$.",
  "parts": [
    {
      "label": "(a)(i)",
      "part_stem": "Introductory text shared across child subparts or null. If Fig. X.Y is referenced, insert {{figure:fig_X_Y}}.",
      "text": "The prompt text. If Fig. X.Y is referenced, insert {{figure:fig_X_Y}}. All math strictly in $...$ or $$...$$.",
      "marks": int,
      "answer_prompt": "Verbatim prompt printed before the answer line (e.g. 'speed =', 'T =', 'a =', 'momentum =', 'decrease in potential energy =') or null",
      "unit": "Verbatim SI unit printed at the end of the answer line (e.g. 'm s^{-1}', 'N m', 'J', 'kg', 'm s^{-2}', '\\\\Omega') or null"
    }
  ],
  "markscheme": [
    {
      "label": "(a)(i)",
      "marks": int,
      "marking_points": [
        {"tag": "C1", "text": "use of s = ut + 1/2 a t^2"},
        {"tag": "A1", "text": "t = 2.7 s"}
      ]
    }
  ]
}

STRICT RULES:
1. Verbatim accuracy: Transcribe every word and condition from the question and mark scheme images. Never paraphrase.
2. Answer prompts & units: Look carefully at the answer space at the bottom of each subpart. Always capture answer_prompt (e.g. 'a =') and unit (e.g. 'm s^{-2}') if printed.
3. Mark scheme: Transcribe official mark scheme points verbatim with their exact criterion tags (B1, M1, A1, C1). Do NOT summarize or invent text.
4. Figures: When the question text refers to 'Fig. X.Y' or 'as shown in Fig. X.Y', insert '{{figure:fig_X_Y}}' immediately following that reference.
5. Math in LaTeX: Enclose all variables, formulas, and units in $...$ or $$...$$.
6. Output strictly valid JSON.
"""

ENRICHMENT_SYSTEM_PROMPT = """You are an expert Cambridge International AS-Level Physics (9702) Master Teacher and Chief Examiner.
Your task is to generate natural, step-by-step learning walkthroughs and enrichment modeled after the gold-standard Cambridge Mathematics M1 and S1 walkthroughs.

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
      "formulas_used": ["p = mv", "p_{AB} = mv \\\\cos\\\\theta"],
      "hints": [
        "Hint 1: Core physical concept or diagram clue (do not reveal final answer).",
        "Hint 2: Formula setup or necessary unit conversion."
      ],
      "teacher_walkthrough": [
        "Step 1: **Clear Step Heading**\\nShort, friendly teacher explanation (1-2 clear, natural sentences):\\nExplain the physical concept and why this formula applies.\\n\\nVertical calculation (never chain equalities horizontally):\\n$$\\\\begin{aligned}\\\\nF_D &= \\\\frac{P}{v} \\\\\\\\\n&= \\\\frac{75000}{25} \\\\\\\\\n&= 3000\\\\text{ N}\\\\n\\\\end{aligned}$$",
        "Step 2: **Next Step Heading**\\n..."
      ],
      "common_pitfalls": [
        "Trap 1: Real examiner-reported candidate mistake.",
        "Trap 2: Common unit, angle, or calculation trap."
      ]
    }
  ]
}

STRICT STANDARDS:
1. NATURAL TEACHER VOICE:
   - Sounds like a warm, supportive Cambridge physics teacher.
   - Keep introductory sentences short, human-friendly, and natural (1-2 sentences maximum per step).
   - Avoid dense multi-line paragraphs. Never use artificial labels like 'Main Idea:' or 'Why this applies:'.

2. VERTICAL CALCULATIONS ONLY:
   - All calculations MUST be laid out vertically line-by-line using `\\\\begin{aligned} ... \\\\end{aligned}` or discrete vertical equations.
   - NEVER chain calculations horizontally (e.g. avoid `a = b = c = d`). Each algebraic manipulation or numerical evaluation belongs on its own line.

3. NO EXAM MARK TAGS OR TRAP CALLOUTS IN STEPS:
   - DO NOT write mark tags like `[C1 Mark]`, `[M1 Mark]`, `[A1 Mark]` or `[B1 Mark]` anywhere in the step text or headings.
   - DO NOT include common trap labels or warnings inside the step text (common pitfalls belong exclusively in the `common_pitfalls` array).

4. STEPPED PROGRESSION:
   - Heading format: 'Step N: **Descriptive Heading**'
   - Step 1 sets up the initial concept or resolves components.
   - Step 2 establishes the governing relation or equates conserved quantities.
   - Step 3 solves vertically for the final target quantity with units.

5. Mark-Proportional Tiered Hints (`hints`):
   - Exactly 1 hint per mark. Never reveal the final calculated value.

6. Formatting Rules:
   - Math strictly in LaTeX: $...$ for inline, $$...$$ for display equations.
   - STRICT: Zero em dashes ('—') and zero en dashes ('–'). Use hyphens, colons, or parentheses instead.
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

def call_muse_spark(api_key, system_prompt, user_content, max_tokens=6500, max_retries=3):
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
        "X-Title": "Kognitiv Batch Processor"
    }
    
    for attempt in range(max_retries):
        try:
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
        except Exception as e:
            if attempt < max_retries - 1:
                wait_sec = 3 * (attempt + 1)
                print(f"      [Retry {attempt+1}/{max_retries}] error: {e}. Waiting {wait_sec}s...")
                time.sleep(wait_sec)
            else:
                return {
                    "elapsed_sec": 0,
                    "tokens": {"prompt_tokens": 0, "completion_tokens": 0, "reasoning_tokens": 0, "total_tokens": 0},
                    "cost_usd": 0.0,
                    "valid_json": False,
                    "parsed_json": None,
                    "raw_content": f"Error: {e}"
                }

def discover_papers(base_dir: Path) -> list[dict]:
    papers = []
    for qp_path in sorted(base_dir.glob("**/source/*_qp_*.pdf")):
        paper_code = qp_path.stem.replace("_qp_", "_")
        ms_candidates = list(qp_path.parent.glob("*_ms_*.pdf"))
        if ms_candidates:
            papers.append({
                "paper_code": paper_code,
                "qp_path": qp_path,
                "ms_path": ms_candidates[0],
                "year_dir": qp_path.parent.parent
            })
    return papers

def process_single_paper(paper_info: dict, output_dir: Path, api_key: str, resume: bool = True, max_workers: int = 3) -> dict:
    qp_pdf = paper_info["qp_path"]
    ms_pdf = paper_info["ms_path"]
    paper_code = paper_info["paper_code"]
    paper_out_dir = output_dir / paper_code
    paper_out_dir.mkdir(parents=True, exist_ok=True)
    
    print("\n" + "=" * 70)
    print(f"PROCESSING PAPER: {paper_code}")
    print(f"QP: {qp_pdf.name} | MS: {ms_pdf.name}")
    print(f"Directory: {paper_out_dir}")
    print("=" * 70)
    
    summary_file = paper_out_dir / "paper_summary.json"
    if resume and summary_file.exists():
        try:
            with open(summary_file, encoding="utf-8") as f:
                summary = json.load(f)
            print(f"✓ {paper_code} is already completely processed! Loaded summary (Cost: ${summary.get('total_cost_usd', 0.0):.6f})")
            return summary
        except Exception:
            pass
            
    paper_start = time.time()
    total_cost = 0.0
    total_prompt_tokens = 0
    total_completion_tokens = 0
    total_reasoning_tokens = 0
    
    # 1. Slicing Question Paper & Extracting Figures
    print("  [1/4] Slicing Question Paper & Extracting Diagrams...")
    qp_doc = pymupdf.open(qp_pdf)
    questions = detect_questions(qp_doc)
    
    compact_pdf = paper_out_dir / "paper_compact.pdf"
    printable_pdf = paper_out_dir / "paper_printable.pdf"
    
    if resume and compact_pdf.exists() and printable_pdf.exists():
        print(f"    [Resumed] Compact & Printable PDFs already exist for {len(questions)} questions.")
        qp_doc.close()
    else:
        sanitized_qp_doc = make_compact_sanitized_copy(qp_doc)
        compact_pngs = []
        printable_pngs = []
        compiled_compact_doc = pymupdf.open()
        compiled_printable_doc = pymupdf.open()
        
        for q in questions:
            c_png = render_compact_question(sanitized_qp_doc, q, paper_out_dir, dpi=150)
            p_png = render_printable_question(qp_doc, q, paper_out_dir, dpi=150)
            compact_pngs.append(c_png)
            printable_pngs.append(p_png)
            
            with pymupdf.open(paper_out_dir / f"question_{q.number:02d}_printable.pdf") as qpdf:
                compiled_printable_doc.insert_pdf(qpdf)
                
        sanitized_qp_doc.close()
        qp_doc.close()
        
        for cpng in compact_pngs:
            with pymupdf.open(cpng) as img_doc:
                pdf_bytes = img_doc.convert_to_pdf()
                with pymupdf.open("pdf", pdf_bytes) as qpdf:
                    compiled_compact_doc.insert_pdf(qpdf)
                    
        compiled_compact_doc.save(compact_pdf)
        compiled_printable_doc.save(printable_pdf)
        compiled_compact_doc.close()
        compiled_printable_doc.close()
    
    # Extract standalone figure diagrams per question
    q_figures_map = {}
    figs_needed = (not resume) or any(not (paper_out_dir / f"question_{q.number:02d}_figures.json").exists() for q in questions)
    if figs_needed:
        qp_fig_doc = pymupdf.open(qp_pdf)
        for q in questions:
            figs = extract_question_figures(qp_fig_doc, q, paper_out_dir, dpi=150)
            q_figures_map[q.number] = figs
            with open(paper_out_dir / f"question_{q.number:02d}_figures.json", "w", encoding="utf-8") as f_out:
                json.dump(figs, f_out, indent=2, ensure_ascii=False)
        qp_fig_doc.close()
    else:
        for q in questions:
            try:
                with open(paper_out_dir / f"question_{q.number:02d}_figures.json", encoding="utf-8") as f_in:
                    q_figures_map[q.number] = json.load(f_in)
            except Exception:
                q_figures_map[q.number] = []
    
    # 2. Slicing Mark Scheme
    print("  [2/4] Slicing Mark Scheme...")
    ms_dir = paper_out_dir / "mark_scheme"
    if resume and (ms_dir / "paper_markscheme.pdf").exists():
        print("    [Resumed] Mark scheme already sliced.")
    else:
        slice_mark_scheme(ms_pdf, ms_dir, dpi=150)
    
    # 3. AI Pass 1: OCR (Parallel)
    print(f"  [3/4] AI Pass 1: Question & Mark Scheme OCR (Parallel, {max_workers} workers)...")
    ocr_data = {}
    
    def process_ocr_q(q):
        ocr_file = paper_out_dir / f"question_{q.number:02d}_ocr.json"
        meta_file = paper_out_dir / f"question_{q.number:02d}_ocr_meta.json"
        if resume and ocr_file.exists():
            try:
                with open(ocr_file, encoding="utf-8") as f:
                    data = json.load(f)
                meta = {}
                if meta_file.exists():
                    with open(meta_file, encoding="utf-8") as f:
                        meta = json.load(f)
                else:
                    prompt_toks = 2000
                    comp_toks = len(json.dumps(data)) // 4
                    meta = {
                        "tokens": {
                            "prompt_tokens": prompt_toks,
                            "completion_tokens": comp_toks,
                            "reasoning_tokens": 500,
                            "total_tokens": prompt_toks + comp_toks
                        },
                        "cost_usd": (prompt_toks * PRICING_PROMPT) + (comp_toks * PRICING_COMPL)
                    }
                return q.number, data, meta, True
            except Exception:
                pass

        printable_png = paper_out_dir / f"question_{q.number:02d}_printable.png"
        ms_png = ms_dir / f"ms_q{q.number:02d}.png"
        
        with open(printable_png, "rb") as f1, open(ms_png, "rb") as f2:
            b64_q = base64.b64encode(f1.read()).decode()
            b64_ms = base64.b64encode(f2.read()).decode()
            
        q_figs = q_figures_map.get(q.number, [])
        fig_note = ""
        if q_figs:
            fig_ids = [f"{fig['label']} -> token {{{{figure:{fig['id']}}}}}" for fig in q_figs]
            fig_note = f"\nDetected figures in this question: {', '.join(fig_ids)}. Place each figure token immediately after its reference or caption in main_stem or part text."
            
        user_content = [
            {"type": "text", "text": f"Digitize Question {q.number} and its Mark Scheme with 100% verbatim fidelity. Capture all answer prompts and units.{fig_note}"},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64_q}"}},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64_ms}"}}
        ]
        
        res = call_muse_spark(api_key, OCR_SYSTEM_PROMPT, user_content, max_tokens=6500)
        pj = res.get("parsed_json") or {"raw": res.get("raw_content")}
        with open(ocr_file, "w", encoding="utf-8") as out_f:
            json.dump(pj, out_f, indent=2, ensure_ascii=False)
        with open(meta_file, "w", encoding="utf-8") as out_f:
            json.dump(res, out_f, indent=2, ensure_ascii=False)
        return q.number, pj, res, False

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_ocr_q, q): q for q in questions}
        for future in as_completed(futures):
            q_num, pj, res, was_cached = future.result()
            ocr_data[q_num] = pj
            cost = res.get("cost_usd", 0.0)
            t = res.get("tokens", {})
            total_cost += cost
            total_prompt_tokens += t.get("prompt_tokens", 0)
            total_completion_tokens += t.get("completion_tokens", 0)
            total_reasoning_tokens += t.get("reasoning_tokens", 0)
            if was_cached:
                print(f"    Q{q_num:02d} OCR: [Resumed from cache]")
            else:
                print(f"    Q{q_num:02d} OCR: {res.get('elapsed_sec')}s | Cost: ${cost:.6f} | Valid: {res.get('valid_json')}")
        
    # 4. AI Pass 2: Enrichment (Parallel)
    print(f"  [4/4] AI Pass 2: Pedagogical Enrichment (Parallel, {max_workers} workers)...")
    enrichment_data = {}
    
    def process_enrichment_q(q):
        enrichment_file = paper_out_dir / f"question_{q.number:02d}_enrichment.json"
        meta_file = paper_out_dir / f"question_{q.number:02d}_enrichment_meta.json"
        if resume and enrichment_file.exists():
            try:
                with open(enrichment_file, encoding="utf-8") as f:
                    data = json.load(f)
                meta = {}
                if meta_file.exists():
                    with open(meta_file, encoding="utf-8") as f:
                        meta = json.load(f)
                else:
                    prompt_toks = 2500
                    comp_toks = len(json.dumps(data)) // 4
                    meta = {
                        "tokens": {
                            "prompt_tokens": prompt_toks,
                            "completion_tokens": comp_toks,
                            "reasoning_tokens": 1500,
                            "total_tokens": prompt_toks + comp_toks
                        },
                        "cost_usd": (prompt_toks * PRICING_PROMPT) + (comp_toks * PRICING_COMPL)
                    }
                return q.number, data, meta, True
            except Exception:
                pass

        q_ocr = ocr_data.get(q.number) or {}
        printable_png = paper_out_dir / f"question_{q.number:02d}_printable.png"
        with open(printable_png, "rb") as f1:
            b64_q = base64.b64encode(f1.read()).decode()
            
        prompt_text = f"""### Question Information (including Verbatim Mark Scheme):
{json.dumps(q_ocr, indent=2)}

Now generate complete pedagogical enrichment adhering strictly to the Cambridge M1/S1 walkthrough style:
1. Stepped teacher walkthrough: Natural teacher voice (NO artificial meta-labels). Write a clear step heading, followed by brief friendly bullets explaining the step, followed by the PROPER, complete calculation in display math ($$...$$). Clearly note which official mark is earned ([C1 Mark], [M1 Mark], [A1 Mark], [B1 Mark]).
2. Mark-proportional tiered hints (1 hint per mark).
3. Realistic examiner-reported pitfalls and formulas used."""
        user_content = [
            {"type": "text", "text": prompt_text},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64_q}"}}
        ]
        
        res = call_muse_spark(api_key, ENRICHMENT_SYSTEM_PROMPT, user_content, max_tokens=6500)
        pj = res.get("parsed_json") or {"raw": res.get("raw_content")}
        with open(enrichment_file, "w", encoding="utf-8") as out_f:
            json.dump(pj, out_f, indent=2, ensure_ascii=False)
        with open(meta_file, "w", encoding="utf-8") as out_f:
            json.dump(res, out_f, indent=2, ensure_ascii=False)
        return q.number, pj, res, False

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_enrichment_q, q): q for q in questions}
        for future in as_completed(futures):
            q_num, pj, res, was_cached = future.result()
            enrichment_data[q_num] = pj
            cost = res.get("cost_usd", 0.0)
            t = res.get("tokens", {})
            total_cost += cost
            total_prompt_tokens += t.get("prompt_tokens", 0)
            total_completion_tokens += t.get("completion_tokens", 0)
            total_reasoning_tokens += t.get("reasoning_tokens", 0)
            if was_cached:
                print(f"    Q{q_num:02d} Enrichment: [Resumed from cache]")
            else:
                print(f"    Q{q_num:02d} Enrichment: {res.get('elapsed_sec')}s | Cost: ${cost:.6f} | Valid: {res.get('valid_json')}")
        
    paper_elapsed = time.time() - paper_start
    summary = {
        "paper_code": paper_code,
        "total_questions": len(questions),
        "paper_elapsed_sec": round(paper_elapsed, 2),
        "total_cost_usd": round(total_cost, 6),
        "tokens": {
            "prompt_tokens": total_prompt_tokens,
            "completion_tokens": total_completion_tokens,
            "reasoning_tokens": total_reasoning_tokens,
            "total_tokens": total_prompt_tokens + total_completion_tokens
        }
    }
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
        
    print(f"✓ {paper_code} Finished in {paper_elapsed:.1f}s | Cost: ${total_cost:.6f}")
    return summary

def main():
    parser = argparse.ArgumentParser(description="Batch Processor for Cambridge Physics P2 Papers")
    parser.add_argument("--all", action="store_true", help="Process all discoverable past papers")
    parser.add_argument("--paper", type=str, help="Process a single paper by code (e.g. 9702_s23_21)")
    parser.add_argument("--papers", nargs="+", help="Process a list of paper codes")
    parser.add_argument("--years", nargs="+", help="Filter papers by years (e.g. 2022 2023)")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of papers to process")
    parser.add_argument("--output-dir", type=Path, default=ROOT_DIR / "testing/output_batch_papers", help="Output directory")
    parser.add_argument("--workers", type=int, default=8, help="Number of concurrent workers for AI calls (default: 8)")
    parser.add_argument("--no-resume", action="store_true", help="Do not resume from cached OCR / enrichment JSONs")
    args = parser.parse_args()
    
    api_key = get_api_key()
    all_discovered = discover_papers(PAPERS_BASE)
    print(f"Total Cambridge Physics P2 papers discovered in repository: {len(all_discovered)}")
    
    # Filter selection
    target_papers = []
    if args.paper:
        target_papers = [p for p in all_discovered if args.paper.lower() in p["paper_code"].lower()]
    elif args.papers:
        target_papers = [p for p in all_discovered if any(code.lower() in p["paper_code"].lower() for code in args.papers)]
    elif args.years:
        target_papers = [p for p in all_discovered if any(yr in str(p["qp_path"]) for yr in args.years)]
    elif args.all:
        target_papers = all_discovered
    else:
        print("Please specify --paper, --papers, --years, or --all.")
        print("Example: ./batch_paper_processor.py --paper 9702_s23_21")
        sys.exit(0)
        
    if args.limit:
        target_papers = target_papers[:args.limit]
        
    print(f"Selected {len(target_papers)} paper(s) to process.")
    
    batch_start = time.time()
    batch_results = []
    total_batch_cost = 0.0
    
    for idx, p_info in enumerate(target_papers, start=1):
        print(f"\n>>> Progress: [{idx}/{len(target_papers)}] <<<")
        try:
            res = process_single_paper(p_info, args.output_dir, api_key, resume=not args.no_resume, max_workers=args.workers)
            batch_results.append(res)
            total_batch_cost += res.get("total_cost_usd", 0.0)
        except Exception as e:
            print(f"❌ Error processing {p_info['paper_code']}: {e}")
            
    batch_elapsed = time.time() - batch_start
    batch_summary = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "papers_processed": len(batch_results),
        "total_elapsed_sec": round(batch_elapsed, 2),
        "total_cost_usd": round(total_batch_cost, 6),
        "average_cost_per_paper": round(total_batch_cost / max(1, len(batch_results)), 6),
        "projected_cost_70_papers": round((total_batch_cost / max(1, len(batch_results))) * 70, 2),
        "results": batch_results
    }
    
    summary_path = args.output_dir / "batch_summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(batch_summary, f, indent=2, ensure_ascii=False)
        
    print("\n" + "=" * 70)
    print("BATCH PROCESSING COMPLETE!")
    print(f"Papers Processed: {len(batch_results)}")
    print(f"Total Time: {batch_elapsed:.1f}s (Avg {batch_elapsed/max(1, len(batch_results)):.1f}s / paper)")
    print(f"TOTAL BATCH COST: ${total_batch_cost:.6f}")
    print(f"PROJECTED COST FOR 70 PAPERS: ${batch_summary['projected_cost_70_papers']:.2f}")
    print(f"Batch Summary Saved: {summary_path}")
    print("=" * 70)

if __name__ == "__main__":
    main()
