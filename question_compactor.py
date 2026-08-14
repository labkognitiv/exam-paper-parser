from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import pymupdf


START_RE = re.compile(r"^\s*(\d{1,2})\s+(?:\([a-z]\)|[A-Z])")
TOTAL_RE = re.compile(r"\[\s*Total\s*:\s*\d+\s*\]", re.IGNORECASE)
DOTS_RE = re.compile(r"\.{8,}")
BLANK_RE = re.compile(r"^\s*BLANK PAGE\s*$", re.IGNORECASE)
FIGURE_CAPTION_RE = re.compile(
    r"^Fig\.\s*(\d+)\.(\d+)(?:\s*\([^)]*\))?$", re.IGNORECASE
)
PAPER_NAME_RE = re.compile(
    r"^(?P<subject>\d{4})_(?P<session>[msw])(?P<year>\d{2})_qp_(?P<variant>\d{2})$",
    re.IGNORECASE,
)
PART_TOKEN_RE = re.compile(r"^\s*\(([a-z]+|\d+)\)\s*", re.IGNORECASE)
MARK_RE = re.compile(r"\[(\d+)\]")
FIGURE_REF_RE = re.compile(r"Fig\.\s*(\d+)\.(\d+)", re.IGNORECASE)


@dataclass(frozen=True)
class Question:
    number: int
    start_page: int
    end_page: int


@dataclass(frozen=True)
class Band:
    page_number: int
    rect: pymupdf.Rect


def normalized(text: str) -> str:
    return " ".join(text.replace("\x00", " ").split())


def detect_questions(doc: pymupdf.Document) -> list[Question]:
    starts: list[tuple[int, int]] = []
    for page_number, page in enumerate(doc):
        for block in page.get_text("blocks", sort=True):
            x0, y0, _x1, _y1, text = block[:5]
            if x0 > 90 or y0 > 135:
                continue
            match = START_RE.match(normalized(text))
            if match:
                number = int(match.group(1))
                if not starts or number > starts[-1][0]:
                    starts.append((number, page_number))
                    break

    if not starts:
        raise ValueError("No numbered questions were detected near page tops.")

    questions: list[Question] = []
    for index, (number, start_page) in enumerate(starts):
        next_start = starts[index + 1][1] if index + 1 < len(starts) else len(doc)
        end_page = next_start - 1
        for page_number in range(start_page, next_start):
            if TOTAL_RE.search(page_text(doc[page_number])):
                end_page = page_number
                break
        questions.append(Question(number, start_page, end_page))
    return questions


def page_text(page: pymupdf.Page) -> str:
    return normalized(page.get_text("text", sort=True))


def make_sanitized_copy(
    source: pymupdf.Document, *, keep_answer_lines: bool
) -> pymupdf.Document:
    sanitized = pymupdf.open()
    sanitized.insert_pdf(source)
    if keep_answer_lines:
        return sanitized

    for page in sanitized:
        for block in page.get_text("blocks", sort=True):
            x0, y0, x1, y1, text = block[:5]
            clean = normalized(text)
            if not DOTS_RE.search(clean):
                continue
            # Mask the response line, but preserve an isolated mark allocation
            # by redrawing it at the right edge when present.
            mark_match = re.search(r"\[(\d+)\]\s*$", clean)
            mask = pymupdf.Rect(max(42, x0 - 2), y0 - 2, min(page.rect.width - 42, x1 + 2), y1 + 2)
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
    # A row is inked when enough pixels are visibly non-white. This ignores
    # compression noise while retaining thin diagram strokes and text.
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
    body = pymupdf.Rect(42, 60, width - 42, min(height - 72, 770))
    if BLANK_RE.match(page_text(page)):
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

    # Merge ordinary line spacing but collapse genuine working-space gaps.
    merged = merge_intervals(raw, gap=20)
    result: list[Band] = []
    for y0, y1 in merged:
        if y1 - y0 < 2:
            continue
        result.append(Band(page_number, pymupdf.Rect(body.x0, y0, body.x1, y1)))
    return result


