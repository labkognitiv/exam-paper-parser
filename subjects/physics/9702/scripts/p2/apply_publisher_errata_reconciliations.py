#!/usr/bin/env python3
"""Create additive reviewed mark schemes for documented Physics P2 publisher errata.

The locked ``markscheme.json`` files and source PDFs are never edited.  Each
reviewed record is reproducible from those files plus the printed question
marks, and carries hashes of the source evidence it supersedes for checking.
"""

from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path


REPO = next(
    parent
    for parent in Path(__file__).resolve().parents
    if (parent / "subjects").is_dir() and (parent / "pyproject.toml").is_file()
)
P2 = REPO / "subjects/physics/9702/past papers/p2"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} is not a JSON object")
    return value


def write_json(path: Path, value: dict) -> None:
    rendered = json.dumps(value, indent=2, ensure_ascii=False) + "\n"
    if not path.is_file() or path.read_text(encoding="utf-8") != rendered:
        path.write_text(rendered, encoding="utf-8")


def question_dir(relative: str, number: str) -> Path:
    return P2 / relative / f"question_{number}"


def review_meta(
    question: dict,
    raw_markscheme: Path,
    source_pdf: Path,
    reason: str,
    evidence: list[Path] | None = None,
) -> dict:
    return {
        "schema_version": "9702_p2_reviewed_markscheme_meta_v1",
        "status": "PASS",
        "review_kind": "publisher_erratum_reconciliation",
        "official_source_locked": True,
        "question_id": question["question_id"],
        "reviewed_markscheme": "markscheme_reviewed.json",
        "locked_markscheme": {
            "file": "markscheme.json",
            "sha256": sha256(raw_markscheme),
        },
        "source_question": {
            "file": "question_ocr.json",
            "sha256": sha256(raw_markscheme.parent / "question_ocr.json"),
        },
        "source_pdf": {
            "path": source_pdf.relative_to(REPO).as_posix(),
            "sha256": sha256(source_pdf),
        },
        "additional_evidence": [
            {
                "path": path.relative_to(REPO).as_posix(),
                "sha256": sha256(path),
            }
            for path in evidence or []
        ],
        "reason": reason,
        "reviewed_total_marks": question["total_marks"],
        "reviewed_on": "2026-09-08",
    }


def normalise_points(points: list[dict], part_id: str) -> list[dict]:
    result = []
    for index, point in enumerate(points, 1):
        result.append({
            "id": f"{part_id}_mp{index:02d}",
            "tag": point.get("tag"),
            "text": point.get("text"),
            "guidance": point.get("guidance"),
            **({"marks": point["marks"]} if "marks" in point else {}),
            **({"is_alternative": point["is_alternative"]} if "is_alternative" in point else {}),
        })
    return result


def checked_review(question: dict, parts: list[dict]) -> dict:
    total = sum(part["marks"] for part in parts)
    if total != question["total_marks"]:
        raise ValueError(f"{question['question_id']}: reviewed {total} != printed {question['total_marks']}")
    return {
        "schema_version": "1.0",
        "paper_code": question["paper_code"],
        "question_id": question["question_id"],
        "question_num": question.get("question_num"),
        "total_marks": total,
        "parts": parts,
    }


def label_from_companion_id(part_id: str) -> str:
    match = re.search(r"_q\d\d_(.+)$", part_id)
    if not match:
        raise ValueError(f"cannot derive label from {part_id}")
    return "".join(f"({piece})" for piece in match.group(1).split("_"))


