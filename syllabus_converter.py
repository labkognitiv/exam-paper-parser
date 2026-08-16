from __future__ import annotations

import argparse
import re
from pathlib import Path

import pymupdf


HEADER_PREFIX_RE = re.compile(
    r"^Cambridge International AS\s*&\s*A Level Physics 9702 syllabus for (?:exams? in )?\d{4}, \d{4} and \d{4}\.?(?:\s+|$)",
    re.I,
)
PAGE_NUMBER_RE = re.compile(r"^\d{1,3}$")
BACK_TO_CONTENTS_RE = re.compile(r"^Back to contents page\s*$", re.I)
FOOTER_URL_RE = re.compile(r"^(?:www\.)?cambridgeinternational\.org/", re.I)


def _normalise_line(text: str) -> str:
    return " ".join(text.replace("\u00a0", " ").split())


def _line_text(line: dict) -> str:
    """Keep visibly separate table/column cells distinct in plain text."""
    pieces: list[str] = []
    previous_x1: float | None = None
    for span in line.get("spans", []):
        value = _normalise_line(str(span.get("text", "")))
        if not value:
            continue
        x0, _y0, x1, _y1 = span["bbox"]
        if previous_x1 is not None and float(x0) - previous_x1 > 18:
            pieces.append(" | ")
        elif pieces and not pieces[-1].endswith((" ", "-", "/")):
            pieces.append(" ")
        pieces.append(value)
        previous_x1 = float(x1)
    return "".join(pieces).strip()


def extract_page_text(page: pymupdf.Page) -> str:
    """Extract readable syllabus text while retaining block and line boundaries."""
    blocks: list[tuple[float, float, str]] = []
    for block in page.get_text("dict", sort=True).get("blocks", []):
        if block.get("type") != 0:
            continue
        line_records: list[tuple[float, float, str]] = []
        for line in block.get("lines", []):
            text = _line_text(line)
            line_x0, line_y0, _lx1, _line_y1 = line["bbox"]
            text = HEADER_PREFIX_RE.sub("", text).strip()
            if not text or BACK_TO_CONTENTS_RE.match(text):
                continue
            if line_y0 > page.rect.height - 55 and (
                PAGE_NUMBER_RE.match(text) or FOOTER_URL_RE.match(text)
            ):
                continue
            line_records.append((float(line_y0), float(line_x0), text))
        if not line_records:
            continue
        lines: list[str] = []
        for line_y0, line_x0, text in sorted(line_records):
            if lines and abs(line_y0 - previous_y0) < 2:
                lines[-1] += " | " + text
            else:
                lines.append(text)
            previous_y0 = line_y0
        x0, y0, _x1, _y1 = block["bbox"]
        blocks.append((float(y0), float(x0), "\n".join(lines)))

    blocks.sort(key=lambda item: (round(item[0], 1), item[1]))
    return "\n\n".join(text for _y, _x, text in blocks).strip()


def convert_pdf(pdf: Path, output_root: Path) -> Path:
    if not pdf.is_file() or pdf.suffix.lower() != ".pdf":
        raise ValueError(f"Expected a PDF file: {pdf}")

    destination = output_root / pdf.stem
    destination.mkdir(parents=True, exist_ok=True)
    output_path = destination / f"{pdf.stem}.txt"

    pages: list[str] = []
    with pymupdf.open(pdf) as document:
        if document.needs_pass:
            raise ValueError(f"Password-protected PDF is not supported: {pdf}")
        for page_number, page in enumerate(document, start=1):
            text = extract_page_text(page)
            pages.append(f"--- Page {page_number} ---\n\n{text}".rstrip())

    if not any(page.partition("\n\n")[2].strip() for page in pages):
        raise ValueError(f"No selectable text found; OCR is required: {pdf}")

    temporary_path = output_path.with_suffix(".tmp.txt")
    temporary_path.write_text("\n\n".join(pages) + "\n", encoding="utf-8")
    temporary_path.replace(output_path)
    print(f"{pdf.name}: wrote {len(pages)} pages to {output_path}")
    return output_path


def find_pdfs(source: Path) -> list[Path]:
    if source.is_file():
        return [source]
    if source.is_dir():
        return sorted(path for path in source.rglob("*.pdf") if path.is_file())
    raise FileNotFoundError(source)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert born-digital Cambridge syllabus PDFs to page-delimited text."
    )
    parser.add_argument("source", type=Path, help="A syllabus PDF or directory of PDFs")
    parser.add_argument("--output", type=Path, default=Path("output/physics/syllabus"))
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    pdfs = find_pdfs(args.source)
    if not pdfs:
        raise ValueError(f"No PDF files found in {args.source}")
    for pdf in pdfs:
        convert_pdf(pdf, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
