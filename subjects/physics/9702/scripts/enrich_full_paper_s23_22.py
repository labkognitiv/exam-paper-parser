#!/usr/bin/env python3
"""
Full Paper Pedagogical Enrichment Script
Processes all 8 questions of Cambridge Physics 9702/22/M/J/23 using Meta Muse Spark 1.3 Contributor.
Outputs individual question enrichment JSONs and an aggregated cost & performance summary.
"""

import json
import base64
import time
import re
import urllib.request
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
QUESTIONS_DIR = ROOT_DIR / "9702/prototypes/past-paper-question-reviewer/public/data/questions"
ASSETS_DIR = ROOT_DIR / "9702/prototypes/past-paper-question-reviewer/public/data/assets"
OUTPUT_DIR = ROOT_DIR / "testing/output_enrichment_s23_22"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MODEL_ID = "meta/muse-spark-1.3-contributor"
MODEL_NAME = "Meta Muse Spark 1.3 Contributor"
PRICING_PROMPT = 0.10 / 1_000_000
PRICING_COMPL = 0.20 / 1_000_000

def get_api_key():
    cmd = ["security", "find-generic-password", "-s", "kognitiv-openrouter-api-key", "-w"]
    return subprocess.check_output(cmd).decode("utf-8").strip()

SYSTEM_PROMPT = """You are an expert Cambridge International AS-Level Physics (9702) teacher and curriculum author.
Your task is to generate high-quality pedagogical learning content and student enrichment for a past exam paper question.

You are provided with:
1. Question Stem and Parts text (with mark counts).
2. Official Cambridge Mark Scheme text and marking points.
3. Relevant diagram/figure images (if the question contains figures).

You must output a single, strictly valid JSON object. Do not include explanatory text outside the JSON.

### Strict Pedagogical Standards:

1. **Mark-Proportional Tiered Progressive Hints**:
   - For every marked part, the number of hints MUST strictly equal its mark count:
     * 1 mark = exactly 1 specific conceptual or observational hint.
     * 2 marks = exactly 2 tiered progressive hints.
     * 3 marks = exactly 3 tiered progressive hints.
   - Hints must be very specific, guiding the student on what physical relationship to look for, what values to read from the graph or text, or what algebraic setup is needed.
   - Progression:
     * Hint 1 directs student attention to the core physics concept, definition, or key diagram observation.
     * Hint 2 directs the student to the formula setup, variable relationship, or necessary unit conversion.
     * Hint 3 directs the algebraic rearrangement or intermediate calculation.
   - NEVER give away the final numerical answer or final calculated value in hints.

2. **Humane Teacher Walkthrough (`teacher_walkthrough`)**:
   - NO conversational fluff or pleasantries: Do NOT use phrases like "Hello", "Lovely", "Great", "Well done", or "Now for the calculation".
   - Start immediately with the physical principle, definition, or governing equation.
   - Show ALL intermediate arithmetic and algebraic calculations explicitly, line by line:
     * Write the governing formula.
     * Show the full numerical substitution.
     * Show intermediate arithmetic products, clearing of denominators, powers of 10, and unit conversions without skipping steps.
     * State the final calculated value with correct physical units.
   - Format math cleanly with LaTeX: display formulas in `$$...$$` on their own lines, inline variables in `$x$`.
   - STRICT CONSTRAINT: NO em dashes ("—") and NO en dashes ("–") anywhere. Use commas, colons, parentheses, or clear sentences.

3. **Technical Mark Scheme Walkthrough (`walkthrough`)**:
   - Concise step-by-step derivation directly matching Cambridge mark scheme marks (e.g. B1, C1, A1, M1).

4. **Common Student Pitfalls (`common_pitfalls`)**:
   - 2 to 3 real examiner-reported traps (e.g. reading total length instead of extension, missing powers of 10 or unit conversions, sign errors, forgetting square roots or factor of 1/2).

5. **Difficulty & Question Patterns**:
   - `difficulty`: integer 1 to 5.
   - `question_patterns`: array of standard patterns (e.g. ["property_identification"], ["graph_interpretation", "direct_calculation"], ["algebraic_derivation"]).

### JSON Schema:
{
  "question_difficulty": 2,
  "question_patterns": ["..."],
  "parts": [
    {
      "part_id": "part_id_here",
      "difficulty": 1,
      "question_patterns": ["..."],
      "hints": ["Hint 1..."],
      "walkthrough": ["..."],
      "teacher_walkthrough": ["..."],
      "common_pitfalls": ["..."]
    }
  ]
}
"""

