#!/usr/bin/env python3
"""Unified CLI Verification Suite Coordinator for Cambridge Physics 9702 Past Papers.

Runs 4 deterministic layers of validation across Physics papers:
1. Assets & Structure: Core files, image health, diagrams, manifest sync.
2. Marks Reconciliation: Subpart marks vs total marks, QP vs MS parity, paper totals (P1: 40, P2: 60, P4: 100).
3. Content & Syntax: Subpart alignment, LaTeX/KaTeX math delimiter and brace balance.
4. Enrichment Quality: Walkthrough completeness, progressive scaffolding hints, skills & definitions matching knowledge-base.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
import json
from pathlib import Path
import re
import sys
import time

# Ensure scripts directory is in sys.path
SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from verify_physics_paper_assets import verify_physics_paper_assets
from verify_physics_marks import verify_physics_marks_for_paper
from verify_physics_content_syntax import verify_physics_content_syntax_for_paper
from verify_physics_enrichment import verify_physics_enrichment_for_paper, load_physics_valid_ids

REPO_ROOT = next((p for p in Path(__file__).resolve().parents if (p / "subjects").is_dir() and (p / "pyproject.toml").is_file()), Path(__file__).resolve().parents[2])
PHYSICS_PAPERS_ROOT = REPO_ROOT / "subjects/physics/9702/past papers"


def verify_full_paper(
    paper_dir: Path,
    fix: bool = False,
    skip_enrichment: bool = False,
    skip_ocr: bool = False,
) -> list[dict]:
    """Execute all verification layers for a single Physics paper."""
    all_issues = []

    # Layer 1: Marks Reconciliation
    marks_issues = verify_physics_marks_for_paper(paper_dir, fix=fix)
    all_issues.extend(marks_issues)

    # Layer 2: Asset & Image Health
    assets_issues = verify_physics_paper_assets(paper_dir, fix=fix)
    all_issues.extend(assets_issues)

    # Layer 3: Content Syntax & Delimiters
    syntax_issues = verify_physics_content_syntax_for_paper(paper_dir, fix=fix)
    all_issues.extend(syntax_issues)

    # Layer 4: Pedagogical Quality & Triangulation
    if not skip_enrichment:
        try:
            valid_skills, valid_defs = load_physics_valid_ids()
        except Exception:
            valid_skills, valid_defs = set(), set()
        enrichment_issues = verify_physics_enrichment_for_paper(
            paper_dir, valid_skill_ids=valid_skills, valid_defs=valid_defs, fix=fix
        )
        all_issues.extend(enrichment_issues)

    # Layer 5: OCR Structure & Table/KaTeX Fidelity
    if not skip_ocr:
        try:
            try:
                from p2.audit_physics_ocr_structure import audit_paper_ocr
            except ImportError:
                from audit_physics_ocr_structure import audit_paper_ocr
            ocr_struct_results = audit_paper_ocr(paper_dir)
            for q_name, issues in ocr_struct_results.items():
                for iss in issues:
                    all_issues.append({
                        "paper": paper_dir.name,
                        "file": q_name,
                        "category": f"ocr_structure_{iss['category']}",
                        "level": iss["level"],
                        "message": iss["message"],
                    })
        except Exception:
            pass

    return all_issues


def run_verification(
    component: str = "all",
    paper_filter: str | None = None,
    year_filter: int | None = None,
    selected_checks: list[str] | None = None,
    fix: bool = False,
) -> tuple[dict, list[dict]]:
    valid_checks = {"assets", "marks", "syntax", "enrichment"}
    checks_to_run = set(selected_checks) if selected_checks else valid_checks

    components = ["p1", "p2", "p4"] if component == "all" else [component]
    paper_dirs: list[tuple[str, Path]] = []

    for comp in components:
        comp_dir = PHYSICS_PAPERS_ROOT / comp
        if not comp_dir.is_dir():
            continue
        discovered: list[tuple[str, Path, int | None]] = []
        for qp in sorted(comp_dir.rglob("*_qp_*.pdf")):
            p_dir = qp.parent.parent
            m = re.match(r"^(9702_[msw](\d{2}))_qp_(\d{2})$", qp.stem, re.I)
            code = f"{m.group(1).lower()}_{m.group(3)}" if m else p_dir.name
            yr = 2000 + int(m.group(2)) if m else None
            discovered.append((code, p_dir, yr))

        seen_dirs = {p for _, p, _ in discovered}
        for qd in sorted(comp_dir.rglob("question_01")):
            cand = qd.parent
            if cand not in seen_dirs:
                yr = None
                for part in cand.parts:
                    if re.match(r"^20\d{2}$", part):
                        yr = int(part)
                        break
                discovered.append((cand.name, cand, yr))
                seen_dirs.add(cand)

        for p_code, p_dir, yr in discovered:
            if year_filter and yr != year_filter:
                continue
            if paper_filter:
                pf = paper_filter.lower()
                if pf not in p_code.lower() and pf not in p_dir.name.lower() and pf not in str(p_dir).lower():
                    continue
            paper_dirs.append((p_code, p_dir))

    all_issues = []
    paper_results = {}
    valid_skills, valid_defs = (load_physics_valid_ids() if "enrichment" in checks_to_run else (set(), set()))

    start_time = time.time()

    for p_code, p_dir in paper_dirs:
        paper_issues = []

        if "assets" in checks_to_run:
            paper_issues.extend(verify_physics_paper_assets(p_dir, fix=fix))
        if "marks" in checks_to_run:
            paper_issues.extend(verify_physics_marks_for_paper(p_dir, fix=fix))
        if "syntax" in checks_to_run:
            paper_issues.extend(verify_physics_content_syntax_for_paper(p_dir, fix=fix))
        if "enrichment" in checks_to_run:
            paper_issues.extend(
                verify_physics_enrichment_for_paper(
                    p_dir, valid_skill_ids=valid_skills, valid_defs=valid_defs, fix=fix
                )
            )

        for iss in paper_issues:
            if iss.get("paper") == p_dir.name and p_code != p_dir.name:
                iss["paper"] = p_code

        p_errors = [i for i in paper_issues if i["level"] == "ERROR"]
        p_warnings = [i for i in paper_issues if i["level"] == "WARNING"]

        status = "FAIL" if p_errors else ("WARN" if p_warnings else "PASS")
        paper_results[p_code] = {
            "status": status,
            "error_count": len(p_errors),
            "warning_count": len(p_warnings),
            "issues": paper_issues,
        }
        all_issues.extend(paper_issues)

    elapsed = time.time() - start_time

    summary = {
        "total_papers": len(paper_dirs),
        "pass_count": sum(1 for r in paper_results.values() if r["status"] == "PASS"),
        "warn_count": sum(1 for r in paper_results.values() if r["status"] == "WARN"),
        "fail_count": sum(1 for r in paper_results.values() if r["status"] == "FAIL"),
        "total_errors": sum(r["error_count"] for r in paper_results.values()),
        "total_warnings": sum(r["warning_count"] for r in paper_results.values()),
        "elapsed_seconds": round(elapsed, 2),
    }

    return summary, all_issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--component", choices=["p1", "p2", "p4", "all"], default="all")
    parser.add_argument("--paper", help="Specific paper code or name")
    parser.add_argument("--year", type=int, help="Specific exam year (e.g. 2023)")
    parser.add_argument("--checks", nargs="+", choices=["assets", "marks", "syntax", "enrichment"])
    parser.add_argument("--fix", action="store_true", help="Auto-fix repairable defects")
    parser.add_argument("--report-json", type=Path, help="Save structured report to JSON file")
    args = parser.parse_args()

    summary, all_issues = run_verification(
        component=args.component,
        paper_filter=args.paper,
        year_filter=args.year,
        selected_checks=args.checks,
        fix=args.fix,
    )

    print("=" * 80)
    print(f"PHYSICS 9702 VERIFICATION ({'AUTO-FIX' if args.fix else 'CHECK'} MODE)")
    print(f"Papers Checked:   {summary['total_papers']}")
    print(f"  Passed Clean:   {summary['pass_count']}")
    print(f"  With Warnings:  {summary['warn_count']}")
    print(f"  With Errors:    {summary['fail_count']}")
    print(f"Total Errors:     {summary['total_errors']}")
    print(f"Total Warnings:   {summary['total_warnings']}")
    print("=" * 80)

    if summary["total_errors"] > 0:
        print("\nFailures / Errors:")
        errors = [i for i in all_issues if i["level"] == "ERROR"]
        for iss in errors[:30]:
            print(f"  ❌ [{iss.get('paper')}] {iss.get('question') or ''} ({iss.get('category')}): {iss.get('message')}")
        if len(errors) > 30:
            print(f"  ... and {len(errors) - 30} more errors.")
        print()

    if args.report_json:
        report = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "summary": summary,
            "issues": all_issues,
        }
        with open(args.report_json, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"Report saved to: {args.report_json}")

    sys.exit(1 if summary["total_errors"] > 0 else 0)


if __name__ == "__main__":
    main()
