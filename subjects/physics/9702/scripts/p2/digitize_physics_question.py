#!/usr/bin/env python3
"""AI Question OCR Digitizer for Cambridge Physics (9702) Past Papers.

Uses Meta Muse Spark (meta/muse-spark-1.3-contributor) via OpenRouter to transcribe
per-question official question images (`question_compact.png` / `question_printable.png`)
verbatim into structured `question_ocr.json` files with KaTeX physical formulas,
display equations, subpart hierarchies, answer prompts/units, and figure tokens.
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
from audit_physics_ocr_structure import audit_question_structure

REPO_ROOT = next(
    (p for p in Path(__file__).resolve().parents if (p / "subjects").is_dir() and (p / "pyproject.toml").is_file()),
    Path(__file__).resolve().parents[3],
)
PHYSICS_PAPERS_ROOT = REPO_ROOT / "subjects/physics/9702/past papers"

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


PHYSICS_QUESTION_OCR_SYSTEM_PROMPT = """You are an expert Cambridge International AS & A Level Physics (9702) past paper question digitizer.
Your goal is to transcribe the provided official Cambridge question image with 100% verbatim fidelity into a structured JSON object.

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
      "answer_prompt": "Verbatim prompt printed immediately before the dotted answer line (e.g. 'speed =', 'resultant moment =', 'SI base units', 'ratio =') or null",
      "unit": "Verbatim unit printed at the end of the dotted answer line (e.g. '\\text{m s}^{-1}', '\\text{N m}', '\\text{kg m s}^{-2}', '\\text{J}', '%') or null"
    }
  ],
  "figures_referenced": ["string of figure ids referenced in the text"]
}

STRICT PHYSICS & FORMATTING RULES:
1. Verbatim Accuracy: Transcribe every word, variable, condition, exponent, and label verbatim. Never paraphrase or alter text.
2. Physical Formulas & KaTeX Formatting:
   - Physical quantities and symbols in math italics: $v$, $u$, $a$, $t$, $s$, $m$, $F$, $\\rho$, $\\lambda$, $\\theta$, $\\omega$, $I$, $V$, $R$, $p_1$, $p_2$.
   - Display equations: standalone formulas on their own line in `$$...$$` (e.g. $$v^2 = u^2 + 2as$$, $$p = \\rho g h$$, $$F = \\frac{G M m}{r^2}$$).
   - SI base units and derived units in upright text font inside math: $\\text{kg m s}^{-2}$, $\\text{N m}$, $\\text{W m}^{-2}$, $\\text{m s}^{-1}$, $\\text{m s}^{-2}$, $\\text{J}$, $\\text{Pa}$, $\\text{V}$, $\\text{A}$, $\\Omega$.
   - Never use raw Unicode dashes like \u2014 or \u2013. Always use standard ASCII hyphens (-).
3. Question Hierarchy & Elimination of Duplicate Stems:
   - Setup text before any (a)/(b) in `question_stem`.
   - When introductory text, problem descriptions, or diagrams precede child subparts (e.g. text before (i) and (ii)), place it in `part_stem`. Never duplicate identical text across multiple parts!
   - For subparts with Roman numerals (e.g. (a)(i), (a)(ii)), label accurately as "(a)(i)" and "(a)(ii)".
4. Diagram, Circuit & Figure Tokens:
   - When a diagram, graph, oscilloscope trace, or circuit is referenced (e.g. "Fig. 1.1", "Fig. 2.1"), insert the figure token `{{figure:figure_X_Y}}` on its own line right where it appears in the text.
   - List every referenced figure ID in `figures_referenced`.
5. Answer Prompts & Units:
   - Capture what is printed before the dotted answer space in `answer_prompt`.
   - Capture what is printed after the dotted answer space in `unit`.
   - Strip all dotted answer lines (.......) completely.
6. Output strictly valid JSON without Markdown fences or extra commentary.
"""

PHYSICS_QUESTION_REPAIR_SYSTEM_PROMPT = """You are an expert Cambridge International AS & A Level Physics (9702) Exam Verification & Layout Editor.
Your job is to inspect the official Cambridge examination question image, review the draft OCR JSON, and correct all structural, visual, KaTeX, and formula formatting defects.

EXACT EXAM STRUCTURE & LAYOUT RULES:
1. Verbatim Fidelity & Chronological Flow:
   - Elements must appear in the exact visual order of the printed exam paper.
   - No dropped words, questions, or context.
2. Physical Formulas & Math:
   - Variables italicized ($m$, $v$, $F$), units upright ($\\text{m s}^{-1}$, $\\text{N}$).
   - Balanced math delimiters ($...$, $$...$$, {...}).
   - Zero em dashes (\u2014) or en dashes (\u2013). Use standard ASCII hyphens (-).
3. Diagrams & Graphs:
   - Ensure every `Fig. X.Y` has an anchor token `{{figure:figure_X_Y}}` on its own line.
4. Answer Prompts:
   - Capture prefix in `answer_prompt` and suffix in `unit`. Omit dotted lines.

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


