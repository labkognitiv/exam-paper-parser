#!/usr/bin/env python3
"""Dedicated Master Orchestrator for Cambridge Physics 9702 Paper 2 (AS Structured Theory).

Coordinates the complete Paper 2 theory lifecycle in a single command:
1. Slices raw Question Paper & Mark Scheme PDFs into question directories (deterministic).
2. Performs 0-cost deterministic extraction quality audit (7 questions, 60 marks, image health, edge clipping).
3. Transcribes Question OCR structure into KaTeX JSON with automatic visual layout repair pass (multimodal AI).
4. Transcribes Mark Scheme tables verbatim into JSON with point distributions (B, M, A, C) & guidance (multimodal AI).
5. Runs a source-grounded second mark-scheme OCR pass (multimodal AI).
6. Mandatory Question OCR Review & Polish Pass (multimodal AI).
7. Generates N progressive hints for N marks (60 hints) and stepped teacher walkthroughs (multimodal AI).
8. Runs deterministic 5-layer master verification with auto-healing (marks, assets, syntax, zero dashes).
9. Automatically updates the orchestration tracker and optionally rebuilds the local web reviewer dataset.

Usage:
    python3 subjects/physics/9702/scripts/p2/process_p2_paper.py 9702_s24_21
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
import time

SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent

for p in [str(SCRIPT_DIR), str(SCRIPTS_ROOT)]:
    if p not in sys.path:
        sys.path.insert(0, p)

REPO_ROOT = next(
    (p for p in Path(__file__).resolve().parents if (p / "subjects").is_dir() and (p / "pyproject.toml").is_file()),
    Path(__file__).resolve().parents[4],
)
PHYSICS_P2_DIR = REPO_ROOT / "subjects/physics/9702/past papers/p2"
PROTOTYPE_DIR = REPO_ROOT / "subjects/physics/9702/prototypes/past-paper-question-reviewer"

import slice_p2_paper
from check_p2_extraction import check_p2_extraction, find_p2_paper_dir
import digitize_physics_question
import digitize_physics_markscheme
import review_physics_markscheme_ocr
import audit_physics_ocr_structure
import review_physics_question_ocr
import enrich_physics_p2
from verify_physics_paper import verify_full_paper


def resolve_p2_target(paper_query: str) -> tuple[str, Path, Path, Path]:
    code, variant_dir = find_p2_paper_dir(paper_query)
    source_dir = variant_dir / "source"

    qp_candidates = list(source_dir.glob("*_qp_*.pdf"))
    if not qp_candidates:
        raise FileNotFoundError(f"Missing Question Paper PDF in {source_dir}")
    ms_candidates = list(source_dir.glob("*_ms_*.pdf"))
    if not ms_candidates:
        raise FileNotFoundError(f"Missing Mark Scheme PDF in {source_dir}")

    return code, variant_dir, qp_candidates[0], ms_candidates[0]


def process_p2_orchestration(
    paper_query: str,
    question_filter: int | None = None,
    max_workers: int = 6,
    force: bool = False,
    skip_slice: bool = False,
    skip_ocr: bool = False,
    skip_ms: bool = False,
    skip_review: bool = False,
    skip_enrich: bool = False,
    skip_verify: bool = False,
    fix: bool = True,
    dpi: int = 150,
) -> dict:
    official_code, variant_dir, qp_pdf, ms_pdf = resolve_p2_target(paper_query)

    print("\n" + "=" * 80)
    print(f"ORCHESTRATING CAMBRIDGE PHYSICS PAPER 2 (THEORY): {official_code}")
    print(f"Directory:   {variant_dir}")
    print(f"QP Source:   {qp_pdf.name}")
    print(f"MS Source:   {ms_pdf.name}")
    print(f"Workers:     {max_workers} | Force: {force}")
    print("=" * 80)

    start_total = time.time()
    stage_summaries = {}

    # STAGE 1: PDF SLICING
    t0 = time.time()
    if skip_slice:
        print("\n>>> STAGE 1: PDF Slicing [SKIPPED per user flag]")
        stage_summaries["slicing"] = {"status": "SKIPPED", "elapsed_sec": 0.0}
    else:
        print("\n>>> STAGE 1: Slicing Question Paper & Mark Scheme PDFs...")
        q1_dir = variant_dir / "question_01"
        already_sliced = (q1_dir / "question_compact.png").is_file() and (q1_dir / "markscheme.png").is_file()

        if already_sliced and not force:
            print("  ✓ Paper 2 questions already sliced. Skipping slicing (use --force to re-slice).")
        else:
            slice_p2_paper.process_theory_paper(qp_pdf, ms_pdf, variant_dir, dpi=dpi)
            print("  ✓ Successfully sliced Paper 2 questions, figures & mark scheme.")

        stage_summaries["slicing"] = {"status": "SUCCESS", "elapsed_sec": round(time.time() - t0, 2)}

    # STAGE 2: DETERMINISTIC EXTRACTION AUDIT ($0.00)
    t0 = time.time()
    print("\n>>> STAGE 2: Running Deterministic Extraction Quality Audit ($0.00)...")
    ext_res = check_p2_extraction(variant_dir)

    print(f"  - Questions Extracted:        {ext_res['total_questions']}")
    print(f"  - Valid Compact Images:       {ext_res['valid_compact_images']}/{ext_res['total_questions']}")
    print(f"  - Valid Printable Images:     {ext_res['valid_printable_images']}/{ext_res['total_questions']}")
    print(f"  - Valid Mark Scheme Slices:   {ext_res['valid_ms_images']}/{ext_res['total_questions']}")
    print(f"  - Valid Diagram/Figure Crops: {ext_res['valid_figures']}/{ext_res['total_figures']}")

    if ext_res.get("errors"):
        print(f"  ✗ Extraction audit found {len(ext_res['errors'])} error(s):")
        for err in ext_res["errors"]:
            print(f"    [ERROR] {err}")
        stage_summaries["extraction_check"] = {
            "status": "FAIL",
            "elapsed_sec": round(time.time() - t0, 2),
            "errors": len(ext_res["errors"]),
        }
    else:
        print("  ✓ Theory slices verified healthy (clipping, boilerplate, figures & marks passed).")
        stage_summaries["extraction_check"] = {
            "status": "PASS",
            "elapsed_sec": round(time.time() - t0, 2),
            "errors": 0,
        }

    # STAGE 3: QUESTION OCR DIGITIZATION & LAYOUT REPAIR
    t0 = time.time()
    if skip_ocr:
        print("\n>>> STAGE 3: Question OCR [SKIPPED per user flag]")
        stage_summaries["question_ocr"] = {"status": "SKIPPED", "elapsed_sec": 0.0, "cost": 0.0}
    else:
        print("\n>>> STAGE 3: Running Question OCR Digitization & Layout Repair via Meta Muse Spark...")
        api_key = digitize_physics_question.get_api_key()
        ocr_res = digitize_physics_question.process_paper(
            variant_dir,
            api_key=api_key,
            force=force,
            repair=True,
            max_workers=max_workers,
        )
        audit_res = audit_physics_ocr_structure.audit_paper_ocr(variant_dir)
        total_ocr_errs = sum(len([i for i in issues if i["level"] == "ERROR"]) for issues in audit_res.values())
        print(f"  ✓ Stage 3 OCR Structure Audit: {total_ocr_errs} error(s) across {len(audit_res)} questions.")
        stage_summaries["question_ocr"] = {
            "status": "SUCCESS" if total_ocr_errs == 0 else "WARNING",
            "elapsed_sec": round(time.time() - t0, 2),
            "cost": ocr_res.get("total_cost", 0.0),
            "tokens": ocr_res.get("total_tokens", 0),
            "count": ocr_res.get("questions_digitized", 0),
            "audit_errors": total_ocr_errs,
        }

    # STAGE 4: MARK SCHEME DIGITIZATION
    t0 = time.time()
    if skip_ms:
        print("\n>>> STAGE 4: Mark Scheme Digitization [SKIPPED per user flag]")
        stage_summaries["markscheme_ocr"] = {"status": "SKIPPED", "elapsed_sec": 0.0, "cost": 0.0}
    else:
        print("\n>>> STAGE 4: Running Mark Scheme Digitization via Meta Muse Spark...")
        ms_res = digitize_physics_markscheme.process_paper_markschemes(
            official_code,
            question_filter=question_filter,
            force=force,
            max_workers=max_workers,
        )
        stage_summaries["markscheme_ocr"] = {
            "status": "SUCCESS",
            "elapsed_sec": round(time.time() - t0, 2),
            "cost": ms_res.get("total_cost_usd", 0.0),
            "tokens": ms_res.get("total_tokens", 0),
            "count": ms_res.get("questions_processed", 0),
            "total_marks": ms_res.get("paper_total_marks", 0),
        }

    # STAGE 5: SOURCE-GROUNDED MARK SCHEME OCR REVIEW
    t0 = time.time()
    if skip_ms:
        print("\n>>> STAGE 5: Mark Scheme OCR Review [Mark Scheme OCR was skipped]")
        stage_summaries["markscheme_review"] = {"status": "SKIPPED", "elapsed_sec": 0.0, "cost": 0.0}
    else:
        print("\n>>> STAGE 5: Running Source-Grounded Mark Scheme OCR Review via Meta Muse Spark...")
        ms_review_res = review_physics_markscheme_ocr.process_paper_markscheme_review(
            official_code,
            question_filter=question_filter,
            force=force,
            max_workers=max_workers,
        )
        stage_summaries["markscheme_review"] = {
            "status": "SUCCESS" if not ms_review_res.get("failures") else "FAIL",
            "elapsed_sec": round(time.time() - t0, 2),
            "cost": ms_review_res.get("total_cost_usd", 0.0),
            "tokens": ms_review_res.get("total_tokens", 0),
            "count": ms_review_res.get("questions_reviewed", 0),
            "failures": len(ms_review_res.get("failures", [])),
        }

    # STAGE 6: MANDATORY QUESTION OCR REVIEW & POLISH PASS
    t0 = time.time()
    if skip_review or skip_ocr:
        reason = "Question OCR was skipped" if skip_ocr else "SKIPPED per user flag"
        print(f"\n>>> STAGE 6: Mandatory Question OCR Review [{reason}]")
        stage_summaries["ocr_review"] = {"status": "SKIPPED", "elapsed_sec": 0.0, "cost": 0.0}
    else:
        print("\n>>> STAGE 6: Running Mandatory Question OCR Review & Polish Pass via Meta Muse Spark...")
        rev_res = review_physics_question_ocr.process_paper_ocr_review(
            variant_dir,
            paper_code=official_code,
            question_filter=question_filter,
            force=force,
            max_workers=max_workers,
        )
        stage_summaries["ocr_review"] = {
            "status": "SUCCESS",
            "elapsed_sec": rev_res.get("elapsed_sec", round(time.time() - t0, 2)),
            "cost": rev_res.get("total_cost_usd", 0.0),
            "tokens": rev_res.get("total_tokens", 0),
            "count": rev_res.get("questions_reviewed", 0),
        }

    # STAGE 7: PEDAGOGICAL AI ENRICHMENT
    t0 = time.time()
    if skip_enrich:
        print("\n>>> STAGE 7: Pedagogical AI Enrichment [SKIPPED per user flag]")
        stage_summaries["enrichment"] = {"status": "SKIPPED", "elapsed_sec": 0.0, "cost": 0.0}
    else:
        print("\n>>> STAGE 7: Generating N Progressive Hints for N Marks (60 hints) & Stepped Walkthroughs...")
        enr_res = enrich_physics_p2.process_paper_theory_enrichment(
            official_code,
            question_filter=question_filter,
            force=force,
            max_workers=max_workers,
        )
        stage_summaries["enrichment"] = {
            "status": "SUCCESS",
            "elapsed_sec": round(time.time() - t0, 2),
            "cost": enr_res.get("total_cost_usd", 0.0),
            "tokens": enr_res.get("total_tokens", 0),
            "count": enr_res.get("questions_processed", 0),
        }

    # STAGE 8: DETERMINISTIC 5-LAYER MASTER VERIFICATION
    t0 = time.time()
    if skip_verify:
        print("\n>>> STAGE 8: 5-Layer Master Verification [SKIPPED per user flag]")
        stage_summaries["verification"] = {"status": "SKIPPED", "elapsed_sec": 0.0, "errors": 0, "warnings": 0}
    else:
        print(f"\n>>> STAGE 8: Running 5-Layer Master Verification (Fix typography: {fix})...")
        issues = verify_full_paper(variant_dir, fix=fix, skip_enrichment=skip_enrich, skip_ocr=skip_ocr)
        errors = [i for i in issues if i.get("level") == "ERROR"]
        warnings = [i for i in issues if i.get("level") == "WARNING"]

        if not errors and not warnings:
            print("  ✓ Verification Result: PASS (0 errors, 0 warnings)")
        else:
            print(f"  Result: {len(errors)} error(s), {len(warnings)} warning(s)")
            for iss in errors:
                print(f"    [ERROR] [{iss.get('question', '-')}] {iss.get('message')}")
            for iss in warnings:
                print(f"    [WARN]  [{iss.get('question', '-')}] {iss.get('message')}")

        stage_summaries["verification"] = {
            "status": "PASS" if not errors and not warnings else ("WARN" if not errors else "FAIL"),
            "elapsed_sec": round(time.time() - t0, 2),
            "errors": len(errors),
            "warnings": len(warnings),
        }

    total_elapsed = round(time.time() - start_total, 2)
    total_cost = sum(v.get("cost", 0.0) for v in stage_summaries.values())
    total_tokens = sum(v.get("tokens", 0) for v in stage_summaries.values())

    # FINAL SUMMARY REPORT
    print("\n" + "=" * 80)
    print(f"PHYSICS PAPER 2 PIPELINE SUMMARY: {official_code}")
    print(f"Total Time: {total_elapsed}s | AI Cost: ${total_cost:.5f} | Tokens: {total_tokens}")
    print("-" * 80)
    for st_name, st_info in stage_summaries.items():
        cost_str = f" | Cost: ${st_info.get('cost', 0.0):.5f}" if "cost" in st_info else ""
        print(f"  - {st_name.upper():<18}: {st_info.get('status')} ({st_info.get('elapsed_sec')}s{cost_str})")
    print("=" * 80 + "\n")

    # STAGE 8: UPDATE ORCHESTRATION TRACKER
    try:
        from orchestration_tracker import record_orchestration_run
        q_dirs = sorted([d for d in variant_dir.iterdir() if d.is_dir() and d.name.startswith("question_")])
        record_orchestration_run("p2", {
            "paper_code": official_code,
            "questions_count": stage_summaries.get("slicing", {}).get("questions", len(q_dirs) or 7),
            "total_marks": stage_summaries.get("markscheme_ocr", {}).get("total_marks", 60),
            "slicing": stage_summaries.get("slicing", {}).get("status", "PASS"),
            "question_ocr": stage_summaries.get("question_ocr", {}).get("status", "PASS"),
            "mark_scheme": stage_summaries.get("markscheme_ocr", {}).get("status", "PASS"),
            "ocr_review": stage_summaries.get("ocr_review", {}).get("status", "PASS"),
            "enrichment": stage_summaries.get("enrichment", {}).get("status", "PASS"),
            "verification": stage_summaries.get("verification", {}).get("status", "PASS"),
            "cost_usd": total_cost,
            "duration_sec": total_elapsed,
            "status": "COMPLETE" if stage_summaries.get("verification", {}).get("status") in ("PASS", "WARN", "SKIPPED") else "FAILED",
            "notes": "Orchestrated via process_p2_paper.py",
        })
        print("  ✓ Updated Physics P2 Tracker: subjects/physics/9702/reviews/p2-orchestration-tracker.md")
    except Exception as exc:
        print(f"  Warning: Could not update Physics P2 tracker: {exc}")

    return {
        "paper_code": official_code,
        "variant_dir": str(variant_dir),
        "total_elapsed_sec": total_elapsed,
        "total_cost_usd": total_cost,
        "total_tokens": total_tokens,
        "stages": stage_summaries,
    }


def rebuild_reviewer_dataset() -> None:
    build_script = PROTOTYPE_DIR / "build_data.py"
    if not build_script.is_file():
        print(f"Warning: Could not find build_data.py at {build_script}", file=sys.stderr)
        return

    print(">>> REBUILDING WEB REVIEWER DATASET...")
    try:
        subprocess.run([sys.executable, str(build_script)], check=True)
        print("✓ Web reviewer dataset updated successfully.\n")
    except subprocess.CalledProcessError as exc:
        print(f"Error updating reviewer dataset: {exc}", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(description="Master Dedicated Orchestrator for Cambridge Physics 9702 Paper 2")
    parser.add_argument("paper", nargs="?", help="Paper code or query (e.g. 9702_s24_21)")
    parser.add_argument("--question", type=int, help="Process a single question number")
    parser.add_argument("--max-workers", type=int, default=6, help="Parallel worker threads")
    parser.add_argument("--force", action="store_true", help="Re-generate even if artifacts exist")
    parser.add_argument("--skip-slice", action="store_true", help="Skip slicing stage")
    parser.add_argument("--skip-ocr", action="store_true", help="Skip Question OCR stage")
    parser.add_argument("--skip-ms", action="store_true", help="Skip Mark Scheme OCR stage")
    parser.add_argument("--skip-review", action="store_true", help="Skip mandatory Question OCR review pass")
    parser.add_argument("--skip-enrich", action="store_true", help="Skip pedagogical AI enrichment stage")
    parser.add_argument("--skip-verify", action="store_true", help="Skip verification stage")
    parser.add_argument("--no-rebuild-ui", action="store_true", help="Skip refreshing web reviewer dataset")
    parser.add_argument("--dpi", type=int, default=150, help="Rendering DPI for question crops")

    args = parser.parse_args()
    if not args.paper:
        print("Error: Specify a paper code (e.g. 9702_s24_21)", file=sys.stderr)
        sys.exit(1)

    t_global_start = time.time()
    process_p2_orchestration(
        args.paper,
        question_filter=args.question,
        max_workers=args.max_workers,
        force=args.force,
        skip_slice=args.skip_slice,
        skip_ocr=args.skip_ocr,
        skip_ms=args.skip_ms,
        skip_review=args.skip_review,
        skip_enrich=args.skip_enrich,
        skip_verify=args.skip_verify,
        dpi=args.dpi,
    )

    if not args.no_rebuild_ui:
        rebuild_reviewer_dataset()

    print(f"All Physics Paper 2 tasks finished in {time.time() - t_global_start:.2f}s.")


if __name__ == "__main__":
    main()