def rebuild_s21_raster_markscheme(number: str) -> tuple[Path, dict, dict]:
    relative = "2021/may-june/variant-3"
    directory = question_dir(relative, number)
    question = read_json(directory / "question_ocr.json")
    raw = directory / "markscheme.json"
    companion = P2 / relative / "mark-schemes" / f"markscheme_{number}.official-criteria.json"
    companion_data = read_json(companion)
    by_label = {part["label"]: part for part in question["parts"] if part.get("marks", 0) > 0}
    parts = []
    for source_part in companion_data["parts"]:
        target = by_label.get(label_from_companion_id(source_part["id"]))
        if target is None:
            raise ValueError(f"{question['question_id']}: no printed leaf for {source_part['id']}")
        if target["marks"] != source_part["marks"]:
            raise ValueError(f"{question['question_id']}: mark mismatch for {target['label']}")
        part_id = target["id"]
        parts.append({
            "id": part_id,
            "label": target["label"],
            "marks": target["marks"],
            "marking_points": normalise_points(source_part["marking_points"], part_id),
        })
    review = checked_review(question, parts)
    pdf = P2 / relative / "source/9702_s21_ms_23.pdf"
    meta = review_meta(
        question,
        raw,
        pdf,
        "The locked raster mark-scheme extraction has zero marks. The existing official-criteria companion supplies the source-grounded leaf criteria and matches every printed leaf and mark.",
        [companion],
    )
    return directory, review, meta


def clone_with_overrides(relative: str, number: str, transform, reason: str) -> tuple[Path, dict, dict]:
    directory = question_dir(relative, number)
    question = read_json(directory / "question_ocr.json")
    raw_path = directory / "markscheme.json"
    raw = read_json(raw_path)
    parts = transform(copy.deepcopy(raw["parts"]))
    review = checked_review(question, parts)
    # Paper codes have four components, so use the known source file discovered in the paper root.
    source_pdf = next((directory.parent / "source").glob("*_ms_*.pdf"))
    meta = review_meta(question, raw_path, source_pdf, reason)
    return directory, review, meta


def replace_part_marks(parts: list[dict], part_id: str, marks: int) -> list[dict]:
    found = False
    for part in parts:
        if part.get("id") == part_id:
            part["marks"] = marks
            found = True
    if not found:
        raise ValueError(f"missing part {part_id}")
    return parts


def remove_part(parts: list[dict], part_id: str) -> list[dict]:
    result = [part for part in parts if part.get("id") != part_id]
    if len(result) != len(parts) - 1:
        raise ValueError(f"missing or duplicate part {part_id}")
    return result


def reviewed_s22_21() -> tuple[Path, dict, dict]:
    return clone_with_overrides(
        "2022/may-june/variant-1",
        "02",
        lambda parts: replace_part_marks(parts, "9702_s22_21_q02_b_i", 3),
        "The published source awards C2 and A1 for 2(b)(i), but the locked extracted part field is incorrectly recorded as one mark. The reviewed record preserves the original criterion text and restores the source total of three marks.",
    )


