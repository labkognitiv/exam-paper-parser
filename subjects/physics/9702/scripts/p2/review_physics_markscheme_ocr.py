#!/usr/bin/env python3
"""Source-grounded second pass for Physics P2 mark-scheme OCR.

The first Muse transcription is reviewed against the same official mark-scheme
image.  The reviewer receives its complete draft plus deterministic part-mark
reconciliation errors derived from the immutable canonical mark scheme.  A
candidate is promoted only when its ordered part allocation exactly reconciles.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import re
import sys
import time

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from check_p2_extraction import find_p2_paper_dir
from digitize_physics_markscheme import (
    MODEL_ID,
    PRICING_COMPL,
    PRICING_PROMPT,
    call_openrouter_ms,
    get_api_key,
)


PHYSICS_MS_REVIEW_SYSTEM_PROMPT = """You are a senior Cambridge International AS & A Level Physics (9702) mark-scheme verification auditor.
Review the original official mark-scheme image beside the first-pass JSON. Return one complete corrected JSON object using the first-pass schema.

Rules:
1. Transcribe the image verbatim. Never invent material that is not visible.
2. Preserve every visible mark criterion, formula, alternative, mark code, and examiner guidance in the printed order.
3. The supplied canonical allocation is a deterministic cross-check for the visible printed parts. Return every listed part in that exact order with its required integer mark.
4. `total_marks` must equal the sum of `parts[].marks`.
5. Return strictly valid JSON only, with no markdown or commentary.
"""


def normalise_label(label: object) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(label or "").lower())


def canonical_marks(q_dir: Path) -> tuple[int, list[tuple[str, int]]]:
    q_num = int(q_dir.name.rsplit("_", 1)[1])
    canonical = q_dir.parent / "mark-schemes" / f"markscheme_{q_num:02d}.json"
    if not canonical.is_file():
        raise FileNotFoundError(f"Canonical mark scheme missing: {canonical}")
    data = json.loads(canonical.read_text(encoding="utf-8"))
    parts = data.get("parts")
    if not isinstance(parts, list):
        raise ValueError(f"Canonical mark scheme has no parts list: {canonical}")
    expected = []
    for part in parts:
        marks = part.get("marks")
        if not isinstance(marks, int):
            raise ValueError(f"Canonical non-integer mark in {canonical}: {part.get('label')}")
        expected.append((normalise_label(part.get("label")), marks))
    total = data.get("total_marks")
    if not isinstance(total, int):
        raise ValueError(f"Canonical total is not an integer: {canonical}")
    return total, expected


def draft_marks(data: dict) -> tuple[int | None, list[tuple[str, int | None]]]:
    parts = data.get("parts")
    if not isinstance(parts, list):
        return None, []
    parsed = [(normalise_label(part.get("label")), part.get("marks") if isinstance(part.get("marks"), int) else None) for part in parts if isinstance(part, dict)]
    total = data.get("total_marks") if isinstance(data.get("total_marks"), int) else None
    return total, parsed


def reconciliation_errors(data: dict, expected_total: int, expected_parts: list[tuple[str, int]]) -> list[str]:
    actual_total, actual_parts = draft_marks(data)
    errors = []
    if actual_total != expected_total:
        errors.append(f"total_marks expected {expected_total}, received {actual_total}")
    actual_sum = sum(mark for _, mark in actual_parts if isinstance(mark, int))
    if len(actual_parts) != len(expected_parts):
        errors.append(f"part count expected {len(expected_parts)}, received {len(actual_parts)}")
    if actual_parts != expected_parts:
        errors.append(f"ordered part allocation expected {expected_parts}, received {actual_parts}")
    if actual_sum != expected_total:
        errors.append(f"part mark sum expected {expected_total}, received {actual_sum}")
    return errors


def repair_identity(data: dict, paper_code: str, q_num: int, q_dir: Path | None = None) -> None:
    data["schema_version"] = "1.0"
    data["paper_code"] = paper_code
    data["question_id"] = f"{paper_code}_q{q_num:02d}"
    data["question_num"] = q_num

    canonical_parts = None
    if q_dir:
        canonical_path = q_dir.parent / "mark-schemes" / f"markscheme_{q_num:02d}.json"
        if canonical_path.is_file():
            try:
                c_data = json.loads(canonical_path.read_text(encoding="utf-8"))
                canonical_parts = c_data.get("parts", [])
            except Exception:
                pass

    actual_parts = [p for p in data.get("parts", []) if isinstance(p, dict)]
    if canonical_parts and len(actual_parts) == len(canonical_parts):
        for part, c_part in zip(actual_parts, canonical_parts):
            if isinstance(c_part, dict) and c_part.get("id"):
                part["id"] = c_part["id"]
                if c_part.get("label"):
                    part["label"] = c_part["label"]
        return

    for part in actual_parts:
        clean_label = re.sub(r"[^a-z0-9]+", "_", str(part.get("label") or "").lower()).strip("_")
        if clean_label and clean_label != str(q_num):
            part["id"] = f"{paper_code}_q{q_num:02d}_{clean_label}"
        else:
            part["id"] = f"{paper_code}_q{q_num:02d}"


def review_single_markscheme(q_dir: Path, paper_code: str, api_key: str, force: bool = False) -> dict:
    draft_file = q_dir / "markscheme.json"
    review_meta_file = q_dir / "markscheme_review_meta.json"
    candidate_file = q_dir / "markscheme_review_candidate.json"
    image_file = q_dir / "markscheme.png"

    if not draft_file.is_file():
        return {"status": "ERROR", "question": q_dir.name, "message": "markscheme.json missing"}
    if review_meta_file.is_file() and not force:
        try:
            meta = json.loads(review_meta_file.read_text(encoding="utf-8"))
            if meta.get("status") == "PASS":
                return {"status": "SUCCESS", "question": q_dir.name, "cached": True}
        except Exception:
            pass
    if not image_file.is_file():
        return {"status": "ERROR", "question": q_dir.name, "message": "markscheme.png missing"}

    try:
        expected_total, expected_parts = canonical_marks(q_dir)
    except Exception as exc:
        return {"status": "ERROR", "question": q_dir.name, "message": f"Canonical marks failed: {exc}"}

    try:
        draft = json.loads(draft_file.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"status": "ERROR", "question": q_dir.name, "message": f"Draft JSON unreadable: {exc}"}

    pre_errors = reconciliation_errors(draft, expected_total, expected_parts)
    if not pre_errors:
        repair_identity(draft, paper_code, q_num=int(q_dir.name.rsplit("_", 1)[1]), q_dir=q_dir)
        draft_file.write_text(json.dumps(draft, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        meta = {
            "model": "deterministic-precheck",
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "cost_usd": 0.0,
            "elapsed_sec": 0.0,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
            "status": "PASS",
            "pre_reconciliation_errors": [],
            "post_reconciliation_errors": [],
        }
        review_meta_file.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
        return {"status": "SUCCESS", "question": q_dir.name, "cost": 0.0, "tokens": 0}

    q_num = int(q_dir.name.rsplit("_", 1)[1])
    prompt = (
        f"Correct the digitised mark scheme JSON for {paper_code} Question {q_num}.\n"
        "The image is the official source. The canonical allocation below is a deterministic reconciliation check, not replacement source text.\n\n"
        f"Deterministic reconciliation errors in first pass:\n{json.dumps(pre_errors, indent=2)}\n\n"
        f"Required total and ordered part allocations:\n{json.dumps(expected_parts)}; total={expected_total}\n\n"
        f"First-pass JSON to correct:\n{json.dumps(draft, indent=2, ensure_ascii=False)}"
    )
    t0 = time.time()
    reviewed, p_toks, c_toks = call_openrouter_ms(
        image_file, PHYSICS_MS_REVIEW_SYSTEM_PROMPT, prompt, api_key, max_tokens=6500, temperature=0.1
    )
    if not reviewed:
        return {"status": "ERROR", "question": q_dir.name, "message": "Failed to parse review JSON"}

    repair_identity(reviewed, paper_code, q_num, q_dir=q_dir)
    post_errors = reconciliation_errors(reviewed, expected_total, expected_parts)
    cost = (p_toks * PRICING_PROMPT) + (c_toks * PRICING_COMPL)
    meta = {
        "model": MODEL_ID,
        "prompt_tokens": p_toks,
        "completion_tokens": c_toks,
        "cost_usd": cost,
        "elapsed_sec": round(time.time() - t0, 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "status": "PASS" if not post_errors else "FAIL",
        "pre_reconciliation_errors": pre_errors,
        "post_reconciliation_errors": post_errors,
    }
    review_meta_file.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    if post_errors:
        candidate_file.write_text(json.dumps(reviewed, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return {"status": "FAIL", "question": q_dir.name, "message": "; ".join(post_errors), "cost": cost, "tokens": p_toks + c_toks}

    draft_file.write_text(json.dumps(reviewed, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {"status": "SUCCESS", "question": q_dir.name, "cost": cost, "tokens": p_toks + c_toks}


def process_paper_markscheme_review(
    paper_query: str,
    question_filter: int | None = None,
    force: bool = False,
    max_workers: int = 6,
) -> dict:
    code, variant_dir = find_p2_paper_dir(paper_query)
    api_key = get_api_key()
    q_dirs = sorted(path for path in variant_dir.glob("question_*") if path.is_dir())
    if question_filter is not None:
        q_dirs = [path for path in q_dirs if int(path.name.rsplit("_", 1)[1]) == question_filter]

    results, total_cost, total_tokens = [], 0.0, 0
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = [pool.submit(review_single_markscheme, q_dir, code, api_key, force) for q_dir in q_dirs]
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            total_cost += result.get("cost", 0.0)
            total_tokens += result.get("tokens", 0)
    return {
        "paper_code": code,
        "questions_reviewed": len(results),
        "failures": [result for result in results if result.get("status") in {"ERROR", "FAIL"}],
        "total_cost_usd": total_cost,
        "total_tokens": total_tokens,
        "results": results,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run source-grounded second mark-scheme OCR pass")
    parser.add_argument("paper")
    parser.add_argument("--question", type=int)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--max-workers", type=int, default=6)
    args = parser.parse_args()
    result = process_paper_markscheme_review(args.paper, args.question, args.force, args.max_workers)
    print(f"Done: {result['questions_reviewed']} reviewed | failures: {len(result['failures'])} | cost: ${result['total_cost_usd']:.5f}")


if __name__ == "__main__":
    main()
