#!/usr/bin/env python3
"""compile_topic_evidence.py

Phase 2 Orchestrator Evidence Compilation.
Aggregates all mapped past-paper evidence across 2016-2025 into topic-level
and module-level evidence indexes for all 25 Cambridge Physics 9702 topics.

Strict rules: 1. Zero em dashes (Unicode U+2014) anywhere in code, markdown, logs, or messages.
2. Mapped IDs must strictly resolve against official 2025-2027 AS/A2 registries.
"""

from __future__ import annotations

import glob
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Set

PHYSICS_ROOT = Path(__file__).resolve().parents[2]
REPO_ROOT = Path(__file__).resolve().parents[5]
PAST_PAPERS = PHYSICS_ROOT / "past papers"
STUDY_TOPICS = PHYSICS_ROOT / "study" / "topics"

AS_TAX_PATH = PHYSICS_ROOT / "knowledge" / "2025-2027" / "as" / "9702-2025-2027-as-taxonomy.json"
AS_OUTCOMES_PATH = PHYSICS_ROOT / "knowledge" / "2025-2027" / "as" / "9702-2025-2027-as-learning-outcomes.json"
A2_TAX_PATH = PHYSICS_ROOT / "knowledge" / "2025-2027" / "a2" / "9702-2025-2027-a2-taxonomy.json"
A2_OUTCOMES_PATH = PHYSICS_ROOT / "knowledge" / "2025-2027" / "a2" / "9702-2025-2027-a2-learning-outcomes.json"


def slugify(s: str) -> str:
    s = s.lower().replace("&", "and").replace(".", "")
    s = re.sub(r"[,\(\)\/]", "", s)
    s = re.sub(r"\s+", "_", s.strip())
    return s


def load_syllabus() -> Dict[str, Any]:
    with open(AS_TAX_PATH, "r", encoding="utf-8") as f:
        as_tax = json.load(f)
    with open(AS_OUTCOMES_PATH, "r", encoding="utf-8") as f:
        as_out = json.load(f)
    with open(A2_TAX_PATH, "r", encoding="utf-8") as f:
        a2_tax = json.load(f)
    with open(A2_OUTCOMES_PATH, "r", encoding="utf-8") as f:
        a2_out = json.load(f)

    topics: List[Dict[str, Any]] = []
    for t in as_tax.get("topics", []):
        t_copy = dict(t)
        t_copy["level"] = "AS"
        topics.append(t_copy)
    for t in a2_tax.get("topics", []):
        t_copy = dict(t)
        t_copy["level"] = "A2"
        topics.append(t_copy)

    outcomes_by_topic: Dict[str, List[str]] = defaultdict(list)
    outcomes_by_module: Dict[str, List[str]] = defaultdict(list)
    outcome_details: Dict[str, Dict[str, Any]] = {}

    for o in as_out.get("outcomes", []) + a2_out.get("outcomes", []):
        oid = o["outcome_id"]
        tid = o["topic_id"]
        mid = o["module_id"]
        outcomes_by_topic[tid].append(oid)
        outcomes_by_module[mid].append(oid)
        outcome_details[oid] = o

    return {
        "topics": topics,
        "outcomes_by_topic": outcomes_by_topic,
        "outcomes_by_module": outcomes_by_module,
        "outcome_details": outcome_details,
    }


