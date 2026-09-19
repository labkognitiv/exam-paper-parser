#!/usr/bin/env python3
"""Build a read-only internal-question snapshot grouped by module and lesson."""

from __future__ import annotations

import json
from pathlib import Path


PROTOTYPE = Path(__file__).resolve().parent
STUDY = PROTOTYPE.parents[1] / "study"
TOPICS = STUDY / "topics"


def title_from_lesson(lesson_dir: Path) -> str:
    lesson_file = lesson_dir / "lesson.json"
    if lesson_file.exists():
        try:
            return json.loads(lesson_file.read_text())["title"]
        except (KeyError, json.JSONDecodeError):
            pass
    return lesson_dir.name


def main() -> None:
    modules: dict[str, dict] = {}
    source_files: list[str] = []

    for question_path in sorted(TOPICS.glob("*/course-modules/*/lessons/*/practice-questions/*.json")):
        question = json.loads(question_path.read_text())
        lesson_dir = question_path.parents[1]
        module_dir = question_path.parents[3]
        module_file = module_dir / "module.json"
        module_data = json.loads(module_file.read_text()) if module_file.exists() else {}
        module_id = question.get("lesson_id", "").rsplit("_l", 1)[0]
        module_title = module_data.get("title") or module_data.get("module_title") or module_dir.name
        lesson_id = question["lesson_id"]
        module = modules.setdefault(module_id, {"id": module_id, "title": module_title, "lessons": {}})
        lesson = module["lessons"].setdefault(lesson_id, {"id": lesson_id, "title": title_from_lesson(lesson_dir), "questions": []})
        question["source_path"] = str(question_path)
        question["short_label"] = question["question_id"].rsplit("_", 1)[-1].upper()
        lesson["questions"].append(question)
        source_files.append(str(question_path))

    output_modules = []
    for module in modules.values():
        lessons = list(module["lessons"].values())
        lessons.sort(key=lambda item: item["id"])
        for lesson in lessons:
            lesson["questions"].sort(key=lambda item: item["question_id"])
        output_modules.append({"id": module["id"], "title": module["title"], "lessons": lessons})
    output_modules.sort(key=lambda item: item["id"])

    payload = {
        "schema_version": "internal_question_reviewer_v1",
        "modules": output_modules,
        "question_count": len(source_files),
        "source_files": source_files,
    }
    target = PROTOTYPE / "data.js"
    target.write_text("window.INTERNAL_QUESTION_DATA = " + json.dumps(payload, ensure_ascii=False, indent=2) + ";\n")
    print(f"Wrote {target} with {len(source_files)} questions")


if __name__ == "__main__":
    main()