def extract_figures(
    page: pymupdf.Page,
    output_dir: Path,
    *,
    dpi: int,
) -> tuple[list[Path], list[pymupdf.Rect]]:
    """Render captioned vector/raster figures as separate PNG files."""
    captions: list[tuple[re.Match[str], pymupdf.Rect]] = []
    page_dict = page.get_text("dict")
    for block in page_dict["blocks"]:
        for line in block.get("lines", []):
            text = "".join(span["text"] for span in line["spans"]).strip()
            match = FIGURE_CAPTION_RE.match(text)
            if not match:
                continue
            rect = pymupdf.Rect(line["bbox"])
            # Real captions in these papers are horizontally centred. This
            # rejects prompt lines that merely begin with "Fig. 2.1".
            if abs((rect.x0 + rect.x1) / 2 - page.rect.width / 2) <= 70:
                captions.append((match, rect))

    drawing_rects: list[pymupdf.Rect] = []
    for drawing in page.get_drawings():
        rect = pymupdf.Rect(drawing["rect"])
        if rect.width >= 0.5 and rect.height >= 0.5:
            drawing_rects.append(rect)
    for block in page_dict["blocks"]:
        if block.get("type") == 1:
            drawing_rects.append(pymupdf.Rect(block["bbox"]))

    written: list[Path] = []
    diagram_rects: list[pymupdf.Rect] = []
    for match, caption in captions:
        figure_label = f"Fig. {match.group(1)}.{match.group(2)}"
        # The closest earlier text block referring to this exact figure is the
        # prompt immediately above it. It provides a safer boundary than the
        # raw vector object list, which can contain repeated source-page forms.
        reference_blocks: list[pymupdf.Rect] = []
        for block in page_dict["blocks"]:
            if block.get("type") != 0:
                continue
            block_rect = pymupdf.Rect(block["bbox"])
            block_text = " ".join(
                "".join(span["text"] for span in line["spans"])
                for line in block.get("lines", [])
            )
            if block_rect.y1 < caption.y0 - 2 and figure_label in block_text:
                reference_blocks.append(block_rect)

        if reference_blocks:
            reference = max(reference_blocks, key=lambda rect: rect.y1)
            prompt_bottom = reference.y1
            # Include immediately following wrapped lines from the same prompt,
            # even when the PDF stores them as a separate text block.
            changed = True
            while changed:
                changed = False
                for block in page_dict["blocks"]:
                    if block.get("type") != 0:
                        continue
                    rect = pymupdf.Rect(block["bbox"])
                    if prompt_bottom < rect.y0 <= prompt_bottom + 7 and rect.y1 < caption.y0:
                        prompt_bottom = rect.y1
                        changed = True
            top = prompt_bottom + 20
        else:
            top = caption.y0
            changed = True
            selected: set[int] = set()
            while changed:
                changed = False
                for index, rect in enumerate(drawing_rects):
                    if index in selected or rect.y0 >= caption.y0:
                        continue
                    if rect.y1 >= top - 24:
                        selected.add(index)
                        top = min(top, rect.y0)
                        changed = True
            if not selected:
                continue
        clip = pymupdf.Rect(
            24,
            max(0, top - 12),
            page.rect.width - 24,
            min(page.rect.height, caption.y1 + 12),
        )
        paper_number, figure_number = match.group(1), match.group(2)
        figure_path = output_dir / f"figure_{paper_number}_{figure_number}.png"
        temp_path = figure_path.with_suffix(".tmp.png")
        pix = page.get_pixmap(
            matrix=pymupdf.Matrix(dpi / 72, dpi / 72),
            clip=clip,
            alpha=False,
        )
        pix.save(temp_path)
        temp_path.replace(figure_path)
        written.append(figure_path)
        # Remove the diagram across the page width, then mask only the centred
        # caption's own horizontal extent. This preserves mark allocations such
        # as [2] that may be printed at the right edge on the same baseline.
        diagram_rects.append(
            pymupdf.Rect(clip.x0, clip.y0, clip.x1, max(clip.y0, caption.y0 - 3))
        )
        diagram_rects.append(
            pymupdf.Rect(
                max(0, caption.x0 - 5),
                max(0, caption.y0 - 3),
                min(page.rect.width, caption.x1 + 5),
                min(page.rect.height, caption.y1 + 4),
            )
        )
    return written, diagram_rects


