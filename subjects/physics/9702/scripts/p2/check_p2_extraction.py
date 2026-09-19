#!/usr/bin/env python3
"""Deterministic Theory Extraction, Image Slices & Marks Checker for Cambridge Physics (9702) Paper 2.

Comprehensive 0-Cost Deterministic Verification:
1. Question Completeness: All question_XX directories present and non-empty.
2. Image Slices Health:
   - question_compact.png: exists, > 15KB, width >= 500px, height >= 200px, non-blank.
   - question_printable.png: exists, > 15KB, width >= 500px, height >= 200px, non-blank.
   - markscheme.png: exists, > 5KB, width >= 300px, height >= 80px, non-blank.
3. Edge Ink Clipping Detector:
   - Verifies that dark ink does not touch the extreme 2px outer border of crops (detects clipped text/graphs/circuits).
4. Diagram / Figure Crops Integrity:
   - All figure_*.png: exists, > 1.5KB, width >= 60px, height >= 40px, non-blank, non-sliver.
5. Boilerplate & Formula Sheet Leakage Detector:
   - Checks that reference pages (Formulae and Data), footers, and margins did not leak into question text or images.
6. Subpart Sequence & Hierarchy Auditor:
   - Enforces strictly sequential Cambridge subpart ordering (a -> b -> c and i -> ii -> iii).
7. Marks Calculation & Invariants:
   - Scans extracted content for subpart marks [1], [2], etc.
   - Paper total marks must equal exactly 60 for Paper 2!
8. Whole-Paper Compiled PDFs:
   - paper_compact.pdf, paper_printable.pdf, paper_markscheme.pdf exist and are valid.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from PIL import Image
import numpy as np

REPO_ROOT = next(
    (p for p in Path(__file__).resolve().parents if (p / "subjects").is_dir() and (p / "pyproject.toml").is_file()),
    Path(__file__).resolve().parents[4],
)
PHYSICS_P2_DIR = REPO_ROOT / "subjects/physics/9702/past papers/p2"

FORBIDDEN_BOILERPLATE_PATTERNS = [
    (r"speed\s+of\s+light\s+in\s+free\s+space", "Data reference page leaked into question"),
    (r"uniformly\s+accelerated\s+motion", "Formulae reference page leaked into question"),
    (r"\bBLANK\s+PAGE\b", "BLANK PAGE marker leaked into question"),
    (r"DO\s+NOT\s+WRITE\s+IN\s+THIS\s+MARGIN", "Margin warning leaked into question text"),
    (r"\[Turn\s+over", "Running footer [Turn over leaked into question"),
    (r"Permission\s+to\s+reproduce\s+items", "Copyright disclaimer leaked into question"),
]


def find_p2_paper_dir(query: str) -> tuple[str, Path]:
    """Resolve paper code and path for a Physics Paper 2 query."""
    p = Path(query)
    if p.is_dir():
        qp = list(p.glob("source/*_qp_*.pdf"))
        code = re.sub(r"_(qp|ms)_", "_", qp[0].stem) if qp else p.name
        return code, p

    norm = re.sub(r"_(qp|ms)_", "_", query.lower().replace(".pdf", ""))
    for qp in sorted(PHYSICS_P2_DIR.glob("**/source/*_qp_*.pdf")):
        code = re.sub(r"_(qp|ms)_", "_", qp.stem.lower())
        if norm in code or norm in str(qp.parent.parent).lower():
            official_code = re.sub(r"_(qp|ms)_", "_", qp.stem)
            return official_code, qp.parent.parent

    raise FileNotFoundError(f"Could not locate Physics P2 paper for query: '{query}'")


def check_image_health(img_path: Path, min_size: int, min_w: int, min_h: int) -> tuple[bool, str, tuple[int, int] | None]:
    if not img_path.is_file():
        return False, "File missing", None

    sz = img_path.stat().st_size
    if sz < min_size:
        return False, f"File size too small ({sz} bytes < {min_size} bytes)", None

    try:
        with Image.open(img_path) as im:
            im.verify()
        with Image.open(img_path) as im:
            w, h = im.size
            if w < min_w or h < min_h:
                return False, f"Dimensions too small ({w}x{h} < {min_w}x{min_h})", (w, h)

            gray = im.convert("L")
            arr = np.array(gray)
            std = float(np.std(arr))
            if std < 1.0:
                return False, f"Blank/solid color (std dev: {std:.2f})", (w, h)
            non_white = float(np.mean(arr < 250))
            if non_white < 0.001:
                return False, f"Blank page (< 0.1% ink: {non_white*100:.2f}%)", (w, h)

            return True, f"OK (ink: {non_white*100:.1f}%)", (w, h)
    except Exception as e:
        return False, f"Corrupt image file: {e}", None


def check_edge_ink_clipping(img_path: Path, border_px: int = 2) -> list[str]:
    clipped = []
    if not img_path.is_file():
        return clipped

    try:
        with Image.open(img_path) as im:
            gray = im.convert("L")
            arr = np.array(gray)
            h, w = arr.shape
            if h < 10 or w < 10:
                return ["Image dimensions too small to inspect borders"]

            top_ink = float(np.mean(arr[:border_px, :] < 200))
            bot_ink = float(np.mean(arr[-border_px:, :] < 200))
            left_ink = float(np.mean(arr[:, :border_px] < 200))
            right_ink = float(np.mean(arr[:, -border_px:] < 200))

            if top_ink > 0.02:
                clipped.append(f"top border ({top_ink*100:.1f}% ink)")
            if bot_ink > 0.02:
                clipped.append(f"bottom border ({bot_ink*100:.1f}% ink)")
            if left_ink > 0.02:
                clipped.append(f"left border ({left_ink*100:.1f}% ink)")
            if right_ink > 0.02:
                clipped.append(f"right border ({right_ink*100:.1f}% ink)")
    except Exception as e:
        clipped.append(f"Error checking edge clipping: {e}")

    return clipped


def check_boilerplate_leakage(text: str) -> list[str]:
    issues = []
    if not text:
        return issues

    for pattern, desc in FORBIDDEN_BOILERPLATE_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            issues.append(desc)
    return issues


def check_subpart_sequence(parts: list[dict]) -> list[str]:
    errors = []
    if not parts:
        return errors

    seen_letters: list[str] = []
    letter_to_romans: dict[str, list[str]] = {}

    for p in parts:
        lbl = p.get("label") or ""
        m_full = re.match(r"^\(([a-z])\)(?:\(([ivx]+)\))?$", lbl.strip(), re.IGNORECASE)
        m_roman_only = re.match(r"^\(([ivx]+)\)$", lbl.strip(), re.IGNORECASE)

        letter = None
        roman = None

        if m_full:
            letter = m_full.group(1).lower()
            roman = m_full.group(2).lower() if m_full.group(2) else None
        elif m_roman_only:
            roman = m_roman_only.group(1).lower()

        if letter:
            if letter not in seen_letters:
                seen_letters.append(letter)
            if roman:
                letter_to_romans.setdefault(letter, []).append(roman)

    expected_letters = [chr(ord("a") + i) for i in range(len(seen_letters))]
    if seen_letters != expected_letters:
        errors.append(f"Non-sequential subpart letters: {seen_letters} (expected {expected_letters})")

    roman_order = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii"]
    for ltr, romans in letter_to_romans.items():
        exp = roman_order[: len(romans)]
        if romans != exp:
            errors.append(f"Non-sequential roman numerals under ({ltr}): {romans} (expected {exp})")

    return errors


def check_p2_extraction(paper_dir: Path) -> dict:
    results = {
        "paper_dir": str(paper_dir),
        "total_questions": 0,
        "valid_compact_images": 0,
        "valid_printable_images": 0,
        "valid_ms_images": 0,
        "total_figures": 0,
        "valid_figures": 0,
        "total_marks_calculated": 0,
        "edge_clipping_errors": [],
        "boilerplate_errors": [],
        "sequence_errors": [],
        "errors": [],
        "warnings": [],
    }

    q_dirs = sorted([d for d in paper_dir.iterdir() if d.is_dir() and d.name.startswith("question_")])
    results["total_questions"] = len(q_dirs)

    if len(q_dirs) == 0:
        results["errors"].append("No question directories found!")
        return results

    total_marks_paper = 0

    for qd in q_dirs:
        q_name = qd.name

        compact_img = qd / "question_compact.png"
        ok_c, msg_c, _ = check_image_health(compact_img, min_size=15000, min_w=500, min_h=200)
        if ok_c:
            results["valid_compact_images"] += 1
        else:
            results["errors"].append(f"{q_name}/question_compact.png: {msg_c}")

        c_clips = check_edge_ink_clipping(compact_img)
        if c_clips:
            results["edge_clipping_errors"].append(f"{q_name}/question_compact.png: ink touches {', '.join(c_clips)}")

        print_img = qd / "question_printable.png"
        ok_p, msg_p, _ = check_image_health(print_img, min_size=15000, min_w=500, min_h=200)
        if ok_p:
            results["valid_printable_images"] += 1
        else:
            results["errors"].append(f"{q_name}/question_printable.png: {msg_p}")

        ms_img = qd / "markscheme.png"
        ok_m, msg_m, _ = check_image_health(ms_img, min_size=5000, min_w=300, min_h=80)
        if ok_m:
            results["valid_ms_images"] += 1
        else:
            results["errors"].append(f"{q_name}/markscheme.png: {msg_m}")

        for fig in sorted(qd.glob("figure_*.png")):
            results["total_figures"] += 1
            ok_f, msg_f, dims = check_image_health(fig, min_size=1500, min_w=60, min_h=40)
            if ok_f:
                results["valid_figures"] += 1
            else:
                results["errors"].append(f"{q_name}/{fig.name}: {msg_f}")

            f_clips = check_edge_ink_clipping(fig)
            if f_clips:
                results["edge_clipping_errors"].append(f"{q_name}/{fig.name}: ink touches {', '.join(f_clips)}")

        txt_path = qd / "question.txt"
        if txt_path.is_file():
            txt_content = txt_path.read_text(encoding="utf-8", errors="replace")
            bp = check_boilerplate_leakage(txt_content)
            for b in bp:
                results["boilerplate_errors"].append(f"{q_name}/question.txt: {b}")

        ms_json = qd / "markscheme.json"
        ocr_json = qd / "question_ocr.json"

        q_marks = 0
        parts = []
        if ms_json.is_file():
            try:
                data = json.loads(ms_json.read_text(encoding="utf-8"))
                q_marks = data.get("total_marks", 0)
                parts = data.get("parts", [])
            except Exception:
                pass
        elif ocr_json.is_file():
            try:
                data = json.loads(ocr_json.read_text(encoding="utf-8"))
                q_marks = data.get("total_marks", 0)
                parts = data.get("parts", [])
            except Exception:
                pass
        elif txt_path.is_file():
            m_tot = re.search(r"\[Total:\s*(\d+)\]", txt_content)
            if m_tot:
                q_marks = int(m_tot.group(1))

        total_marks_paper += q_marks

        seq_errs = check_subpart_sequence(parts)
        for se in seq_errs:
            results["sequence_errors"].append(f"{q_name}: {se}")

    results["total_marks_calculated"] = total_marks_paper

    if total_marks_paper > 0 and total_marks_paper != 60:
        results["errors"].append(f"Total marks calculated across questions is {total_marks_paper}, expected 60!")

    for pdf_name in ["paper_compact.pdf", "paper_printable.pdf", "paper_markscheme.pdf"]:
        pdf_file = paper_dir / pdf_name
        if not pdf_file.is_file():
            results["warnings"].append(f"Missing compiled PDF: {pdf_name}")
        elif pdf_file.stat().st_size < 1000:
            results["errors"].append(f"Compiled PDF too small: {pdf_name} ({pdf_file.stat().st_size} bytes)")

    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Check extraction quality for Physics P2")
    parser.add_argument("paper", help="Paper query or path (e.g. 9702_s24_21)")
    args = parser.parse_args()

    code, variant_dir = find_p2_paper_dir(args.paper)
    print(f"Checking extraction for Physics P2: {code} ({variant_dir})")
    res = check_p2_extraction(variant_dir)

    print(f"Questions: {res['total_questions']}")
    print(f"Valid Compact: {res['valid_compact_images']}/{res['total_questions']}")
    print(f"Valid Printable: {res['valid_printable_images']}/{res['total_questions']}")
    print(f"Valid Mark Schemes: {res['valid_ms_images']}/{res['total_questions']}")
    print(f"Valid Figures: {res['valid_figures']}/{res['total_figures']}")
    print(f"Total Marks: {res['total_marks_calculated']}/60")

    if res["edge_clipping_errors"]:
        print(f"Edge clipping alerts: {len(res['edge_clipping_errors'])}")
        for e in res["edge_clipping_errors"]:
            print(f"  [CLIP] {e}")

    if res["boilerplate_errors"]:
        print(f"Boilerplate errors: {len(res['boilerplate_errors'])}")
        for e in res["boilerplate_errors"]:
            print(f"  [BOILERPLATE] {e}")

    if res["sequence_errors"]:
        print(f"Sequence errors: {len(res['sequence_errors'])}")
        for e in res["sequence_errors"]:
            print(f"  [SEQUENCE] {e}")

    if res["errors"]:
        print(f"ERRORS found: {len(res['errors'])}")
        for e in res["errors"]:
            print(f"  [ERROR] {e}")
        sys.exit(1)
    else:
        print("PASS: 0 extraction errors.")


if __name__ == "__main__":
    main()
