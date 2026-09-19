#!/usr/bin/env python3
"""Comprehensive Question Typology and N-Gram Mining Engine for Cambridge Physics (9702).

Analyzes the complete 2016-2025 past paper archive (Paper 1 MCQ, Paper 2 AS Theory, Paper 4 A2 Theory)
to extract authentic Cambridge question archetypes, syntactic command n-grams, and mark scheme reward chains.

Outputs:
1. Master Reference in Knowledge Base:
   subjects/physics/9702/knowledge/2025-2027/question-typology-and-testing-patterns.md
2. Machine-readable Dataset:
   subjects/physics/9702/knowledge/2025-2027/question-typology.json
3. Topic-Specific Testing Profiles:
   subjects/physics/9702/study/topics/<topic_id>_<slug>/question-types.md across all 25 topics.

Rule: Strictly ZERO em dashes anywhere in code, markdown, logs, or outputs.
"""

from __future__ import annotations

import collections
import json
import math
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

PHY_ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_ROOT = PHY_ROOT / "knowledge/2025-2027"
PAPERS_ROOT = PHY_ROOT / "past papers"
STUDY_ROOT = PHY_ROOT / "study/topics"

AS_TAX_PATH = KNOWLEDGE_ROOT / "as/9702-2025-2027-as-taxonomy.json"
A2_TAX_PATH = KNOWLEDGE_ROOT / "a2/9702-2025-2027-a2-taxonomy.json"


def sanitize(text: str) -> str:
    """Ensure strictly zero em dashes in any text output."""
    return text.replace(chr(8212), "-").replace("\u2014", "-")


def tokenize(text: str) -> List[str]:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text.split()


STOPWORDS = {
    "the", "a", "an", "and", "or", "in", "on", "of", "to", "for", "with",
    "as", "by", "that", "this", "is", "are", "be", "from", "at", "which",
    "into", "each", "between", "about", "both", "such", "when", "then", "will",
    "what", "how", "following", "one", "two", "three", "four", "part", "subpart"
}

MS_STOPWORDS = STOPWORDS | {
    "eg", "avp", "circ", "text", "correct", "because", "option", "total", "mark",
    "marks", "allow", "ignore", "ora", "accept", "reject", "point", "points",
    "table", "fig", "figure", "question", "answers", "answer", "student", "candidates",
    "candidate", "one", "two", "three", "four", "five", "six", "first", "second",
    "third", "either", "also", "may", "can", "could", "would", "should", "must",
    "not", "does", "do", "did", "due", "per", "via", "only", "shows", "shown",
    "stated", "statement", "given", "give", "ref", "reference", "e", "g", "b", "c", "d",
    "well", "done", "so", "it", "no", "less", "etc", "use", "using", "see", "seen",
    "unit", "units", "ecf", "c1", "a1", "m1", "b1", "times", "frac", "cdot", "sqrt",
    "quad", "qquad", "left", "right", "begin", "end", "pm", "delta", "lambda", "mu",
    "theta", "alpha", "beta", "gamma", "kg", "m", "s", "m2", "m3", "ms", "ms1", "ms2"
}


def clean_prompt_for_prefix(prompt: str) -> str:
    """Clean question numbering, layout boilerplate, and label prefixes from prompts for n-gram extraction."""
    p = prompt.strip()
    for _ in range(5):
        p = re.sub(r"^\s*\d+[\s\.\:\)]+", "", p)
        p = re.sub(r"^\s*[\(\[][a-z0-9ivx]+[\)\]][\s\.\:]*", "", p, flags=re.IGNORECASE)
        p = re.sub(r"^\s*(?:[a-z]|[ivx]+)[\.\)\:][\s]+", "", p, flags=re.IGNORECASE)
    p = re.sub(r"^(?:fig\b\.?|figure|table)\s*[\d\.]+\s*", "figure ", p, flags=re.IGNORECASE)

    # Strip narrative layout boilerplate so n-grams reflect authentic command verbs
    boilerplate_prefixes = [
        r"^the\s+diagram\s+shows\s+",
        r"^a\s+diagram\s+shows\s+",
        r"^figure\s+shows\s+",
        r"^the\s+graph\s+shows\s+",
        r"^a\s+graph\s+of\s+",
        r"^which\s+statement\s+about\s+",
        r"^which\s+statement\s+is\s+",
        r"^which\s+row\s+shows\s+",
        r"^which\s+row\s+correctly\s+",
        r"^in\s+the\s+diagram\s+",
        r"^a\s+student\s+measures\s+",
        r"^a\s+student\s+investigates\s+",
    ]
    for bp in boilerplate_prefixes:
        p = re.sub(bp, "", p, flags=re.IGNORECASE)

    return p.strip()


