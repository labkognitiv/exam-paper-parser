#!/usr/bin/env python3
"""
scripts/extract_all_p4_papers.py

1. Copies all Cambridge Physics 9702 Paper 4 (2016-2025) PDFs from Desktop:
   - subjects/physics/9702/sources/p4/question-papers/
   - subjects/physics/9702/sources/p4/mark-schemes/
2. Extracts Question Papers into subjects/physics/9702/papers/p4/parsed-questions/<paper_code>/
3. Extracts Mark Schemes into subjects/physics/9702/papers/p4/mark-schemes/<paper_code>/
4. Runs automated verification across all extracted papers.
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

ROOT = Path(__file__).resolve().parent.parent
DESKTOP_DIR = Path.home() / "Desktop/A-Level-Physics-9702"

INPUT_P4_QP = ROOT / "subjects/physics/9702/sources/p4/question-papers"
INPUT_P4_MS = ROOT / "subjects/physics/9702/sources/p4/mark-schemes"

OUTPUT_P4_QP = ROOT / "subjects/physics/9702/papers/p4/parsed-questions"
OUTPUT_P4_MS = ROOT / "subjects/physics/9702/papers/p4/mark-schemes"

def normalize_code(name: str) -> str:
    return re.sub(r"_(qp|ms)_", "_", name.lower().replace(".pdf", ""))

def parse_single_qp(qp_path_str: str) -> tuple[str, bool, str]:
    qp = Path(qp_path_str)
    qp_out_dir = OUTPUT_P4_QP / qp.stem
    qp_out_dir.mkdir(parents=True, exist_ok=True)
    
    cmd = [
        sys.executable,
        "-m", "question_compactor",
        str(qp),
        "--output-dir", str(qp_out_dir)
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if res.returncode == 0:
        return qp.stem, True, ""
    return qp.stem, False, res.stderr.strip() or res.stdout.strip()

def parse_single_ms(ms_path_str: str) -> tuple[str, bool, str]:
    ms = Path(ms_path_str)
    cmd = [
        sys.executable,
        "-m", "markscheme_converter",
        str(ms),
        "--output", str(OUTPUT_P4_MS)
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if res.returncode == 0:
        return ms.stem, True, ""
    return ms.stem, False, res.stderr.strip() or res.stdout.strip()

def verify_all_extracted_papers(min_year=16):
    print("\n=== Running Comprehensive P4 Extraction Verification ===")
    
    qp_dirs = sorted([d for d in OUTPUT_P4_QP.glob("9702_*_qp_4*") if d.is_dir()])
    ms_dirs = sorted([d for d in OUTPUT_P4_MS.glob("9702_*_ms_4*") if d.is_dir()])

    total_papers = 0
    passed_papers = 0
    issues = []

    print(f"Found {len(qp_dirs)} QP directories, {len(ms_dirs)} MS directories.")

    ms_dir_map = {normalize_code(d.name): d for d in ms_dirs}

    for qp_dir in qp_dirs:
        code = normalize_code(qp_dir.name)
        match_year = re.search(r"_([msw])(\d{2})_", qp_dir.name)
        if match_year and int(match_year.group(2)) < min_year:
            continue

        total_papers += 1
        ms_dir = ms_dir_map.get(code)

        if not ms_dir:
            issues.append(f"{code}: Missing matching mark scheme directory")
            continue

        q_json_files = sorted(qp_dir.glob("question_*.json"))
        ms_json_files = sorted(ms_dir.glob("markscheme_*.json"))

        if not q_json_files:
            issues.append(f"{code}: No question_*.json files in {qp_dir.name}")
            continue

        if len(q_json_files) != len(ms_json_files):
            issues.append(f"{code}: Question count mismatch (QP has {len(q_json_files)}, MS has {len(ms_json_files)})")
            continue

        # Check question and mark scheme files
        paper_errors = []
        for q_file in q_json_files:
            qnum = q_file.stem.replace("question_", "")
            ms_file = ms_dir / f"markscheme_{qnum}.json"
            if not ms_file.exists():
                paper_errors.append(f"Missing {ms_file.name}")
                continue

            q_img = qp_dir / f"question_{qnum}_with_figures.png"
            if not q_img.exists():
                q_img = qp_dir / f"question_{qnum}.png"
                if not q_img.exists():
                    paper_errors.append(f"Missing image for question {qnum}")

            # Validate JSON loads
            try:
                qd = json.loads(q_file.read_text(encoding="utf-8"))
                msd = json.loads(ms_file.read_text(encoding="utf-8"))
                
                # Check mark totals
                q_total = qd.get("total_marks")
                ms_total = msd.get("total_marks")
                if q_total is not None and ms_total is not None and q_total != ms_total:
                    paper_errors.append(f"Q{qnum} marks mismatch (QP={q_total}, MS={ms_total})")
            except Exception as e:
                paper_errors.append(f"Q{qnum} JSON error: {e}")

        if paper_errors:
            for pe in paper_errors:
                issues.append(f"{code}: {pe}")
        else:
            passed_papers += 1

    print(f"\nVerification Results (2016-2025):")
    print(f"Total Papers Checked: {total_papers}")
    print(f"Passed Papers: {passed_papers}")
    print(f"Failed / Incomplete Papers: {len(issues)}")

    if issues:
        print("\nIdentified Issues:")
        for iss in issues[:20]:
            print(f"  - {iss}")
        if len(issues) > 20:
            print(f"  ... and {len(issues) - 20} more issues.")
    else:
        print("\n✓ ALL EXTRACTED P4 PAPERS PASSED 100% VERIFICATION!")

def main():
    parser = argparse.ArgumentParser(description="Extract all Physics 9702 P4 papers.")
    parser.add_argument("--min-year", type=int, default=16, help="Minimum 2-digit year (default: 16 for 2016)")
    parser.add_argument("--workers", type=int, default=8, help="Number of parallel worker processes (default: 8)")
    args = parser.parse_args()

    print("=== Physics 9702 Paper 4 (A2 Theory) Batch Extractor ===")

    INPUT_P4_QP.mkdir(parents=True, exist_ok=True)
    INPUT_P4_MS.mkdir(parents=True, exist_ok=True)
    OUTPUT_P4_QP.mkdir(parents=True, exist_ok=True)
    OUTPUT_P4_MS.mkdir(parents=True, exist_ok=True)

    if not DESKTOP_DIR.exists():
        print(f"Desktop directory {DESKTOP_DIR} not found. Checking existing input...")
    else:
        print(f"Scanning {DESKTOP_DIR} for Paper 4 PDFs...")
        qp_count = 0
        ms_count = 0
        for pdf_file in DESKTOP_DIR.glob("**/*.pdf"):
            fname = pdf_file.name.lower()
            m = re.search(r"_([msw])(\d{2})_", fname)
            if m and int(m.group(2)) >= args.min_year:
                if "_qp_4" in fname:
                    dest = INPUT_P4_QP / pdf_file.name
                    shutil.copy2(pdf_file, dest)
                    qp_count += 1
                elif "_ms_4" in fname:
                    dest = INPUT_P4_MS / pdf_file.name
                    shutil.copy2(pdf_file, dest)
                    ms_count += 1

        print(f"Imported {qp_count} Question Papers to {INPUT_P4_QP}")
        print(f"Imported {ms_count} Mark Schemes to {INPUT_P4_MS}")

    # Gather QPs and MSs
    qp_pdfs = sorted([p for p in INPUT_P4_QP.glob("*.pdf") if int(re.search(r"_([msw])(\d{2})_", p.name).group(2)) >= args.min_year])
    ms_pdfs = sorted([p for p in INPUT_P4_MS.glob("*.pdf") if int(re.search(r"_([msw])(\d{2})_", p.name).group(2)) >= args.min_year])

    print(f"\nProcessing {len(qp_pdfs)} Question Papers with {args.workers} workers...")
    qp_errors = []
    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(parse_single_qp, str(p)): p for p in qp_pdfs}
        for f in as_completed(futures):
            stem, success, err = f.result()
            if success:
                print(f"  ✓ QP: {stem}")
            else:
                print(f"  ✗ QP: {stem} -> {err}")
                qp_errors.append((stem, err))

    print(f"\nProcessing {len(ms_pdfs)} Mark Schemes with {args.workers} workers...")
    ms_errors = []
    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(parse_single_ms, str(p)): p for p in ms_pdfs}
        for f in as_completed(futures):
            stem, success, err = f.result()
            if success:
                print(f"  ✓ MS: {stem}")
            else:
                print(f"  ✗ MS: {stem} -> {err}")
                ms_errors.append((stem, err))

    # Run verification check
    verify_all_extracted_papers(min_year=args.min_year)

if __name__ == "__main__":
    main()
