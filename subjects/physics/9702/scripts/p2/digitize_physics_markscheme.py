#!/usr/bin/env python3
"""AI Mark Scheme Digitizer for Cambridge Physics (9702) Past Papers.

Uses Meta Muse Spark (meta/muse-spark-1.3-contributor) via OpenRouter to transcribe
per-question official mark scheme images (`markscheme.png`) verbatim into structured
`markscheme.json` files with criteria tags (B1, M1, A1, C1), mark allocations,
examiner guidance, formula substitutions, and SI units.
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


PHYSICS_MS_SYSTEM_PROMPT = """You are an expert Cambridge International AS & A Level Physics (9702) mark scheme digitizer.
Your goal is to transcribe the provided official Cambridge mark scheme image with 100% verbatim fidelity into a structured JSON object.

OUTPUT JSON SCHEMA:
{
  "schema_version": "1.0",
  "paper_code": "string (e.g. 9702_s24_21)",
  "question_id": "string (e.g. 9702_s24_21_q01)",
  "question_num": int,
  "total_marks": int,
  "parts": [
    {
      "id": "string (e.g. 9702_s24_21_q01_a or 9702_s24_21_q01_b_i)",
      "label": "(a)",
      "marks": int,
      "marking_points": [
        {
          "tag": "B1", // mark code ('B1', 'M1', 'A1', 'C1', 'B2', etc.) or criterion index ('1', '2')
          "text": "verbatim answer criteria text ;", // preserve semicolons (;), alternative answers (/ or 'or'), algebraic working, substitutions
          "guidance": "verbatim examiner guidance" // 'A ...', 'R ...', 'I ...', 'ecf', 'allow 2 or 3 s.f.', 'no mark if unit omitted' or null
        }
      ]
    }
  ]
}

STRICT TRANSCRIPTION RULES:
1. 100% VERBATIM ACCURACY:
   - Transcribe every single formula, substitution, condition, and value exactly as shown in the mark scheme image.
   - NEVER paraphrase, summarize, omit, or re-order criteria.
   - Semicolons (;) indicate distinct marking criteria in Cambridge mark schemes; preserve all semicolons.
   - Slashes (/) and 'or' indicate alternative acceptable values/expressions; preserve them exactly.
2. EXAMINER GUIDANCE & MARK CODES:
   - Cambridge Physics mark categories:
     - 'B' = Independent mark (independent of method).
     - 'M' = Method mark (must be earned before corresponding A mark can score).
     - 'A' = Accuracy mark (correct answer derived from correct physics).
     - 'C' = Compensation mark (correct working toward solution).
   - Guidance column / notes often contain:
     - 'A' = Accept (allowed alternatives)
     - 'R' = Reject (prohibited misconceptions)
     - 'I' = Ignore (neutral statements)
     - 'AW' = Alternative Wording
     - 'ecf' = Error Carried Forward
     - 'allow X or Y s.f.' = significant figure permissions
     - 'max X if ...' = Cap conditions
   - Place all examiner guidance and notes into the 'guidance' field for that marking point.
3. QUESTION & PART HIERARCHY:
   - Identify every subpart: e.g. '(a)', '(b)(i)', '(b)(ii)', '(c)', '(d)(i)', etc.
   - Part 'id' format: '{paper_code}_q{question_num:02d}_{clean_label}' (e.g. for (b)(i) -> 'b_i').
4. MARKS RECONCILIATION:
   - Each subpart must record its exact integer mark from the 'Marks' column.
   - 'total_marks' MUST strictly equal the sum of all parts' marks.
5. MATH & SI UNITS:
   - Use KaTeX for mathematical expressions, formulas ($v = u + at$), powers of 10 ($10^{-4}$), and units ($\\text{m s}^{-1}$, $\\text{kg m s}^{-2}$, $\\text{N m}$, $\\text{J}$).
6. FORMAT:
   - Output strictly valid JSON with no markdown wrapping.
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


def call_openrouter_ms(
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
                print(f"    [ERROR] MS OCR call failed: {e}", file=sys.stderr)
                return None, 0, 0
            time.sleep(2 ** attempt)

    return None, 0, 0


def digitize_single_ms(
    q_dir: Path,
    paper_code: str,
    q_num: int,
    api_key: str,
    force: bool = False,
) -> dict:
    ms_json = q_dir / "markscheme.json"
    ms_meta = q_dir / "markscheme_meta.json"

    if ms_json.is_file() and not force:
        return {"status": "SKIPPED", "question": q_dir.name, "cost": 0.0, "tokens": 0}

    ms_img = q_dir / "markscheme.png"
    if not ms_img.is_file():
        return {"status": "ERROR", "question": q_dir.name, "message": "markscheme.png missing"}

    t0 = time.time()
    user_prompt = f"Digitize this Cambridge Physics 9702 mark scheme table for {q_dir.name} (Paper: {paper_code}) verbatim."
    data, p_toks, c_toks = call_openrouter_ms(
        ms_img,
        PHYSICS_MS_SYSTEM_PROMPT,
        user_prompt,
        api_key,
    )

    if not data:
        return {"status": "ERROR", "question": q_dir.name, "message": "Failed to parse MS JSON"}

    data["schema_version"] = "1.0"
    data["paper_code"] = paper_code
    data["question_id"] = f"{paper_code}_q{q_num:02d}"
    data["question_num"] = q_num

    # Recalculate total marks from parts if missing or mismatched
    parts = data.get("parts", [])
    part_sum = sum(p.get("marks", 0) for p in parts)
    if part_sum > 0:
        data["total_marks"] = part_sum

    ms_json.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

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
    ms_meta.write_text(json.dumps(meta, indent=2), encoding="utf-8")

    return {
        "status": "SUCCESS",
        "question": q_dir.name,
        "total_marks": data.get("total_marks", 0),
        "parts_count": len(parts),
        "cost": cost,
        "tokens": p_toks + c_toks,
        "elapsed": elapsed,
    }


def process_paper_markschemes(
    paper_query: str,
    question_filter: int | None = None,
    force: bool = False,
    max_workers: int = 6,
) -> dict:
    from check_p2_extraction import find_p2_paper_dir
    code, variant_dir = find_p2_paper_dir(paper_query)
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
            pool.submit(digitize_single_ms, qd, code, int(qd.name.split("_")[-1]), api_key, force=force): qd
            for qd in q_dirs
        }
        for future in as_completed(future_to_qd):
            res = future.result()
            results.append(res)
            total_cost += res.get("cost", 0.0)
            total_tokens += res.get("tokens", 0)

    paper_mark_sum = sum(r.get("total_marks", 0) for r in results)
    elapsed = round(time.time() - t0, 2)

    return {
        "paper_code": code,
        "questions_processed": len(results),
        "paper_total_marks": paper_mark_sum,
        "total_cost_usd": total_cost,
        "total_tokens": total_tokens,
        "total_elapsed_sec": elapsed,
        "results": results,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Digitize Physics P2 Mark Schemes via Meta Muse Spark")
    parser.add_argument("paper", help="Paper query or directory")
    parser.add_argument("--question", type=int, help="Optional specific question")
    parser.add_argument("--force", action="store_true", help="Force re-digitization")
    parser.add_argument("--max-workers", type=int, default=6, help="Worker threads")
    args = parser.parse_args()

    res = process_paper_markschemes(args.paper, question_filter=args.question, force=args.force, max_workers=args.max_workers)
    print(f"Done: {res['questions_processed']} mark schemes digitized | Total Marks: {res['paper_total_marks']} | Cost: ${res['total_cost_usd']:.5f}")


if __name__ == "__main__":
    main()
