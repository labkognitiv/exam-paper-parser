#!/usr/bin/env python3
"""Force-regenerate Physics 9702 P1 enrichment one fully-validated year at a time.

All P1 papers in a year start together. Each child invokes the enricher with 40
question workers. The next year never starts unless every selected paper in the
current year both exits cleanly and passes deterministic validation.
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
PHYSICS_ROOT = SCRIPT_DIR.parents[1]
REPO_ROOT = next(
    (parent for parent in Path(__file__).resolve().parents if (parent / "subjects").is_dir()),
    PHYSICS_ROOT.parents[1],
)
P1_ROOT = PHYSICS_ROOT / "9702" / "past papers" / "p1"
ENRICHER = SCRIPT_DIR / "enrich_physics_mcqs.py"
VALIDATOR = REPO_ROOT / "scripts" / "validate_p1_enrichment.py"
REPORT_DIR = REPO_ROOT / "artifacts" / "physics" / "p1" / "enrichment-runs"
QUESTION_RE = re.compile(r"question_(\d{2})\.json$")


def paper_code(package: Path) -> str:
    question = package / "question_01.json"
    data = json.loads(question.read_text(encoding="utf-8"))
    code = data.get("paper_code")
    if not isinstance(code, str) or not re.fullmatch(r"9702_[msw]\d{2}_1\d", code):
        raise ValueError(f"Invalid P1 paper code in {question}")
    return code


def discover(year: int) -> list[dict]:
    papers = []
    for package in sorted((P1_ROOT / str(year)).rglob("question-package")):
        papers.append({"paper_code": paper_code(package), "package": package})
    return sorted(papers, key=lambda item: item["paper_code"])


def preflight(paper: dict) -> tuple[bool, str]:
    package = paper["package"]
    questions = sorted(path for path in package.glob("question_*.json") if QUESTION_RE.fullmatch(path.name))
    if len(questions) != 40:
        return False, f"expected 40 canonical question JSON files, found {len(questions)}"
    try:
        answers = json.loads((package / "answer_key.json").read_text(encoding="utf-8")).get("answers")
    except (OSError, json.JSONDecodeError) as error:
        return False, f"unreadable answer_key.json: {error}"
    if not isinstance(answers, dict) or set(answers) != {str(number) for number in range(1, 41)}:
        return False, "answer_key.json does not contain exactly questions 1-40"
    for question_path in questions:
        data = json.loads(question_path.read_text(encoding="utf-8"))
        number = int(QUESTION_RE.fullmatch(question_path.name).group(1))
        image = package / data.get("question_image", f"question_{number:02d}.png")
        if not image.is_file() or image.stat().st_size == 0:
            return False, f"missing or empty authentic image {image.name}"
    return True, "40 canonical questions, answer key, and images"


def strict_options_check(paper_code_value: str) -> list[str]:
    """Enforce the final-regeneration requirement beyond legacy schema validity."""
    year = f"20{paper_code_value.split('_')[1][1:]}"
    session = {"m": "february-march", "s": "may-june", "w": "october-november"}[paper_code_value.split("_")[1][0]]
    variant = f"variant-{paper_code_value.split('_')[2][1]}"
    enrich_dir = P1_ROOT / year / session / variant / "enrichment"
    errors = []
    for number in range(1, 41):
        path = enrich_dir / f"{paper_code_value}_q{number:02d}.enrichment.json"
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            errors.append(f"q{number:02d}: unreadable enrichment: {error}")
            continue
        breakdown = data.get("options_breakdown")
        if not isinstance(breakdown, dict) or set(breakdown) != {"A", "B", "C", "D"}:
            errors.append(f"q{number:02d}: options_breakdown must contain exactly A-D")
    return errors


def incomplete_questions(paper_code_value: str) -> list[int]:
    """Return only records that were not successfully promoted in this run."""
    year = f"20{paper_code_value.split('_')[1][1:]}"
    session = {"m": "february-march", "s": "may-june", "w": "october-november"}[paper_code_value.split("_")[1][0]]
    variant = f"variant-{paper_code_value.split('_')[2][1]}"
    enrich_dir = P1_ROOT / year / session / variant / "enrichment"
    incomplete = []
    for number in range(1, 41):
        path = enrich_dir / f"{paper_code_value}_q{number:02d}.enrichment.json"
        try:
            breakdown = json.loads(path.read_text(encoding="utf-8")).get("options_breakdown")
        except (OSError, json.JSONDecodeError):
            incomplete.append(number)
            continue
        if not isinstance(breakdown, dict) or set(breakdown) != {"A", "B", "C", "D"}:
            incomplete.append(number)
    return incomplete


def validate(paper_code_value: str, log_path: Path, exit_code: int) -> tuple[str, list[str]]:
    validation = subprocess.run(
        [sys.executable, str(VALIDATOR), "--paper", paper_code_value, "--json"],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write("\n--- deterministic validation ---\n")
        handle.write(validation.stdout)
        if validation.stderr:
            handle.write(validation.stderr)
    errors = strict_options_check(paper_code_value)
    try:
        report = json.loads(validation.stdout)
        errors.extend(report.get("deterministic_errors", []))
    except json.JSONDecodeError:
        errors.append("validator did not emit readable JSON")
    if exit_code != 0:
        errors.insert(0, f"enricher exited {exit_code}")
    if validation.returncode != 0:
        errors.insert(0, f"validator exited {validation.returncode}")
    return ("PASS" if not errors else "FAIL"), errors


def run_year(year: int) -> dict:
    papers = discover(year)
    report = {"year": year, "papers": [], "status": "FAIL"}
    if not papers:
        report["error"] = "no P1 paper packages discovered"
        return report
    checks = [(paper, *preflight(paper)) for paper in papers]
    if not all(ok for _paper, ok, _detail in checks):
        report["papers"] = [
            {"paper_code": paper["paper_code"], "status": "PREFLIGHT_FAIL" if not ok else "NOT_STARTED", "detail": detail}
            for paper, ok, detail in checks
        ]
        return report

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    started = []
    for paper, _ok, detail in checks:
        log = REPORT_DIR / f"{paper['paper_code']}.log"
        handle = log.open("w", encoding="utf-8")
        process = subprocess.Popen(
            [sys.executable, str(ENRICHER), paper["paper_code"], "--force", "--max-workers", "40", "--json"],
            cwd=REPO_ROOT,
            stdout=handle,
            stderr=subprocess.STDOUT,
            text=True,
        )
        started.append((paper, detail, log, handle, process))

    for paper, detail, log, handle, process in started:
        exit_code = process.wait()
        handle.close()
        status, errors = validate(paper["paper_code"], log, exit_code)
        report["papers"].append(
            {
                "paper_code": paper["paper_code"],
                "status": status,
                "preflight": detail,
                "exit_code": exit_code,
                "errors": errors,
                "log": str(log),
            }
        )
        print(f"  {status} {paper['paper_code']}", flush=True)
    report["status"] = "PASS" if all(item["status"] == "PASS" for item in report["papers"]) else "FAIL"
    return report


def resume_year(year: int) -> dict:
    """Retry only unpromoted questions, then rewrite the year report."""
    papers = discover(year)
    report = {"year": year, "resumed": True, "papers": [], "status": "FAIL"}
    if not papers:
        report["error"] = "no P1 paper packages discovered"
        return report
    retry_jobs = []
    retry_targets: dict[str, list[int]] = {}
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    for paper in papers:
        ok, detail = preflight(paper)
        if not ok:
            report["papers"].append({"paper_code": paper["paper_code"], "status": "PREFLIGHT_FAIL", "detail": detail})
            continue
        retry_targets[paper["paper_code"]] = incomplete_questions(paper["paper_code"])
        for number in retry_targets[paper["paper_code"]]:
            log = REPORT_DIR / f"{paper['paper_code']}_q{number:02d}.retry.log"
            handle = log.open("w", encoding="utf-8")
            process = subprocess.Popen(
                [
                    sys.executable,
                    str(ENRICHER),
                    paper["paper_code"],
                    "--question",
                    str(number),
                    "--force",
                    "--max-workers",
                    "40",
                    "--max-tokens",
                    "5000",
                    "--json",
                ],
                cwd=REPO_ROOT,
                stdout=handle,
                stderr=subprocess.STDOUT,
                text=True,
            )
            retry_jobs.append((paper["paper_code"], number, log, handle, process))
    for paper_code_value, number, log, handle, process in retry_jobs:
        exit_code = process.wait()
        handle.close()
        print(f"  RETRY {'PASS' if exit_code == 0 else 'FAIL'} {paper_code_value} q{number:02d}", flush=True)
    for paper in papers:
        code = paper["paper_code"]
        log = REPORT_DIR / f"{code}.log"
        exit_code = 0
        errors = []
        if any(item.get("paper_code") == code and item["status"] == "PREFLIGHT_FAIL" for item in report["papers"]):
            continue
        for retry_code, number, retry_log, _handle, process in retry_jobs:
            if retry_code == code and process.returncode != 0:
                errors.append(f"retry q{number:02d} exited {process.returncode}; log: {retry_log}")
        status, validation_errors = validate(code, log, exit_code)
        errors.extend(validation_errors)
        report["papers"].append(
            {
                "paper_code": code,
                "status": "PASS" if not errors else "FAIL",
                "retried_questions": retry_targets[code],
                "errors": errors,
                "log": str(log),
            }
        )
        print(f"  {'PASS' if not errors else 'FAIL'} {code}", flush=True)
    report["status"] = "PASS" if len(report["papers"]) == len(papers) and all(item["status"] == "PASS" for item in report["papers"]) else "FAIL"
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--from-year", type=int, default=2025)
    parser.add_argument("--to-year", type=int, default=2016)
    parser.add_argument("--resume-year", type=int, help="Retry only incomplete questions in one stopped year")
    args = parser.parse_args()
    if args.from_year < args.to_year:
        parser.error("--from-year must be greater than or equal to --to-year")

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    started = time.time()
    if args.resume_year is not None:
        print(f"YEAR {args.resume_year}: retrying only incomplete questions", flush=True)
        report = resume_year(args.resume_year)
        report["elapsed_seconds"] = round(time.time() - started, 2)
        report_path = REPORT_DIR / f"{args.resume_year}.json"
        temporary = report_path.with_suffix(".tmp.json")
        temporary.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        temporary.replace(report_path)
        print(f"YEAR {args.resume_year}: {report['status']}", flush=True)
        return 0 if report["status"] == "PASS" else 1
    for year in range(args.from_year, args.to_year - 1, -1):
        print(f"YEAR {year}: starting all P1 papers concurrently", flush=True)
        report = run_year(year)
        report["elapsed_seconds"] = round(time.time() - started, 2)
        report_path = REPORT_DIR / f"{year}.json"
        temporary = report_path.with_suffix(".tmp.json")
        temporary.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        temporary.replace(report_path)
        print(f"YEAR {year}: {report['status']}", flush=True)
        if report["status"] != "PASS":
            print(f"STOPPED: {year} did not fully pass; no earlier year was started.", flush=True)
            return 1
    print("DONE: 2025 through 2016 all passed", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
