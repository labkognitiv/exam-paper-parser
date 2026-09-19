#!/usr/bin/env python3
"""
Sync 5-Paper Batch Pipeline Output to Physics Past-Paper Reviewer Prototype
Copies question slices, mark schemes, PDFs, and unified OCR + Enrichment JSONs into
`subjects/physics/9702/prototypes/past-paper-question-reviewer/public/data/`
"""

import json
import shutil
from pathlib import Path

import argparse
import json
import re
import shutil
from pathlib import Path

DEFAULT_BATCH_OUTPUT = Path("/Users/abdullahaftab/Kognitiv/exam-paper-parser/subjects/physics/9702/testing/output_batch_papers")
PROTOTYPE_DATA = Path("/Users/abdullahaftab/Kognitiv/exam-paper-parser/subjects/physics/9702/prototypes/past-paper-question-reviewer/public/data")

PAPERS_META = {
    "9702_s22_22": {
        "title": "May/June 2022 (P22)",
        "full_title": "Physics 9702 · Paper 22 (AS Structured Questions)",
        "session": "May/June",
        "year": 2022,
        "variant": "22",
        "paper_code": "9702/22/M/J/22"
    },
    "9702_m23_22": {
        "title": "Feb/March 2023 (P22)",
        "full_title": "Physics 9702 · Paper 22 (AS Structured Questions)",
        "session": "Feb/March",
        "year": 2023,
        "variant": "22",
        "paper_code": "9702/22/F/M/23"
    },
    "9702_s23_22": {
        "title": "May/June 2023 (P22)",
        "full_title": "Physics 9702 · Paper 22 (AS Structured Questions)",
        "session": "May/June",
        "year": 2023,
        "variant": "22",
        "paper_code": "9702/22/M/J/23"
    },
    "9702_s23_23": {
        "title": "May/June 2023 (P23)",
        "full_title": "Physics 9702 · Paper 23 (AS Structured Questions)",
        "session": "May/June",
        "year": 2023,
        "variant": "23",
        "paper_code": "9702/23/M/J/23"
    },
    "9702_w23_21": {
        "title": "Oct/Nov 2023 (P21)",
        "full_title": "Physics 9702 · Paper 21 (AS Structured Questions)",
        "session": "Oct/Nov",
        "year": 2023,
        "variant": "21",
        "paper_code": "9702/21/O/N/23"
    },
    "9702_w23_22": {
        "title": "Oct/Nov 2023 (P22)",
        "full_title": "Physics 9702 · Paper 22 (AS Structured Questions)",
        "session": "Oct/Nov",
        "year": 2023,
        "variant": "22",
        "paper_code": "9702/22/O/N/23"
    }
}

def derive_paper_meta(paper_code: str) -> dict:
    if paper_code in PAPERS_META:
        return PAPERS_META[paper_code]
    
    m = re.match(r"9702_([msw])(\d{2})_(\d{2})", paper_code.lower())
    if m:
        season_char, yr_str, var_str = m.group(1), m.group(2), m.group(3)
        year = 2000 + int(yr_str)
        season_map = {"m": "Feb/March", "s": "May/June", "w": "Oct/Nov"}
        season_code = {"m": "F/M", "s": "M/J", "w": "O/N"}
        session = season_map.get(season_char, "Past Paper")
        code_middle = season_code.get(season_char, "P")
        return {
            "title": f"{session} {year} (P{var_str})",
            "full_title": f"Physics 9702 · Paper {var_str} (AS Structured Questions)",
            "session": session,
            "year": year,
            "variant": var_str,
            "paper_code": f"9702/{var_str}/{code_middle}/{yr_str}"
        }
    return {
        "title": paper_code,
        "full_title": paper_code,
        "session": "Past Paper",
        "year": 2022,
        "variant": "22",
        "paper_code": paper_code
    }

