#!/usr/bin/env python3
"""Build dataset for the 2016 Physics 9702 Paper 2 reviewer prototype."""

import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
KB = ROOT / "subjects/physics/9702"
OUT = Path(__file__).resolve().parent / "data.js"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def by_id(items, key):
    return {item[key]: item for item in items}


def main():
    definitions = by_id(load(KB / "knowledge/definitions.json")["definitions"], "definition_id")
    formulas = by_id(load(KB / "knowledge/formulas.json")["formulas"], "formula_id")
    skills = by_id(load(KB / "knowledge/skills.json")["skills"], "skill_id")
    curriculum = KB / "curriculum/2025-2027"
    taxonomies = [load(curriculum / level / f"9702-2025-2027-{level}-taxonomy.json") for level in ("as", "a2")]
    outcome_sets = [load(curriculum / level / f"9702-2025-2027-{level}-learning-outcomes.json") for level in ("as", "a2")]
    topics = {topic["topic_id"]: topic["topic_name"] for taxonomy in taxonomies for topic in taxonomy["topics"]}
    modules = {module["module_id"]: module["module_name"] for taxonomy in taxonomies for topic in taxonomy["topics"] for module in topic["modules"]}
    outcomes = {item["outcome_id"]: item["outcome_text"] for data in outcome_sets for item in data["outcomes"]}
    groups = {}

    for enrichment_path in sorted((KB / "past-paper-revision/p2").glob("2016/**/enrichment/*.enrichment.json")):
        enrichment = load(enrichment_path)
        question_id = enrichment["question_id"]
        _, session, variant, qtoken = question_id.split("_")
        qnum = int(qtoken[1:])
        candidates = list((KB / "extracted-content/p2/2016").glob(f"**/variant-*/questions/question_{qnum:02d}.json"))
        question_path = next((path for path in candidates if load(path).get("question_id") == question_id), None)
        if question_path is None:
            continue
        mark_path = question_path.parent.parent / "mark-schemes" / f"markscheme_{qnum:02d}.json"
        if not mark_path.is_file():
            continue
        question, markscheme = load(question_path), load(mark_path)
        official = defaultdict(list)
        for mark_part in markscheme.get("parts", []):
            official[mark_part.get("id")].append(mark_part)
        enrich_parts = {part["part_id"]: part for part in enrichment.get("parts", [])}
        occurrences = defaultdict(int)
        parts = []
        for part in question.get("parts", []):
            part_id = part.get("id")
            occurrences[part_id] += 1
            mark_candidates = official.get(part_id, [])
            mark_part = mark_candidates[min(occurrences[part_id] - 1, len(mark_candidates) - 1)] if mark_candidates else {}
            enriched = enrich_parts.get(part_id)
            payload = None
            if enriched:
                mapping = enriched.get("mapping", {})
                knowledge = enriched.get("knowledge_refs", {})
                skill_block = enriched.get("skills", {})
                skill_ids = [skill_block.get("primary_skill_id"), *skill_block.get("supporting_skill_ids", [])]
                points = {point.get("id"): point for point in mark_part.get("marking_points", [])}
                criteria = []
                for rubric in enriched.get("checking", {}).get("ai_rubric", []):
                    source = points.get(rubric.get("criterion_id"), {})
                    criteria.append({"id": rubric.get("criterion_id"), "official": source.get("text", "Official marking point"), "observable": rubric.get("observable", ""), "alternatives": rubric.get("alternative_criterion_ids", [])})
                payload = {
                    "difficulty": enriched.get("difficulty", 2),
                    "patterns": enriched.get("question_patterns", []),
                    "mapping": {"topic": topics.get(mapping.get("primary_topic_id"), mapping.get("primary_topic_id")), "module": modules.get(mapping.get("primary_module_id"), mapping.get("primary_module_id")), "outcomes": [outcomes.get(item, item) for item in mapping.get("outcome_ids", [])]},
                    "skills": [{"id": item, "name": skills[item]["name"], "description": skills[item]["description"]} for item in skill_ids if item in skills],
                    "definitions": [{"id": item, "term": definitions[item]["term"], "description": definitions[item]["accepted_definition"]} for item in knowledge.get("definition_ids", []) if item in definitions],
                    "formulas": [{"id": item, "name": formulas[item]["name"], "latex": formulas[item]["latex"]} for item in knowledge.get("formula_ids", []) if item in formulas],
                    "hints": enriched.get("hints", []),
                    "walkthrough": enriched.get("walkthrough", []),
                    "criteria": criteria,
                    "checking": {"mode": enriched.get("checking", {}).get("mode", "hybrid"), "fullMarks": enriched.get("checking", {}).get("full_marks_if_all_deterministic_checks_pass", False), "deterministicCount": len(enriched.get("checking", {}).get("deterministic_checks", [])), "rubricCount": len(criteria)},
                }
            parts.append({"id": part_id, "path": part.get("path", []), "label": part.get("label") or "(" + ")(".join(part.get("path", [])) + ")", "parentId": part.get("parent_id"), "displayOrder": part.get("display_order", 0), "marks": part.get("marks"), "isLeaf": part.get("marks") is not None, "text": part.get("question_text", ""), "latex": part.get("question_text_latex") or part.get("question_text", ""), "figureIds": part.get("figure_ids", []), "responseSchema": part.get("response_schema"), "enrichment": payload})

        figures = []
        for figure in question.get("figures", []):
            figure_file = question_path.parent / figure.get("file", "")
            figures.append({"id": figure.get("id"), "label": figure.get("label", ""), "file": figure.get("file"), "url": "/" + figure_file.relative_to(ROOT).as_posix() if figure_file.is_file() else "", "placement": figure.get("placement", {}), "referenced_by": figure.get("referenced_by", [])})
        image_name = question.get("question_image_with_figures") or question.get("question_image")
        image_path = question_path.parent / image_name
        season = {"m": "March", "s": "May/June", "w": "Oct/Nov"}.get(session[0], session)
        paper_key = f"{session}_{variant}"
        group = groups.setdefault(paper_key, {"key": paper_key, "paperCode": f"9702_{session}_{variant}", "label": f"{season} 20{session[1:]} · Paper {variant}", "questions": []})
        group["questions"].append({"id": question_id, "number": qnum, "totalMarks": question.get("total_marks", 0), "stem": question.get("question_stem", ""), "stemLatex": question.get("question_stem_latex") or question.get("question_stem", ""), "image": "/" + image_path.relative_to(ROOT).as_posix(), "figures": figures, "contentFlow": question.get("content_flow", []), "parts": parts})

    papers = sorted(groups.values(), key=lambda item: item["key"])
    for paper in papers:
        paper["questions"].sort(key=lambda item: item["number"])
    payload = {"year": "2016", "papers": papers, "stats": {"papers": len(papers), "questions": sum(len(item["questions"]) for item in papers), "parts": sum(len(question["parts"]) for paper in papers for question in paper["questions"])}}
    OUT.write_text("window.REVIEW_DATA = " + json.dumps(payload, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")
    print(f"Wrote {OUT}: {payload['stats']['papers']} papers (2016 only), {payload['stats']['questions']} questions, {payload['stats']['parts']} parts")


if __name__ == "__main__":
    main()