def compact_single_page(source_doc: pymupdf.Document, source_page: pymupdf.Page) -> pymupdf.Document:
    """Collapse whitespace on an already assembled/masked question page."""
    body = pymupdf.Rect(18, 18, source_page.rect.width - 18, source_page.rect.height - 18)
    scale = 1.5
    occupied = ink_rows(source_page, body, scale=scale)
    intervals: list[tuple[float, float]] = []
    start: int | None = None
    for index, is_ink in enumerate(occupied + [False]):
        if is_ink and start is None:
            start = index
        elif not is_ink and start is not None:
            intervals.append((body.y0 + start / scale - 3, body.y0 + index / scale + 3))
            start = None
    intervals = merge_intervals(intervals, gap=20)
    if not intervals:
        raise ValueError("Question became empty after figure removal.")

    margin = 24.0
    gap = 8.0
    width = source_page.rect.width
    height = margin * 2 + sum(y1 - y0 for y0, y1 in intervals) + gap * (len(intervals) - 1)
    result = pymupdf.open()
    target = result.new_page(width=width, height=height)
    y = margin
    for y0, y1 in intervals:
        clip = pymupdf.Rect(18, max(0, y0), width - 18, min(source_page.rect.height, y1))
        destination = pymupdf.Rect(18, y, width - 18, y + clip.height)
        target.show_pdf_page(destination, source_doc, source_page.number, clip=clip, keep_proportion=False)
        y += clip.height + gap
    return result


def question_text(page: pymupdf.Page) -> str:
    """Extract readable text from the final, figure-free question page."""
    superscripts = str.maketrans(
        "0123456789+-−–=()",
        "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻⁻⁼⁽⁾",
    )
    subscripts = str.maketrans(
        "0123456789+-=()",
        "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎",
    )

    raw_lines: list[str] = []
    for block in page.get_text("dict", sort=True)["blocks"]:
        block_lines = block.get("lines", [])
        for line in block_lines:
            spans = line.get("spans", [])
            if not spans:
                continue
            base_size = max(span["size"] for span in spans)
            base_spans = [span for span in spans if span["size"] >= base_size * 0.9]
            base_origin = max(span["origin"][1] for span in base_spans)
            pieces: list[str] = []
            for span in spans:
                text = span["text"]
                if span["size"] < base_size * 0.9:
                    offset = span["origin"][1] - base_origin
                    if offset < -1:
                        text = text.translate(superscripts)
                    elif offset > 1:
                        text = text.translate(subscripts)
                pieces.append(text)
            raw_lines.append("".join(pieces))
        if block_lines:
            raw_lines.append("")

    lines: list[str] = []
    previous_blank = False
    for raw_line in raw_lines:
        line = DOTS_RE.sub("", raw_line).strip()
        line = re.sub(r"(\[\d+\])(?:\s*\1)+", r"\1", line)
        line = re.sub(r"[ \t]{2,}", " ", line)
        if not line:
            if lines and not previous_blank:
                lines.append("")
                previous_blank = True
            continue
        lines.append(line)
        previous_blank = False
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines) + "\n"


def paper_metadata(input_pdf: Path) -> dict[str, object]:
    stem = input_pdf.stem
    match = PAPER_NAME_RE.match(stem)
    if not match:
        return {
            "source_filename": input_pdf.name,
            "subject_code": None,
            "year": None,
            "session": None,
            "variant": None,
            "paper_code": stem,
            "metadata_confidence": 0.0,
        }
    session_code = match.group("session").lower()
    session_names = {"m": "February/March", "s": "May/June", "w": "October/November"}
    subject = match.group("subject")
    year = 2000 + int(match.group("year"))
    variant = int(match.group("variant"))
    return {
        "source_filename": input_pdf.name,
        "subject_code": subject,
        "year": year,
        "session": session_names[session_code],
        "session_code": session_code,
        "variant": variant,
        "paper_code": f"{subject}_{session_code}{str(year)[-2:]}_{variant:02d}",
        "metadata_confidence": 1.0,
    }


def guess_answer_type(text: str) -> tuple[str, float]:
    lower = " ".join(text.lower().split())
    if re.search(r"\b(draw|sketch|plot)\b", lower):
        return ("graph" if "graph" in lower or "variation" in lower else "drawing", 0.95)
    if "complete" in lower and "table" in lower:
        return "table", 0.9
    if "tick" in lower or "underline" in lower:
        return "selection", 0.9
    if re.search(r"\b(calculate|determine)\b", lower):
        return "numeric-with-working", 0.85
    if re.search(r"\b(show that|derive|prove)\b", lower):
        return "working", 0.9
    if re.search(r"\b(define|state|explain|describe|suggest)\b", lower):
        return "text", 0.85
    return "text", 0.5