def collect_evidence() -> Dict[str, List[Dict[str, Any]]]:
    evidence_by_topic: Dict[str, List[Dict[str, Any]]] = defaultdict(list)

    # 1. P1 MCQs
    p1_files = sorted(glob.glob(str(PAST_PAPERS / "p1" / "**" / "enrichment" / "*.enrichment.json"), recursive=True))
    for p in p1_files:
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
        qid = data.get("question_id", "")
        # Derive paper_code e.g. 9702_m24_12 from question_id 9702_m24_12_q01
        m = re.match(r"(9702_[msw]\d{2}_1\d)_q\d{2}", qid)
        paper_code = m.group(1) if m else ""

        mapping = data.get("mapping", {})
        tid = data.get("primary_topic_id") or mapping.get("primary_topic_id")
        mid = data.get("primary_module_id") or mapping.get("primary_module_id")
        oids = data.get("outcome_ids") or mapping.get("outcome_ids", [])

        if tid:
            evidence_by_topic[tid].append({
                "question_id": qid,
                "part_id": qid,
                "paper_code": paper_code,
                "component": "P1",
                "module_id": mid,
                "outcome_ids": oids,
                "difficulty": data.get("difficulty", 1),
                "patterns": data.get("question_patterns", []),
            })

    # 2. P2 and P4 Theory
    for comp in ["p2", "p4"]:
        q_files = sorted(glob.glob(str(PAST_PAPERS / comp / "**" / "question_*" / "enrichment.json"), recursive=True))
        for q in q_files:
            with open(q, "r", encoding="utf-8") as f:
                data = json.load(f)
            qid = data.get("question_id", "")
            # Derive paper_code e.g. 9702_m24_22 or 9702_m24_42
            m = re.match(r"(9702_[msw]\d{2}_\d{2})_q\d{2}", qid)
            paper_code = m.group(1) if m else ""

            for part in data.get("parts", []):
                pid = part.get("part_id", "")
                mapping = part.get("mapping", {})
                tid = part.get("primary_topic_id") or mapping.get("primary_topic_id")
                mid = part.get("primary_module_id") or mapping.get("primary_module_id")
                oids = part.get("outcome_ids") or mapping.get("outcome_ids", [])

                if tid:
                    evidence_by_topic[tid].append({
                        "question_id": qid,
                        "part_id": pid,
                        "paper_code": paper_code,
                        "component": comp.upper(),
                        "module_id": mid,
                        "outcome_ids": oids,
                        "marks": part.get("marks", 1),
                        "difficulty": part.get("difficulty", 2),
                        "patterns": part.get("question_patterns", []),
                    })

    return evidence_by_topic