def build_question_prompt(qdata):
    lines = []
    lines.append(f"### Question {qdata.get('number', '')}: {qdata.get('title', '')}")
    lines.append(f"**Total Marks**: {qdata.get('marks', '')}")
    lines.append(f"**Stem**:\n{qdata.get('stem', '')}\n")
    
    lines.append("### Question Parts:")
    for p in qdata.get("parts", []):
        pid = p.get("id")
        lbl = p.get("label", "")
        marks = p.get("marks")
        marks_str = f"[{marks} marks]" if marks is not None else "[context / no marks directly]"
        ptext = p.get("text", "").strip()
        lines.append(f"- **Part {lbl}** (id: `{pid}`) {marks_str}:\n  {ptext}\n")
        
    lines.append("### Official Cambridge Mark Scheme:")
    for p in qdata.get("parts", []):
        lbl = p.get("label", "")
        ms = p.get("markscheme", {})
        mps = ms.get("marking_points", [])
        if mps:
            lines.append(f"- **Part {lbl}**:")
            for mp in mps:
                lines.append(f"  * [{mp.get('tag', '')}] {mp.get('text', '')}")
                
    return "\n".join(lines)

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

def process_question(qnum, api_key):
    qfile = QUESTIONS_DIR / f"9702_s23_22_q0{qnum}.json"
    with open(qfile) as f:
        qdata = json.load(f)
        
    qid = qdata.get("id")
    print(f"\n========================================================")
    print(f"Processing Question {qnum} ({qid}) - {qdata.get('marks')} Marks")
    print(f"========================================================")
    
    prompt_text = build_question_prompt(qdata)
    user_content = [{"type": "text", "text": prompt_text}]
    
    # Check for figures
    figures = qdata.get("figures", [])
    q_asset_dir = ASSETS_DIR / qid
    loaded_figs = 0
    for fig in figures:
        fig_file = fig.get("file")
        if fig_file:
            fig_path = q_asset_dir / fig_file
            if fig_path.exists():
                with open(fig_path, "rb") as img_f:
                    b64 = base64.b64encode(img_f.read()).decode()
                    user_content.append({
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{b64}"}
                    })
                    loaded_figs += 1
                    print(f"  Attached figure: {fig_file}")
                    
    print(f"  Payload: Text prompt + {loaded_figs} figure(s)")
    
    req_body = {
        "model": MODEL_ID,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_content}
        ],
        "reasoning": {"effort": "low"},
        "max_tokens": 6000,
        "temperature": 0.2
    }
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://kognitiv.io",
        "X-Title": "Kognitiv Exam Parser"
    }
    
    max_retries = 3
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
                msg = choice["message"]
                raw_content = msg.get("content") or ""
                usage = data.get("usage", {})
                
                prompt_tokens = usage.get("prompt_tokens", 0)
                completion_tokens = usage.get("completion_tokens", 0)
                reasoning_tokens = usage.get("completion_tokens_details", {}).get("reasoning_tokens", 0)
                
                cost = usage.get("cost")
                if cost is None:
                    cost = (prompt_tokens * PRICING_PROMPT) + (completion_tokens * PRICING_COMPL)
                    
                parsed_json = extract_json(raw_content)
                valid_json = parsed_json is not None
                
                # Check for dashes
                em_count = len(re.findall(r"—", raw_content))
                en_count = len(re.findall(r"–", raw_content))
                
                print(f"  SUCCESS in {elapsed:.2f}s | Cost: ${cost:.6f} | Tokens: {prompt_tokens} in, {completion_tokens} out (Reasoning: {reasoning_tokens})")
                print(f"  Valid JSON: {valid_json} | Dash violations: {em_count + en_count}")
                
                result = {
                    "question_id": qid,
                    "question_num": qnum,
                    "title": qdata.get("title"),
                    "marks": qdata.get("marks"),
                    "elapsed_sec": round(elapsed, 2),
                    "tokens": {
                        "prompt_tokens": prompt_tokens,
                        "completion_tokens": completion_tokens,
                        "reasoning_tokens": reasoning_tokens,
                        "total_tokens": prompt_tokens + completion_tokens
                    },
                    "cost_usd": round(cost, 6),
                    "valid_json": valid_json,
                    "dash_violations": em_count + en_count,
                    "parsed_json": parsed_json,
                    "raw_content": raw_content
                }
                
                out_file = OUTPUT_DIR / f"q0{qnum}_enrichment.json"
                with open(out_file, "w", encoding="utf-8") as out_f:
                    json.dump(result, out_f, indent=2, ensure_ascii=False)
                    
                return result
        except Exception as e:
            print(f"  Attempt {attempt+1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(3)
            else:
                return {
                    "question_id": qid,
                    "question_num": qnum,
                    "error": str(e),
                    "cost_usd": 0.0
                }

def main():
    api_key = get_api_key()
    print("================================================================")
    print(f"Enriching Full Paper: Cambridge Physics 9702/22/M/J/23 (8 Questions)")
    print(f"Model: {MODEL_NAME} ({MODEL_ID})")
    print("================================================================")
    
    paper_start = time.time()
    results = []
    total_cost = 0.0
    total_prompt_tokens = 0
    total_completion_tokens = 0
    total_reasoning_tokens = 0
    
    for qnum in range(1, 9):
        res = process_question(qnum, api_key)
        results.append(res)
        cost = res.get("cost_usd", 0.0)
        total_cost += cost
        tokens = res.get("tokens", {})
        total_prompt_tokens += tokens.get("prompt_tokens", 0)
        total_completion_tokens += tokens.get("completion_tokens", 0)
        total_reasoning_tokens += tokens.get("reasoning_tokens", 0)
        time.sleep(1.5)  # Brief pause between questions
        
    paper_elapsed = time.time() - paper_start
    
    summary = {
        "paper": "9702_s23_22",
        "model": MODEL_ID,
        "total_questions": len(results),
        "total_marks": 60,
        "paper_elapsed_sec": round(paper_elapsed, 2),
        "total_cost_usd": round(total_cost, 6),
        "projected_cost_70_papers_usd": round(total_cost * 70, 4),
        "tokens": {
            "total_prompt_tokens": total_prompt_tokens,
            "total_completion_tokens": total_completion_tokens,
            "total_reasoning_tokens": total_reasoning_tokens,
            "grand_total_tokens": total_prompt_tokens + total_completion_tokens
        },
        "questions": results
    }
    
    summary_file = OUTPUT_DIR / "paper_enrichment_summary.json"
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
        
    print("\n================================================================")
    print("PAPER ENRICHMENT COMPLETE!")
    print("================================================================")
    print(f"Total Questions: {len(results)}")
    print(f"Total Time: {paper_elapsed:.2f}s (Average {paper_elapsed/8:.2f}s per question)")
    print(f"Total Prompt Tokens: {total_prompt_tokens:,}")
    print(f"Total Completion Tokens: {total_completion_tokens:,} (Reasoning: {total_reasoning_tokens:,})")
    print(f"TOTAL PAPER COST: ${total_cost:.6f}")
    print(f"PROJECTED COST FOR 70 PAPERS: ${total_cost * 70:.2f}")
    print(f"Summary saved to: {summary_file}")

if __name__ == "__main__":
    main()
