#!/usr/bin/env python3
"""Batch Image and Mark Scheme Extractor for Cambridge Physics 9702 Paper 2 (Theory).

Extracts all question images, diagrams, and mark scheme slices for all 69 Paper 2 papers (2016 to 2025)
with ZERO API calls using local PyMuPDF rendering.
Processes papers in configurable batches of 5.

Outputs per question:
- question_compact.png
- question_printable.png
- question_printable.pdf
- figure_X_Y.png (all question figures)
- question.txt
- markscheme.png

Outputs at paper root:
- paper_compact.pdf
- paper_printable.pdf
- paper_markscheme.pdf

Zero em dashes, zero en dashes.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import shutil
import sys
import time

REPO_ROOT = next(
    (p for p in Path(__file__).resolve().parents if (p / "subjects").is_dir() and (p / "pyproject.toml").is_file()),
    Path(__file__).resolve().parents[4],
)
PHYSICS_P2_DIR = REPO_ROOT / "subjects/physics/9702/past papers/p2"
SCRIPTS_P2_DIR = Path(__file__).resolve().parent

if str(SCRIPTS_P2_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_P2_DIR))

import slice_p2_paper

PAPER_RE = re.compile(
    r"^(?P<subject>\d{4})_(?P<session>[msw])(?P<year>\d{2})_qp_(?P<variant>2\d)$",
    re.I,
)


def get_all_p2_papers(min_year: int = 2016, max_year: int = 2025) -> list[dict]:
    """Find and return all complete P2 papers sorted chronologically."""
    papers = []
    for qp_pdf in sorted(PHYSICS_P2_DIR.rglob("*_qp_*.pdf")):
        m = PAPER_RE.match(qp_pdf.stem)
        if not m:
            continue
        ms_candidates = list(qp_pdf.parent.glob("*_ms_*.pdf"))
        if not ms_candidates:
            continue
        ms_pdf = ms_candidates[0]
        paper_dir = qp_pdf.parent.parent

        year = 2000 + int(m.group("year"))
        if year < min_year or year > max_year:
            continue

        session_order = {"m": 1, "s": 2, "w": 3}.get(m.group("session").lower(), 9)
        variant = int(m.group("variant"))
        paper_code = f"{m.group('subject')}_{m.group('session').lower()}{m.group('year')}_{variant}"

        papers.append(
            {
                "paper_code": paper_code,
                "year": year,
                "session_order": session_order,
                "variant": variant,
                "qp_pdf": qp_pdf,
                "ms_pdf": ms_pdf,
                "paper_dir": paper_dir,
            }
        )

    # Sort deterministically: year -> session -> variant
    papers.sort(key=lambda p: (p["year"], p["session_order"], p["variant"]))
    return papers


def audit_paper_assets(paper_dir: Path) -> tuple[bool, str, int, int]:
    """Verify that question directories contain question images and markscheme images."""
    q_dirs = sorted([d for d in paper_dir.glob("question_*") if d.is_dir()])
    if not q_dirs:
        return False, "no question directories found", 0, 0

    total_images = 0
    total_figures = 0

    for q_dir in q_dirs:
        comp_img = q_dir / "question_compact.png"
        print_img = q_dir / "question_printable.png"
        ms_img = q_dir / "markscheme.png"

        if not comp_img.exists() or comp_img.stat().st_size < 1000:
            return False, f"missing or corrupt {comp_img.name} in {q_dir.name}", 0, 0
        if not print_img.exists() or print_img.stat().st_size < 1000:
            return False, f"missing or corrupt {print_img.name} in {q_dir.name}", 0, 0
        if not ms_img.exists() or ms_img.stat().st_size < 1000:
            return False, f"missing or corrupt {ms_img.name} in {q_dir.name}", 0, 0

        # Count figures
        figs = list(q_dir.glob("figure_*.*"))
        total_figures += len(figs)
        total_images += 3 + len(figs)  # compact + printable + markscheme + figures

    # Check compiled PDFs
    p_comp = paper_dir / "paper_compact.pdf"
    p_print = paper_dir / "paper_printable.pdf"
    p_ms = paper_dir / "paper_markscheme.pdf"

    if not p_comp.exists() or not p_print.exists() or not p_ms.exists():
        return False, "missing compiled paper-level PDFs", 0, 0

    return True, "valid", len(q_dirs), total_images


def run_batch(
    batch_num: int,
    total_batches: int,
    batch_papers: list[dict],
    dpi: int = 150,
    force: bool = False,
) -> list[dict]:
    print(f"\n{'=' * 75}")
    print(f"STARTING BATCH {batch_num}/{total_batches} ({len(batch_papers)} papers)")
    print(f"{'=' * 75}")

    results = []
    t_batch_start = time.time()

    for idx, paper in enumerate(batch_papers, 1):
        p_code = paper["paper_code"]
        qp_pdf = paper["qp_pdf"]
        ms_pdf = paper["ms_pdf"]
        p_dir = paper["paper_dir"]

        is_valid, msg, n_qs, n_imgs = audit_paper_assets(p_dir)
        if is_valid and not force:
            print(f"[{idx}/{len(batch_papers)}] {p_code}: Already processed and verified ({n_qs} questions, {n_imgs} assets). Skipping.")
            results.append(
                {
                    "paper_code": p_code,
                    "status": "SKIPPED (verified)",
                    "questions": n_qs,
                    "images": n_imgs,
                    "elapsed_sec": 0.0,
                }
            )
            continue

        print(f"\n[{idx}/{len(batch_papers)}] Processing {p_code}...")
        t0 = time.time()
        try:
            slice_p2_paper.process_theory_paper(qp_pdf, ms_pdf, p_dir, dpi=dpi)
            elapsed = round(time.time() - t0, 2)

            is_valid, reason, num_qs, num_imgs = audit_paper_assets(p_dir)
            if not is_valid:
                print(f"  FAILED audit for {p_code}: {reason}")
                results.append(
                    {
                        "paper_code": p_code,
                        "status": f"FAILED ({reason})",
                        "questions": num_qs,
                        "images": num_imgs,
                        "elapsed_sec": elapsed,
                    }
                )
            else:
                print(f"  SUCCESS {p_code}: {num_qs} questions extracted, {num_imgs} assets created in {elapsed}s")
                results.append(
                    {
                        "paper_code": p_code,
                        "status": "SUCCESS",
                        "questions": num_qs,
                        "images": num_imgs,
                        "elapsed_sec": elapsed,
                    }
                )
        except Exception as exc:
            print(f"  ERROR processing {p_code}: {exc}")
            results.append(
                {
                    "paper_code": p_code,
                    "status": f"ERROR ({exc})",
                    "questions": 0,
                    "images": 0,
                    "elapsed_sec": 0.0,
                }
            )

    batch_elapsed = round(time.time() - t_batch_start, 2)
    total_imgs = sum(r["images"] for r in results if "SUCCESS" in r["status"] or "SKIPPED" in r["status"])
    total_qs = sum(r["questions"] for r in results if "SUCCESS" in r["status"] or "SKIPPED" in r["status"])
    print(f"\nBatch {batch_num}/{total_batches} finished in {batch_elapsed}s. Verified {total_qs} questions, {total_imgs} total image assets.")
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Batch Image and Mark Scheme Extractor for Physics 9702 Paper 2 (Theory)")
    parser.add_argument("--batch", type=int, default=None, help="Process a specific batch number (1-based)")
    parser.add_argument("--batch-size", type=int, default=5, help="Number of papers per batch (default: 5)")
    parser.add_argument("--all", action="store_true", help="Process all batches sequentially")
    parser.add_argument("--force", action="store_true", help="Force re-extraction even if assets exist")
    parser.add_argument("--dpi", type=int, default=150, help="Rendering DPI (default: 150)")
    parser.add_argument("--list", action="store_true", help="List all batches and papers without processing")
    parser.add_argument("--min-year", type=int, default=2016, help="Earliest year (default: 2016)")
    parser.add_argument("--max-year", type=int, default=2025, help="Latest year (default: 2025)")
    args = parser.parse_args()

    all_papers = get_all_p2_papers(min_year=args.min_year, max_year=args.max_year)
    total_papers = len(all_papers)
    batch_size = args.batch_size
    batches = [all_papers[i : i + batch_size] for i in range(0, total_papers, batch_size)]
    total_batches = len(batches)

    print(f"Found {total_papers} total Paper 2 papers across {total_batches} batches (batch size: {batch_size}) for years {args.min_year}-{args.max_year}.")

    if args.list:
        for b_idx, batch_papers in enumerate(batches, 1):
            print(f"\nBatch {b_idx}/{total_batches} ({len(batch_papers)} papers):")
            for p in batch_papers:
                print(f"  - {p['paper_code']}: {p['qp_pdf'].name}")
        return

    if args.batch is not None:
        if not (1 <= args.batch <= total_batches):
            print(f"Error: Batch {args.batch} out of range (1 to {total_batches})", file=sys.stderr)
            sys.exit(1)
        run_batch(args.batch, total_batches, batches[args.batch - 1], dpi=args.dpi, force=args.force)
        return

    if not args.all:
        print("Specify --all to run all batches, --batch <N> to run one batch, or --list to inspect batches.")
        return

    # Run all batches
    all_results = []
    t_global_start = time.time()

    for b_idx, batch_papers in enumerate(batches, 1):
        res = run_batch(b_idx, total_batches, batch_papers, dpi=args.dpi, force=args.force)
        all_results.extend(res)

    total_time = round(time.time() - t_global_start, 2)
    successful = [r for r in all_results if "SUCCESS" in r["status"] or "SKIPPED" in r["status"]]
    total_extracted_images = sum(r["images"] for r in successful)
    total_extracted_questions = sum(r["questions"] for r in successful)

    print(f"\n{'=' * 75}")
    print("ALL BATCHES COMPLETE")
    print(f"Total Papers:       {total_papers}")
    print(f"Successful:         {len(successful)}/{total_papers}")
    print(f"Total Questions:    {total_extracted_questions}")
    print(f"Total Assets:       {total_extracted_images} image/diagram/markscheme files")
    print(f"Total Time:         {total_time}s")
    print(f"AI API Cost:        $0.000000 (Zero API calls)")
    print(f"{'=' * 75}\n")


if __name__ == "__main__":
    main()
