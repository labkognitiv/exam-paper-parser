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


def extract_answer_key(pdf: Path) -> dict[int, dict]:
    answers: dict[int, dict] = {}
    with pymupdf.open(pdf) as doc:
        for page in doc:
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


def visual_source_rect(page: pymupdf.Page, question_clip: pymupdf.Rect) -> pymupdf.Rect | None:
    """Return one safe source region containing all intrinsic visual content."""
    visual_rects: list[pymupdf.Rect] = []
    for drawing in page.get_drawings():
        rect = pymupdf.Rect(drawing["rect"]) & question_clip
        if not rect.is_empty and (rect.width > 12 or rect.height > 12):
            visual_rects.append(rect)
    for block in page.get_text("dict").get("blocks", []):
        if block.get("type") != 1:
            continue
        rect = pymupdf.Rect(block["bbox"]) & question_clip
        if not rect.is_empty:
            visual_rects.append(rect)
    if not visual_rects:
        return None

    region = pymupdf.Rect(visual_rects[0])
    for rect in visual_rects[1:]:
        region |= rect

    # Include labels, values, units and option letters immediately attached to
    # a visual. The complete question crop remains the source of truth.
    nearby = pymupdf.Rect(
        max(question_clip.x0, region.x0 - 90),
        max(question_clip.y0, region.y0 - 55),
        min(question_clip.x1, region.x1 + 90),
        min(question_clip.y1, region.y1 + 55),
    )
    for block in page.get_text("blocks", sort=True):
        block_rect = pymupdf.Rect(block[:4]) & question_clip
        if block_rect.is_empty or not block[4].strip():
            continue
        if not (block_rect & nearby).is_empty:
            region |= block_rect

    return pymupdf.Rect(
        max(question_clip.x0, region.x0 - 8),
        max(question_clip.y0, region.y0 - 8),
        min(question_clip.x1, region.x1 + 8),
        min(question_clip.y1, region.y1 + 8),
    )


def display_mode(page: pymupdf.Page, question_clip: pymupdf.Rect, visual: pymupdf.Rect | None) -> str:
    if visual is None:
        return "text_options"
    option_positions: list[tuple[str, pymupdf.Rect]] = []
    for block in page.get_text("dict", clip=question_clip, sort=True).get("blocks", []):
        for line in block.get("lines", []):
            text = "".join(str(span.get("text", "")) for span in line.get("spans", [])).strip()
            match = re.match(r"^([A-D])(?:\s|$)", text)
            if match:
                option_positions.append((match.group(1), pymupdf.Rect(line["bbox"])))
    if len(option_positions) == 4:
        xs = [rect.x0 for _label, rect in option_positions]
        overlaps_visual = any(rect.y0 <= visual.y1 and rect.y1 >= visual.y0 for _label, rect in option_positions)
        if overlaps_visual or max(xs) - min(xs) > 90:
            return "image_question"
    return "text_diagram_options"


def render_figure(
    page: pymupdf.Page,
    source_rect: pymupdf.Rect,
    output_path: Path,
    dpi: int,
    border_pixels: int = 64,
) -> None:
    source = page.get_pixmap(
        matrix=pymupdf.Matrix(dpi / 72, dpi / 72),
        clip=source_rect,
        colorspace=pymupdf.csRGB,
        alpha=False,
    )
    canvas = pymupdf.Pixmap(
        pymupdf.csRGB,
        pymupdf.IRect(0, 0, source.width + 2 * border_pixels, source.height + 2 * border_pixels),
        False,
    )
    canvas.clear_with(255)
    source.set_origin(border_pixels, border_pixels)
    canvas.copy(source, source.irect)
    temporary = output_path.with_suffix(".tmp.png")
    canvas.save(temporary)
    temporary.replace(output_path)


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

            for stale_figure in destination.glob(f"figure_{question.number:02d}_*.png"):
                stale_figure.unlink()
            visual_rect = visual_source_rect(page, clip)
            figures: list[dict] = []
            if visual_rect is not None:
                figure_path = destination / f"figure_{question.number:02d}_01.png"
                render_figure(page, visual_rect, figure_path, dpi=dpi)
                figures.append({
                    "id": f"fig_{question.number:02d}_01",
                    "file": figure_path.name,
                    "source_page": question.page_number + 1,
                    "source_bbox_points": [round(value, 2) for value in visual_rect],
                    "canvas_border_pixels": 64,
                    "extraction_method": "vector-raster-visual-bounds",
                })
                written.append(figure_path)

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
                "display_mode": display_mode(page, clip, visual_rect),
                "display_source": "question_image",
                "rebuild_status": "not_rebuilt",
                "has_visual_content": visual_rect is not None,
                "has_diagram": visual_rect is not None,
                "figures": figures,
                "review_flags": [],
            }
            json_path = destination / f"question_{question.number:02d}.json"
            json_path.write_text(
                json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            written.extend((image_path, json_path, text_path))

    figure_count = sum(1 for path in written if path.name.startswith("figure_"))
    print(
        f"{pdf.name}: wrote {len(questions)} MCQ PNG, JSON, and TXT sets "
        f"with {figure_count} visual assets to {destination}"
    )
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