def reviewed_s22_22() -> tuple[Path, dict, dict]:
    relative = "2022/may-june/variant-2"
    directory = question_dir(relative, "02")
    question = read_json(directory / "question_ocr.json")
    raw_path = directory / "markscheme.json"
    by_label = {part["label"]: part for part in question["parts"] if part.get("marks", 0) > 0}

    def part(label: str, points: list[dict]) -> dict:
        target = by_label[label]
        return {
            "id": target["id"],
            "label": label,
            "marks": target["marks"],
            "marking_points": normalise_points(points, target["id"]),
        }

    review = checked_review(question, [
        part("(a)", [
            {"tag": "C1", "marks": 1, "is_alternative": False, "text": "T sin 68° + 32 = 280", "guidance": None},
            {"tag": "A1", "marks": 1, "is_alternative": False, "text": "T = 270 N", "guidance": None},
        ]),
        part("(b)(i)", [
            {"tag": "A1", "marks": 1, "is_alternative": False, "text": "F = ρgV; V = 280 / (1.0 × 10³ × 9.81) = 0.029 m³", "guidance": None},
        ]),
        part("(b)(ii)", [
            {"tag": "C1", "marks": 1, "is_alternative": False, "text": "ρ = (32 / 9.81) / 0.029", "guidance": None},
            {"tag": "A1", "marks": 1, "is_alternative": False, "text": "ρ = 110 kg m⁻³", "guidance": None},
        ]),
        part("(c)", [
            {"tag": "C1", "marks": 1, "is_alternative": False, "text": "ΔE = mgΔh or ΔE = WΔh", "guidance": None},
            {"tag": "C1", "marks": 1, "is_alternative": False, "text": "Δh = −77 / 32 = −2.4", "guidance": None},
            {"tag": "A1", "marks": 1, "is_alternative": False, "text": "final height = 6.2 − 2.4 = 3.8 m", "guidance": None},
        ]),
        part("(d)(i)", [
            {"tag": "B1", "marks": 1, "is_alternative": False, "text": "T = kx, where k is a constant; or T = (EA / L)x, where A is cross-sectional area, E is Young modulus and L is original length", "guidance": None},
        ]),
        part("(d)(ii)", [
            {"tag": "C1", "marks": 1, "is_alternative": False, "text": "E = 1/2 kx² or E = 1/2 Fx and F = kx", "guidance": None},
            {"tag": "A1", "marks": 1, "is_alternative": False, "text": "E = 0.65 × 2² = 2.6 J", "guidance": None},
            {"tag": "C1", "marks": 1, "is_alternative": True, "text": "Alternative: E = 1/2 Fx; 0.65 = 1/2 × 270 × x, so x = 4.8 × 10⁻³ m and k = 5.6 × 10⁴", "guidance": None},
            {"tag": "A1", "marks": 1, "is_alternative": True, "text": "Alternative: final E = 1/2 × 540 × x = 2.6 J", "guidance": None},
        ]),
    ])
    pdf = P2 / relative / "source/9702_s22_ms_22.pdf"
    meta = review_meta(
        question,
        raw_path,
        pdf,
        "The locked extraction dropped 2(a), 2(b)(i) and 2(b)(ii), undercounted 2(c), and split a continuation of 2(d)(ii) into a non-printed 2(d)(iii). This reviewed record follows the printed question and the published mark-scheme pages 7–9.",
    )
    return directory, review, meta


def main() -> None:
    repairs = [
        *(rebuild_s21_raster_markscheme(number) for number in ("01", "02", "03", "04", "05", "06")),
        reviewed_s22_21(),
        reviewed_s22_22(),
        clone_with_overrides(
            "2024/october-november/variant-2",
            "04",
            lambda parts: remove_part(parts, "9702_w24_22_q04_u"),
            "The locked source has an unprinted 4(u) two-mark calculation. Its identical intended criteria occur under 6(c)(i); the reviewed Q4 therefore retains only printed Q4 parts.",
        ),
        clone_with_overrides(
            "2024/october-november/variant-2",
            "06",
            lambda parts: replace_part_marks(parts, "9702_w24_22_q06_c_i", 3),
            "The published criteria for 6(c)(i) contain C1, C1 and A1, but the locked part field is one mark. The reviewed record restores the printed three marks without changing its criteria.",
        ),
        clone_with_overrides(
            "2025/february-march/variant-2",
            "04",
            lambda parts: remove_part(parts, "9702_m25_22_q04_u"),
            "The locked source has an unprinted 4(u) three-mark calculation. Its identical intended criteria occur under 7(b); the reviewed Q4 therefore retains only printed Q4 parts.",
        ),
        clone_with_overrides(
            "2025/february-march/variant-2",
            "07",
            lambda parts: replace_part_marks(parts, "9702_m25_22_q07_b", 3),
            "The 7(b) criteria contain C1, C1 and A1, but the locked part field is zero. The reviewed record restores the printed three marks without changing its criteria.",
        ),
    ]
    for directory, reviewed, meta in repairs:
        write_json(directory / "markscheme_reviewed.json", reviewed)
        write_json(directory / "markscheme_review_meta.json", meta)
        print(f"reconciled {reviewed['question_id']} ({reviewed['total_marks']} marks)")


if __name__ == "__main__":
    main()