def parse_question_parts(
    text: str,
    *,
    question_id: str,
) -> tuple[str, list[dict[str, object]], int | None]:
    nodes: list[dict[str, object]] = []
    by_path: dict[tuple[str, ...], dict[str, object]] = {}
    stem_lines: list[str] = []
    current: dict[str, object] | None = None
    current_alpha: str | None = None
    current_roman: str | None = None
    total_marks: int | None = None

    for line_number, original_line in enumerate(text.splitlines(), start=1):
        line = original_line.strip()
        total_match = re.search(r"\[Total:\s*(\d+)\]", line, re.IGNORECASE)
        if total_match:
            total_marks = int(total_match.group(1))
            continue
        if line_number == 1:
            line = re.sub(r"^\d+\s*", "", line)

        tokens: list[str] = []
        remainder = line
        while True:
            token_match = PART_TOKEN_RE.match(remainder)
            if not token_match:
                break
            tokens.append(token_match.group(1).lower())
            remainder = remainder[token_match.end():]

        for token_index, token in enumerate(tokens):
            roman_tokens = {"i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"}
            if token.isdigit():
                path = tuple(part for part in (current_alpha, current_roman, token) if part)
            elif token in roman_tokens and current_alpha is not None and not (
                token_index == 0 and len(tokens) > 1
            ):
                current_roman = token
                path = (current_alpha, token)
            else:
                current_alpha = token
                current_roman = None
                path = (token,)

            if path not in by_path:
                part_id = question_id + "_" + "_".join(path)
                parent_path = path[:-1]
                node: dict[str, object] = {
                    "id": part_id,
                    "path": list(path),
                    "label": "".join(f"({item})" for item in path),
                    "parent_id": question_id + "_" + "_".join(parent_path) if parent_path else None,
                    "display_order": len(nodes) + 1,
                    "question_text": "",
                    "marks": None,
                    "answer_type": None,
                    "answer_type_confidence": None,
                    "unit": None,
                    "figure_ids": [],
                    "figure_references": [],
                    "_lines": [],
                }
                nodes.append(node)
                by_path[path] = node
            current = by_path[path]

        mark_matches = list(MARK_RE.finditer(remainder))
        if current is not None and mark_matches:
            current["marks"] = int(mark_matches[-1].group(1))
            remainder = MARK_RE.sub("", remainder).strip()

        if remainder:
            if current is None:
                stem_lines.append(remainder)
            else:
                current["_lines"].append(remainder)

    for node in nodes:
        part_text = "\n".join(node.pop("_lines")).strip()
        node["question_text"] = part_text
        answer_type, confidence = guess_answer_type(part_text)
        node["answer_type"] = answer_type
        node["answer_type_confidence"] = confidence
        unit_matches = re.findall(r"=\s*([^=\[\]]+?)\s*(?:\[\d+\]|$)", part_text)
        if unit_matches:
            candidate = unit_matches[-1].strip()
            if candidate and len(candidate) <= 20 and not re.search(r"\d", candidate):
                node["unit"] = candidate
        refs = []
        for major, minor in FIGURE_REF_RE.findall(part_text):
            label = f"Fig. {major}.{minor}"
            if label not in refs:
                refs.append(label)
        node["figure_references"] = refs

    return "\n".join(stem_lines).strip(), nodes, total_marks