def call_openrouter_ocr(
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
                print(f"    [ERROR] OpenRouter call failed: {e}", file=sys.stderr)
                return None, 0, 0
            time.sleep(2 ** attempt)

    return None, 0, 0


def get_paper_code(q_dir: Path) -> str:
    paper_dir = q_dir.parent
    source_dir = paper_dir / "source"
    if source_dir.is_dir():
        for f in source_dir.glob("*.pdf"):
            m = re.match(r"^(\d{4})_([msw]\d{2})_(?:qp|ms)_(\d{2})", f.name)
            if m:
                return f"{m.group(1)}_{m.group(2)}_{m.group(3)}"
    session_map = {"may-june": "s", "feb-march": "m", "oct-nov": "w"}
    session = session_map.get(paper_dir.parent.name.lower(), "s")
    year = paper_dir.parent.parent.name[-2:]
    variant = paper_dir.name.split("-")[-1]
    return f"9702_{session}{year}_2{variant}"


def digitize_single_question(
    q_dir: Path,
    api_key: str,
    force: bool = False,
    repair: bool = True,
) -> dict:
    ocr_file = q_dir / "question_ocr.json"
    meta_file = q_dir / "question_ocr_meta.json"

    if ocr_file.is_file() and not force:
        return {"status": "SKIPPED", "question": q_dir.name, "cost": 0.0, "tokens": 0}

    img_path = q_dir / "question_compact.png"
    if not img_path.is_file():
        img_path = q_dir / "question_printable.png"
    if not img_path.is_file():
        return {"status": "ERROR", "question": q_dir.name, "message": "No question image found"}

    t0 = time.time()
    user_prompt = f"Digitize this Cambridge Physics 9702 question from {q_dir.name} with 100% verbatim accuracy."
    data, p_toks, c_toks = call_openrouter_ocr(
        img_path,
        PHYSICS_QUESTION_OCR_SYSTEM_PROMPT,
        user_prompt,
        api_key,
    )

    if not data:
        return {"status": "ERROR", "question": q_dir.name, "message": "Failed to parse OCR JSON"}

    code = get_paper_code(q_dir)
    q_num = int(q_dir.name.split("_")[-1])
    data["paper_code"] = code
    data["question_id"] = f"{code}_q{q_num:02d}"
    data["question_num"] = q_num
    for part in data.get("parts", []):
        raw_label = part.get("label") or ""
        part_label = raw_label.replace("(", "").replace(")", "").replace(" ", "_").strip("_")
        if part_label:
            part["id"] = f"{code}_q{q_num:02d}_{part_label}"
        else:
            part["id"] = f"{code}_q{q_num:02d}"

    ocr_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    issues = audit_question_structure(q_dir)
    errors = [i for i in issues if i["level"] == "ERROR"]

    if errors and repair:
        err_descriptions = "\n".join([f"- {e['category']}: {e['message']}" for e in errors])
        repair_user_prompt = (
            f"Review and repair the following OCR JSON for {q_dir.name} based on the original image.\n"
            f"Errors identified to fix:\n{err_descriptions}\n\n"
            f"Current Draft JSON:\n{json.dumps(data, indent=2, ensure_ascii=False)}"
        )
        repaired_data, r_ptoks, r_ctoks = call_openrouter_ocr(
            img_path,
            PHYSICS_QUESTION_REPAIR_SYSTEM_PROMPT,
            repair_user_prompt,
            api_key,
        )
        if repaired_data:
            data = repaired_data
            data["paper_code"] = code
            data["question_id"] = f"{code}_q{q_num:02d}"
            data["question_num"] = q_num
            for part in data.get("parts", []):
                raw_label = part.get("label") or ""
                part_label = raw_label.replace("(", "").replace(")", "").replace(" ", "_").strip("_")
                if part_label:
                    part["id"] = f"{code}_q{q_num:02d}_{part_label}"
                else:
                    part["id"] = f"{code}_q{q_num:02d}"
            p_toks += r_ptoks
            c_toks += r_ctoks
            ocr_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    cost = (p_toks * PRICING_PROMPT) + (c_toks * PRICING_COMPL)
    elapsed = round(time.time() - t0, 2)

    meta = {
        "model": MODEL_ID,
        "prompt_tokens": p_toks,
        "completion_tokens": c_toks,
        "cost_usd": cost,
        "elapsed_sec": elapsed,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
    }
    meta_file.write_text(json.dumps(meta, indent=2), encoding="utf-8")

    return {
        "status": "SUCCESS",
        "question": q_dir.name,
        "cost": cost,
        "tokens": p_toks + c_toks,
        "elapsed": elapsed,
    }


def process_paper(
    paper_dir: Path,
    api_key: str | None = None,
    force: bool = False,
    repair: bool = True,
    max_workers: int = 6,
) -> dict:
    if not api_key:
        api_key = get_api_key()

    q_dirs = sorted([d for d in paper_dir.iterdir() if d.is_dir() and d.name.startswith("question_")])
    results = []
    total_cost = 0.0
    total_tokens = 0

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        future_to_qd = {
            pool.submit(digitize_single_question, qd, api_key, force=force, repair=repair): qd
            for qd in q_dirs
        }
        for future in as_completed(future_to_qd):
            res = future.result()
            results.append(res)
            total_cost += res.get("cost", 0.0)
            total_tokens += res.get("tokens", 0)

    return {
        "questions_digitized": len(results),
        "total_cost": total_cost,
        "total_tokens": total_tokens,
        "results": results,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Digitize Physics P2 questions via Meta Muse Spark")
    parser.add_argument("paper", help="Paper directory or code (e.g. 9702_s24_21)")
    parser.add_argument("--force", action="store_true", help="Force re-digitization")
    parser.add_argument("--no-repair", action="store_true", help="Disable auto-repair pass")
    parser.add_argument("--max-workers", type=int, default=6, help="Parallel worker threads")
    args = parser.parse_args()

    from check_p2_extraction import find_p2_paper_dir
    code, variant_dir = find_p2_paper_dir(args.paper)
    api_key = get_api_key()

    print(f"Digitizing Physics P2: {code} ({variant_dir}) with {args.max_workers} workers...")
    res = process_paper(
        variant_dir,
        api_key=api_key,
        force=args.force,
        repair=not args.no_repair,
        max_workers=args.max_workers,
    )
    print(f"Done: {res['questions_digitized']} questions digitized | Cost: ${res['total_cost']:.5f} | Tokens: {res['total_tokens']}")


if __name__ == "__main__":
    main()
