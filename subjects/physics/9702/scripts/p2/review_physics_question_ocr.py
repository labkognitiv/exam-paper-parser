#!/usr/bin/env python3
"""Mandatory Multimodal AI Question OCR Review & Polish Pass for Cambridge Physics (9702).

Performs a rigorous secondary quality audit of digitized question_ocr.json against the
original Cambridge question image using Meta Muse Spark.

Mandatory Review Checks:
1. Verbatim Content Fidelity:
   - Verifies every word, variable, exponent, condition, number, and unit against the printed page.
   - Detects and restores any dropped words, subparts, or introductory context.
2. Mathematical & Physical Formula Formatting:
   - Enforces KaTeX math blocks: $v^2 = u^2 + 2as$, $F = ma$, $\\text{kg m s}^{-2}$, $\\text{N m}$, $\\text{W m}^{-2}$.
   - Cleans all typographical em dashes and en dashes to standard ASCII hyphens (-).
3. Visual Layout & Chronological Hierarchy:
   - Elements appear in the exact visual sequence of the printed exam paper.
   - Shared introductory text is placed in 'part_stem', overarching narratives in 'question_stem'.
4. Diagram & Figure Token Placements:
   - Verifies referenced diagrams/circuits/graphs have {{figure:figure_X_Y}} tokens placed on their own lines.
5. Answer Prompts & Units:
   - Captures printed prefix in 'answer_prompt' (e.g. 'speed =', 'resultant moment =', 'SI base units').
   - Captures printed suffix in 'unit' (e.g. '\\text{m s}^{-1}', '\\text{N m}', '%').
   - Verifies printed answer line dot strings (.... or ____) are completely purged from prompts.
"""

from __future__ import annotations

import argparse
import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import re
import subprocess
import sys
import time
import urllib.request

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

REPO_ROOT = next(
    (p for p in Path(__file__).resolve().parents if (p / "subjects").is_dir() and (p / "pyproject.toml").is_file()),
    Path(__file__).resolve().parents[3],
)
PHYSICS_PAPERS_ROOT = REPO_ROOT / "subjects/physics/9702/past papers"

from audit_physics_ocr_structure import audit_question_structure

MODEL_ID = "meta/muse-spark-1.3-contributor"
PRICING_PROMPT = 0.10 / 1_000_000
PRICING_COMPL = 0.20 / 1_000_000


def get_api_key() -> str:
    """Retrieve OpenRouter API key from macOS Keychain."""
    cmd = ["security", "find-generic-password", "-s", "kognitiv-openrouter-api-key", "-w"]
    try:
        return subprocess.check_output(cmd).decode("utf-8").strip()
    except Exception as exc:
        raise RuntimeError(f"Failed to retrieve OpenRouter API key from Keychain: {exc}")