def write_question_json(
    input_pdf: Path,
    source_doc: pymupdf.Document,
    question: Question,
    output_dir: Path,
    text_path: Path,
    figure_paths: list[Path],
) -> Path:
    metadata = paper_metadata(input_pdf)
    question_id = f"{metadata['paper_code']}_q{question.number:02d}"
    stem, parts, total_marks = parse_question_parts(
        text_path.read_text(encoding="utf-8"), question_id=question_id
    )
    # The compact question crop can omit a total printed at the extreme bottom
    # of a page. Read the authoritative total from the original source pages.
    for page_number in range(question.start_page, question.end_page + 1):
        source_total = re.search(
            r"\[\s*Total\s*:\s*(\d+)\s*\]",
            page_text(source_doc[page_number]),
            re.IGNORECASE,
        )
        if source_total:
            total_marks = int(source_total.group(1))
            break
    for part in parts:
        if part["marks"] is not None:
            part["marks_source"] = "compacted_text"
        else:
            part["marks_source"] = None

    # If one and only one answerable leaf part lost its mark at a page boundary,
    # the authoritative printed total determines that missing value exactly.
    known_marks = sum(int(part["marks"]) for part in parts if part["marks"] is not None)
    leaf_parts = []
    for part in parts:
        path = tuple(part["path"])
        has_child = any(
            len(other["path"]) > len(path) and tuple(other["path"][: len(path)]) == path
            for other in parts
        )
        if not has_child:
            leaf_parts.append(part)
    unmarked_leaves = [part for part in leaf_parts if part["marks"] is None]
    missing_marks = total_marks - known_marks if total_marks is not None else 0
    if len(unmarked_leaves) == 1 and 0 < missing_marks <= 5:
        unmarked_leaves[0]["marks"] = missing_marks
        unmarked_leaves[0]["marks_source"] = "reconciled_from_printed_total"
    figures: list[dict[str, object]] = []
    for figure_path in figure_paths:
        match = re.match(r"figure_(\d+)_(\d+)\.png$", figure_path.name)
        if not match:
            continue
        label = f"Fig. {match.group(1)}.{match.group(2)}"
        direct_parts = [part["id"] for part in parts if label in part["figure_references"]]
        introduced_by = direct_parts[0] if direct_parts else None
        figure_id = f"fig_{match.group(1)}_{match.group(2)}"
        figures.append({
            "id": figure_id,
            "label": label,
            "file": figure_path.name,
            "introduced_by": introduced_by,
            "referenced_by": direct_parts,
            "mapping_method": "explicit_text_reference" if direct_parts else "caption_proximity",
            "mapping_confidence": 1.0 if direct_parts else 0.6,
        })
        for part in parts:
            if part["id"] in direct_parts:
                part["figure_ids"].append(figure_id)

    detected_marks = sum(int(part["marks"]) for part in parts if part["marks"] is not None)
    mark_total_valid = total_marks is not None and detected_marks == total_marks
    review_flags: list[str] = []
    if total_marks is None:
        review_flags.append("total_marks_not_detected")
    elif not mark_total_valid:
        review_flags.append("part_marks_do_not_match_total")
    if any(figure["introduced_by"] is None for figure in figures):
        review_flags.append("figure_without_explicit_part_reference")

    payload = {
        "schema_version": "1.0",
        "question_id": question_id,
        **metadata,
        "question_num": question.number,
        "source_pages": list(range(question.start_page + 1, question.end_page + 2)),
        "total_marks": total_marks,
        "detected_part_marks": detected_marks,
        "marks_validation_passed": mark_total_valid,
        "question_stem": stem,
        "question_image": f"question_{question.number:02d}.png",
        "question_image_with_figures": (
            f"question_{question.number:02d}_with_figures.png"
            if (output_dir / f"question_{question.number:02d}_with_figures.png").exists()
            else None
        ),
        "question_text_file": text_path.name,
        "has_diagram": bool(figures),
        "figures": figures,
        "parts": parts,
        "review_flags": sorted(set(review_flags)),
        "human_review_status": "pending" if review_flags else "not_required",
        "enrichment": {
            "difficulty": None,
            "topic_id": None,
            "primary_skill": None,
            "skill_tags": [],
            "ai_rubric": None,
        },
    }
    json_path = output_dir / f"question_{question.number:02d}.json"
    temp_path = json_path.with_suffix(".tmp.json")
    temp_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temp_path.replace(json_path)
    return json_path