def get_ngrams(tokens: List[str], n: int) -> List[str]:
    return [" ".join(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]


# The Six Core Cambridge Physics Archetypes
ARCHETYPES = [
    "Quantitative Calculation & Multi-Step Derivation",
    "Graphical Sketching & Trend Interpretation",
    "Physical Mechanism & Field Explanation",
    "Definition, Law & Conservation Principle",
    "Diagrammatic Vector & Circuit Construction",
    "Experimental Uncertainty & Measurement Analysis",
]


def classify_question(prompt: str, proper_ans: str, ms_text: str, comp: str, patterns: List[str]) -> str:
    p_lower = prompt.lower()
    pat_set = set(patterns)

    # 1. Experimental Uncertainty & Measurement Analysis
    if pat_set & {"uncertainty_analysis", "measurement_selection", "physical_quantity_estimation"}:
        return "Experimental Uncertainty & Measurement Analysis"
    unc_keywords = ["uncertainty", "percentage uncertainty", "fractional uncertainty", "absolute uncertainty",
                    "systematic error", "random error", "estimate the order of magnitude", "precision",
                    "resolution", "micrometer", "vernier", "calliper"]
    if any(k in p_lower for k in unc_keywords):
        return "Experimental Uncertainty & Measurement Analysis"

    # 2. Diagrammatic Vector & Circuit Construction
    if pat_set & {"force_diagram_construction", "electric_field_line_construction", "vector_diagram_construction", "circuit_diagram_construction", "motion_path_representation"}:
        return "Diagrammatic Vector & Circuit Construction"
    diag_keywords = ["draw an arrow", "draw arrows", "draw field lines", "draw the circuit", "complete the circuit",
                     "sketch the pattern", "draw a vector diagram", "draw a line to represent", "label the forces",
                     "mark the direction", "arrow to show the direction", "sketch the lines"]
    if any(k in p_lower for k in diag_keywords):
        return "Diagrammatic Vector & Circuit Construction"

    # 3. Graphical Sketching & Trend Interpretation
    if pat_set & {"graph_construction", "graph_interpretation"}:
        return "Graphical Sketching & Trend Interpretation"
    graph_keywords = ["sketch the graph", "sketch on fig", "sketch a graph", "plot a graph", "variation with",
                      "from the graph", "use the graph", "gradient of", "area under", "deduce from fig",
                      "describe the variation"]
    if any(k in p_lower for k in graph_keywords):
        return "Graphical Sketching & Trend Interpretation"

    # 4. Definition, Law & Conservation Principle: Strictly require authentic definition command triggers
    def_keywords = ["define ", "define\n", "state what is meant by", "explain what is meant by", "state the principle of",
                    "state newton", "state coulomb", "state ohm", "state kepler", "state faraday", "state lenz",
                    "law of conservation of", "conservation of linear momentum", "conservation of energy",
                    "state two conditions for", "state the two conditions", "define electric potential",
                    "define gravitational potential", "define simple harmonic", "define work done",
                    "define power", "define density", "define pressure", "define internal energy",
                    "state the first law of thermodynamics", "state boyle", "state the ideal gas law"]
    if any(k in p_lower for k in def_keywords) or (comp == "p1" and "which statement defines" in p_lower):
        return "Definition, Law & Conservation Principle"

    # 5. Quantitative Calculation & Derivation
    if pat_set & {"direct_calculation", "multi_step_calculation", "equation_derivation"}:
        return "Quantitative Calculation & Multi-Step Derivation"
    calc_keywords = ["calculate", "determine", "show that", "derive", "magnitude of", "numerical value",
                     "speed of", "velocity of", "frequency of", "wavelength of", "resistance of",
                     "potential difference", "current in", "energy of", "mass of", "acceleration of",
                     "force on", "power of", "ratio of"]
    if any(k in p_lower for k in calc_keywords):
        return "Quantitative Calculation & Multi-Step Derivation"

    # 6. Physical Mechanism & Field Explanation
    if pat_set & {"explanation", "comparison", "interference_analysis", "particle_model_application"}:
        return "Physical Mechanism & Field Explanation"
    mech_keywords = ["explain why", "explain how", "describe the motion", "explain in terms of",
                     "describe and explain", "suggest why", "give a reason", "account for", "compare the"]
    if any(k in p_lower for k in mech_keywords):
        return "Physical Mechanism & Field Explanation"

    # Default fallback based on calculated/numeric vs conceptual response
    if any(c.isdigit() for c in proper_ans) and comp in ["p2", "p4"]:
        return "Quantitative Calculation & Multi-Step Derivation"
    return "Physical Mechanism & Field Explanation"


def main():
    print("Starting Cambridge Physics (9702) Question Typology & N-Gram Mining Engine...")

    as_tax = json.loads(AS_TAX_PATH.read_text(encoding="utf-8"))
    a2_tax = json.loads(A2_TAX_PATH.read_text(encoding="utf-8"))

    topic_names: Dict[str, str] = {}
    topic_levels: Dict[str, str] = {}
    for top in as_tax["topics"]:
        tid = top["topic_id"]
        topic_names[tid] = top["topic_name"]
        topic_levels[tid] = "AS"
    for top in a2_tax["topics"]:
        tid = top["topic_id"]
        topic_names[tid] = top["topic_name"]
        topic_levels[tid] = "A2"

    corpus_items = []
    topic_items: Dict[str, List[Dict[str, Any]]] = {tid: [] for tid in topic_names}
    comp_items: Dict[str, List[Dict[str, Any]]] = {"p1": [], "p2": [], "p4": []}

    # 1. Ingest Paper 1 (MCQ) items
    print("Ingesting Paper 1 (MCQ) items...")
    for en_file in sorted(PAPERS_ROOT.glob("p1/**/enrichment/*.enrichment.json")):
        try:
            en_data = json.loads(en_file.read_text(encoding="utf-8"))
        except Exception:
            continue

        tid = en_data.get("topic_id") or en_data.get("mapping", {}).get("primary_topic_id")
        if not tid or tid not in topic_names:
            continue

        qid = en_data.get("question_id", en_file.stem.split(".")[0])
        qnum_str = qid.split("_q")[-1] if "_q" in qid else "01"
        try:
            qnum_int = int(qnum_str)
        except ValueError:
            qnum_int = 1

        qp_dir = en_file.parent.parent / "question-package"
        prompt = ""
        q_json = qp_dir / f"question_{qnum_int:02d}.json"
        if not q_json.is_file():
            q_json = qp_dir / f"question_{qnum_int}.json"

        if q_json.is_file() and q_json.stat().st_size > 0:
            try:
                q_data = json.loads(q_json.read_text(encoding="utf-8"))
                prompt = q_data.get("question_text", "")
            except Exception:
                pass

        if not prompt:
            txt_file = qp_dir / f"question_{qnum_int:02d}.txt"
            if not txt_file.is_file():
                txt_file = qp_dir / f"question_{qnum_int}.txt"
            if txt_file.is_file() and txt_file.stat().st_size > 0:
                prompt = txt_file.read_text(encoding="utf-8")

        acc = en_data.get("accepted_answer", "")
        ms_text = en_data.get("options_breakdown", {}).get(acc, {}).get("explanation", "")
        proper_ans = f"Option {acc}"
        pats = en_data.get("question_patterns", [])
        archetype = classify_question(prompt, proper_ans, ms_text, "p1", pats)

        item = {
            "id": qid,
            "component": "p1",
            "topic_id": tid,
            "module_id": en_data.get("module_id") or en_data.get("mapping", {}).get("primary_module_id", ""),
            "outcome_ids": en_data.get("mapping", {}).get("outcome_ids", []),
            "marks": 1,
            "prompt": prompt.strip(),
            "proper_answer": proper_ans,
            "markscheme": ms_text.strip(),
            "archetype": archetype,
        }
        corpus_items.append(item)
        topic_items[tid].append(item)
        comp_items["p1"].append(item)

    # 2. Ingest Paper 2 & Paper 4 items
    for comp in ["p2", "p4"]:
        print(f"Ingesting Paper {comp[1]} Theory items...")
        for q_dir in sorted(PAPERS_ROOT.glob(f"{comp}/**/question_*")):
            if not q_dir.is_dir():
                continue
            en_file = q_dir / "enrichment.json"
            if not en_file.is_file() or en_file.stat().st_size == 0:
                continue

            try:
                en_data = json.loads(en_file.read_text(encoding="utf-8"))
            except Exception:
                continue

            ms_file = q_dir / "markscheme.json"
            ms_rev = q_dir / "markscheme_reviewed.json"
            target_ms = ms_file if (ms_file.is_file() and ms_file.stat().st_size > 0) else ms_rev
            ms_map = {}
            if target_ms.is_file() and target_ms.stat().st_size > 0:
                try:
                    ms_data = json.loads(target_ms.read_text(encoding="utf-8"))
                    for mp in ms_data.get("parts", []):
                        pts = mp.get("marking_points", [])
                        raw_id = mp.get("id", "").lower()
                        ms_text_val = " ".join([p.get("text", "") for p in pts if isinstance(p, dict)])
                        ms_map[raw_id] = ms_text_val
                        ms_map[raw_id.replace("_", "")] = ms_text_val
                except Exception:
                    pass

            ocr_file = q_dir / "question_ocr.json"
            txt_file = q_dir / "question.txt"
            stem_map = {}
            if ocr_file.is_file() and ocr_file.stat().st_size > 0:
                try:
                    ocr_data = json.loads(ocr_file.read_text(encoding="utf-8"))
                    for op in ocr_data.get("parts", []):
                        raw_id = op.get("id", "").lower()
                        stem_val = op.get("part_stem") or op.get("text") or ""
                        stem_map[raw_id] = stem_val
                        stem_map[raw_id.replace("_", "")] = stem_val
                except Exception:
                    pass
            general_stem = txt_file.read_text(encoding="utf-8") if (txt_file.is_file() and txt_file.stat().st_size > 0) else ""

            for part in en_data.get("parts", []):
                if not isinstance(part, dict):
                    continue
                tid = part.get("primary_topic_id") or part.get("mapping", {}).get("primary_topic_id")
                if not tid or tid not in topic_names:
                    continue
                pid = part.get("part_id", "")
                pid_lower = pid.lower()
                pid_norm = pid_lower.replace("_", "")
                prompt = stem_map.get(pid_lower, "") or stem_map.get(pid_norm, "") or general_stem
                proper_ans = part.get("proper_answer", "")
                ms_text = ms_map.get(pid_lower, "") or ms_map.get(pid_norm, "")
                pats = part.get("question_patterns", [])
                archetype = classify_question(prompt, proper_ans, ms_text, comp, pats)

                item = {
                    "id": pid,
                    "component": comp,
                    "topic_id": tid,
                    "module_id": part.get("primary_module_id") or part.get("mapping", {}).get("primary_module_id", ""),
                    "outcome_ids": part.get("outcome_ids") or part.get("mapping", {}).get("outcome_ids", []),
                    "marks": part.get("marks", 1),
                    "prompt": prompt.strip(),
                    "proper_answer": proper_ans.strip(),
                    "markscheme": ms_text.strip(),
                    "archetype": archetype,
                }
                corpus_items.append(item)
                topic_items[tid].append(item)
                comp_items[comp].append(item)

    total_count = len(corpus_items)
    print(f"Total Physics items extracted across corpus: {total_count}")

    # Global N-Gram frequencies
    prompt_prefixes_2 = collections.Counter()
    prompt_prefixes_3 = collections.Counter()
    ms_bigrams = collections.Counter()
    ms_trigrams = collections.Counter()
    global_archetype_counts = collections.Counter([item["archetype"] for item in corpus_items])

    for item in corpus_items:
        clean_p = clean_prompt_for_prefix(item["prompt"])
        p_tokens = tokenize(clean_p)
        if len(p_tokens) >= 2:
            prompt_prefixes_2[" ".join(p_tokens[:2])] += 1
        if len(p_tokens) >= 3:
            prompt_prefixes_3[" ".join(p_tokens[:3])] += 1

        ms_clean_tokens = [t for t in tokenize(item["markscheme"]) if t not in MS_STOPWORDS and not t.isdigit() and len(t) > 1]
        if len(ms_clean_tokens) >= 2:
            ms_bigrams.update(get_ngrams(ms_clean_tokens, 2))
        if len(ms_clean_tokens) >= 3:
            ms_trigrams.update(get_ngrams(ms_clean_tokens, 3))

    # Compile JSON summary data
    dataset = {
        "total_items": total_count,
        "components": {
            "p1": len(comp_items["p1"]),
            "p2": len(comp_items["p2"]),
            "p4": len(comp_items["p4"]),
        },
        "global_archetype_distribution": dict(global_archetype_counts),
        "top_prompt_prefixes_3": prompt_prefixes_3.most_common(40),
        "top_markscheme_bigrams": ms_bigrams.most_common(40),
        "topics": {},
    }

    for tid, items in topic_items.items():
        t_archs = collections.Counter([it["archetype"] for it in items])
        t_p_prefixes = collections.Counter()
        t_ms_bigrams = collections.Counter()
        for it in items:
            clean_p = clean_prompt_for_prefix(it["prompt"])
            p_toks = tokenize(clean_p)
            if len(p_toks) >= 3:
                t_p_prefixes[" ".join(p_toks[:3])] += 1
            ms_toks = [t for t in tokenize(it["markscheme"]) if t not in MS_STOPWORDS and not t.isdigit() and len(t) > 1]
            if len(ms_toks) >= 2:
                t_ms_bigrams.update(get_ngrams(ms_toks, 2))

        dataset["topics"][tid] = {
            "topic_id": tid,
            "topic_name": topic_names[tid],
            "level": topic_levels[tid],
            "total_items": len(items),
            "archetypes": dict(t_archs),
            "top_prefixes": t_p_prefixes.most_common(10),
            "top_ms_phrases": t_ms_bigrams.most_common(10),
        }

    json_path = KNOWLEDGE_ROOT / "question-typology.json"
    json_path.write_text(json.dumps(dataset, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote machine-readable dataset to {json_path}")

    # Generate Master Knowledge Base Document
    print("Generating Master Knowledge Base Document...")
    kb_md = []
    kb_md.append("# Cambridge Physics (9702) Question Typology & Testing Pattern Reference")
    kb_md.append("")
    kb_md.append("## Executive Overview")
    kb_md.append("")
    kb_md.append(f"This reference deconstructs Cambridge examination questioning methods across the complete 2016-2025 past paper archive ({total_count} mapped items across Paper 1 MCQ, Paper 2 AS Theory, and Paper 4 A2 Theory).")
    kb_md.append("Using syntactic positional n-grams and mark scheme phrase mining, it identifies the six foundational question archetypes, authentic prompt templates, and examiner reward criteria.")
    kb_md.append("")
    kb_md.append("## Archetype Distribution")
    kb_md.append("")
    kb_md.append("| Question Archetype | Total Questions | Percentage | Primary Cognitive Domain |")
    kb_md.append("| :--- | :--- | :--- | :--- |")
    for arch in ARCHETYPES:
        cnt = global_archetype_counts.get(arch, 0)
        pct = (cnt / total_count * 100) if total_count else 0
        domain_desc = {
            "Quantitative Calculation & Multi-Step Derivation": "AO1 / AO2 - Formula application, algebraic derivation, numerical accuracy",
            "Graphical Sketching & Trend Interpretation": "AO2 / AO3 - Gradient, area under curve, graphical sketching, trend analysis",
            "Physical Mechanism & Field Explanation": "AO1 / AO2 - Causal physics explanations, field interactions, particle dynamics",
            "Definition, Law & Conservation Principle": "AO1 - Precise statement of physical laws, definitions, and SI relationships",
            "Diagrammatic Vector & Circuit Construction": "AO2 - Free-body force arrows, electric/magnetic field lines, circuit schematics",
            "Experimental Uncertainty & Measurement Analysis": "AO3 - Absolute/percentage uncertainty, error propagation, instrument calibration",
        }.get(arch, "AO1 / AO2")
        kb_md.append(f"| **{arch}** | {cnt} | {pct:.1f}% | {domain_desc} |")
    kb_md.append("")
    kb_md.append("## Cambridge Command Verb & Prefix N-Gram Dictionary")
    kb_md.append("")
    kb_md.append("Analysis of question opening sequences reveals repetitive trigger patterns that dictate student response structure:")
    kb_md.append("")
    kb_md.append("| Prefix Trigram | Frequency | Typical Target | Expected Student Response Frame |")
    kb_md.append("| :--- | :--- | :--- | :--- |")
    for prefix, cnt in prompt_prefixes_3.most_common(25):
        target = "Variable / Physical Quantity"
        if "calculate the" in prefix or "determine the" in prefix:
            target = "Numerical value"
            frame = "State formula -> substitute quantities in SI units -> calculate -> round to correct sig figs + unit"
        elif "show that" in prefix:
            target = "Derived value or relationship"
            frame = "State unrounded calculated value before quoting the target figure"
        elif "explain why" in prefix or "explain how" in prefix:
            target = "Physical causality"
            frame = "Chain of physical reasoning: identify applied law -> link forces/fields -> state equilibrium or acceleration"
        elif "describe the" in prefix:
            target = "Observed motion or physical change"
            frame = "State qualitative changes (e.g. constant velocity, decreasing acceleration) without unrequested theories"
        elif "state what" in prefix or "state the" in prefix or "define the" in prefix:
            target = "Law, principle, or definition"
            frame = "Verbatim syllabus definition or law statement without missing essential qualifiers"
        elif "sketch the" in prefix or "sketch on" in prefix:
            target = "Graphical curve or field lines"
            frame = "Mark key intercepts, asymptotic limits, initial gradients, and directional arrows"
        elif "with reference to" in prefix:
            target = "Figure or experimental apparatus"
            frame = "Cite specific features, coordinates, or reading differences from the stimulus"
        elif "diagram shows" in prefix or "figure shows" in prefix or "graph shows" in prefix:
            target = "Visual or experimental stimulus"
            frame = "Contextual stimulus providing geometry, circuit topology, or kinematics data for subsequent parts"
        elif "which statement" in prefix or "which row" in prefix or "what is" in prefix or "which of" in prefix:
            target = "Multiple choice discrimination"
            frame = "Systematic dimensional analysis or elimination of distractor options"
        elif "student carried" in prefix or "student investigated" in prefix:
            target = "Experimental setup"
            frame = "Identify measuring instruments, controlled parameters, and measurement uncertainties"
        else:
            target = "Syllabus outcome"
            frame = "Direct answer matching Cambridge physics conventions"
        kb_md.append(f"| `{prefix}` | {cnt} | {target} | {frame} |")
    kb_md.append("")
    kb_md.append("## Top Mark Scheme Causal Bigrams")
    kb_md.append("")
    kb_md.append("Examiners reward specific linked pairs of physics terms. The most frequent scoring bigrams in mark schemes are:")
    kb_md.append("")
    kb_md.append("| Mark Scheme Bigram | Occurrences | Topic Association | Scoring Rationale |")
    kb_md.append("| :--- | :--- | :--- | :--- |")
    for bg, cnt in ms_bigrams.most_common(20):
        kb_md.append(f"| `{bg}` | {cnt} | Syllabus-wide | Verbatim credit point required in marking notes |")
    kb_md.append("")
    kb_md.append("## Cross-Topic Testing Tendency Matrix")
    kb_md.append("")
    kb_md.append("| Topic ID | Topic Name | Level | Items | Top Question Archetype | Top Tested Pattern |")
    kb_md.append("| :--- | :--- | :--- | :--- | :--- | :--- |")
    for tid in sorted(topic_names.keys()):
        t_data = dataset["topics"][tid]
        top_arch = max(t_data["archetypes"].items(), key=lambda x: x[1])[0] if t_data["archetypes"] else "N/A"
        top_pref = t_data["top_prefixes"][0][0] if t_data["top_prefixes"] else "N/A"
        kb_md.append(f"| `{tid}` | {t_data['topic_name']} | {t_data['level']} | {t_data['total_items']} | {top_arch} | `{top_pref}` |")
    kb_md.append("")

    kb_doc_path = KNOWLEDGE_ROOT / "question-typology-and-testing-patterns.md"
    kb_doc_path.write_text(sanitize("\n".join(kb_md) + "\n"), encoding="utf-8")
    print(f"Wrote Master Knowledge Base Document to {kb_doc_path}")

    # Generate 25 Per-Topic Documents
    print("Generating 25 Topic-Specific Question Type Documents in study/topics/...")
    for tid, items in topic_items.items():
        topic_dir = None
        matches = list(STUDY_ROOT.glob(f"{tid}_*"))
        if matches:
            topic_dir = matches[0]
        else:
            t_slug = tid + "_" + re.sub(r"[^a-z0-9]+", "_", topic_names[tid].lower()).strip("_")
            topic_dir = STUDY_ROOT / t_slug

        if not topic_dir.is_dir():
            topic_dir.mkdir(parents=True, exist_ok=True)

        t_data = dataset["topics"][tid]
        t_archs = t_data["archetypes"]
        total_t_items = t_data["total_items"]

        # Select up to 2 real examples per archetype
        examples_by_arch: Dict[str, List[Dict[str, Any]]] = collections.defaultdict(list)
        for it in items:
            arch = it["archetype"]
            if len(examples_by_arch[arch]) < 2 and len(it["prompt"]) > 20:
                examples_by_arch[arch].append(it)

        t_md = []
        t_md.append(f"# Question Typology & Testing Analysis: {topic_names[tid]}")
        t_md.append("")
        t_md.append("## Topic Scope & Testing Profile")
        t_md.append("")
        t_md.append(f"- Topic ID: `{tid}` ({topic_names[tid]}), Level: {t_data['level']}.")
        t_md.append(f"- Total Past Paper Questions (2016-2025): {total_t_items} mapped items.")
        t_md.append("- Scope Rule: Strictly ZERO em dashes anywhere in this analysis.")
        t_md.append("")
        t_md.append("## Archetype Distribution for this Topic")
        t_md.append("")
        t_md.append("| Question Archetype | Count | Percentage | Cambridge Testing Focus |")
        t_md.append("| :--- | :--- | :--- | :--- |")
        for arch in ARCHETYPES:
            c = t_archs.get(arch, 0)
            p = (c / total_t_items * 100) if total_t_items else 0.0
            t_md.append(f"| **{arch}** | {c} | {p:.1f}% | Evaluates mastery of {topic_names[tid]} |")
        t_md.append("")
        t_md.append("## Top Question Prompt N-Grams")
        t_md.append("")
        t_md.append("The most frequent opening phrases used by Cambridge examiners for this topic:")
        t_md.append("")
        t_md.append("| Stem Prefix N-Gram | Frequency | Cognitive Expectation |")
        t_md.append("| :--- | :--- | :--- |")
        for pref, c in t_data["top_prefixes"]:
            t_md.append(f"| `{pref}` | {c} | Standard prompt starter in {topic_names[tid]} |")
        t_md.append("")
        t_md.append("## Top Mark Scheme Scoring Phrases")
        t_md.append("")
        t_md.append("High-frequency keyword combinations rewarded in examiner mark schemes:")
        t_md.append("")
        t_md.append("| Mark Scheme Keyword Pair | Frequency | Credit Condition |")
        t_md.append("| :--- | :--- | :--- |")
        for phrase, c in t_data["top_ms_phrases"]:
            t_md.append(f"| `{phrase}` | {c} | Core marking point |")
        t_md.append("")
        t_md.append("## Authentic Cambridge Past Paper Examples")
        t_md.append("")
        for arch in ARCHETYPES:
            exs = examples_by_arch.get(arch, [])
            if not exs:
                continue
            t_md.append(f"### Archetype: {arch}")
            t_md.append("")
            for idx, ex in enumerate(exs, 1):
                clean_prompt = ex["prompt"].replace("\n", " ").strip()
                if len(clean_prompt) > 220:
                    clean_prompt = clean_prompt[:220] + "..."
                clean_ms = ex["markscheme"].replace("\n", " ").strip()
                if len(clean_ms) > 180:
                    clean_ms = clean_ms[:180] + "..."
                t_md.append(f"**Example {idx} ({ex['id']})** - Marks: {ex['marks']}")
                t_md.append(f"- **Question Prompt**: {clean_prompt}")
                if clean_ms:
                    t_md.append(f"- **Mark Scheme Criteria**: {clean_ms}")
                if ex["proper_answer"] and ex["proper_answer"] != "Option ":
                    clean_pa = ex["proper_answer"].replace("\n", " ").strip()
                    if len(clean_pa) > 150:
                        clean_pa = clean_pa[:150] + "..."
                    t_md.append(f"- **Target Answer**: {clean_pa}")
                t_md.append("")

        out_path = topic_dir / "question-types.md"
        out_path.write_text(sanitize("\n".join(t_md) + "\n"), encoding="utf-8")
        print(f"  Generated {out_path}")

    print("Physics question typology and n-gram mining completed successfully.")


if __name__ == "__main__":
    main()
