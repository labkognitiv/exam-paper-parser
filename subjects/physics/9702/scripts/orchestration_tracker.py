#!/usr/bin/env python3
"""Orchestration Tracker Manager for Cambridge Physics (9702).

Maintains separate, persistent trackers for:
- Paper 1 (MCQ): subjects/physics/9702/reviews/p1-orchestration-tracker.md
- Paper 2 (AS Theory): subjects/physics/9702/reviews/p2-orchestration-tracker.md
- Paper 4 (A Level Theory): subjects/physics/9702/reviews/p4-orchestration-tracker.md

Zero em dashes, zero en dashes.
"""

from __future__ import annotations

import datetime
import fcntl
import json
from pathlib import Path
from typing import Any

REPO_ROOT = next(
    (p for p in Path(__file__).resolve().parents if (p / "subjects").is_dir() and (p / "pyproject.toml").is_file()),
    Path(__file__).resolve().parents[3],
)
REVIEWS_DIR = REPO_ROOT / "subjects/physics/9702/reviews"


def _get_tracker_paths(component: str) -> tuple[Path, Path]:
    c = component.lower()
    if c not in ("p1", "p2", "p4"):
        raise ValueError(f"Unknown component: {component}. Expected 'p1', 'p2', or 'p4'.")
    REVIEWS_DIR.mkdir(parents=True, exist_ok=True)
    json_path = REVIEWS_DIR / f"{c}-orchestration-tracker.json"
    md_path = REVIEWS_DIR / f"{c}-orchestration-tracker.md"
    return json_path, md_path


def load_tracker_data(component: str) -> dict[str, Any]:
    json_path, _ = _get_tracker_paths(component)
    if json_path.is_file():
        try:
            with open(json_path, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "component": component.upper(),
        "last_updated": None,
        "runs": [],
    }


def save_tracker_data(component: str, data: dict[str, Any]) -> None:
    json_path, md_path = _get_tracker_paths(component)
    data["last_updated"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    md_content = render_tracker_markdown(component, data)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)


def record_orchestration_run(component: str, record: dict[str, Any]) -> None:
    c = component.lower()
    json_path, _ = _get_tracker_paths(c)
    lock_path = json_path.with_suffix(".lock")

    with open(lock_path, "w") as lock_file:
        fcntl.flock(lock_file, fcntl.LOCK_EX)
        try:
            data = load_tracker_data(c)
            runs = data.get("runs", [])

            paper_code = record.get("paper_code", "")
            now_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M")
            record.setdefault("date", now_str)

            existing_idx = next((i for i, r in enumerate(runs) if r.get("paper_code") == paper_code), None)
            if existing_idx is not None:
                runs[existing_idx] = record
            else:
                runs.append(record)

            data["runs"] = runs
            save_tracker_data(c, data)
        finally:
            fcntl.flock(lock_file, fcntl.LOCK_UN)


def render_tracker_markdown(component: str, data: dict[str, Any]) -> str:
    c = component.lower()
    runs = data.get("runs", [])
    title_map = {
        "p1": "Paper 1 (Multiple Choice)",
        "p2": "Paper 2 (AS Level Structured Theory)",
        "p4": "Paper 4 (A Level Structured Theory)",
    }
    title = title_map.get(c, f"Paper {component.upper()}")

    complete_count = sum(1 for r in runs if r.get("status") == "COMPLETE")
    total_cost = sum(r.get("cost_usd", 0.0) for r in runs)
    last_up = data.get("last_updated") or "Never"

    lines = [
        f"# Physics 9702 {title} Orchestration Tracker",
        "",
        f"Last updated: {last_up}",
        "",
        "This tracker records automated single-command orchestration runs for Cambridge Physics (9702).",
        "All verification passes, OCR reviews, pedagogical enrichments, and model costs are tracked per paper.",
        "",
        "## Summary",
        "",
        "| Measure | Count |",
        "|---|---:|",
        f"| Total Papers Tracked | {len(runs)} |",
        f"| Fully Orchestrated (COMPLETE) | {complete_count} |",
        f"| Total Pipeline Cost | ${total_cost:.4f} |",
        "",
        "## Orchestration Runs",
        "",
        "| Paper | Date | Questions | Marks | Slicing | OCR | MS | Review | Enrichment | Verification | Cost ($) | Time (s) | Status |",
        "|---|---|---:|---:|:---:|:---:|:---:|:---:|:---:|:---:|---:|---:|:---:|",
    ]

    for r in sorted(runs, key=lambda x: x.get("paper_code", "")):
        p_code = r.get("paper_code", "-")
        date_str = r.get("date", "-")
        q_count = r.get("questions_count", "-")
        marks = r.get("total_marks", "-")
        slicing = r.get("slicing", "-")
        ocr = r.get("question_ocr", "-")
        ms = r.get("mark_scheme", "-")
        rev = r.get("ocr_review", "-")
        enr = r.get("enrichment", "-")
        ver = r.get("verification", "-")
        cost = f"${r.get('cost_usd', 0.0):.4f}"
        dur = f"{r.get('duration_sec', 0.0):.1f}"
        stat = r.get("status", "-")

        lines.append(
            f"| `{p_code}` | {date_str} | {q_count} | {marks} | {slicing} | {ocr} | {ms} | {rev} | {enr} | {ver} | {cost} | {dur} | {stat} |"
        )

    lines.append("")
    return "\n".join(lines)
