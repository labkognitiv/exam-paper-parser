from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

import pymupdf


QUESTION_RE = re.compile(r"^(?P<number>\d{1,2})(?P<part>(?:\([a-z]+\)|\([ivx]+\)|\(\d+\))*)$", re.I)
MARK_TAG_RE = re.compile(r"^\(?(?:A|B|C|M)\d+\)?$", re.I)
LINE_TAG_RE = re.compile(r"\s+(?P<tag>\(?(?:A|B|C|M)(?P<marks>\d+)\)?)\s*$", re.I)
PAPER_RE = re.compile(r"^(?P<subject>\d{4})_(?P<session>[msw])(?P<year>\d{2})_ms_(?P<variant>\d{2})$", re.I)

SYMBOLS = str.maketrans({
    "\uf0b4": "×",
    "\uf071": "θ",
    "\uf06c": "λ",
    "\uf044": "Δ",
    "\uf057": "Ω",
    "\uf0b1": "±",
    "\uf0a5": "∝",
})


def clean(text: str) -> str:
    return " ".join(text.translate(SYMBOLS).replace("\x00", " ").split())


def paper_output_name(pdf: Path) -> str:
    match = PAPER_RE.match(pdf.stem)
    if not match:
        return pdf.stem
    return (
        f"{match.group('subject')}_{match.group('session').lower()}"
        f"{match.group('year')}_ms_{match.group('variant')}"
    )


def paper_metadata(pdf: Path) -> dict:
    match = PAPER_RE.match(pdf.stem)
    if not match:
        return {"paper_code": pdf.stem, "subject_code": None, "year": None,
                "session": None, "session_code": None, "variant": None}
    session_code = match.group("session").lower()
    sessions = {"m": "February/March", "s": "May/June", "w": "October/November"}
    return {
        "paper_code": f"{match.group('subject')}_{session_code}{match.group('year')}_{match.group('variant')}",
        "subject_code": match.group("subject"),
        "year": 2000 + int(match.group("year")),
        "session": sessions[session_code],
        "session_code": session_code,
        "variant": int(match.group("variant")),
    }


def question_json(pdf: Path, number: int, lines: list[str]) -> dict:
    metadata = paper_metadata(pdf)
    question_id = f"{metadata['paper_code']}_q{number:02d}"
    parts: list[dict] = []
    current_part: dict | None = None

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue
        tag_match = LINE_TAG_RE.search(line)
        tag = tag_match.group("tag") if tag_match else None
        text = line[:tag_match.start()].rstrip() if tag_match else line

        first_token = text.split()[0] if text else ""
        label_match = QUESTION_RE.match(first_token)
        if label_match and int(label_match.group("number")) == number:
            part_label = label_match.group("part") or ""
            suffix = "_" + "_".join(re.findall(r"\(([^)]+)\)", part_label)) if part_label else ""
            current_part = {
                "id": f"{question_id}{suffix}",
                "label": part_label or str(number),
                "marks": 0,
                "marking_points": [],
            }
            parts.append(current_part)
            text = text[len(first_token):].strip()

        if current_part is None:
            current_part = {
                "id": question_id,
                "label": str(number),
                "marks": 0,
                "marking_points": [],
            }
            parts.append(current_part)

        if not tag:
            if text:
                current_part.setdefault("notes", []).append(text)
            continue

        is_alternative = tag.startswith("(") and tag.endswith(")")
        mark_code = tag.strip("()")
        marks = int(tag_match.group("marks"))
        point = {
            "id": f"{current_part['id']}_mp{len(current_part['marking_points']) + 1:02d}",
            "text": text,
            "tag": mark_code,
            "marks": marks,
            "is_alternative": is_alternative,
        }
        current_part["marking_points"].append(point)
        if not is_alternative:
            current_part["marks"] += marks

    return {
        "schema_version": "1.0",
        "source_filename": pdf.name,
        **metadata,
        "question_id": question_id,
        "question_num": number,
        "total_marks": sum(part["marks"] for part in parts),
        "parts": parts,
    }


