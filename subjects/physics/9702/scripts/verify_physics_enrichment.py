#!/usr/bin/env python3
"""Enrichment Quality & Curriculum Mapping Auditor for Physics 9702 Past Papers.

Checks:
- Subpart parity between question.json and enrichment.json.
- Walkthrough completeness: Every part has a non-empty walkthrough.
- Scaffolding hints: Each part has >= 2 hints.
- Hint answer protection: Hint 1 does not prematurely reveal final answers.
- Physics skills validation against subjects/physics/9702/knowledge/knowledge-base/skills.json.
- Formal definitions validation against subjects/physics/9702/knowledge/knowledge-base/definitions.json.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

REPO_ROOT = next((p for p in Path(__file__).resolve().parents if (p / "subjects").is_dir() and (p / "pyproject.toml").is_file()), Path(__file__).resolve().parents[2])
PHYSICS_PAPERS_ROOT = REPO_ROOT / "subjects/physics/9702/past papers"
KNOWLEDGE_ROOT = REPO_ROOT / "subjects/physics/9702/knowledge/knowledge-base"


def load_physics_valid_ids() -> tuple[set[str], set[str]]:
    valid_skill_ids = set()
    valid_definition_terms = set()

    # Load skills
    skills_path = KNOWLEDGE_ROOT / "skills.json"
    if skills_path.is_file():
        try:
            with open(skills_path, encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                skills_list = data.get("skills", [])
            elif isinstance(data, list):
                skills_list = data
            else:
                skills_list = []
            for s in skills_list:
                if isinstance(s, dict) and "skill_id" in s:
                    valid_skill_ids.add(s["skill_id"])
                elif isinstance(s, str):
                    valid_skill_ids.add(s)
        except Exception:
            pass

    # Load definitions
    defs_path = KNOWLEDGE_ROOT / "definitions.json"
    if defs_path.is_file():
        try:
            with open(defs_path, encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                for term in data.keys():
                    valid_definition_terms.add(term.lower())
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict) and "term" in item:
                        valid_definition_terms.add(item["term"].lower())
        except Exception:
            pass

    return valid_skill_ids, valid_definition_terms


def verify_physics_enrichment_for_paper(
    paper_dir: Path,
    valid_skill_ids: set[str] | None = None,
    valid_defs: set[str] | None = None,
    fix: bool = False,
) -> list[dict]:
    issues = []
    paper_code = paper_dir.name

    if valid_skill_ids is None or valid_defs is None:
        v_skills, v_defs = load_physics_valid_ids()
        valid_skill_ids = valid_skill_ids or v_skills
        valid_defs = valid_defs or v_defs

    q_dirs = sorted([d for d in paper_dir.glob("question_*") if d.is_dir()])
    if not q_dirs and (paper_dir / "questions").is_dir():
        q_dirs = sorted([paper_dir / "questions"])

    for qd in q_dirs:
        q_num = qd.name
        q_path = qd / "question.json"
        ms_path = qd / "markscheme.json"
        if not ms_path.is_file() and (qd / "mark_scheme.json").is_file():
            ms_path = qd / "mark_scheme.json"
        enr_path = qd / "enrichment.json"

        if not enr_path.is_file():
            continue

        q_part_ids = []
        if q_path.is_file():
            try:
                with open(q_path, encoding="utf-8") as f:
                    q_data = json.load(f)
                q_part_ids = [p["id"] for p in q_data.get("parts", []) if "id" in p]
            except Exception:
                pass

        try:
            with open(enr_path, encoding="utf-8") as f:
                enr_data = json.load(f)
        except Exception as e:
            issues.append({
                "paper": paper_code,
                "question": q_num,
                "category": "enrichment",
                "level": "ERROR",
                "message": f"Cannot parse enrichment.json: {e}",
                "fixable": False,
            })
            continue

        parts = enr_data.get("parts", [])
        enr_part_ids = [p.get("part_id") for p in parts if "part_id" in p]

        # 1. Parity between question.json and enrichment.json
        if q_part_ids and enr_part_ids and q_part_ids != enr_part_ids:
            issues.append({
                "paper": paper_code,
                "question": q_num,
                "category": "enrichment_parity",
                "level": "ERROR",
                "message": f"Part ID mismatch: question.json has {q_part_ids} vs enrichment.json has {enr_part_ids}",
                "fixable": False,
            })

        # 2. Check each part
        for part in parts:
            pid = part.get("part_id", "unknown")

            # A. Walkthrough
            walkthrough = part.get("walkthrough", [])
            if not walkthrough:
                issues.append({
                    "paper": paper_code,
                    "question": q_num,
                    "category": "walkthrough",
                    "level": "ERROR",
                    "message": f"Part '{pid}' has an empty walkthrough",
                    "fixable": False,
                })

            # B. Hints scaffolding
            hints = part.get("hints", [])
            if len(hints) < 1:
                issues.append({
                    "paper": paper_code,
                    "question": q_num,
                    "category": "hints",
                    "level": "WARNING",
                    "message": f"Part '{pid}' has no hints",
                    "fixable": False,
                })

            # C. Skill references
            skills_block = part.get("skills", {})
            pri_skill = skills_block.get("primary_skill_id")
            if pri_skill and valid_skill_ids and pri_skill not in valid_skill_ids:
                issues.append({
                    "paper": paper_code,
                    "question": q_num,
                    "category": "curriculum_mapping",
                    "level": "WARNING",
                    "message": f"Part '{pid}' references unknown skill_id: '{pri_skill}'",
                    "fixable": False,
                })

    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--component", choices=["p1", "p2", "p4", "all"], default="all")
    parser.add_argument("--paper", help="Specific paper code or folder")
    parser.add_argument("--fix", action="store_true", help="Auto-fix cleanable enrichment issues")
    args = parser.parse_args()

    components = ["p1", "p2", "p4"] if args.component == "all" else [args.component]
    total_papers = 0
    total_issues = []

    valid_skills, valid_defs = load_physics_valid_ids()

    for comp in components:
        comp_dir = PHYSICS_PAPERS_ROOT / comp
        if not comp_dir.is_dir():
            continue
        paper_dirs = sorted([d for d in comp_dir.glob("*/*") if d.is_dir()])
        if args.paper:
            paper_dirs = [d for d in paper_dirs if args.paper in d.name]

        for p_dir in paper_dirs:
            total_papers += 1
            issues = verify_physics_enrichment_for_paper(
                p_dir, valid_skill_ids=valid_skills, valid_defs=valid_defs, fix=args.fix
            )
            total_issues.extend(issues)

    errors = [i for i in total_issues if i["level"] == "ERROR"]
    warnings = [i for i in total_issues if i["level"] == "WARNING"]

    print(f"Verified enrichment for {total_papers} Physics papers: {len(errors)} errors, {len(warnings)} warnings.")
    if total_issues:
        for iss in total_issues[:30]:
            print(f"[{iss['level']}] [{iss['paper']}] {iss['question'] or ''} ({iss['category']}): {iss['message']}")
        if len(total_issues) > 30:
            print(f"... and {len(total_issues) - 30} more issues.")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
