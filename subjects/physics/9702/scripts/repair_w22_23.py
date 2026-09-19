#!/usr/bin/env python3
"""
scripts/repair_w22_23.py
Repairs all questions and enrichments for 9702_w22_23 (Q01 to Q06).
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
# Question 1
# ==============================================================================
def repair_q01():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w22_qp_23/question_01.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w22_23_q01.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["question_stem"] = (
        "The rate of flow Q of a liquid along a narrow pipe of length L and radius r is given by\n"
        "Q = (αr^{4}) / L\n"
        "where α is a constant.\n"
        "An experiment is carried out to determine the value of α. The data from the experiment are shown in Table 1.1.\n"
        "Table 1.1\n"
        "quantity | value | percentage uncertainty\n"
        "Q | 2.72 × 10^{-8} m^{3} s^{-1} | ± 3%\n"
        "r | 7.1 × 10^{-5} m | ± 2%\n"
        "L | 2.5 × 10^{-2} m | ± 4%"
    )
    qd["question_stem_latex"] = (
        "The rate of flow $Q$ of a liquid along a narrow pipe of length $L$ and radius $r$ is given by\n"
        "$$Q = \\frac{\\alpha r^{4}}{L}$$\n"
        "where $\\alpha$ is a constant.\n"
        "An experiment is carried out to determine the value of $\\alpha$. The data from the experiment are shown in Table 1.1.\n"
        "Table 1.1\n"
        "quantity | value | percentage uncertainty\n"
        "$Q$ | $2.72 \\times 10^{-8}\\text{ m}^{3}\\text{ s}^{-1}$ | $\\pm 3\\%$\n"
        "$r$ | $7.1 \\times 10^{-5}\\text{ m}$ | $\\pm 2\\%$\n"
        "$L$ | $2.5 \\times 10^{-2}\\text{ m}$ | $\\pm 4\\%$"
    )

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w22_23_q01_a"]
    p_a["question_text"] = "Use information in Table 1.1 to show that the SI base unit of α is s^{-1}."
    p_a["question_text_latex"] = "Use information in Table 1.1 to show that the SI base unit of $\\alpha$ is $\\text{s}^{-1}$."
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q01_a_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q01_a_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w22_23_q01_b"]
    p_b["question_text"] = "Show that the percentage uncertainty in α is 15%."
    p_b["question_text_latex"] = "Show that the percentage uncertainty in $\\alpha$ is $15\\%$."
    p_b["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q01_b_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q01_b_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_w22_23_q01_c"]
    p_c["question_text"] = (
        "Calculate α with its absolute uncertainty. Give your answer to an appropriate number of significant figures.\n"
        "α = ( ± ) × 10^{7} s^{-1}"
    )
    p_c["question_text_latex"] = (
        "Calculate $\\alpha$ with its absolute uncertainty. Give your answer to an appropriate number of significant figures.\n"
        "$$\\alpha = ( \\text{...................} \\pm \\text{...................} ) \\times 10^{7}\\text{ s}^{-1}$$"
    )
    p_c["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q01_c_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q01_c_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    },
                    {
                        "field_id": "9702_w22_23_q01_c_field_02",
                        "control": "number",
                        "role": "value",
                        "label": "Central value of α",
                        "required": True
                    },
                    {
                        "field_id": "9702_w22_23_q01_c_field_03",
                        "control": "number",
                        "role": "uncertainty",
                        "label": "Absolute uncertainty",
                        "required": True
                    }
                ]
            }
        ]
    }

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))


# ==============================================================================
# Question 2
# ==============================================================================
def repair_q02():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w22_qp_23/question_02.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w22_23_q02.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["question_stem"] = (
        "The engine of a toy rocket pushes gases vertically downwards and this results in the rocket accelerating vertically upwards from the ground.\n"
        "The rocket starts to move from rest at time t = 0. The variation with time t of the vertical velocity v of the rocket for the first 0.30 s of the flight is shown in Fig. 2.1.\n"
        "As the rocket moves, the thrust force T provided by the rocket engine is 16 N.\n"
        "Assume that the mass of the rocket is constant for this part of its flight.\n"
        "Assume that air resistance is negligible."
    )
    qd["question_stem_latex"] = (
        "The engine of a toy rocket pushes gases vertically downwards and this results in the rocket accelerating vertically upwards from the ground.\n"
        "The rocket starts to move from rest at time $t = 0$. The variation with time $t$ of the vertical velocity $v$ of the rocket for the first $0.30\\text{ s}$ of the flight is shown in Fig. 2.1.\n"
        "As the rocket moves, the thrust force $T$ provided by the rocket engine is $16\\text{ N}$.\n"
        "Assume that the mass of the rocket is constant for this part of its flight.\n"
        "Assume that air resistance is negligible."
    )

    qd["figures"] = [
        {
            "id": "fig_2_1",
            "label": "Fig. 2.1",
            "file": "figure_2_1.png",
            "introduced_by": "question_stem",
            "referenced_by": [],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "question",
                "position": "after_stem",
                "anchor": "The variation with time t of the vertical velocity v of the rocket for the first 0.30 s of the flight is shown in Fig. 2.1."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w22_23_q02_a"]
    p_a["question_text"] = "For this part of the rocket’s flight:"
    p_a["question_text_latex"] = "For this part of the rocket’s flight:"

    p_a_i = parts_by_id["9702_w22_23_q02_a_i"]
    p_a_i["question_text"] = "show that the acceleration of the rocket is 55 m s^{-2}"
    p_a_i["question_text_latex"] = "show that the acceleration of the rocket is $55\\text{ m s}^{-2}$"
    p_a_i["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q02_a_i_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q02_a_i_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_a_ii = parts_by_id["9702_w22_23_q02_a_ii"]
    p_a_ii["question_text"] = "state an expression for the resultant force F experienced by the rocket in terms of the thrust force T and the weight W of the rocket"
    p_a_ii["question_text_latex"] = (
        "state an expression for the resultant force $F$ experienced by the rocket in terms of the thrust force $T$ and the weight $W$ of the rocket\n"
        "$$F = \\text{...................................................}$$"
    )
    p_a_ii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q02_a_ii_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q02_a_ii_field_01",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Expression for F",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_a_iii = parts_by_id["9702_w22_23_q02_a_iii"]
    p_a_iii["question_text"] = "calculate the mass of the rocket.\nmass = kg"
    p_a_iii["question_text_latex"] = (
        "calculate the mass of the rocket.\n"
        "$$\\text{mass} = \\text{...................................................}\\text{ kg}$$"
    )
    p_a_iii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q02_a_iii_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q02_a_iii_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    },
                    {
                        "field_id": "9702_w22_23_q02_a_iii_field_02",
                        "control": "number",
                        "role": "answer",
                        "label": "Mass",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w22_23_q02_b"]
    p_b["question_text"] = "At time t = 0.30 s, a small piece of metal separates from the rocket.\nCalculate:"
    p_b["question_text_latex"] = "At time $t = 0.30\\text{ s}$, a small piece of metal separates from the rocket.\nCalculate:"

    p_b_i = parts_by_id["9702_w22_23_q02_b_i"]
    p_b_i["question_text"] = "the height of the rocket above the ground at t = 0.30 s\nheight = m"
    p_b_i["question_text_latex"] = (
        "the height of the rocket above the ground at $t = 0.30\\text{ s}$\n"
        "$$\\text{height} = \\text{...................................................}\\text{ m}$$"
    )
    p_b_i["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q02_b_i_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q02_b_i_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    },
                    {
                        "field_id": "9702_w22_23_q02_b_i_field_02",
                        "control": "number",
                        "role": "answer",
                        "label": "Height",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b_ii = parts_by_id["9702_w22_23_q02_b_ii"]
    p_b_ii["question_text"] = "the speed at which the piece of metal strikes the ground.\nspeed = m s^{-1}"
    p_b_ii["question_text_latex"] = (
        "the speed at which the piece of metal strikes the ground.\n"
        "$$\\text{speed} = \\text{...................................................}\\text{ m s}^{-1}$$"
    )
    p_b_ii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q02_b_ii_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q02_b_ii_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    },
                    {
                        "field_id": "9702_w22_23_q02_b_ii_field_02",
                        "control": "number",
                        "role": "answer",
                        "label": "Speed",
                        "required": True
                    }
                ]
            }
        ]
    }

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))


# ==============================================================================
# Question 3
# ==============================================================================
def repair_q03():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w22_qp_23/question_03.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w22_23_q03.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_3_1",
            "label": "Fig. 3.1",
            "file": "figure_3_1.png",
            "introduced_by": "9702_w22_23_q03_b",
            "referenced_by": [
                "9702_w22_23_q03_b",
                "9702_w22_23_q03_c",
                "9702_w22_23_q03_d"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w22_23_q03_b",
                "anchor": "Fig. 3.1"
            }
        },
        {
            "id": "fig_3_2",
            "label": "Fig. 3.2",
            "file": "figure_3_2.png",
            "introduced_by": "9702_w22_23_q03_c",
            "referenced_by": [
                "9702_w22_23_q03_c",
                "9702_w22_23_q03_c_ii",
                "9702_w22_23_q03_d"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w22_23_q03_c",
                "anchor": "Fig. 3.2"
            }
        },
        {
            "id": "fig_3_3",
            "label": "Fig. 3.3",
            "file": "figure_3_3.png",
            "introduced_by": "9702_w22_23_q03_c",
            "referenced_by": [
                "9702_w22_23_q03_c",
                "9702_w22_23_q03_c_i"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w22_23_q03_c",
                "anchor": "Fig. 3.3"
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w22_23_q03_a"]
    p_a["question_text"] = "State the principle of moments."
    p_a["question_text_latex"] = "State the principle of moments."
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q03_a_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q03_a_field_01",
                        "control": "long_text",
                        "role": "explanation",
                        "label": "Principle of moments",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w22_23_q03_b"]
    p_b["question_text"] = (
        "A hollow plastic sphere is attached at one end of a bar. The sphere is partially submerged in water and the bar is attached to a fixed vertical support by a pivot P, as shown in Fig. 3.1.\n"
        "The sphere has weight 0.30 N. The distance from P to the centre of gravity of the sphere is 0.29 m. Assume that the weight of the bar is negligible.\n"
        "Calculate the moment of the weight of the sphere about P.\nmoment = N m"
    )
    p_b["question_text_latex"] = (
        "A hollow plastic sphere is attached at one end of a bar. The sphere is partially submerged in water and the bar is attached to a fixed vertical support by a pivot P, as shown in Fig. 3.1.\n"
        "The sphere has weight $0.30\\text{ N}$. The distance from P to the centre of gravity of the sphere is $0.29\\text{ m}$. Assume that the weight of the bar is negligible.\n"
        "Calculate the moment of the weight of the sphere about P.\n"
        "$$\\text{moment} = \\text{...................................................}\\text{ N m}$$"
    )
    p_b["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q03_b_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q03_b_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    },
                    {
                        "field_id": "9702_w22_23_q03_b_field_02",
                        "control": "number",
                        "role": "answer",
                        "label": "Moment",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_w22_23_q03_c"]
    p_c["question_text"] = (
        "The system shown in Fig. 3.1 is part of a mechanism that controls the amount of water in a tank.\n"
        "Water enters the tank and causes the sphere to rise. This results in the bar becoming horizontal. Fig. 3.2 shows the system in its new position.\n"
        "In this position the rod R exerts a force to compress a horizontal spring that controls the water supply to the tank. R is positioned at a perpendicular distance of 0.017 m above P.\n"
        "The variation of the force F applied to the spring with compression x of the spring is shown in Fig. 3.3."
    )
    p_c["question_text_latex"] = (
        "The system shown in Fig. 3.1 is part of a mechanism that controls the amount of water in a tank.\n"
        "Water enters the tank and causes the sphere to rise. This results in the bar becoming horizontal. Fig. 3.2 shows the system in its new position.\n"
        "In this position the rod R exerts a force to compress a horizontal spring that controls the water supply to the tank. R is positioned at a perpendicular distance of $0.017\\text{ m}$ above P.\n"
        "The variation of the force $F$ applied to the spring with compression $x$ of the spring is shown in Fig. 3.3."
    )

    p_c_i = parts_by_id["9702_w22_23_q03_c_i"]
    p_c_i["question_text"] = "Use Fig. 3.3 to calculate the spring constant k of the spring.\nk = N m^{-1}"
    p_c_i["question_text_latex"] = (
        "Use Fig. 3.3 to calculate the spring constant $k$ of the spring.\n"
        "$$k = \\text{...................................................}\\text{ N m}^{-1}$$"
    )
    p_c_i["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q03_c_i_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q03_c_i_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    },
                    {
                        "field_id": "9702_w22_23_q03_c_i_field_02",
                        "control": "number",
                        "role": "answer",
                        "label": "Spring constant",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_c_ii = parts_by_id["9702_w22_23_q03_c_ii"]
    p_c_ii["question_text"] = (
        "At the position shown in Fig. 3.2, the system is stationary and in equilibrium.\n"
        "The radius of the sphere is 0.0480 m and 26.0% of the volume of the sphere is submerged.\n"
        "The density of water is 1.00 × 10^{3} kg m^{-3}.\n"
        "Show that the upthrust on the sphere is 1.18 N."
    )
    p_c_ii["question_text_latex"] = (
        "At the position shown in Fig. 3.2, the system is stationary and in equilibrium.\n"
        "The radius of the sphere is $0.0480\\text{ m}$ and $26.0\\%$ of the volume of the sphere is submerged.\n"
        "The density of water is $1.00 \\times 10^{3}\\text{ kg m}^{-3}$.\n"
        "Show that the upthrust on the sphere is $1.18\\text{ N}$."
    )
    p_c_ii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q03_c_ii_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q03_c_ii_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_c_iii = parts_by_id["9702_w22_23_q03_c_iii"]
    p_c_iii["question_text"] = "By taking moments about P, determine the force exerted on the spring by the rod R.\nforce = N"
    p_c_iii["question_text_latex"] = (
        "By taking moments about P, determine the force exerted on the spring by the rod R.\n"
        "$$\\text{force} = \\text{...................................................}\\text{ N}$$"
    )
    p_c_iii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q03_c_iii_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q03_c_iii_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    },
                    {
                        "field_id": "9702_w22_23_q03_c_iii_field_02",
                        "control": "number",
                        "role": "answer",
                        "label": "Force",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_c_iv = parts_by_id["9702_w22_23_q03_c_iv"]
    p_c_iv["question_text"] = "Calculate the elastic potential energy E_{P} of the compressed spring.\nE_{P} = J"
    p_c_iv["question_text_latex"] = (
        "Calculate the elastic potential energy $E_{\\text{P}}$ of the compressed spring.\n"
        "$$E_{\\text{P}} = \\text{...................................................}\\text{ J}$$"
    )
    p_c_iv["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q03_c_iv_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q03_c_iv_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    },
                    {
                        "field_id": "9702_w22_23_q03_c_iv_field_02",
                        "control": "number",
                        "role": "answer",
                        "label": "Elastic potential energy",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_d = parts_by_id["9702_w22_23_q03_d"]
    p_d["question_text"] = (
        "When the sphere moves from the position shown in Fig. 3.1 to the position shown in Fig. 3.2, the upthrust on the sphere does work.\n"
        "Assume that resistive forces are negligible.\n"
        "Explain why the work done by the upthrust is not equal to the gain in elastic potential energy of the spring."
    )
    p_d["question_text_latex"] = (
        "When the sphere moves from the position shown in Fig. 3.1 to the position shown in Fig. 3.2, the upthrust on the sphere does work.\n"
        "Assume that resistive forces are negligible.\n"
        "Explain why the work done by the upthrust is not equal to the gain in elastic potential energy of the spring."
    )
    p_d["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q03_d_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q03_d_field_01",
                        "control": "long_text",
                        "role": "explanation",
                        "label": "Explanation",
                        "required": True
                    }
                ]
            }
        ]
    }

    # Fix enrichment parts
    for ep in ed["parts"]:
        pid = ep["part_id"]
        if pid in ("9702_w22_23_q03_b", "9702_w22_23_q03_c_i", "9702_w22_23_q03_c_iii", "9702_w22_23_q03_c_iv", "9702_w22_23_q03_d"):
            ep["knowledge_refs"]["definition_ids"] = []
        if pid == "9702_w22_23_q03_d":
            ep["mapping"]["outcome_ids"] = ["9702_t05_m01_o02"]

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))


# ==============================================================================
# Question 4
# ==============================================================================
def repair_q04():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w22_qp_23/question_04.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w22_23_q04.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_4_1",
            "label": "Fig. 4.1",
            "file": "figure_4_1.png",
            "introduced_by": "9702_w22_23_q04_a",
            "referenced_by": [
                "9702_w22_23_q04_a",
                "9702_w22_23_q04_a_i",
                "9702_w22_23_q04_a_ii"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w22_23_q04_a",
                "anchor": "Fig. 4.1"
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w22_23_q04_a"]
    p_a["question_text"] = (
        "A progressive longitudinal wave travels through a medium from left to right. Fig. 4.1 shows the positions of some of the particles of the medium at time t_{0} and a graph showing the particle displacements at the same time t_{0}.\n"
        "Particle displacements to the right of their equilibrium positions are shown as positive on the graph and particle displacements to the left are shown as negative on the graph.\n"
        "The period of the wave is T."
    )
    p_a["question_text_latex"] = (
        "A progressive longitudinal wave travels through a medium from left to right. Fig. 4.1 shows the positions of some of the particles of the medium at time $t_{0}$ and a graph showing the particle displacements at the same time $t_{0}$.\n"
        "Particle displacements to the right of their equilibrium positions are shown as positive on the graph and particle displacements to the left are shown as negative on the graph.\n"
        "The period of the wave is $T$."
    )

    p_a_i = parts_by_id["9702_w22_23_q04_a_i"]
    p_a_i["question_text"] = "On Fig. 4.1, draw circles around two particles which are exactly one wavelength apart."
    p_a_i["question_text_latex"] = "On Fig. 4.1, draw circles around two particles which are exactly one wavelength apart."
    p_a_i["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q04_a_i_canvas",
                "type": "canvas",
                "background_figure_id": "fig_4_1"
            }
        ]
    }

    p_a_ii = parts_by_id["9702_w22_23_q04_a_ii"]
    p_a_ii["question_text"] = "On Fig. 4.1, sketch a line on the graph to represent the displacements of the particles for the longitudinal wave at time t_{0} + T / 4."
    p_a_ii["question_text_latex"] = "On Fig. 4.1, sketch a line on the graph to represent the displacements of the particles for the longitudinal wave at time $t_{0} + \\frac{T}{4}$."
    p_a_ii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q04_a_ii_canvas",
                "type": "canvas",
                "background_figure_id": "fig_4_1"
            }
        ]
    }

    p_a_iii = parts_by_id["9702_w22_23_q04_a_iii"]
    p_a_iii["question_text"] = "State the direction of motion of particle Z at time t_{0} + T / 4."
    p_a_iii["question_text_latex"] = "State the direction of motion of particle Z at time $t_{0} + \\frac{T}{4}$."
    p_a_iii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q04_a_iii_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q04_a_iii_field_01",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Direction of motion",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w22_23_q04_b"]
    p_b["question_text"] = (
        "The frequency of the wave in (a) is 16 kHz. The distance between particles X and Y is 0.19 m.\n"
        "Calculate the speed of the wave as it travels through the medium.\n"
        "speed = m s^{-1}"
    )
    p_b["question_text_latex"] = (
        "The frequency of the wave in (a) is $16\\text{ kHz}$. The distance between particles X and Y is $0.19\\text{ m}$.\n"
        "Calculate the speed of the wave as it travels through the medium.\n"
        "$$\\text{speed} = \\text{...................................................}\\text{ m s}^{-1}$$"
    )
    p_b["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q04_b_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q04_b_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    },
                    {
                        "field_id": "9702_w22_23_q04_b_field_02",
                        "control": "number",
                        "role": "answer",
                        "label": "Speed",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_w22_23_q04_c"]
    p_c["question_text"] = (
        "A longitudinal sound wave is travelling through a solid. The initial intensity of the wave is I_{0}.\n"
        "The frequency of the wave remains constant and the amplitude falls to half of its original value.\n"
        "Determine, in terms of I_{0}, the final intensity of the wave.\n"
        "intensity = I_{0}"
    )
    p_c["question_text_latex"] = (
        "A longitudinal sound wave is travelling through a solid. The initial intensity of the wave is $I_{0}$.\n"
        "The frequency of the wave remains constant and the amplitude falls to half of its original value.\n"
        "Determine, in terms of $I_{0}$, the final intensity of the wave.\n"
        "$$\\text{intensity} = \\text{................................................... }I_{0}$$"
    )
    p_c["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q04_c_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q04_c_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    },
                    {
                        "field_id": "9702_w22_23_q04_c_field_02",
                        "control": "number",
                        "role": "answer",
                        "label": "Factor of I₀",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_d = parts_by_id["9702_w22_23_q04_d"]
    p_d["question_text"] = "The sound wave in (c) now meets another sound wave travelling in the opposite direction."
    p_d["question_text_latex"] = "The sound wave in (c) now meets another sound wave travelling in the opposite direction."

    p_d_i = parts_by_id["9702_w22_23_q04_d_i"]
    p_d_i["question_text"] = "State a condition necessary for these two waves to form a stationary wave."
    p_d_i["question_text_latex"] = "State a condition necessary for these two waves to form a stationary wave."
    p_d_i["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q04_d_i_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q04_d_i_field_01",
                        "control": "long_text",
                        "role": "explanation",
                        "label": "Condition",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_d_ii = parts_by_id["9702_w22_23_q04_d_ii"]
    p_d_ii["question_text"] = "State two ways in which a stationary wave differs from a progressive wave."
    p_d_ii["question_text_latex"] = "State two ways in which a stationary wave differs from a progressive wave."
    p_d_ii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q04_d_ii_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q04_d_ii_field_01",
                        "control": "long_text",
                        "role": "explanation",
                        "label": "Differences",
                        "required": True
                    }
                ]
            }
        ]
    }

    # Fix enrichment parts
    for ep in ed["parts"]:
        pid = ep["part_id"]
        if pid in ("9702_w22_23_q04_a_i", "9702_w22_23_q04_a_iii", "9702_w22_23_q04_d_ii"):
            ep["knowledge_refs"]["definition_ids"] = []
        if pid in ("9702_w22_23_q04_d_i", "9702_w22_23_q04_d_ii"):
            ep["skills"]["primary_skill_id"] = "9702_skill_stationary_waves"

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))


# ==============================================================================
# Question 5
# ==============================================================================
def repair_q05():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w22_qp_23/question_05.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w22_23_q05.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_5_1",
            "label": "Fig. 5.1",
            "file": "figure_5_1.png",
            "introduced_by": "9702_w22_23_q05_b",
            "referenced_by": [
                "9702_w22_23_q05_b",
                "9702_w22_23_q05_c",
                "9702_w22_23_q05_d"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_w22_23_q05_b",
                "anchor": "Fig. 5.1"
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w22_23_q05_a"]
    p_a["question_text"] = "State Kirchhoff’s second law."
    p_a["question_text_latex"] = "State Kirchhoff’s second law."
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q05_a_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q05_a_field_01",
                        "control": "long_text",
                        "role": "explanation",
                        "label": "Kirchhoff's second law",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w22_23_q05_b"]
    p_b["question_text"] = (
        "Three identical cells, each of electromotive force (e.m.f.) 1.5 V and internal resistance 590 mΩ, are connected in parallel across a conductor, as shown in Fig. 5.1.\n"
        "The conductor is composed of two cylindrical sections A and B.\n"
        "The total resistance of the circuit is 2.2 Ω."
    )
    p_b["question_text_latex"] = (
        "Three identical cells, each of electromotive force (e.m.f.) $1.5\\text{ V}$ and internal resistance $590\\text{ m}\\Omega$, are connected in parallel across a conductor, as shown in Fig. 5.1.\n"
        "The conductor is composed of two cylindrical sections A and B.\n"
        "The total resistance of the circuit is $2.2\\,\\Omega$."
    )

    p_b_i = parts_by_id["9702_w22_23_q05_b_i"]
    p_b_i["question_text"] = "Show that the resistance of the conductor is 2.0 Ω."
    p_b_i["question_text_latex"] = "Show that the resistance of the conductor is $2.0\\,\\Omega$."
    p_b_i["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q05_b_i_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q05_b_i_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b_ii = parts_by_id["9702_w22_23_q05_b_ii"]
    p_b_ii["question_text"] = "Calculate the current in the conductor.\ncurrent = A"
    p_b_ii["question_text_latex"] = (
        "Calculate the current in the conductor.\n"
        "$$\\text{current} = \\text{...................................................}\\text{ A}$$"
    )
    p_b_ii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q05_b_ii_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q05_b_ii_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    },
                    {
                        "field_id": "9702_w22_23_q05_b_ii_field_02",
                        "control": "number",
                        "role": "answer",
                        "label": "Current",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_w22_23_q05_c"]
    p_c["question_text"] = (
        "The two cylindrical sections A and B of the conductor in Fig. 5.1 are made from the same material and have the same length.\n"
        "The diameter of section A is 4.3 mm and the diameter of section B is 7.6 mm.\n"
        "The resistance of section A is R_{A} and the resistance of section B is R_{B}."
    )
    p_c["question_text_latex"] = (
        "The two cylindrical sections A and B of the conductor in Fig. 5.1 are made from the same material and have the same length.\n"
        "The diameter of section A is $4.3\\text{ mm}$ and the diameter of section B is $7.6\\text{ mm}$.\n"
        "The resistance of section A is $R_{\\text{A}}$ and the resistance of section B is $R_{\\text{B}}$."
    )

    p_c_i = parts_by_id["9702_w22_23_q05_c_i"]
    p_c_i["question_text"] = "Calculate the ratio R_{A} / R_{B}.\nratio ="
    p_c_i["question_text_latex"] = (
        "Calculate the ratio $\\frac{R_{\\text{A}}}{R_{\\text{B}}}$.\n"
        "$$\\text{ratio} = \\text{...................................................}$$"
    )
    p_c_i["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q05_c_i_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q05_c_i_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    },
                    {
                        "field_id": "9702_w22_23_q05_c_i_field_02",
                        "control": "number",
                        "role": "answer",
                        "label": "Ratio",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_c_ii = parts_by_id["9702_w22_23_q05_c_ii"]
    p_c_ii["question_text"] = (
        "Calculate the ratio (average drift speed of free electrons in section A) / (average drift speed of free electrons in section B).\n"
        "Explain your reasoning.\n"
        "ratio ="
    )
    p_c_ii["question_text_latex"] = (
        "Calculate the ratio\n"
        "$$\\frac{\\text{average drift speed of free electrons in section A}}{\\text{average drift speed of free electrons in section B}}$$\n"
        "Explain your reasoning.\n"
        "$$\\text{ratio} = \\text{...................................................}$$"
    )
    p_c_ii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q05_c_ii_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q05_c_ii_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working and explanation",
                        "required": True
                    },
                    {
                        "field_id": "9702_w22_23_q05_c_ii_field_02",
                        "control": "number",
                        "role": "answer",
                        "label": "Ratio",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_d = parts_by_id["9702_w22_23_q05_d"]
    p_d["question_text"] = (
        "The circuit of Fig. 5.1 is altered by removing one of the cells.\n"
        "State and explain the effect, if any, of this change on the potential difference across the conductor."
    )
    p_d["question_text_latex"] = (
        "The circuit of Fig. 5.1 is altered by removing one of the cells.\n"
        "State and explain the effect, if any, of this change on the potential difference across the conductor."
    )
    p_d["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q05_d_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q05_d_field_01",
                        "control": "long_text",
                        "role": "explanation",
                        "label": "State and explanation",
                        "required": True
                    }
                ]
            }
        ]
    }

    # Fix outcome in part b_i
    for ep in ed["parts"]:
        if ep["part_id"] == "9702_w22_23_q05_b_i":
            ep["mapping"]["outcome_ids"] = ["9702_t10_m01_o04"]

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))


# ==============================================================================
# Question 6
# ==============================================================================
def repair_q06():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_w22_qp_23/question_06.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_w22_23_q06.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_w22_23_q06_a"]
    p_a["question_text"] = (
        "The nuclide ^{14}_{6}C (carbon-14) is unstable and undergoes β^{-} decay, emitting a high-energy electron and an antineutrino to form a new nuclide X. The equation for this decay is shown.\n"
        "^{14}_{6}C -> ..._...X + ..._...e^{-} + ^{0}_{0}ν\n"
        "Complete the equation."
    )
    p_a["question_text_latex"] = (
        "The nuclide $^{14}_{6}\\text{C}$ (carbon-14) is unstable and undergoes $\\beta^{-}$ decay, emitting a high-energy electron and an antineutrino to form a new nuclide X. The equation for this decay is shown.\n"
        "$$^{14}_{6}\\text{C} \\rightarrow \\, ^{...}_{...}\\text{X} + \\, ^{...}_{...}\\text{e}^{-} + \\, ^{0}_{0}\\bar{\\nu}$$\n"
        "Complete the equation."
    )
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q06_a_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q06_a_field_01",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Completed equation",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_w22_23_q06_b"]
    p_b["question_text"] = ""
    p_b["question_text_latex"] = ""

    p_b_i = parts_by_id["9702_w22_23_q06_b_i"]
    p_b_i["question_text"] = "State the equation for β^{-} decay in terms of the fundamental particles involved."
    p_b_i["question_text_latex"] = "State the equation for $\\beta^{-}$ decay in terms of the fundamental particles involved."
    p_b_i["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q06_b_i_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q06_b_i_field_01",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Fundamental particle equation",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b_ii = parts_by_id["9702_w22_23_q06_b_ii"]
    p_b_ii["question_text"] = "Use your equation from (b)(i) to show how charge is conserved in β^{-} decay."
    p_b_ii["question_text_latex"] = "Use your equation from (b)(i) to show how charge is conserved in $\\beta^{-}$ decay."
    p_b_ii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q06_b_ii_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q06_b_ii_field_01",
                        "control": "long_text",
                        "role": "working",
                        "label": "Working",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_w22_23_q06_c"]
    p_c["question_text"] = "Neutrinos were first proposed to exist more than 20 years before they were directly detected, in order to explain a particular experimental observation about β-decay."
    p_c["question_text_latex"] = "Neutrinos were first proposed to exist more than 20 years before they were directly detected, in order to explain a particular experimental observation about $\\beta$-decay."

    p_c_i = parts_by_id["9702_w22_23_q06_c_i"]
    p_c_i["question_text"] = "State an observation about β-decay that is explained by the existence of neutrinos."
    p_c_i["question_text_latex"] = "State an observation about $\\beta$-decay that is explained by the existence of neutrinos."
    p_c_i["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q06_c_i_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q06_c_i_field_01",
                        "control": "long_text",
                        "role": "explanation",
                        "label": "Observation",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_c_ii = parts_by_id["9702_w22_23_q06_c_ii"]
    p_c_ii["question_text"] = "Suggest how the existence of neutrinos explains the observation in (c)(i)."
    p_c_ii["question_text_latex"] = "Suggest how the existence of neutrinos explains the observation in (c)(i)."
    p_c_ii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_w22_23_q06_c_ii_block_01",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_w22_23_q06_c_ii_field_01",
                        "control": "long_text",
                        "role": "explanation",
                        "label": "Explanation",
                        "required": True
                    }
                ]
            }
        ]
    }

    # Fix enrichment parts
    for ep in ed["parts"]:
        pid = ep["part_id"]
        if pid == "9702_w22_23_q06_a":
            ep["skills"]["primary_skill_id"] = "9702_skill_nuclear_decay_equations"
            ep["skills"]["supporting_skill_ids"] = ["9702_skill_fundamental_particles_interactions"]
        elif pid == "9702_w22_23_q06_b_i":
            ep["knowledge_refs"]["definition_ids"] = []
            ep["skills"]["primary_skill_id"] = "9702_skill_fundamental_particles_interactions"
            ep["skills"]["supporting_skill_ids"] = ["9702_skill_quark_model_hadrons"]
        elif pid == "9702_w22_23_q06_b_ii":
            ep["skills"]["primary_skill_id"] = "9702_skill_quark_model_hadrons"
            ep["skills"]["supporting_skill_ids"] = ["9702_skill_fundamental_particles_interactions"]
        elif pid in ("9702_w22_23_q06_c_i", "9702_w22_23_q06_c_ii"):
            ep["skills"]["primary_skill_id"] = "9702_skill_fundamental_particles_interactions"
            ep["skills"]["supporting_skill_ids"] = []

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))


def main():
    print("Repairing Q01...")
    repair_q01()
    print("Repairing Q02...")
    repair_q02()
    print("Repairing Q03...")
    repair_q03()
    print("Repairing Q04...")
    repair_q04()
    print("Repairing Q05...")
    repair_q05()
    print("Repairing Q06...")
    repair_q06()
    print("All repairs completed successfully!")

if __name__ == "__main__":
    main()