def extract_questions(pdf: Path) -> dict[int, list[str]]:
    questions: dict[int, list[str]] = defaultdict(list)
    current_question: int | None = None

    with pymupdf.open(pdf) as doc:
        for page in doc:
            page_text = page.get_text("text")
            if not ("Question" in page_text and "Answer" in page_text and "Marks" in page_text):
                continue

            answer_blocks: list[dict] = []
            mark_blocks: list[tuple[float, str]] = []
            for block in sorted(page.get_text("blocks"), key=lambda b: (b[1], b[0])):
                x0, y0, _x1, y1, raw = block[:5]
                if y0 < 70 or y0 > page.rect.height - 46:
                    continue
                lines = [clean(line) for line in raw.splitlines() if clean(line)]
                if not lines or lines == ["Question", "Answer", "Marks"]:
                    continue
                joined = clean(" ".join(lines))
                if x0 >= 720 and MARK_TAG_RE.match(joined):
                    mark_blocks.append(((y0 + y1) / 2, joined))
                    continue

                embedded_mark = ""
                if lines and MARK_TAG_RE.match(lines[-1]):
                    embedded_mark = lines.pop()
                if not lines:
                    continue

                first_token = lines[0].split()[0]
                match = QUESTION_RE.match(first_token)
                label = ""
                if match:
                    current_question = int(match.group("number"))
                    label = first_token
                    lines[0] = lines[0][len(first_token):].strip()
                    lines = [line for line in lines if line]
                if current_question is None:
                    continue
                answer_blocks.append({
                    "question": current_question,
                    "label": label,
                    "text": clean(" ".join(lines)),
                    "mark": embedded_mark,
                    "y0": y0,
                    "y1": y1,
                })

            # Tags are often separate right-column blocks. Attach each one to
            # the answer paragraph occupying the same vertical row.
            for mark_y, tag in mark_blocks:
                candidates = [b for b in answer_blocks if b["y0"] - 3 <= mark_y <= b["y1"] + 3]
                if not candidates:
                    candidates = answer_blocks
                if candidates:
                    target = min(candidates, key=lambda b: abs((b["y0"] + b["y1"]) / 2 - mark_y))
                    target["mark"] = tag

            consolidated: list[dict] = []
            for item in answer_blocks:
                if (
                    consolidated
                    and not item["label"]
                    and not item["mark"]
                    and item["question"] == consolidated[-1]["question"]
                ):
                    consolidated[-1]["text"] = clean(f"{consolidated[-1]['text']} {item['text']}")
                    consolidated[-1]["y1"] = item["y1"]
                else:
                    consolidated.append(item)

            previous_y: float | None = None
            for item in consolidated:
                number = item["question"]
                if previous_y is not None and item["y0"] - previous_y > 25 and questions[number]:
                    questions[number].append("")
                previous_y = item["y1"]
                content = " ".join(piece for piece in (item["label"], item["text"]) if piece)
                if item["mark"]:
                    questions[number].append(f"{content:<90} {item['mark']}".rstrip())
                elif content:
                    questions[number].append(content)

    if not questions:
        raise ValueError("No mark-scheme Question / Answer / Marks tables were detected.")
    return dict(questions)


def convert_pdf(pdf: Path, output_root: Path) -> list[Path]:
    destination = output_root / paper_output_name(pdf)
    destination.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for number, lines in sorted(extract_questions(pdf).items()):
        text_path = destination / f"markscheme_{number:02d}.txt"
        text_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
        json_path = destination / f"markscheme_{number:02d}.json"
        json_path.write_text(
            json.dumps(question_json(pdf, number, lines), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        written.extend((text_path, json_path))
    return written


def pdfs_at(source: Path) -> list[Path]:
    if source.is_file():
        return [source]
    return sorted(source.glob("*.pdf"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Extract Cambridge mark schemes into question text files.")
    parser.add_argument("source", nargs="?", default=Path("input/physics/markscheme"), type=Path)
    parser.add_argument("--output", type=Path, default=Path("output/physics/markscheme"))
    args = parser.parse_args(argv)

    pdfs = pdfs_at(args.source)
    if not pdfs:
        parser.error(f"No PDF files found at {args.source}")
    for pdf in pdfs:
        files = convert_pdf(pdf, args.output)
        print(f"{pdf.name}: wrote {len(files) // 2} TXT and JSON mark-scheme pairs to {files[0].parent}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