def sync_paper(paper_dir: Path):
    if not paper_dir.is_dir():
        return None
    paper_code = paper_dir.name
    meta_info = derive_paper_meta(paper_code)

    papers_out_dir = PROTOTYPE_DATA / "papers"
    papers_out_dir.mkdir(parents=True, exist_ok=True)
    
    paper_assets_dir = PROTOTYPE_DATA / "assets" / paper_code
    paper_assets_dir.mkdir(parents=True, exist_ok=True)

    # Copy full paper PDFs if present
    for pdf_name in ("paper_compact.pdf", "paper_printable.pdf"):
        src = paper_dir / pdf_name
        if src.exists():
            shutil.copy2(src, paper_assets_dir / pdf_name)
            
    ms_pdf = paper_dir / "mark_scheme" / "paper_markscheme.pdf"
    if ms_pdf.exists():
        shutil.copy2(ms_pdf, paper_assets_dir / "paper_markscheme.pdf")

    # Discover questions
    ocr_files = sorted(paper_dir.glob("question_*_ocr.json"))
    if not ocr_files:
        return None

    questions_dict = {}

    for ocr_file in ocr_files:
        stem = ocr_file.stem.replace("_ocr", "") # e.g. question_01
        q_num_str = stem.split("_")[-1]
        q_num = int(q_num_str)
        q_key = f"q{q_num:02d}"

        with open(ocr_file, encoding="utf-8") as f:
            ocr_data = json.load(f)

        enrichment_file = paper_dir / f"{stem}_enrichment.json"
        enrichment_data = {}
        if enrichment_file.exists():
            with open(enrichment_file, encoding="utf-8") as f:
                enrichment_data = json.load(f)

        q_asset_dir = PROTOTYPE_DATA / "assets" / f"{paper_code}_q{q_num:02d}"
        q_asset_dir.mkdir(parents=True, exist_ok=True)

        compact_png = paper_dir / f"{stem}_compact.png"
        if compact_png.exists():
            shutil.copy2(compact_png, q_asset_dir / "question_compact.png")

        printable_png = paper_dir / f"{stem}_printable.png"
        if printable_png.exists():
            shutil.copy2(printable_png, q_asset_dir / "question_printable.png")

        printable_pdf = paper_dir / f"{stem}_printable.pdf"
        if printable_pdf.exists():
            shutil.copy2(printable_pdf, q_asset_dir / "question_printable.pdf")

        ms_slice = paper_dir / "mark_scheme" / f"ms_q{q_num:02d}.png"
        if ms_slice.exists():
            shutil.copy2(ms_slice, q_asset_dir / "markscheme.png")

        # Copy standalone figure PNGs
        q_figs_file = paper_dir / f"{stem}_figures.json"
        q_figs_list = []
        if q_figs_file.exists():
            try:
                with open(q_figs_file, encoding="utf-8") as f_figs:
                    q_figs_list = json.load(f_figs)
            except Exception:
                pass
                
        figure_urls = {}
        for fig in q_figs_list:
            fig_file = fig.get("file")
            src_fig = paper_dir / fig_file
            if src_fig.exists():
                shutil.copy2(src_fig, q_asset_dir / fig_file)
                shutil.copy2(src_fig, paper_assets_dir / fig_file)
                figure_urls[fig["id"]] = f"/data/assets/{paper_code}_q{q_num:02d}/{fig_file}"

        enr_parts_map = {}
        for ep in enrichment_data.get("parts", []):
            label = ep.get("part") or ""
            clean_label = label.lower().replace(" ", "")
            enr_parts_map[clean_label] = ep

        ms_parts_map = {}
        for mp in ocr_data.get("markscheme", []):
            label = mp.get("label") or ""
            clean_label = label.lower().replace(" ", "")
            ms_parts_map[clean_label] = mp.get("marking_points", [])

        merged_parts = []
        for p in ocr_data.get("parts", []):
            label = p.get("label") or ""
            clean_label = label.lower().replace(" ", "")
            matching_enr = enr_parts_map.get(clean_label) or {}
            matching_ms_points = ms_parts_map.get(clean_label) or []

            merged_parts.append({
                "label": label,
                "part_stem": p.get("part_stem"),
                "text": p.get("text", ""),
                "marks": p.get("marks"),
                "answer_prompt": p.get("answer_prompt"),
                "unit": p.get("unit"),
                "hints": matching_enr.get("hints", []),
                "teacher_walkthrough": matching_enr.get("teacher_walkthrough", []),
                "walkthrough": matching_enr.get("walkthrough", []),
                "markscheme_points": matching_ms_points,
                "common_pitfalls": matching_enr.get("common_pitfalls", []),
                "formulas_used": matching_enr.get("formulas_used", []),
                "target_time_minutes": matching_enr.get("target_time_minutes")
            })

        q_entry = {
            "question_num": q_num,
            "total_marks": ocr_data.get("total_marks", sum(p.get("marks", 0) for p in merged_parts if p.get("marks"))),
            "title": ocr_data.get("title") or f"Theory Question {q_num}",
            "main_stem": ocr_data.get("main_stem"),
            "figures": q_figs_list,
            "figure_urls": figure_urls,
            "parts": merged_parts,
            "markscheme": ocr_data.get("markscheme", []),
            "difficulty": enrichment_data.get("difficulty", 2),
            "question_patterns": enrichment_data.get("question_patterns", []),
            "meta": {
                "model": "meta/muse-spark-1.3-contributor",
                "compact_image_url": f"/data/assets/{paper_code}_q{q_num:02d}/question_compact.png",
                "printable_image_url": f"/data/assets/{paper_code}_q{q_num:02d}/question_printable.png",
                "printable_pdf_url": f"/data/assets/{paper_code}_q{q_num:02d}/question_printable.pdf",
                "markscheme_image_url": f"/data/assets/{paper_code}_q{q_num:02d}/markscheme.png" if ms_slice.exists() else None,
            }
        }
        questions_dict[q_key] = q_entry

    paper_json = {
        "paper_code": paper_code,
        "metadata": meta_info,
        "total_questions": len(questions_dict),
        "total_marks": sum(q["total_marks"] for q in questions_dict.values()),
        "questions": questions_dict
    }

    out_file = papers_out_dir / f"{paper_code}.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(paper_json, f, indent=2, ensure_ascii=False)

    print(f"✓ Synced {paper_code}: {len(questions_dict)} questions -> {out_file.name}")
    return {
        "paper_code": paper_code,
        "title": meta_info["title"],
        "full_title": meta_info["full_title"],
        "year": meta_info["year"],
        "session": meta_info["session"],
        "variant": meta_info["variant"],
        "total_questions": len(questions_dict),
        "total_marks": sum(q["total_marks"] for q in questions_dict.values()),
        "json_url": f"/data/papers/{paper_code}.json",
        "paper_compact_pdf": f"/data/assets/{paper_code}/paper_compact.pdf",
        "paper_printable_pdf": f"/data/assets/{paper_code}/paper_printable.pdf",
        "paper_markscheme_pdf": f"/data/assets/{paper_code}/paper_markscheme.pdf"
    }

