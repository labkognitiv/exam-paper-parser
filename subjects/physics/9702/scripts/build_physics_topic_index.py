#!/usr/bin/env python3
"""Build a topic syllabus document and component evidence index."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
KB = REPO / "subjects/physics/9702"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def unique(values):
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic-id", required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--component", choices=("p1", "p2"), default="p2")
    args = parser.parse_args()

    taxonomy_path = KB / "knowledge/2025-2027/as/9702-2025-2027-as-taxonomy.json"
    outcomes_path = KB / "knowledge/2025-2027/as/9702-2025-2027-as-learning-outcomes.json"
    taxonomy = load(taxonomy_path)
    outcome_data = load(outcomes_path)
    topic = next(item for item in taxonomy["topics"] if item["topic_id"] == args.topic_id)
    outcomes = [item for item in outcome_data["outcomes"] if item["topic_id"] == args.topic_id]

    topic_dir = KB / "topics" / f"{args.topic_id}_{args.slug}"
    syllabus_document = {
        "schema_version": "9702_topic_syllabus_v1",
        "subject_code": "9702",
        "level": "AS",
        "syllabus_years": "2025-2027",
        "topic": topic,
        "learning_outcomes": outcomes,
        "sources": {
            "taxonomy": str(taxonomy_path.relative_to(REPO)),
            "learning_outcomes": str(outcomes_path.relative_to(REPO)),
            "syllabus_text": "subjects/physics/9702/syllabus/664565-2025-2027-syllabus/reduced/9702-2025-2027-as-subject-content.txt",
        },
    }
    write(topic_dir / "syllabus.json", syllabus_document)

    enrichment_paths = sorted((KB / "enrichment" / args.component).glob("*.enrichment.json"))
    question_records = []
    matched_parts = []
    for path in enrichment_paths:
        enrichment = load(path)
        parts = [part for part in enrichment["parts"] if part["mapping"]["primary_topic_id"] == args.topic_id]
        if not parts:
            continue
        question_records.append({
            "question_id": enrichment["question_id"],
            "enrichment_path": str(path.relative_to(REPO)),
            "part_ids": [part["part_id"] for part in parts],
        })
        matched_parts.extend(parts)

    registry_specs = {
        "definition_ids": ("definitions.json", "definitions", "definition_id", "term"),
        "formula_ids": ("formulas.json", "formulas", "formula_id", "name"),
        "skill_ids": ("skills.json", "skills", "skill_id", "name"),
        "question_pattern_ids": ("question-patterns.json", "patterns", "pattern_id", "name"),
    }
    ids = {
        "definition_ids": unique(x for part in matched_parts for x in part["knowledge_refs"]["definition_ids"]),
        "formula_ids": unique(x for part in matched_parts for x in part["knowledge_refs"]["formula_ids"]),
        "skill_ids": unique(
            x
            for part in matched_parts
            for x in [part["skills"]["primary_skill_id"], *part["skills"]["supporting_skill_ids"]]
        ),
        "question_pattern_ids": unique(x for part in matched_parts for x in part["question_patterns"]),
    }
    resolved = {}
    for output_key, (filename, array_key, id_key, name_key) in registry_specs.items():
        records = {item[id_key]: item for item in load(KB / "knowledge" / filename)[array_key]}
        resolved[output_key] = [
            {id_key: item_id, name_key: records[item_id][name_key]}
            for item_id in ids[output_key]
        ]

    evidence_index = {
        "schema_version": "9702_topic_evidence_index_v1",
        "topic_id": args.topic_id,
        "component": args.component.upper(),
        "source": "question enrichment records",
        "counts": {
            "questions": len(question_records),
            "answerable_parts": len(matched_parts),
        },
        "syllabus_ids_used": {
            "module_ids": unique(part["mapping"]["primary_module_id"] for part in matched_parts),
            "outcome_ids": unique(x for part in matched_parts for x in part["mapping"]["outcome_ids"]),
        },
        "knowledge_ids_used": resolved,
        "questions": question_records,
    }
    write(topic_dir / f"{args.component}-evidence-index.json", evidence_index)

    for module in topic["modules"]:
        module_questions = []
        module_parts = []
        for path in enrichment_paths:
            enrichment = load(path)
            parts = [
                part
                for part in enrichment["parts"]
                if part["mapping"]["primary_module_id"] == module["module_id"]
            ]
            if not parts:
                continue
            module_questions.append({
                "question_id": enrichment["question_id"],
                "enrichment_path": str(path.relative_to(REPO)),
                "part_ids": [part["part_id"] for part in parts],
            })
            module_parts.extend(parts)

        module_dir = topic_dir / "modules" / f"{module['module_id']}_{slugify(module['module_name'])}"
        module_evidence = {
            "schema_version": "9702_module_evidence_index_v1",
            "topic_id": args.topic_id,
            "module_id": module["module_id"],
            "component": args.component.upper(),
            "source": "question enrichment records",
            "counts": {
                "questions": len(module_questions),
                "answerable_parts": len(module_parts),
            },
            "outcome_ids_used": unique(
                outcome_id
                for part in module_parts
                for outcome_id in part["mapping"]["outcome_ids"]
            ),
            "questions": module_questions,
        }
        write(module_dir / f"{args.component}-evidence-index.json", module_evidence)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
