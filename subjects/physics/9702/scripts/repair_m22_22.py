#!/usr/bin/env python3
"""
scripts/repair_m22_22.py
Repairs all questions and enrichments for 9702_m22_22 (Q01 to Q07).
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
    print("Saved %s" % path.relative_to(ROOT))

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
def repair_m22_22_q01():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_m22_qp_22/question_01.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_m22_22_q01.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["question_stem"] = (
        "A sphere of radius 2.1 mm falls with terminal (constant) velocity through a liquid, as shown in Fig. 1.1.\n"
        "Three forces act on the moving sphere. The weight of the sphere is 7.2 × 10^{-4} N and the upthrust "
        "acting on it is 4.8 × 10^{-4} N. The viscous force F_{V} acting on the sphere is given by\n"
        "F_{V} = krv\n"
        "where r is the radius of the sphere, v is its velocity and k is a constant. The value of k in SI units is 17."
    )
    qd["question_stem_latex"] = (
        "A sphere of radius $2.1\\text{ mm}$ falls with terminal (constant) velocity through a liquid, as shown in Fig. 1.1.\n"
        "Three forces act on the moving sphere. The weight of the sphere is $7.2 \\times 10^{-4}\\text{ N}$ and the upthrust "
        "acting on it is $4.8 \\times 10^{-4}\\text{ N}$. The viscous force $F_V$ acting on the sphere is given by\n"
        "$$F_V = krv$$\n"
        "where $r$ is the radius of the sphere, $v$ is its velocity and $k$ is a constant. The value of $k$ in SI units is 17."
    )

    qd["figures"] = [
        {
            "id": "fig_1_1",
            "label": "Fig. 1.1",
            "file": "figure_1_1.png",
            "introduced_by": "9702_m22_22_q01_c_i",
            "referenced_by": [
                "9702_m22_22_q01_c_i"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "response_background",
                "part_id": "9702_m22_22_q01_c_i",
                "anchor": "On the sphere in Fig. 1.1, draw three arrows to show the directions of the weight W, the upthrust U and the viscous force F_V acting on the sphere."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_m22_22_q01_a"]
    p_a["question_text"] = "Determine the SI base units of k.\nSI base units"
    p_a["question_text_latex"] = "Determine the SI base units of $k$.\n$$\\text{SI base units ....................................................}$$"
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q01_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q01_a_value",
                        "control": "short_text",
                        "role": "answer",
                        "label": "SI base units",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_m22_22_q01_b"]
    p_b["question_text"] = "Use the value of the upthrust acting on the sphere to calculate the density ρ of the liquid.\nρ = kg m^{-3}"
    p_b["question_text_latex"] = "Use the value of the upthrust acting on the sphere to calculate the density $\\rho$ of the liquid.\n$$\\rho = \\text{.................................................... kg m}^{-3}$$"
    p_b["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q01_b_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q01_b_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "ρ",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{kg m}^{-3}"
                        }
                    }
                ]
            }
        ]
    }

    p_ci = parts_by_id["9702_m22_22_q01_c_i"]
    p_ci["question_text"] = "On the sphere in Fig. 1.1, draw three arrows to show the directions of the weight W, the upthrust U and the viscous force F_{V} acting on the sphere."
    p_ci["question_text_latex"] = "On the sphere in Fig. 1.1, draw three arrows to show the directions of the weight $W$, the upthrust $U$ and the viscous force $F_V$ acting on the sphere."
    p_ci["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q01_c_i_canvas",
                "type": "canvas",
                "background_figure_id": "fig_1_1"
            }
        ]
    }

    p_cii = parts_by_id["9702_m22_22_q01_c_ii"]
    p_cii["question_text"] = "Determine the magnitude of the terminal (constant) velocity of the sphere.\nvelocity = m s^{-1}"
    p_cii["question_text_latex"] = "Determine the magnitude of the terminal (constant) velocity of the sphere.\n$$\\text{velocity} = \\text{.................................................... m s}^{-1}$$"
    p_cii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q01_c_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q01_c_ii_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "velocity",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m s}^{-1}"
                        }
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_m22_22_q01_a"]["mapping"] = {
        "primary_topic_id": "9702_t01",
        "primary_module_id": "9702_t01_m02",
        "outcome_ids": ["9702_t01_m02_o02"]
    }
    ed_parts["9702_m22_22_q01_a"]["skills"] = {
        "primary_skill_id": "9702_skill_si_units_homogeneity",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q01_a"]["question_patterns"] = ["equation_derivation"]
    ed_parts["9702_m22_22_q01_a"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_newtons_second_law"]
    }

    ed_parts["9702_m22_22_q01_b"]["mapping"] = {
        "primary_topic_id": "9702_t04",
        "primary_module_id": "9702_t04_m03",
        "outcome_ids": ["9702_t04_m03_o03"]
    }
    ed_parts["9702_m22_22_q01_b"]["skills"] = {
        "primary_skill_id": "9702_skill_upthrust_archimedes",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q01_b"]["question_patterns"] = ["multi_step_calculation"]
    ed_parts["9702_m22_22_q01_b"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_density", "9702_formula_upthrust"]
    }

    ed_parts["9702_m22_22_q01_c_i"]["mapping"] = {
        "primary_topic_id": "9702_t04",
        "primary_module_id": "9702_t04_m02",
        "outcome_ids": ["9702_t04_m02_o02"]
    }
    ed_parts["9702_m22_22_q01_c_i"]["skills"] = {
        "primary_skill_id": "9702_skill_equilibrium_coplanar_forces",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q01_c_i"]["question_patterns"] = ["force_diagram_construction"]
    ed_parts["9702_m22_22_q01_c_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": []
    }

    ed_parts["9702_m22_22_q01_c_ii"]["mapping"] = {
        "primary_topic_id": "9702_t03",
        "primary_module_id": "9702_t03_m02",
        "outcome_ids": ["9702_t03_m02_o01"]
    }
    ed_parts["9702_m22_22_q01_c_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_drag_terminal_velocity",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q01_c_ii"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_m22_22_q01_c_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_newtons_second_law"]
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)


# ==============================================================================
# Q02
# ==============================================================================
def repair_m22_22_q02():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_m22_qp_22/question_02.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_m22_22_q02.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_2_1",
            "label": "Fig. 2.1",
            "file": "figure_2_1.png",
            "introduced_by": "9702_m22_22_q02_a",
            "referenced_by": [
                "9702_m22_22_q02_a",
                "9702_m22_22_q02_e"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_m22_22_q02_a",
                "anchor": "A block is moving along a horizontal surface. Fig. 2.1 shows the variation with time t of the velocity v of the block from t = 0 to t = 6.0 s."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_m22_22_q02_a"]
    p_a["question_text"] = "A block is moving along a horizontal surface. Fig. 2.1 shows the variation with time t of the velocity v of the block from t = 0 to t = 6.0 s.\nUse Fig. 2.1 to determine the acceleration of the block at time t = 4.0 s.\nacceleration = m s^{-2}"
    p_a["question_text_latex"] = "A block is moving along a horizontal surface. Fig. 2.1 shows the variation with time $t$ of the velocity $v$ of the block from $t = 0$ to $t = 6.0\\text{ s}$.\nUse Fig. 2.1 to determine the acceleration of the block at time $t = 4.0\\text{ s}$.\n$$\\text{acceleration} = \\text{.................................................... m s}^{-2}$$"
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q02_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q02_a_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "acceleration",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m s}^{-2}"
                        }
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_m22_22_q02_b"]
    p_b["question_text"] = "State what is represented by the area under the graph from t = 0 to t = 6.0 s."
    p_b["question_text_latex"] = "State what is represented by the area under the graph from $t = 0$ to $t = 6.0\\text{ s}$."
    p_b["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q02_b_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q02_b_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Quantity represented",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_m22_22_q02_c"]
    p_c["question_text"] = "Calculate the distance moved by the block from t = 0 to t = 6.0 s.\ndistance = m"
    p_c["question_text_latex"] = "Calculate the distance moved by the block from $t = 0$ to $t = 6.0\\text{ s}$.\n$$\\text{distance} = \\text{.................................................... m}$$"
    p_c["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q02_c_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q02_c_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "distance",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m}"
                        }
                    }
                ]
            }
        ]
    }

    p_d = parts_by_id["9702_m22_22_q02_d"]
    p_d["question_text"] = "State Newton’s first law of motion."
    p_d["question_text_latex"] = "State Newton’s first law of motion."
    p_d["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q02_d_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q02_d_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Statement",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_e = parts_by_id["9702_m22_22_q02_e"]
    p_e["question_text"] = "A person states that the acceleration of the block from t = 0 to t = 6.0 s is a vector quantity.\nState the feature of the graph in Fig. 2.1 that indicates that the acceleration is in the opposite direction to the velocity."
    p_e["question_text_latex"] = "A person states that the acceleration of the block from $t = 0$ to $t = 6.0\\text{ s}$ is a vector quantity.\nState the feature of the graph in Fig. 2.1 that indicates that the acceleration is in the opposite direction to the velocity."
    p_e["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q02_e_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q02_e_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Explanation",
                        "required": True
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_m22_22_q02_a"]["mapping"] = {
        "primary_topic_id": "9702_t02",
        "primary_module_id": "9702_t02_m01",
        "outcome_ids": ["9702_t02_m01_o03"]
    }
    ed_parts["9702_m22_22_q02_a"]["skills"] = {
        "primary_skill_id": "9702_skill_motion_graphs",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q02_a"]["question_patterns"] = ["direct_calculation", "graph_interpretation"]
    ed_parts["9702_m22_22_q02_a"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_acceleration"]
    }

    ed_parts["9702_m22_22_q02_b"]["mapping"] = {
        "primary_topic_id": "9702_t02",
        "primary_module_id": "9702_t02_m01",
        "outcome_ids": ["9702_t02_m01_o03"]
    }
    ed_parts["9702_m22_22_q02_b"]["skills"] = {
        "primary_skill_id": "9702_skill_motion_graphs",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q02_b"]["question_patterns"] = ["graph_interpretation"]
    ed_parts["9702_m22_22_q02_b"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": []
    }

    ed_parts["9702_m22_22_q02_c"]["mapping"] = {
        "primary_topic_id": "9702_t02",
        "primary_module_id": "9702_t02_m01",
        "outcome_ids": ["9702_t02_m01_o03"]
    }
    ed_parts["9702_m22_22_q02_c"]["skills"] = {
        "primary_skill_id": "9702_skill_motion_graphs",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q02_c"]["question_patterns"] = ["direct_calculation", "graph_interpretation"]
    ed_parts["9702_m22_22_q02_c"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Distance is calculated from the geometric area of the velocity-time graph trapezoid (1/2 * (6.0 + 2.0) * 12 = 48 m) rather than an algebraic kinematic formula."
    }

    ed_parts["9702_m22_22_q02_d"]["mapping"] = {
        "primary_topic_id": "9702_t03",
        "primary_module_id": "9702_t03_m01",
        "outcome_ids": ["9702_t03_m01_o02"]
    }
    ed_parts["9702_m22_22_q02_d"]["skills"] = {
        "primary_skill_id": "9702_skill_newtons_laws",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q02_d"]["question_patterns"] = ["definition"]
    ed_parts["9702_m22_22_q02_d"]["knowledge_refs"] = {
        "definition_ids": ["9702_def_newtons_first_law"],
        "formula_ids": []
    }

    ed_parts["9702_m22_22_q02_e"]["mapping"] = {
        "primary_topic_id": "9702_t02",
        "primary_module_id": "9702_t02_m01",
        "outcome_ids": ["9702_t02_m01_o03"]
    }
    ed_parts["9702_m22_22_q02_e"]["skills"] = {
        "primary_skill_id": "9702_skill_motion_graphs",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q02_e"]["question_patterns"] = ["graph_interpretation", "explanation"]
    ed_parts["9702_m22_22_q02_e"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": []
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)


# ==============================================================================
# Q03
# ==============================================================================
def repair_m22_22_q03():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_m22_qp_22/question_03.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_m22_22_q03.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["question_stem"] = (
        "A solid metal ball of mass 0.18 kg is thrown vertically upwards from the ground with an initial speed of "
        "15 m s^{-1}. The ball moves with constant deceleration."
    )
    qd["question_stem_latex"] = (
        "A solid metal ball of mass $0.18\\text{ kg}$ is thrown vertically upwards from the ground with an initial speed of "
        "$15\\text{ m s}^{-1}$. The ball moves with constant deceleration."
    )

    qd["figures"] = [
        {
            "id": "fig_3_1",
            "label": "Fig. 3.1",
            "file": "figure_3_1.png",
            "introduced_by": "9702_m22_22_q03_d",
            "referenced_by": [
                "9702_m22_22_q03_d"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_m22_22_q03_d",
                "anchor": "The ball was thrown upwards from a point on flat horizontal ground, as shown in Fig. 3.1."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_m22_22_q03_a"]
    p_a["question_text"] = "Determine the maximum height above the ground reached by the ball.\nheight = m"
    p_a["question_text_latex"] = "Determine the maximum height above the ground reached by the ball.\n$$\\text{height} = \\text{.................................................... m}$$"
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q03_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q03_a_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "height",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m}"
                        }
                    }
                ]
            }
        ]
    }

    p_bi = parts_by_id["9702_m22_22_q03_b_i"]
    p_bi["question_text"] = "Calculate the initial momentum of the ball.\nmomentum = N s"
    p_bi["question_text_latex"] = "Calculate the initial momentum of the ball.\n$$\\text{momentum} = \\text{.................................................... N s}$$"
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q03_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q03_b_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "momentum",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{N s}"
                        }
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_m22_22_q03_b_ii"]
    p_bii["question_text"] = "Calculate the rate of change of momentum of the ball as it moves upwards.\nrate of change of momentum = N"
    p_bii["question_text_latex"] = "Calculate the rate of change of momentum of the ball as it moves upwards.\n$$\\text{rate of change of momentum} = \\text{.................................................... N}$$"
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q03_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q03_b_ii_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "rate of change of momentum",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{N}"
                        }
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_m22_22_q03_c"]
    p_c["question_text"] = "State and explain how the principle of conservation of momentum applies to the ball and the Earth as the ball moves upwards."
    p_c["question_text_latex"] = "State and explain how the principle of conservation of momentum applies to the ball and the Earth as the ball moves upwards."
    p_c["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q03_c_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q03_c_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Explanation",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_d = parts_by_id["9702_m22_22_q03_d"]
    p_d["question_text"] = "The ball was thrown upwards from a point on flat horizontal ground, as shown in Fig. 3.1.\nThe ball in its initial position made an angle of 35° with the horizontal ground. The contact area between the ball and the ground was 2.4 × 10^{-4} m^{2}.\nCalculate the average pressure exerted by the ball on the ground in this position.\npressure = Pa"
    p_d["question_text_latex"] = "The ball was thrown upwards from a point on flat horizontal ground, as shown in Fig. 3.1.\nThe ball in its initial position made an angle of $35^\\circ$ with the horizontal ground. The contact area between the ball and the ground was $2.4 \\times 10^{-4}\\text{ m}^2$.\nCalculate the average pressure exerted by the ball on the ground in this position.\n$$\\text{pressure} = \\text{.................................................... Pa}$$"
    p_d["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q03_d_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q03_d_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "pressure",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{Pa}"
                        }
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_m22_22_q03_a"]["mapping"] = {
        "primary_topic_id": "9702_t02",
        "primary_module_id": "9702_t02_m01",
        "outcome_ids": ["9702_t02_m01_o04"]
    }
    ed_parts["9702_m22_22_q03_a"]["skills"] = {
        "primary_skill_id": "9702_skill_kinematics_equations",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q03_a"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_m22_22_q03_a"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_constant_acceleration_velocity_displacement"]
    }

    ed_parts["9702_m22_22_q03_b_i"]["mapping"] = {
        "primary_topic_id": "9702_t03",
        "primary_module_id": "9702_t03_m01",
        "outcome_ids": ["9702_t03_m01_o01"]
    }
    ed_parts["9702_m22_22_q03_b_i"]["skills"] = {
        "primary_skill_id": "9702_skill_newtons_laws",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q03_b_i"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_m22_22_q03_b_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_momentum"]
    }

    ed_parts["9702_m22_22_q03_b_ii"]["mapping"] = {
        "primary_topic_id": "9702_t03",
        "primary_module_id": "9702_t03_m01",
        "outcome_ids": ["9702_t03_m01_o04"]
    }
    ed_parts["9702_m22_22_q03_b_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_newtons_laws",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q03_b_ii"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_m22_22_q03_b_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_force_momentum_rate", "9702_formula_weight"]
    }

    ed_parts["9702_m22_22_q03_c"]["mapping"] = {
        "primary_topic_id": "9702_t03",
        "primary_module_id": "9702_t03_m03",
        "outcome_ids": ["9702_t03_m03_o02"]
    }
    ed_parts["9702_m22_22_q03_c"]["skills"] = {
        "primary_skill_id": "9702_skill_linear_momentum_collisions",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q03_c"]["question_patterns"] = ["explanation"]
    ed_parts["9702_m22_22_q03_c"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": []
    }

    ed_parts["9702_m22_22_q03_d"]["mapping"] = {
        "primary_topic_id": "9702_t04",
        "primary_module_id": "9702_t04_m03",
        "outcome_ids": ["9702_t04_m03_o02"]
    }
    ed_parts["9702_m22_22_q03_d"]["skills"] = {
        "primary_skill_id": "9702_skill_density_pressure",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q03_d"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_m22_22_q03_d"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_pressure_force"]
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)


# ==============================================================================
# Q04
# ==============================================================================
def repair_m22_22_q04():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_m22_qp_22/question_04.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_m22_22_q04.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["question_stem"] = (
        "A child moves down a long slide, as shown in Fig. 4.1.\n"
        "The child moves from rest at the top end X of the slide. An average resistive force of 76 N opposes "
        "the motion of the child as they move to the lower end Y of the slide. The kinetic energy of the child "
        "at Y is 300 J. The decrease in gravitational potential energy of the child as it moves from X to Y is "
        "3200 J."
    )
    qd["question_stem_latex"] = (
        "A child moves down a long slide, as shown in Fig. 4.1.\n"
        "The child moves from rest at the top end X of the slide. An average resistive force of $76\\text{ N}$ opposes "
        "the motion of the child as they move to the lower end Y of the slide. The kinetic energy of the child "
        "at Y is $300\\text{ J}$. The decrease in gravitational potential energy of the child as it moves from X to Y is "
        "$3200\\text{ J}$."
    )

    qd["figures"] = [
        {
            "id": "fig_4_1",
            "label": "Fig. 4.1",
            "file": "figure_4_1.png",
            "introduced_by": None,
            "referenced_by": [],
            "mapping_method": "caption_proximity",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "question",
                "position": "after_stem_text",
                "anchor": "Fig. 4.1"
            }
        },
        {
            "id": "fig_4_2",
            "label": "Fig. 4.2",
            "file": "figure_4_2.png",
            "introduced_by": "9702_m22_22_q04_d",
            "referenced_by": [
                "9702_m22_22_q04_d"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_m22_22_q04_d",
                "anchor": "At end Y of the slide, the child is brought to rest by a board, as shown in Fig. 4.2."
            }
        },
        {
            "id": "fig_4_3",
            "label": "Fig. 4.3",
            "file": "figure_4_3.png",
            "introduced_by": "9702_m22_22_q04_d_iii",
            "referenced_by": [
                "9702_m22_22_q04_d_iii"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "response_background",
                "part_id": "9702_m22_22_q04_d_iii",
                "anchor": "The maximum compression of the spring is x_{0}. On Fig. 4.3, sketch a graph to show the variation of the elastic potential energy of the spring with its compression x from x = 0 to x = x_{0}. Numerical values are not required."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_m22_22_q04_a"]
    p_a["question_text"] = "Determine the ratio
(kinetic energy of the child at Y when the resistive force is 76 N) / (kinetic energy of the child at Y if there is no resistive force).
ratio ="
    p_a["question_text_latex"] = "Determine the ratio\n$$\\frac{\\text{kinetic energy of the child at Y when the resistive force is } 76\\text{ N}}{\\text{kinetic energy of the child at Y if there is no resistive force}}$$\n$$\\text{ratio} = \\text{....................................................}$$"
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q04_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q04_a_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "ratio",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_m22_22_q04_b"]
    p_b["question_text"] = "Use the answer in (a) to calculate the ratio
(speed of the child at Y when the resistive force is 76 N) / (speed of the child at Y if there is no resistive force).
ratio ="
    p_b["question_text_latex"] = "Use the answer in (a) to calculate the ratio\n$$\\frac{\\text{speed of the child at Y when the resistive force is } 76\\text{ N}}{\\text{speed of the child at Y if there is no resistive force}}$$\n$$\\text{ratio} = \\text{....................................................}$$"
    p_b["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q04_b_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q04_b_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "ratio",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_m22_22_q04_c"]
    p_c["question_text"] = "Calculate the length of the slide from X to Y.\nlength = m"
    p_c["question_text_latex"] = "Calculate the length of the slide from X to Y.\n$$\\text{length} = \\text{.................................................... m}$$"
    p_c["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q04_c_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q04_c_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "length",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m}"
                        }
                    }
                ]
            }
        ]
    }

    p_d = parts_by_id["9702_m22_22_q04_d"]
    p_d["question_text"] = (
        "At end Y of the slide, the child is brought to rest by a board, as shown in Fig. 4.2.\n"
        "A spring connects the board to a fixed point. The spring obeys Hooke’s law and has a spring "
        "constant of 63 N m^{-1}. The child hits the board so that it moves to the right and compresses the "
        "spring. The speed of the child becomes zero when the elastic potential energy of the spring "
        "has increased to its maximum value of 140 J."
    )
    p_d["question_text_latex"] = (
        "At end Y of the slide, the child is brought to rest by a board, as shown in Fig. 4.2.\n"
        "A spring connects the board to a fixed point. The spring obeys Hooke’s law and has a spring "
        "constant of $63\\text{ N m}^{-1}$. The child hits the board so that it moves to the right and compresses the "
        "spring. The speed of the child becomes zero when the elastic potential energy of the spring "
        "has increased to its maximum value of $140\\text{ J}$."
    )

    p_di = parts_by_id["9702_m22_22_q04_d_i"]
    p_di["question_text"] = "Calculate the maximum compression of the spring.\nmaximum compression = m"
    p_di["question_text_latex"] = "Calculate the maximum compression of the spring.\n$$\\text{maximum compression} = \\text{.................................................... m}$$"
    p_di["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q04_d_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q04_d_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "maximum compression",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m}"
                        }
                    }
                ]
            }
        ]
    }

    p_dii = parts_by_id["9702_m22_22_q04_d_ii"]
    p_dii["question_text"] = "Calculate the percentage efficiency of the transfer of the kinetic energy of the child to the elastic potential energy of the spring.\npercentage efficiency = %"
    p_dii["question_text_latex"] = "Calculate the percentage efficiency of the transfer of the kinetic energy of the child to the elastic potential energy of the spring.\n$$\\text{percentage efficiency} = \\text{.................................................... \\%}$$"
    p_dii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q04_d_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q04_d_ii_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "percentage efficiency",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\%"
                        }
                    }
                ]
            }
        ]
    }

    p_diii = parts_by_id["9702_m22_22_q04_d_iii"]
    p_diii["question_text"] = "The maximum compression of the spring is x_{0}. On Fig. 4.3, sketch a graph to show the variation of the elastic potential energy of the spring with its compression x from x = 0 to x = x_{0}. Numerical values are not required."
    p_diii["question_text_latex"] = "The maximum compression of the spring is $x_0$. On Fig. 4.3, sketch a graph to show the variation of the elastic potential energy of the spring with its compression $x$ from $x = 0$ to $x = x_0$. Numerical values are not required."
    p_diii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q04_d_iii_canvas",
                "type": "canvas",
                "background_figure_id": "fig_4_3"
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_m22_22_q04_a"]["mapping"] = {
        "primary_topic_id": "9702_t05",
        "primary_module_id": "9702_t05_m01",
        "outcome_ids": ["9702_t05_m01_o02"]
    }
    ed_parts["9702_m22_22_q04_a"]["skills"] = {
        "primary_skill_id": "9702_skill_conservation_of_energy",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q04_a"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_m22_22_q04_a"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "The ratio is determined directly from the stated kinetic energy and gravitational potential energy decrease using energy conservation without an additional formula."
    }

    ed_parts["9702_m22_22_q04_b"]["mapping"] = {
        "primary_topic_id": "9702_t05",
        "primary_module_id": "9702_t05_m02",
        "outcome_ids": ["9702_t05_m02_o04"]
    }
    ed_parts["9702_m22_22_q04_b"]["skills"] = {
        "primary_skill_id": "9702_skill_kinetic_potential_energy",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q04_b"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_m22_22_q04_b"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_kinetic_energy"]
    }

    ed_parts["9702_m22_22_q04_c"]["mapping"] = {
        "primary_topic_id": "9702_t05",
        "primary_module_id": "9702_t05_m01",
        "outcome_ids": ["9702_t05_m01_o01"]
    }
    ed_parts["9702_m22_22_q04_c"]["skills"] = {
        "primary_skill_id": "9702_skill_work_done",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q04_c"]["question_patterns"] = ["multi_step_calculation"]
    ed_parts["9702_m22_22_q04_c"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_work"]
    }

    ed_parts["9702_m22_22_q04_d_i"]["mapping"] = {
        "primary_topic_id": "9702_t06",
        "primary_module_id": "9702_t06_m02",
        "outcome_ids": ["9702_t06_m02_o04"]
    }
    ed_parts["9702_m22_22_q04_d_i"]["skills"] = {
        "primary_skill_id": "9702_skill_hookes_law_elastic_energy",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q04_d_i"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_m22_22_q04_d_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_elastic_potential_energy"]
    }

    ed_parts["9702_m22_22_q04_d_ii"]["mapping"] = {
        "primary_topic_id": "9702_t05",
        "primary_module_id": "9702_t05_m01",
        "outcome_ids": ["9702_t05_m01_o04"]
    }
    ed_parts["9702_m22_22_q04_d_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_power_efficiency",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q04_d_ii"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_m22_22_q04_d_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_efficiency"]
    }

    ed_parts["9702_m22_22_q04_d_iii"]["mapping"] = {
        "primary_topic_id": "9702_t06",
        "primary_module_id": "9702_t06_m02",
        "outcome_ids": ["9702_t06_m02_o04"]
    }
    ed_parts["9702_m22_22_q04_d_iii"]["skills"] = {
        "primary_skill_id": "9702_skill_hookes_law_elastic_energy",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q04_d_iii"]["question_patterns"] = ["graph_construction"]
    ed_parts["9702_m22_22_q04_d_iii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_elastic_potential_energy"]
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)


# ==============================================================================
# Q05
# ==============================================================================
def repair_m22_22_q05():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_m22_qp_22/question_05.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_m22_22_q05.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_5_1",
            "label": "Fig. 5.1",
            "file": "figure_5_1.png",
            "introduced_by": "9702_m22_22_q05_c",
            "referenced_by": [
                "9702_m22_22_q05_c",
                "9702_m22_22_q05_c_ii"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_m22_22_q05_c",
                "anchor": "A beam of vertically polarised monochromatic light is incident normally on a polarising filter, as shown in Fig. 5.1."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_ai = parts_by_id["9702_m22_22_q05_a_i"]
    p_ai["question_text"] = "State the conditions required for the formation of a stationary wave."
    p_ai["question_text_latex"] = "State the conditions required for the formation of a stationary wave."
    p_ai["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q05_a_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q05_a_i_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Conditions",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_aii = parts_by_id["9702_m22_22_q05_a_ii"]
    p_aii["question_text"] = "State the phase difference between any two vibrating particles in a stationary wave between two adjacent nodes."
    p_aii["question_text_latex"] = "State the phase difference between any two vibrating particles in a stationary wave between two adjacent nodes."
    p_aii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q05_a_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q05_a_ii_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Phase difference",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_m22_22_q05_b"]
    p_b["question_text"] = "A motorcycle is travelling at 13.0 m s^{-1} along a straight road. The rider of the motorcycle sees a pedestrian standing ahead of him on the road and sounds the motorcycle horn.
The horn emits sound of frequency 543 Hz. The speed of sound in the air is 334 m s^{-1}."
    p_b["question_text_latex"] = "A motorcycle is travelling at $13.0\text{ m s}^{-1}$ along a straight road. The rider of the motorcycle sees a pedestrian standing ahead of him on the road and sounds the motorcycle horn.
The horn emits sound of frequency $543\text{ Hz}$. The speed of sound in the air is $334\text{ m s}^{-1}$."

    p_bi = parts_by_id["9702_m22_22_q05_b_i"]
    p_bi["question_text"] = "Calculate the frequency, to three significant figures, of the sound heard by the pedestrian.
frequency = Hz"
    p_bi["question_text_latex"] = "Calculate the frequency, to three significant figures, of the sound heard by the pedestrian.
$$\text{frequency} = \text{.................................................... Hz}$$"
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q05_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q05_b_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "frequency",
                        "required": True,
                        "unit": {
                            "unit_latex": "\text{Hz}"
                        }
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_m22_22_q05_b_ii"]
    p_bii["question_text"] = "The motorcycle rider passes the stationary pedestrian and then moves directly away from her. As the motorcycle moves away, the sound heard by the pedestrian decreases in frequency.
State what happens, if anything, to the speed of the motorcycle as it moves away from the pedestrian."
    p_bii["question_text_latex"] = "The motorcycle rider passes the stationary pedestrian and then moves directly away from her. As the motorcycle moves away, the sound heard by the pedestrian decreases in frequency.
State what happens, if anything, to the speed of the motorcycle as it moves away from the pedestrian."
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q05_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q05_b_ii_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Speed of motorcycle",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_m22_22_q05_c"]
    p_c["question_text"] = "A beam of vertically polarised monochromatic light is incident normally on a polarising filter, as shown in Fig. 5.1.
The intensity of the incident light is I_{0}. The filter is initially positioned so that its transmission axis makes an angle of 20° with the vertical.
The intensity of the transmitted light is I_{T}."
    p_c["question_text_latex"] = "A beam of vertically polarised monochromatic light is incident normally on a polarising filter, as shown in Fig. 5.1.
The intensity of the incident light is $I_0$. The filter is initially positioned so that its transmission axis makes an angle of $20^\circ$ with the vertical.
The intensity of the transmitted light is $I_T$."

    p_ci = parts_by_id["9702_m22_22_q05_c_i"]
    p_ci["question_text"] = "By considering the ratio I_{T} / I_{0}, calculate the ratio (amplitude of transmitted light) / (amplitude of incident light).
ratio ="
    p_ci["question_text_latex"] = "By considering the ratio $I_T / I_0$, calculate the ratio
$$\frac{\text{amplitude of transmitted light}}{\text{amplitude of incident light}}$$
$$\text{ratio} = \text{....................................................}$$"
    p_ci["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q05_c_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q05_c_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "ratio",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_cii = parts_by_id["9702_m22_22_q05_c_ii"]
    p_cii["question_text"] = "The filter is now rotated, about the direction of the light beam, from its starting position shown in Fig. 5.1 through an angle θ.
The intensity of the transmitted light decreases to 0.59 I_{0}.
Calculate a possible value of θ.
θ = °"
    p_cii["question_text_latex"] = "The filter is now rotated, about the direction of the light beam, from its starting position shown in Fig. 5.1 through an angle $\theta$.
The intensity of the transmitted light decreases to $0.59 I_0$.
Calculate a possible value of $\theta$.
$$\theta = \text{....................................................}^\circ$$"
    p_cii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q05_c_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q05_c_ii_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "θ",
                        "required": True,
                        "unit": {
                            "unit_latex": "^\circ"
                        }
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_m22_22_q05_a_i"]["mapping"] = {
        "primary_topic_id": "9702_t08",
        "primary_module_id": "9702_t08_m01",
        "outcome_ids": ["9702_t08_m01_o03"]
    }
    ed_parts["9702_m22_22_q05_a_i"]["skills"] = {
        "primary_skill_id": "9702_skill_stationary_waves",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q05_a_i"]["question_patterns"] = ["explanation"]
    ed_parts["9702_m22_22_q05_a_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": []
    }

    ed_parts["9702_m22_22_q05_a_ii"]["mapping"] = {
        "primary_topic_id": "9702_t08",
        "primary_module_id": "9702_t08_m01",
        "outcome_ids": ["9702_t08_m01_o03"]
    }
    ed_parts["9702_m22_22_q05_a_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_stationary_waves",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q05_a_ii"]["question_patterns"] = ["property_identification"]
    ed_parts["9702_m22_22_q05_a_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": []
    }

    ed_parts["9702_m22_22_q05_b_i"]["mapping"] = {
        "primary_topic_id": "9702_t07",
        "primary_module_id": "9702_t07_m03",
        "outcome_ids": ["9702_t07_m03_o02"]
    }
    ed_parts["9702_m22_22_q05_b_i"]["skills"] = {
        "primary_skill_id": "9702_skill_doppler_effect",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q05_b_i"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_m22_22_q05_b_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_doppler_moving_source"]
    }

    ed_parts["9702_m22_22_q05_b_ii"]["mapping"] = {
        "primary_topic_id": "9702_t07",
        "primary_module_id": "9702_t07_m03",
        "outcome_ids": ["9702_t07_m03_o01"]
    }
    ed_parts["9702_m22_22_q05_b_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_doppler_effect",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q05_b_ii"]["question_patterns"] = ["property_identification"]
    ed_parts["9702_m22_22_q05_b_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": []
    }

    ed_parts["9702_m22_22_q05_c_i"]["mapping"] = {
        "primary_topic_id": "9702_t07",
        "primary_module_id": "9702_t07_m05",
        "outcome_ids": ["9702_t07_m05_o02"]
    }
    ed_parts["9702_m22_22_q05_c_i"]["skills"] = {
        "primary_skill_id": "9702_skill_polarisation_malus_law",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q05_c_i"]["question_patterns"] = ["multi_step_calculation"]
    ed_parts["9702_m22_22_q05_c_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_malus_law", "9702_formula_wave_intensity_amplitude"]
    }

    ed_parts["9702_m22_22_q05_c_ii"]["mapping"] = {
        "primary_topic_id": "9702_t07",
        "primary_module_id": "9702_t07_m05",
        "outcome_ids": ["9702_t07_m05_o02"]
    }
    ed_parts["9702_m22_22_q05_c_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_polarisation_malus_law",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q05_c_ii"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_m22_22_q05_c_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_malus_law"]
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)


# ==============================================================================
# Q06
# ==============================================================================
def repair_m22_22_q06():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_m22_qp_22/question_06.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_m22_22_q06.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["question_stem"] = (
        "The ends of a metal resistance wire are connected to a battery of electromotive force (e.m.f.) 8.0 V "
        "and negligible internal resistance, as shown in Fig. 6.1.\n"
        "The power dissipated by the resistance wire is 36 W."
    )
    qd["question_stem_latex"] = (
        "The ends of a metal resistance wire are connected to a battery of electromotive force (e.m.f.) $8.0\\text{ V}$ "
        "and negligible internal resistance, as shown in Fig. 6.1.\n"
        "The power dissipated by the resistance wire is $36\\text{ W}$."
    )

    qd["figures"] = [
        {
            "id": "fig_6_1",
            "label": "Fig. 6.1",
            "file": "figure_6_1.png",
            "introduced_by": None,
            "referenced_by": [
                "9702_m22_22_q06_c",
                "9702_m22_22_q06_d"
            ],
            "mapping_method": "caption_proximity",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "question",
                "position": "after_stem_text",
                "anchor": "Fig. 6.1"
            }
        },
        {
            "id": "fig_6_2",
            "label": "Fig. 6.2",
            "file": "figure_6_2.png",
            "introduced_by": "9702_m22_22_q06_d",
            "referenced_by": [
                "9702_m22_22_q06_d"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_m22_22_q06_d",
                "anchor": "The circuit shown in Fig. 6.1 is modified by connecting a second battery, of e.m.f. 8.0 V and negligible internal resistance, in parallel with the original battery and the original resistance wire, as shown in Fig. 6.2."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_ai = parts_by_id["9702_m22_22_q06_a_i"]
    p_ai["question_text"] = "the current in the resistance wire\ncurrent = A"
    p_ai["question_text_latex"] = "the current in the resistance wire\n$$\\text{current} = \\text{.................................................... A}$$"
    p_ai["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q06_a_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q06_a_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "current",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{A}"
                        }
                    }
                ]
            }
        ]
    }

    p_aii = parts_by_id["9702_m22_22_q06_a_ii"]
    p_aii["question_text"] = "the number of free electrons that pass through the resistance wire in a time of 50 s\nnumber ="
    p_aii["question_text_latex"] = "the number of free electrons that pass through the resistance wire in a time of $50\\text{ s}$\n$$\\text{number} = \\text{....................................................}$$"
    p_aii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q06_a_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q06_a_ii_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "number",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_aiii = parts_by_id["9702_m22_22_q06_a_iii"]
    p_aiii["question_text"] = "the resistance of the wire.\nresistance = Ω"
    p_aiii["question_text_latex"] = "the resistance of the wire.\n$$\\text{resistance} = \\text{.................................................... }\\Omega$$"
    p_aiii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q06_a_iii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q06_a_iii_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "resistance",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\Omega"
                        }
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_m22_22_q06_b"]
    p_b["question_text"] = "The metal of the resistance wire in the circuit has a resistivity of 1.4 × 10^{-6} Ω m. The cross-sectional area of the wire is 0.25 mm^{2}.\nCalculate the length of the wire.\nlength = m"
    p_b["question_text_latex"] = "The metal of the resistance wire in the circuit has a resistivity of $1.4 \\times 10^{-6}\\text{ }\\Omega\\text{ m}$. The cross-sectional area of the wire is $0.25\\text{ mm}^2$.\nCalculate the length of the wire.\n$$\\text{length} = \\text{.................................................... m}$$"
    p_b["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q06_b_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q06_b_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "length",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m}"
                        }
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_m22_22_q06_c"]
    p_c["question_text"] = "The circuit shown in Fig. 6.1 is modified by replacing the original resistance wire with a second resistance wire.\nThe second wire is made of the same metal and has the same length as the original wire, but has a larger cross-sectional area.\nState and explain whether the power dissipated by the second wire is less than, the same as, or greater than the power dissipated by the original wire."
    p_c["question_text_latex"] = "The circuit shown in Fig. 6.1 is modified by replacing the original resistance wire with a second resistance wire.\nThe second wire is made of the same metal and has the same length as the original wire, but has a larger cross-sectional area.\nState and explain whether the power dissipated by the second wire is less than, the same as, or greater than the power dissipated by the original wire."
    p_c["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q06_c_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q06_c_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Explanation",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_d = parts_by_id["9702_m22_22_q06_d"]
    p_d["question_text"] = "The circuit shown in Fig. 6.1 is modified by connecting a second battery, of e.m.f. 8.0 V and negligible internal resistance, in parallel with the original battery and the original resistance wire, as shown in Fig. 6.2.\nBy reference to the current in the resistance wire, state and explain whether the addition of the second battery causes the power in the original resistance wire to decrease, increase or stay the same."
    p_d["question_text_latex"] = "The circuit shown in Fig. 6.1 is modified by connecting a second battery, of e.m.f. $8.0\\text{ V}$ and negligible internal resistance, in parallel with the original battery and the original resistance wire, as shown in Fig. 6.2.\nBy reference to the current in the resistance wire, state and explain whether the addition of the second battery causes the power in the original resistance wire to decrease, increase or stay the same."
    p_d["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q06_d_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q06_d_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Explanation",
                        "required": True
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_m22_22_q06_a_i"]["mapping"] = {
        "primary_topic_id": "9702_t09",
        "primary_module_id": "9702_t09_m02",
        "outcome_ids": ["9702_t09_m02_o03"]
    }
    ed_parts["9702_m22_22_q06_a_i"]["skills"] = {
        "primary_skill_id": "9702_skill_potential_difference_power",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q06_a_i"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_m22_22_q06_a_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_electrical_power"]
    }

    ed_parts["9702_m22_22_q06_a_ii"]["mapping"] = {
        "primary_topic_id": "9702_t09",
        "primary_module_id": "9702_t09_m01",
        "outcome_ids": ["9702_t09_m01_o01", "9702_t09_m01_o02"]
    }
    ed_parts["9702_m22_22_q06_a_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_electric_current_drift_speed",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q06_a_ii"]["question_patterns"] = ["multi_step_calculation"]
    ed_parts["9702_m22_22_q06_a_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_charge_current_time", "9702_formula_charge_quantisation"]
    }

    ed_parts["9702_m22_22_q06_a_iii"]["mapping"] = {
        "primary_topic_id": "9702_t09",
        "primary_module_id": "9702_t09_m02",
        "outcome_ids": ["9702_t09_m02_o03"]
    }
    ed_parts["9702_m22_22_q06_a_iii"]["skills"] = {
        "primary_skill_id": "9702_skill_potential_difference_power",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q06_a_iii"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_m22_22_q06_a_iii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_electrical_power", "9702_formula_ohms_law"]
    }

    ed_parts["9702_m22_22_q06_b"]["mapping"] = {
        "primary_topic_id": "9702_t09",
        "primary_module_id": "9702_t09_m03",
        "outcome_ids": ["9702_t09_m03_o06"]
    }
    ed_parts["9702_m22_22_q06_b"]["skills"] = {
        "primary_skill_id": "9702_skill_resistivity",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q06_b"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_m22_22_q06_b"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_resistivity"]
    }

    ed_parts["9702_m22_22_q06_c"]["mapping"] = {
        "primary_topic_id": "9702_t09",
        "primary_module_id": "9702_t09_m03",
        "outcome_ids": ["9702_t09_m03_o06"]
    }
    ed_parts["9702_m22_22_q06_c"]["skills"] = {
        "primary_skill_id": "9702_skill_resistivity",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q06_c"]["question_patterns"] = ["explanation", "comparison"]
    ed_parts["9702_m22_22_q06_c"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_resistivity", "9702_formula_electrical_power"]
    }

    ed_parts["9702_m22_22_q06_d"]["mapping"] = {
        "primary_topic_id": "9702_t10",
        "primary_module_id": "9702_t10_m01",
        "outcome_ids": ["9702_t10_m01_o02"]
    }
    ed_parts["9702_m22_22_q06_d"]["skills"] = {
        "primary_skill_id": "9702_skill_emf_internal_resistance",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q06_d"]["question_patterns"] = ["circuit_analysis", "explanation"]
    ed_parts["9702_m22_22_q06_d"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_electrical_power"]
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)


# ==============================================================================
# Q07
# ==============================================================================
def repair_m22_22_q07():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_m22_qp_22/question_07.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_m22_22_q07.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_m22_22_q07_a"]
    p_a["question_text"] = "A nucleus of sodium-22 (^{22}_{11}Na) decays by emitting a β^{+} particle. A different nucleus is formed by the decay."
    p_a["question_text_latex"] = "A nucleus of sodium-22 ($^{22}_{11}\\text{Na}$) decays by emitting a $\\beta^+$ particle. A different nucleus is formed by the decay."

    p_ai = parts_by_id["9702_m22_22_q07_a_i"]
    p_ai["question_text"] = "State the name of another lepton that is produced by the decay."
    p_ai["question_text_latex"] = "State the name of another lepton that is produced by the decay."
    p_ai["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q07_a_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q07_a_i_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Lepton",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_aii = parts_by_id["9702_m22_22_q07_a_ii"]
    p_aii["question_text"] = "Determine the nucleon number and the proton number of the nucleus that is formed by the decay.\nnucleon number =\nproton number ="
    p_aii["question_text_latex"] = "Determine the nucleon number and the proton number of the nucleus that is formed by the decay.\n$$\\text{nucleon number} = \\text{....................................................}$$\n$$\\text{proton number} = \\text{....................................................}$$"
    p_aii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q07_a_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q07_a_ii_nucleon_number",
                        "control": "short_text",
                        "role": "answer",
                        "label": "nucleon number",
                        "required": True
                    },
                    {
                        "field_id": "9702_m22_22_q07_a_ii_proton_number",
                        "control": "short_text",
                        "role": "answer",
                        "label": "proton number",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_aiii = parts_by_id["9702_m22_22_q07_a_iii"]
    p_aiii["question_text"] = "The quark composition of a nucleon in the sodium-22 nucleus is changed during the decay.\nDescribe the change to the quark composition of the nucleon."
    p_aiii["question_text_latex"] = "The quark composition of a nucleon in the sodium-22 nucleus is changed during the decay.\nDescribe the change to the quark composition of the nucleon."
    p_aiii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q07_a_iii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q07_a_iii_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Quark change",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_m22_22_q07_b"]
    p_b["question_text"] = "A baryon consists of quarks that are the same flavour (type). The charge of the baryon is –2e, where e is the elementary charge."
    p_b["question_text_latex"] = "A baryon consists of quarks that are the same flavour (type). The charge of the baryon is –2e, where e is the elementary charge."

    p_bi = parts_by_id["9702_m22_22_q07_b_i"]
    p_bi["question_text"] = "Calculate, in terms of e, the charge of each quark.\ncharge = e"
    p_bi["question_text_latex"] = "Calculate, in terms of $e$, the charge of each quark.\n$$\\text{charge} = \\text{.................................................... } e$$"
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q07_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q07_b_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "charge",
                        "required": True,
                        "unit": {
                            "unit_latex": "e"
                        }
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_m22_22_q07_b_ii"]
    p_bii["question_text"] = "State a possible flavour (type) of the quarks."
    p_bii["question_text_latex"] = "State a possible flavour (type) of the quarks."
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_m22_22_q07_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_m22_22_q07_b_ii_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Flavour",
                        "required": True
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_m22_22_q07_a_i"]["mapping"] = {
        "primary_topic_id": "9702_t11",
        "primary_module_id": "9702_t11_m01",
        "outcome_ids": ["9702_t11_m01_o09"]
    }
    ed_parts["9702_m22_22_q07_a_i"]["skills"] = {
        "primary_skill_id": "9702_skill_nuclear_decay_equations",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q07_a_i"]["question_patterns"] = ["property_identification"]
    ed_parts["9702_m22_22_q07_a_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": []
    }

    ed_parts["9702_m22_22_q07_a_ii"]["mapping"] = {
        "primary_topic_id": "9702_t11",
        "primary_module_id": "9702_t11_m01",
        "outcome_ids": ["9702_t11_m01_o06"]
    }
    ed_parts["9702_m22_22_q07_a_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_nuclear_decay_equations",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q07_a_ii"]["question_patterns"] = ["equation_completion"]
    ed_parts["9702_m22_22_q07_a_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": []
    }

    ed_parts["9702_m22_22_q07_a_iii"]["mapping"] = {
        "primary_topic_id": "9702_t11",
        "primary_module_id": "9702_t11_m02",
        "outcome_ids": ["9702_t11_m02_o05"]
    }
    ed_parts["9702_m22_22_q07_a_iii"]["skills"] = {
        "primary_skill_id": "9702_skill_fundamental_particles_interactions",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q07_a_iii"]["question_patterns"] = ["particle_model_application"]
    ed_parts["9702_m22_22_q07_a_iii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": []
    }

    ed_parts["9702_m22_22_q07_b_i"]["mapping"] = {
        "primary_topic_id": "9702_t11",
        "primary_module_id": "9702_t11_m02",
        "outcome_ids": ["9702_t11_m02_o02"]
    }
    ed_parts["9702_m22_22_q07_b_i"]["skills"] = {
        "primary_skill_id": "9702_skill_quark_model_hadrons",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q07_b_i"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_m22_22_q07_b_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "The charge of each identical constituent quark is calculated by dividing the total baryon charge -2e equally between the three quarks (-2e / 3 = -2/3 e)."
    }

    ed_parts["9702_m22_22_q07_b_ii"]["mapping"] = {
        "primary_topic_id": "9702_t11",
        "primary_module_id": "9702_t11_m02",
        "outcome_ids": ["9702_t11_m02_o02"]
    }
    ed_parts["9702_m22_22_q07_b_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_quark_model_hadrons",
        "supporting_skill_ids": []
    }
    ed_parts["9702_m22_22_q07_b_ii"]["question_patterns"] = ["classification"]
    ed_parts["9702_m22_22_q07_b_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": []
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)


def main():
    repair_m22_22_q01()
    repair_m22_22_q02()
    repair_m22_22_q03()
    repair_m22_22_q04()
    repair_m22_22_q05()
    repair_m22_22_q06()
    repair_m22_22_q07()
    print("Repaired 9702_m22_22 successfully.")

if __name__ == "__main__":
    main()
