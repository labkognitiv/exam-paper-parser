#!/usr/bin/env python3
"""Cambridge Physics 9702 Mark Scheme Slicer.

Slices mark scheme tables into question-by-question images (ms_q01.png, ms_q02.png, ...)
or question_XX/markscheme.png, and compiles them into a unified mark scheme PDF (paper_markscheme.pdf).
Supports:
- Upright landscape rendering across all PDF rotation states ({0, 90, 270})
- Authentic Question-column boundary detection without false matches
- Tight table bottom detection eliminating trailing blank whitespace
- Seamless vertical appending of continuation pages

Zero em dashes, zero en dashes.
"""

from __future__ import annotations

import argparse
import io
import re
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import pymupdf


def get_table_bottom_on_page(page: pymupdf.Page, top_y: float, footer_limit: float) -> float:
    """Find the exact bottom coordinate of the table on this page."""
    rot = page.rotation_matrix

    # 1. Look for horizontal border line drawn below top_y and above footer_limit
    border_y = 0.0
    for d in page.get_drawings():
        r = d["rect"] * rot
        if r.y0 >= max(top_y, 100.0) and r.y1 <= footer_limit and (r.x1 - r.x0) > 200 and (r.y1 - r.y0) <= 5.0:
            if r.y1 > border_y:
                border_y = r.y1

    # 2. Fallback to lowest table text block
    text_y = 0.0
    for b in page.get_text("blocks"):
        if not b[4].strip():
            continue
        if any(w in b[4] for w in ["Cambridge", "Page ", "9702/", "9701/"]):
            continue
        r = pymupdf.Rect(b[:4]) * rot
        if r.y0 >= top_y and r.y1 <= footer_limit:
            if r.y1 > text_y:
                text_y = r.y1

    # If border line is found and at or below lowest text, use border line
    if border_y > top_y + 10 and border_y >= text_y - 15:
        return min(footer_limit, border_y + 4.0)

    if text_y > top_y + 10:
        return min(footer_limit, text_y + 8.0)

    if border_y > top_y + 10:
        return min(footer_limit, border_y + 4.0)

    return footer_limit