def main():
    parser = argparse.ArgumentParser(description="Sync Batch Output to Prototype")
    parser.add_argument("--batch-dirs", nargs="+", default=[
        str(DEFAULT_BATCH_OUTPUT),
        "/Users/abdullahaftab/Kognitiv/exam-paper-parser/subjects/physics/9702/testing/output_batch_5papers"
    ], help="Directories containing processed papers")
    args = parser.parse_args()

    manifest_papers = {}
    for b_dir_str in args.batch_dirs:
        b_dir = Path(b_dir_str)
        if not b_dir.exists():
            continue
        for paper_dir in sorted(b_dir.iterdir()):
            if paper_dir.is_dir() and paper_dir.name.startswith("9702_"):
                res = sync_paper(paper_dir)
                if res and res["paper_code"] not in manifest_papers:
                    manifest_papers[res["paper_code"]] = res

    # Sort manifest papers: 2022 first (or by year descending)
    sorted_papers = sorted(manifest_papers.values(), key=lambda p: (p["year"], p["session"], p["variant"]), reverse=True)
    
    # Put 9702_s22_22 at the front if present
    s22_idx = next((i for i, p in enumerate(sorted_papers) if p["paper_code"] == "9702_s22_22"), None)
    if s22_idx is not None:
        target = sorted_papers.pop(s22_idx)
        sorted_papers.insert(0, target)

    manifest_file = PROTOTYPE_DATA / "papers_manifest.json"
    with open(manifest_file, "w", encoding="utf-8") as f:
        json.dump({"papers": sorted_papers}, f, indent=2, ensure_ascii=False)

    print(f"\nManifest written to {manifest_file} with {len(sorted_papers)} papers!")

if __name__ == "__main__":
    main()