PHYSICS_QUESTION_REVIEW_SYSTEM_PROMPT = """You are a senior Cambridge International AS & A Level Physics (9702) Exam Verification Auditor.
Your job is to perform a meticulous side-by-side quality audit of the digitized question JSON against the official Cambridge exam page image.
You must return the polished, corrected, complete JSON object.

OUTPUT JSON SCHEMA:
{
  "schema_version": "1.0",
  "paper_code": "string (e.g. 9702_s24_21)",
  "question_id": "string (e.g. 9702_s24_21_q01)",
  "question_num": int,
  "total_marks": int,
  "question_stem": "Introductory scenario text / background narrative printed before any subparts. If the question has no subparts, place the entire problem text here. Math, formulas, and physical units strictly in $...$ or $$...$$. Insert {{figure:fig_id}} where diagrams appear.",
  "parts": [
    {
      "id": "string (e.g. 9702_s24_21_q01_a or 9702_s24_21_q01_b_i)",
      "label": "(a)", // "(a)", "(b)", "(b)(i)", or null if single whole question without subparts
      "part_stem": "Introductory text shared across child subparts (e.g. text printed before (i) and (ii)), or null",
      "text": "The prompt text for this subpart. All variables, units, equations, and math strictly in KaTeX $...$ or $$...$$.",
      "marks": int, // mark allocation in brackets [1], [2], etc.
      "answer_prompt": "Verbatim prompt printed immediately before the dotted answer line (e.g. 'speed =', 'resultant moment =', 'ratio =') or null",
      "unit": "Verbatim unit printed at the end of the dotted answer line (e.g. '\\text{m s}^{-1}', '\\text{N m}', '\\text{kg m s}^{-2}', '\\text{J}', '%') or null"
    }
  ],
  "figures_referenced": ["string of figure ids referenced in the text"]
}

STRICT PHYSICS REVIEW & POLISH RULES:
1. Verbatim Content Fidelity:
   - Transcribe every single word, variable, condition, exponent, and value verbatim. Never paraphrase or summarize.
   - Detect and restore any dropped introductory text, question parts, or setup context.
2. Mathematical & Physical Notation in KaTeX:
   - Variables italicized: $v$, $u$, $a$, $t$, $s$, $m$, $F$, $\\rho$, $\\lambda$, $\\theta$, $\\omega$, $I$, $V$, $R$.
   - Display equations: $$v^2 = u^2 + 2as$$, $$p = \\rho g h$$, $$E_{\\text{k}} = \\frac{1}{2}mv^2$$.
   - SI base units and derived units in upright text font: $\\text{kg m s}^{-2}$, $\\text{N m}$, $\\text{W m}^{-2}$, $\\text{m s}^{-1}$, $\\text{J}$, $\\text{Pa}$, $\\text{V}$, $\\text{A}$.
   - Invariant: ZERO em dashes (\u2014) and ZERO en dashes (\u2013). Use standard ASCII hyphens (-).
3. Question Hierarchy & Elimination of Duplicate Stems:
   - Narrative text printed before any subpart letter belongs in `question_stem`.
   - When introductory text, problem descriptions, or diagrams precede child subparts (e.g. text before (i) and (ii)), place it in `part_stem`. Never duplicate identical text across multiple parts!
4. Diagram & Graph Tokens:
   - When a diagram, graph, oscilloscope trace, or circuit is printed (e.g. "Fig. 1.1", "Fig. 2.1"), insert `{{figure:figure_X_Y}}` on its own line where it appears visually.
   - Also list every referenced figure ID in `figures_referenced`.
5. Answer Prompts & Units:
   - Capture what is printed before the dotted answer space in `answer_prompt`.
   - Capture what is printed after the dotted answer space in `unit`.
   - Strip all dotted answer lines (.......) completely.

Output strictly valid JSON matching the schema without markdown fences or extra commentary.
"""


def extract_json(raw_text: str) -> dict | None:
    if not raw_text:
        return None
    cleaned = raw_text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*\n?", "", cleaned)
        cleaned = re.sub(r"\n?```\s*$", "", cleaned)
        cleaned = cleaned.strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        m = re.search(r"(\{.*\})", cleaned, re.DOTALL)
        if m:
            try:
                return json.loads(m.group(1))
            except json.JSONDecodeError:
                pass
    return None