def slice_mark_scheme(
    ms_pdf_path: Path,
    output_dir: Path,
    dpi: int = 150,
    *,
    per_question_dirs: bool = False,
    valid_questions: list[int] | None = None,
) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(ms_pdf_path)

    # 1. Identify first table page containing Question 1
    first_table_page = None
    for pno in range(len(doc)):
        page = doc[pno]
        rot = page.rotation_matrix
        qs = [r * rot for r in page.search_for("Question")]
        anss = [r * rot for r in page.search_for("Answer") + page.search_for("Mark Scheme")]
        for q in qs:
            if q.x0 < 130 and 40 < q.y0 < 120:
                for a in anss:
                    if q.x1 - 10.0 <= a.x0 < 600 and abs(q.y0 - a.y0) < 5.0:
                        first_table_page = pno
                        break
            if first_table_page is not None:
                break
        if first_table_page is not None:
            break

    # If not found via aligned headers, fallback for older PDFs (e.g. decomposed syllables or older layout)
    if first_table_page is None:
        for pno in range(1, len(doc)):
            page = doc[pno]
            rot = page.rotation_matrix
            pdict = page.get_text("dict")
            has_q1 = False
            for b in pdict.get("blocks", []):
                for l in b.get("lines", []):
                    for s in l.get("spans", []):
                        txt = s["text"].strip()
                        r_rot = pymupdf.Rect(s["bbox"]) * rot
                        if 45.0 <= r_rot.x0 <= 100.0 and 40.0 <= r_rot.y0 <= page.rect.height - 35:
                            if re.match(r"^1(?:\s*\([a-z]|\s*$)", txt):
                                has_q1 = True
                                break
                    if has_q1:
                        break
                if has_q1:
                    break
            if has_q1:
                first_table_page = pno
                break

    if first_table_page is None:
        first_table_page = 1 if len(doc) > 1 else 0

    table_pages = list(range(first_table_page, len(doc)))
    if not table_pages:
        doc.close()
        raise ValueError(f"No mark scheme tables found in {ms_pdf_path.name}")

    # 2. Extract question bounding intervals on each page
    question_slices: dict[int, list[tuple[int, float, float]]] = {}
    current_q: int | None = None

    for pno in table_pages:
        page = doc[pno]
        rot = page.rotation_matrix
        footer_limit = page.rect.height - 35.0

        # Header y detection in visual space
        q_headers = [r * rot for r in page.search_for("Question")]
        q_headers = [r for r in q_headers if r.x0 < 130 and r.y0 < 120]
        default_top_y = max(40.0, q_headers[0].y0 - 6.0) if q_headers else 45.0

        # Adaptive column right bound based on page orientation (portrait vs landscape)
        q_col_max_x = 80.0 if page.rect.width < 700 else 100.0

        pdict = page.get_text("dict")
        items_on_page: list[tuple[int, float]] = []
        for b in pdict.get("blocks", []):
            for line in b.get("lines", []):
                for span in line.get("spans", []):
                    txt = span["text"].strip()
                    if not txt:
                        continue
                    r = pymupdf.Rect(span["bbox"]) * rot
                    if r.x0 <= q_col_max_x and 40.0 <= r.y0 <= footer_limit:
                        m = re.match(r"^([1-9]|1[0-5])(?:\s*\([a-z]|\s*$)", txt)
                        if m:
                            q_num = int(m.group(1))
                            if valid_questions is not None and q_num not in valid_questions:
                                continue
                            items_on_page.append((q_num, r.y0))

        # Sort items vertically down page
        items_on_page.sort(key=lambda x: x[1])

        # Enforce monotonic progression to reject formulas or sub-elements
        distinct_starts: list[tuple[int, float]] = []
        for q_num, y_pos in items_on_page:
            if not distinct_starts:
                if current_q is None:
                    if q_num == 1:
                        distinct_starts.append((q_num, y_pos))
                elif q_num >= current_q:
                    distinct_starts.append((q_num, y_pos))
            elif q_num >= distinct_starts[-1][0]:
                if distinct_starts[-1][0] != q_num:
                    distinct_starts.append((q_num, y_pos))

        if not distinct_starts:
            # Entire page continues previous question
            if current_q is not None:
                tbl_bottom = get_table_bottom_on_page(page, default_top_y, footer_limit)
                question_slices.setdefault(current_q, []).append((pno, default_top_y, tbl_bottom))
            continue

        # If first distinct question starts below table top, previous question continues here
        first_q, first_y = distinct_starts[0]
        if current_q is not None and first_q != current_q and (first_y - default_top_y) > 20:
            question_slices.setdefault(current_q, []).append((pno, default_top_y, first_y - 4.0))

        # Process each question starting on this page
        for i, (q_num, y_start) in enumerate(distinct_starts):
            current_q = q_num
            # Slice starts slightly above question label or at top header
            y0 = default_top_y if i == 0 and abs(y_start - default_top_y) < 30 else max(default_top_y, y_start - 8.0)
            if i + 1 < len(distinct_starts):
                y1 = distinct_starts[i + 1][1] - 4.0
            else:
                y1 = get_table_bottom_on_page(page, y0, footer_limit)
            question_slices.setdefault(current_q, []).append((pno, y0, y1))

    # 3. Render each question into markscheme.png or ms_qXX.png
    output_pngs: list[Path] = []
    compiled_doc = pymupdf.open()

    for q_num in sorted(question_slices.keys()):
        slices = question_slices[q_num]
        p_widths = [doc[pno].rect.width for pno, _, _ in slices]
        width = max(p_widths) if p_widths else 842.0

        rendered_imgs = []
        for idx, (pno, y0, y1) in enumerate(slices):
            page = doc[pno]
            rot = page.rotation_matrix
            clip_rot = pymupdf.Rect(0, y0, width, y1)
            inv_rot = ~rot
            clip_orig = clip_rot * inv_rot

            pix = page.get_pixmap(
                matrix=pymupdf.Matrix(dpi / 72, dpi / 72),
                clip=clip_orig,
                colorspace=pymupdf.csRGB,
                alpha=False,
            )
            img = Image.open(io.BytesIO(pix.tobytes("png")))
            if rot.a == 0 and rot.b == 1 and rot.c == -1 and rot.d == 0:
                img = img.rotate(-90, expand=True)
            elif rot.a == 0 and rot.b == -1 and rot.c == 1 and rot.d == 0:
                img = img.rotate(90, expand=True)
            elif rot.a == -1 and rot.d == -1:
                img = img.rotate(180, expand=True)

            # If multi-page slice and this is continuation page, prepend header banner if needed
            if idx > 0 and len(slices) > 1:
                header_p = doc[slices[0][0]]
                h_rot = header_p.rotation_matrix
                h_clip_rot = pymupdf.Rect(0, 40.0, width, 85.0)
                h_clip_orig = h_clip_rot * (~h_rot)
                h_pix = header_p.get_pixmap(
                    matrix=pymupdf.Matrix(dpi / 72, dpi / 72),
                    clip=h_clip_orig,
                    colorspace=pymupdf.csRGB,
                    alpha=False,
                )
                h_img = Image.open(io.BytesIO(h_pix.tobytes("png")))
                if h_rot.a == 0 and h_rot.b == 1 and h_rot.c == -1 and h_rot.d == 0:
                    h_img = h_img.rotate(-90, expand=True)
                elif h_rot.a == 0 and h_rot.b == -1 and h_rot.c == 1 and h_rot.d == 0:
                    h_img = h_img.rotate(90, expand=True)

                combo_w = max(img.width, h_img.width)
                combo_h = img.height + h_img.height + 4
                combo = Image.new("RGB", (combo_w, combo_h), (255, 255, 255))
                combo.paste(h_img, (0, 0))
                combo.paste(img, (0, h_img.height + 4))
                img = combo

            rendered_imgs.append(img)

        # Stitch all slices vertically
        total_w = max(im.width for im in rendered_imgs)
        gap = 12
        total_h = sum(im.height for im in rendered_imgs) + gap * (len(rendered_imgs) - 1)

        stitched = Image.new("RGB", (total_w, total_h), (255, 255, 255))
        curr_y = 0
        for im in rendered_imgs:
            stitched.paste(im, (0, curr_y))
            curr_y += im.height + gap

        # Save question mark scheme image
        if per_question_dirs:
            q_dir = output_dir / f"question_{q_num:02d}"
            q_dir.mkdir(parents=True, exist_ok=True)
            out_png = q_dir / "markscheme.png"
        else:
            out_png = output_dir / f"ms_q{q_num:02d}.png"

        temp_png = out_png.with_suffix(".tmp.png")
        stitched.save(temp_png)
        temp_png.replace(out_png)
        output_pngs.append(out_png)

        # Add to compiled doc
        img_bytes = io.BytesIO()
        stitched.save(img_bytes, format="PNG")
        img_bytes.seek(0)
        c_page = compiled_doc.new_page(width=float(stitched.width), height=float(stitched.height))
        c_page.insert_image(c_page.rect, stream=img_bytes.getvalue())

    # Save compiled PDF at output root
    compiled_pdf_path = output_dir / "paper_markscheme.pdf"
    temp_pdf = compiled_pdf_path.with_suffix(".tmp.pdf")
    compiled_doc.save(temp_pdf)
    temp_pdf.replace(compiled_pdf_path)
    compiled_doc.close()
    doc.close()

    return output_pngs


def main() -> None:
    parser = argparse.ArgumentParser(description="Cambridge Physics 9702 Mark Scheme Slicer")
    parser.add_argument("ms_pdf", type=Path, help="Path to mark scheme PDF file")
    parser.add_argument("output_dir", type=Path, help="Target output directory")
    parser.add_argument("--dpi", type=int, default=150, help="Rendering DPI (default: 150)")
    parser.add_argument(
        "--per-question-dirs",
        action="store_true",
        help="Write markscheme.png into question_XX/ subfolders",
    )
    args = parser.parse_args()

    slice_mark_scheme(args.ms_pdf, args.output_dir, dpi=args.dpi, per_question_dirs=args.per_question_dirs)


if __name__ == "__main__":
    main()
