from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

import pymupdf


QUESTION_RE = re.compile(
    r"^(?P<number>\d{1,2})"
    r"(?P<part>(?:\([a-z]+\)|\([ivx]+\)|\(\d+\))*)"
    r"(?P<item>\d+\.?)?$",
    re.I,
)
MARK_CODE = r"(?:A1|B[1-3]|C1|M1)"
MARK_TAG_RE = re.compile(rf"^\(?{MARK_CODE}\)?$", re.I)
LINE_TAG_RE = re.compile(rf"\s+(?P<tag>\(?(?:A1|B(?P<bmarks>[1-3])|C1|M1)\)?)\s*$", re.I)
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

MERGED_PAGE_NUMBER_WORD_RE = re.compile(
    r"^(?P<number>\d{1,2})\((?P<word>[a-z]{2,})\)(?P<rest>.*)$",
    re.I,
)


def clean(text: str) -> str:
    return " ".join(text.translate(SYMBOLS).replace("\x00", " ").split())


def repair_merged_page_number_word(line: str, current_question: int | None) -> str:
    """Prevent footer page numbers merged into answer prose becoming questions."""
    match = MERGED_PAGE_NUMBER_WORD_RE.match(line)
    if not match or current_question is None:
        return line
    number = int(match.group("number"))
    if number <= current_question + 1:
        return line
    return clean(f"({match.group('word')}){match.group('rest')}")


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
            part_label = (label_match.group("part") or "") + (label_match.group("item") or "")
            suffix_tokens = re.findall(r"\(([^)]+)\)", part_label)
            item = (label_match.group("item") or "").rstrip(".")
            if item:
                suffix_tokens.append(item)
            suffix = "_" + "_".join(suffix_tokens) if suffix_tokens else ""
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
        marks = int(tag_match.group("bmarks") or "1")
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


def extract_table_stream_questions(pdf: Path) -> dict[int, list[str]]:
    """Extract landscape Cambridge tables from their reliable text stream.

    Older landscape PDFs expose misleading block coordinates, but their plain
    text stream retains the printed row order. Only explicit compound labels
    such as ``2(b)(ii)1`` begin a question row; standalone equation numbers do
    not.
    """
    questions: dict[int, list[str]] = defaultdict(list)
    current_question: int | None = None
    current_label = ""
    pending: list[str] = []
    in_table = False

    def flush(tag: str = "") -> None:
        nonlocal current_label, pending
        if current_question is None or (not current_label and not pending and not tag):
            return
        content = clean(" ".join(pending))
        line = " ".join(piece for piece in (current_label, content) if piece)
        if tag:
            line = f"{line:<90} {tag}".rstrip()
        if line:
            questions[current_question].append(line)
        current_label = ""
        pending = []

    furniture_prefixes = (
        "Cambridge International", "Cambridge Assessment", "© UCLES",
        "© Cambridge", "Page ", "PUBLISHED", "May/June ",
        "March ", "October/November ",
    )

    with pymupdf.open(pdf) as doc:
        for page in doc:
            raw_lines = page.get_text("text").splitlines()
            page_has_table = any(line.strip() == "Question" for line in raw_lines) and any(
                line.strip() == "Answer" for line in raw_lines
            ) and any(line.strip() in {"Mark", "Marks"} for line in raw_lines)
            if not page_has_table:
                continue
            in_table = False
            header_seen: set[str] = set()
            for raw_line in raw_lines:
                line = clean(raw_line)
                if not line:
                    continue
                if not in_table:
                    if line in {"Question", "Answer", "Mark", "Marks"}:
                        header_seen.add(line)
                        if "Question" in header_seen and "Answer" in header_seen and ({"Mark", "Marks"} & header_seen):
                            in_table = True
                    continue
                if line.startswith(furniture_prefixes) or re.fullmatch(r"9702/2[1-4]", line):
                    continue
                if line in {"Question", "Answer", "Mark", "Marks"}:
                    continue
                line = repair_merged_page_number_word(line, current_question)

                label_match = QUESTION_RE.fullmatch(line)
                if label_match and label_match.group("part"):
                    flush()
                    current_question = int(label_match.group("number"))
                    current_label = line
                    continue

                embedded_label = re.match(
                    r"^(?P<label>\d{1,2}(?:\([a-z0-9]+\))+(?:\d+\.?)?)\s+(?P<text>.+)$",
                    line,
                    re.I,
                )
                if embedded_label:
                    flush()
                    parsed = QUESTION_RE.fullmatch(embedded_label.group("label"))
                    if parsed:
                        current_question = int(parsed.group("number"))
                        current_label = embedded_label.group("label")
                        pending.append(embedded_label.group("text"))
                        continue

                if current_question is None:
                    continue
                tag_match = LINE_TAG_RE.search(line)
                if tag_match:
                    text = line[:tag_match.start()].strip()
                    if text:
                        pending.append(text)
                    flush(tag_match.group("tag"))
                elif MARK_TAG_RE.fullmatch(line):
                    flush(line)
                else:
                    pending.append(line)
            flush()

    return dict(questions)


