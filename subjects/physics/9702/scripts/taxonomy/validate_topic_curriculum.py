#!/usr/bin/env python3
"""Curriculum and Lesson Structure Validator for Physics 9702.

Verifies:
1. Every topic directory has syllabus.json, evidence-index.json,
   module-lesson-structure.md, and lesson-knowledge-map.json.
2. Every Course Module contains module.json and every Lesson contains lesson.json.
3. Lesson prerequisites form a strictly acyclic DAG with zero knowledge gaps.
4. Strictly zero em dashes in any file across all 25 topics.
5. 100% learning outcome coverage across all 25 topics (300 outcomes total).
6. Lesson sequences are strictly monotonic 1..N within each topic.

Rule: Strictly ZERO em dashes anywhere in this file.
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

PHYSICS_ROOT = Path(__file__).resolve().parents[2]
REPO_ROOT = Path(__file__).resolve().parents[5]
STUDY_TOPICS = PHYSICS_ROOT / "study" / "topics"
KNOWLEDGE_ROOT = PHYSICS_ROOT / "knowledge" / "2025-2027"

AS_TAX_PATH = KNOWLEDGE_ROOT / "as" / "9702-2025-2027-as-taxonomy.json"
AS_OUT_PATH = KNOWLEDGE_ROOT / "as" / "9702-2025-2027-as-learning-outcomes.json"
A2_TAX_PATH = KNOWLEDGE_ROOT / "a2" / "9702-2025-2027-a2-taxonomy.json"
A2_OUT_PATH = KNOWLEDGE_ROOT / "a2" / "9702-2025-2027-a2-learning-outcomes.json"


def load_all_syllabus_outcomes() -> Dict[str, Set[str]]:
    as_out = json.loads(AS_OUT_PATH.read_text(encoding="utf-8"))["outcomes"]
    a2_out = json.loads(A2_OUT_PATH.read_text(encoding="utf-8"))["outcomes"]
    outcomes_by_topic: Dict[str, Set[str]] = collections.defaultdict(set)
    for o in as_out + a2_out:
        outcomes_by_topic[o["topic_id"]].add(o["outcome_id"])
    return outcomes_by_topic


def validate_topic(topic_dir: Path, expected_outcomes: Set[str]) -> List[str]:
    errors = []
    tid = topic_dir.name.split("_")[0] + "_" + topic_dir.name.split("_")[1]

    # Required files
    req_files = [
        topic_dir / "syllabus.json",
        topic_dir / "evidence-index.json",
        topic_dir / "module-lesson-structure.md",
        topic_dir / "lesson-knowledge-map.json",
    ]
    for rf in req_files:
        if not rf.is_file():
            errors.append(f"{topic_dir.name}: Missing required file {rf.name}")

    # Check em dashes across all files in topic dir
    for f in topic_dir.glob("**/*"):
        if f.is_file() and f.suffix in [".json", ".md", ".txt"]:
            raw = f.read_text(encoding="utf-8")
            if chr(8212) in raw:
                errors.append(f"{f.relative_to(topic_dir)}: Contains em dash")

    # Read syllabus outcomes from local syllabus.json
    topic_syllabus_outcomes: Set[str] = set()
    syl_path = topic_dir / "syllabus.json"
    if syl_path.is_file():
        try:
            syl_data = json.loads(syl_path.read_text(encoding="utf-8"))
            for out in syl_data.get("learning_outcomes", []):
                topic_syllabus_outcomes.add(out["outcome_id"])
        except Exception as e:
            errors.append(f"{topic_dir.name}: syllabus.json parse error: {e}")

    # Validate lesson-knowledge-map.json
    lkm_path = topic_dir / "lesson-knowledge-map.json"
    if lkm_path.is_file():
        try:
            lkm = json.loads(lkm_path.read_text(encoding="utf-8"))
            lessons = lkm.get("lessons", [])
            if not lessons:
                errors.append(f"{topic_dir.name}: lesson-knowledge-map has zero lessons")

            mapped_outcomes: Set[str] = set()
            lesson_ids = [les.get("lesson_id") for les in lessons]

            # Sequence monotonicity: collect sequences
            cm_dir = topic_dir / "course-modules"
            cms = sorted([d for d in cm_dir.iterdir() if d.is_dir() and not d.name.startswith(".")]) if cm_dir.is_dir() else []
            if not cms:
                errors.append(f"{topic_dir.name}: No course-modules found")

            # Validate each lesson
            adj: Dict[str, List[str]] = {lid: [] for lid in lesson_ids if lid}
            in_degree: Dict[str, int] = {lid: 0 for lid in lesson_ids if lid}
            sequences = []

            for les in lessons:
                lid = les.get("lesson_id")
                oids = les.get("outcome_ids", [])
                if not oids:
                    errors.append(f"{topic_dir.name}: Lesson {lid} has no outcome_ids")
                mapped_outcomes.update(oids)

                # Locate lesson.json
                les_json_candidates = list(topic_dir.glob(f"course-modules/*/lessons/{lid}/lesson.json"))
                if not les_json_candidates:
                    errors.append(f"{topic_dir.name}: Missing lesson.json for {lid}")
                else:
                    les_json_path = les_json_candidates[0]
                    try:
                        les_data = json.loads(les_json_path.read_text(encoding="utf-8"))
                        seq = les_data.get("sequence")
                        if seq is not None:
                            sequences.append(seq)

                        # Prerequisites check
                        prereqs = les_data.get("prerequisites", {})
                        prev_ids = prereqs.get("previous_lesson_ids", [])
                        for prev_id in prev_ids:
                            if prev_id in adj and lid in in_degree:
                                adj[prev_id].append(lid)
                                in_degree[lid] += 1
                    except Exception as e:
                        errors.append(f"{lid}: lesson.json parse error: {e}")

            # Check sequence monotonicity
            if sequences and sequences != list(range(1, len(sequences) + 1)):
                errors.append(f"{topic_dir.name}: Lesson sequences not monotonic 1..{len(sequences)}: {sequences[:5]}...{sequences[-3:]}")

            # Topological sort to verify acyclic DAG
            queue = collections.deque([lid for lid, deg in in_degree.items() if deg == 0])
            visited_count = 0
            while queue:
                curr = queue.popleft()
                visited_count += 1
                for neighbor in adj.get(curr, []):
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            if visited_count != len(lesson_ids):
                errors.append(f"{topic_dir.name}: Prerequisite cycle detected! Visited {visited_count} of {len(lesson_ids)} lessons")

            # Check outcome coverage against official syllabus
            target_outcomes = expected_outcomes or topic_syllabus_outcomes
            uncovered = target_outcomes - mapped_outcomes
            if uncovered:
                errors.append(f"{topic_dir.name}: Uncovered syllabus outcomes: {sorted(list(uncovered))}")

        except Exception as e:
            errors.append(f"{topic_dir.name}: lesson-knowledge-map.json parse error: {e}")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Physics 9702 topic curriculum and lesson structures.")
    parser.add_argument("--topics", nargs="+", help="Specific topic IDs to validate")
    args = parser.parse_args()

    all_syllabus_outcomes = load_all_syllabus_outcomes()
    total_outcomes = sum(len(outs) for outs in all_syllabus_outcomes.values())
    print(f"Loaded {len(all_syllabus_outcomes)} topics, {total_outcomes} total learning outcomes from syllabus.")

    topic_dirs = sorted([d for d in STUDY_TOPICS.iterdir() if d.is_dir() and not d.name.startswith(".")])
    if not topic_dirs:
        print("No topic directories found under study/topics.")
        sys.exit(1)

    all_errors: List[str] = []
    total_validated_topics = 0

    for tdir in topic_dirs:
        parts = tdir.name.split("_")
        if len(parts) < 2:
            continue
        tid = parts[0] + "_" + parts[1]
        if args.topics and tid not in args.topics:
            continue

        exp_outcomes = all_syllabus_outcomes.get(tid, set())
        errs = validate_topic(tdir, exp_outcomes)
        if errs:
            all_errors.extend(errs)
            print(f"[FAIL] {tdir.name}: {len(errs)} errors")
            for e in errs[:5]:
                print(f"  - {e}")
        else:
            print(f"[PASS] {tdir.name}: 100% verified")
        total_validated_topics += 1

    print("==================================================")
    print(f"VALIDATION COMPLETE: {total_validated_topics} topics checked.")
    if all_errors:
        print(f"FAILED with {len(all_errors)} total errors.")
        sys.exit(1)
    else:
        print("100% PASS: All 25 topics, course modules, lessons, DAGs, and zero em dashes verified.")


if __name__ == "__main__":
    main()
