"""Cambridge Physics 9702 Paper 2 Dual Parser.

Produces two distinct versions for each question:
1. Compact (Internal):
   - Collapses empty answer/working space
   - Removes dotted answer lines and SI unit prompt lines
   - Preserves mark allocations [X] and [Total: Y]
   - Keeps all figures and diagrams inline within the question
2. Printable (Student-Faced):
   - Merges the question across its source pages into a unified document
   - Strips page headers (page numbers, paper code) and footers (copyright, [Turn over])
   - Retains 100% of authentic answer spaces, answer lines, SI unit prompts, and figures
   - Suitable for direct printing and student solving
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
from dataclasses import dataclass
import pymupdf

ROOT_SRC = Path(__file__).resolve().parents[3] / "src"
if str(ROOT_SRC) not in sys.path:
    sys.path.insert(0, str(ROOT_SRC))
from question_compactor.question_compactor import extract_figures


START_RE = re.compile(r"^\s*(\d{1,2})\s+(?:\([a-z]\)|[A-Z])")
ANSWER_PAGE_START_RE = re.compile(
    r"Answer all the questions in the spaces provided\.\s*(\d{1,2})\s+\([a-z]\)",
    re.IGNORECASE,
)
MID_PAGE_START_RE = re.compile(r"^\s*(\d{1,2})\s+\(a\)", re.IGNORECASE)
TOTAL_RE = re.compile(r"\[\s*Total\s*:\s*\d+\s*\]", re.IGNORECASE)
DOTS_RE = re.compile(r"\.{6,}")
BLANK_RE = re.compile(r"^\s*BLANK PAGE\s*$", re.IGNORECASE)


@dataclass(frozen=True)
class Question:
    number: int
    start_page: int
    end_page: int
    start_y: float
    end_y: float | None


@dataclass(frozen=True)
class Band:
    page_number: int
    rect: pymupdf.Rect


def normalized(text: str) -> str:
    return " ".join(text.replace("\x00", " ").split())


def detect_questions(doc: pymupdf.Document) -> list[Question]:
    starts: list[tuple[int, int, float]] = []
    for page_number, page in enumerate(doc):
        for block in page.get_text("blocks", sort=True):
            x0, y0, _x1, _y1, text = block[:5]
            if x0 > 90 or y0 > min(page.rect.height - 72, 770):
                continue
            block_text = normalized(text)
            match = START_RE.match(block_text) if y0 <= 135 else MID_PAGE_START_RE.match(block_text)
            if match is None and y0 <= 135:
                match = ANSWER_PAGE_START_RE.search(block_text)
            if match:
                number = int(match.group(1))
                if not starts or number > starts[-1][0]:
                    starts.append((number, page_number, max(50.0, y0 - 4)))

    if not starts:
        raise ValueError("No numbered questions detected in PDF.")

    questions: list[Question] = []
    for index, (number, start_page, start_y) in enumerate(starts):
        if index + 1 < len(starts):
            _next_num, next_page, next_y = starts[index + 1]
            shares_next_page = next_page == start_page or next_y > 135
            end_page = next_page if shares_next_page else next_page - 1
            end_y = next_y if shares_next_page else None
        else:
            end_page = len(doc) - 1
            end_y = None

        for page_number in range(start_page, end_page + 1):
            page = doc[page_number]
            clip_y0 = start_y if page_number == start_page else 0
            clip_y1 = end_y if page_number == end_page and end_y is not None else page.rect.height
            scoped_text = normalized(page.get_text("text", clip=pymupdf.Rect(0, clip_y0, page.rect.width, clip_y1)))
            if TOTAL_RE.search(scoped_text):
                end_page = page_number
                break
        questions.append(Question(number, start_page, end_page, start_y, end_y))
    return questions


def make_compact_sanitized_copy(source: pymupdf.Document) -> pymupdf.Document:
    """Create a sanitized copy where answer lines and answer prompt/units are masked."""
    sanitized = pymupdf.open()
    sanitized.insert_pdf(source)

    for page in sanitized:
        blocks = page.get_text("blocks", sort=True)
        for block in blocks:
            x0, y0, x1, y1, text = block[:5]
            clean = normalized(text)
            if not DOTS_RE.search(clean):
                continue

            lines = [line.strip() for line in text.strip().splitlines() if line.strip()]
            # Multiple dotted lines are fine, but reject prompts that have substantial text
            # before the dots in a large multi-line block
            prompt_lines = [line for line in lines if not DOTS_RE.search(line)]
            if len(prompt_lines) > 1:
                continue

            mark_match = re.search(r"\[(\d+)\]\s*$", clean)
            mask = pymupdf.Rect(max(40, x0 - 2), y0 - 2, min(page.rect.width - 40, x1 + 2), y1 + 2)
            page.draw_rect(mask, color=None, fill=(1, 1, 1), overlay=True)
            if mark_match:
                label = f"[{mark_match.group(1)}]"
                page.insert_text(
                    (page.rect.width - 62, y1 - 1),
                    label,
                    fontsize=8,
                    fontname="helv",
                    color=(0, 0, 0),
                    overlay=True,
                )
    return sanitized


def ink_rows(page: pymupdf.Page, clip: pymupdf.Rect, scale: float = 1.5) -> list[bool]:
    pix = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), clip=clip, colorspace=pymupdf.csGRAY, alpha=False)
    samples = pix.samples
    rows: list[bool] = []
    threshold = max(2, int(pix.width * 0.0015))
    for row in range(pix.height):
        start = row * pix.stride
        data = samples[start : start + pix.width]
        rows.append(sum(value < 244 for value in data) >= threshold)
    return rows


def merge_intervals(intervals: list[tuple[float, float]], gap: float) -> list[tuple[float, float]]:
    if not intervals:
        return []
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        old_start, old_end = merged[-1]
        if start - old_end <= gap:
            merged[-1] = (old_start, max(old_end, end))
        else:
            merged.append((start, end))
    return merged


def content_bands(page: pymupdf.Page, page_number: int) -> list[Band]:
    width, height = page.rect.width, page.rect.height
    body = pymupdf.Rect(40, 55, width - 40, min(height - 65, 775))
    if BLANK_RE.match(normalized(page.get_text("text"))):
        return []

    scale = 1.5
    occupied = ink_rows(page, body, scale=scale)
    raw: list[tuple[float, float]] = []
    start: int | None = None
    for index, is_ink in enumerate(occupied + [False]):
        if is_ink and start is None:
            start = index
        elif not is_ink and start is not None:
            y0 = body.y0 + start / scale
            y1 = body.y0 + index / scale
            raw.append((max(body.y0, y0 - 3), min(body.y1, y1 + 3)))
            start = None

    # Merge ordinary spacing (<= 20 pt), collapse blank working space (> 20 pt)
    merged = merge_intervals(raw, gap=20)
    result: list[Band] = []
    for y0, y1 in merged:
        if y1 - y0 < 2:
            continue
        result.append(Band(page_number, pymupdf.Rect(body.x0, y0, body.x1, y1)))
    return result


def render_compact_question(
    sanitized_doc: pymupdf.Document,
    question: Question,
    output_dir: Path,
    *,
    dpi: int = 150,
) -> Path:
    """Version 1: Compact question image with figures, without answer spaces/lines/prompts."""
    bands: list[Band] = []
    for page_number in range(question.start_page, question.end_page + 1):
        for band in content_bands(sanitized_doc[page_number], page_number):
            y0 = question.start_y if page_number == question.start_page else band.rect.y0
            y1 = question.end_y if page_number == question.end_page and question.end_y is not None else band.rect.y1
            clipped = pymupdf.Rect(
                band.rect.x0,
                max(band.rect.y0, y0),
                band.rect.x1,
                min(band.rect.y1, y1),
            )
            if clipped.height >= 2:
                bands.append(Band(page_number, clipped))

    if not bands:
        raise ValueError(f"Question {question.number} contains no printable bands.")

    margin = 24.0
    band_gap = 8.0
    content_width = max(band.rect.width for band in bands)
    page_width = content_width + margin * 2
    page_height = margin * 2 + sum(band.rect.height for band in bands) + band_gap * (len(bands) - 1)

    output = pymupdf.open()
    target = output.new_page(width=page_width, height=page_height)
    y = margin
    for band in bands:
        dest = pymupdf.Rect(margin, y, margin + band.rect.width, y + band.rect.height)
        target.show_pdf_page(dest, sanitized_doc, band.page_number, clip=band.rect, keep_proportion=False)
        y += band.rect.height + band_gap

    png_path = output_dir / f"question_{question.number:02d}_compact.png"
    temp_png = png_path.with_suffix(".tmp.png")
    pix = target.get_pixmap(matrix=pymupdf.Matrix(dpi / 72, dpi / 72), colorspace=pymupdf.csRGB, alpha=False)
    pix.save(temp_png)
    temp_png.replace(png_path)
    output.close()
    return png_path


def render_printable_question(
    source_doc: pymupdf.Document,
    question: Question,
    output_dir: Path,
    *,
    dpi: int = 150,
) -> Path:
    """Version 2: Merged question image keeping authentic answer spaces, answer lines, and prompts."""
    slices: list[tuple[int, pymupdf.Rect]] = []
    width = source_doc[0].rect.width

    for page_number in range(question.start_page, question.end_page + 1):
        page = source_doc[page_number]
        blocks = page.get_text("blocks", sort=True)

        # Content top: below page number header (~35-52)
        y0 = max(55.0, question.start_y if page_number == question.start_page else 55.0)

        # Content bottom: before footer (~790) or after [Total: X]
        y1 = 780.0
        if page_number == question.end_page:
            found_total = False
            for b in blocks:
                if TOTAL_RE.search(b[4]):
                    y1 = min(780.0, b[3] + 16.0)
                    found_total = True
                    break
            if not found_total:
                # If no total found, take bottom of last block before footer
                last_bottom = max((b[3] for b in blocks if b[3] < 785.0), default=780.0)
                y1 = min(780.0, last_bottom + 10.0)
        else:
            last_bottom = max((b[3] for b in blocks if b[3] < 785.0), default=780.0)
            y1 = min(780.0, last_bottom + 10.0)

        if y1 > y0 + 10:
            clip = pymupdf.Rect(36.0, y0, width - 36.0, y1)
            slices.append((page_number, clip))

    if not slices:
        raise ValueError(f"Question {question.number} printable slice is empty.")

    margin = 20.0
    slice_gap = 12.0
    total_height = margin * 2 + sum(clip.height for _, clip in slices) + slice_gap * (len(slices) - 1)

    output = pymupdf.open()
    target = output.new_page(width=width, height=total_height)
    y = margin
    for page_number, clip in slices:
        dest = pymupdf.Rect(clip.x0, y, clip.x1, y + clip.height)
        target.show_pdf_page(dest, source_doc, page_number, clip=clip, keep_proportion=False)
        y += clip.height + slice_gap

    pdf_path = output_dir / f"question_{question.number:02d}_printable.pdf"
    png_path = output_dir / f"question_{question.number:02d}_printable.png"
    output.save(pdf_path)
    temp_png = png_path.with_suffix(".tmp.png")
    pix = target.get_pixmap(matrix=pymupdf.Matrix(dpi / 72, dpi / 72), colorspace=pymupdf.csRGB, alpha=False)
    pix.save(temp_png)
    temp_png.replace(png_path)
    output.close()
    return png_path


def extract_question_figures(
    doc: pymupdf.Document,
    question: Question,
    output_dir: Path,
    *,
    dpi: int = 150
) -> list[dict]:
    """Extract standalone captioned diagram/graph PNGs for this question."""
    figures: list[dict] = []
    seen: set[str] = set()
    for page_number in range(question.start_page, question.end_page + 1):
        page = doc[page_number]
        written, _ = extract_figures(page, output_dir, dpi=dpi)
        for fig_path in written:
            if fig_path.name in seen:
                continue
            seen.add(fig_path.name)
            m = re.search(r"figure_(\d+)_(\d+)\.png", fig_path.name)
            if m:
                if int(m.group(1)) != question.number:
                    continue
                fig_id = f"fig_{m.group(1)}_{m.group(2)}"
                fig_label = f"Fig. {m.group(1)}.{m.group(2)}"
            else:
                fig_id = fig_path.stem
                fig_label = fig_path.stem
            figures.append({
                "id": fig_id,
                "label": fig_label,
                "file": fig_path.name,
                "path": str(fig_path)
            })
    return figures


def process_paper(input_pdf: Path, output_dir: Path, dpi: int = 150) -> None:
    doc = pymupdf.open(input_pdf)
    questions = detect_questions(doc)
    print(f"Loaded {input_pdf.name}: detected {len(questions)} questions")
    for q in questions:
        print(f"  Q{q.number}: pages {q.start_page+1}-{q.end_page+1}")

    output_dir.mkdir(parents=True, exist_ok=True)
    sanitized_doc = make_compact_sanitized_copy(doc)

    for q in questions:
        compact_path = render_compact_question(sanitized_doc, q, output_dir, dpi=dpi)
        printable_path = render_printable_question(doc, q, output_dir, dpi=dpi)
        print(f"  Q{q.number:02d} -> Compact: {compact_path.name} | Printable: {printable_path.name}")

    sanitized_doc.close()
    doc.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="P2 Dual Question Parser (Compact & Printable)")
    parser.add_argument("pdf_path", type=Path, nargs="?", help="Path to P2 question paper PDF")
    parser.add_argument("--output-dir", type=Path, default=Path("output"), help="Output directory")
    parser.add_argument("--dpi", type=int, default=150, help="Rendering DPI (default: 150)")
    args = parser.parse_args()

    default_pdf = Path(
        "/Users/abdullahaftab/Kognitiv/exam-paper-parser/subjects/physics/9702/past papers/p2/2023/may-june/variant-2/source/9702_s23_qp_22.pdf"
    )
    pdf_path = args.pdf_path or default_pdf
    process_paper(pdf_path, args.output_dir, dpi=args.dpi)


if __name__ == "__main__":
    main()
