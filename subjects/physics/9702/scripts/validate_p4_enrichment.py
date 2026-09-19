#!/usr/bin/env python3
"""
validate_p4_enrichment.py

Comprehensive deterministic and semantic validator for Physics 9702 P4 Structured Theory enrichment.
Checks schema, part hierarchy, mark-scheme criteria parity, taxonomy, skills, definitions, formulas,
LaTeX integrity, and hint/walkthrough quality.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

KB = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[4]

BANNED_PHRASES = [
    "todo",
    "placeholder",
    "relevant progressive hint",
    "as described above",
    "as shown above",
    "tbd",
    "insert hint here",
    "insert walkthrough here",
    "the answer is",
]

def load_registries():
    # AS and A2 taxonomies
    tax_as_file = KB / "knowledge/2025-2027/as/9702-2025-2027-as-taxonomy.json"
    tax_a2_file = KB / "knowledge/2025-2027/a2/9702-2025-2027-a2-taxonomy.json"
    
    topics = {}
    modules_to_topic = {}
    
    for tf in (tax_as_file, tax_a2_file):
        if tf.exists():
            tax = json.loads(tf.read_text(encoding="utf-8"))
            for t in tax.get("topics", []):
                tid = t["topic_id"]
                topics[tid] = t["topic_name"]
                for m in t.get("modules", []):
                    mid = m["module_id"]
                    modules_to_topic[mid] = tid

    # AS and A2 learning outcomes
    out_as_file = KB / "knowledge/2025-2027/as/9702-2025-2027-as-learning-outcomes.json"
    out_a2_file = KB / "knowledge/2025-2027/a2/9702-2025-2027-a2-learning-outcomes.json"
    outcome_to_module = {}
    outcome_to_topic = {}
    for of in (out_as_file, out_a2_file):
        if of.exists():
            odata = json.loads(of.read_text(encoding="utf-8"))
            for o in odata.get("outcomes", []):
                outcome_to_module[o["outcome_id"]] = o["module_id"]
                outcome_to_topic[o["outcome_id"]] = o["topic_id"]

    kb_base = KB / "knowledge/knowledge-base" if (KB / "knowledge/knowledge-base").exists() else KB / "knowledge"
    skills_file = kb_base / "skills.json"
    skills_data = json.loads(skills_file.read_text(encoding="utf-8"))
    skills = {s["skill_id"]: s for s in skills_data.get("skills", [])}

    patterns_file = kb_base / "question-patterns.json"
    patterns_data = json.loads(patterns_file.read_text(encoding="utf-8"))
    patterns = {p["pattern_id"] for p in patterns_data.get("patterns", [])}

    defs_file = kb_base / "definitions.json"
    defs_data = json.loads(defs_file.read_text(encoding="utf-8"))
    definitions = {d["definition_id"]: d for d in defs_data.get("definitions", [])}

    forms_file = kb_base / "formulas.json"
    forms_data = json.loads(forms_file.read_text(encoding="utf-8"))
    formulas = {f["formula_id"]: f for f in forms_data.get("formulas", [])}

    schema_file = kb_base / "contracts/question-enrichment.schema.json"
    schema = json.loads(schema_file.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)

    return {
        "topics": topics,
        "modules_to_topic": modules_to_topic,
        "outcome_to_module": outcome_to_module,
        "outcome_to_topic": outcome_to_topic,
        "skills": skills,
        "patterns": patterns,
        "definitions": definitions,
        "formulas": formulas,
        "validator": validator
    }

def validate_single_question(enrich_data, q_data, ms_data, registries):
    errors = []
    semantic_reviews = []

    # 1. Schema check
    schema_errs = list(registries["validator"].iter_errors(enrich_data))
    if schema_errs:
        for err in schema_errs:
            errors.append(f"Schema error: {err.message} at {'/'.join(str(p) for p in err.path)}")
        return errors, semantic_reviews

    qid = enrich_data["question_id"]
    if enrich_data.get("component") != "P4":
        errors.append(f"Component mismatch: expected 'P4', found '{enrich_data.get('component')}'")

    if "numerical_values_checked" not in enrich_data:
        errors.append("Missing required field 'numerical_values_checked' in enrichment record")

    # 2. Identity match
    if q_data and q_data.get("question_id") != qid:
        errors.append(f"Identity mismatch: enrichment question_id '{qid}' != question '{q_data.get('question_id')}'")

    # 3. Whole-question mapping check
    q_map = enrich_data.get("mapping", {})
    root_topics = set(q_map.get("topic_ids", []))
    root_modules = set(q_map.get("module_ids", []))
    root_outcomes = set(q_map.get("outcome_ids", []))

    for tid in root_topics:
        if tid not in registries["topics"]:
            errors.append(f"Invalid question topic_id '{tid}' not found in AS/A2 taxonomy")
    for mid in root_modules:
        if mid not in registries["modules_to_topic"]:
            errors.append(f"Invalid question module_id '{mid}' not found in AS/A2 taxonomy")

    # 4. Question patterns check
    root_patterns = set(enrich_data.get("question_patterns", []))
    for pat in root_patterns:
        if pat not in registries["patterns"]:
            errors.append(f"Invalid question pattern '{pat}' in question header")

    # 5. Parts validation
    parts = enrich_data.get("parts", [])
    if not parts:
        errors.append("No parts defined in question enrichment")

    leaf_topics = set()
    leaf_modules = set()
    leaf_outcomes = set()
    leaf_patterns = set()
    leaf_criteria = set()

    ms_points = {}
    if ms_data:
        for ms_part in ms_data.get("parts", []):
            for mp in ms_part.get("marking_points", []):
                ms_points[mp["id"]] = mp

    for part_idx, p in enumerate(parts):
        pid = p.get("part_id", f"part_{part_idx}")
        pmap = p.get("mapping", {})
        ptid = pmap.get("primary_topic_id")
        pmid = pmap.get("primary_module_id")

        if ptid:
            leaf_topics.add(ptid)
        if pmid:
            leaf_modules.add(pmid)

        part_topic_set = {ptid} if ptid else set()

        for pat in p.get("question_patterns", []):
            leaf_patterns.add(pat)

        for oid in pmap.get("outcome_ids", []):
            leaf_outcomes.add(oid)
            if oid in registries["outcome_to_topic"]:
                leaf_topics.add(registries["outcome_to_topic"][oid])
                part_topic_set.add(registries["outcome_to_topic"][oid])
            if oid in registries["outcome_to_module"]:
                leaf_modules.add(registries["outcome_to_module"][oid])

        for secondary in pmap.get("direct_secondary_mappings", []):
            secondary_module = secondary.get("module_id")
            if secondary_module:
                leaf_modules.add(secondary_module)
            if registries["modules_to_topic"].get(secondary_module) != ptid:
                errors.append(f"{pid}: Secondary module '{secondary_module}' does not belong to primary topic '{ptid}'")
            for oid in secondary.get("outcome_ids", []):
                leaf_outcomes.add(oid)
                if registries["outcome_to_module"].get(oid) != secondary_module:
                    errors.append(f"{pid}: Secondary outcome '{oid}' does not belong to module '{secondary_module}'")

        # Topic & Module
        if ptid and ptid not in registries["topics"]:
            errors.append(f"{pid}: Invalid primary_topic_id '{ptid}'")
        if pmid and pmid not in registries["modules_to_topic"]:
            errors.append(f"{pid}: Invalid primary_module_id '{pmid}'")
        elif ptid and pmid and registries["modules_to_topic"].get(pmid) != ptid:
            errors.append(f"{pid}: Module '{pmid}' belongs to topic '{registries['modules_to_topic'].get(pmid)}', not '{ptid}'")

        # Skills
        sk = p.get("skills", {})
        pskill = sk.get("primary_skill_id")
        if pskill:
            if pskill not in registries["skills"]:
                errors.append(f"{pid}: Invalid primary_skill_id '{pskill}' not found in skills.json")
            else:
                sk_obj = registries["skills"][pskill]
                sk_topics = set(sk_obj.get("topic_ids", []))
                if sk_topics and not (sk_topics & part_topic_set):
                    errors.append(f"{pid}: Skill '{pskill}' topic {sk_topics} not compatible with part topics {part_topic_set}")

        for ssk in sk.get("supporting_skill_ids", []):
            if ssk not in registries["skills"]:
                errors.append(f"{pid}: Invalid supporting_skill_id '{ssk}' not found in skills.json")
            else:
                sk_obj = registries["skills"][ssk]
                sk_topics = set(sk_obj.get("topic_ids", []))
                if sk_topics and not (sk_topics & (part_topic_set | root_topics)):
                    errors.append(f"{pid}: Supporting skill '{ssk}' topic {sk_topics} not compatible with part topics {part_topic_set}")

        # Knowledge Refs
        krefs = p.get("knowledge_refs", {})
        for did in krefs.get("definition_ids", []):
            if did not in registries["definitions"]:
                errors.append(f"{pid}: Invalid definition_id '{did}' not found in definitions.json")
        for fid in krefs.get("formula_ids", []):
            if fid not in registries["formulas"]:
                errors.append(f"{pid}: Invalid formula_id '{fid}' not found in formulas.json")

        # Hints
        hints = p.get("hints", [])
        if len(hints) < 2:
            errors.append(f"{pid}: Expected >= 2 progressive hints, found {len(hints)}")
        for i, h in enumerate(hints):
            if len(h.strip()) < 10:
                errors.append(f"{pid}: Hint {i+1} too short (<10 chars)")
            for bp in BANNED_PHRASES:
                if bp in h.lower():
                    errors.append(f"{pid}: Hint {i+1} contains banned phrase '{bp}'")

        # Walkthrough
        wt = p.get("walkthrough", [])
        if len(wt) < 2:
            errors.append(f"{pid}: Expected >= 2 walkthrough steps, found {len(wt)}")
        for i, w in enumerate(wt):
            if len(w.strip()) < 10:
                errors.append(f"{pid}: Walkthrough step {i+1} too short (<10 chars)")
            for bp in BANNED_PHRASES:
                if bp in w.lower():
                    errors.append(f"{pid}: Walkthrough step {i+1} contains banned phrase '{bp}'")

        # Checking & Rubric
        chk = p.get("checking", {})
        rubric = chk.get("ai_rubric", [])
        for r_idx, item in enumerate(rubric):
            cid = item.get("criterion_id")
            leaf_criteria.add(cid)
            for alt in item.get("alternative_criterion_ids", []):
                leaf_criteria.add(alt)
            obs = item.get("observable", "")
            if not obs or len(obs.strip()) < 10:
                errors.append(f"{pid}: Criterion {cid} observable is too short or empty")
            if ms_points and cid not in ms_points:
                errors.append(f"{pid}: criterion_id '{cid}' not found in official mark scheme")

        # Text and LaTeX sanity
        full_text = " ".join(hints) + " " + " ".join(wt) + " " + " ".join(r.get("observable", "") for r in rubric)
        if chr(65533) in full_text:
            errors.append(f"{pid}: Corrupt unicode character detected")
        dollar_count = full_text.count("$")
        if dollar_count % 2 != 0:
            errors.append(f"{pid}: Unbalanced LaTeX math delimiters '$' ({dollar_count} dollar signs)")
        pid_artifacts = re.findall(r"\$\{[A-Za-z0-9_]+\}", full_text)
        if pid_artifacts:
            errors.append(f"{pid}: Detected unexpanded template variable: {pid_artifacts}")

    # 6. Complete 100% Mark-Scheme Coverage
    if ms_points:
        missing_from_rubric = set(ms_points.keys()) - leaf_criteria
        if missing_from_rubric:
            errors.append(f"Incomplete mark scheme coverage: {len(missing_from_rubric)} marking points missing from rubric: {sorted(missing_from_rubric)}")

    # 7. Exact Root vs Leaf Union Parity
    if root_topics != leaf_topics:
        diff_missing = leaf_topics - root_topics
        diff_extra = root_topics - leaf_topics
        if diff_missing:
            errors.append(f"Root mapping.topic_ids is missing leaf topics: {sorted(diff_missing)}")
        if diff_extra:
            errors.append(f"Root mapping.topic_ids contains unused topics: {sorted(diff_extra)}")

    if root_modules != leaf_modules:
        diff_missing = leaf_modules - root_modules
        diff_extra = root_modules - leaf_modules
        if diff_missing:
            errors.append(f"Root mapping.module_ids is missing leaf modules: {sorted(diff_missing)}")
        if diff_extra:
            errors.append(f"Root mapping.module_ids contains unused modules: {sorted(diff_extra)}")

    if root_outcomes != leaf_outcomes:
        diff_missing = leaf_outcomes - root_outcomes
        diff_extra = root_outcomes - leaf_outcomes
        if diff_missing:
            errors.append(f"Root mapping.outcome_ids is missing leaf outcome_ids: {sorted(diff_missing)}")
        if diff_extra:
            errors.append(f"Root mapping.outcome_ids contains unused outcome_ids: {sorted(diff_extra)}")

    if root_patterns != leaf_patterns:
        diff_missing = leaf_patterns - root_patterns
        diff_extra = root_patterns - leaf_patterns
        if diff_missing:
            errors.append(f"Root question_patterns is missing leaf patterns: {sorted(diff_missing)}")
        if diff_extra:
            errors.append(f"Root question_patterns contains unused patterns: {sorted(diff_extra)}")

    return errors, semantic_reviews

def validate_paper(paper_code, registries):
    clean_code = paper_code.replace("_qp_", "_").replace("_ms_", "_")
    code_parts = clean_code.split("_")
    if len(code_parts) == 3:
        qp_folder = f"{code_parts[0]}_{code_parts[1]}_qp_{code_parts[2]}"
        ms_folder = f"{code_parts[0]}_{code_parts[1]}_ms_{code_parts[2]}"
        sessions = {"m": "february-march", "s": "may-june", "w": "october-november"}
        session_char = code_parts[1][0]
        year = f"20{code_parts[1][1:]}"
        session = sessions.get(session_char, "may-june")
        v_digit = code_parts[2][1] if len(code_parts[2]) == 2 else code_parts[2]
        variant_dir = f"variant-{v_digit}"

        structured_qp = KB / "past papers/p4" / year / session / variant_dir / "parsed-questions"
        legacy_qp = ROOT / f"subjects/physics/9702/papers/p4/parsed-questions/{qp_folder}"
        q_dir = structured_qp if structured_qp.exists() else legacy_qp

        structured_ms = KB / "past papers/p4" / year / session / variant_dir / "mark-schemes"
        legacy_ms = ROOT / f"subjects/physics/9702/papers/p4/mark-schemes/{ms_folder}"
        ms_dir = structured_ms if structured_ms.exists() else legacy_ms

        structured_enrich = KB / "past papers/p4" / year / session / variant_dir / "enrichment"
        legacy_enrich = KB / "enrichment/p4"
        p_enrich_dir = structured_enrich if structured_enrich.exists() else legacy_enrich
    else:
        qp_folder = clean_code
        ms_folder = clean_code
        q_dir = ROOT / f"subjects/physics/9702/papers/p4/parsed-questions/{qp_folder}"
        ms_dir = ROOT / f"subjects/physics/9702/papers/p4/mark-schemes/{ms_folder}"
        p_enrich_dir = KB / "enrichment/p4"

    report = {
        "paper_code": clean_code,
        "question_count": 0,
        "valid_questions": 0,
        "deterministic_errors": [],
        "semantic_review_items": [],
        "status": "FAIL"
    }

    if not q_dir.exists():
        report["deterministic_errors"].append(f"Question directory not found: {q_dir}")
        return report
    if not ms_dir.exists():
        report["deterministic_errors"].append(f"Mark scheme directory not found: {ms_dir}")
        return report

    # Check hash baseline if available
    hashes_file = KB / f"hashes/p4/{ms_folder}.sha256.json"
    if hashes_file.exists():
        hash_manifest = json.loads(hashes_file.read_text(encoding="utf-8"))
        import hashlib
        for ms_fname, expected_hash in hash_manifest.items():
            ms_fpath = ms_dir / ms_fname
            if not ms_fpath.exists():
                report["deterministic_errors"].append(f"Mark scheme file {ms_fname} missing against hash baseline")
            else:
                actual_hash = hashlib.sha256(ms_fpath.read_bytes()).hexdigest()
                if actual_hash != expected_hash:
                    report["deterministic_errors"].append(f"Mark scheme {ms_fname} hash mismatch: {actual_hash} != {expected_hash} (source mutated!)")

    enrich_files = sorted(p_enrich_dir.glob(f"{clean_code}_q*.enrichment.json"))
    if not enrich_files:
        report["deterministic_errors"].append(f"No P4 enrichment files found for paper {clean_code} in {p_enrich_dir}")
        return report

    for ef in enrich_files:
        report["question_count"] += 1
        qnum = ef.stem.split("_q")[-1].replace(".enrichment", "")
        
        q_file = q_dir / f"question_{qnum}.json"
        ms_file = ms_dir / f"markscheme_{qnum}.json"

        if not q_file.exists():
            report["deterministic_errors"].append(f"{ef.name}: Question file not found: {q_file}")
            continue
        if not ms_file.exists():
            report["deterministic_errors"].append(f"{ef.name}: Mark scheme file not found: {ms_file}")
            continue

        e_data = json.loads(ef.read_text(encoding="utf-8"))
        q_data = json.loads(q_file.read_text(encoding="utf-8"))
        ms_data = json.loads(ms_file.read_text(encoding="utf-8"))

        errors, reviews = validate_single_question(e_data, q_data, ms_data, registries)
        if errors:
            for err in errors:
                report["deterministic_errors"].append(f"{ef.name}: {err}")
        else:
            report["valid_questions"] += 1

        if reviews:
            for rev in reviews:
                report["semantic_review_items"].append(f"{ef.name}: {rev}")

    if not report["deterministic_errors"] and report["question_count"] > 0:
        report["status"] = "PASS"

    return report

def main():
    parser = argparse.ArgumentParser(description="Validate Physics 9702 P4 Structured Question enrichment records.")
    parser.add_argument("--enrichment", type=Path, help="Path to single P4 enrichment JSON file")
    parser.add_argument("--question", type=Path, help="Path to matching question JSON file")
    parser.add_argument("--markscheme", type=Path, help="Path to matching markscheme JSON file")
    parser.add_argument("--paper", type=str, help="Paper code to validate (e.g. 9702_s22_42)")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON report")
    args = parser.parse_args()

    registries = load_registries()

    if args.enrichment:
        if not args.enrichment.exists():
            print(f"File not found: {args.enrichment}")
            sys.exit(1)
        e_data = json.loads(args.enrichment.read_text(encoding="utf-8"))
        q_data = json.loads(args.question.read_text(encoding="utf-8")) if args.question and args.question.exists() else None
        ms_data = json.loads(args.markscheme.read_text(encoding="utf-8")) if args.markscheme and args.markscheme.exists() else None

        errors, reviews = validate_single_question(e_data, q_data, ms_data, registries)
        if args.json:
            result = {
                "enrichment": str(args.enrichment),
                "errors": errors,
                "reviews": reviews,
                "status": "PASS" if not errors else "FAIL"
            }
            print(json.dumps(result, indent=2))
        else:
            if errors:
                for err in errors:
                    print(f"FAIL: {err}")
                sys.exit(1)
            else:
                print("PASS")
        sys.exit(0 if not errors else 1)

    if args.paper:
        report = validate_paper(args.paper, registries)
        if args.json:
            print(json.dumps(report, indent=2))
        else:
            if report["status"] == "PASS":
                print(f"PASS: {report['paper_code']} ({report['valid_questions']}/{report['question_count']} questions valid)")
            else:
                print(f"FAIL: {report['paper_code']}")
                for err in report["deterministic_errors"]:
                    print(f"  - {err}")
        sys.exit(0 if report["status"] == "PASS" else 1)

    parser.print_help()

if __name__ == "__main__":
    main()
