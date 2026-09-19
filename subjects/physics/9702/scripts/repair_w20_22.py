#!/usr/bin/env python3
"""
scripts/repair_w20_22.py
Repairs all questions and enrichments for 9702_w20_22 (Q01 to Q07).
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
def repair_w20_22_q01():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w20_qp_22/question_01.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w20_22_q01.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_1_1",
            "label": "Fig. 1.1",
            "file": "figure_1_1.png",
            "introduced_by": "9702_w20_22_q01_b",
            "referenced_by": ["9702_w20_22_q01_b"],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w20_22_q01_b",
                "anchor": "A toy train moves along a straight section of track. Fig. 1.1 shows the variation with time t of the distance d moved by the train."
            }
        },
        {
            "id": "fig_1_2",
            "label": "Fig. 1.2",
            "file": "figure_1_2.png",
            "introduced_by": "9702_w20_22_q01_c",
            "referenced_by": ["9702_w20_22_q01_c"],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w20_22_q01_c",
                "anchor": "The straight section of track in (b) is part of the loop of track shown in Fig. 1.2."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w20_22_q01_a"]
    p_a["question_text"] = "Complete Table 1.1 by putting a tick (✓) in the appropriate column to indicate whether the listed quantities are scalars or vectors."
    p_a["question_text_latex"] = "Complete Table 1.1 by putting a tick (✓) in the appropriate column to indicate whether the listed quantities are scalars or vectors."
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q01_a_table",
                "type": "table",
                "columns": [
                    {
                        "column_id": "quantity",
                        "label": "quantity"
                    },
                    {
                        "column_id": "scalar",
                        "label": "scalar"
                    },
                    {
                        "column_id": "vector",
                        "label": "vector"
                    }
                ],
                "rows": [
                    {
                        "row_id": "acceleration",
                        "cells": [
                            {"column_id": "quantity", "type": "static", "value": "acceleration"},
                            {"column_id": "scalar", "type": "editable", "field": {"field_id": "9702_w20_22_q01_a_acc_scalar", "control": "single_choice", "role": "selection", "required": False, "options": ["tick"]}},
                            {"column_id": "vector", "type": "editable", "field": {"field_id": "9702_w20_22_q01_a_acc_vector", "control": "single_choice", "role": "selection", "required": False, "options": ["tick"]}}
                        ]
                    },
                    {
                        "row_id": "density",
                        "cells": [
                            {"column_id": "quantity", "type": "static", "value": "density"},
                            {"column_id": "scalar", "type": "editable", "field": {"field_id": "9702_w20_22_q01_a_den_scalar", "control": "single_choice", "role": "selection", "required": False, "options": ["tick"]}},
                            {"column_id": "vector", "type": "editable", "field": {"field_id": "9702_w20_22_q01_a_den_vector", "control": "single_choice", "role": "selection", "required": False, "options": ["tick"]}}
                        ]
                    },
                    {
                        "row_id": "temperature",
                        "cells": [
                            {"column_id": "quantity", "type": "static", "value": "temperature"},
                            {"column_id": "scalar", "type": "editable", "field": {"field_id": "9702_w20_22_q01_a_temp_scalar", "control": "single_choice", "role": "selection", "required": False, "options": ["tick"]}},
                            {"column_id": "vector", "type": "editable", "field": {"field_id": "9702_w20_22_q01_a_temp_vector", "control": "single_choice", "role": "selection", "required": False, "options": ["tick"]}}
                        ]
                    },
                    {
                        "row_id": "momentum",
                        "cells": [
                            {"column_id": "quantity", "type": "static", "value": "momentum"},
                            {"column_id": "scalar", "type": "editable", "field": {"field_id": "9702_w20_22_q01_a_mom_scalar", "control": "single_choice", "role": "selection", "required": False, "options": ["tick"]}},
                            {"column_id": "vector", "type": "editable", "field": {"field_id": "9702_w20_22_q01_a_mom_vector", "control": "single_choice", "role": "selection", "required": False, "options": ["tick"]}}
                        ]
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w20_22_q01_b"]
    p_b["question_text"] = "A toy train moves along a straight section of track. Fig. 1.1 shows the variation with time t of the distance d moved by the train."
    p_b["question_text_latex"] = "A toy train moves along a straight section of track. Fig. 1.1 shows the variation with time $t$ of the distance $d$ moved by the train."

    p_bi = parts_by_id["9702_w20_22_q01_b_i"]
    p_bi["question_text"] = "Describe qualitatively the motion of the train between time t = 0 and time t = 1.0 s."
    p_bi["question_text_latex"] = "Describe qualitatively the motion of the train between time $t = 0$ and time $t = 1.0\\text{ s}$."
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q01_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q01_b_i_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Answer",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_w20_22_q01_b_ii"]
    p_bii["question_text"] = "Determine the speed of the train at time t = 2.0 s.\nspeed = m s^{-1}"
    p_bii["question_text_latex"] = "Determine the speed of the train at time $t = 2.0\\text{ s}$.\n$$\\text{speed} = \\text{.................................................... m s}^{-1}$$"
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q01_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q01_b_ii_value",
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

    p_c = parts_by_id["9702_w20_22_q01_c"]
    p_c["question_text"] = "The straight section of track in (b) is part of the loop of track shown in Fig. 1.2.\nThe train completes exactly one lap of the loop.\nState and explain the average velocity of the train over the one complete lap."
    p_c["question_text_latex"] = "The straight section of track in (b) is part of the loop of track shown in Fig. 1.2.\nThe train completes exactly one lap of the loop.\nState and explain the average velocity of the train over the one complete lap."
    p_c["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q01_c_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q01_c_answer",
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
    ed_parts["9702_w20_22_q01_a"]["mapping"] = {
        "primary_topic_id": "9702_t01",
        "primary_module_id": "9702_t01_m04",
        "outcome_ids": ["9702_t01_m04_o01"]
    }
    ed_parts["9702_w20_22_q01_a"]["skills"] = {
        "primary_skill_id": "9702_skill_scalars_vectors",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q01_a"]["question_patterns"] = ["classification"]
    ed_parts["9702_w20_22_q01_a"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Classification of physical quantities as scalars or vectors."
    }

    ed_parts["9702_w20_22_q01_b_i"]["mapping"] = {
        "primary_topic_id": "9702_t02",
        "primary_module_id": "9702_t02_m01",
        "outcome_ids": ["9702_t02_m01_o05"]
    }
    ed_parts["9702_w20_22_q01_b_i"]["skills"] = {
        "primary_skill_id": "9702_skill_motion_graphs",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q01_b_i"]["question_patterns"] = ["graph_interpretation"]
    ed_parts["9702_w20_22_q01_b_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Deducing changing speed from the gradient of a distance-time graph."
    }

    ed_parts["9702_w20_22_q01_b_ii"]["mapping"] = {
        "primary_topic_id": "9702_t02",
        "primary_module_id": "9702_t02_m01",
        "outcome_ids": ["9702_t02_m01_o05"]
    }
    ed_parts["9702_w20_22_q01_b_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_motion_graphs",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q01_b_ii"]["question_patterns"] = ["graph_interpretation", "direct_calculation"]
    ed_parts["9702_w20_22_q01_b_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_average_speed"]
    }

    ed_parts["9702_w20_22_q01_c"]["mapping"] = {
        "primary_topic_id": "9702_t02",
        "primary_module_id": "9702_t02_m01",
        "outcome_ids": ["9702_t02_m01_o02"]
    }
    ed_parts["9702_w20_22_q01_c"]["skills"] = {
        "primary_skill_id": "9702_skill_displacement_velocity_acceleration",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q01_c"]["question_patterns"] = ["explanation"]
    ed_parts["9702_w20_22_q01_c"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_average_velocity"]
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)

# ==============================================================================
# Q02
# ==============================================================================
def repair_w20_22_q02():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w20_qp_22/question_02.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w20_22_q02.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_2_1",
            "label": "Fig. 2.1",
            "file": "figure_2_1.png",
            "introduced_by": "9702_w20_22_q02_a",
            "referenced_by": ["9702_w20_22_q02_a"],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w20_22_q02_a",
                "anchor": "A cylinder is suspended from the end of a string. The cylinder is stationary in water with the axis of the cylinder vertical, as shown in Fig. 2.1."
            }
        },
        {
            "id": "fig_2_2",
            "label": "Fig. 2.2",
            "file": "figure_2_2.png",
            "introduced_by": "9702_w20_22_q02_b",
            "referenced_by": ["9702_w20_22_q02_b"],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w20_22_q02_b",
                "anchor": "The string is now used to move the cylinder in (a) vertically upwards through the water. The variation with time t of the velocity v of the cylinder is shown in Fig. 2.2."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w20_22_q02_a"]
    p_a["question_text"] = "A cylinder is suspended from the end of a string. The cylinder is stationary in water with the axis of the cylinder vertical, as shown in Fig. 2.1.\nThe cylinder has weight 0.84 N, height h and a circular cross-section of diameter 0.031 m.\nThe density of the water is 1.0 × 10^{3} kg m^{-3}. The difference between the pressures on the top and bottom faces of the cylinder is 520 Pa."
    p_a["question_text_latex"] = "A cylinder is suspended from the end of a string. The cylinder is stationary in water with the axis of the cylinder vertical, as shown in Fig. 2.1.\nThe cylinder has weight $0.84\\text{ N}$, height $h$ and a circular cross-section of diameter $0.031\\text{ m}$.\nThe density of the water is $1.0 \\times 10^{3}\\text{ kg m}^{-3}$. The difference between the pressures on the top and bottom faces of the cylinder is $520\\text{ Pa}$."

    p_ai = parts_by_id["9702_w20_22_q02_a_i"]
    p_ai["question_text"] = "Calculate the height h of the cylinder.\nh = m"
    p_ai["question_text_latex"] = "Calculate the height $h$ of the cylinder.\n$$h = \\text{.................................................... m}$$"
    p_ai["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q02_a_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q02_a_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "h",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m}"
                        }
                    }
                ]
            }
        ]
    }

    p_aii = parts_by_id["9702_w20_22_q02_a_ii"]
    p_aii["question_text"] = "Show that the upthrust acting on the cylinder is 0.39 N."
    p_aii["question_text_latex"] = "Show that the upthrust acting on the cylinder is $0.39\\text{ N}$."
    p_aii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q02_a_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q02_a_ii_working",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_aiii = parts_by_id["9702_w20_22_q02_a_iii"]
    p_aiii["question_text"] = "Calculate the tension T in the string.\nT = N"
    p_aiii["question_text_latex"] = "Calculate the tension $T$ in the string.\n$$T = \\text{.................................................... N}$$"
    p_aiii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q02_a_iii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q02_a_iii_value",
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

    p_b = parts_by_id["9702_w20_22_q02_b"]
    p_b["question_text"] = "The string is now used to move the cylinder in (a) vertically upwards through the water. The variation with time t of the velocity v of the cylinder is shown in Fig. 2.2."
    p_b["question_text_latex"] = "The string is now used to move the cylinder in (a) vertically upwards through the water. The variation with time $t$ of the velocity $v$ of the cylinder is shown in Fig. 2.2."

    p_bi = parts_by_id["9702_w20_22_q02_b_i"]
    p_bi["question_text"] = "Calculate the magnitude of the acceleration of the cylinder at time t = 2.0 s.\nacceleration = m s^{-2}"
    p_bi["question_text_latex"] = "Calculate the magnitude of the acceleration of the cylinder at time $t = 2.0\\text{ s}$.\n$$\\text{acceleration} = \\text{.................................................... m s}^{-2}$$"
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q02_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q02_b_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Acceleration",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m s}^{-2}"
                        }
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_w20_22_q02_b_ii"]
    p_bii["question_text"] = "Calculate the depth of the base of the cylinder below the surface of the water at time t = 4.0 s.\ndepth = m"
    p_bii["question_text_latex"] = "Calculate the depth of the base of the cylinder below the surface of the water at time $t = 4.0\\text{ s}$.\n$$\\text{depth} = \\text{.................................................... m}$$"
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q02_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q02_b_ii_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Depth",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m}"
                        }
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_w20_22_q02_c"]
    p_c["question_text"] = "The force T in the string is now removed and the cylinder falls vertically downwards through the water."
    p_c["question_text_latex"] = "The force $T$ in the string is now removed and the cylinder falls vertically downwards through the water."

    p_ci = parts_by_id["9702_w20_22_q02_c_i"]
    p_ci["question_text"] = "State the name of the upward force acting on the cylinder."
    p_ci["question_text_latex"] = "State the name of the upward force acting on the cylinder."
    p_ci["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q02_c_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q02_c_i_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Name of force",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_cii = parts_by_id["9702_w20_22_q02_c_ii"]
    p_cii["question_text"] = "Explain why the acceleration of the cylinder decreases between time t = 0 and time t = 4.0 s."
    p_cii["question_text_latex"] = "Explain why the acceleration of the cylinder decreases between time $t = 0$ and time $t = 4.0\\text{ s}$."
    p_cii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q02_c_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q02_c_ii_answer",
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
    ed_parts["9702_w20_22_q02_a_i"]["mapping"] = {
        "primary_topic_id": "9702_t04",
        "primary_module_id": "9702_t04_m03",
        "outcome_ids": ["9702_t04_m03_o03"]
    }
    ed_parts["9702_w20_22_q02_a_i"]["skills"] = {
        "primary_skill_id": "9702_skill_density_pressure",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q02_a_i"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_22_q02_a_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_hydrostatic_pressure"]
    }

    ed_parts["9702_w20_22_q02_a_ii"]["mapping"] = {
        "primary_topic_id": "9702_t04",
        "primary_module_id": "9702_t04_m03",
        "outcome_ids": ["9702_t04_m03_o04"]
    }
    ed_parts["9702_w20_22_q02_a_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_upthrust_archimedes",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q02_a_ii"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_22_q02_a_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_pressure_force"]
    }

    ed_parts["9702_w20_22_q02_a_iii"]["mapping"] = {
        "primary_topic_id": "9702_t04",
        "primary_module_id": "9702_t04_m02",
        "outcome_ids": ["9702_t04_m02_o01"]
    }
    ed_parts["9702_w20_22_q02_a_iii"]["skills"] = {
        "primary_skill_id": "9702_skill_equilibrium_coplanar_forces",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q02_a_iii"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_22_q02_a_iii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Equilibrium of vertical forces: T + U = W."
    }

    ed_parts["9702_w20_22_q02_b_i"]["mapping"] = {
        "primary_topic_id": "9702_t02",
        "primary_module_id": "9702_t02_m01",
        "outcome_ids": ["9702_t02_m01_o05"]
    }
    ed_parts["9702_w20_22_q02_b_i"]["skills"] = {
        "primary_skill_id": "9702_skill_motion_graphs",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q02_b_i"]["question_patterns"] = ["graph_interpretation", "direct_calculation"]
    ed_parts["9702_w20_22_q02_b_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_acceleration"]
    }

    ed_parts["9702_w20_22_q02_b_ii"]["mapping"] = {
        "primary_topic_id": "9702_t02",
        "primary_module_id": "9702_t02_m01",
        "outcome_ids": ["9702_t02_m01_o03", "9702_t02_m01_o07"]
    }
    ed_parts["9702_w20_22_q02_b_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_motion_graphs",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q02_b_ii"]["question_patterns"] = ["graph_interpretation", "multi_step_calculation"]
    ed_parts["9702_w20_22_q02_b_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Determining distance fallen from geometric area under velocity-time graph."
    }

    ed_parts["9702_w20_22_q02_c_i"]["mapping"] = {
        "primary_topic_id": "9702_t03",
        "primary_module_id": "9702_t03_m02",
        "outcome_ids": ["9702_t03_m02_o01"]
    }
    ed_parts["9702_w20_22_q02_c_i"]["skills"] = {
        "primary_skill_id": "9702_skill_drag_terminal_velocity",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q02_c_i"]["question_patterns"] = ["property_identification"]
    ed_parts["9702_w20_22_q02_c_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Identifying viscous drag force acting on an object falling through a fluid."
    }

    ed_parts["9702_w20_22_q02_c_ii"]["mapping"] = {
        "primary_topic_id": "9702_t03",
        "primary_module_id": "9702_t03_m02",
        "outcome_ids": ["9702_t03_m02_o02"]
    }
    ed_parts["9702_w20_22_q02_c_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_drag_terminal_velocity",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q02_c_ii"]["question_patterns"] = ["explanation"]
    ed_parts["9702_w20_22_q02_c_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Explaining decreasing acceleration as viscous force increases with velocity."
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)

# ==============================================================================
# Q03
# ==============================================================================
def repair_w20_22_q03():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w20_qp_22/question_03.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w20_22_q03.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_3_1",
            "label": "Fig. 3.1",
            "file": "figure_3_1.png",
            "introduced_by": "9702_w20_22_q03_a",
            "referenced_by": ["9702_w20_22_q03_a"],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w20_22_q03_a",
                "anchor": "A spring is fixed at one end and is compressed by applying a force to the other end. The variation of the force F acting on the spring with its compression x is shown in Fig. 3.1."
            }
        },
        {
            "id": "fig_3_2",
            "label": "Fig. 3.2",
            "file": "figure_3_2.png",
            "introduced_by": "9702_w20_22_q03_c",
            "referenced_by": ["9702_w20_22_q03_c"],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w20_22_q03_c",
                "anchor": "The ball in (b) leaves the toy at point A and moves vertically upwards through the air. Point B is the position of the ball when it is at maximum height h above point A, as illustrated in Fig. 3.2."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w20_22_q03_a"]
    p_a["question_text"] = "A spring is fixed at one end and is compressed by applying a force to the other end. The variation of the force F acting on the spring with its compression x is shown in Fig. 3.1.\nA compression of 0.045 m is produced when a force F_{1} acts on the spring. The spring has a spring constant of 800 N m^{-1}."
    p_a["question_text_latex"] = "A spring is fixed at one end and is compressed by applying a force to the other end. The variation of the force $F$ acting on the spring with its compression $x$ is shown in Fig. 3.1.\nA compression of $0.045\\text{ m}$ is produced when a force $F_{1}$ acts on the spring. The spring has a spring constant of $800\\text{ N m}^{-1}$."

    p_ai = parts_by_id["9702_w20_22_q03_a_i"]
    p_ai["question_text"] = "Determine F_{1}.\nF_{1} = N"
    p_ai["question_text_latex"] = "Determine $F_{1}$.\n$$F_{1} = \\text{.................................................... N}$$"
    p_ai["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q03_a_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q03_a_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "F_1",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{N}"
                        }
                    }
                ]
            }
        ]
    }

    p_aii = parts_by_id["9702_w20_22_q03_a_ii"]
    p_aii["question_text"] = "Use Fig. 3.1 to show that, for a compression of 0.045 m, the elastic potential energy of the spring is 0.81 J."
    p_aii["question_text_latex"] = "Use Fig. 3.1 to show that, for a compression of $0.045\\text{ m}$, the elastic potential energy of the spring is $0.81\\text{ J}$."
    p_aii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q03_a_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q03_a_ii_working",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w20_22_q03_b"]
    p_b["question_text"] = "A child's toy uses the spring in (a) to launch a ball of mass 0.020 kg vertically into the air. The ball is initially held against one end of the spring which has a compression of 0.045 m. The spring is then released to launch the ball. The kinetic energy of the ball as it leaves the toy is 0.72 J."
    p_b["question_text_latex"] = "A child's toy uses the spring in (a) to launch a ball of mass $0.020\\text{ kg}$ vertically into the air. The ball is initially held against one end of the spring which has a compression of $0.045\\text{ m}$. The spring is then released to launch the ball. The kinetic energy of the ball as it leaves the toy is $0.72\\text{ J}$."

    p_bi = parts_by_id["9702_w20_22_q03_b_i"]
    p_bi["question_text"] = "The toy converts the elastic potential energy of the spring into the kinetic energy of the ball. Use the information in (a)(ii) to calculate the percentage efficiency of this conversion.\nefficiency = %"
    p_bi["question_text_latex"] = "The toy converts the elastic potential energy of the spring into the kinetic energy of the ball. Use the information in (a)(ii) to calculate the percentage efficiency of this conversion.\n$$\\text{efficiency} = \\text{....................................................}\\%$$"
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q03_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q03_b_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Efficiency",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\%"
                        }
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_w20_22_q03_b_ii"]
    p_bii["question_text"] = "Determine the initial momentum of the ball as it leaves the toy.\nmomentum = N s"
    p_bii["question_text_latex"] = "Determine the initial momentum of the ball as it leaves the toy.\n$$\\text{momentum} = \\text{.................................................... N s}$$"
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q03_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q03_b_ii_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Momentum",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{N s}"
                        }
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_w20_22_q03_c"]
    p_c["question_text"] = "The ball in (b) leaves the toy at point A and moves vertically upwards through the air. Point B is the position of the ball when it is at maximum height h above point A, as illustrated in Fig. 3.2.\nThe gravitational potential energy of the ball increases by 0.60 J as it moves from A to B."
    p_c["question_text_latex"] = "The ball in (b) leaves the toy at point A and moves vertically upwards through the air. Point B is the position of the ball when it is at maximum height $h$ above point A, as illustrated in Fig. 3.2.\nThe gravitational potential energy of the ball increases by $0.60\\text{ J}$ as it moves from A to B."

    p_ci = parts_by_id["9702_w20_22_q03_c_i"]
    p_ci["question_text"] = "Calculate h.\nh = m"
    p_ci["question_text_latex"] = "Calculate $h$.\n$$h = \\text{.................................................... m}$$"
    p_ci["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q03_c_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q03_c_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "h",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m}"
                        }
                    }
                ]
            }
        ]
    }

    p_cii = parts_by_id["9702_w20_22_q03_c_ii"]
    p_cii["question_text"] = "Determine the average force due to air resistance acting on the ball for its movement from A to B.\naverage force = N"
    p_cii["question_text_latex"] = "Determine the average force due to air resistance acting on the ball for its movement from A to B.\n$$\\text{average force} = \\text{.................................................... N}$$"
    p_cii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q03_c_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q03_c_ii_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Average force",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{N}"
                        }
                    }
                ]
            }
        ]
    }

    p_ciii = parts_by_id["9702_w20_22_q03_c_iii"]
    p_ciii["question_text"] = "When there is air resistance, the ball takes time T to move from A to B.\nState and explain whether the time taken for the ball to move from A to its maximum height will be more than, less than or equal to time T if there is no air resistance."
    p_ciii["question_text_latex"] = "When there is air resistance, the ball takes time $T$ to move from A to B.\nState and explain whether the time taken for the ball to move from A to its maximum height will be more than, less than or equal to time $T$ if there is no air resistance."
    p_ciii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q03_c_iii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q03_c_iii_answer",
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
    ed_parts["9702_w20_22_q03_a_i"]["mapping"] = {
        "primary_topic_id": "9702_t06",
        "primary_module_id": "9702_t06_m01",
        "outcome_ids": ["9702_t06_m01_o03"]
    }
    ed_parts["9702_w20_22_q03_a_i"]["skills"] = {
        "primary_skill_id": "9702_skill_hookes_law_elastic_energy",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q03_a_i"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_22_q03_a_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_hookes_law"]
    }

    ed_parts["9702_w20_22_q03_a_ii"]["mapping"] = {
        "primary_topic_id": "9702_t06",
        "primary_module_id": "9702_t06_m02",
        "outcome_ids": ["9702_t06_m02_o03", "9702_t06_m02_o04"]
    }
    ed_parts["9702_w20_22_q03_a_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_hookes_law_elastic_energy",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q03_a_ii"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_22_q03_a_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_elastic_potential_energy"]
    }

    ed_parts["9702_w20_22_q03_b_i"]["mapping"] = {
        "primary_topic_id": "9702_t05",
        "primary_module_id": "9702_t05_m01",
        "outcome_ids": ["9702_t05_m01_o04"]
    }
    ed_parts["9702_w20_22_q03_b_i"]["skills"] = {
        "primary_skill_id": "9702_skill_power_efficiency",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q03_b_i"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_22_q03_b_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_efficiency"]
    }

    ed_parts["9702_w20_22_q03_b_ii"]["mapping"] = {
        "primary_topic_id": "9702_t03",
        "primary_module_id": "9702_t03_m01",
        "outcome_ids": ["9702_t03_m01_o01"]
    }
    ed_parts["9702_w20_22_q03_b_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_linear_momentum_collisions",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q03_b_ii"]["question_patterns"] = ["multi_step_calculation"]
    ed_parts["9702_w20_22_q03_b_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_kinetic_energy", "9702_formula_momentum"]
    }

    ed_parts["9702_w20_22_q03_c_i"]["mapping"] = {
        "primary_topic_id": "9702_t05",
        "primary_module_id": "9702_t05_m02",
        "outcome_ids": ["9702_t05_m02_o02"]
    }
    ed_parts["9702_w20_22_q03_c_i"]["skills"] = {
        "primary_skill_id": "9702_skill_kinetic_potential_energy",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q03_c_i"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_22_q03_c_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_gravitational_potential_energy"]
    }

    ed_parts["9702_w20_22_q03_c_ii"]["mapping"] = {
        "primary_topic_id": "9702_t05",
        "primary_module_id": "9702_t05_m01",
        "outcome_ids": ["9702_t05_m01_o02"]
    }
    ed_parts["9702_w20_22_q03_c_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_work_done",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q03_c_ii"]["question_patterns"] = ["multi_step_calculation"]
    ed_parts["9702_w20_22_q03_c_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_work"]
    }

    ed_parts["9702_w20_22_q03_c_iii"]["mapping"] = {
        "primary_topic_id": "9702_t03",
        "primary_module_id": "9702_t03_m02",
        "outcome_ids": ["9702_t03_m02_o02"]
    }
    ed_parts["9702_w20_22_q03_c_iii"]["skills"] = {
        "primary_skill_id": "9702_skill_drag_terminal_velocity",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q03_c_iii"]["question_patterns"] = ["explanation"]
    ed_parts["9702_w20_22_q03_c_iii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Qualitative comparison of flight time with and without resistive drag forces."
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)

# ==============================================================================
# Q04
# ==============================================================================
def repair_w20_22_q04():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w20_qp_22/question_04.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w20_22_q04.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["question_stem"] = "A rigid plank is used to make a ramp between two different horizontal levels of ground, as shown in Fig. 4.1.\nPoint A at one end of the plank rests on the lower level of the ground. A force acts on, and is perpendicular to, the plank at point B. The plank is held in equilibrium by a rope that connects point D on the plank to the ground. The plank has a weight that may be considered to act from its centre of gravity C.\nThe rope is perpendicular to the plank and has tension T. The plank is at an angle of 38° to the vertical.\nThe forces and the distances along the plank of points A, B, C and D are shown in Fig. 4.1."
    qd["question_stem_latex"] = "A rigid plank is used to make a ramp between two different horizontal levels of ground, as shown in Fig. 4.1.\nPoint A at one end of the plank rests on the lower level of the ground. A force acts on, and is perpendicular to, the plank at point B. The plank is held in equilibrium by a rope that connects point D on the plank to the ground. The plank has a weight that may be considered to act from its centre of gravity C.\nThe rope is perpendicular to the plank and has tension $T$. The plank is at an angle of $38^\\circ$ to the vertical.\nThe forces and the distances along the plank of points A, B, C and D are shown in Fig. 4.1."

    qd["figures"] = [
        {
            "id": "fig_4_1",
            "label": "Fig. 4.1",
            "file": "figure_4_1.png",
            "introduced_by": None,
            "referenced_by": [],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "question",
                "position": "after_stem",
                "anchor": "A rigid plank is used to make a ramp between two different horizontal levels of ground, as shown in Fig. 4.1."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w20_22_q04_a"]
    p_a["question_text"] = "Show that the component of the weight that is perpendicular to the plank is 59 N."
    p_a["question_text_latex"] = "Show that the component of the weight that is perpendicular to the plank is $59\\text{ N}$."
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q04_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q04_a_working",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w20_22_q04_b"]
    p_b["question_text"] = "By taking moments about end A of the plank, calculate the tension T.\nT = N"
    p_b["question_text_latex"] = "By taking moments about end A of the plank, calculate the tension $T$.\n$$T = \\text{.................................................... N}$$"
    p_b["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q04_b_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q04_b_value",
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
    ed_parts["9702_w20_22_q04_a"]["mapping"] = {
        "primary_topic_id": "9702_t01",
        "primary_module_id": "9702_t01_m04",
        "outcome_ids": ["9702_t01_m04_o03"]
    }
    ed_parts["9702_w20_22_q04_a"]["skills"] = {
        "primary_skill_id": "9702_skill_scalars_vectors",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q04_a"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_22_q04_a"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Resolution of a weight vector into a perpendicular component using trigonometry."
    }

    ed_parts["9702_w20_22_q04_b"]["mapping"] = {
        "primary_topic_id": "9702_t04",
        "primary_module_id": "9702_t04_m01",
        "outcome_ids": ["9702_t04_m01_o02"]
    }
    ed_parts["9702_w20_22_q04_b"]["skills"] = {
        "primary_skill_id": "9702_skill_moments_couples",
        "supporting_skill_ids": ["9702_skill_equilibrium_coplanar_forces"]
    }
    ed_parts["9702_w20_22_q04_b"]["question_patterns"] = ["multi_step_calculation"]
    ed_parts["9702_w20_22_q04_b"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_moment"]
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)

# ==============================================================================
# Q05
# ==============================================================================
def repair_w20_22_q05():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w20_qp_22/question_05.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w20_22_q05.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["question_stem"] = "Microwaves with the same wavelength and amplitude are emitted in phase from two sources X and Y, as shown in Fig. 5.1.\nA microwave detector is moved along a path parallel to the line joining X and Y. An interference pattern is detected. A central intensity maximum is located at point A and there is an adjacent intensity minimum at point B. The microwaves have a wavelength of 0.040 m."
    qd["question_stem_latex"] = "Microwaves with the same wavelength and amplitude are emitted in phase from two sources X and Y, as shown in Fig. 5.1.\nA microwave detector is moved along a path parallel to the line joining X and Y. An interference pattern is detected. A central intensity maximum is located at point A and there is an adjacent intensity minimum at point B. The microwaves have a wavelength of $0.040\\text{ m}$."

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
                "anchor": "Microwaves with the same wavelength and amplitude are emitted in phase from two sources X and Y, as shown in Fig. 5.1."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w20_22_q05_a"]
    p_a["question_text"] = "Calculate the frequency, in GHz, of the microwaves.\nfrequency = GHz"
    p_a["question_text_latex"] = "Calculate the frequency, in GHz, of the microwaves.\n$$\\text{frequency} = \\text{.................................................... GHz}$$"
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q05_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q05_a_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Frequency",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{GHz}"
                        }
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w20_22_q05_b"]
    p_b["question_text"] = "For the waves arriving at point B, determine:"
    p_b["question_text_latex"] = "For the waves arriving at point B, determine:"

    p_bi = parts_by_id["9702_w20_22_q05_b_i"]
    p_bi["question_text"] = "the path difference\npath difference = m"
    p_bi["question_text_latex"] = "the path difference\n$$\\text{path difference} = \\text{.................................................... m}$$"
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q05_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q05_b_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Path difference",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m}"
                        }
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_w20_22_q05_b_ii"]
    p_bii["question_text"] = "the phase difference.\nphase difference = °"
    p_bii["question_text_latex"] = "the phase difference.\n$$\\text{phase difference} = \\text{....................................................}^\\circ$$"
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q05_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q05_b_ii_value",
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

    p_c = parts_by_id["9702_w20_22_q05_c"]
    p_c["question_text"] = "The amplitude of the wave from source X is now doubled. The amplitude of the wave from source Y is unchanged.\nState and explain what happens to the intensity of the microwaves detected at point A."
    p_c["question_text_latex"] = "The amplitude of the wave from source X is now doubled. The amplitude of the wave from source Y is unchanged.\nState and explain what happens to the intensity of the microwaves detected at point A."
    p_c["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q05_c_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q05_c_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Answer",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_d = parts_by_id["9702_w20_22_q05_d"]
    p_d["question_text"] = "Describe and explain the effect, if any, on the position of the intensity maximum at A and the position of the intensity minimum at B when:"
    p_d["question_text_latex"] = "Describe and explain the effect, if any, on the position of the intensity maximum at A and the position of the intensity minimum at B when:"

    p_di = parts_by_id["9702_w20_22_q05_d_i"]
    p_di["question_text"] = "the frequency of the microwaves emitted by X and Y is increased"
    p_di["question_text_latex"] = "the frequency of the microwaves emitted by X and Y is increased"
    p_di["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q05_d_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q05_d_i_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Answer",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_dii = parts_by_id["9702_w20_22_q05_d_ii"]
    p_dii["question_text"] = "the phase of the wave emitted from source X is changed by 180° so that the two sources emit waves that are in antiphase."
    p_dii["question_text_latex"] = "the phase of the wave emitted from source X is changed by $180^\\circ$ so that the two sources emit waves that are in antiphase."
    p_dii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q05_d_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q05_d_ii_answer",
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
    ed_parts["9702_w20_22_q05_a"]["mapping"] = {
        "primary_topic_id": "9702_t07",
        "primary_module_id": "9702_t07_m01",
        "outcome_ids": ["9702_t07_m01_o05"]
    }
    ed_parts["9702_w20_22_q05_a"]["skills"] = {
        "primary_skill_id": "9702_skill_progressive_wave_properties",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q05_a"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_22_q05_a"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_wave_speed"]
    }

    ed_parts["9702_w20_22_q05_b_i"]["mapping"] = {
        "primary_topic_id": "9702_t08",
        "primary_module_id": "9702_t08_m03",
        "outcome_ids": ["9702_t08_m03_o02"]
    }
    ed_parts["9702_w20_22_q05_b_i"]["skills"] = {
        "primary_skill_id": "9702_skill_two_source_interference",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q05_b_i"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_22_q05_b_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_two_source_interference_path_difference"]
    }

    ed_parts["9702_w20_22_q05_b_ii"]["mapping"] = {
        "primary_topic_id": "9702_t08",
        "primary_module_id": "9702_t08_m03",
        "outcome_ids": ["9702_t08_m03_o03"]
    }
    ed_parts["9702_w20_22_q05_b_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_two_source_interference",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q05_b_ii"]["question_patterns"] = ["property_identification"]
    ed_parts["9702_w20_22_q05_b_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Deducing phase difference corresponding to destructive interference at an intensity minimum."
    }

    ed_parts["9702_w20_22_q05_c"]["mapping"] = {
        "primary_topic_id": "9702_t07",
        "primary_module_id": "9702_t07_m01",
        "outcome_ids": ["9702_t07_m01_o07"]
    }
    ed_parts["9702_w20_22_q05_c"]["skills"] = {
        "primary_skill_id": "9702_skill_wave_intensity_amplitude",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q05_c"]["question_patterns"] = ["interference_analysis", "explanation"]
    ed_parts["9702_w20_22_q05_c"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_wave_intensity_amplitude"]
    }

    ed_parts["9702_w20_22_q05_d_i"]["mapping"] = {
        "primary_topic_id": "9702_t08",
        "primary_module_id": "9702_t08_m03",
        "outcome_ids": ["9702_t08_m03_o04"]
    }
    ed_parts["9702_w20_22_q05_d_i"]["skills"] = {
        "primary_skill_id": "9702_skill_two_source_interference",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q05_d_i"]["question_patterns"] = ["interference_analysis", "explanation"]
    ed_parts["9702_w20_22_q05_d_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_double_slit_interference"]
    }

    ed_parts["9702_w20_22_q05_d_ii"]["mapping"] = {
        "primary_topic_id": "9702_t08",
        "primary_module_id": "9702_t08_m03",
        "outcome_ids": ["9702_t08_m03_o01"]
    }
    ed_parts["9702_w20_22_q05_d_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_two_source_interference",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q05_d_ii"]["question_patterns"] = ["interference_analysis", "explanation"]
    ed_parts["9702_w20_22_q05_d_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Deducing swap of intensity maxima and minima positions when source phase shifts by 180 degrees."
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)

# ==============================================================================
# Q06
# ==============================================================================
def repair_w20_22_q06():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w20_qp_22/question_06.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w20_22_q06.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_6_1",
            "label": "Fig. 6.1",
            "file": "figure_6_1.png",
            "introduced_by": "9702_w20_22_q06_a",
            "referenced_by": ["9702_w20_22_q06_a"],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w20_22_q06_a",
                "anchor": "A network of three resistors of resistances R_{1}, R_{2} and R_{3} is shown in Fig. 6.1."
            }
        },
        {
            "id": "fig_6_2",
            "label": "Fig. 6.2",
            "file": "figure_6_2.png",
            "introduced_by": "9702_w20_22_q06_b",
            "referenced_by": ["9702_w20_22_q06_b"],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w20_22_q06_b",
                "anchor": "A battery of electromotive force (e.m.f.) 8.0 V and internal resistance r is connected to three resistors X, Y and Z, as shown in Fig. 6.2."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w20_22_q06_a"]
    p_a["question_text"] = "A network of three resistors of resistances R_{1}, R_{2} and R_{3} is shown in Fig. 6.1.\nThe individual currents in the resistors are I_{1}, I_{2} and I_{3}. The total current in the combination of resistors is I and the potential difference across the combination is V.\nShow that the total resistance R of the network is given by\n1/R = 1/R_{1} + 1/R_{2} + 1/R_{3}."
    p_a["question_text_latex"] = "A network of three resistors of resistances $R_{1}$, $R_{2}$ and $R_{3}$ is shown in Fig. 6.1.\nThe individual currents in the resistors are $I_{1}$, $I_{2}$ and $I_{3}$. The total current in the combination of resistors is $I$ and the potential difference across the combination is $V$.\nShow that the total resistance $R$ of the network is given by\n$$\\frac{1}{R} = \\frac{1}{R_{1}} + \\frac{1}{R_{2}} + \\frac{1}{R_{3}}$$"
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q06_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q06_a_working",
                        "control": "long_text",
                        "role": "working",
                        "label": "Derivation",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w20_22_q06_b"]
    p_b["question_text"] = "A battery of electromotive force (e.m.f.) 8.0 V and internal resistance r is connected to three resistors X, Y and Z, as shown in Fig. 6.2.\nResistor Y has a resistance of 16 Ω. The current in resistor X is 0.49 A and the current in resistor Y is 0.45 A.\nCalculate:"
    p_b["question_text_latex"] = "A battery of electromotive force (e.m.f.) $8.0\\text{ V}$ and internal resistance $r$ is connected to three resistors X, Y and Z, as shown in Fig. 6.2.\nResistor Y has a resistance of $16\\ \\Omega$. The current in resistor X is $0.49\\text{ A}$ and the current in resistor Y is $0.45\\text{ A}$.\nCalculate:"

    p_bi = parts_by_id["9702_w20_22_q06_b_i"]
    p_bi["question_text"] = "the current in the battery\ncurrent = A"
    p_bi["question_text_latex"] = "the current in the battery\n$$\\text{current} = \\text{.................................................... A}$$"
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q06_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q06_b_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Current",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{A}"
                        }
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_w20_22_q06_b_ii"]
    p_bii["question_text"] = "the internal resistance r of the battery.\nr = Ω"
    p_bii["question_text_latex"] = "the internal resistance $r$ of the battery.\n$$r = \\text{.................................................... }\\Omega$$"
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q06_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q06_b_ii_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Internal resistance",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\Omega"
                        }
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_w20_22_q06_c"]
    p_c["question_text"] = "Resistors X and Y are made of wires of the same length and the same material. The diameter of the wire of resistor X is 2.1 times the diameter of the wire of resistor Y.\nCalculate the ratio average drift speed in X / average drift speed in Y.\nratio ="
    p_c["question_text_latex"] = "Resistors X and Y are made of wires of the same length and the same material. The diameter of the wire of resistor X is 2.1 times the diameter of the wire of resistor Y.\nCalculate the ratio:\n$$\\frac{\\text{average drift speed in X}}{\\text{average drift speed in Y}}$$\n$$\\text{ratio} = \\text{....................................................}$$"
    p_c["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q06_c_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q06_c_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "Average drift speed in Y",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m s}^{-1}"
                        }
                    }
                ]
            }
        ]
    }

    p_d = parts_by_id["9702_w20_22_q06_d"]
    p_d["question_text"] = "A third resistor Z is connected in parallel with resistors X and Y in the circuit in (b).\nState and explain the effect of connecting resistor Z on the potential difference across the battery terminals."
    p_d["question_text_latex"] = "A third resistor Z is connected in parallel with resistors X and Y in the circuit in (b).\nState and explain the effect of connecting resistor Z on the potential difference across the battery terminals."
    p_d["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q06_d_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q06_d_answer",
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
    ed_parts["9702_w20_22_q06_a"]["mapping"] = {
        "primary_topic_id": "9702_t10",
        "primary_module_id": "9702_t10_m02",
        "outcome_ids": ["9702_t10_m02_o05"]
    }
    ed_parts["9702_w20_22_q06_a"]["skills"] = {
        "primary_skill_id": "9702_skill_resistor_networks",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q06_a"]["question_patterns"] = ["equation_derivation"]
    ed_parts["9702_w20_22_q06_a"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_parallel_resistance", "9702_formula_kirchhoff_first_law"]
    }

    ed_parts["9702_w20_22_q06_b_i"]["mapping"] = {
        "primary_topic_id": "9702_t10",
        "primary_module_id": "9702_t10_m02",
        "outcome_ids": ["9702_t10_m02_o01"]
    }
    ed_parts["9702_w20_22_q06_b_i"]["skills"] = {
        "primary_skill_id": "9702_skill_kirchhoffs_laws",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q06_b_i"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_22_q06_b_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_kirchhoff_first_law"]
    }

    ed_parts["9702_w20_22_q06_b_ii"]["mapping"] = {
        "primary_topic_id": "9702_t10",
        "primary_module_id": "9702_t10_m01",
        "outcome_ids": ["9702_t10_m01_o05"]
    }
    ed_parts["9702_w20_22_q06_b_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_emf_internal_resistance",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q06_b_ii"]["question_patterns"] = ["multi_step_calculation"]
    ed_parts["9702_w20_22_q06_b_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_terminal_potential_difference"]
    }

    ed_parts["9702_w20_22_q06_c"]["mapping"] = {
        "primary_topic_id": "9702_t09",
        "primary_module_id": "9702_t09_m01",
        "outcome_ids": ["9702_t09_m01_o04"]
    }
    ed_parts["9702_w20_22_q06_c"]["skills"] = {
        "primary_skill_id": "9702_skill_electric_current_drift_speed",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q06_c"]["question_patterns"] = ["direct_calculation"]
    ed_parts["9702_w20_22_q06_c"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_current_drift"]
    }

    ed_parts["9702_w20_22_q06_d"]["mapping"] = {
        "primary_topic_id": "9702_t10",
        "primary_module_id": "9702_t10_m01",
        "outcome_ids": ["9702_t10_m01_o05"]
    }
    ed_parts["9702_w20_22_q06_d"]["skills"] = {
        "primary_skill_id": "9702_skill_emf_internal_resistance",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q06_d"]["question_patterns"] = ["circuit_analysis", "explanation"]
    ed_parts["9702_w20_22_q06_d"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": ["9702_formula_terminal_potential_difference"]
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)

# ==============================================================================
# Q07
# ==============================================================================
def repair_w20_22_q07():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w20_qp_22/question_07.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w20_22_q07.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_7_1",
            "label": "Fig. 7.1",
            "file": "figure_7_1.png",
            "introduced_by": "9702_w20_22_q07_b",
            "referenced_by": ["9702_w20_22_q07_b", "9702_w20_22_q07_b_i"],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w20_22_q07_b",
                "anchor": "Fig. 7.1 shows an electron in an electric field, in a vacuum, at an instant when the electron is stationary."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w20_22_q07_a"]
    p_a["question_text"] = "State a similarity and a difference between an up quark and an up antiquark."
    p_a["question_text_latex"] = "State a similarity and a difference between an up quark and an up antiquark."
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q07_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q07_a_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Answer",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w20_22_q07_b"]
    p_b["question_text"] = "Fig. 7.1 shows an electron in an electric field, in a vacuum, at an instant when the electron is stationary."
    p_b["question_text_latex"] = "Fig. 7.1 shows an electron in an electric field, in a vacuum, at an instant when the electron is stationary."

    p_bi = parts_by_id["9702_w20_22_q07_b_i"]
    p_bi["question_text"] = "On Fig. 7.1, draw an arrow to show the direction of the electric force acting on the stationary electron."
    p_bi["question_text_latex"] = "On Fig. 7.1, draw an arrow to show the direction of the electric force acting on the stationary electron."
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q07_b_i_canvas",
                "type": "canvas",
                "background_figure_id": "fig_7_1",
                "tools": ["arrow", "line"]
            }
        ]
    }

    p_bii = parts_by_id["9702_w20_22_q07_b_ii"]
    p_bii["question_text"] = "The electron is in the electric field between two horizontal metal plates. The potential difference between the plates is constant.\nDescribe and explain the variation, if any, in the magnitude of the acceleration of the electron as it moves vertically downwards towards the bottom plate."
    p_bii["question_text_latex"] = "The electron is in the electric field between two horizontal metal plates. The potential difference between the plates is constant.\nDescribe and explain the variation, if any, in the magnitude of the acceleration of the electron as it moves vertically downwards towards the bottom plate."
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q07_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q07_b_ii_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Answer",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_biii = parts_by_id["9702_w20_22_q07_b_iii"]
    p_biii["question_text"] = "An α-particle is now placed in the same initial position between the plates.\nCompare the electric force acting on the α-particle with the electric force that acted on the electron in (b)(i)."
    p_biii["question_text_latex"] = "An $\\alpha$-particle is now placed in the same initial position between the plates.\nCompare the electric force acting on the $\\alpha$-particle with the electric force that acted on the electron in (b)(i)."
    p_biii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w20_22_q07_b_iii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w20_22_q07_b_iii_answer",
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
    ed_parts["9702_w20_22_q07_a"]["mapping"] = {
        "primary_topic_id": "9702_t11",
        "primary_module_id": "9702_t11_m02",
        "outcome_ids": ["9702_t11_m02_o02"]
    }
    ed_parts["9702_w20_22_q07_a"]["skills"] = {
        "primary_skill_id": "9702_skill_quark_model_hadrons",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q07_a"]["question_patterns"] = ["comparison"]
    ed_parts["9702_w20_22_q07_a"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Qualitative comparison between an up quark and an up antiquark."
    }

    ed_parts["9702_w20_22_q07_b_i"]["mapping"] = {
        "primary_topic_id": "9702_t09",
        "primary_module_id": "9702_t09_m01",
        "outcome_ids": ["9702_t09_m01_o01"]
    }
    ed_parts["9702_w20_22_q07_b_i"]["skills"] = {
        "primary_skill_id": "9702_skill_uniform_electric_fields",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q07_b_i"]["question_patterns"] = ["force_diagram_construction"]
    ed_parts["9702_w20_22_q07_b_i"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Drawing direction of electric force on a stationary electron in an electric field."
    }

    ed_parts["9702_w20_22_q07_b_ii"]["mapping"] = {
        "primary_topic_id": "9702_t09",
        "primary_module_id": "9702_t09_m01",
        "outcome_ids": ["9702_t09_m01_o01"]
    }
    ed_parts["9702_w20_22_q07_b_ii"]["skills"] = {
        "primary_skill_id": "9702_skill_uniform_electric_fields",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q07_b_ii"]["question_patterns"] = ["explanation"]
    ed_parts["9702_w20_22_q07_b_ii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Explaining constant force and acceleration in a uniform electric field."
    }

    ed_parts["9702_w20_22_q07_b_iii"]["mapping"] = {
        "primary_topic_id": "9702_t11",
        "primary_module_id": "9702_t11_m01",
        "outcome_ids": ["9702_t11_m01_o07"]
    }
    ed_parts["9702_w20_22_q07_b_iii"]["skills"] = {
        "primary_skill_id": "9702_skill_nuclear_decay_equations",
        "supporting_skill_ids": []
    }
    ed_parts["9702_w20_22_q07_b_iii"]["question_patterns"] = ["comparison"]
    ed_parts["9702_w20_22_q07_b_iii"]["knowledge_refs"] = {
        "definition_ids": [],
        "formula_ids": [],
        "formula_empty_justification": "Comparing magnitude and direction of electric force based on particle charge (+2e vs -e)."
    }

    finalize_enrichment(ed)
    save_json(enr_path, ed)

def main():
    repair_w20_22_q01()
    repair_w20_22_q02()
    repair_w20_22_q03()
    repair_w20_22_q04()
    repair_w20_22_q05()
    repair_w20_22_q06()
    repair_w20_22_q07()

if __name__ == "__main__":
    main()
