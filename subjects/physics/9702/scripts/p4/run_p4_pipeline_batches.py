#!/usr/bin/env python3
"""Run P4 derived AI processing in unrestricted, question-parallel waves.

Slicing is excluded. Each process performs only additive AI work and P4 source
verification. A failed paper is recorded but never stops later independent waves.
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

from batch_slice_p4 import audit_paper_assets, get_all_p4_papers

REPO_ROOT = next(
    (path for path in Path(__file__).resolve().parents if (path / "subjects").is_dir() and (path / "pyproject.toml").is_file()),
    Path(__file__).resolve().parents[4],
)
PIPELINE = SCRIPT_DIR / "process_p4_paper.py"
REPORT_DIR = REPO_ROOT / "artifacts/physics/p4/batch-pipeline"
REQUIRED = ("question_ocr.json", "markscheme.json", "markscheme_review_meta.json", "question_ocr_review_meta.json", "enrichment.json", "enrichment_meta.json")


def is_complete(paper_dir: Path) -> bool:
    q_dirs = sorted(path for path in paper_dir.glob("question_*") if path.is_dir())
    if not q_dirs:
        return False
    for q_dir in q_dirs:
        if not all((q_dir / name).is_file() for name in REQUIRED):
            return False
        try:
            meta = json.loads((q_dir / "markscheme_review_meta.json").read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return False
        if meta.get("status") != "PASS":
            return False
    return True


def preflight(paper: dict) -> tuple[bool, str]:
    ok, detail, count, _assets = audit_paper_assets(paper["paper_dir"])
    return ok, f"{count} questions; {detail}"


def run_wave(index: int, total: int, papers: list[dict], workers: int, dry_run: bool) -> list[dict]:
    print(f"WAVE {index}/{total}: {', '.join(paper['paper_code'] for paper in papers)}", flush=True)
    checks = [{"paper_code": paper["paper_code"], "ok": preflight(paper)[0], "detail": preflight(paper)[1]} for paper in papers]
    for check in checks:
        print(f"  PREFLIGHT {'PASS' if check['ok'] else 'FAIL'} {check['paper_code']}: {check['detail']}", flush=True)
    if dry_run or not all(check["ok"] for check in checks):
        return [{**check, "status": "DRY_RUN" if dry_run else "PREFLIGHT_FAIL"} for check in checks]

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    started = []
    for paper in papers:
        log = REPORT_DIR / f"{paper['paper_code']}.log"
        handle = log.open("w", encoding="utf-8")
        process = subprocess.Popen([sys.executable, str(PIPELINE), paper["paper_code"], "--max-workers", str(workers)], cwd=REPO_ROOT, stdout=handle, stderr=subprocess.STDOUT, text=True)
        started.append((paper, log, process, handle))
    results = []
    for paper, log, process, handle in started:
        exit_code = process.wait()
        handle.close()
        output = log.read_text(encoding="utf-8", errors="replace")
        passed = exit_code == 0 and bool(re.search(r"\bVERIFICATION\s*:\s*PASS\b", output))
        result = {"paper_code": paper["paper_code"], "status": "PASS" if passed else "FAIL", "exit_code": exit_code, "log": str(log)}
        results.append(result)
        print(f"  {result['status']} {paper['paper_code']} (log: {log})", flush=True)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--year", type=int)
    parser.add_argument("--batch-size", type=int, default=0, help="Papers per wave; 0 runs every selected paper together")
    parser.add_argument("--question-workers", type=int, default=14)
    parser.add_argument("--include-complete", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.batch_size < 0:
        parser.error("batch-size must be zero or a positive integer")
    if args.question_workers < 13:
        parser.error("question-workers must be at least 13 so every P4 question can run concurrently")

    papers = get_all_p4_papers()
    if args.year is not None:
        papers = [paper for paper in papers if paper["year"] == args.year]
    targets = papers if args.include_complete else [paper for paper in papers if not is_complete(paper["paper_dir"])]
    batch_size = len(targets) if args.batch_size == 0 else args.batch_size
    waves = [targets[i:i + batch_size] for i in range(0, len(targets), batch_size)] if targets else []
    print(f"P4 batch pipeline: {len(targets)} targets in {len(waves)} waves", flush=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    all_results = []
    started = time.time()
    scope = str(args.year) if args.year is not None else "all-years"
    for index, wave in enumerate(waves, 1):
        results = run_wave(index, len(waves), wave, args.question_workers, args.dry_run)
        all_results.extend(results)
        (REPORT_DIR / f"{scope}_wave_{index:02d}.json").write_text(json.dumps({"wave": index, "total_waves": len(waves), "results": results, "elapsed_seconds": round(time.time() - started, 2)}, indent=2) + "\n", encoding="utf-8")
    passed = sum(result["status"] == "PASS" for result in all_results)
    print(f"DONE: {passed}/{len(all_results)} papers passed", flush=True)
    return 0 if args.dry_run or passed == len(targets) else 1


if __name__ == "__main__":
    raise SystemExit(main())
