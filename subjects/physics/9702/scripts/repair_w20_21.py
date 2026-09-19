#!/usr/bin/env python3
"""
scripts/repair_w20_21.py
Repairs all questions and enrichments for 9702_w20_21 (Q01 to Q08).
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def ordered_unique(seq):
    seen = set()
    res = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            res.append(x)
    return res

def save_json(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Saved {path.relative_to(ROOT)}")

def finalize_question(q_data):
    flow = []
    if q_data.get("question_stem") and q_data["question_stem"].strip():
        flow.append({"type": "stem"})
    for p in q_data.get("parts", []):
        flow.append({"type": "part", "part_id": p["id"]})
    q_data["content_flow"] = flow
    q_data["verification"] = {
        "content_structure_checked": True,
        "marks_reconciled": True,
        "numerical_values_checked": False
    }
    return q_data

def finalize_enrichment(enr_data):
    enr_data["numerical_values_checked"] = False
    pats = []
    topics = []
    modules = []
    outcomes = []
    for part in enr_data.get("parts", []):
        pats.extend(part.get("question_patterns", []))
        m = part.get("mapping", {})
        top = m.get("primary_topic_id")
        mod = m.get("primary_module_id")
        if top:
            topics.append(top)
        if mod:
            modules.append(mod)
        outcomes.extend(m.get("outcome_ids", []))
    
    enr_data["question_patterns"] = ordered_unique(pats)
    enr_data["mapping"] = {
        "topic_ids": ordered_unique(topics),
        "module_ids": ordered_unique(modules),
        "outcome_ids": ordered_unique(outcomes)
    }
    return enr_data

# ==============================================================================
# Q01
# ==============================================================================
def repair_w20_21_q01():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w20_qp_21/question_01.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w20_21_q01.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_1_1",
            "label": "Fig. 1.1",
            "file": "figure_1_1.png",
            "introduced_by": "9702_w20_21_q01_b",
            "referenced_by": ["9702_w20_21_q01_b"],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w20_21_q01_b",
                "anchor": "A uniform rigid rod of length 2.4 m is shown in Fig. 1.1."
            }
        },
        {
            "id": "fig_1_2",
            "label": "Fig. 1.2",
            "file": "figure_1_2.png",
            "introduced_by": "9702_w20_21_q01_c",
            "referenced_by": ["9702_w20_21_q01_c"],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w20_21_q01_c",
                "anchor": "A fishing rod AB, made from the rod in (b), is shown in Fig. 1.2."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}
    
    p_ai = parts_by_id["9702_w20_21_q01_a_i"]
    p_ai["question_text"] = "Define the moment of a force about a point."
    p_ai["question_text_latex"] = "Define the moment of a force about a point."
    p_ai["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q01_a_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q01_a_i_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Answer",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_aii = parts_by_id["9702_w20_21_q01_a_ii"]
    p_aii["question_text"] = "Determine the SI base units of the moment of a force.\nbase units"
    p_aii["question_text_latex"] = "Determine the SI base units of the moment of a force.\n\\text{base units}"
    p_aii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q01_a_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q01_a_ii_value",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Base units",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w20_21_q01_b"]
    p_b["question_text"] = "A uniform rigid rod of length 2.4 m is shown in Fig. 1.1.\nThe rod has a weight of 5.2 N and is made of wood of density 790 kg m^{-3}.\nCalculate the cross-sectional area A, in mm^{2}, of the rod.\nA = mm^{2}"
    p_b["question_text_latex"] = "A uniform rigid rod of length $2.4\\text{ m}$ is shown in Fig. 1.1.\nThe rod has a weight of $5.2\\text{ N}$ and is made of wood of density $790\\text{ kg m}^{-3}$.\nCalculate the cross-sectional area $A$, in $\\text{mm}^2$, of the rod.\n$$A = \\text{.................................................... mm}^2$$"
    p_b["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q01_b_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q01_b_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "A",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{mm}^2"
                        }
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_w20_21_q01_c"]
    p_c["question_text"] = "A fishing rod AB, made from the rod in (b), is shown in Fig. 1.2.\nEnd A of the rod rests on the ground and a string is attached to the other end B. A support stick exerts a force perpendicular to the rod at point C. The weight of the rod acts at point D.\nThe tension T in the string is in a direction perpendicular to the rod. The rod is in equilibrium and inclined at an angle of 56° to the vertical.\nThe forces and the distances along the rod of points A, B, C and D are shown in Fig. 1.2."
    p_c["question_text_latex"] = "A fishing rod AB, made from the rod in (b), is shown in Fig. 1.2.\nEnd A of the rod rests on the ground and a string is attached to the other end B. A support stick exerts a force perpendicular to the rod at point C. The weight of the rod acts at point D.\nThe tension $T$ in the string is in a direction perpendicular to the rod. The rod is in equilibrium and inclined at an angle of $56^\\circ$ to the vertical.\nThe forces and the distances along the rod of points A, B, C and D are shown in Fig. 1.2."

    p_ci = parts_by_id["9702_w20_21_q01_c_i"]
    p_ci["question_text"] = "Show that the component of the weight that is perpendicular to the rod is 4.3 N."
    p_ci["question_text_latex"] = "Show that the component of the weight that is perpendicular to the rod is $4.3\\text{ N}$."
    p_ci["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q01_c_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q01_c_i_working",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_cii = parts_by_id["9702_w20_21_q01_c_ii"]
    p_cii["question_text"] = "By taking moments about end A of the rod, calculate the tension T.\nT = N"
    p_cii["question_text_latex"] = "By taking moments about end A of the rod, calculate the tension $T$.\n$$T = \\text{.................................................... N}$$"
    p_cii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q01_c_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q01_c_ii_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "T",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{N}"
                        }
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_w20_21_q01_a_i"]["mapping"] = {
        "primary_topic_id": "9702_t04",
        "primary_module_id": "9702_t04_m01",
        "outcome_ids": ["9702_t04_m01_o02"]
    }
    ed_parts["9702_w20_21_q01_a_i"]["skills"] = {
        "primary_skill_id": "9702_skill_moments_couples",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q01_a_i"]["question_patterns"] = ["definition"]
    ed_parts["9702_w20_21_q01_a_i"]["knowledge_refs"] = {
        "definition_ids": ["9702_def_moment_of_force"],
        "formula_ids": ["9702_formula_moment"]
    }

    ed_parts["9702_w20_21_q01_a_ii"]["mapping"] = {
        "primary_topic_id": "9702_t01",
        "primary_module_id": "9702_t01_m02",
        "outcome_ids": ["9702_t01_m02_o02"]
    }
    ed_parts["9702_w20_21_q01_a_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_si_units_homogeneity",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q01_a_ii"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_21_q01_a_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_moment"]
    }

    ed_parts["9702_w20_21_q01_b"]["mapping"] = {
        "primary_topic_id": "9702_t04",
        "primary_module_id": "9702_t04_m03",
        "outcome_ids": ["9702_t04_m03_o01"]
    }
    ed_parts["9702_w20_21_q01_b"]["skills"] = {
        "primary_skill_id": "9702_skill_density_pressure",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q01_b"]["question_patterns"] = ["multi_step_calculation"]
    ed_parts["9702_w20_21_q01_b"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_density", "9702_formula_weight"]
    }

    ed_parts["9702_w20_21_q01_c_i"]["mapping"] = {
        "primary_topic_id": "9702_t01",
        "primary_module_id": "9702_t01_m04",
        "outcome_ids": ["9702_t01_m04_o03"]
    }
    ed_parts["9702_w20_21_q01_c_i"]["skills"] = {
        "primary_skill_id": "9702_skill_scalars_vectors",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q01_c_i"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_21_q01_c_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Resolution of a weight vector into a perpendicular component using trigonometry."
    }

    ed_parts["9702_w20_21_q01_c_ii"]["mapping"] = {
        "primary_topic_id": "9702_t04",
        "primary_module_id": "9702_t04_m01",
        "outcome_ids": ["9702_t04_m01_o02"]
    }
    ed_parts["9702_w20_21_q01_c_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_moments_couples",
        "supporting_skill_ids": ["9702_skill_equilibrium_coplanar_forces"]
    }
    ed_parts["9702_w20_21_q01_c_ii"]["question_patterns"] = ["multi_step_calculation"]
    ed_parts["9702_w20_21_q01_c_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_moment"]
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)

# ==============================================================================
# Q02
# ==============================================================================
def repair_w20_21_q02():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w20_qp_21/question_02.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w20_21_q02.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["question_stem"] = "A small block is lifted vertically upwards by a toy aircraft, as illustrated in Fig. 2.1.\nAs the block is moving upwards, the string breaks at time t = 0. The block initially continues moving upwards and then falls and hits the ground at time t = 0.90 s. The variation with time t of the velocity v of the block is shown in Fig. 2.2.\nAir resistance is negligible."
    qd["question_stem_latex"] = "A small block is lifted vertically upwards by a toy aircraft, as illustrated in Fig. 2.1.\nAs the block is moving upwards, the string breaks at time $t = 0$. The block initially continues moving upwards and then falls and hits the ground at time $t = 0.90\\text{ s}$. The variation with time $t$ of the velocity $v$ of the block is shown in Fig. 2.2.\nAir resistance is negligible."

    qd["figures"] = [
        {
            "id": "fig_2_1",
            "label": "Fig. 2.1",
            "file": "figure_2_1.png",
            "introduced_by": None,
            "referenced_by": [],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "question",
                "position": "after_stem",
                "anchor": "A small block is lifted vertically upwards by a toy aircraft, as illustrated in Fig. 2.1."
            }
        },
        {
            "id": "fig_2_2",
            "label": "Fig. 2.2",
            "file": "figure_2_2.png",
            "introduced_by": "9702_w20_21_q02_a",
            "referenced_by": ["9702_w20_21_q02_a", "9702_w20_21_q02_b"],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "question",
                "position": "after_stem",
                "anchor": "The variation with time t of the velocity v of the block is shown in Fig. 2.2."
            }
        },
        {
            "id": "fig_2_3",
            "label": "Fig. 2.3",
            "file": "figure_2_3.png",
            "introduced_by": "9702_w20_21_q02_d",
            "referenced_by": ["9702_w20_21_q02_d"],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w20_21_q02_d",
                "anchor": "On Fig. 2.3, sketch a line to show the variation of the distance moved by the block with time t from t = 0 to t = 0.20 s. Numerical values of distance are not required."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w20_21_q02_a"]
    p_a["question_text"] = "State the feature of the graph in Fig. 2.2 that shows the block has a constant acceleration."
    p_a["question_text_latex"] = "State the feature of the graph in Fig. 2.2 that shows the block has a constant acceleration."
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q02_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q02_a_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Answer",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w20_21_q02_b"]
    p_b["question_text"] = "Use Fig. 2.2 to determine the height of the block above the ground when the string breaks at time t = 0.\nheight = m"
    p_b["question_text_latex"] = "Use Fig. 2.2 to determine the height of the block above the ground when the string breaks at time $t = 0$.\n$$\\text{height} = \\text{.................................................... m}$$"
    p_b["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q02_b_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q02_b_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Height",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m}"
                        }
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_w20_21_q02_c"]
    p_c["question_text"] = "The block has a weight of 0.86 N.\nCalculate the difference in gravitational potential energy of the block between time t = 0 and time t = 0.90 s.\ndifference in gravitational potential energy = J"
    p_c["question_text_latex"] = "The block has a weight of $0.86\\text{ N}$.\nCalculate the difference in gravitational potential energy of the block between time $t = 0$ and time $t = 0.90\\text{ s}$.\n$$\\text{difference in gravitational potential energy} = \\text{.................................................... J}$$"
    p_c["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q02_c_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q02_c_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Difference in gravitational potential energy",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{J}"
                        }
                    }
                ]
            }
        ]
    }

    p_d = parts_by_id["9702_w20_21_q02_d"]
    p_d["question_text"] = "On Fig. 2.3, sketch a line to show the variation of the distance moved by the block with time t from t = 0 to t = 0.20 s. Numerical values of distance are not required."
    p_d["question_text_latex"] = "On Fig. 2.3, sketch a line to show the variation of the distance moved by the block with time $t$ from $t = 0$ to $t = 0.20\\text{ s}$. Numerical values of distance are not required."
    p_d["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q02_d_canvas",
                "type": "canvas",
                "background_figure_id": "fig_2_3",
                "tools": ["line", "pen"]
            }
        ]
    }

    p_e = parts_by_id["9702_w20_21_q02_e"]
    p_e["question_text"] = "A block of greater mass is now released from the same height with the same upward velocity.\nAir resistance is still negligible.\nState and explain the effect, if any, of the increased mass on the speed with which the block hits the ground."
    p_e["question_text_latex"] = "A block of greater mass is now released from the same height with the same upward velocity.\nAir resistance is still negligible.\nState and explain the effect, if any, of the increased mass on the speed with which the block hits the ground."
    p_e["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q02_e_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q02_e_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Answer",
                        "required": True
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_w20_21_q02_a"]["mapping"] = {
        "primary_topic_id": "9702_t02",
        "primary_module_id": "9702_t02_m01",
        "outcome_ids": ["9702_t02_m01_o05"]
    }
    ed_parts["9702_w20_21_q02_a"]["skills"] = {
        "primary_skill_id": "9702_skill_motion_graphs",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q02_a"]["question_patterns"] = ["graph_interpretation"]
    ed_parts["9702_w20_21_q02_a"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Qualitative interpretation of constant gradient representing constant acceleration on a velocity-time graph."
    }

    ed_parts["9702_w20_21_q02_b"]["mapping"] = {
        "primary_topic_id": "9702_t02",
        "primary_module_id": "9702_t02_m01",
        "outcome_ids": ["9702_t02_m01_o03", "9702_t02_m01_o07"]
    }
    ed_parts["9702_w20_21_q02_b"]["skills"] = {
        "primary_skill_id": "9702_skill_motion_graphs",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q02_b"]["question_patterns"] = ["graph_interpretation", "multi_step_calculation"]
    ed_parts["9702_w20_21_q02_b"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Determining displacement and initial height geometrically from triangular areas under a velocity-time graph."
    }

    ed_parts["9702_w20_21_q02_c"]["mapping"] = {
        "primary_topic_id": "9702_t05",
        "primary_module_id": "9702_t05_m02",
        "outcome_ids": ["9702_t05_m02_o02"]
    }
    ed_parts["9702_w20_21_q02_c"]["skills"] = {
        "primary_skill_id": "9702_skill_kinetic_potential_energy",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q02_c"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_21_q02_c"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_gravitational_potential_energy"]
    }

    ed_parts["9702_w20_21_q02_d"]["mapping"] = {
        "primary_topic_id": "9702_t02",
        "primary_module_id": "9702_t02_m01",
        "outcome_ids": ["9702_t02_m01_o04"]
    }
    ed_parts["9702_w20_21_q02_d"]["skills"] = {
        "primary_skill_id": "9702_skill_motion_graphs",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q02_d"]["question_patterns"] = ["graph_construction"]
    ed_parts["9702_w20_21_q02_d"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Qualitative sketch of a distance-time curve showing decreasing gradient for decelerating motion."
    }

    ed_parts["9702_w20_21_q02_e"]["mapping"] = {
        "primary_topic_id": "9702_t02",
        "primary_module_id": "9702_t02_m01",
        "outcome_ids": ["9702_t02_m01_o06"]
    }
    ed_parts["9702_w20_21_q02_e"]["skills"] = {
        "primary_skill_id": "9702_skill_displacement_velocity_acceleration",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q02_e"]["question_patterns"] = ["explanation"]
    ed_parts["9702_w20_21_q02_e"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Qualitative deduction that acceleration of free fall g is independent of mass in the absence of air resistance."
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)

# ==============================================================================
# Q03
# ==============================================================================
def repair_w20_21_q03():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w20_qp_21/question_03.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w20_21_q03.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_3_1",
            "label": "Fig. 3.1",
            "file": "figure_3_1.png",
            "introduced_by": "9702_w20_21_q03_b",
            "referenced_by": ["9702_w20_21_q03_b"],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w20_21_q03_b",
                "anchor": "A ball falls vertically downwards towards a horizontal floor and then rebounds along its original path, as illustrated in Fig. 3.1."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w20_21_q03_a"]
    p_a["question_text"] = "Define force."
    p_a["question_text_latex"] = "Define force."
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q03_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q03_a_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Answer",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w20_21_q03_b"]
    p_b["question_text"] = "A ball falls vertically downwards towards a horizontal floor and then rebounds along its original path, as illustrated in Fig. 3.1.\nThe ball reaches the floor with speed 3.8 m s^{-1}. The ball is then in contact with the floor for a time of 0.081 s before leaving it with speed 1.7 m s^{-1}. The mass of the ball is 0.062 kg."
    p_b["question_text_latex"] = "A ball falls vertically downwards towards a horizontal floor and then rebounds along its original path, as illustrated in Fig. 3.1.\nThe ball reaches the floor with speed $3.8\\text{ m s}^{-1}$. The ball is then in contact with the floor for a time of $0.081\\text{ s}$ before leaving it with speed $1.7\\text{ m s}^{-1}$. The mass of the ball is $0.062\\text{ kg}$."

    p_bi = parts_by_id["9702_w20_21_q03_b_i"]
    p_bi["question_text"] = "Calculate the loss of kinetic energy of the ball during the collision.\nloss of kinetic energy = J"
    p_bi["question_text_latex"] = "Calculate the loss of kinetic energy of the ball during the collision.\n$$\\text{loss of kinetic energy} = \\text{.................................................... J}$$"
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q03_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q03_b_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Loss of kinetic energy",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{J}"
                        }
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_w20_21_q03_b_ii"]
    p_bii["question_text"] = "Determine the magnitude of the change in momentum of the ball during the collision.\nchange in momentum = N s"
    p_bii["question_text_latex"] = "Determine the magnitude of the change in momentum of the ball during the collision.\n$$\\text{change in momentum} = \\text{.................................................... N s}$$"
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q03_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q03_b_ii_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Magnitude of change in momentum",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{N s}"
                        }
                    }
                ]
            }
        ]
    }

    p_biii = parts_by_id["9702_w20_21_q03_b_iii"]
    p_biii["question_text"] = "Show that the magnitude of the average resultant force acting on the ball during the collision is 4.2 N."
    p_biii["question_text_latex"] = "Show that the magnitude of the average resultant force acting on the ball during the collision is $4.2\\text{ N}$."
    p_biii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q03_b_iii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q03_b_iii_working",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_biv = parts_by_id["9702_w20_21_q03_b_iv"]
    p_biv["question_text"] = "Use the information in (iii) to calculate the magnitude of:\n1. the average force of the floor on the ball during the collision\n2. the average force of the ball on the floor during the collision."
    p_biv["question_text_latex"] = "Use the information in (iii) to calculate the magnitude of:\n1. the average force of the floor on the ball during the collision\n2. the average force of the ball on the floor during the collision."
    p_biv["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q03_b_iv_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q03_b_iv_1",
                        "control": "quantity",
                        "role": "answer",
                        "label": "1. Average force of floor on ball",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{N}"
                        }
                    },
                    {
                        "field_id": "9702_w20_21_q03_b_iv_2",
                        "control": "quantity",
                        "role": "answer",
                        "label": "2. Average force of ball on floor",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{N}"
                        }
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_w20_21_q03_a"]["mapping"] = {
        "primary_topic_id": "9702_t03",
        "primary_module_id": "9702_t03_m01",
        "outcome_ids": ["9702_t03_m01_o04"]
    }
    ed_parts["9702_w20_21_q03_a"]["skills"] = {
        "primary_skill_id": "9702_skill_newtons_laws",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q03_a"]["question_patterns"] = ["definition"]
    ed_parts["9702_w20_21_q03_a"]["knowledge_refs"] = {
        "definition_ids": ["9702_def_force"],
        "formula_ids": ["9702_formula_force_momentum_rate"]
    }

    ed_parts["9702_w20_21_q03_b_i"]["mapping"] = {
        "primary_topic_id": "9702_t05",
        "primary_module_id": "9702_t05_m02",
        "outcome_ids": ["9702_t05_m02_o01"]
    }
    ed_parts["9702_w20_21_q03_b_i"]["skills"] = {
        "primary_skill_id": "9702_skill_kinetic_potential_energy",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q03_b_i"]["question_patterns"] = ["multi_step_calculation"]
    ed_parts["9702_w20_21_q03_b_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_kinetic_energy"]
    }

    ed_parts["9702_w20_21_q03_b_ii"]["mapping"] = {
        "primary_topic_id": "9702_t03",
        "primary_module_id": "9702_t03_m01",
        "outcome_ids": ["9702_t03_m01_o01"]
    }
    ed_parts["9702_w20_21_q03_b_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_linear_momentum_collisions",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q03_b_ii"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_21_q03_b_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_momentum"]
    }

    ed_parts["9702_w20_21_q03_b_iii"]["mapping"] = {
        "primary_topic_id": "9702_t03",
        "primary_module_id": "9702_t03_m01",
        "outcome_ids": ["9702_t03_m01_o04"]
    }
    ed_parts["9702_w20_21_q03_b_iii"]["skills"] = {
        "primary_skill_id": "9702_skill_newtons_laws",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q03_b_iii"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_21_q03_b_iii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_force_momentum_rate"]
    }

    ed_parts["9702_w20_21_q03_b_iv"]["mapping"] = {
        "primary_topic_id": "9702_t03",
        "primary_module_id": "9702_t03_m01",
        "outcome_ids": ["9702_t03_m01_o04", "9702_t03_m01_o05"]
    }
    ed_parts["9702_w20_21_q03_b_iv"]["skills"] = {
        "primary_skill_id": "9702_skill_newtons_laws",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q03_b_iv"]["question_patterns"] = ["multi_step_calculation"]
    ed_parts["9702_w20_21_q03_b_iv"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_weight", "9702_formula_force_momentum_rate"]
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)

# ==============================================================================
# Q04
# ==============================================================================
def repair_w20_21_q04():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w20_qp_21/question_04.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w20_21_q04.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["total_marks"] = 9
    qd["detected_part_marks"] = 9
    qd["marks_validation_passed"] = True
    qd["review_flags"] = []

    qd["figures"] = [
        {
            "id": "fig_4_1",
            "label": "Fig. 4.1",
            "file": "figure_4_1.png",
            "introduced_by": "9702_w20_21_q04_b_i",
            "referenced_by": ["9702_w20_21_q04_b_i", "9702_w20_21_q04_b_ii"],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w20_21_q04_b_i",
                "anchor": "The variation of the force F with extension x of the wire is shown in Fig. 4.1."
            }
        },
        {
            "id": "fig_4_2",
            "label": "Fig. 4.2",
            "file": "figure_4_2.png",
            "introduced_by": "9702_w20_21_q04_b_iii",
            "referenced_by": ["9702_w20_21_q04_b_iii"],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w20_21_q04_b_iii",
                "anchor": "The new graph obtained is shown in Fig. 4.2."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w20_21_q04_a"]
    p_a["question_text"] = "Define, for a wire:"
    p_a["question_text_latex"] = "Define, for a wire:"

    p_ai = parts_by_id["9702_w20_21_q04_a_i"]
    p_ai["question_text"] = "stress"
    p_ai["question_text_latex"] = "stress"
    p_ai["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q04_a_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q04_a_i_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Stress definition",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_aii = parts_by_id["9702_w20_21_q04_a_ii"]
    p_aii["question_text"] = "strain."
    p_aii["question_text_latex"] = "strain."
    p_aii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q04_a_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q04_a_ii_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Strain definition",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w20_21_q04_b"]
    p_b["question_text"] = ""
    p_b["question_text_latex"] = ""

    p_bi = parts_by_id["9702_w20_21_q04_b_i"]
    p_bi["question_text"] = "A school experiment is performed on a metal wire to determine the Young modulus of the metal. A force is applied to one end of the wire which is fixed at the other end. The variation of the force F with extension x of the wire is shown in Fig. 4.1.\nThe maximum force applied to the wire is F_{1}.\nThe gradient of the graph line in Fig. 4.1 is G. The wire has initial length L and cross-sectional area A.\nDetermine an expression, in terms of A, G and L, for the Young modulus E of the metal.\nE ="
    p_bi["question_text_latex"] = "A school experiment is performed on a metal wire to determine the Young modulus of the metal. A force is applied to one end of the wire which is fixed at the other end. The variation of the force $F$ with extension $x$ of the wire is shown in Fig. 4.1.\nThe maximum force applied to the wire is $F_{1}$.\nThe gradient of the graph line in Fig. 4.1 is $G$. The wire has initial length $L$ and cross-sectional area $A$.\nDetermine an expression, in terms of $A$, $G$ and $L$, for the Young modulus $E$ of the metal.\n$$E = \\text{....................................................}$$"
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q04_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q04_b_i_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "E",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_w20_21_q04_b_ii"]
    p_bii["question_text"] = "A student repeats the experiment in (b)(i) using a new wire that has twice the diameter of the first wire. The initial length of the wire and the metal of the wire are unchanged.\nOn Fig. 4.1, draw the graph line representing the new wire for the force increasing from F = 0 to F = F_{1}."
    p_bii["question_text_latex"] = "A student repeats the experiment in (b)(i) using a new wire that has twice the diameter of the first wire. The initial length of the wire and the metal of the wire are unchanged.\nOn Fig. 4.1, draw the graph line representing the new wire for the force increasing from $F = 0$ to $F = F_{1}$."
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q04_b_ii_canvas",
                "type": "canvas",
                "background_figure_id": "fig_4_1",
                "tools": ["line", "pen"]
            }
        ]
    }

    p_biii = parts_by_id["9702_w20_21_q04_b_iii"]
    p_biii["marks"] = 2
    p_biii["question_text"] = "Another student repeats the original experiment in (b)(i), increasing the force beyond F_{1} to a new maximum force F_{2}. The new graph obtained is shown in Fig. 4.2.\n1. On Fig. 4.2, shade an area that represents the work done to extend the wire when the force is increased from F_{1} to F_{2}.\n2. Explain how the student can check that the elastic limit of the wire was not exceeded when force F_{2} was applied."
    p_biii["question_text_latex"] = "Another student repeats the original experiment in (b)(i), increasing the force beyond $F_{1}$ to a new maximum force $F_{2}$. The new graph obtained is shown in Fig. 4.2.\n1. On Fig. 4.2, shade an area that represents the work done to extend the wire when the force is increased from $F_{1}$ to $F_{2}$.\n2. Explain how the student can check that the elastic limit of the wire was not exceeded when force $F_{2}$ was applied."
    p_biii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q04_b_iii_canvas",
                "type": "canvas",
                "background_figure_id": "fig_4_2",
                "tools": ["pen", "fill"]
            },
            {
                "block_id": "9702_w20_21_q04_b_iii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q04_b_iii_explanation",
                        "control": "long_text",
                        "role": "answer",
                        "label": "2. Explanation",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_biv = parts_by_id["9702_w20_21_q04_b_iv"]
    p_biv["question_text"] = "Each student in the class performs the experiment in (b)(i). The teacher describes the values of the Young modulus calculated by the students as having high accuracy and low precision.\nExplain what is meant by low precision."
    p_biv["question_text_latex"] = "Each student in the class performs the experiment in (b)(i). The teacher describes the values of the Young modulus calculated by the students as having high accuracy and low precision.\nExplain what is meant by low precision."
    p_biv["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q04_b_iv_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q04_b_iv_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Answer",
                        "required": True
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_w20_21_q04_a_i"]["mapping"] = {
        "primary_topic_id": "9702_t06",
        "primary_module_id": "9702_t06_m01",
        "outcome_ids": ["9702_t06_m01_o01"]
    }
    ed_parts["9702_w20_21_q04_a_i"]["skills"] = {
        "primary_skill_id": "9702_skill_young_modulus",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q04_a_i"]["question_patterns"] = ["definition"]
    ed_parts["9702_w20_21_q04_a_i"]["knowledge_refs"] = {
        "definition_ids": ["9702_def_stress"],
        "formula_ids": ["9702_formula_stress"]
    }

    ed_parts["9702_w20_21_q04_a_ii"]["mapping"] = {
        "primary_topic_id": "9702_t06",
        "primary_module_id": "9702_t06_m01",
        "outcome_ids": ["9702_t06_m01_o01"]
    }
    ed_parts["9702_w20_21_q04_a_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_young_modulus",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q04_a_ii"]["question_patterns"] = ["definition"]
    ed_parts["9702_w20_21_q04_a_ii"]["knowledge_refs"] = {
        "definition_ids": ["9702_def_strain"],
        "formula_ids": ["9702_formula_strain"]
    }

    ed_parts["9702_w20_21_q04_b_i"]["mapping"] = {
        "primary_topic_id": "9702_t06",
        "primary_module_id": "9702_t06_m01",
        "outcome_ids": ["9702_t06_m01_o02"]
    }
    ed_parts["9702_w20_21_q04_b_i"]["skills"] = {
        "primary_skill_id": "9702_skill_young_modulus",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q04_b_i"]["question_patterns"] = ["equation_derivation"]
    ed_parts["9702_w20_21_q04_b_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_young_modulus"]
    }

    ed_parts["9702_w20_21_q04_b_ii"]["mapping"] = {
        "primary_topic_id": "9702_t06",
        "primary_module_id": "9702_t06_m01",
        "outcome_ids": ["9702_t06_m01_o02"]
    }
    ed_parts["9702_w20_21_q04_b_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_young_modulus",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q04_b_ii"]["question_patterns"] = ["graph_construction"]
    ed_parts["9702_w20_21_q04_b_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_young_modulus"]
    }

    ed_parts["9702_w20_21_q04_b_iii"]["mapping"] = {
        "primary_topic_id": "9702_t06",
        "primary_module_id": "9702_t06_m02",
        "outcome_ids": ["9702_t06_m02_o01", "9702_t06_m02_o02"]
    }
    ed_parts["9702_w20_21_q04_b_iii"]["skills"] = {
        "primary_skill_id": "9702_skill_elastic_plastic_behaviour",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q04_b_iii"]["question_patterns"] = ["graph_interpretation", "explanation"]
    ed_parts["9702_w20_21_q04_b_iii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Graphical identification of work done as area under force-extension curve and physical test for plastic deformation."
    }

    ed_parts["9702_w20_21_q04_b_iv"]["mapping"] = {
        "primary_topic_id": "9702_t01",
        "primary_module_id": "9702_t01_m03",
        "outcome_ids": ["9702_t01_m03_o02"]
    }
    ed_parts["9702_w20_21_q04_b_iv"]["skills"] = {
        "primary_skill_id": "9702_skill_errors_uncertainties",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q04_b_iv"]["question_patterns"] = ["explanation"]
    ed_parts["9702_w20_21_q04_b_iv"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Qualitative explanation of experimental measurement precision."
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)

# ==============================================================================
# Q05
# ==============================================================================
def repair_w20_21_q05():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w20_qp_21/question_05.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w20_21_q05.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["question_stem"] = "A progressive wave Y passes a point P. The variation with time t of the displacement x for the wave at P is shown in Fig. 5.1.\nThe wave has a wavelength of 8.0 cm."
    qd["question_stem_latex"] = "A progressive wave Y passes a point P. The variation with time $t$ of the displacement $x$ for the wave at P is shown in Fig. 5.1.\nThe wave has a wavelength of $8.0\\text{ cm}$."

    qd["figures"] = [
        {
            "id": "fig_5_1",
            "label": "Fig. 5.1",
            "file": "figure_5_1.png",
            "introduced_by": None,
            "referenced_by": [],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "question",
                "position": "after_stem",
                "anchor": "The variation with time t of the displacement x for the wave at P is shown in Fig. 5.1."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w20_21_q05_a"]
    p_a["question_text"] = "Determine the speed of the wave.\nspeed = m s^{-1}"
    p_a["question_text_latex"] = "Determine the speed of the wave.\n$$\\text{speed} = \\text{.................................................... m s}^{-1}$$"
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q05_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q05_a_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Speed",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m s}^{-1}"
                        }
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w20_21_q05_b"]
    p_b["question_text"] = "A second wave Z has wavelength 8.0 cm and amplitude 2.0 mm at point P. Waves Y and Z have the same speed.\nFor the waves at point P, calculate the ratio (intensity of wave Z) / (intensity of wave Y).\nratio ="
    p_b["question_text_latex"] = "A second wave Z has wavelength $8.0\\text{ cm}$ and amplitude $2.0\\text{ mm}$ at point P. Waves Y and Z have the same speed.\nFor the waves at point P, calculate the ratio:\n$$\\frac{\\text{intensity of wave Z}}{\\text{intensity of wave Y}}$$\n$$\\text{ratio} = \\text{....................................................}$$"
    p_b["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q05_b_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q05_b_value",
                        "control": "number",
                        "role": "answer",
                        "label": "Ratio",
                        "required": True
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_w20_21_q05_a"]["mapping"] = {
        "primary_topic_id": "9702_t07",
        "primary_module_id": "9702_t07_m01",
        "outcome_ids": ["9702_t07_m01_o05"]
    }
    ed_parts["9702_w20_21_q05_a"]["skills"] = {
        "primary_skill_id": "9702_skill_progressive_wave_properties",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q05_a"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_21_q05_a"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_wave_speed", "9702_formula_period_frequency"]
    }

    ed_parts["9702_w20_21_q05_b"]["mapping"] = {
        "primary_topic_id": "9702_t07",
        "primary_module_id": "9702_t07_m01",
        "outcome_ids": ["9702_t07_m01_o07"]
    }
    ed_parts["9702_w20_21_q05_b"]["skills"] = {
        "primary_skill_id": "9702_skill_wave_intensity_amplitude",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q05_b"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_21_q05_b"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_wave_intensity_amplitude"]
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)

# ==============================================================================
# Q06
# ==============================================================================
def repair_w20_21_q06():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w20_qp_21/question_06.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w20_21_q06.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = []

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w20_21_q06_a"]
    p_a["question_text"] = "Describe the conditions required for two waves to be able to form a stationary wave."
    p_a["question_text_latex"] = "Describe the conditions required for two waves to be able to form a stationary wave."
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q06_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q06_a_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Answer",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w20_21_q06_b"]
    p_b["question_text"] = "A stationary wave on a string has nodes and antinodes. The distance between a node and an adjacent antinode is 6.0 cm."
    p_b["question_text_latex"] = "A stationary wave on a string has nodes and antinodes. The distance between a node and an adjacent antinode is $6.0\\text{ cm}$."

    p_bi = parts_by_id["9702_w20_21_q06_b_i"]
    p_bi["question_text"] = "State what is meant by a node."
    p_bi["question_text_latex"] = "State what is meant by a node."
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q06_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q06_b_i_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Answer",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_w20_21_q06_b_ii"]
    p_bii["question_text"] = "Calculate the wavelength of the two waves forming the stationary wave.\nwavelength = cm"
    p_bii["question_text_latex"] = "Calculate the wavelength of the two waves forming the stationary wave.\n$$\\text{wavelength} = \\text{.................................................... cm}$$"
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q06_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q06_b_ii_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Wavelength",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{cm}"
                        }
                    }
                ]
            }
        ]
    }

    p_biii = parts_by_id["9702_w20_21_q06_b_iii"]
    p_biii["question_text"] = "State the phase difference between the particles at two adjacent antinodes of the stationary wave.\nphase difference = °"
    p_biii["question_text_latex"] = "State the phase difference between the particles at two adjacent antinodes of the stationary wave.\n$$\\text{phase difference} = \\text{....................................................}^\\circ$$"
    p_biii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q06_b_iii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q06_b_iii_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Phase difference",
                        "required": True,
                        "unit": {
                            "unit_latex": "^\\circ"
                        }
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_w20_21_q06_a"]["mapping"] = {
        "primary_topic_id": "9702_t08",
        "primary_module_id": "9702_t08_m01",
        "outcome_ids": ["9702_t08_m01_o01"]
    }
    ed_parts["9702_w20_21_q06_a"]["skills"] = {
        "primary_skill_id": "9702_skill_stationary_waves",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q06_a"]["question_patterns"] = ["explanation"]
    ed_parts["9702_w20_21_q06_a"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Qualitative description of conditions required for stationary wave formation."
    }

    ed_parts["9702_w20_21_q06_b_i"]["mapping"] = {
        "primary_topic_id": "9702_t08",
        "primary_module_id": "9702_t08_m01",
        "outcome_ids": ["9702_t08_m01_o02"]
    }
    ed_parts["9702_w20_21_q06_b_i"]["skills"] = {
        "primary_skill_id": "9702_skill_stationary_waves",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q06_b_i"]["question_patterns"] = ["definition"]
    ed_parts["9702_w20_21_q06_b_i"]["knowledge_refs"] = {
        "definition_ids": ["9702_def_node"],
        "formula_ids": []
    }

    ed_parts["9702_w20_21_q06_b_ii"]["mapping"] = {
        "primary_topic_id": "9702_t08",
        "primary_module_id": "9702_t08_m01",
        "outcome_ids": ["9702_t08_m01_o03"]
    }
    ed_parts["9702_w20_21_q06_b_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_stationary_waves",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q06_b_ii"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_21_q06_b_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_stationary_wave_spacing"]
    }

    ed_parts["9702_w20_21_q06_b_iii"]["mapping"] = {
        "primary_topic_id": "9702_t08",
        "primary_module_id": "9702_t08_m01",
        "outcome_ids": ["9702_t08_m01_o04"]
    }
    ed_parts["9702_w20_21_q06_b_iii"]["skills"] = {
        "primary_skill_id": "9702_skill_stationary_waves",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q06_b_iii"]["question_patterns"] = ["property_identification"]
    ed_parts["9702_w20_21_q06_b_iii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Deducing phase difference between adjacent antinodes in a stationary wave."
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)

# ==============================================================================
# Q07
# ==============================================================================
def repair_w20_21_q07():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w20_qp_21/question_07.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w20_21_q07.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_7_1",
            "label": "Fig. 7.1",
            "file": "figure_7_1.png",
            "introduced_by": "9702_w20_21_q07_c",
            "referenced_by": ["9702_w20_21_q07_c"],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w20_21_q07_c",
                "anchor": "A cell of electromotive force (e.m.f.) E and internal resistance r is connected to a variable resistor of resistance R, as shown in Fig. 7.1."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w20_21_q07_a"]
    p_a["question_text"] = "Define the ohm."
    p_a["question_text_latex"] = "Define the ohm."
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q07_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q07_a_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Answer",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w20_21_q07_b"]
    p_b["question_text"] = "A uniform wire has resistance 3.2 Ω. The wire has length 2.5 m and is made from metal of resistivity 460 nΩ m.\nCalculate the cross-sectional area of the wire.\ncross-sectional area = m^{2}"
    p_b["question_text_latex"] = "A uniform wire has resistance $3.2\\ \\Omega$. The wire has length $2.5\\text{ m}$ and is made from metal of resistivity $460\\text{ n}\\Omega\\text{ m}$.\nCalculate the cross-sectional area of the wire.\n$$\\text{cross-sectional area} = \\text{.................................................... m}^2$$"
    p_b["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q07_b_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q07_b_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Cross-sectional area",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m}^2"
                        }
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_w20_21_q07_c"]
    p_c["question_text"] = "A cell of electromotive force (e.m.f.) E and internal resistance r is connected to a variable resistor of resistance R, as shown in Fig. 7.1.\nThe current in the circuit is I."
    p_c["question_text_latex"] = "A cell of electromotive force (e.m.f.) $E$ and internal resistance $r$ is connected to a variable resistor of resistance $R$, as shown in Fig. 7.1.\nThe current in the circuit is $I$."

    p_ci = parts_by_id["9702_w20_21_q07_c_i"]
    p_ci["question_text"] = "State, in terms of energy, why the potential difference across the variable resistor is less than the e.m.f. of the cell."
    p_ci["question_text_latex"] = "State, in terms of energy, why the potential difference across the variable resistor is less than the e.m.f. of the cell."
    p_ci["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q07_c_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q07_c_i_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Answer",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_cii = parts_by_id["9702_w20_21_q07_c_ii"]
    p_cii["question_text"] = "State an expression for E in terms of I, R and r.\nE ="
    p_cii["question_text_latex"] = "State an expression for $E$ in terms of $I$, $R$ and $r$.\n$$E = \\text{....................................................}$$"
    p_cii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q07_c_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q07_c_ii_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "E",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_ciii = parts_by_id["9702_w20_21_q07_c_iii"]
    p_ciii["question_text"] = "The resistance R of the variable resistor is changed so that it is equal to r.\nDetermine an expression, in terms of only E and r, for the power P dissipated in the variable resistor.\nP ="
    p_ciii["question_text_latex"] = "The resistance $R$ of the variable resistor is changed so that it is equal to $r$.\nDetermine an expression, in terms of only $E$ and $r$, for the power $P$ dissipated in the variable resistor.\n$$P = \\text{....................................................}$$"
    p_ciii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q07_c_iii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q07_c_iii_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "P",
                        "required": True
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_w20_21_q07_a"]["mapping"] = {
        "primary_topic_id": "9702_t09",
        "primary_module_id": "9702_t09_m03",
        "outcome_ids": ["9702_t09_m03_o01"]
    }
    ed_parts["9702_w20_21_q07_a"]["skills"] = {
        "primary_skill_id": "9702_skill_iv_characteristics",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q07_a"]["question_patterns"] = ["definition"]
    ed_parts["9702_w20_21_q07_a"]["knowledge_refs"] = {
        "definition_ids": ["9702_def_ohm"],
        "formula_ids": ["9702_formula_ohms_law"]
    }

    ed_parts["9702_w20_21_q07_b"]["mapping"] = {
        "primary_topic_id": "9702_t09",
        "primary_module_id": "9702_t09_m03",
        "outcome_ids": ["9702_t09_m03_o06"]
    }
    ed_parts["9702_w20_21_q07_b"]["skills"] = {
        "primary_skill_id": "9702_skill_resistivity",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q07_b"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_21_q07_b"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_resistivity"]
    }

    ed_parts["9702_w20_21_q07_c_i"]["mapping"] = {
        "primary_topic_id": "9702_t10",
        "primary_module_id": "9702_t10_m01",
        "outcome_ids": ["9702_t10_m01_o04"]
    }
    ed_parts["9702_w20_21_q07_c_i"]["skills"] = {
        "primary_skill_id": "9702_skill_emf_internal_resistance",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q07_c_i"]["question_patterns"] = ["explanation"]
    ed_parts["9702_w20_21_q07_c_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Qualitative explanation in terms of energy dissipated in internal resistance."
    }

    ed_parts["9702_w20_21_q07_c_ii"]["mapping"] = {
        "primary_topic_id": "9702_t10",
        "primary_module_id": "9702_t10_m01",
        "outcome_ids": ["9702_t10_m01_o05"]
    }
    ed_parts["9702_w20_21_q07_c_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_emf_internal_resistance",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q07_c_ii"]["question_patterns"] = ["equation_recall"]
    ed_parts["9702_w20_21_q07_c_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_terminal_potential_difference"]
    }

    ed_parts["9702_w20_21_q07_c_iii"]["mapping"] = {
        "primary_topic_id": "9702_t10",
        "primary_module_id": "9702_t10_m01",
        "outcome_ids": ["9702_t10_m01_o05"]
    }
    ed_parts["9702_w20_21_q07_c_iii"]["skills"] = {
        "primary_skill_id": "9702_skill_emf_internal_resistance",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q07_c_iii"]["question_patterns"] = ["equation_derivation"]
    ed_parts["9702_w20_21_q07_c_iii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_electrical_power", "9702_formula_terminal_potential_difference"]
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)

# ==============================================================================
# Q08
# ==============================================================================
def repair_w20_21_q08():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w20_qp_21/question_08.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w20_21_q08.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_8_1",
            "label": "Fig. 8.1",
            "file": "figure_8_1.png",
            "introduced_by": "9702_w20_21_q08_c",
            "referenced_by": ["9702_w20_21_q08_c"],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w20_21_q08_c",
                "anchor": "The nucleus in (b) is moved along a straight line from point A to point B in a uniform horizontal electric field in a vacuum, as shown in Fig. 8.1."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w20_21_q08_a"]
    p_a["question_text"] = "State a similarity and a difference between a down quark and a down antiquark."
    p_a["question_text_latex"] = "State a similarity and a difference between a down quark and a down antiquark."
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q08_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q08_a_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Answer",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w20_21_q08_b"]
    p_b["question_text"] = "For a nucleus of aluminium-25 (^{25}_{13}Al ):"
    p_b["question_text_latex"] = "For a nucleus of aluminium-25 ($^{25}_{13}\\text{Al}$):"

    p_bi = parts_by_id["9702_w20_21_q08_b_i"]
    p_bi["question_text"] = "state the number of protons and the number of neutrons"
    p_bi["question_text_latex"] = "state the number of protons and the number of neutrons"
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q08_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q08_b_i_protons",
                        "control": "number",
                        "role": "answer",
                        "label": "Number of protons",
                        "required": True
                    },
                    {
                        "field_id": "9702_w20_21_q08_b_i_neutrons",
                        "control": "number",
                        "role": "answer",
                        "label": "Number of neutrons",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_w20_21_q08_b_ii"]
    p_bii["question_text"] = "show that the charge is 2.1 × 10^{-18} C."
    p_bii["question_text_latex"] = "show that the charge is $2.1 \\times 10^{-18}\\text{ C}$."
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q08_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q08_b_ii_working",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_w20_21_q08_c"]
    p_c["question_text"] = "The nucleus in (b) is moved along a straight line from point A to point B in a uniform horizontal electric field in a vacuum, as shown in Fig. 8.1.\nThe electric field strength is 11 kV m^{-1}.\nCalculate the work done to move the charge from A to B.\nwork done = J"
    p_c["question_text_latex"] = "The nucleus in (b) is moved along a straight line from point A to point B in a uniform horizontal electric field in a vacuum, as shown in Fig. 8.1.\nThe electric field strength is $11\\text{ kV m}^{-1}$.\nCalculate the work done to move the charge from A to B.\n$$\\text{work done} = \\text{.................................................... J}$$"
    p_c["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_21_q08_c_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_21_q08_c_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Work done",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{J}"
                        }
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_w20_21_q08_a"]["mapping"] = {
        "primary_topic_id": "9702_t11",
        "primary_module_id": "9702_t11_m02",
        "outcome_ids": ["9702_t11_m02_o02"]
    }
    ed_parts["9702_w20_21_q08_a"]["skills"] = {
        "primary_skill_id": "9702_skill_quark_model_hadrons",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q08_a"]["question_patterns"] = ["comparison"]
    ed_parts["9702_w20_21_q08_a"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Qualitative comparison between a down quark and a down antiquark."
    }

    ed_parts["9702_w20_21_q08_b_i"]["mapping"] = {
        "primary_topic_id": "9702_t11",
        "primary_module_id": "9702_t11_m01",
        "outcome_ids": ["9702_t11_m01_o05"]
    }
    ed_parts["9702_w20_21_q08_b_i"]["skills"] = {
        "primary_skill_id": "9702_skill_nuclear_atom_scattering",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q08_b_i"]["question_patterns"] = ["property_identification"]
    ed_parts["9702_w20_21_q08_b_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Deducing proton number and neutron number from standard nuclide notation."
    }

    ed_parts["9702_w20_21_q08_b_ii"]["mapping"] = {
        "primary_topic_id": "9702_t11",
        "primary_module_id": "9702_t11_m01",
        "outcome_ids": ["9702_t11_m01_o02"]
    }
    ed_parts["9702_w20_21_q08_b_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_nuclear_atom_scattering",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q08_b_ii"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_21_q08_b_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Calculating total charge Q = N * e by multiplying proton number by elementary charge."
    }

    ed_parts["9702_w20_21_q08_c"]["mapping"] = {
        "primary_topic_id": "9702_t09",
        "primary_module_id": "9702_t09_m02",
        "outcome_ids": ["9702_t09_m02_o02"]
    }
    ed_parts["9702_w20_21_q08_c"]["skills"] = {
        "primary_skill_id": "9702_skill_uniform_electric_fields",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_21_q08_c"]["question_patterns"] = ["multi_step_calculation"]
    ed_parts["9702_w20_21_q08_c"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_uniform_electric_field_strength", "9702_formula_work"]
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)

def main():
    repair_w20_21_q01()
    repair_w20_21_q02()
    repair_w20_21_q03()
    repair_w20_21_q04()
    repair_w20_21_q05()
    repair_w20_21_q06()
    repair_w20_21_q07()
    repair_w20_21_q08()

if __name__ == "__main__":
    main()
