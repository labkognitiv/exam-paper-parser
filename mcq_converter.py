from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path

import pymupdf


PAPER_RE = re.compile(
    r"^(?P<subject>\d{4})_(?P<session>[msw])(?P<year>\d{2})_qp_(?P<variant>1\d)$",
    re.I,
)
MARKSCHEME_RE = re.compile(
    r"^(?P<subject>\d{4})_(?P<session>[msw])(?P<year>\d{2})_ms_(?P<variant>1\d)$",
    re.I,
)
ANSWER_ROW_RE = re.compile(r"^(?P<number>\d{1,2})\s+(?P<answer>[A-D])\s+(?P<marks>\d+)$")
QUESTION_LINE_RE = re.compile(r"^(?P<number>\d{1,2})(?:\s+\S|$)")


@dataclass(frozen=True)
class McqQuestion:
    number: int
    page_number: int
    y0: float
    y1: float


def metadata(pdf: Path) -> dict:
    match = PAPER_RE.match(pdf.stem) or MARKSCHEME_RE.match(pdf.stem)
    if not match:
        raise ValueError(f"MCQ filename must look like 9702_s25_qp_11.pdf: {pdf.name}")
    session_code = match.group("session").lower()
    sessions = {"m": "February/March", "s": "May/June", "w": "October/November"}
    return {
        "subject_code": match.group("subject"),
        "year": 2000 + int(match.group("year")),
        "session": sessions[session_code],
        "session_code": session_code,
        "variant": int(match.group("variant")),
        "paper_code": f"{match.group('subject')}_{session_code}{match.group('year')}_{match.group('variant')}",
    }


def extract_split_answer_rows(lines: list[str]) -> dict[int, dict]:
    """Read legacy keys with number/letter pairs split across lines or columns."""
    answers: dict[int, dict] = {}
    cleaned = [line.strip() for line in lines if line.strip()]
    candidates: list[tuple[int, str]] = []
    pair_re = re.compile(r"(?<!\S)([1-9]|[1-3]\d|40)\s+([A-D])(?=\s|$)")
    for line in cleaned:
        candidates.extend((int(match.group(1)), match.group(2)) for match in pair_re.finditer(line))
    for index in range(len(cleaned) - 1):
        if not re.fullmatch(r"(?:[1-9]|[1-3]\d|40)", cleaned[index]):
            continue
        if not re.fullmatch(r"[A-D]", cleaned[index + 1]):
            continue
        candidates.append((int(cleaned[index]), cleaned[index + 1]))
    for number, answer in candidates:
        if number in answers and answers[number]["answer"] != answer:
            raise ValueError(f"Conflicting legacy answers for question {number}")
        answers[number] = {"answer": answer, "marks": 1}
    return answers


def extract_answer_key(pdf: Path) -> dict[int, dict]:
    answers: dict[int, dict] = {}
    text_lines: list[str] = []
    with pymupdf.open(pdf) as doc:
        for page in doc:
            text_lines.extend(page.get_text("text", sort=True).splitlines())
            for block in page.get_text("blocks", sort=True):
                row = " ".join(block[4].split())
                match = ANSWER_ROW_RE.match(row)
                if not match:
                    continue
                number = int(match.group("number"))
                if number in answers:
                    raise ValueError(f"Duplicate answer for question {number} in {pdf.name}")
                answers[number] = {
                    "answer": match.group("answer"),
                    "marks": int(match.group("marks")),
                }
    expected = set(range(1, 41))
    if set(answers) != expected:
        legacy_answers = extract_split_answer_rows(text_lines)
        if set(legacy_answers) == expected:
            answers = legacy_answers
    found = set(answers)
    if found != expected:
        missing = sorted(expected - found)
        extra = sorted(found - expected)
        raise ValueError(f"Invalid MCQ answer key {pdf.name}: missing={missing}, extra={extra}")
    if any(row["marks"] != 1 for row in answers.values()):
        raise ValueError(f"Expected every MCQ to be worth one mark in {pdf.name}")
    return answers