def call_openrouter_review(
    image_path: Path,
    system_prompt: str,
    user_prompt: str,
    api_key: str,
    model: str = MODEL_ID,
    max_tokens: int = 6500,
    temperature: float = 0.1,
    retry_count: int = 3,
) -> tuple[dict | None, int, int]:
    img_bytes = image_path.read_bytes()
    b64_img = base64.b64encode(img_bytes).decode("utf-8")
    ext = image_path.suffix.lstrip(".").lower() or "png"
    mime = f"image/{ext}" if ext != "jpg" else "image/jpeg"

    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": user_prompt},
                {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64_img}"}},
            ],
        },
    ]

    payload = {
        "model": model,
        "messages": messages,
        "reasoning": {"effort": "low"},
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://kognitiv.edu",
        "X-Title": "Kognitiv Exam Pipeline",
    }

    for attempt in range(retry_count):
        try:
            req = urllib.request.Request(
                "https://openrouter.ai/api/v1/chat/completions",
                data=json.dumps(payload).encode("utf-8"),
                headers=headers,
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                resp_data = json.loads(resp.read().decode("utf-8"))
                choice = resp_data["choices"][0]["message"].get("content") or ""
                usage = resp_data.get("usage", {})
                p_toks = usage.get("prompt_tokens", 0)
                c_toks = usage.get("completion_tokens", 0)
                parsed = extract_json(choice)
                return parsed, p_toks, c_toks
        except Exception as e:
            if attempt == retry_count - 1:
                print(f"    [ERROR] OpenRouter review call failed: {e}", file=sys.stderr)
                return None, 0, 0
            time.sleep(2 ** attempt)

    return None, 0, 0


def review_single_question_ocr(
    q_dir: Path,
    paper_code: str,
    api_key: str,
    force: bool = False,
) -> dict:
    ocr_file = q_dir / "question_ocr.json"
    review_meta_file = q_dir / "question_ocr_review_meta.json"

    if not ocr_file.is_file():
        return {"status": "ERROR", "question": q_dir.name, "message": "question_ocr.json missing"}

    if review_meta_file.is_file() and not force:
        return {"status": "SKIPPED", "question": q_dir.name, "cost": 0.0, "tokens": 0}

    img_path = q_dir / "question_compact.png"
    if not img_path.is_file():
        img_path = q_dir / "question_printable.png"
    if not img_path.is_file():
        return {"status": "ERROR", "question": q_dir.name, "message": "No question image found"}

    draft_data = json.loads(ocr_file.read_text(encoding="utf-8"))

    user_prompt = (
        f"Perform mandatory review of this Cambridge Physics 9702 question ({q_dir.name}).\n"
        f"Side-by-side audit against original image and return polished, 100% accurate JSON.\n\n"
        f"Current Draft JSON:\n{json.dumps(draft_data, indent=2, ensure_ascii=False)}"
    )

    t0 = time.time()
    reviewed_data, p_toks, c_toks = call_openrouter_review(
        img_path,
        PHYSICS_QUESTION_REVIEW_SYSTEM_PROMPT,
        user_prompt,
        api_key,
    )

    if not reviewed_data:
        return {"status": "ERROR", "question": q_dir.name, "message": "Failed to parse reviewed JSON"}

    reviewed_data["paper_code"] = paper_code
    q_num = int(q_dir.name.split("_")[-1])
    reviewed_data["question_id"] = f"{paper_code}_q{q_num:02d}"
    reviewed_data["question_num"] = q_num
    for part in reviewed_data.get("parts", []):
        raw_label = part.get("label") or ""
        part_label = raw_label.replace("(", "").replace(")", "").replace(" ", "_").strip("_")
        if part_label:
            part["id"] = f"{paper_code}_q{q_num:02d}_{part_label}"
        else:
            part["id"] = f"{paper_code}_q{q_num:02d}"

    ocr_file.write_text(json.dumps(reviewed_data, indent=2, ensure_ascii=False), encoding="utf-8")

    cost = (p_toks * PRICING_PROMPT) + (c_toks * PRICING_COMPL)
    elapsed = round(time.time() - t0, 2)

    meta = {
        "model": MODEL_ID,
        "prompt_tokens": p_toks,
        "completion_tokens": c_toks,
        "cost_usd": cost,
        "elapsed_sec": elapsed,
        "status": "REVIEWED_AND_POLISHED",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
    }
    review_meta_file.write_text(json.dumps(meta, indent=2), encoding="utf-8")

    return {
        "status": "SUCCESS",
        "question": q_dir.name,
        "cost": cost,
        "tokens": p_toks + c_toks,
        "elapsed": elapsed,
    }


def process_paper_ocr_review(
    variant_dir: Path,
    paper_code: str,
    question_filter: int | None = None,
    force: bool = False,
    max_workers: int = 6,
) -> dict:
    api_key = get_api_key()
    q_dirs = sorted([d for d in variant_dir.iterdir() if d.is_dir() and d.name.startswith("question_")])

    if question_filter is not None:
        q_dirs = [d for d in q_dirs if int(d.name.split("_")[-1]) == question_filter]

    results = []
    total_cost = 0.0
    total_tokens = 0
    t0 = time.time()

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        future_to_qd = {
            pool.submit(review_single_question_ocr, qd, paper_code, api_key, force=force): qd
            for qd in q_dirs
        }
        for future in as_completed(future_to_qd):
            res = future.result()
            results.append(res)
            total_cost += res.get("cost", 0.0)
            total_tokens += res.get("tokens", 0)

    elapsed = round(time.time() - t0, 2)
    return {
        "questions_reviewed": len(results),
        "total_cost_usd": total_cost,
        "total_tokens": total_tokens,
        "elapsed_sec": elapsed,
        "results": results,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Mandatory Physics Question OCR Review")
    parser.add_argument("paper", help="Paper query or path (e.g. 9702_s24_21)")
    parser.add_argument("--question", type=int, help="Optional question number")
    parser.add_argument("--force", action="store_true", help="Force re-review")
    parser.add_argument("--max-workers", type=int, default=6, help="Parallel workers")
    args = parser.parse_args()

    from check_p2_extraction import find_p2_paper_dir
    code, variant_dir = find_p2_paper_dir(args.paper)

    print(f"Running Mandatory OCR Review for Physics P2: {code} ({variant_dir})...")
    res = process_paper_ocr_review(
        variant_dir,
        paper_code=code,
        question_filter=args.question,
        force=args.force,
        max_workers=args.max_workers,
    )
    print(f"Done: {res['questions_reviewed']} reviewed in {res['elapsed_sec']}s | Cost: ${res['total_cost_usd']:.5f} | Tokens: {res['total_tokens']}")


if __name__ == "__main__":
    main()
