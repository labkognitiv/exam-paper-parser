#!/usr/bin/env python3
"""Orchestrate additive AI processing for one sliced Physics 9702 P4 paper.

P4 has immutable canonical questions in ``parsed-questions/`` and immutable
official mark schemes in ``mark-schemes/``. This workflow never writes either.
It writes Muse-derived OCR, two-pass mark-scheme OCR and enrichment only inside
the matching ``question_XX/`` directory, then verifies those derivatives against
the canonical records and hashes the canonical records before and after work.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
import re
import sys
import time

SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent
P2_SCRIPTS = SCRIPTS_ROOT / "p2"
for path in (SCRIPT_DIR, P2_SCRIPTS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

REPO_ROOT = next(
    (path for path in Path(__file__).resolve().parents if (path / "subjects").is_dir() and (path / "pyproject.toml").is_file()),
    Path(__file__).resolve().parents[4],
)
P4_ROOT = REPO_ROOT / "subjects/physics/9702/past papers/p4"

from batch_slice_p4 import audit_paper_assets, get_all_p4_papers
import audit_physics_ocr_structure
import digitize_physics_markscheme
import digitize_physics_question
import enrich_physics_p2
import review_physics_markscheme_ocr
import review_physics_question_ocr


def resolve_p4_target(paper_query: str) -> tuple[str, Path]:
    query = paper_query.lower()
    for paper in get_all_p4_papers():
        if query in {paper["paper_code"].lower(), paper["paper_dir"].name.lower()}:
            return paper["paper_code"], paper["paper_dir"]
    candidate = Path(paper_query).expanduser()
    if candidate.is_dir() and (candidate / "source").is_dir():
        source = next(candidate.joinpath("source").glob("*_qp_*.pdf"), None)
        if source:
            match = re.match(r"^(9702_[msw]\d{2})_qp_(4\d)$", source.stem, re.I)
            if match:
                return f"{match.group(1).lower()}_{match.group(2)}", candidate
    raise FileNotFoundError(f"No sliced P4 paper found for: {paper_query}")


def question_dirs(variant_dir: Path, question_filter: int | None = None) -> list[Path]:
    directories = sorted(path for path in variant_dir.glob("question_*") if path.is_dir())
    if question_filter is not None:
        directories = [path for path in directories if int(path.name.rsplit("_", 1)[1]) == question_filter]
    return directories


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_snapshot(variant_dir: Path) -> dict[str, str]:
    files = sorted((variant_dir / "parsed-questions").glob("question_*.json"))
    files += sorted((variant_dir / "mark-schemes").glob("markscheme_*.json"))
    return {str(path.relative_to(variant_dir)): sha256(path) for path in files}


def canonical_records(variant_dir: Path, q_num: int) -> tuple[dict, dict]:
    question_path = variant_dir / "parsed-questions" / f"question_{q_num:02d}.json"
    markscheme_path = variant_dir / "mark-schemes" / f"markscheme_{q_num:02d}.json"
    return (
        json.loads(question_path.read_text(encoding="utf-8")),
        json.loads(markscheme_path.read_text(encoding="utf-8")),
    )


def canonical_preflight(variant_dir: Path, expected_total: int = 100) -> list[str]:
    errors: list[str] = []
    ok, detail, count, _images = audit_paper_assets(variant_dir)
    if not ok:
        errors.append(f"asset audit failed: {detail}")
    q_dirs = question_dirs(variant_dir)
    question_files = sorted((variant_dir / "parsed-questions").glob("question_*.json"))
    markscheme_files = sorted((variant_dir / "mark-schemes").glob("markscheme_*.json"))
    if not q_dirs or len(q_dirs) != len(question_files) or len(q_dirs) != len(markscheme_files):
        errors.append(f"inventory mismatch: slices={len(q_dirs)}, questions={len(question_files)}, markschemes={len(markscheme_files)}")
        return errors

    question_total = 0
    markscheme_total = 0
    for q_dir in q_dirs:
        q_num = int(q_dir.name.rsplit("_", 1)[1])
        try:
            question, markscheme = canonical_records(variant_dir, q_num)
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"Q{q_num}: cannot read canonical record: {exc}")
            continue
        if question.get("question_id") != markscheme.get("question_id"):
            errors.append(f"Q{q_num}: canonical question/markscheme IDs disagree")
        q_marks = question.get("total_marks")
        ms_marks = markscheme.get("total_marks")
        if not isinstance(q_marks, int) or not isinstance(ms_marks, int):
            errors.append(f"Q{q_num}: canonical total_marks must be integers")
            continue
        if q_marks != ms_marks:
            errors.append(f"Q{q_num}: canonical marks disagree: question={q_marks}, markscheme={ms_marks}")
        question_total += q_marks
        markscheme_total += ms_marks
    if count != len(q_dirs):
        errors.append(f"asset audit question count {count} differs from slice inventory {len(q_dirs)}")
    if question_total != expected_total or markscheme_total != expected_total:
        errors.append(f"paper totals must be {expected_total}: question={question_total}, markscheme={markscheme_total}")
    return errors


def run_parallel(q_dirs: list[Path], max_workers: int, operation) -> dict:
    results: list[dict] = []
    total_cost = 0.0
    total_tokens = 0
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = [pool.submit(operation, q_dir) for q_dir in q_dirs]
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            total_cost += result.get("cost", 0.0)
            total_tokens += result.get("tokens", 0)
    failures = [result for result in results if result.get("status") in {"ERROR", "FAIL"}]
    return {"count": len(results), "cost": total_cost, "tokens": total_tokens, "failures": failures, "results": results}


def verify_derived_question(q_dir: Path, paper_code: str, variant_dir: Path) -> list[str]:
    errors: list[str] = []
    q_num = int(q_dir.name.rsplit("_", 1)[1])
    try:
        canonical_question, canonical_ms = canonical_records(variant_dir, q_num)
    except (OSError, json.JSONDecodeError) as exc:
        return [str(exc)]

    ocr_path = q_dir / "question_ocr.json"
    ms_path = q_dir / "markscheme.json"
    review_meta_path = q_dir / "markscheme_review_meta.json"
    enrichment_path = q_dir / "enrichment.json"
    required = (ocr_path, ms_path, review_meta_path, q_dir / "question_ocr_review_meta.json", enrichment_path, q_dir / "enrichment_meta.json")
    for path in required:
        if not path.is_file():
            errors.append(f"{path.name} missing")
    if errors:
        return errors

    try:
        ocr = json.loads(ocr_path.read_text(encoding="utf-8"))
        model_ms = json.loads(ms_path.read_text(encoding="utf-8"))
        review_meta = json.loads(review_meta_path.read_text(encoding="utf-8"))
        enrichment = json.loads(enrichment_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"invalid derived JSON: {exc}"]

    if review_meta.get("status") != "PASS":
        errors.append("markscheme second pass did not reconcile")
    if ocr.get("question_id") != canonical_question.get("question_id"):
        errors.append("question OCR identity differs from canonical question")
    if ocr.get("total_marks") != canonical_question.get("total_marks"):
        errors.append(f"question OCR marks {ocr.get('total_marks')} differ from canonical {canonical_question.get('total_marks')}")
    expected_total, expected_parts = review_physics_markscheme_ocr.canonical_marks(q_dir)
    reconciliation = review_physics_markscheme_ocr.reconciliation_errors(model_ms, expected_total, expected_parts)
    errors.extend(f"markscheme OCR: {error}" for error in reconciliation)
    lint_errors = [issue["message"] for issue in audit_physics_ocr_structure.audit_question_structure(q_dir) if issue["level"] == "ERROR"]
    errors.extend(f"question OCR: {error}" for error in lint_errors)

    if canonical_question.get("official_reconciliation"):
        expected_parts_map = {
            p.get("id"): p.get("marks")
            for p in canonical_question.get("parts", [])
            if isinstance(p, dict) and p.get("marks") and p.get("marks") > 0
        }
    else:
        expected_parts_map = {
            part.get("id"): part.get("marks")
            for part in canonical_ms.get("parts", [])
            if isinstance(part, dict)
        }

    enriched_parts = {part.get("part_id"): part for part in enrichment.get("parts", []) if isinstance(part, dict)}
    if set(enriched_parts) != set(expected_parts_map):
        errors.append("enrichment part IDs differ from canonical mark scheme")
    for part_id, marks in expected_parts_map.items():
        if not isinstance(marks, int) or marks <= 0:
            continue
        hints = enriched_parts.get(part_id, {}).get("hints", [])
        if not isinstance(hints, list) or len(hints) != marks:
            errors.append(f"{part_id}: expected {marks} hints, found {len(hints) if isinstance(hints, list) else 'non-list'}")
    return errors


def process_p4_orchestration(
    paper_query: str,
    question_filter: int | None = None,
    max_workers: int = 12,
    force: bool = False,
    skip_ocr: bool = False,
    skip_ms: bool = False,
    skip_review: bool = False,
    skip_enrich: bool = False,
    skip_verify: bool = False,
) -> dict:
    paper_code, variant_dir = resolve_p4_target(paper_query)
    q_dirs = question_dirs(variant_dir, question_filter)
    if not q_dirs:
        raise FileNotFoundError(f"No P4 question slices in {variant_dir}")
    preflight_errors = canonical_preflight(variant_dir)
    if preflight_errors:
        raise RuntimeError("P4 canonical preflight failed:\n- " + "\n- ".join(preflight_errors))
    source_before = canonical_snapshot(variant_dir)
    stages: dict[str, dict] = {"preflight": {"status": "PASS", "errors": 0}}
    total_cost = 0.0
    total_tokens = 0

    def add_stage(name: str, result: dict) -> None:
        nonlocal total_cost, total_tokens
        stages[name] = {"status": "FAIL" if result["failures"] else "SUCCESS", **result}
        total_cost += result["cost"]
        total_tokens += result["tokens"]

    if skip_ocr:
        stages["question_ocr"] = {"status": "SKIPPED"}
    else:
        api_key = digitize_physics_question.get_api_key()
        add_stage("question_ocr", run_parallel(q_dirs, max_workers, lambda q: digitize_physics_question.digitize_single_question(q, api_key, force=force, repair=True)))

    if skip_ms:
        stages["markscheme_ocr"] = {"status": "SKIPPED"}
        stages["markscheme_review"] = {"status": "SKIPPED"}
    else:
        api_key = digitize_physics_markscheme.get_api_key()
        add_stage("markscheme_ocr", run_parallel(q_dirs, max_workers, lambda q: digitize_physics_markscheme.digitize_single_ms(q, paper_code, int(q.name.rsplit("_", 1)[1]), api_key, force=force)))
        add_stage("markscheme_review", run_parallel(q_dirs, max_workers, lambda q: review_physics_markscheme_ocr.review_single_markscheme(q, paper_code, api_key, force=force)))

    if skip_review or skip_ocr:
        stages["question_ocr_review"] = {"status": "SKIPPED"}
    else:
        api_key = review_physics_question_ocr.get_api_key()
        add_stage("question_ocr_review", run_parallel(q_dirs, max_workers, lambda q: review_physics_question_ocr.review_single_question_ocr(q, paper_code, api_key, force=force)))

    if skip_enrich:
        stages["enrichment"] = {"status": "SKIPPED"}
    else:
        api_key = enrich_physics_p2.get_api_key()
        def enrich(q_dir: Path) -> dict:
            name, _data, meta, cached = enrich_physics_p2.enrich_single_theory_question(q_dir, api_key, force=force)
            tokens = meta.get("tokens", {})
            return {"status": "SKIPPED" if cached else ("SUCCESS" if meta.get("valid_json", True) else "ERROR"), "question": name, "cost": 0.0 if cached else meta.get("cost_usd", 0.0), "tokens": 0 if cached else tokens.get("total_tokens", 0)}
        add_stage("enrichment", run_parallel(q_dirs, max_workers, enrich))

    source_after = canonical_snapshot(variant_dir)
    source_changed = source_before != source_after
    if skip_verify:
        stages["verification"] = {"status": "SKIPPED"}
        verification_errors: list[str] = []
    else:
        verification_errors = []
        if source_changed:
            verification_errors.append("immutable canonical question or official mark-scheme source changed during processing")
        for q_dir in q_dirs:
            verification_errors.extend(f"{q_dir.name}: {error}" for error in verify_derived_question(q_dir, paper_code, variant_dir))
        stages["verification"] = {"status": "PASS" if not verification_errors else "FAIL", "errors": verification_errors}

    status = "PASS" if stages["verification"]["status"] == "PASS" else "FAIL"
    print(f"VERIFICATION : {status}")
    return {"paper_code": paper_code, "variant_dir": str(variant_dir), "status": status, "total_cost_usd": total_cost, "total_tokens": total_tokens, "stages": stages, "verification_errors": verification_errors}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paper", help="P4 paper code, e.g. 9702_s25_41")
    parser.add_argument("--question", type=int)
    parser.add_argument("--max-workers", type=int, default=12)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--skip-ocr", action="store_true")
    parser.add_argument("--skip-ms", action="store_true")
    parser.add_argument("--skip-review", action="store_true")
    parser.add_argument("--skip-enrich", action="store_true")
    parser.add_argument("--skip-verify", action="store_true")
    args = parser.parse_args()
    result = process_p4_orchestration(args.paper, args.question, args.max_workers, args.force, args.skip_ocr, args.skip_ms, args.skip_review, args.skip_enrich, args.skip_verify)
    print(f"P4 {result['paper_code']}: {result['status']} | cost ${result['total_cost_usd']:.5f} | tokens {result['total_tokens']}")


if __name__ == "__main__":
    main()