def write_question(
    source: pymupdf.Document,
    question: Question,
    output_dir: Path,
    *,
    dpi: int,
    extract_figure_images: bool,
) -> tuple[Path, Path, Path | None, int, list[Path]]:
    bands: list[Band] = []
    for page_number in range(question.start_page, question.end_page + 1):
        bands.extend(content_bands(source[page_number], page_number))
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
        destination = pymupdf.Rect(margin, y, margin + band.rect.width, y + band.rect.height)
        target.show_pdf_page(destination, source, band.page_number, clip=band.rect, keep_proportion=False)
        y += band.rect.height + band_gap

    png_path = output_dir / f"question_{question.number:02d}.png"
    with_figures_path = output_dir / f"question_{question.number:02d}_with_figures.png"
    text_path = output_dir / f"question_{question.number:02d}.txt"
    if with_figures_path.exists():
        with_figures_path.unlink()
    written_with_figures: Path | None = None
    figure_paths: list[Path] = []
    if extract_figure_images:
        figure_paths, diagram_rects = extract_figures(target, output_dir, dpi=dpi)
        if diagram_rects:
            temp_with_figures = with_figures_path.with_suffix(".tmp.png")
            figure_pix = target.get_pixmap(
                matrix=pymupdf.Matrix(dpi / 72, dpi / 72), alpha=False
            )
            figure_pix.save(temp_with_figures)
            temp_with_figures.replace(with_figures_path)
            written_with_figures = with_figures_path
        for diagram_rect in diagram_rects:
            target.add_redact_annot(diagram_rect, fill=(1, 1, 1))
        if diagram_rects:
            target.apply_redactions()
        if diagram_rects:
            compacted_output = compact_single_page(output, target)
            output.close()
            output = compacted_output
            target = output[0]

    temp_png = png_path.with_suffix(".tmp.png")
    temp_text = text_path.with_suffix(".tmp.txt")
    pix = target.get_pixmap(matrix=pymupdf.Matrix(dpi / 72, dpi / 72), alpha=False)
    pix.save(temp_png)
    temp_text.write_text(question_text(target), encoding="utf-8")
    output.close()
    temp_png.replace(png_path)
    temp_text.replace(text_path)
    old_pdf = output_dir / f"question_{question.number:02d}.pdf"
    if old_pdf.exists():
        old_pdf.unlink()
    return png_path, text_path, written_with_figures, len(bands), figure_paths


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Compact one PDF, or all PDFs in a directory. If no path is given, "
            "the current directory is used."
        )
    )
    parser.add_argument(
        "input_path",
        type=Path,
        nargs="?",
        default=Path("."),
        help="PDF or directory containing PDFs (default: current directory)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="optional output directory; by default each PDF gets a sibling folder",
    )
    parser.add_argument("--dpi", type=int, default=150)
    parser.add_argument("--keep-answer-lines", action="store_true")
    parser.add_argument(
        "--no-figures",
        action="store_true",
        help="do not export captioned figures as separate PNG files",
    )
    parser.add_argument("--dry-run", action="store_true")
    return parser


def find_input_pdfs(input_path: Path) -> list[Path]:
    input_path = input_path.expanduser().resolve()
    if input_path.is_file():
        if input_path.suffix.lower() != ".pdf":
            raise ValueError(f"input file is not a PDF: {input_path}")
        return [input_path]
    if input_path.is_dir():
        pdfs = sorted(
            path for path in input_path.iterdir()
            if path.is_file() and path.suffix.lower() == ".pdf"
        )
        if not pdfs:
            raise ValueError(f"no PDF files found in: {input_path}")
        return pdfs
    raise ValueError(f"input path not found: {input_path}")


def process_pdf(input_pdf: Path, output_dir: Path, args: argparse.Namespace) -> None:
    original = pymupdf.open(input_pdf)
    questions = detect_questions(original)
    print(f"\n{input_pdf.name}: detected {len(questions)} questions")
    for question in questions:
        pages = f"{question.start_page + 1}-{question.end_page + 1}"
        print(f"  question {question.number}: source pages {pages}")
    if args.dry_run:
        original.close()
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    sanitized = make_sanitized_copy(original, keep_answer_lines=args.keep_answer_lines)
    for question in questions:
        png_path, text_path, with_figures_path, band_count, figure_paths = write_question(
            sanitized,
            question,
            output_dir,
            dpi=args.dpi,
            extract_figure_images=not args.no_figures,
        )
        print(
            f"  wrote {png_path.name} and {text_path.name} "
            f"({band_count} content bands)"
        )
        if with_figures_path:
            print(f"  wrote {with_figures_path.name}")
        for figure_path in figure_paths:
            print(f"  wrote {figure_path.name}")
        json_path = write_question_json(
            input_pdf, original, question, output_dir, text_path, figure_paths
        )
        print(f"  wrote {json_path.name}")
    sanitized.close()
    original.close()
    print(f"  output folder: {output_dir}")


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.dpi < 72:
        print("error: --dpi must be at least 72", file=sys.stderr)
        return 2
    try:
        resolved_input = args.input_path.expanduser().resolve()
        input_is_directory = resolved_input.is_dir()
        input_pdfs = find_input_pdfs(args.input_path)
        for input_pdf in input_pdfs:
            if args.output_dir is None:
                if input_is_directory and resolved_input.name.lower() == "papertoconvert":
                    output_dir = resolved_input.parent / "output" / input_pdf.stem
                else:
                    output_dir = input_pdf.parent / input_pdf.stem
            elif not input_is_directory:
                output_dir = args.output_dir.expanduser().resolve()
            else:
                output_dir = args.output_dir.expanduser().resolve() / input_pdf.stem
            process_pdf(input_pdf, output_dir, args)
    except (ValueError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
