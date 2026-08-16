#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = ROOT / "output/physics/p2/questions"
MARK_SCHEME_ROOT = ROOT / "output/physics/p2/mark-schemes"
DESTINATION = Path(__file__).with_name("paper-data.js")

PAPERS = (
    "9702_m16_qp_22",
    "9702_s16_qp_21",
    "9702_s16_qp_22",
    "9702_s16_qp_23",
    "9702_w16_qp_21",
    "9702_w16_qp_22",
    "9702_w16_qp_23",
)

# Keep the original confirmed-2016 corpus and add focused renderer fixtures for
# newly supported response blocks without pulling an entire additional paper in.
EXTRA_QUESTIONS = (
    ("9702_m17_qp_22", "question_01.json"),
)


def prepare_question(data: dict, paper: str, path: Path) -> dict:
    relative_root = f"../../output/physics/p2/questions/{paper}"
    data["prototype_image"] = f"{relative_root}/{data['question_image_with_figures'] or data['question_image']}"
    data["prototype_paper"] = paper
    for figure in data.get("figures", []):
        figure["prototype_file"] = f"{relative_root}/{figure['file']}"

    mark_scheme_paper = paper.replace("_qp_", "_ms_")
    mark_scheme_path = MARK_SCHEME_ROOT / mark_scheme_paper / f"markscheme_{data['question_num']:02d}.json"
    if mark_scheme_path.exists():
        mark_scheme = json.loads(mark_scheme_path.read_text(encoding="utf-8"))
        if mark_scheme.get("question_id") == data.get("question_id"):
            data["prototype_mark_scheme"] = mark_scheme
    return data


def main() -> None:
    questions = []
    for paper in PAPERS:
        source = SOURCE_ROOT / paper
        for path in sorted(source.glob("question_*.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            verification = data.get("verification", {})
            if not verification.get("content_structure_checked") or not verification.get("marks_reconciled"):
                continue
            questions.append(prepare_question(data, paper, path))
    for paper, filename in EXTRA_QUESTIONS:
        source = SOURCE_ROOT / paper
        path = source / filename
        data = json.loads(path.read_text(encoding="utf-8"))
        verification = data.get("verification", {})
        if not verification.get("content_structure_checked") or not verification.get("marks_reconciled"):
            continue
        questions.append(prepare_question(data, paper, path))
    DESTINATION.write_text(
        "window.PAPER_DATA = " + json.dumps(questions, ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