def apply_answer_key(pdf: Path, output_root: Path) -> Path:
    paper = metadata(pdf)
    question_stem = pdf.stem.replace("_ms_", "_qp_")
    destination = output_root / question_stem
    destination.mkdir(parents=True, exist_ok=True)
    answers = extract_answer_key(pdf)
    missing_question_json: list[int] = []

    for number, row in sorted(answers.items()):
        question_path = destination / f"question_{number:02d}.json"
        if not question_path.exists():
            missing_question_json.append(number)
            continue
        payload = json.loads(question_path.read_text(encoding="utf-8"))
        payload["correct_answer"] = row["answer"]
        payload["answer_source_filename"] = pdf.name
        temp_path = question_path.with_suffix(".tmp.json")
        temp_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        temp_path.replace(question_path)

    answer_key = {
        "schema_version": "1.0",
        "paper_code": paper["paper_code"],
        "source_filename": pdf.name,
        "total_questions": len(answers),
        "total_marks": sum(row["marks"] for row in answers.values()),
        "answers": {str(number): row["answer"] for number, row in sorted(answers.items())},
        "validation_passed": True,
        "question_json_updated": len(answers) - len(missing_question_json),
        "missing_question_json": missing_question_json,
    }
    path = destination / "answer_key.json"
    path.write_text(json.dumps(answer_key, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        f"{pdf.name}: wrote validated 40-answer key and updated "
        f"{answer_key['question_json_updated']} question JSON files in {destination}"
    )
    return path


def question_starts(doc: pymupdf.Document) -> list[tuple[int, int, float]]:
    starts: list[tuple[int, int, float]] = []
    expected = 1
    for page_number, page in enumerate(doc):
        for block in page.get_text("dict", sort=True).get("blocks", []):
            for line in block.get("lines", []):
                text = "".join(span["text"] for span in line["spans"]).strip()
                x0, y0, _x1, _y1 = line["bbox"]
                match = QUESTION_LINE_RE.match(text)
                if (
                    match
                    and int(match.group("number")) == expected
                    and x0 < 90
                    and 45 < y0 < page.rect.height - 45
                ):
                    starts.append((expected, page_number, y0))
                    expected += 1
    if not starts:
        raise ValueError("No sequential MCQ question numbers were detected.")
    return starts


def permission_boundary(page: pymupdf.Page) -> float | None:
    for block in page.get_text("blocks", sort=True):
        if "Permission to reproduce items" in block[4]:
            return float(block[1]) - 8
    return None


def content_bottom(page: pymupdf.Page, y0: float, limit: float) -> float:
    bottoms: list[float] = []
    for block in page.get_text("blocks", sort=True):
        x0, by0, x1, by1, text = block[:5]
        if text.strip() and x1 > 42 and x0 < page.rect.width - 42 and by1 > y0 and by0 < limit:
            bottoms.append(min(float(by1), limit))
    for drawing in page.get_drawings():
        rect = pymupdf.Rect(drawing["rect"])
        if rect.y1 > y0 and rect.y0 < limit and rect.x1 > 42 and rect.x0 < page.rect.width - 42:
            bottoms.append(min(float(rect.y1), limit))
    return min(limit, (max(bottoms) + 10) if bottoms else limit)


def detect_questions(doc: pymupdf.Document) -> list[McqQuestion]:
    starts = question_starts(doc)
    questions: list[McqQuestion] = []
    for index, (number, page_number, y0) in enumerate(starts):
        page = doc[page_number]
        next_start = starts[index + 1] if index + 1 < len(starts) else None
        if next_start and next_start[1] == page_number:
            y1 = next_start[2] - 7
        else:
            limit = min(page.rect.height - 47, permission_boundary(page) or page.rect.height)
            y1 = content_bottom(page, y0, limit)
        questions.append(McqQuestion(number, page_number, max(48, y0 - 7), y1))
    return questions


def has_visual_content(page: pymupdf.Page, clip: pymupdf.Rect) -> bool:
    for drawing in page.get_drawings():
        rect = pymupdf.Rect(drawing["rect"])
        overlap = rect & clip
        if not overlap.is_empty and (overlap.width > 12 or overlap.height > 12):
            return True
    for block in page.get_text("dict").get("blocks", []):
        if block.get("type") == 1 and not (pymupdf.Rect(block["bbox"]) & clip).is_empty:
            return True
    return False


def extract_question_text(page: pymupdf.Page, clip: pymupdf.Rect) -> str:
    """Extract the visible MCQ text within the same bounds as the question image."""
    lines: list[str] = []
    for block in page.get_text("dict", clip=clip, sort=True).get("blocks", []):
        for line in block.get("lines", []):
            text = "".join(str(span.get("text", "")) for span in line.get("spans", []))
            text = text.strip()
            if text:
                lines.append(text)
    return "\n".join(lines).strip()


def convert_pdf(pdf: Path, output_root: Path, dpi: int = 150) -> list[Path]:
    paper = metadata(pdf)
    destination = output_root / pdf.stem
    destination.mkdir(parents=True, exist_ok=True)
    # Rerunning an output created by the diagram-exporting parser should restore
    # the simpler source-image package and remove its obsolete visual crops.
    for stale_figure in destination.glob("figure_*.png"):
        stale_figure.unlink()
    written: list[Path] = []

    with pymupdf.open(pdf) as doc:
        questions = detect_questions(doc)
        for question in questions:
            page = doc[question.page_number]
            clip = pymupdf.Rect(42, question.y0, page.rect.width - 42, question.y1)
            image_path = destination / f"question_{question.number:02d}.png"
            temp_image = image_path.with_suffix(".tmp.png")
            pix = page.get_pixmap(
                matrix=pymupdf.Matrix(dpi / 72, dpi / 72),
                clip=clip,
                alpha=False,
            )
            pix.save(temp_image)
            temp_image.replace(image_path)

            question_text = extract_question_text(page, clip)
            text_path = destination / f"question_{question.number:02d}.txt"
            temp_text = text_path.with_suffix(".tmp.txt")
            temp_text.write_text(question_text + "\n", encoding="utf-8")
            temp_text.replace(text_path)

            question_id = f"{paper['paper_code']}_q{question.number:02d}"
            payload = {
                "schema_version": "1.0",
                "question_id": question_id,
                "source_filename": pdf.name,
                **paper,
                "question_num": question.number,
                "source_pages": [question.page_number + 1],
                "question_image": image_path.name,
                "question_text": question_text,
                "question_text_file": text_path.name,
                "question_text_format": "plain-text",
                "answer_type": "multiple-choice",
                "options": ["A", "B", "C", "D"],
                "response_schema": {
                    "type": "single-choice",
                    "required": True,
                    "options": [
                        {"id": option, "label": option}
                        for option in ("A", "B", "C", "D")
                    ],
                },
                "marks": 1,
                "correct_answer": None,
                "has_visual_content": has_visual_content(page, clip),
                "review_flags": [],
            }
            json_path = destination / f"question_{question.number:02d}.json"
            json_path.write_text(
                json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            written.extend((image_path, json_path, text_path))

    print(f"{pdf.name}: wrote {len(questions)} MCQ PNG, JSON, and TXT sets to {destination}")
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Crop multiple-choice exam questions.")
    parser.add_argument("source", nargs="?", type=Path, default=Path("input/physics/mcq"))
    parser.add_argument("--output", type=Path, default=Path("output/physics/mcq"))
    parser.add_argument("--dpi", type=int, default=150)
    args = parser.parse_args(argv)
    if args.dpi < 72:
        parser.error("--dpi must be at least 72")
    pdfs = [args.source] if args.source.is_file() else sorted(args.source.glob("*.pdf"))
    if not pdfs:
        parser.error(f"No PDF files found at {args.source}")
    question_pdfs = [pdf for pdf in pdfs if PAPER_RE.match(pdf.stem)]
    markscheme_pdfs = [pdf for pdf in pdfs if MARKSCHEME_RE.match(pdf.stem)]
    unsupported = [pdf.name for pdf in pdfs if pdf not in question_pdfs and pdf not in markscheme_pdfs]
    if unsupported:
        raise ValueError(f"Unsupported MCQ filenames: {', '.join(unsupported)}")
    for pdf in question_pdfs:
        convert_pdf(pdf, args.output, dpi=args.dpi)
    for pdf in markscheme_pdfs:
        apply_answer_key(pdf, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
