#!/usr/bin/env python3
"""Build lazy review data from canonical Physics 9702 paper packages (P1, P2, P4)."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import shutil


PROTOTYPE = Path(__file__).resolve().parent
SUBJECT = Path(__file__).resolve().parents[2]
PAPERS = SUBJECT / "past papers"
KNOWLEDGE = SUBJECT / "knowledge"
DATA = PROTOTYPE / "public" / "data"


def extract_subpart_texts(q_text: str, labels: list[str]) -> dict[str, str]:
    if not q_text or not labels:
        return {}
    pattern = r"(?=(?:^|\n)\s*(?:\([a-z0-9]+\)(?:\([ivx]+\))?|\([a-z]\)|\([ivx]+\)))"
    splits = [s.strip() for s in re.split(pattern, q_text) if s.strip()]
    part_map: dict[str, str] = {}
    curr_letter = ""
    for chunk in splits:
        m_full = re.match(r"^(\([a-z]\)\([ivx]+\))", chunk)
        m_num = re.match(r"^(\((?:i|ii|iii|iv|v|vi|vii|viii|ix|x|\d+)\))", chunk)
        m_let = re.match(r"^(\([a-z]\))", chunk)

        if m_full:
            tag = m_full.group(1)
            curr_letter = m_full.group(1)[:3]
            part_map[tag] = chunk
        elif m_num and curr_letter:
            tag = f"{curr_letter}{m_num.group(1)}"
            part_map[tag] = chunk
        elif m_let:
            tag = m_let.group(1)
            curr_letter = tag
            part_map[tag] = chunk

    result: dict[str, str] = {}
    for lbl in labels:
        if lbl in part_map:
            result[lbl] = part_map[lbl]
        else:
            for chunk in splits:
                if chunk.startswith(lbl):
                    result[lbl] = chunk
                    break
    return result


def read(path: Path) -> tuple[dict, list[str]]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}, [] if isinstance(value, dict) else ["JSON root is not an object"]
    except (OSError, json.JSONDecodeError) as error:
        return {}, [f"Cannot parse {path.name}: {error}"]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def find_paper_code(variant_dir: Path, component: str, season: str, year: int, variant_num: str) -> str:
    for qd in variant_dir.glob("question_*"):
        if qd.is_dir():
            for jname in ("question_ocr.json", "markscheme.json"):
                jp = qd / jname
                if jp.is_file():
                    try:
                        d = json.loads(jp.read_text(encoding="utf-8"))
                        if d.get("paper_code"):
                            return d["paper_code"]
                    except Exception:
                        pass
    source_dir = variant_dir / "source"
    if source_dir.is_dir():
        for qp in source_dir.glob("*_qp_*.pdf"):
            return qp.stem.replace("_qp_", "_")
    season_code = {"february-march": "m", "may-june": "s", "october-november": "w"}.get(season, "s")
    c_num = component.replace("p", "")
    full_var = f"{c_num}{variant_num}"
    yy = str(year)[-2:]
    return f"9702_{season_code}{yy}_{full_var}"


def match_figures_for_text(text_block: str, figures: list[dict]) -> list[dict]:
    if not text_block or not figures:
        return []
    ref_ids = []
    for m1 in re.finditer(r"\{\{figure:([^}]+)\}\}", text_block):
        ref_ids.append(m1.group(1).strip())
    matched = []
    seen = set()
    for fid in ref_ids:
        if fid in seen:
            continue
        fig = next((f for f in figures if f["id"] == fid), None)
        if fig:
            seen.add(fid)
            matched.append(fig)
    return matched


def load_knowledge() -> tuple[dict, dict, dict, dict]:
    taxonomy: dict[str, dict] = {}
    for tpath in [
        KNOWLEDGE / "2025-2027/as/9702-2025-2027-as-taxonomy.json",
        KNOWLEDGE / "2025-2027/a2/9702-2025-2027-a2-taxonomy.json",
    ]:
        if tpath.is_file():
            tdata, _ = read(tpath)
            for topic in tdata.get("topics", []):
                tid = topic.get("topic_id")
                modules = {m["module_id"]: m.get("module_name", "") for m in topic.get("modules", [])}
                taxonomy[tid] = {
                    "name": topic.get("topic_name", ""),
                    "modules": modules,
                }

    definitions: dict[str, dict] = {}
    def_path = KNOWLEDGE / "knowledge-base/definitions.json"
    if def_path.is_file():
        ddata, _ = read(def_path)
        for d in ddata.get("definitions", []):
            definitions[d["definition_id"]] = d

    formulas: dict[str, dict] = {}
    form_path = KNOWLEDGE / "knowledge-base/formulas.json"
    if form_path.is_file():
        fdata, _ = read(form_path)
        for f in fdata.get("formulas", []):
            formulas[f["formula_id"]] = f

    skills: dict[str, dict] = {}
    skill_path = KNOWLEDGE / "knowledge-base/skills.json"
    if skill_path.is_file():
        sdata, _ = read(skill_path)
        for s in sdata.get("skills", []):
            skills[s["skill_id"]] = s

    return taxonomy, definitions, formulas, skills


def main() -> None:
    if DATA.exists():
        shutil.rmtree(DATA)
    (DATA / "questions").mkdir(parents=True)
    index = {"components": [], "questionCount": 0, "issueCount": 0}
    manifest = {"description": "Derived reviewer snapshot; canonical Physics content unchanged.", "sources": []}

    taxonomy, definitions_kb, formulas_kb, skills_kb = load_knowledge()

    for component in ("p1", "p2", "p4"):
        papers = []
        comp_dir = PAPERS / component
        if not comp_dir.is_dir():
            continue

        for year_dir in sorted(comp_dir.glob("20*"), reverse=True):
            for season_dir in sorted(year_dir.iterdir()):
                if not season_dir.is_dir():
                    continue
                for paper_dir in sorted(season_dir.iterdir()):
                    if not paper_dir.is_dir():
                        continue

                    variant_num = paper_dir.name.replace("variant-", "")
                    year_val = int(year_dir.name)
                    session_names = {
                        "february-march": "Feb/March",
                        "may-june": "May/June",
                        "october-november": "Oct/Nov",
                    }
                    session_label = session_names.get(season_dir.name, season_dir.name.replace("-", " ").title())
                    paper_code = find_paper_code(paper_dir, component, season_dir.name, year_val, variant_num)

                    # Copy paper-level PDFs for every component. P1 stores its
                    # originals under source/ rather than as normalized paper_* files.
                    paper_assets_dir = DATA / "assets" / paper_code
                    paper_assets_dir.mkdir(parents=True, exist_ok=True)
                    for pdf_name in ("paper_compact.pdf", "paper_printable.pdf", "paper_markscheme.pdf"):
                        src_pdf = paper_dir / pdf_name
                        if src_pdf.is_file():
                            shutil.copy2(src_pdf, paper_assets_dir / pdf_name)
                            manifest["sources"].append({
                                "path": src_pdf.relative_to(SUBJECT).as_posix(),
                                "sha256": sha256(src_pdf),
                            })
                    if component == "p1":
                        source_dir = paper_dir / "source"
                        question_paper = next(source_dir.glob("*_qp_*.pdf"), None) if source_dir.is_dir() else None
                        mark_scheme = next(source_dir.glob("*_ms_*.pdf"), None) if source_dir.is_dir() else None
                        if question_paper:
                            shutil.copy2(question_paper, paper_assets_dir / "paper_printable.pdf")
                            shutil.copy2(question_paper, paper_assets_dir / "paper_compact.pdf")
                            manifest["sources"].append({
                                "path": question_paper.relative_to(SUBJECT).as_posix(),
                                "sha256": sha256(question_paper),
                            })
                        if mark_scheme:
                            shutil.copy2(mark_scheme, paper_assets_dir / "paper_markscheme.pdf")
                            manifest["sources"].append({
                                "path": mark_scheme.relative_to(SUBJECT).as_posix(),
                                "sha256": sha256(mark_scheme),
                            })

                    has_ocr_pipeline = any(paper_dir.glob("question_*/question_ocr.json"))
                    if has_ocr_pipeline:
                        paper_assets_dir = DATA / "assets" / paper_code
                        paper_assets_dir.mkdir(parents=True, exist_ok=True)
                        for pdf_name in ("paper_compact.pdf", "paper_printable.pdf", "paper_markscheme.pdf"):
                            src_pdf = paper_dir / pdf_name
                            if src_pdf.is_file():
                                shutil.copy2(src_pdf, paper_assets_dir / pdf_name)
                                manifest["sources"].append({
                                    "path": src_pdf.relative_to(SUBJECT).as_posix(),
                                    "sha256": sha256(src_pdf),
                                })

                        questions = []
                        for q_dir in sorted([p for p in paper_dir.glob("question_*") if p.is_dir() and ((p / "question_ocr.json").is_file() or (p / "markscheme.json").is_file() or (p / "question.txt").is_file())]):
                            num = int(q_dir.name.rsplit("_", 1)[-1])
                            question_id = f"{paper_code}_q{num:02d}"
                            q_asset_dir = DATA / "assets" / question_id
                            q_asset_dir.mkdir(parents=True, exist_ok=True)

                            figures = []
                            printable_img_url = None
                            compact_img_url = None
                            markscheme_img_url = None

                            for fpath in sorted(q_dir.iterdir()):
                                if not fpath.is_file():
                                    continue
                                shutil.copy2(fpath, q_asset_dir / fpath.name)
                                manifest["sources"].append({
                                    "path": fpath.relative_to(SUBJECT).as_posix(),
                                    "sha256": sha256(fpath),
                                })

                                if fpath.name == "question_printable.png":
                                    printable_img_url = f"/data/assets/{question_id}/{fpath.name}"
                                elif fpath.name == "question_compact.png":
                                    compact_img_url = f"/data/assets/{question_id}/{fpath.name}"
                                elif fpath.name == "markscheme.png":
                                    markscheme_img_url = f"/data/assets/{question_id}/{fpath.name}"
                                elif fpath.name.startswith("figure_") and fpath.suffix.lower() == ".png":
                                    fig_stem = fpath.stem
                                    parts_fig = fig_stem.replace("figure_", "").split("_")
                                    fig_label = f"Figure {'.'.join(parts_fig)}" if len(parts_fig) >= 2 else fig_stem
                                    figures.append({
                                        "id": fig_stem,
                                        "label": fig_label,
                                        "url": f"/data/assets/{question_id}/{fpath.name}",
                                    })

                            ms_json_file = q_dir / "markscheme.json"
                            reviewed_ms = q_dir / "markscheme_reviewed.json"
                            reviewed_meta = q_dir / "markscheme_review_meta.json"
                            if reviewed_ms.is_file() and reviewed_meta.is_file():
                                try:
                                    meta = json.loads(reviewed_meta.read_text(encoding="utf-8"))
                                    if (
                                        meta.get("status") == "PASS"
                                        and meta.get("review_kind") == "publisher_erratum_reconciliation"
                                        and meta.get("official_source_locked") is True
                                    ):
                                        ms_json_file = reviewed_ms
                                except (OSError, json.JSONDecodeError):
                                    pass
                            ms_obj = None
                            q_marks = None
                            ms_parts_map = {}
                            if ms_json_file.is_file():
                                try:
                                    with open(ms_json_file, encoding="utf-8") as f_ms:
                                        ms_obj = json.load(f_ms)
                                    q_marks = ms_obj.get("total_marks")
                                    for p in ms_obj.get("parts", []):
                                        lbl = p.get("label", "")
                                        pid = p.get("id") or p.get("part_id")
                                        if lbl:
                                            ms_parts_map[lbl] = p
                                        if pid:
                                            ms_parts_map[pid] = p
                                except Exception:
                                    pass

                            enr_json_file = q_dir / "enrichment.json"
                            enr_obj = None
                            enr_parts_map = {}
                            if enr_json_file.is_file():
                                try:
                                    with open(enr_json_file, encoding="utf-8") as f_enr:
                                        enr_obj = json.load(f_enr)
                                    if enr_obj and "parts" in enr_obj:
                                        for p in enr_obj.get("parts", []):
                                            if isinstance(p, dict):
                                                pid = p.get("part_id") or p.get("id")
                                                lbl = p.get("label")
                                                if pid:
                                                    enr_parts_map[pid] = p
                                                if lbl:
                                                    enr_parts_map[lbl] = p
                                except Exception:
                                    pass

                            ocr_json_file = q_dir / "question_ocr.json"
                            ocr_obj = None
                            if ocr_json_file.is_file():
                                try:
                                    with open(ocr_json_file, encoding="utf-8") as f_ocr:
                                        ocr_obj = json.load(f_ocr)
                                except Exception:
                                    pass

                            q_text = ""
                            for txt_candidate in [q_dir / "question.txt", q_dir / f"question_{num:02d}.txt"]:
                                if txt_candidate.is_file():
                                    try:
                                        q_text = txt_candidate.read_text(encoding="utf-8").strip()
                                        break
                                    except Exception:
                                        pass

                            q_parts = []
                            if ocr_obj and ocr_obj.get("parts"):
                                for op in ocr_obj.get("parts", []):
                                    lbl = op.get("label", "")
                                    pid = op.get("id") or f"{question_id}_{lbl.replace('(', '').replace(')', '').replace(' ', '_')}"
                                    ms_p = ms_parts_map.get(lbl) or ms_parts_map.get(pid)
                                    part_enr = enr_parts_map.get(pid) or enr_parts_map.get(lbl)

                                    p_marks = op.get("marks")
                                    if p_marks is None and ms_p:
                                        p_marks = ms_p.get("marks")

                                    p_stem = op.get("part_stem")
                                    p_text = op.get("text", "")
                                    part_figs = match_figures_for_text(f"{p_stem or ''} {p_text}", figures)

                                    q_parts.append({
                                        "id": pid,
                                        "label": lbl,
                                        "part_stem": p_stem,
                                        "text": p_text,
                                        "marks": p_marks,
                                        "answer_prompt": op.get("answer_prompt"),
                                        "unit": op.get("unit"),
                                        "dependencies": [],
                                        "figureIds": [f["id"] for f in part_figs],
                                        "figures": part_figs,
                                        "markscheme_points": ms_p.get("marking_points", []) if ms_p else [],
                                        "hints": part_enr.get("hints", []) if part_enr else [],
                                        "proper_answer": part_enr.get("proper_answer") if part_enr else None,
                                        "walkthrough": part_enr.get("walkthrough", []) if part_enr else [],
                                        "enrichment": part_enr,
                                        "markscheme": ms_p,
                                    })
                            else:
                                if ms_obj and ms_obj.get("parts"):
                                    part_labels = [p.get("label", "") for p in ms_obj.get("parts", []) if p.get("label")]
                                    part_texts = extract_subpart_texts(q_text, part_labels)
                                    for p in ms_obj.get("parts", []):
                                        pid = p.get("id") or p.get("part_id")
                                        lbl = p.get("label", "")
                                        part_enr = enr_parts_map.get(pid) or enr_parts_map.get(lbl)
                                        p_txt = part_texts.get(lbl, "")
                                        part_figs = match_figures_for_text(p_txt, figures)
                                        q_parts.append({
                                            "id": pid,
                                            "label": lbl,
                                            "part_stem": None,
                                            "text": p_txt,
                                            "marks": p.get("marks"),
                                            "answer_prompt": None,
                                            "unit": None,
                                            "dependencies": [],
                                            "figureIds": [f["id"] for f in part_figs],
                                            "figures": part_figs,
                                            "markscheme_points": p.get("marking_points", []),
                                            "hints": part_enr.get("hints", []) if part_enr else [],
                                            "proper_answer": part_enr.get("proper_answer") if part_enr else None,
                                            "walkthrough": part_enr.get("walkthrough", []) if part_enr else [],
                                            "enrichment": part_enr,
                                            "markscheme": p,
                                        })

                            if ocr_obj and "question_stem" in ocr_obj:
                                display_stem = ocr_obj.get("question_stem") or ""
                            elif not q_parts and q_text:
                                display_stem = q_text
                            else:
                                display_stem = ""
                            stem_figures = match_figures_for_text(display_stem, figures)

                            payload = {
                                "id": question_id,
                                "component": component.upper(),
                                "paperCode": paper_code,
                                "number": num,
                                "year": year_val,
                                "session": session_label,
                                "variant": variant_num,
                                "title": f"Question {num}",
                                "stem": display_stem,
                                "marks": q_marks or sum(p.get("marks") or 0 for p in q_parts),
                                "parts": q_parts,
                                "figures": figures,
                                "stemFigures": stem_figures,
                                "questionPrintableImage": printable_img_url,
                                "questionCompactImage": compact_img_url,
                                "questionImage": printable_img_url or compact_img_url,
                                "markschemeImage": markscheme_img_url,
                                "isMcq": False,
                                "enrichment": enr_obj,
                                "markscheme": ms_obj,
                                "questionOcr": ocr_obj,
                                "issues": [],
                                "sourcePath": q_dir.relative_to(SUBJECT).as_posix(),
                            }

                            (DATA / "questions" / f"{question_id}.json").write_text(
                                json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n",
                                encoding="utf-8",
                            )

                            questions.append({"id": question_id, "number": num, "issues": 0})
                            index["questionCount"] += 1

                        if questions:
                            papers.append({
                                "id": paper_code,
                                "paper_code": paper_code,
                                "year": year_val,
                                "session": session_label,
                                "variant": variant_num,
                                "questions": questions,
                            })
                        continue

                    # Determine question directory
                    q_dir = None
                    for candidate in ("question-package", "questions", "parsed-questions"):
                        target_cand = paper_dir / candidate
                        if target_cand.is_dir() and any(target_cand.glob("question_*.json")):
                            q_dir = target_cand
                            break

                    if not q_dir:
                        continue

                    questions = []
                    for question_path in sorted(q_dir.glob("question_*.json")):
                        question, issues = read(question_path)
                        if not question:
                            if component != "p1":
                                continue
                            number = int(question_path.stem.rsplit("_", 1)[-1])
                            text_path = question_path.with_suffix(".txt")
                            image_path = question_path.with_suffix(".png")
                            answer_key, answer_key_issues = read(q_dir / "answer_key.json")
                            issues.extend(answer_key_issues)
                            question = {
                                "question_id": f"{paper_code}_q{number:02d}",
                                "paper_code": paper_code,
                                "question_num": number,
                                "year": year_val,
                                "session": session_label,
                                "variant": variant_num,
                                "question_text": text_path.read_text(encoding="utf-8") if text_path.is_file() else "",
                                "question_image": image_path.name if image_path.is_file() else "",
                                "answer_type": "multiple-choice",
                                "options": ["A", "B", "C", "D"],
                                "correct_answer": answer_key.get("answers", {}).get(str(number), ""),
                                "marks": 1,
                            }

                        number = int(question.get("question_num") or question_path.stem.rsplit("_", 1)[-1])
                        question_id = question.get("question_id") or f"{paper_dir.name}_q{number:02d}"

                        # Locate mark scheme & enrichment
                        mark_path = paper_dir / "mark-schemes" / f"markscheme_{number:02d}.json"
                        enrichment_path = paper_dir / "enrichment" / f"{question_id}.enrichment.json"

                        markscheme, mark_issues = read(mark_path) if mark_path.is_file() else ({}, [])
                        enrichment, enrichment_issues = read(enrichment_path) if enrichment_path.is_file() else ({}, [])

                        # Missing mark schemes are expected for P1, but notable for P2/P4
                        if component != "p1" and not mark_path.is_file():
                            issues.append("Missing mark scheme")
                        if not enrichment_path.is_file():
                            issues.append("Missing enrichment")

                        issues.extend(mark_issues + enrichment_issues)
                        if markscheme and markscheme.get("question_id") not in (None, question_id):
                            issues.append("Mark-scheme question ID mismatch")
                        if enrichment and enrichment.get("question_id") not in (None, question_id):
                            issues.append("Enrichment question ID mismatch")

                        figures = []
                        asset_dir = DATA / "assets" / question_id
                        q_parts_raw = question.get("parts", [])

                        # Handle figures in question metadata
                        for figure in question.get("figures", []):
                            if isinstance(figure, str):
                                fig_file = figure
                                fig_id = figure
                                fig_label = figure
                                fig_dict = {"id": fig_id, "label": fig_label, "file": fig_file}
                            elif isinstance(figure, dict):
                                fig_file = figure.get("file", "")
                                fig_id = figure.get("id", "unnamed")
                                fig_label = figure.get("label", "")
                                fig_dict = figure
                            else:
                                continue
                            source = (question_path.parent / fig_file).resolve()
                            if not source.is_file():
                                issues.append(f"Missing figure: {fig_file or fig_id}")
                                continue
                            asset_dir.mkdir(parents=True, exist_ok=True)
                            target = asset_dir / source.name
                            shutil.copy2(source, target)

                            # Determine figure target placement (part or stem)
                            pl = fig_dict.get("placement", {})
                            scope = pl.get("scope")
                            part_id = pl.get("part_id") or fig_dict.get("introduced_by")
                            if not part_id and fig_dict.get("referenced_by"):
                                part_id = fig_dict["referenced_by"][0]
                            if not part_id:
                                for p in q_parts_raw:
                                    if fig_id in p.get("figure_ids", []):
                                        part_id = p.get("id")
                                        break

                            target_scope = "question" if (scope == "question" and not part_id) else (part_id or "question")

                            figures.append({
                                **fig_dict,
                                "url": f"/data/assets/{question_id}/{target.name}",
                                "targetPartId": target_scope,
                            })

                        # Special handling for P1 MCQ
                        is_mcq = component == "p1" or question.get("answer_type") == "multiple-choice"
                        q_image = None
                        if question.get("question_image"):
                            q_img_path = (question_path.parent / question.get("question_image", "")).resolve()
                            if q_img_path.is_file():
                                asset_dir.mkdir(parents=True, exist_ok=True)
                                target = asset_dir / q_img_path.name
                                shutil.copy2(q_img_path, target)
                                q_image = f"/data/assets/{question_id}/{target.name}"

                        # Normalize parts
                        enrichment_parts = {part.get("part_id"): part for part in enrichment.get("parts", [])}
                        mark_parts = {part.get("id"): part for part in markscheme.get("parts", [])}
                        parts = []

                        if is_mcq:
                            # Single MCQ part
                            mcq_part_id = f"{question_id}_mcq"
                            parts.append({
                                "id": mcq_part_id,
                                "label": "",
                                "text": question.get("question_text", ""),
                                "marks": question.get("marks", 1),
                                "dependencies": [],
                                "figureIds": [],
                                "figures": [],
                                "enrichment": {
                                    "hints": enrichment.get("hints", []),
                                    "walkthrough": enrichment.get("walkthrough", []),
                                    "topic_id": enrichment.get("topic_id"),
                                    "module_id": enrichment.get("module_id"),
                                    "skill_id": enrichment.get("skill_id"),
                                    "accepted_answer": enrichment.get("accepted_answer") or question.get("correct_answer"),
                                },
                                "markscheme": {
                                    "answer": question.get("correct_answer", ""),
                                    "official": f"Correct option: {question.get('correct_answer', '')}",
                                },
                            })
                        else:
                            for part in q_parts_raw:
                                part_id = part.get("id", "")
                                part_enr = enrichment_parts.get(part_id, {})
                                part_ms = mark_parts.get(part_id, {})

                                # Resolve knowledge refs (definitions & formulas)
                                krefs = part_enr.get("knowledge_refs", {})
                                resolved_definitions = [
                                    definitions_kb[did]
                                    for did in krefs.get("definition_ids", [])
                                    if did in definitions_kb
                                ]
                                resolved_formulas = [
                                    formulas_kb[fid]
                                    for fid in krefs.get("formula_ids", [])
                                    if fid in formulas_kb
                                ]

                                # Filter figures that belong to this part
                                part_figures = [f for f in figures if f.get("targetPartId") == part_id]

                                parts.append({
                                    "id": part_id,
                                    "label": part.get("label", ""),
                                    "text": part.get("question_text_latex") or part.get("question_text", ""),
                                    "marks": part.get("marks"),
                                    "dependencies": part.get("dependencies", []),
                                    "figureIds": part.get("figure_ids", []),
                                    "figures": part_figures,
                                    "enrichment": {
                                        **part_enr,
                                        "resolved_definitions": resolved_definitions,
                                        "resolved_formulas": resolved_formulas,
                                    },
                                    "markscheme": part_ms,
                                })

                        # Filter stem figures (targetPartId == "question")
                        stem_figures = [f for f in figures if f.get("targetPartId") == "question"]

                        # Title determination
                        topic_name = ""
                        topic_id = enrichment.get("topic_id")
                        if not topic_id and enrichment.get("mapping", {}).get("topic_ids"):
                            topic_id = enrichment["mapping"]["topic_ids"][0]
                        if not topic_id and parts and parts[0].get("enrichment", {}).get("mapping", {}).get("primary_topic_id"):
                            topic_id = parts[0]["enrichment"]["mapping"]["primary_topic_id"]

                        if topic_id and topic_id in taxonomy:
                            topic_name = taxonomy[topic_id]["name"]
                        else:
                            topic_name = f"Physics {component.upper()}"

                        paper_code = question.get("paper_code") or paper_dir.name
                        year_val = question.get("year", int(year_dir.name))
                        session_val = question.get("session", season_dir.name.replace("-", " ").title())
                        variant_val = question.get("variant", paper_dir.name.replace("variant-", ""))

                        payload = {
                            "id": question_id,
                            "component": component.upper(),
                            "paperCode": paper_code,
                            "number": number,
                            "year": year_val,
                            "session": session_val,
                            "variant": variant_val,
                            "title": topic_name,
                            "stem": question.get("question_stem_latex") or question.get("question_stem", ""),
                            "marks": question.get("total_marks") or question.get("marks", sum(p.get("marks") or 0 for p in parts)),
                            "parts": parts,
                            "figures": figures,
                            "stemFigures": stem_figures,
                            "questionImage": q_image,
                            "isMcq": is_mcq,
                            "options": question.get("options", []),
                            "correctAnswer": question.get("correct_answer", ""),
                            "enrichment": enrichment,
                            "markscheme": markscheme,
                            "issues": issues,
                            "sourcePath": question_path.relative_to(SUBJECT).as_posix(),
                        }

                        (DATA / "questions" / f"{question_id}.json").write_text(
                            json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8"
                        )

                        for source in (question_path, mark_path, enrichment_path):
                            if source.is_file():
                                manifest["sources"].append({
                                    "path": source.relative_to(SUBJECT).as_posix(),
                                    "sha256": sha256(source)
                                })

                        questions.append({"id": question_id, "number": number, "issues": len(issues)})
                        index["questionCount"] += 1
                        index["issueCount"] += len(issues)

                    if questions:
                        papers.append({
                            "id": paper_code,
                            "year": year_val,
                            "session": session_val,
                            "variant": variant_val,
                            "questions": questions,
                        })

        index["components"].append({
            "id": component,
            "name": f"Physics {component.upper()}",
            "papers": papers,
        })

    (DATA / "index.json").write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    (PROTOTYPE / "source-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Built {index['questionCount']} Physics questions across components with {index['issueCount']} notices.")


if __name__ == "__main__":
    main()
