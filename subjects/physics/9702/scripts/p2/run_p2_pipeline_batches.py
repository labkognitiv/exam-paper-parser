#!/usr/bin/env python3
"""Run remaining Physics 9702 P2 AI pipeline work in one unrestricted wave.

Slicing is deliberately excluded. By default every selected paper starts
concurrently, and every process receives enough question workers to submit every
question in its paper concurrently. ``--batch-size`` is retained only as an
explicit operational throttle; it is never the default.
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
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from batch_slice_p2 import get_all_p2_papers
from check_p2_extraction import check_p2_extraction


REPO_ROOT = next(
    (p for p in Path(__file__).resolve().parents if (p / "subjects").is_dir() and (p / "pyproject.toml").is_file()),
    Path(__file__).resolve().parents[4],
)
PIPELINE = SCRIPT_DIR / "process_p2_paper.py"
REPORT_DIR = REPO_ROOT / "artifacts/physics/p2/batch-pipeline"
REVIEWER_BUILD = REPO_ROOT / "subjects/physics/9702/prototypes/past-paper-question-reviewer/build_data.py"
REQUIRED_FILES = (
    "question_ocr.json",
    "question_ocr_meta.json",
    "markscheme.json",
    "markscheme_meta.json",
    "markscheme_review_meta.json",
    "question_ocr_review_meta.json",
    "enrichment.json",
    "enrichment_meta.json",
)


def is_complete(paper_dir: Path) -> bool:
    question_dirs = sorted(p for p in paper_dir.glob("question_*") if p.is_dir())
    if not question_dirs:
        return False
    for question_dir in question_dirs:
        if not all((question_dir / name).is_file() for name in REQUIRED_FILES):
            return False
        try:
            review_meta = json.loads((question_dir / "markscheme_review_meta.json").read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return False
        if review_meta.get("status") != "PASS":
            return False
    return True


def preflight(paper: dict) -> tuple[bool, str]:
    result = check_p2_extraction(paper["paper_dir"])
    question_dirs = sorted(p for p in paper["paper_dir"].glob("question_*") if p.is_dir())
    required_assets = ("question_compact.png", "question_printable.png", "markscheme.png")
    missing = [
        f"{question_dir.name}/{asset}"
        for question_dir in question_dirs
        for asset in required_assets
        if not (question_dir / asset).is_file() or (question_dir / asset).stat().st_size == 0
    ]
    if not question_dirs or missing:
        detail = "; ".join(missing) if missing else "no question directories"
        return False, detail

    # Mark schemes containing a single printed line can be shorter than the
    # generic 80px health threshold. They are source-complete and must proceed
    # to multimodal OCR, while retaining the deterministic warning in the log.
    warnings = result["errors"]
    summary = f"{result['total_questions']} questions"
    if warnings:
        summary += f"; extraction warnings: {'; '.join(warnings)}"
    return True, summary


def run_wave(
    wave_number: int,
    total_waves: int,
    papers: list[dict],
    question_workers: int,
    dry_run: bool,
) -> list[dict]:
    print(f"WAVE {wave_number}/{total_waves}: {', '.join(p['paper_code'] for p in papers)}", flush=True)
    preflight_results = []
    for paper in papers:
        ok, detail = preflight(paper)
        preflight_results.append({"paper_code": paper["paper_code"], "ok": ok, "detail": detail})
        print(f"  PREFLIGHT {'PASS' if ok else 'FAIL'} {paper['paper_code']}: {detail}", flush=True)
    if not all(result["ok"] for result in preflight_results):
        return [{**result, "status": "PREFLIGHT_FAIL" if not result["ok"] else "NOT_STARTED"} for result in preflight_results]
    if dry_run:
        return [{**result, "status": "DRY_RUN"} for result in preflight_results]

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    processes: list[tuple[dict, Path, subprocess.Popen[str], object]] = []
    for paper in papers:
        log_path = REPORT_DIR / f"{paper['paper_code']}.log"
        log_file = log_path.open("w", encoding="utf-8")
        command = [
            sys.executable,
            str(PIPELINE),
            paper["paper_code"],
            "--skip-slice",
            "--no-rebuild-ui",
            "--max-workers",
            str(question_workers),
        ]
        process = subprocess.Popen(
            command,
            cwd=REPO_ROOT,
            stdout=log_file,
            stderr=subprocess.STDOUT,
            text=True,
        )
        processes.append((paper, log_path, process, log_file))

    results = []
    for paper, log_path, process, log_file in processes:
        exit_code = process.wait()
        log_file.close()
        output = log_path.read_text(encoding="utf-8", errors="replace")
        verified = bool(re.search(r"\bVERIFICATION\s*:\s*PASS\b", output))
        status = "PASS" if exit_code == 0 and verified else "FAIL"
        results.append(
            {
                "paper_code": paper["paper_code"],
                "status": status,
                "exit_code": exit_code,
                "verified": verified,
                "log": str(log_path),
            }
        )
        print(f"  {status} {paper['paper_code']} (log: {log_path})", flush=True)
    return results


def rebuild_reviewer_after_verified_year(year: int, results: list[dict]) -> bool:
    """Refresh derived reviewer data only from a fully verified year."""
    if not results or any(result["status"] != "PASS" for result in results):
        print(
            f"REVIEWER REBUILD SKIPPED {year}: year is not fully verified; "
            "failed or immutable-source-blocked records cannot enter derived data.",
            flush=True,
        )
        return False
    if not REVIEWER_BUILD.is_file():
        print(f"REVIEWER REBUILD SKIPPED {year}: build script missing: {REVIEWER_BUILD}", flush=True)
        return False
    subprocess.run([sys.executable, str(REVIEWER_BUILD)], cwd=REPO_ROOT, check=True)
    print(f"REVIEWER REBUILD PASS {year}: all selected papers verified before rebuild.", flush=True)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--batch-size",
        type=int,
        help="Optional explicit paper throttle; omit for one unrestricted all-selected-paper wave",
    )
    parser.add_argument("--question-workers", type=int, default=10)
    parser.add_argument("--include-complete", action="store_true")
    parser.add_argument("--year", type=int, help="Run only one exam year")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.batch_size is not None and args.batch_size < 1:
        parser.error("batch-size must be positive")
    if args.question_workers < 8:
        parser.error("question-workers must be at least 8 so every paper question runs concurrently")

    candidates = get_all_p2_papers(min_year=2016, max_year=2025)
    if args.year is not None:
        candidates = [paper for paper in candidates if paper["year"] == args.year]
    targets = candidates if args.include_complete else [
        paper for paper in candidates if not is_complete(paper["paper_dir"])
    ]
    batch_size = args.batch_size or max(1, len(targets))
    waves = [targets[index:index + batch_size] for index in range(0, len(targets), batch_size)]
    print(f"P2 batch pipeline: {len(targets)} targets in {len(waves)} waves", flush=True)

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    all_results = []
    started = time.time()
    for index, wave in enumerate(waves, 1):
        results = run_wave(index, len(waves), wave, args.question_workers, args.dry_run)
        all_results.extend(results)
        report = {
            "wave": index,
            "total_waves": len(waves),
            "results": results,
            "elapsed_seconds": round(time.time() - started, 2),
        }
        report_scope = str(args.year) if args.year is not None else "all-years"
        report_path = REPORT_DIR / f"{report_scope}_wave_{index:02d}.json"
        temp_path = report_path.with_suffix(".tmp.json")
        temp_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        temp_path.replace(report_path)
        if any(result["status"] != "PASS" for result in results) and not args.dry_run:
            print(f"CONTINUING: wave {index} contains a failed paper; remaining independent papers will still run", flush=True)

    passed = sum(result["status"] == "PASS" for result in all_results)
    print(f"DONE: {passed}/{len(all_results)} papers passed", flush=True)
    if args.dry_run:
        return 0
    if args.year is not None:
        rebuild_reviewer_after_verified_year(args.year, all_results)
    return 0 if passed == len(targets) else 1


if __name__ == "__main__":
    raise SystemExit(main())
