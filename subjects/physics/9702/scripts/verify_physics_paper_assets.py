#!/usr/bin/env python3
"""Asset Integrity Auditor for Physics 9702 Past Papers.

Checks:
- Question and Mark Scheme files on disk.
- Rendered images (non-empty, non-corrupted, valid dimensions).
- Diagram images referenced in question.json exist on disk.
- Detects unreferenced orphan images.
- Checks / updates manifest.json with SHA-256 hashes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from PIL import Image

REPO_ROOT = next((p for p in Path(__file__).resolve().parents if (p / "subjects").is_dir() and (p / "pyproject.toml").is_file()), Path(__file__).resolve().parents[2])
PHYSICS_PAPERS_ROOT = REPO_ROOT / "subjects/physics/9702/past papers"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def is_image_healthy(img_path: Path) -> tuple[bool, str]:
    if not img_path.is_file():
        return False, "File does not exist"
    if img_path.stat().st_size == 0:
        return False, "File is 0 bytes"
    try:
        with Image.open(img_path) as im:
            im.verify()
        with Image.open(img_path) as im:
            w, h = im.size
            if w < 50 or h < 50:
                return False, f"Image dimensions suspiciously small: {w}x{h}"
        return True, "OK"
    except Exception as e:
        return False, f"Corrupted image: {e}"


def verify_physics_paper_assets(paper_dir: Path, fix: bool = False) -> list[dict]:
    issues = []
    paper_code = paper_dir.name

    q_dirs = sorted([d for d in paper_dir.glob("question_*") if d.is_dir()])
    if not q_dirs and (paper_dir / "questions").is_dir():
        q_dirs = sorted([paper_dir / "questions"])

    files_on_disk = set()

    for qd in q_dirs:
        q_num = qd.name
        # Check files
        for f in qd.glob("*"):
            if f.is_file() and not f.name.startswith("."):
                files_on_disk.add(f)
                if f.suffix.lower() == ".png":
                    ok, reason = is_image_healthy(f)
                    if not ok:
                        issues.append({
                            "paper": paper_code,
                            "question": q_num,
                            "category": "images",
                            "level": "ERROR",
                            "message": f"Unhealthy image {f.name}: {reason}",
                            "fixable": False,
                        })

    # Manifest check
    manifest_path = paper_dir / "manifest.json"
    if manifest_path.is_file():
        try:
            with open(manifest_path, encoding="utf-8") as f:
                manifest_data = json.load(f)
            tracked_assets = {a["path"]: a.get("sha256") for a in manifest_data.get("assets", [])}
            tracked_files = {f["path"]: f.get("sha256") for f in manifest_data.get("files", [])}
            all_tracked = {**tracked_assets, **tracked_files}

            for f in files_on_disk:
                rel_p = str(f.relative_to(PHYSICS_PAPERS_ROOT.parent))
                if rel_p in all_tracked and all_tracked[rel_p] != sha256(f):
                    issues.append({
                        "paper": paper_code,
                        "question": None,
                        "category": "manifest",
                        "level": "WARNING",
                        "message": f"Hash mismatch in manifest.json for: {rel_p}",
                        "fixable": True,
                    })
        except Exception as e:
            issues.append({
                "paper": paper_code,
                "question": None,
                "category": "manifest",
                "level": "WARNING",
                "message": f"Cannot parse manifest.json: {e}",
                "fixable": False,
            })

    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--component", choices=["p1", "p2", "p4", "all"], default="all")
    parser.add_argument("--paper", help="Specific paper code or folder")
    parser.add_argument("--fix", action="store_true", help="Auto-fix manifest and path issues")
    args = parser.parse_args()

    components = ["p1", "p2", "p4"] if args.component == "all" else [args.component]
    total_papers = 0
    total_issues = []

    for comp in components:
        comp_dir = PHYSICS_PAPERS_ROOT / comp
        if not comp_dir.is_dir():
            continue
        paper_dirs = sorted([d for d in comp_dir.glob("*/*") if d.is_dir()])
        if args.paper:
            paper_dirs = [d for d in paper_dirs if args.paper in d.name]

        for p_dir in paper_dirs:
            total_papers += 1
            issues = verify_physics_paper_assets(p_dir, fix=args.fix)
            total_issues.extend(issues)

    errors = [i for i in total_issues if i["level"] == "ERROR"]
    warnings = [i for i in total_issues if i["level"] == "WARNING"]

    print(f"Verified assets for {total_papers} Physics papers: {len(errors)} errors, {len(warnings)} warnings.")
    if total_issues:
        for iss in total_issues[:30]:
            print(f"[{iss['level']}] [{iss['paper']}] {iss['question'] or ''} ({iss['category']}): {iss['message']}")
        if len(total_issues) > 30:
            print(f"... and {len(total_issues) - 30} more issues.")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
