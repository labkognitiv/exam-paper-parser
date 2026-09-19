#!/usr/bin/env python3
"""Cambridge Physics 9702 Paper 4 Unified Theory Dual Parser.

Within each question directory (question_XX/):
- question_compact.png: screen-optimized layout collapsing empty answer spaces
- question_printable.png: authentic student-faced layout retaining full answer spaces
- question_printable.pdf: printable single-question PDF
- markscheme.png: question-specific mark scheme slice
- figure_X_Y.png: extracted diagram/graph figures belonging to this question
- question.txt: cleaned text for question OCR

At the paper folder root:
- paper_compact.pdf: compiled compact whole-paper PDF
- paper_printable.pdf: compiled printable whole-paper PDF
- paper_markscheme.pdf: compiled whole-paper mark scheme PDF
- source/: raw QP and MS PDFs

Zero em dashes, zero en dashes.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
import pymupdf

ROOT_SRC = next(
    (p for p in Path(__file__).resolve().parents if (p / "src").is_dir() and (p / "pyproject.toml").is_file()),
    Path(__file__).resolve().parents[3],
) / "src"
if str(ROOT_SRC) not in sys.path:
    sys.path.insert(0, str(ROOT_SRC))

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from question_compactor.question_compactor import extract_figures
from slice_mark_scheme import slice_mark_scheme

REPO_ROOT = next(
    (p for p in Path(__file__).resolve().parents if (p / "subjects").is_dir() and (p / "pyproject.toml").is_file()),
    Path(__file__).resolve().parents[3],
)
PHYSICS_BASE = REPO_ROOT / "subjects/physics/9702/past papers"

START_RE = re.compile(r"^\s*([1-9]|1[0-5])\s+(?:\([a-z]\)|[A-Za-z(\"'])")
ANSWER_PAGE_START_RE = re.compile(
    r"Answer all the questions in the spaces provided\.\s*([1-9]|1[0-5])\s+\([a-z]\)",
    re.IGNORECASE,
)
MID_PAGE_START_RE = re.compile(r"^\s*([1-9]|1[0-5])\s+(?:\(a\)|[A-Z])", re.IGNORECASE)
TOTAL_RE = re.compile(r"\[\s*Total\s*:\s*(\d+)\s*\]", re.IGNORECASE)
TRAILING_MARK_RE = re.compile(r"\[(\d+)\]\s*$")
DOTS_RE = re.compile(r"\.{6,}")
BLANK_RE = re.compile(r"^\s*BLANK PAGE\s*$", re.IGNORECASE)
PAPER_NAME_RE = re.compile(
    r"^(?P<subject>\d{4})_(?P<session>[msw])(?P<year>\d{2})_qp_(?P<variant>\d{2})$",
    re.IGNORECASE,
)
FOOTER_RE = re.compile(
    r"(?:©\s*UCLES|©\s*Cambridge|\[Turn\s*over|Permission\s+to\s+reproduce|BLANK\s+PAGE|\b9702/\d{2}/|\b9701/\d{2}/)",
    re.IGNORECASE,
)
PAGE_NUM_RE = re.compile(r"^\s*\d{1,2}\s*$")
BARCODE_TEXT_RE = re.compile(r"^\s*\*\s*\d+[\s\d]*\*\s*$")
MARGIN_RE = re.compile(r"DO NOT WRITE IN THIS MARGIN", re.IGNORECASE)


def is_barcode_span(txt: str, bbox: tuple[float, float, float, float]) -> bool:
    """Detect whether a text span is a 1D barcode or 2D DataMatrix code."""
    if 55 < bbox[1] < 770 and 40 < bbox[0] < 540:
        return False
    if any(ord(c) in (1, 2, 3, 4, 5, 6, 7, 8, 14, 15, 16) for c in txt):
        letters = sum(1 for c in txt if c.isalpha())
        if letters < 3:
            return True
    if bbox[1] > 780:
        high_chars = sum(1 for c in txt if ord(c) > 255)
        ascii_letters = sum(1 for c in txt if c.isalpha() and ord(c) < 128)
        if high_chars > 3 and ascii_letters == 0:
            return True
    return False


def redact_page_unwanted_elements(page: pymupdf.Page) -> None:
    """Mask all barcodes, QR codes, page numbers, running footers, and margin text."""
    width, height = page.rect.width, page.rect.height

    # 1. Header and Margin exclusion zones
    page.add_redact_annot(pymupdf.Rect(0, 0, width, 52), fill=(1, 1, 1))
    page.add_redact_annot(pymupdf.Rect(0, 0, 36, height), fill=(1, 1, 1))
    page.add_redact_annot(pymupdf.Rect(width - 36, 0, width, height), fill=(1, 1, 1))

    # 2. Text elements
    d = page.get_text("dict")
    for b in d["blocks"]:
        if "lines" not in b:
            continue
        for l in b["lines"]:
            for s in l["spans"]:
                txt = s["text"].strip()
                bb = s["bbox"]
                bbox = pymupdf.Rect(bb[0] - 2, bb[1] - 2, bb[2] + 2, bb[3] + 2)

                if is_barcode_span(txt, bb):
                    page.add_redact_annot(bbox, fill=(1, 1, 1))
                elif BARCODE_TEXT_RE.match(txt) and bbox.y0 < 55:
                    page.add_redact_annot(bbox, fill=(1, 1, 1))
                elif PAGE_NUM_RE.match(txt) and bbox.y0 < 55 and 260 < bbox.x0 < 340:
                    page.add_redact_annot(bbox, fill=(1, 1, 1))
                elif FOOTER_RE.search(txt) and bbox.y0 > 650:
                    page.add_redact_annot(bbox, fill=(1, 1, 1))
                    if "permission to reproduce" in txt.lower():
                        page.add_redact_annot(pymupdf.Rect(0, bbox.y0 - 10, width, height), fill=(1, 1, 1))
                elif MARGIN_RE.search(txt):
                    page.add_redact_annot(bbox, fill=(1, 1, 1))

    # 3. Vector drawings strictly within outer margins (registration marks, alignment marks)
    for d_item in page.get_drawings():
        r = d_item["rect"]
        if r.y1 <= 52 or r.y0 >= 795 or r.x1 <= 40 or r.x0 >= width - 40:
            page.add_redact_annot(pymupdf.Rect(r.x0 - 1, r.y0 - 1, r.x1 + 1, r.y1 + 1), fill=(1, 1, 1))

    page.apply_redactions()


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
    cleaned = re.sub(r"[\x00-\x1f\x7f-\x9f]", " ", text)
    return " ".join(cleaned.split())


def paper_metadata(qp_path: Path) -> dict:
    stem = qp_path.stem
    match = PAPER_NAME_RE.match(stem)
    if not match:
        return {
            "source_filename": qp_path.name,
            "subject_code": "9702",
            "year": None,
            "session": None,
            "session_code": None,
            "variant": None,
            "paper_code": stem.replace("_qp_", "_"),
        }
    session_code = match.group("session").lower()
    sessions = {"m": "February/March", "s": "May/June", "w": "October/November"}
    year = 2000 + int(match.group("year"))
    variant = int(match.group("variant"))
    return {
        "source_filename": qp_path.name,
        "subject_code": match.group("subject"),
        "year": year,
        "session": sessions[session_code],
        "session_code": session_code,
        "variant": variant,
        "paper_code": f"{match.group('subject')}_{session_code}{match.group('year')}_{match.group('variant')}",
    }


def detect_questions(doc: pymupdf.Document) -> list[Question]:
    starts: list[tuple[int, int, float]] = []
    expected = 1
    for page_number, page in enumerate(doc):
        if page_number == 0:
            continue
        for block in page.get_text("blocks", sort=True):
            x0, y0, _x1, _y1, text = block[:5]
            if x0 > 80 or y0 > min(page.rect.height - 72, 770):
                continue
            block_text = normalized(text)
            match = START_RE.match(block_text) if y0 <= 135 else MID_PAGE_START_RE.match(block_text)
            if match is None and y0 <= 135:
                match = ANSWER_PAGE_START_RE.search(block_text)
            if match:
                number = int(match.group(1))
                if number == expected:
                    starts.append((number, page_number, max(50.0, y0 - 4)))
                    expected += 1

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
    body = pymupdf.Rect(40, 58, width - 40, min(height - 45, 796))
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
) -> tuple[Path, pymupdf.Document]:
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

    png_path = output_dir / "question_compact.png"
    temp_png = png_path.with_suffix(".tmp.png")
    pix = target.get_pixmap(matrix=pymupdf.Matrix(dpi / 72, dpi / 72), colorspace=pymupdf.csRGB, alpha=False)
    pix.save(temp_png)
    temp_png.replace(png_path)

    return png_path, output


def render_printable_question(
    source_doc: pymupdf.Document,
    question: Question,
    output_dir: Path,
    *,
    dpi: int = 150,
) -> tuple[Path, Path]:
    slices: list[tuple[int, pymupdf.Rect]] = []
    width = source_doc[0].rect.width

    for page_number in range(question.start_page, question.end_page + 1):
        page = source_doc[page_number]
        blocks = page.get_text("blocks", sort=True)
        valid_blocks = [
            b for b in blocks 
            if b[4].strip() and not BLANK_RE.match(normalized(b[4]))
        ]

        # Scope blocks on shared boundary pages
        if page_number == question.start_page:
            valid_blocks = [b for b in valid_blocks if b[3] >= question.start_y]
            min_start_y = max(58.0, question.start_y - 6.0) if question.start_y > 100.0 else 58.0
            y0 = max(min_start_y, question.start_y)
        else:
            min_start_y = 58.0
            if valid_blocks:
                first_y0 = min(b[1] for b in valid_blocks)
                y0 = max(58.0, first_y0 - 6.0)
            else:
                y0 = 60.0

        max_end_y = question.end_y if (page_number == question.end_page and question.end_y is not None) else 796.0
        if page_number == question.end_page and question.end_y is not None:
            valid_blocks = [b for b in valid_blocks if b[1] <= question.end_y]

        for d_item in page.get_drawings():
            r = d_item["rect"]
            if min_start_y <= r.y0 < y0 and r.x0 >= 36.0 and r.x1 <= width - 36.0:
                y0 = max(min_start_y, r.y0 - 6.0)
        for img_info in page.get_image_info():
            r = img_info["bbox"]
            if min_start_y <= r[1] < y0 and r[0] >= 36.0 and r[2] <= width - 36.0:
                y0 = max(min_start_y, r[1] - 6.0)

        found_total = False
        if page_number == question.end_page:
            if question.end_y is not None:
                y1 = question.end_y
            else:
                for b in valid_blocks:
                    if TOTAL_RE.search(b[4]):
                        y1 = min(max_end_y, b[3] + 8.0)
                        found_total = True
                        break
                if not found_total:
                    y1 = min(max_end_y, max((b[3] for b in valid_blocks), default=780.0) + 8.0)
        else:
            y1 = min(max_end_y, max((b[3] for b in valid_blocks), default=780.0) + 8.0)

        if not found_total:
            for d_item in page.get_drawings():
                r = d_item["rect"]
                if y1 < r.y1 <= max_end_y and r.x0 >= 36.0 and r.x1 <= width - 36.0:
                    y1 = min(max_end_y, r.y1 + 8.0)
            for img_info in page.get_image_info():
                r = img_info["bbox"]
                if y1 < r[3] <= max_end_y and r[0] >= 36.0 and r[2] <= width - 36.0:
                    y1 = min(max_end_y, r[3] + 8.0)

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

    pdf_path = output_dir / "question_printable.pdf"
    png_path = output_dir / "question_printable.png"
    output.save(pdf_path)

    temp_png = png_path.with_suffix(".tmp.png")
    pix = target.get_pixmap(matrix=pymupdf.Matrix(dpi / 72, dpi / 72), colorspace=pymupdf.csRGB, alpha=False)
    pix.save(temp_png)
    temp_png.replace(png_path)
    output.close()

    return png_path, pdf_path


def extract_question_figures_all(
    doc: pymupdf.Document,
    question: Question,
    output_dir: Path,
    *,
    dpi: int = 150,
) -> list[dict]:
    figures: list[dict] = []
    seen: set[str] = set()
    for page_number in range(question.start_page, question.end_page + 1):
        page = doc[page_number]
        written, _ = extract_figures(page, output_dir, dpi=dpi)
        for fig_path in written:
            m = re.search(r"figure_(\d+)_(\d+)\.png", fig_path.name)
            if m and int(m.group(1)) != question.number:
                if fig_path.exists():
                    fig_path.unlink()
                continue
            if fig_path.name in seen:
                continue
            seen.add(fig_path.name)
            if m:
                fig_id = f"fig_{m.group(1)}_{m.group(2)}"
                fig_label = f"Fig. {m.group(1)}.{m.group(2)}"
            else:
                fig_id = fig_path.stem
                fig_label = fig_path.stem
            figures.append({
                "id": fig_id,
                "label": fig_label,
                "file": fig_path.name,
                "path": fig_path.name,
            })
    return figures


def extract_theory_question_text(doc: pymupdf.Document, question: Question) -> str:
    lines: list[str] = []
    for pno in range(question.start_page, question.end_page + 1):
        page = doc[pno]
        y0 = question.start_y if pno == question.start_page else 45.0
        y1 = question.end_y if (pno == question.end_page and question.end_y is not None) else (page.rect.height - 45.0)
        clip = pymupdf.Rect(36.0, y0, page.rect.width - 36.0, y1)
        txt = page.get_text("text", clip=clip)
        for line in txt.splitlines():
            cleaned = re.sub(r"\.{3,}\s*", "", line).strip()
            # Normalize dashes to standard ASCII hyphen (zero en/em dashes)
            cleaned = cleaned.replace("\u2014", " - ").replace("\u2013", "-").replace("\u2212", "-")
            if cleaned and not re.match(r"^\[Total:\s*\d+\]", cleaned):
                lines.append(cleaned)
    return "\n".join(lines).strip()


def process_theory_paper(qp_pdf: Path, ms_pdf: Path, paper_dir: Path, dpi: int = 150) -> None:
    paper_meta = paper_metadata(qp_pdf)
    paper_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n================================================================================")
    print(f"PROCESSING PHYSICS THEORY PAPER: {paper_meta['paper_code']}")
    print(f"QP: {qp_pdf.name} | MS: {ms_pdf.name}")
    print(f"Directory: {paper_dir}")
    print(f"================================================================================")

    doc = pymupdf.open(qp_pdf)
    
    # Clean base document with all barcodes, QR codes, page numbers, footers and margin text purged
    clean_source = pymupdf.open()
    clean_source.insert_pdf(doc)
    for page in clean_source:
        redact_page_unwanted_elements(page)

    questions = detect_questions(clean_source)
    print(f"Detected {len(questions)} questions in {qp_pdf.name}:")
    for q in questions:
        print(f"  Q{q.number}: pages {q.start_page + 1}-{q.end_page + 1}")

    # Clean up any stale question directories from previous runs
    valid_q_dir_names = {f"question_{q.number:02d}" for q in questions}
    for old_q_dir in paper_dir.glob("question_*"):
        if old_q_dir.is_dir() and old_q_dir.name not in valid_q_dir_names:
            shutil.rmtree(old_q_dir)

    sanitized_doc = make_compact_sanitized_copy(clean_source)

    compiled_compact_doc = pymupdf.open()
    compiled_printable_doc = pymupdf.open()

    for q in questions:
        q_dir = paper_dir / f"question_{q.number:02d}"
        q_dir.mkdir(parents=True, exist_ok=True)

        # 1. Dual renders
        compact_png, q_compact_doc = render_compact_question(sanitized_doc, q, q_dir, dpi=dpi)
        printable_png, printable_pdf = render_printable_question(clean_source, q, q_dir, dpi=dpi)

        # Append to whole-paper compilations
        compiled_compact_doc.insert_pdf(q_compact_doc)
        q_compact_doc.close()
        with pymupdf.open(printable_pdf) as q_print_pdf:
            compiled_printable_doc.insert_pdf(q_print_pdf)

        # 2. Extract Figures (from unredacted doc to preserve clean diagram boundaries)
        figures = extract_question_figures_all(doc, q, q_dir, dpi=dpi)

        # 3. Extract and save clean OCR question text
        question_text = extract_theory_question_text(clean_source, q)
        text_path = q_dir / "question.txt"
        temp_text = text_path.with_suffix(".tmp.txt")
        temp_text.write_text(question_text + "\n", encoding="utf-8")
        temp_text.replace(text_path)

        print(f"  ✓ Q{q.number:02d}: Compact ({compact_png.name}), Printable ({printable_png.name}), Figures ({len(figures)}), Text ({len(question_text)} chars)")

    # 3. Save compiled whole-paper PDFs at paper root
    compiled_compact_path = paper_dir / "paper_compact.pdf"
    temp_compact = compiled_compact_path.with_suffix(".tmp.pdf")
    compiled_compact_doc.save(temp_compact)
    temp_compact.replace(compiled_compact_path)
    compiled_compact_doc.close()

    compiled_printable_path = paper_dir / "paper_printable.pdf"
    temp_printable = compiled_printable_path.with_suffix(".tmp.pdf")
    compiled_printable_doc.save(temp_printable)
    temp_printable.replace(compiled_printable_path)
    compiled_printable_doc.close()

    sanitized_doc.close()
    clean_source.close()
    doc.close()

    # 4. Mark Scheme Slicing (writes markscheme.png directly into each question_XX directory)
    print("  Slicing Mark Scheme...")
    valid_q_nums = [q.number for q in questions]
    ms_slices = slice_mark_scheme(
        ms_pdf, paper_dir, dpi=dpi, per_question_dirs=True, valid_questions=valid_q_nums
    )
    print(f"  ✓ Mark Scheme sliced: {len(ms_slices)} question slices in {paper_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Unified Cambridge Physics 9702 Paper 4 Dual Parser")
    parser.add_argument("--qp", type=Path, help="Path to question paper PDF")
    parser.add_argument("--ms", type=Path, help="Path to mark scheme PDF")
    parser.add_argument("--dir", type=Path, help="Paper directory")
    parser.add_argument("--dpi", type=int, default=150, help="Rendering DPI (default: 150)")
    args = parser.parse_args()

    if args.qp and args.ms and args.dir:
        process_theory_paper(args.qp, args.ms, args.dir, dpi=args.dpi)
    else:
        print("Usage: slice_p4_paper.py --qp <qp_pdf> --ms <ms_pdf> --dir <paper_dir>")


if __name__ == "__main__":
    main()
