#!/usr/bin/env python3
"""
scripts/extract_physics_p4_papers.py

Extracts sample or specified Cambridge Physics 9702 Paper 4 (A2 Theory) PDFs:
1. Copies requested PDF(s) from Desktop to subjects/physics/9702/sources/p4/
2. Extracts Question Paper(s) to subjects/physics/9702/papers/p4/parsed-questions/<paper_code>/
3. Extracts Mark Scheme(s) to subjects/physics/9702/papers/p4/mark-schemes/<paper_code>/

Usage:
  .venv/bin/python scripts/extract_physics_p4_papers.py --paper 9702_s22_42
  .venv/bin/python scripts/extract_physics_p4_papers.py --limit 2
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DESKTOP_DIR = Path.home() / "Desktop/A-Level-Physics-9702"

INPUT_P4_QP = ROOT / "subjects/physics/9702/sources/p4/question-papers"
INPUT_P4_MS = ROOT / "subjects/physics/9702/sources/p4/mark-schemes"

OUTPUT_P4_QP = ROOT / "subjects/physics/9702/papers/p4/parsed-questions"
OUTPUT_P4_MS = ROOT / "subjects/physics/9702/papers/p4/mark-schemes"

def normalize_code(name: str) -> str:
    # 9702_s22_qp_42 -> 9702_s22_42
    return re.sub(r"_(qp|ms)_", "_", name.lower().replace(".pdf", ""))

def main():
    parser = argparse.ArgumentParser(description="Extract sample Physics 9702 P4 papers.")
    parser.add_argument("--paper", type=str, help="Specific paper code to extract (e.g. 9702_s22_42 or 9702_m22_42)")
    parser.add_argument("--limit", type=int, default=2, help="Number of sample papers to process if --paper is not specified (default: 2)")
    args = parser.parse_args()

    print("=== Physics 9702 Paper 4 (A2 Theory) Extractor ===")

    INPUT_P4_QP.mkdir(parents=True, exist_ok=True)
    INPUT_P4_MS.mkdir(parents=True, exist_ok=True)
    OUTPUT_P4_QP.mkdir(parents=True, exist_ok=True)
    OUTPUT_P4_MS.mkdir(parents=True, exist_ok=True)

    target_qps = []
    target_mss = []

    if DESKTOP_DIR.exists():
        all_pdfs = list(DESKTOP_DIR.glob("**/*.pdf"))
        print(f"Scanning {DESKTOP_DIR} ({len(all_pdfs)} total PDFs found)...")

        if args.paper:
            target_norm = normalize_code(args.paper)
            print(f"Searching for target paper code: '{target_norm}'")
            for p in all_pdfs:
                fn = p.name.lower()
                norm = normalize_code(fn)
                if norm == target_norm:
                    if "_qp_" in fn:
                        dest = INPUT_P4_QP / p.name
                        shutil.copy2(p, dest)
                        target_qps.append(dest)
                    elif "_ms_" in fn:
                        dest = INPUT_P4_MS / p.name
                        shutil.copy2(p, dest)
                        target_mss.append(dest)
        else:
            # Pick recent papers
            recent_qps = sorted([p for p in all_pdfs if "_qp_4" in p.name.lower() and any(y in p.name for y in ["_s22_", "_m22_", "_w22_", "_s23_"])])
            for qp in recent_qps[:args.limit]:
                dest_qp = INPUT_P4_QP / qp.name
                shutil.copy2(qp, dest_qp)
                target_qps.append(dest_qp)

                ms_name = qp.name.replace("_qp_", "_ms_")
                ms_candidates = [p for p in all_pdfs if p.name == ms_name]
                if ms_candidates:
                    dest_ms = INPUT_P4_MS / ms_candidates[0].name
                    shutil.copy2(ms_candidates[0], dest_ms)
                    target_mss.append(dest_ms)

    # Fallback to local input
    if not target_qps:
        target_qps = sorted(INPUT_P4_QP.glob("*.pdf"))[:args.limit]
    if not target_mss:
        target_mss = sorted(INPUT_P4_MS.glob("*.pdf"))[:args.limit]

    print(f"\nTarget Question Papers ({len(target_qps)}): {[p.name for p in target_qps]}")
    print(f"Target Mark Schemes ({len(target_mss)}): {[p.name for p in target_mss]}")

    if not target_qps:
        print("Error: No target Question Paper PDFs found.")
        sys.exit(1)

    # 2. Extract Question Papers into paper-specific subfolders
    for idx, qp in enumerate(target_qps, 1):
        print(f"\n[{idx}/{len(target_qps)}] Parsing QP: {qp.name}")
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
            print(f"  ✓ Success QP: {qp_out_dir.name} ({len(list(qp_out_dir.glob('*')))} files)")
        else:
            print(f"  ✗ Error on {qp.name}: {res.stderr.strip() or res.stdout.strip()}")

    # 3. Extract Mark Schemes into paper-specific subfolders
    for idx, ms in enumerate(target_mss, 1):
        print(f"\n[{idx}/{len(target_mss)}] Parsing MS: {ms.name}")
        cmd = [
            sys.executable,
            "-m", "markscheme_converter",
            str(ms),
            "--output", str(OUTPUT_P4_MS)
        ]
        res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        if res.returncode == 0:
            ms_out_dir = OUTPUT_P4_MS / ms.stem
            print(f"  ✓ Success MS: {ms_out_dir.name} ({len(list(ms_out_dir.glob('*')))} files)")
        else:
            print(f"  ✗ Error on {ms.name}: {res.stderr.strip() or res.stdout.strip()}")

    # Clean loose files in OUTPUT_P4_QP if any
    for loose in OUTPUT_P4_QP.glob("*.*"):
        if loose.is_file():
            loose.unlink()

    print("\n=== Extraction Complete ===")

if __name__ == "__main__":
    main()