def extract_questions(pdf: Path) -> dict[int, list[str]]:
    stream_questions = extract_table_stream_questions(pdf)
    if stream_questions:
        keys = sorted(stream_questions)
        if keys == list(range(1, keys[-1] + 1)) and len(keys) >= 5:
            return stream_questions

    questions: dict[int, list[str]] = defaultdict(list)
    current_question: int | None = None

    with pymupdf.open(pdf) as doc:
        for page in doc:
            header_lines = [clean(line) for line in page.get_text("text").splitlines()[:20]]
            has_question_answer = (
                any(line in {"Question Answer", "Question Answer Marks"} for line in header_lines)
                or ("Question" in header_lines and "Answer" in header_lines)
            )
            if not has_question_answer or not any(line in {"Mark", "Marks"} for line in header_lines):
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
        return extract_linear_questions(pdf)
    extracted = dict(questions)
    # A page number can be fused with a full-page guidance block and look like
    # one question containing most of the paper. Fall back to the linear stream
    # when a supposed question has an impossible number of tagged rows.
    if any(sum(bool(LINE_TAG_RE.search(line)) for line in lines) > 20 for lines in extracted.values()):
        return extract_linear_questions(pdf)
    return extracted


LINEAR_PART_RE = re.compile(r"^(?P<labels>(?:\([a-z0-9]+\)\s*)+)(?P<text>.*)$", re.I)


def extract_linear_questions(pdf: Path) -> dict[int, list[str]]:
    """Extract older mark schemes whose answers and marks form one text stream."""
    questions: dict[int, list[str]] = defaultdict(list)
    current_question: int | None = None
    major_part = ""
    minor_part = ""
    pending: list[str] = []
    last_emitted_part: tuple[int, str, str] | None = None

    def flush(tag: str = "") -> None:
        nonlocal pending, last_emitted_part
        if current_question is None or (not pending and not tag):
            return
        part_key = (current_question, major_part, minor_part)
        label = f"{current_question}{major_part}{minor_part}" if part_key != last_emitted_part else ""
        content = clean(" ".join(pending))
        line = f"{label} {content}".strip()
        if tag:
            line = f"{line:<90} {tag}".rstrip()
        questions[current_question].append(line)
        last_emitted_part = part_key
        pending = []

    furniture = (
        "Page ", "Mark Scheme", "Syllabus", "Paper",
        "Cambridge International AS/A Level", "© Cambridge",
    )

    with pymupdf.open(pdf) as doc:
        for page in doc:
            raw_lines = page.get_text("text").splitlines()
            header_lines = [clean(line) for line in raw_lines[:20]]
            has_question_answer = (
                any(line in {"Question Answer", "Question Answer Marks"} for line in header_lines)
                or ("Question" in header_lines and "Answer" in header_lines)
            )
            if not has_question_answer or not any(line in {"Mark", "Marks"} for line in header_lines):
                continue
            for raw_line in raw_lines:
                line = clean(raw_line)
                if not line or line.startswith(furniture):
                    continue
                if re.fullmatch(r"\[\d+\]", line) or line.startswith("PMT"):
                    continue
                if line in {"9702", "21", "22", "23", "24"} and current_question is None:
                    continue

                if re.fullmatch(r"\d{1,2}", line):
                    number = int(line)
                    valid_start = current_question is None and number == 1
                    valid_next = current_question is not None and number == current_question + 1
                    if valid_start or valid_next:
                        flush()
                        current_question = number
                        major_part = ""
                        minor_part = ""
                        continue

                leading_part = re.match(
                    r"^(?P<number>\d{1,2})(?P<labels>(?:\([a-z0-9]+\))+)(?:\s+(?P<text>.*))?$",
                    line,
                    re.I,
                )
                if leading_part:
                    number = int(leading_part.group("number"))
                    if current_question is None or number in {current_question, current_question + 1}:
                        flush()
                        current_question = number
                        line = f"{leading_part.group('labels')} {leading_part.group('text') or ''}".strip()

                if current_question is None:
                    continue

                part_match = LINEAR_PART_RE.match(line)
                if part_match:
                    flush()
                    labels = re.findall(r"\(([^)]+)\)", part_match.group("labels"))
                    for index, value in enumerate(labels):
                        token = f"({value})"
                        if index == 0 and (value.lower() not in {"i", "ii", "iii", "iv", "v", "vi"} or not major_part):
                            major_part = token
                            minor_part = ""
                        else:
                            minor_part = token
                    line = part_match.group("text")
                    if not line:
                        continue

                tag_match = LINE_TAG_RE.search(line)
                if tag_match:
                    text = line[:tag_match.start()].strip()
                    if text:
                        pending.append(text)
                    flush(tag_match.group("tag"))
                elif MARK_TAG_RE.fullmatch(line):
                    flush(line)
                else:
                    pending.append(line)

    flush()
    if not questions:
        raise ValueError("No supported mark-scheme layout was detected.")
    return dict(questions)


def convert_pdf(pdf: Path, output_root: Path) -> list[Path]:
    destination = output_root / paper_output_name(pdf)
    destination.mkdir(parents=True, exist_ok=True)
    extracted = extract_questions(pdf)
    expected_names = {
        f"markscheme_{number:02d}{suffix}"
        for number in extracted
        for suffix in (".txt", ".json")
    }
    for stale in destination.glob("markscheme_*.*"):
        if stale.name not in expected_names and stale.suffix in {".txt", ".json"}:
            stale.unlink()
    written: list[Path] = []
    for number, lines in sorted(extracted.items()):
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
