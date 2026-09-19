#!/usr/bin/env python3
"""structure_topic_lessons.py

Phase 3: Module Structuring & Lesson Planning across all 25 Cambridge Physics 9702 topics.
1. Preserves existing canonical course-module and lesson hierarchies for topics already structured
   (Topics 1, 4, 6, 7, 8, 9, 10, 11) while enriching them with complete 2016-2025 evidence parts.
2. Completes the remaining modules and lessons for Topic 2 (Kinematics) based on its canonical map.
3. Deconstructs un-structured AS topics (Topics 3, 5) and all A2 topics (Topics 12-25) into
   prerequisite-safe Course Modules (<topic_id>_cmNN) and bite-sized Lessons (<cm_id>_lNN).
4. Assigns 2016-2025 past paper evidence parts from evidence-index.json to every lesson.
5. Strict rules:
   - STRICTLY ZERO EM DASHES ('\\u2014') anywhere in code, markdown, logs, or messages.
   - Every mapped ID must strictly resolve against official 2025-2027 AS/A2 registries.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Set

PHYSICS_ROOT = Path(__file__).resolve().parents[2]
REPO_ROOT = Path(__file__).resolve().parents[5]
STUDY_TOPICS = PHYSICS_ROOT / "study" / "topics"

AS_TAX_PATH = PHYSICS_ROOT / "knowledge" / "2025-2027" / "as" / "9702-2025-2027-as-taxonomy.json"
AS_OUTCOMES_PATH = PHYSICS_ROOT / "knowledge" / "2025-2027" / "as" / "9702-2025-2027-as-learning-outcomes.json"
A2_TAX_PATH = PHYSICS_ROOT / "knowledge" / "2025-2027" / "a2" / "9702-2025-2027-a2-taxonomy.json"
A2_OUTCOMES_PATH = PHYSICS_ROOT / "knowledge" / "2025-2027" / "a2" / "9702-2025-2027-a2-learning-outcomes.json"


def clean_no_em_dash(text: str) -> str:
    """Ensure zero em dashes."""
    return text.replace(chr(8212), " - ")


def slugify(s: str) -> str:
    s = s.lower().replace("&", "and").replace(".", "")
    s = re.sub(r"[,\(\)\/]", "", s)
    s = re.sub(r"\s+", "_", s.strip())
    return s


def clean_outcome_title(text: str) -> str:
    """Generate a readable lesson title from outcome text."""
    t = text.strip()
    prefix_pattern = (
        r"^(understand that and use|understand that|show an understanding of|"
        r"show an understanding that|recall and use|recall and apply|recall|"
        r"derive and use|derive|explain that|explain|describe and explain|"
        r"describe|define|distinguish between|state and apply|state and use|"
        r"state|calculate|solve problems involving|sketch and interpret|"
        r"sketch|use|appreciate that)\s+"
    )
    t = re.sub(prefix_pattern, "", t, flags=re.I).strip()
    if not t:
        return "Fundamental Concepts"
    # Capitalize first letter
    t = t[0].upper() + t[1:]
    # Cut at first semicolon or period if too long
    if len(t) > 70:
        parts = re.split(r"[;:]", t)
        if len(parts) > 1 and len(parts[0]) >= 20:
            t = parts[0].strip()
        else:
            comma_parts = t.split(",")
            if len(comma_parts) > 1 and len(comma_parts[0]) >= 25:
                t = comma_parts[0].strip()
            else:
                t = t[:70].strip()
    return clean_no_em_dash(t)


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

    outcomes_by_module: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    outcome_by_id: Dict[str, Dict[str, Any]] = {}
    outcome_to_module: Dict[str, str] = {}

    for o in as_out.get("outcomes", []) + a2_out.get("outcomes", []):
        oid = o["outcome_id"]
        mid = o["module_id"]
        outcomes_by_module[mid].append(o)
        outcome_by_id[oid] = o
        outcome_to_module[oid] = mid

    return {
        "topics": topics,
        "outcomes_by_module": outcomes_by_module,
        "outcome_by_id": outcome_by_id,
        "outcome_to_module": outcome_to_module,
    }


def load_topic_evidence(topic_dir: Path) -> Dict[str, List[str]]:
    """Loads evidence by outcome from evidence-index.json."""
    ev_path = topic_dir / "evidence-index.json"
    evidence_by_outcome: Dict[str, List[str]] = defaultdict(list)
    if ev_path.is_file():
        with open(ev_path, "r", encoding="utf-8") as f:
            ev_data = json.load(f)
        for ev in ev_data.get("evidence", []):
            part_id = ev.get("part_id", "")
            for oid in ev.get("outcome_ids", []):
                evidence_by_outcome[oid].append(part_id)
    return evidence_by_outcome


def enrich_existing_topic(topic_dir: Path, tid: str, syllabus: Dict[str, Any]) -> Dict[str, Any]:
    """Enriches an already structured topic with 2016-2025 evidence parts and ensures zero em dashes."""
    evidence_by_outcome = load_topic_evidence(topic_dir)
    cm_dir = topic_dir / "course-modules"
    if not cm_dir.is_dir():
        return {"topic_id": tid, "course_modules_count": 0, "lessons_count": 0}

    cms = sorted([d for d in cm_dir.iterdir() if d.is_dir() and not d.name.startswith(".")])

    # Check lesson-knowledge-map.json for canonical lesson list
    kmap_path = topic_dir / "lesson-knowledge-map.json"
    kmap_lessons = []
    if kmap_path.is_file():
        try:
            with open(kmap_path, "r", encoding="utf-8") as f:
                kmap_data = json.load(f)
            kmap_lessons = kmap_data.get("lessons", [])
        except Exception:
            kmap_lessons = []

    level = "AS" if int(tid.split("_t")[1]) <= 11 else "A2"
    total_lessons = 0

    if kmap_lessons:
        prior_lids: List[str] = []
        for idx, les_spec in enumerate(kmap_lessons, start=1):
            lid = les_spec.get("lesson_id")
            if not lid:
                continue
            oids = les_spec.get("outcome_ids", [])
            title = clean_no_em_dash(les_spec.get("title", lid))

            # Match course module
            cm_m = re.match(r"(9702_t\d+_cm\d+)", lid)
            cm_id = cm_m.group(1) if cm_m else ""
            cm_candidates = [d for d in cms if d.name.startswith(cm_id)]
            if cm_candidates:
                cm_folder = cm_candidates[0]
            else:
                cm_folder = cm_dir / cm_id
                cm_folder.mkdir(parents=True, exist_ok=True)
                cms = sorted([d for d in cm_dir.iterdir() if d.is_dir() and not d.name.startswith(".")])

            l_folder = cm_folder / "lessons" / lid
            l_folder.mkdir(parents=True, exist_ok=True)
            l_json_path = l_folder / "lesson.json"

            all_parts: Set[str] = set()
            for oid in oids:
                all_parts.update(evidence_by_outcome.get(oid, []))

            ldata = None
            if l_json_path.is_file() and l_json_path.stat().st_size > 0:
                try:
                    with open(l_json_path, "r", encoding="utf-8") as f:
                        ldata = json.load(f)
                except Exception:
                    ldata = None

            if not ldata:
                # Generate complete lesson.json from spec
                goals = []
                for oid in oids:
                    o_obj = syllabus["outcome_by_id"].get(oid)
                    if o_obj:
                        goals.append(clean_no_em_dash(o_obj.get("outcome_text", "")))
                if not goals:
                    goals = [title]

                cambridge_mods = list({syllabus.get("outcome_to_module", {}).get(oid, f"{tid}_m01") for oid in oids}) if oids else [f"{tid}_m01"]

                ldata = {
                    "schema_version": "9702_student_lesson_spec_v1",
                    "subject_code": "9702",
                    "level": level,
                    "topic_id": tid,
                    "cambridge_module_ids": sorted(cambridge_mods),
                    "course_module_id": cm_id,
                    "lesson_id": lid,
                    "sequence": idx,
                    "title": title,
                    "knowledge_mapping": {
                        "outcome_ids": oids,
                        "skill_ids": les_spec.get("skill_ids", []),
                        "definition_ids": les_spec.get("definition_ids", []),
                        "formula_ids": les_spec.get("formula_ids", []),
                        "question_pattern_ids": les_spec.get("question_pattern_ids", ["direct_calculation", "explanation"]),
                    },
                    "prerequisites": {
                        "immediate_previous_lesson_id": prior_lids[-1] if prior_lids else None,
                        "previous_lesson_ids": list(prior_lids),
                        "previous_module_ids": [f"{tid}_cm{i:02d}" for i in range(1, int(cm_id.split("_cm")[1]))] if "_cm" in cm_id and int(cm_id.split("_cm")[1]) > 1 else [],
                        "external_topic_ids": ["9702_t01"] if tid != "9702_t01" else [],
                    },
                    "prior_knowledge_summary": [
                        f"Assumes mastery of prior prerequisites up to sequence {idx - 1}."
                    ] if idx > 1 else ["Foundational entry topic."],
                    "learning_goals": goals,
                    "new_learning": [title],
                    "not_yet_taught": [
                        "Subsequent syllabus outcomes in this topic and later topics."
                    ],
                    "knowledge_boundary": f"Teach strictly the listed {tid} outcomes.",
                    "next_lesson_handoff": f"Handoff delivers verified mastery of {title}.",
                    "past_paper_evidence": {
                        "total_parts": len(all_parts),
                        "evidence_part_ids": sorted(all_parts)[:20],
                    },
                    "authoring_status": {
                        "lesson_specification": "complete",
                        "notes": "not_started",
                        "questions": "not_started",
                        "markscheme": "not_started",
                        "enrichment": "not_started",
                    }
                }
            else:
                # Update sequence strictly to idx
                ldata["sequence"] = idx
                # Update past paper evidence
                if "past_paper_evidence" in ldata and isinstance(ldata["past_paper_evidence"], dict):
                    ldata["past_paper_evidence"]["total_archive_parts"] = len(all_parts)
                    ldata["past_paper_evidence"]["archive_part_ids"] = sorted(all_parts)[:20]
                else:
                    ldata["past_paper_evidence"] = {
                        "total_parts": len(all_parts),
                        "evidence_part_ids": sorted(all_parts)[:20],
                    }

            # Write lesson.json with zero em dashes
            content = json.dumps(ldata, indent=2, ensure_ascii=False) + "\n"
            content = clean_no_em_dash(content)
            with open(l_json_path, "w", encoding="utf-8") as f:
                f.write(content)

            total_lessons += 1
            prior_lids.append(lid)

    # Sanitize module.json files for all course modules
    for cm_folder in cms:
        m_json_path = cm_folder / "module.json"
        if m_json_path.is_file():
            with open(m_json_path, "r", encoding="utf-8") as f:
                content = f.read()
            cleaned = clean_no_em_dash(content)
            if cleaned != content:
                with open(m_json_path, "w", encoding="utf-8") as f:
                    f.write(cleaned)

    # Sanitize module-lesson-structure.md and lesson-knowledge-map.json
    for fname in ["module-lesson-structure.md", "lesson-knowledge-map.json"]:
        fpath = topic_dir / fname
        if fpath.is_file():
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            cleaned = clean_no_em_dash(content)
            if cleaned != content:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(cleaned)

    return {
        "topic_id": tid,
        "course_modules_count": len(cms),
        "lessons_count": total_lessons,
    }


def structure_topic_02(topic_dir: Path, syllabus: Dict[str, Any]) -> Dict[str, Any]:
    """Structures Topic 2 (Kinematics) based on its established 6-module, 15-lesson map."""
    tid = "9702_t02"
    evidence_by_outcome = load_topic_evidence(topic_dir)

    # Load existing lesson knowledge map
    kmap_path = topic_dir / "lesson-knowledge-map.json"
    with open(kmap_path, "r", encoding="utf-8") as f:
        kmap = json.load(f)

    lessons_spec = kmap.get("lessons", [])
    cm_dir = topic_dir / "course-modules"
    cm_dir.mkdir(parents=True, exist_ok=True)

    cm_metadata = [
        ("9702_t02_cm01", "Motion quantities and modelling", ["9702_t02_cm01_l01", "9702_t02_cm01_l02"]),
        ("9702_t02_cm02", "Motion graphs", ["9702_t02_cm02_l03", "9702_t02_cm02_l04", "9702_t02_cm02_l05"]),
        ("9702_t02_cm03", "Uniform acceleration equations", ["9702_t02_cm03_l06", "9702_t02_cm03_l07", "9702_t02_cm03_l08"]),
        ("9702_t02_cm04", "Vertical motion and free fall", ["9702_t02_cm04_l09", "9702_t02_cm04_l10"]),
        ("9702_t02_cm05", "Two-dimensional projectile motion", ["9702_t02_cm05_l11", "9702_t02_cm05_l12"]),
        ("9702_t02_cm06", "Synthesis, representation shift and mixed problem-solving", ["9702_t02_cm06_l13", "9702_t02_cm06_l14", "9702_t02_cm06_l15"]),
    ]

    all_written_lessons = []

    for cm_idx, (cm_id, cm_title, cm_lesson_ids) in enumerate(cm_metadata, start=1):
        cm_slug = f"{cm_id}_{slugify(cm_title)}"
        cm_folder = cm_dir / cm_slug
        cm_folder.mkdir(parents=True, exist_ok=True)
        lessons_folder = cm_folder / "lessons"
        lessons_folder.mkdir(parents=True, exist_ok=True)

        cm_outcomes = set()
        for lid in cm_lesson_ids:
            matching = next((l for l in lessons_spec if l["lesson_id"] == lid), None)
            if matching:
                cm_outcomes.update(matching.get("outcome_ids", []))

        # Write module.json
        prior_cm_ids = [cm[0] for cm in cm_metadata[:cm_idx-1]]
        cm_spec = {
            "schema_version": "9702_course_module_v1",
            "subject_code": "9702",
            "level": "AS",
            "topic_id": tid,
            "course_module_id": cm_id,
            "sequence": cm_idx,
            "title": cm_title,
            "cambridge_module_id": "9702_t02_m01",
            "lesson_ids": cm_lesson_ids,
            "learning_outcome_ids": sorted(cm_outcomes),
            "prerequisite_course_module_ids": prior_cm_ids,
            "handoff": {
                "next_module_can_assume": [cm_title],
                "next_module_must_not_assume": ["Subsequent topic modules"]
            }
        }
        cm_content = clean_no_em_dash(json.dumps(cm_spec, indent=2, ensure_ascii=False) + "\n")
        with open(cm_folder / "module.json", "w", encoding="utf-8") as f:
            f.write(cm_content)

        # Write each lesson
        for lid in cm_lesson_ids:
            l_spec = next((l for l in lessons_spec if l["lesson_id"] == lid), {})
            l_folder = lessons_folder / lid
            l_folder.mkdir(parents=True, exist_ok=True)
            l_json_path = l_folder / "lesson.json"

            # Check if lesson 1 exists in the long named directory
            if lid == "9702_t02_cm01_l01":
                legacy_path = lessons_folder / "9702_t02_cm01_l01_distance_displacement_speed_velocity" / "lesson.json"
                if legacy_path.is_file() and not l_json_path.is_file():
                    # Copy over the rich lesson content
                    shutil.copy2(legacy_path, l_json_path)

            if l_json_path.is_file():
                # Update existing lesson
                with open(l_json_path, "r", encoding="utf-8") as f:
                    ldata = json.load(f)
            else:
                seq = len(all_written_lessons) + 1
                oids = l_spec.get("outcome_ids", [])
                assigned_evidence: Set[str] = set()
                for oid in oids:
                    assigned_evidence.update(evidence_by_outcome.get(oid, []))

                prior_lids = [l["lesson_id"] for l in all_written_lessons]
                title = l_spec.get("title", f"Lesson {seq}")

                goals = []
                for oid in oids:
                    o_obj = syllabus["outcome_by_id"].get(oid)
                    if o_obj:
                        goals.append(o_obj.get("outcome_text", ""))
                if not goals:
                    goals = [title]

                ldata = {
                    "schema_version": "9702_student_lesson_spec_v1",
                    "subject_code": "9702",
                    "level": "AS",
                    "topic_id": tid,
                    "cambridge_module_ids": ["9702_t02_m01"],
                    "course_module_id": cm_id,
                    "lesson_id": lid,
                    "sequence": seq,
                    "title": title,
                    "knowledge_mapping": {
                        "outcome_ids": oids,
                        "skill_ids": l_spec.get("skill_ids", []),
                        "definition_ids": l_spec.get("definition_ids", []),
                        "formula_ids": l_spec.get("formula_ids", []),
                        "question_pattern_ids": l_spec.get("question_pattern_ids", ["direct_calculation", "explanation"])
                    },
                    "prerequisites": {
                        "previous_lesson_ids": prior_lids[-2:] if prior_lids else [],
                        "previous_module_ids": [prior_cm_ids[-1]] if prior_cm_ids else [],
                        "external_topic_ids": ["9702_t01"]
                    },
                    "prior_knowledge_summary": [
                        f"Assumes mastery of prior Kinematics prerequisites up to sequence {seq - 1}."
                    ],
                    "learning_goals": goals,
                    "new_learning": [title],
                    "not_yet_taught": [
                        "Subsequent syllabus outcomes in Kinematics and later topics."
                    ],
                    "knowledge_boundary": "Teach strictly the listed 9702_t02 outcomes without premature jumps into dynamics or energy.",
                    "next_lesson_handoff": f"Handoff delivers verified mastery of {title}.",
                    "past_paper_evidence": {
                        "total_parts": len(assigned_evidence),
                        "evidence_part_ids": sorted(assigned_evidence)[:20]
                    },
                    "authoring_status": {
                        "lesson_specification": "complete",
                        "notes": "not_started",
                        "questions": "not_started",
                        "markscheme": "not_started",
                        "enrichment": "not_started"
                    }
                }

            l_content = clean_no_em_dash(json.dumps(ldata, indent=2, ensure_ascii=False) + "\n")
            with open(l_json_path, "w", encoding="utf-8") as f:
                f.write(l_content)

            all_written_lessons.append({
                "lesson_id": lid,
                "title": l_spec.get("title", lid),
                "outcome_ids": l_spec.get("outcome_ids", []),
            })

    # Sanitize markdown and knowledge map
    for fname in ["module-lesson-structure.md", "lesson-knowledge-map.json"]:
        fpath = topic_dir / fname
        if fpath.is_file():
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            cleaned = clean_no_em_dash(content)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(cleaned)

    return {
        "topic_id": tid,
        "course_modules_count": len(cm_metadata),
        "lessons_count": len(all_written_lessons),
    }


def structure_new_topic(topic_data: Dict[str, Any], syllabus: Dict[str, Any]) -> Dict[str, Any]:
    """Structures an un-structured topic (Topics 3, 5, 12-25) from canonical syllabus outcomes."""
    tid = topic_data["topic_id"]
    tname = topic_data["topic_name"]
    level = topic_data["level"]
    slug = f"{tid}_{slugify(tname)}"
    topic_dir = STUDY_TOPICS / slug
    topic_dir.mkdir(parents=True, exist_ok=True)

    evidence_by_outcome = load_topic_evidence(topic_dir)
    cambridge_modules = topic_data.get("modules", [])

    course_modules = []
    all_lessons = []
    global_lesson_counter = 1

    topic_num = int(tid.split("_t")[1])
    prior_topic_id = f"9702_t{topic_num - 1:02d}" if topic_num > 1 else None

    for cm_counter, cmod in enumerate(cambridge_modules, start=1):
        mid = cmod["module_id"]
        mname = cmod.get("module_name", "")
        outcomes = syllabus["outcomes_by_module"].get(mid, [])
        if not outcomes:
            continue

        cm_id = f"{tid}_cm{cm_counter:02d}"
        cm_slug = f"{cm_id}_{slugify(mname)}"
        cm_dir = topic_dir / "course-modules" / cm_slug
        cm_dir.mkdir(parents=True, exist_ok=True)
        lessons_dir = cm_dir / "lessons"
        lessons_dir.mkdir(parents=True, exist_ok=True)

        cm_lesson_ids = []
        cm_outcomes = []

        # Group outcomes into bite-sized lessons: 1-2 outcomes per lesson
        i = 0
        while i < len(outcomes):
            # Check remaining
            rem = len(outcomes) - i
            if rem == 3:
                # 1 outcome then 2 outcomes
                chunk = outcomes[i:i+1]
                i += 1
            else:
                chunk = outcomes[i:i+2]
                i += 2

            lesson_id = f"{cm_id}_l{global_lesson_counter:02d}"
            global_lesson_counter += 1
            cm_lesson_ids.append(lesson_id)

            chunk_oids = [o["outcome_id"] for o in chunk]
            cm_outcomes.extend(chunk_oids)

            # Generate descriptive title
            title = clean_outcome_title(chunk[0].get("outcome_text", ""))

            prior_lesson_ids = [l["lesson_id"] for l in all_lessons]
            prior_cm_ids = [cm["course_module_id"] for cm in course_modules]

            assigned_evidence: Set[str] = set()
            for oid in chunk_oids:
                assigned_evidence.update(evidence_by_outcome.get(oid, []))

            lesson_data = {
                "schema_version": "9702_student_lesson_spec_v1",
                "subject_code": "9702",
                "level": level,
                "topic_id": tid,
                "cambridge_module_ids": [mid],
                "course_module_id": cm_id,
                "lesson_id": lesson_id,
                "sequence": len(all_lessons) + 1,
                "title": title,
                "knowledge_mapping": {
                    "outcome_ids": chunk_oids,
                    "skill_ids": [],
                    "definition_ids": [],
                    "formula_ids": [],
                    "question_pattern_ids": ["direct_calculation", "explanation"]
                },
                "prerequisites": {
                    "previous_lesson_ids": prior_lesson_ids[-2:] if prior_lesson_ids else [],
                    "previous_module_ids": [prior_cm_ids[-1]] if prior_cm_ids else [],
                    "external_topic_ids": [prior_topic_id] if prior_topic_id else []
                },
                "prior_knowledge_summary": [
                    f"Assumes mastery of prior prerequisites up to lesson sequence {len(all_lessons)}."
                ],
                "learning_goals": [clean_no_em_dash(o.get("outcome_text", "")) for o in chunk],
                "new_learning": [title],
                "not_yet_taught": [
                    "Subsequent syllabus outcomes in this module and later topics."
                ],
                "knowledge_boundary": f"Teach strictly the listed {tid} outcomes without premature jumps into later topics.",
                "next_lesson_handoff": f"Handoff delivers verified mastery of {title}.",
                "past_paper_evidence": {
                    "total_parts": len(assigned_evidence),
                    "evidence_part_ids": sorted(assigned_evidence)[:20],
                },
                "authoring_status": {
                    "lesson_specification": "complete",
                    "notes": "not_started",
                    "questions": "not_started",
                    "markscheme": "not_started",
                    "enrichment": "not_started",
                }
            }

            # Write lesson.json
            l_dir = lessons_dir / lesson_id
            l_dir.mkdir(parents=True, exist_ok=True)
            l_content = clean_no_em_dash(json.dumps(lesson_data, indent=2, ensure_ascii=False) + "\n")
            with open(l_dir / "lesson.json", "w", encoding="utf-8") as f:
                f.write(l_content)

            all_lessons.append({
                "lesson_id": lesson_id,
                "title": title,
                "outcome_ids": chunk_oids,
                "evidence_ids": sorted(assigned_evidence)[:20],
            })

        cm_spec = {
            "schema_version": "9702_course_module_v1",
            "subject_code": "9702",
            "level": level,
            "topic_id": tid,
            "course_module_id": cm_id,
            "sequence": cm_counter,
            "title": clean_no_em_dash(mname),
            "cambridge_module_id": mid,
            "lesson_ids": cm_lesson_ids,
            "learning_outcome_ids": cm_outcomes,
            "prerequisite_course_module_ids": [cm["course_module_id"] for cm in course_modules],
            "handoff": {
                "next_module_can_assume": [clean_no_em_dash(mname)],
                "next_module_must_not_assume": ["Subsequent topic modules"]
            }
        }
        cm_content = clean_no_em_dash(json.dumps(cm_spec, indent=2, ensure_ascii=False) + "\n")
        with open(cm_dir / "module.json", "w", encoding="utf-8") as f:
            f.write(cm_content)

        course_modules.append(cm_spec)

    # Generate module-lesson-structure.md
    md_lines = [
        f"# 9702 Topic {topic_num}: {clean_no_em_dash(tname)}",
        "",
        f"Structure status: complete ({len(course_modules)} course modules, {len(all_lessons)} lessons).",
        "",
        "This directory contains structure only. Official sources and canonical extraction remain immutable.",
        "",
        "## Cambridge modules",
        ""
    ]
    for cmod in cambridge_modules:
        md_lines.append(f"- {cmod['module_id']}: {clean_no_em_dash(cmod.get('module_name', ''))}")
    md_lines.extend(["", "## Course pathway", ""])

    for cm in course_modules:
        md_lines.append(f"### {cm['course_module_id']}: {cm['title']}")
        md_lines.append("")
        for lid in cm["lesson_ids"]:
            matching_l = next((l for l in all_lessons if l["lesson_id"] == lid), None)
            ltitle = matching_l["title"] if matching_l else lid
            oids_str = ", ".join(matching_l["outcome_ids"]) if matching_l else ""
            md_lines.append(f"- {lid}: {ltitle} ({oids_str})")
        md_lines.append("")

    md_lines.extend([
        "## Boundary and handoff",
        "",
        f"Pedagogical pathway for {tid} ({clean_no_em_dash(tname)}). Entry prerequisites are defined strictly by prior sequence. Zero premature knowledge jumps.",
        ""
    ])

    md_content = clean_no_em_dash("\n".join(md_lines) + "\n")
    with open(topic_dir / "module-lesson-structure.md", "w", encoding="utf-8") as f:
        f.write(md_content)

    # Generate lesson-knowledge-map.json
    kmap = {
        "schema_version": "9702_topic_lesson_knowledge_map_v2",
        "topic_id": tid,
        "cambridge_module_ids": [m["module_id"] for m in cambridge_modules],
        "course_module_ids": [cm["course_module_id"] for cm in course_modules],
        "lesson_plan": f"subjects/physics/9702/study/topics/{slug}/module-lesson-structure.md",
        "lessons": all_lessons,
    }
    kmap_content = clean_no_em_dash(json.dumps(kmap, indent=2, ensure_ascii=False) + "\n")
    with open(topic_dir / "lesson-knowledge-map.json", "w", encoding="utf-8") as f:
        f.write(kmap_content)

    return {
        "topic_id": tid,
        "course_modules_count": len(course_modules),
        "lessons_count": len(all_lessons),
    }


def structure_all_topics(topics_filter: List[str] | None = None) -> List[Dict[str, Any]]:
    syllabus = load_syllabus()
    results = []

    # Existing established topics that already have canonical structures
    established_topics = {"9702_t01", "9702_t04", "9702_t06", "9702_t07", "9702_t08", "9702_t09", "9702_t10", "9702_t11"}

    for t in syllabus["topics"]:
        tid = t["topic_id"]
        tname = t["topic_name"]
        slug = f"{tid}_{slugify(tname)}"
        topic_dir = STUDY_TOPICS / slug

        if topics_filter and tid not in topics_filter:
            continue

        if tid in established_topics:
            rep = enrich_existing_topic(topic_dir, tid, syllabus)
            print(f"[PRESERVED & ENRICHED] {tid} ({tname}): {rep['course_modules_count']} modules, {rep['lessons_count']} lessons")
        elif tid == "9702_t02":
            rep = structure_topic_02(topic_dir, syllabus)
            print(f"[POPULATED] {tid} ({tname}): {rep['course_modules_count']} modules, {rep['lessons_count']} lessons")
        else:
            rep = structure_new_topic(t, syllabus)
            print(f"[STRUCTURED NEW] {tid} ({tname}): {rep['course_modules_count']} modules, {rep['lessons_count']} lessons")

        results.append(rep)

    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Structure topic modules and lessons across all 25 topics")
    parser.add_argument("--topics", nargs="+", help="Specific topic IDs to process (default: all)")
    args = parser.parse_args()

    results = structure_all_topics(args.topics)
    total_cms = sum(r["course_modules_count"] for r in results)
    total_lessons = sum(r["lessons_count"] for r in results)

    print("==================================================")
    print(f"ALL {len(results)} TOPICS PROCESSED SUCCESSFULLY.")
    print(f"Total Course Modules: {total_cms}")
    print(f"Total Structured Lessons: {total_lessons}")
    print("==================================================")


if __name__ == "__main__":
    main()