def compile_topic(
    topic_data: Dict[str, Any],
    all_evidence: List[Dict[str, Any]],
    syllabus: Dict[str, Any],
) -> Dict[str, Any]:
    tid = topic_data["topic_id"]
    tname = topic_data["topic_name"]
    level = topic_data["level"]
    slug = f"{tid}_{slugify(tname)}"
    topic_dir = STUDY_TOPICS / slug
    topic_dir.mkdir(parents=True, exist_ok=True)

    # Sort evidence deterministically
    evidence = sorted(all_evidence, key=lambda x: (x["component"], x["paper_code"], x["question_id"], x["part_id"]))

    assessed_outcomes: Set[str] = set()
    p1_count = 0
    p2_count = 0
    p4_count = 0

    for ev in evidence:
        for oid in ev.get("outcome_ids", []):
            assessed_outcomes.add(oid)
        if ev["component"] == "P1":
            p1_count += 1
        elif ev["component"] == "P2":
            p2_count += 1
        elif ev["component"] == "P4":
            p4_count += 1

    all_topic_outcomes = syllabus["outcomes_by_topic"].get(tid, [])
    unassessed_outcomes = sorted(set(all_topic_outcomes) - assessed_outcomes)

    evidence_index = {
        "schema_version": "9702_topic_evidence_index_v2",
        "topic_id": tid,
        "topic_name": tname,
        "level": level,
        "counts": {
            "total_parts": len(evidence),
            "p1_parts": p1_count,
            "p2_parts": p2_count,
            "p4_parts": p4_count,
        },
        "assessed_outcome_ids": sorted(assessed_outcomes),
        "unassessed_outcome_ids": unassessed_outcomes,
        "evidence": evidence,
    }

    ev_path = topic_dir / "evidence-index.json"
    content = json.dumps(evidence_index, indent=2, ensure_ascii=False) + "\n"
    if chr(8212) in content:
        content = content.replace(chr(8212), " - ")
    with open(ev_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Ensure syllabus.json exists for the topic
    syl_path = topic_dir / "syllabus.json"
    if not syl_path.is_file():
        topic_outcomes_list = [syllabus["outcome_details"][oid] for oid in all_topic_outcomes if oid in syllabus["outcome_details"]]
        syllabus_obj = {
            "schema_version": "9702_topic_syllabus_v1",
            "subject_code": "9702",
            "level": level,
            "syllabus_years": "2025-2027",
            "topic": {
                "topic_id": tid,
                "topic_number": topic_data.get("topic_number", int(tid.split("_t")[1])),
                "topic_name": tname,
                "modules": topic_data.get("modules", [])
            },
            "learning_outcomes": topic_outcomes_list
        }
        scontent = json.dumps(syllabus_obj, indent=2, ensure_ascii=False) + "\n"
        if chr(8212) in scontent:
            scontent = scontent.replace(chr(8212), " - ")
        with open(syl_path, "w", encoding="utf-8") as f:
            f.write(scontent)

    # Compile Cambridge modules
    modules_dir = topic_dir / "modules"
    modules_dir.mkdir(parents=True, exist_ok=True)

    for m in topic_data.get("modules", []):
        mid = m["module_id"]
        mname = m.get("module_name", "")
        mslug = f"{mid}_{slugify(mname)}"
        mod_dir = modules_dir / mslug
        mod_dir.mkdir(parents=True, exist_ok=True)

        mod_evidence = [ev for ev in evidence if ev.get("module_id") == mid]
        mod_assessed: Set[str] = set()
        mod_p1 = 0
        mod_p2 = 0
        mod_p4 = 0
        for ev in mod_evidence:
            for oid in ev.get("outcome_ids", []):
                mod_assessed.add(oid)
            if ev["component"] == "P1":
                mod_p1 += 1
            elif ev["component"] == "P2":
                mod_p2 += 1
            elif ev["component"] == "P4":
                mod_p4 += 1

        all_mod_outcomes = syllabus["outcomes_by_module"].get(mid, [])
        mod_unassessed = sorted(set(all_mod_outcomes) - mod_assessed)

        module_json = {
            "schema_version": "9702_topic_module_v1",
            "subject_code": "9702",
            "level": level,
            "topic_id": tid,
            "module_id": mid,
            "module_number": m.get("module_number", ""),
            "module_name": mname,
            "source_syllabus_page": m.get("source_syllabus_page"),
            "learning_outcome_ids": all_mod_outcomes,
            "evidence_counts": {
                "total_parts": len(mod_evidence),
                "p1_parts": mod_p1,
                "p2_parts": mod_p2,
                "p4_parts": mod_p4,
            },
            "assessed_outcome_ids": sorted(mod_assessed),
            "unassessed_outcome_ids": mod_unassessed,
            "evidence_part_ids": [ev["part_id"] for ev in mod_evidence],
        }

        mod_path = mod_dir / "module.json"
        mcontent = json.dumps(module_json, indent=2, ensure_ascii=False) + "\n"
        if chr(8212) in mcontent:
            mcontent = mcontent.replace(chr(8212), " - ")
        with open(mod_path, "w", encoding="utf-8") as f:
            f.write(mcontent)

    return {
        "topic_id": tid,
        "topic_name": tname,
        "level": level,
        "slug": slug,
        "total_parts": len(evidence),
        "assessed_outcomes_count": len(assessed_outcomes),
        "total_outcomes_count": len(all_topic_outcomes),
        "unassessed_outcomes": unassessed_outcomes,
    }


def main() -> None:
    print("Starting Phase 2 Evidence Compilation across all 25 topics...")
    syllabus = load_syllabus()
    evidence_by_topic = collect_evidence()

    total_evidence_parts = sum(len(evs) for evs in evidence_by_topic.values())
    print(f"Collected {total_evidence_parts} total evidence parts across 2016-2025 archive.")

    reports: List[Dict[str, Any]] = []
    for t in syllabus["topics"]:
        tid = t["topic_id"]
        evs = evidence_by_topic.get(tid, [])
        rep = compile_topic(t, evs, syllabus)
        reports.append(rep)
        print(f"Topic {tid}: {rep['topic_name']} ({rep['total_parts']} parts, {rep['assessed_outcomes_count']}/{rep['total_outcomes_count']} outcomes assessed)")

    # Global summary report
    total_assessed = sum(r["assessed_outcomes_count"] for r in reports)
    total_syllabus_outcomes = sum(r["total_outcomes_count"] for r in reports)
    coverage_pct = (total_assessed / total_syllabus_outcomes * 100) if total_syllabus_outcomes else 0

    print("==================================================")
    print(f"PHASE 2 COMPILATION COMPLETE")
    print(f"Total topics compiled: {len(reports)} (11 AS + 14 A2)")
    print(f"Total past paper parts indexed: {total_evidence_parts}")
    print(f"Syllabus outcome coverage: {total_assessed}/{total_syllabus_outcomes} ({coverage_pct:.1f}%)")
    print("==================================================")


if __name__ == "__main__":
    main()
