#!/usr/bin/env python3
"""
Cambridge Mark Scheme Question-by-Question Slicer
Extracts each question's mark scheme table into an individual image (ms_q01.png ... ms_q08.png)
and compiles them into a single unified mark scheme PDF (paper_markscheme.pdf).
"""

import re
import sys
from pathlib import Path
import pymupdf

def slice_mark_scheme(ms_pdf_path: Path, output_dir: Path, dpi: int = 150) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(ms_pdf_path)
    
    # 1. Identify all pages with tables (containing "Question" and "Answer")
    table_pages = []
    for pno, page in enumerate(doc):
        text = page.get_text("text")
        if "Question" in text and "Answer" in text:
            table_pages.append(pno)
            
    if not table_pages:
        raise ValueError(f"No mark scheme tables found in {ms_pdf_path.name}")
        
    print(f"Found mark scheme tables on pages: {[p+1 for p in table_pages]}")
    
    # 2. Find bounding boxes for each question
    # On each table page, look for instances of "Question" header and "X(a)"
    # Rotated rects: (y in rotated space corresponds to vertical position)
    question_slices = {} # q_num -> list of (page_num, y0, y1)
    
    for pno in table_pages:
        page = doc[pno]
        rot = page.rotation_matrix
        
        # Find all table headers "Question"
        q_headers = [r * rot for r in page.search_for("Question")]
        q_headers.sort(key=lambda r: r.y0)
        
        # Find all question rows like 1(a), 2(a), 3(b), etc.
        # Find rows using regex search on text blocks
        blocks = page.get_text("blocks")
        q_rows = [] # (q_num, y_top)
        for b in blocks:
            btext = b[4].strip()
            # Match 1(a), 2(a), etc.
            m = re.match(r"^(\d{1,2})\s*\([a-z]\)", btext)
            if m:
                q_num = int(m.group(1))
                r = pymupdf.Rect(b[:4]) * rot
                q_rows.append((q_num, r.y0))
                
        q_rows.sort(key=lambda x: x[1])
        
        # Determine question intervals on this page
        # If headers exist, each header starts a question table
        # Table top: header.y0 - 10
        # Table bottom: next header.y0 - 15, or footer at ~545
        footer_y = min(page.rect.height - 40, 545.0)
        
        if len(q_headers) == 1:
            # Single question on this page (or continuation)
            if q_rows:
                q_num = q_rows[0][0]
                y0 = max(40.0, q_headers[0].y0 - 8)
                y1 = footer_y
                question_slices.setdefault(q_num, []).append((pno, y0, y1))
        elif len(q_headers) > 1:
            # Multiple questions on this page
            for i, h in enumerate(q_headers):
                y0 = max(40.0, h.y0 - 8)
                y1 = q_headers[i+1].y0 - 10 if i + 1 < len(q_headers) else footer_y
                # Find which question belongs to this header
                header_rows = [qr for qr in q_rows if y0 <= qr[1] <= y1]
                if header_rows:
                    q_num = header_rows[0][0]
                    question_slices.setdefault(q_num, []).append((pno, y0, y1))
        else:
            # Continuation page without "Question" header
            if q_rows:
                q_num = q_rows[0][0]
                y0 = 45.0
                y1 = footer_y
                question_slices.setdefault(q_num, []).append((pno, y0, y1))
                
    # 3. Render each question into ms_qXX.png
    output_pngs = []
    compiled_doc = pymupdf.open()
    
    for q_num in sorted(question_slices.keys()):
        slices = question_slices[q_num]
        print(f"Rendering MS Q{q_num} from {len(slices)} slice(s)...")
        
        # Calculate total height
        margin = 15.0
        slice_gap = 10.0
        total_height = margin * 2 + sum((y1 - y0) for _, y0, y1 in slices) + slice_gap * (len(slices) - 1)
        width = doc[slices[0][0]].rect.width
        
        target_doc = pymupdf.open()
        target_page = target_doc.new_page(width=width, height=total_height)
        
        current_y = margin
        for pno, y0, y1 in slices:
            src_page = doc[pno]
            # Clip in rotated space:
            # Rect(x0=30, y0=y0, x1=width-30, y1=y1)
            clip_rot = pymupdf.Rect(30.0, y0, width - 30.0, y1)
            # In unrotated space:
            derot = src_page.derotation_matrix
            clip_unrot = clip_rot * derot
            
            dest = pymupdf.Rect(margin, current_y, width - margin, current_y + (y1 - y0))
            target_page.show_pdf_page(dest, doc, pno, clip=clip_unrot, keep_proportion=False)
            current_y += (y1 - y0) + slice_gap
            
        png_path = output_dir / f"ms_q{q_num:02d}.png"
        pix = target_page.get_pixmap(matrix=pymupdf.Matrix(dpi / 72, dpi / 72), colorspace=pymupdf.csRGB, alpha=False)
        pix.save(png_path)
        output_pngs.append(png_path)
        
        # Add to compiled doc
        compiled_doc.insert_pdf(target_doc)
        target_doc.close()
        
    compiled_pdf_path = output_dir / "paper_markscheme.pdf"
    compiled_doc.save(compiled_pdf_path)
    compiled_doc.close()
    doc.close()
    
    print(f"Successfully sliced {len(output_pngs)} questions and compiled {compiled_pdf_path.name}")
    return output_pngs

if __name__ == "__main__":
    pdf_file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "/Users/abdullahaftab/Kognitiv/exam-paper-parser/subjects/physics/9702/past papers/p2/2023/may-june/variant-1/source/9702_s23_ms_21.pdf"
    )
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("output_ms_test")
    slice_mark_scheme(pdf_file, out_path)
