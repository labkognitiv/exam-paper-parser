#!/usr/bin/env python3
"""Build versioned Physics 9702 topic/module and learning-outcome registries."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import tempfile
from pathlib import Path


TOPICS = {
    1: "Physical quantities and units",
    2: "Kinematics",
    3: "Dynamics",
    4: "Forces, density and pressure",
    5: "Work, energy and power",
    6: "Deformation of solids",
    7: "Waves",
    8: "Superposition",
    9: "Electricity",
    10: "D.C. circuits",
    11: "Particle physics",
    12: "Motion in a circle",
    13: "Gravitational fields",
    14: "Temperature",
    15: "Ideal gases",
    16: "Thermodynamics",
    17: "Oscillations",
    18: "Electric fields",
    19: "Capacitance",
    20: "Magnetic fields",
    21: "Alternating currents",
    22: "Quantum physics",
    23: "Nuclear physics",
    24: "Medical physics",
    25: "Astronomy and cosmology",
}

MODULE_RE = re.compile(r"^\s*(\d{1,2})\.(\d+)\s+(.+?)\s*$")
TOPIC_RE = re.compile(r"^\s*(\d{1,2})\s+(.+?)\s*$")
OUTCOME_RE = re.compile(r"^\s*(\d{1,2})\s+(.+?)\s*$")
HEADER_MARKERS = (
    "Cambridge International AS & A Level Physics 9702 syllabus",
    "Back to contents page",
    "www.cambridgeinternational.org/alevel",
)


def clean(text: str) -> str:
    text = text.replace("\u0007", "").replace("\ufeff", "")
    return re.sub(r"\s+", " ", text).strip()


def page_texts(pdf: Path, pdftotext: Path, first: int, last: int) -> list[str]:
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "content.txt"
        subprocess.run(
            [
                str(pdftotext),
                "-f",
                str(first),
                "-l",
                str(last),
                "-layout",
                str(pdf),
                str(out),
            ],
            check=True,
        )
        pages = out.read_text(encoding="utf-8").split("\f")
    pages = [page for page in pages if page.strip()]
    if len(pages) != last - first + 1:
        raise ValueError(f"Expected {last - first + 1} pages, extracted {len(pages)}")
    return pages


def parse(pages: list[str], first_page: int) -> tuple[list[dict], list[dict]]:
    modules: list[dict] = []
    outcomes: list[dict] = []
    current_module: dict | None = None
    current_outcome: dict | None = None
    in_outcomes = False

    def flush_outcome() -> None:
        nonlocal current_outcome
        if current_outcome is not None:
            current_outcome["outcome_text"] = clean(current_outcome["outcome_text"])
            outcomes.append(current_outcome)
            current_outcome = None

    for offset, page in enumerate(pages):
        page_number = first_page + offset
        for raw_line in page.splitlines():
            if any(marker in raw_line for marker in HEADER_MARKERS):
                continue
            if re.fullmatch(r"\s*\d{1,2}\s*", raw_line):
                continue
            line = raw_line.rstrip()
            stripped = clean(line)
            if not stripped:
                continue
            if stripped in {"AS Level subject content", "A Level subject content"}:
                continue

            topic_match = TOPIC_RE.match(line)
            if topic_match:
                topic_no = int(topic_match.group(1))
                if topic_no in TOPICS and clean(topic_match.group(2)) == TOPICS[topic_no]:
                    flush_outcome()
                    current_module = None
                    in_outcomes = False
                    continue

            module_match = MODULE_RE.match(line)
            if module_match:
                flush_outcome()
                topic_no = int(module_match.group(1))
                module_within_topic = int(module_match.group(2))
                current_module = {
                    "topic_number": topic_no,
                    "topic_name": TOPICS[topic_no],
                    "module_number": f"{topic_no}.{module_within_topic}",
                    "module_name": clean(module_match.group(3)),
                    "source_syllabus_page": page_number,
                }
                modules.append(current_module)
                in_outcomes = False
                continue

            if stripped == "Candidates should be able to:":
                in_outcomes = True
                continue

            if not in_outcomes or current_module is None:
                continue

            outcome_match = OUTCOME_RE.match(line)
            if outcome_match:
                number = int(outcome_match.group(1))
                # Outcome numbering restarts at 1 within each module. A line that
                # does not advance the expected sequence is mathematical layout
                # content and belongs to the current outcome.
                expected = 1 + sum(
                    1
                    for outcome in outcomes
                    if outcome["module_number"] == current_module["module_number"]
                )
                if current_outcome and current_outcome["module_number"] == current_module["module_number"]:
                    expected += 1
                if number == expected:
                    flush_outcome()
                    module_within_topic = int(current_module["module_number"].split(".")[1])
                    current_outcome = {
                        "topic_number": current_module["topic_number"],
                        "module_number": current_module["module_number"],
                        "outcome_number": number,
                        "outcome_id": (
                            f"9702_t{current_module['topic_number']:02d}"
                            f"_m{module_within_topic:02d}_o{number:02d}"
                        ),
                        "outcome_text": clean(outcome_match.group(2)),
                        "source_syllabus_page": page_number,
                    }
                    continue

            if current_outcome is not None:
                current_outcome["outcome_text"] += " " + stripped

    flush_outcome()
    return modules, outcomes


def write_files(
    output_dir: Path,
    level_slug: str,
    section: str,
    topic_range: range,
    modules: list[dict],
    outcomes: list[dict],
    source_path: str,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    selected_modules = [m for m in modules if m["topic_number"] in topic_range]
    selected_outcomes = [o for o in outcomes if o["topic_number"] in topic_range]
    metadata = {
        "schema_version": "9702_syllabus_spine_v1",
        "subject_code": "9702",
        "subject_name": "Physics",
        "syllabus_years": "2025-2027",
        "syllabus_section": section,
        "level": level_slug,
        "source_syllabus_pdf_path": source_path,
    }

    topics = []
    for topic_no in topic_range:
        topic_modules = []
        for module in selected_modules:
            if module["topic_number"] != topic_no:
                continue
            module_no = int(module["module_number"].split(".")[1])
            topic_modules.append(
                {
                    "module_id": f"9702_t{topic_no:02d}_m{module_no:02d}",
                    "module_number": module["module_number"],
                    "module_name": module["module_name"],
                    "source_syllabus_page": module["source_syllabus_page"],
                }
            )
        topics.append(
            {
                "topic_id": f"9702_t{topic_no:02d}",
                "topic_number": topic_no,
                "topic_name": TOPICS[topic_no],
                "modules": topic_modules,
            }
        )

    taxonomy = {**metadata, "topics": topics}
    taxonomy_path = output_dir / f"9702-2025-2027-{level_slug}-taxonomy.json"
    taxonomy_path.write_text(
        json.dumps(taxonomy, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    outcome_records = []
    for outcome in selected_outcomes:
        topic_no = outcome["topic_number"]
        module_no = int(outcome["module_number"].split(".")[1])
        outcome_records.append(
            {
                "outcome_id": outcome["outcome_id"],
                "topic_id": f"9702_t{topic_no:02d}",
                "module_id": f"9702_t{topic_no:02d}_m{module_no:02d}",
                "outcome_number": outcome["outcome_number"],
                "outcome_text": outcome["outcome_text"],
                "source_syllabus_page": outcome["source_syllabus_page"],
            }
        )
    outcome_registry = {
        **metadata,
        "text_format": "official-pdf-extracted-plain-text",
        "outcomes": outcome_records,
    }
    outcome_path = output_dir / f"9702-2025-2027-{level_slug}-learning-outcomes.json"
    outcome_path.write_text(
        json.dumps(outcome_registry, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--pdftotext", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()

    pages = page_texts(args.pdf, args.pdftotext, 16, 39)
    modules, outcomes = parse(pages, 16)
    source_path = "syllabus/664565-2025-2027-syllabus/664565-2025-2027-syllabus.pdf"
    write_files(
        args.output_root / "as",
        "as",
        "AS Level subject content",
        range(1, 12),
        modules,
        outcomes,
        source_path,
    )
    write_files(
        args.output_root / "a2",
        "a2",
        "A Level subject content",
        range(12, 26),
        modules,
        outcomes,
        source_path,
    )


if __name__ == "__main__":
    main()
