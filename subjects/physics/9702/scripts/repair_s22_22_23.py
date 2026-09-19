#!/usr/bin/env python3
"""
scripts/repair_s22_22_23.py
Repairs all questions and enrichments for 9702_s22_22 and 9702_s22_23 (Q01 to Q07).
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
# 9702_s22_22
# ==============================================================================

def repair_s22_22_q01():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s22_qp_22/question_01.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s22_22_q01.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_1_1",
            "label": "Fig. 1.1",
            "file": "figure_1_1.png",
            "introduced_by": "9702_s22_22_q01_b",
            "referenced_by": [
                "9702_s22_22_q01_b"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_s22_22_q01_b",
                "anchor": "Fig. 1.1 shows a horizontal beam clamped at one end with a block attached to the other end."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s22_22_q01_a"]
    p_a["question_text"] = "In the following list, underline all units that are SI base units.\nampere degree Celsius kilogram newton"
    p_a["question_text_latex"] = "In the following list, underline all units that are SI base units.\n$$\\text{ampere} \\qquad \\text{degree Celsius} \\qquad \\text{kilogram} \\qquad \\text{newton}$$"
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q01_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q01_a_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "SI base units",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_s22_22_q01_b"]
    p_b["question_text"] = (
        "Fig. 1.1 shows a horizontal beam clamped at one end with a block attached to the other end. "
        "The block is made to oscillate vertically.\n"
        "The Young modulus E of the material of the beam is given by\n"
        "E = (kM) / (T^{2})\n"
        "where M is the mass of the block, T is the period of the oscillations and k is a constant.\n"
        "A student determines the values and percentage uncertainties of k, M and T.\n"
        "Table 1.1 lists the percentage uncertainties.\n"
        "Table 1.1\n"
        "quantity | percentage uncertainty\n"
        "k | ± 2.1%\n"
        "M | ± 0.6%\n"
        "T | ± 1.5%\n"
        "The student uses the values of k, M and T to calculate the value of E as 8.245 × 10^{9} Pa."
    )
    p_b["question_text_latex"] = (
        "Fig. 1.1 shows a horizontal beam clamped at one end with a block attached to the other end. "
        "The block is made to oscillate vertically.\n"
        "The Young modulus $E$ of the material of the beam is given by\n"
        "$$E = \\frac{kM}{T^{2}}$$\n"
        "where $M$ is the mass of the block, $T$ is the period of the oscillations and $k$ is a constant.\n"
        "A student determines the values and percentage uncertainties of $k$, $M$ and $T$.\n"
        "Table 1.1 lists the percentage uncertainties.\n"
        "Table 1.1\n"
        "quantity | percentage uncertainty\n"
        "$k$ | $\\pm 2.1\\%$\n"
        "$M$ | $\\pm 0.6\\%$\n"
        "$T$ | $\\pm 1.5\\%$\n"
        "The student uses the values of $k$, $M$ and $T$ to calculate the value of $E$ as $8.245 \\times 10^{9}\\text{ Pa}$."
    )

    p_bi = parts_by_id["9702_s22_22_q01_b_i"]
    p_bi["question_text"] = "Calculate the percentage uncertainty in the value of E.\npercentage uncertainty = %"
    p_bi["question_text_latex"] = "Calculate the percentage uncertainty in the value of $E$.\n$$\\text{percentage uncertainty} = \\text{.................................................... }\\%$$"
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q01_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q01_b_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "percentage uncertainty",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\%"
                        }
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_s22_22_q01_b_ii"]
    p_bii["question_text"] = "Use your answer in (b)(i) to determine the value of E, with its absolute uncertainty, to an appropriate number of significant figures.\nE = ( ± ) × 10^{9} Pa"
    p_bii["question_text_latex"] = "Use your answer in (b)(i) to determine the value of $E$, with its absolute uncertainty, to an appropriate number of significant figures.\n$$E = (\\text{........................} \\pm \\text{........................}) \\times 10^{9}\\text{ Pa}$$"
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q01_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q01_b_ii_value",
                        "control": "short_text",
                        "role": "answer",
                        "label": "E",
                        "required": True
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed["parts"][0]["hints"] = [
        "Recall the seven base quantities of the International System of Units and their corresponding SI base units.",
        "Check each unit in the list: the ampere (electric current) and kilogram (mass) are base units, while newton is a derived unit and degree Celsius is a derived/scale temperature unit."
    ]
    finalize_enrichment(ed)
    save_json(enr_path, ed)


def repair_s22_22_q02():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s22_qp_22/question_02.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s22_22_q02.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["question_stem"] = (
        "A sphere is attached by a metal wire to the horizontal surface at the bottom of a river, as shown in Fig. 2.1.\n"
        "The sphere is fully submerged and in equilibrium, with the wire at an angle of 68° to the horizontal surface. "
        "The weight of the sphere is 32 N. The upthrust acting on the sphere is 280 N. The density of the water is 1.0 × 10^{3} kg m^{-3}.\n"
        "Assume that the force on the sphere due to the water flow is in a horizontal direction."
    )
    qd["question_stem_latex"] = (
        "A sphere is attached by a metal wire to the horizontal surface at the bottom of a river, as shown in Fig. 2.1.\n"
        "The sphere is fully submerged and in equilibrium, with the wire at an angle of $68^\\circ$ to the horizontal surface. "
        "The weight of the sphere is $32\\text{ N}$. The upthrust acting on the sphere is $280\\text{ N}$. The density of the water is $1.0 \\times 10^{3}\\text{ kg m}^{-3}$.\n"
        "Assume that the force on the sphere due to the water flow is in a horizontal direction."
    )

    qd["figures"] = [
        {
            "id": "fig_2_1",
            "label": "Fig. 2.1",
            "file": "figure_2_1.png",
            "introduced_by": "question_stem",
            "referenced_by": [
                "9702_s22_22_q02_a"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "question",
                "position": "after_stem",
                "anchor": "A sphere is attached by a metal wire to the horizontal surface at the bottom of a river, as shown in Fig. 2.1."
            }
        }
    ]

    qd["official_part_mapping"] = []
    qd["official_reconciliation"] = {
        "version": "0.1",
        "part_bindings": [],
        "part_aliases": [
            {
                "official_part_ref": {
                    "part_id": "9702_s22_22_q02_d_ii",
                    "occurrence": 2
                },
                "alias_of": {
                    "part_id": "9702_s22_22_q02_d_ii",
                    "occurrence": 1
                },
                "reason": "alternative_route"
            }
        ],
        "part_transfers": [],
        "marking_point_aliases": []
    }

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s22_22_q02_a"]
    p_a["question_text"] = "By considering the components of force in the vertical direction, determine the tension in the wire.\ntension = N"
    p_a["question_text_latex"] = "By considering the components of force in the vertical direction, determine the tension in the wire.\n$$\\text{tension} = \\text{.................................................... N}$$"
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q02_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q02_a_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "tension",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{N}"
                        }
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_s22_22_q02_b"]
    p_b["question_text"] = "For the sphere, calculate:"
    p_b["question_text_latex"] = "For the sphere, calculate:"

    p_bi = parts_by_id["9702_s22_22_q02_b_i"]
    p_bi["question_text"] = "the volume\nvolume = m^{3}"
    p_bi["question_text_latex"] = "the volume\n$$\\text{volume} = \\text{.................................................... m}^3$$"
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q02_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q02_b_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "volume",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m}^3"
                        }
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_s22_22_q02_b_ii"]
    p_bii["question_text"] = "the density.\ndensity = kg m^{-3}"
    p_bii["question_text_latex"] = "the density.\n$$\\text{density} = \\text{.................................................... kg m}^{-3}$$"
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q02_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q02_b_ii_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "density",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{kg m}^{-3}"
                        }
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_s22_22_q02_c"]
    p_c["question_text"] = (
        "The centre of the sphere is initially at a height of 6.2 m above the horizontal surface. "
        "The speed of the water then increases, causing the sphere to move to a different position. "
        "This movement of the sphere causes its gravitational potential energy to decrease by 77 J.\n"
        "Calculate the final height of the centre of the sphere above the horizontal surface.\n"
        "height = m"
    )
    p_c["question_text_latex"] = (
        "The centre of the sphere is initially at a height of $6.2\\text{ m}$ above the horizontal surface. "
        "The speed of the water then increases, causing the sphere to move to a different position. "
        "This movement of the sphere causes its gravitational potential energy to decrease by $77\\text{ J}$.\n"
        "Calculate the final height of the centre of the sphere above the horizontal surface.\n"
        "$$\\text{height} = \\text{.................................................... m}$$"
    )
    p_c["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q02_c_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q02_c_value",
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

    p_d = parts_by_id["9702_s22_22_q02_d"]
    p_d["question_text"] = (
        "The extension of the wire increases when the sphere changes position as described in (c).\n"
        "The wire obeys Hooke’s law."
    )
    p_d["question_text_latex"] = (
        "The extension of the wire increases when the sphere changes position as described in (c).\n"
        "The wire obeys Hooke’s law."
    )

    p_di = parts_by_id["9702_s22_22_q02_d_i"]
    p_di["question_text"] = (
        "State a symbol equation that gives the relationship between the tension T in the wire and its extension x. "
        "Identify any other symbol that you use."
    )
    p_di["question_text_latex"] = (
        "State a symbol equation that gives the relationship between the tension $T$ in the wire and its extension $x$. "
        "Identify any other symbol that you use."
    )
    p_di["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q02_d_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q02_d_i_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Equation and symbols",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_dii = parts_by_id["9702_s22_22_q02_d_ii"]
    p_dii["question_text"] = (
        "Before the sphere changed position, the initial elastic potential energy of the wire was 0.65 J. "
        "The change in position of the sphere causes the extension of the wire to double.\n"
        "Calculate the final elastic potential energy of the wire after the sphere has changed position.\n"
        "final elastic potential energy = J"
    )
    p_dii["question_text_latex"] = (
        "Before the sphere changed position, the initial elastic potential energy of the wire was $0.65\\text{ J}$. "
        "The change in position of the sphere causes the extension of the wire to double.\n"
        "Calculate the final elastic potential energy of the wire after the sphere has changed position.\n"
        "$$\\text{final elastic potential energy} = \\text{.................................................... J}$$"
    )
    p_dii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q02_d_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q02_d_ii_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "final elastic potential energy",
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

    # Fix enrichment mapping & skills for part a
    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_s22_22_q02_a"]["mapping"]["outcome_ids"] = ["9702_t04_m02_o02"]
    ed_parts["9702_s22_22_q02_a"]["skills"]["primary_skill_id"] = "9702_skill_equilibrium_coplanar_forces"

    # Filter ai_rubric for part d_ii to keep occurrence 1
    ed_parts["9702_s22_22_q02_d_ii"]["checking"]["ai_rubric"] = [
        {
            "criterion_id": "9702_s22_22_q02_d_ii_mp01",
            "criterion_occurrence": 1,
            "alternative_criterion_ids": [
                "9702_s22_22_q02_d_ii_mp03"
            ],
            "observable": "Uses E = ½kx², or an equivalent Hookean elastic-energy relationship, to establish that energy scales with the square of extension."
        },
        {
            "criterion_id": "9702_s22_22_q02_d_ii_mp02",
            "criterion_occurrence": 1,
            "observable": "Recognises that doubling the extension multiplies the initial energy by four and obtains 2.6 J."
        }
    ]

    finalize_enrichment(ed)
    save_json(enr_path, ed)


def repair_s22_22_q03():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s22_qp_22/question_03.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s22_22_q03.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["question_stem"] = (
        "A man standing on a wall throws a small ball vertically upwards with a velocity of 5.6 m s^{-1}. "
        "The ball leaves his hand when it is at a height of 3.1 m above the ground, as shown in Fig. 3.1.\n"
        "Assume that air resistance is negligible."
    )
    qd["question_stem_latex"] = (
        "A man standing on a wall throws a small ball vertically upwards with a velocity of $5.6\\text{ m s}^{-1}$. "
        "The ball leaves his hand when it is at a height of $3.1\\text{ m}$ above the ground, as shown in Fig. 3.1.\n"
        "Assume that air resistance is negligible."
    )

    qd["figures"] = [
        {
            "id": "fig_3_1",
            "label": "Fig. 3.1",
            "file": "figure_3_1.png",
            "introduced_by": "question_stem",
            "referenced_by": [],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "question",
                "position": "after_stem",
                "anchor": "The ball leaves his hand when it is at a height of 3.1 m above the ground, as shown in Fig. 3.1."
            }
        },
        {
            "id": "fig_3_2",
            "label": "Fig. 3.2",
            "file": "figure_3_2.png",
            "introduced_by": "9702_s22_22_q03_c",
            "referenced_by": [
                "9702_s22_22_q03_c"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "response_background",
                "part_id": "9702_s22_22_q03_c",
                "anchor": "On Fig. 3.2, sketch a graph to show the variation of the velocity v of the ball with time t"
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s22_22_q03_a"]
    p_a["question_text"] = "Show that the ball reaches a maximum height above the ground of 4.7 m."
    p_a["question_text_latex"] = "Show that the ball reaches a maximum height above the ground of $4.7\\text{ m}$."
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q03_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q03_a_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Proof",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_s22_22_q03_b"]
    p_b["question_text"] = "The man does not catch the ball as it falls.\nCalculate the time taken for the ball to fall from its maximum height to the ground.\ntime taken = s"
    p_b["question_text_latex"] = "The man does not catch the ball as it falls.\nCalculate the time taken for the ball to fall from its maximum height to the ground.\n$$\\text{time taken} = \\text{.................................................... s}$$"
    p_b["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q03_b_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q03_b_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "time taken",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{s}"
                        }
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_s22_22_q03_c"]
    p_c["question_text"] = (
        "The ball leaves the man’s hand at time t = 0 and hits the ground at time t = T.\n"
        "On Fig. 3.2, sketch a graph to show the variation of the velocity v of the ball with time t from "
        "t = 0 to t = T. Numerical values of v and t are not required. Assume that v is positive in the upward direction."
    )
    p_c["question_text_latex"] = (
        "The ball leaves the man’s hand at time $t = 0$ and hits the ground at time $t = T$.\n"
        "On Fig. 3.2, sketch a graph to show the variation of the velocity $v$ of the ball with time $t$ from "
        "$t = 0$ to $t = T$. Numerical values of $v$ and $t$ are not required. Assume that $v$ is positive in the upward direction."
    )
    p_c["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q03_c_canvas",
                "type": "canvas",
                "background_figure_id": "fig_3_2"
            }
        ]
    }

    p_d = parts_by_id["9702_s22_22_q03_d"]
    p_d["question_text"] = "State what is represented by the gradient of the graph in (c)."
    p_d["question_text_latex"] = "State what is represented by the gradient of the graph in (c)."
    p_d["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q03_d_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q03_d_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Physical quantity",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_e = parts_by_id["9702_s22_22_q03_e"]
    p_e["question_text"] = (
        "The man now throws a second ball with the same velocity and from the same height as the first ball. "
        "The mass of the second ball is greater than that of the first ball. Assume that air resistance is still negligible.\n"
        "For the first and second balls, compare:"
    )
    p_e["question_text_latex"] = (
        "The man now throws a second ball with the same velocity and from the same height as the first ball. "
        "The mass of the second ball is greater than that of the first ball. Assume that air resistance is still negligible.\n"
        "For the first and second balls, compare:"
    )

    p_ei = parts_by_id["9702_s22_22_q03_e_i"]
    p_ei["question_text"] = "the magnitudes of their accelerations"
    p_ei["question_text_latex"] = "the magnitudes of their accelerations"
    p_ei["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q03_e_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q03_e_i_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Comparison of accelerations",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_eii = parts_by_id["9702_s22_22_q03_e_ii"]
    p_eii["question_text"] = "the speeds with which they hit the ground."
    p_eii["question_text_latex"] = "the speeds with which they hit the ground."
    p_eii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q03_e_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q03_e_ii_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Comparison of speeds",
                        "required": True
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_s22_22_q03_d"]["question_patterns"] = ["graph_interpretation"]

    finalize_enrichment(ed)
    save_json(enr_path, ed)


def repair_s22_22_q04():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s22_qp_22/question_04.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s22_22_q04.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s22_22_q04_a"]
    p_a["question_text"] = "State the principle of conservation of momentum."
    p_a["question_text_latex"] = "State the principle of conservation of momentum."
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q04_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q04_a_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Principle of conservation of momentum",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_s22_22_q04_b"]
    p_b["question_text"] = (
        "Two balls, X and Y, move along a horizontal frictionless surface, as shown from above in Fig. 4.1.\n"
        "Ball X has a mass of 3.0 kg and a velocity of 4.0 m s^{-1} in a direction at angle θ to a line AB. "
        "Ball Y has a mass of 2.5 kg and a velocity of 4.8 m s^{-1} in a direction at angle θ to the line AB. "
        "The balls collide and stick together. After colliding, the balls have a velocity of 3.7 m s^{-1} along "
        "the line AB on the horizontal surface, as shown in Fig. 4.2."
    )
    p_b["question_text_latex"] = (
        "Two balls, X and Y, move along a horizontal frictionless surface, as shown from above in Fig. 4.1.\n"
        "Ball X has a mass of $3.0\\text{ kg}$ and a velocity of $4.0\\text{ m s}^{-1}$ in a direction at angle $\\theta$ to a line AB. "
        "Ball Y has a mass of $2.5\\text{ kg}$ and a velocity of $4.8\\text{ m s}^{-1}$ in a direction at angle $\\theta$ to the line AB. "
        "The balls collide and stick together. After colliding, the balls have a velocity of $3.7\\text{ m s}^{-1}$ along "
        "the line AB on the horizontal surface, as shown in Fig. 4.2."
    )

    p_bi = parts_by_id["9702_s22_22_q04_b_i"]
    p_bi["question_text"] = "By considering the components of the momenta along the line AB, calculate θ.\nθ = °"
    p_bi["question_text_latex"] = "By considering the components of the momenta along the line AB, calculate $\\theta$.\n$$\\theta = \\text{.................................................... }^\\circ$$"
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q04_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q04_b_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "θ",
                        "required": True,
                        "unit": {
                            "unit_latex": "^\\circ"
                        }
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_s22_22_q04_b_ii"]
    p_bii["question_text"] = "By calculation of kinetic energies, state and explain whether the collision of the balls is inelastic or perfectly elastic."
    p_bii["question_text_latex"] = "By calculation of kinetic energies, state and explain whether the collision of the balls is inelastic or perfectly elastic."
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q04_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q04_b_ii_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Working and explanation",
                        "required": True
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_s22_22_q04_b_i"]["mapping"]["outcome_ids"] = ["9702_t03_m03_o02"]
    ed_parts["9702_s22_22_q04_b_ii"]["knowledge_refs"]["definition_ids"] = []

    finalize_enrichment(ed)
    save_json(enr_path, ed)


def repair_s22_22_q05():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s22_qp_22/question_05.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s22_22_q05.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["question_stem"] = (
        "Light from a laser is used to produce an interference pattern on a screen, as shown in Fig. 5.1.\n"
        "The light of wavelength 660 nm is incident normally on two slits that have a separation of 0.44 mm.\n"
        "The double slit is parallel to the screen. The perpendicular distance between the double slit and the screen is 1.8 m.\n"
        "The central bright fringe on the screen is formed at point O. The next dark fringe below point O is formed at point P. "
        "The next bright fringe and the next dark fringe below point P are formed at points Q and R respectively."
    )
    qd["question_stem_latex"] = (
        "Light from a laser is used to produce an interference pattern on a screen, as shown in Fig. 5.1.\n"
        "The light of wavelength $660\\text{ nm}$ is incident normally on two slits that have a separation of $0.44\\text{ mm}$.\n"
        "The double slit is parallel to the screen. The perpendicular distance between the double slit and the screen is $1.8\\text{ m}$.\n"
        "The central bright fringe on the screen is formed at point O. The next dark fringe below point O is formed at point P. "
        "The next bright fringe and the next dark fringe below point P are formed at points Q and R respectively."
    )

    qd["figures"] = [
        {
            "id": "fig_5_1",
            "label": "Fig. 5.1",
            "file": "figure_5_1.png",
            "introduced_by": "question_stem",
            "referenced_by": [],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "question",
                "position": "after_stem",
                "anchor": "Light from a laser is used to produce an interference pattern on a screen, as shown in Fig. 5.1."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s22_22_q05_a"]
    p_a["question_text"] = "The light waves from the two slits are coherent.\nState what is meant by coherent."
    p_a["question_text_latex"] = "The light waves from the two slits are coherent.\nState what is meant by coherent."
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q05_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q05_a_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Definition of coherent",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_s22_22_q05_b"]
    p_b["question_text"] = "For the two light waves superposing at R, calculate:"
    p_b["question_text_latex"] = "For the two light waves superposing at R, calculate:"

    p_bi = parts_by_id["9702_s22_22_q05_b_i"]
    p_bi["question_text"] = "the difference in their path lengths, in nm, from the slits\npath difference = nm"
    p_bi["question_text_latex"] = "the difference in their path lengths, in nm, from the slits\n$$\\text{path difference} = \\text{.................................................... nm}$$"
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q05_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q05_b_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "path difference",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{nm}"
                        }
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_s22_22_q05_b_ii"]
    p_bii["question_text"] = "their phase difference.\nphase difference ="
    p_bii["question_text_latex"] = "their phase difference.\n$$\\text{phase difference} = \\text{....................................................}$$"
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q05_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q05_b_ii_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "phase difference",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_s22_22_q05_c"]
    p_c["question_text"] = "Calculate the distance OQ.\ndistance OQ = m"
    p_c["question_text_latex"] = "Calculate the distance OQ.\n$$\\text{distance OQ} = \\text{.................................................... m}$$"
    p_c["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q05_c_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q05_c_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "distance OQ",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m}"
                        }
                    }
                ]
            }
        ]
    }

    p_d = parts_by_id["9702_s22_22_q05_d"]
    p_d["question_text"] = (
        "The intensity of the light incident on the double slit is increased without changing the frequency.\n"
        "Describe how the appearance of the fringes after this change is different from, and similar to, their appearance before the change."
    )
    p_d["question_text_latex"] = (
        "The intensity of the light incident on the double slit is increased without changing the frequency.\n"
        "Describe how the appearance of the fringes after this change is different from, and similar to, their appearance before the change."
    )
    p_d["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q05_d_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q05_d_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Fringe appearance comparison",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_e = parts_by_id["9702_s22_22_q05_e"]
    p_e["question_text"] = (
        "The light of wavelength 660 nm is now replaced by blue light from a laser.\n"
        "State and explain the change, if any, that must be made to the separation of the two slits so that the fringe separation on the screen is the same as it was for light of wavelength 660 nm."
    )
    p_e["question_text_latex"] = (
        "The light of wavelength $660\\text{ nm}$ is now replaced by blue light from a laser.\n"
        "State and explain the change, if any, that must be made to the separation of the two slits so that the fringe separation on the screen is the same as it was for light of wavelength $660\\text{ nm}$."
    )
    p_e["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q05_e_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q05_e_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "State and explanation",
                        "required": True
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_s22_22_q05_d"]["skills"]["primary_skill_id"] = "9702_skill_two_source_interference"
    ed_parts["9702_s22_22_q05_d"]["mapping"]["outcome_ids"] = ["9702_t08_m03_o02", "9702_t08_m03_o03"]

    finalize_enrichment(ed)
    save_json(enr_path, ed)


def repair_s22_22_q06():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s22_qp_22/question_06.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s22_22_q06.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_6_1",
            "label": "Fig. 6.1",
            "file": "figure_6_1.png",
            "introduced_by": "9702_s22_22_q06_a",
            "referenced_by": [
                "9702_s22_22_q06_a"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_s22_22_q06_a",
                "anchor": "A network of three resistors of resistances R_{1}, R_{2} and R_{3} is shown in Fig. 6.1."
            }
        },
        {
            "id": "fig_6_2",
            "label": "Fig. 6.2",
            "file": "figure_6_2.png",
            "introduced_by": "9702_s22_22_q06_b",
            "referenced_by": [
                "9702_s22_22_q06_b"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_s22_22_q06_b",
                "anchor": "as shown in Fig. 6.2."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s22_22_q06_a"]
    p_a["question_text"] = (
        "A network of three resistors of resistances R_{1}, R_{2} and R_{3} is shown in Fig. 6.1.\n"
        "The individual potential differences across the resistors are V_{1}, V_{2} and V_{3}. The current in the "
        "combination of resistors is I and the total potential difference across the combination is V.\n"
        "Show that the combined resistance R of the network is given by\n"
        "R = R_{1} + R_{2} + R_{3}."
    )
    p_a["question_text_latex"] = (
        "A network of three resistors of resistances $R_{1}$, $R_{2}$ and $R_{3}$ is shown in Fig. 6.1.\n"
        "The individual potential differences across the resistors are $V_{1}$, $V_{2}$ and $V_{3}$. The current in the "
        "combination of resistors is $I$ and the total potential difference across the combination is $V$.\n"
        "Show that the combined resistance $R$ of the network is given by\n"
        "$$R = R_{1} + R_{2} + R_{3}.$$"
    )
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q06_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q06_a_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Derivation",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_s22_22_q06_b"]
    p_b["question_text"] = (
        "A battery of electromotive force (e.m.f.) 8.0 V and negligible internal resistance is connected "
        "to a thermistor, a switch X and two fixed resistors, as shown in Fig. 6.2.\n"
        "Resistor R_{1} has resistance 6.0 kΩ and resistor R_{2} has resistance 4.0 kΩ."
    )
    p_b["question_text_latex"] = (
        "A battery of electromotive force (e.m.f.) $8.0\\text{ V}$ and negligible internal resistance is connected "
        "to a thermistor, a switch X and two fixed resistors, as shown in Fig. 6.2.\n"
        "Resistor $R_{1}$ has resistance $6.0\\text{ k}\\Omega$ and resistor $R_{2}$ has resistance $4.0\\text{ k}\\Omega$."
    )

    p_bi = parts_by_id["9702_s22_22_q06_b_i"]
    p_bi["question_text"] = "Switch X is open.\nCalculate the potential difference across R_{1}.\npotential difference = V"
    p_bi["question_text_latex"] = "Switch X is open.\nCalculate the potential difference across $R_{1}$.\n$$\\text{potential difference} = \\text{.................................................... V}$$"
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q06_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q06_b_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "potential difference",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{V}"
                        }
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_s22_22_q06_b_ii"]
    p_bii["question_text"] = (
        "Switch X is now closed. The resistance of the thermistor is 12.0 kΩ.\n"
        "Calculate the current in the battery.\n"
        "current = A"
    )
    p_bii["question_text_latex"] = (
        "Switch X is now closed. The resistance of the thermistor is $12.0\\text{ k}\\Omega$.\n"
        "Calculate the current in the battery.\n"
        "$$\\text{current} = \\text{.................................................... A}$$"
    )
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q06_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q06_b_ii_value",
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

    p_c = parts_by_id["9702_s22_22_q06_c"]
    p_c["question_text"] = (
        "The switch X in the circuit in (b) remains closed. The temperature of the thermistor decreases.\n"
        "By reference to the current in the battery, state and explain the effect, if any, of the decrease in temperature on the power produced by the battery."
    )
    p_c["question_text_latex"] = (
        "The switch X in the circuit in (b) remains closed. The temperature of the thermistor decreases.\n"
        "By reference to the current in the battery, state and explain the effect, if any, of the decrease in temperature on the power produced by the battery."
    )
    p_c["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q06_c_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q06_c_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "State and explanation",
                        "required": True
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_s22_22_q06_c"]["mapping"]["outcome_ids"] = ["9702_t10_m02_o07"]

    finalize_enrichment(ed)
    save_json(enr_path, ed)


def repair_s22_22_q07():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s22_qp_22/question_07.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s22_22_q07.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s22_22_q07_a"]
    p_a["question_text"] = (
        "A nucleus of caesium-137 (^{137}_{55}Cs) decays by emitting a β^{-} particle to produce a nucleus of an element X and an antineutrino. "
        "The decay is represented by\n"
        "^{137}_{55}Cs → ^{Q}_{S}X + ^{P}_{R}β^{-} + ^{0}_{0}ν."
    )
    p_a["question_text_latex"] = (
        "A nucleus of caesium-137 ($^{137}_{55}\\text{Cs}$) decays by emitting a $\\beta^{-}$ particle to produce a nucleus of an element X and an antineutrino. "
        "The decay is represented by\n"
        "$$^{137}_{55}\\text{Cs} \\rightarrow {^{Q}_{S}\\text{X}} + {^{P}_{R}\\beta^{-}} + {^{0}_{0}\\bar{\\nu}}$$"
    )

    p_ai = parts_by_id["9702_s22_22_q07_a_i"]
    p_ai["question_text"] = "State the number represented by each of the following letters."
    p_ai["question_text_latex"] = (
        "State the number represented by each of the following letters.\n"
        "$$P = \\text{........................} \\qquad Q = \\text{........................}$$\n"
        "$$R = \\text{........................} \\qquad S = \\text{........................}$$"
    )
    p_ai["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q07_a_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q07_a_i_p",
                        "control": "short_text",
                        "role": "answer",
                        "label": "P",
                        "required": True
                    },
                    {
                        "field_id": "9702_s22_22_q07_a_i_q",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Q",
                        "required": True
                    },
                    {
                        "field_id": "9702_s22_22_q07_a_i_r",
                        "control": "short_text",
                        "role": "answer",
                        "label": "R",
                        "required": True
                    },
                    {
                        "field_id": "9702_s22_22_q07_a_i_s",
                        "control": "short_text",
                        "role": "answer",
                        "label": "S",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_aii = parts_by_id["9702_s22_22_q07_a_ii"]
    p_aii["question_text"] = "State the name of the class (group) of particles that includes the β^{-} particle and the antineutrino."
    p_aii["question_text_latex"] = "State the name of the class (group) of particles that includes the $\\beta^{-}$ particle and the antineutrino."
    p_aii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q07_a_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q07_a_ii_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Class of particles",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_s22_22_q07_b"]
    p_b["question_text"] = (
        "A particle Y has a quark composition of ddd where d represents a down quark.\n"
        "A particle Z has a quark composition of u̅ d where u̅ represents an up antiquark."
    )
    p_b["question_text_latex"] = (
        "A particle Y has a quark composition of $ddd$ where $d$ represents a down quark.\n"
        "A particle Z has a quark composition of $\\bar{u}d$ where $\\bar{u}$ represents an up antiquark."
    )

    p_bi = parts_by_id["9702_s22_22_q07_b_i"]
    p_bi["question_text"] = "Show that the charges of particles Y and Z are equal."
    p_bi["question_text_latex"] = "Show that the charges of particles Y and Z are equal."
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q07_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q07_b_i_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Proof",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_s22_22_q07_b_ii"]
    p_bii["question_text"] = "State and explain which particle is a meson and which particle is a baryon."
    p_bii["question_text_latex"] = "State and explain which particle is a meson and which particle is a baryon."
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_22_q07_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_22_q07_b_ii_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "State and explanation",
                        "required": True
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    finalize_enrichment(ed)
    save_json(enr_path, ed)


# ==============================================================================
# 9702_s22_23
# ==============================================================================

def repair_s22_23_q01():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s22_qp_23/question_01.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s22_23_q01.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["question_stem"] = "A solid metal sphere has a diameter of (3.42 ± 0.02) cm and a mass of (67 ± 2) g."
    qd["question_stem_latex"] = "A solid metal sphere has a diameter of $(3.42 \\pm 0.02)\\text{ cm}$ and a mass of $(67 \\pm 2)\\text{ g}$."

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s22_23_q01_a"]
    p_a["question_text"] = "Calculate the density, in g cm^{-3}, of the metal.\ndensity = g cm^{-3}"
    p_a["question_text_latex"] = "Calculate the density, in $\\text{g cm}^{-3}$, of the metal.\n$$\\text{density} = \\text{.................................................... g cm}^{-3}$$"
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q01_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q01_a_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "density",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{g cm}^{-3}"
                        }
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_s22_23_q01_b"]
    p_b["question_text"] = "Determine the percentage uncertainty in the density.\npercentage uncertainty = %"
    p_b["question_text_latex"] = "Determine the percentage uncertainty in the density.\n$$\\text{percentage uncertainty} = \\text{.................................................... }\\%$$"
    p_b["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q01_b_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q01_b_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "percentage uncertainty",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\%"
                        }
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    finalize_enrichment(ed)
    save_json(enr_path, ed)


def repair_s22_23_q02():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s22_qp_23/question_02.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s22_23_q02.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["question_stem"] = (
        "An archer releases an arrow towards a target at a velocity of 65.0 m s^{-1} at an angle of 4.30° above the horizontal, as shown in Fig. 2.1.\n"
        "When released, the tip of the arrow is a horizontal distance of 70.0 m from the target and 1.66 m above the horizontal ground.\n"
        "The arrow hits the centre of the target.\n"
        "Assume that air resistance is negligible and that all the mass of the arrow is at its tip."
    )
    qd["question_stem_latex"] = (
        "An archer releases an arrow towards a target at a velocity of $65.0\\text{ m s}^{-1}$ at an angle of $4.30^\\circ$ above the horizontal, as shown in Fig. 2.1.\n"
        "When released, the tip of the arrow is a horizontal distance of $70.0\\text{ m}$ from the target and $1.66\\text{ m}$ above the horizontal ground.\n"
        "The arrow hits the centre of the target.\n"
        "Assume that air resistance is negligible and that all the mass of the arrow is at its tip."
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
                "anchor": "An archer releases an arrow towards a target at a velocity of 65.0 m s^{-1} at an angle of 4.30° above the horizontal, as shown in Fig. 2.1."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s22_23_q02_a"]
    p_a["question_text"] = "Show that the time taken for the arrow to reach the target is 1.08 s."
    p_a["question_text_latex"] = "Show that the time taken for the arrow to reach the target is $1.08\\text{ s}$."
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q02_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q02_a_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Proof",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_s22_23_q02_b"]
    p_b["question_text"] = "Calculate the height of the centre of the target above the ground.\nheight above ground = m"
    p_b["question_text_latex"] = "Calculate the height of the centre of the target above the ground.\n$$\\text{height above ground} = \\text{.................................................... m}$$"
    p_b["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q02_b_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q02_b_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "height above ground",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{m}"
                        }
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_s22_23_q02_c"]
    p_c["question_text"] = (
        "By considering energy changes, state and explain how the final kinetic energy of the arrow as it hits the target compares with its initial kinetic energy immediately after release. "
        "A numerical calculation is not required."
    )
    p_c["question_text_latex"] = (
        "By considering energy changes, state and explain how the final kinetic energy of the arrow as it hits the target compares with its initial kinetic energy immediately after release. "
        "A numerical calculation is not required."
    )
    p_c["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q02_c_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q02_c_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "State and explanation",
                        "required": True
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    finalize_enrichment(ed)
    save_json(enr_path, ed)


def repair_s22_23_q03():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s22_qp_23/question_03.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s22_23_q03.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_3_1",
            "label": "Fig. 3.1",
            "file": "figure_3_1.png",
            "introduced_by": "9702_s22_23_q03_b_ii",
            "referenced_by": [
                "9702_s22_23_q03_b_ii",
                "9702_s22_23_q03_c_i"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "response_background",
                "part_id": "9702_s22_23_q03_b_ii",
                "anchor": "On Fig. 3.1, sketch a graph showing the variation with time t of the velocity v of the car for the first 20 seconds of its motion."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s22_23_q03_a"]
    p_a["question_text"] = "Define velocity."
    p_a["question_text_latex"] = "Define velocity."
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q03_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q03_a_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Definition",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_s22_23_q03_b"]
    p_b["question_text"] = (
        "A constant driving force of 2400 N acts on a car of mass 1200 kg. "
        "The car accelerates from rest in a straight line along a horizontal road.\n"
        "Assume that the resistive forces acting on the car are negligible."
    )
    p_b["question_text_latex"] = (
        "A constant driving force of $2400\\text{ N}$ acts on a car of mass $1200\\text{ kg}$. "
        "The car accelerates from rest in a straight line along a horizontal road.\n"
        "Assume that the resistive forces acting on the car are negligible."
    )

    p_bi = parts_by_id["9702_s22_23_q03_b_i"]
    p_bi["question_text"] = "Calculate the acceleration of the car.\nacceleration = m s^{-2}"
    p_bi["question_text_latex"] = "Calculate the acceleration of the car.\n$$\\text{acceleration} = \\text{.................................................... m s}^{-2}$$"
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q03_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q03_b_i_value",
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

    p_bii = parts_by_id["9702_s22_23_q03_b_ii"]
    p_bii["question_text"] = "On Fig. 3.1, sketch a graph showing the variation with time t of the velocity v of the car for the first 20 seconds of its motion."
    p_bii["question_text_latex"] = "On Fig. 3.1, sketch a graph showing the variation with time $t$ of the velocity $v$ of the car for the first $20\\text{ seconds}$ of its motion."
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q03_b_ii_canvas",
                "type": "canvas",
                "background_figure_id": "fig_3_1"
            }
        ]
    }

    p_c = parts_by_id["9702_s22_23_q03_c"]
    p_c["question_text"] = (
        "In reality, a resistive force due to air resistance acts on the car in (b). "
        "This resistive force increases with speed until it becomes equal in magnitude to the driving force at time t = 12 s."
    )
    p_c["question_text_latex"] = (
        "In reality, a resistive force due to air resistance acts on the car in (b). "
        "This resistive force increases with speed until it becomes equal in magnitude to the driving force at time $t = 12\\text{ s}$."
    )

    p_ci = parts_by_id["9702_s22_23_q03_c_i"]
    p_ci["question_text"] = "On Fig. 3.1, sketch a second line to show the variation with time t of the velocity v of the car for the first 20 seconds of its motion. Label this line B."
    p_ci["question_text_latex"] = "On Fig. 3.1, sketch a second line to show the variation with time $t$ of the velocity $v$ of the car for the first $20\\text{ seconds}$ of its motion. Label this line B."
    p_ci["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q03_c_i_canvas",
                "type": "canvas",
                "background_figure_id": "fig_3_1"
            }
        ]
    }

    p_cii = parts_by_id["9702_s22_23_q03_c_ii"]
    p_cii["question_text"] = (
        "At time t = 20 s, the driving force is increased to 3000 N and remains constant at this value.\n"
        "Describe how the velocity of the car changes due to this increase in the driving force."
    )
    p_cii["question_text_latex"] = (
        "At time $t = 20\\text{ s}$, the driving force is increased to $3000\\text{ N}$ and remains constant at this value.\n"
        "Describe how the velocity of the car changes due to this increase in the driving force."
    )
    p_cii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q03_c_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q03_c_ii_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Description",
                        "required": True
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    finalize_enrichment(ed)
    save_json(enr_path, ed)


def repair_s22_23_q04():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s22_qp_23/question_04.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s22_23_q04.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_4_1",
            "label": "Fig. 4.1",
            "file": "figure_4_1.png",
            "introduced_by": "9702_s22_23_q04_b",
            "referenced_by": [
                "9702_s22_23_q04_b"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_s22_23_q04_b",
                "anchor": "A 0.60 kg mass is attached to a string which is wrapped around the wheel of a generator, as shown in Fig. 4.1."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s22_23_q04_a"]
    p_a["question_text"] = (
        "A mass m moves a vertical distance Δh in a uniform gravitational field and gains gravitational potential energy ΔE_{P}. "
        "The acceleration of free fall is g.\n"
        "Use the concept of work done to show that\n"
        "ΔE_{P} = mgΔh."
    )
    p_a["question_text_latex"] = (
        "A mass $m$ moves a vertical distance $\\Delta h$ in a uniform gravitational field and gains gravitational potential energy $\\Delta E_{\\text{P}}$. "
        "The acceleration of free fall is $g$.\n"
        "Use the concept of work done to show that\n"
        "$$\\Delta E_{\\text{P}} = mg\\Delta h.$$"
    )
    p_a["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q04_a_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q04_a_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Proof",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_s22_23_q04_b"]
    p_b["question_text"] = (
        "A 0.60 kg mass is attached to a string which is wrapped around the wheel of a generator, as shown in Fig. 4.1.\n"
        "The mass is held stationary above the floor. When released, the mass initially accelerates and then falls at a steady speed and spins the wheel. "
        "The generator causes a current in a resistor. Air resistance is negligible.\n"
        "State the main energy change when the mass is falling at a steady speed.\n"
        "energy to energy."
    )
    p_b["question_text_latex"] = (
        "A $0.60\\text{ kg}$ mass is attached to a string which is wrapped around the wheel of a generator, as shown in Fig. 4.1.\n"
        "The mass is held stationary above the floor. When released, the mass initially accelerates and then falls at a steady speed and spins the wheel. "
        "The generator causes a current in a resistor. Air resistance is negligible.\n"
        "State the main energy change when the mass is falling at a steady speed.\n"
        "$$\\text{.................................................... energy to .................................................... energy}$$"
    )
    p_b["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q04_b_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q04_b_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Energy change",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_c = parts_by_id["9702_s22_23_q04_c"]
    p_c["question_text"] = (
        "When falling at a steady speed, the mass in (b) falls through a vertical distance of 1.4 m in a time of 4.0 s. "
        "This causes a current of 90 mA in the resistor. The resistance of the resistor is 47 Ω.\n"
        "Calculate:"
    )
    p_c["question_text_latex"] = (
        "When falling at a steady speed, the mass in (b) falls through a vertical distance of $1.4\\text{ m}$ in a time of $4.0\\text{ s}$. "
        "This causes a current of $90\\text{ mA}$ in the resistor. The resistance of the resistor is $47\\,\\Omega$.\n"
        "Calculate:"
    )

    p_ci = parts_by_id["9702_s22_23_q04_c_i"]
    p_ci["question_text"] = "the rate of work done by the falling mass\nrate of work done = W"
    p_ci["question_text_latex"] = "the rate of work done by the falling mass\n$$\\text{rate of work done} = \\text{.................................................... W}$$"
    p_ci["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q04_c_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q04_c_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "rate of work done",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{W}"
                        }
                    }
                ]
            }
        ]
    }

    p_cii = parts_by_id["9702_s22_23_q04_c_ii"]
    p_cii["question_text"] = "the power dissipated in the resistor\npower = W"
    p_cii["question_text_latex"] = "the power dissipated in the resistor\n$$\\text{power} = \\text{.................................................... W}$$"
    p_cii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q04_c_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q04_c_ii_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "power",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{W}"
                        }
                    }
                ]
            }
        ]
    }

    p_ciii = parts_by_id["9702_s22_23_q04_c_iii"]
    p_ciii["question_text"] = "the efficiency of the generator.\nefficiency ="
    p_ciii["question_text_latex"] = "the efficiency of the generator.\n$$\\text{efficiency} = \\text{....................................................}$$"
    p_ciii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q04_c_iii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q04_c_iii_value",
                        "control": "short_text",
                        "role": "answer",
                        "label": "efficiency",
                        "required": True
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_s22_23_q04_c_i"]["mapping"]["outcome_ids"] = ["9702_t05_m01_o06"]
    ed_parts["9702_s22_23_q04_c_ii"]["skills"]["primary_skill_id"] = "9702_skill_potential_difference_power"

    finalize_enrichment(ed)
    save_json(enr_path, ed)


def repair_s22_23_q05():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s22_qp_23/question_05.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s22_23_q05.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_5_1",
            "label": "Fig. 5.1",
            "file": "figure_5_1.png",
            "introduced_by": "9702_s22_23_q05_a",
            "referenced_by": [
                "9702_s22_23_q05_a"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_s22_23_q05_a",
                "anchor": "Parallel light rays from the Sun are incident normally on a magnifying glass. The magnifying glass directs the light to an area A of radius r, as shown in Fig. 5.1."
            }
        },
        {
            "id": "fig_5_2",
            "label": "Fig. 5.2",
            "file": "figure_5_2.png",
            "introduced_by": "9702_s22_23_q05_b_iii",
            "referenced_by": [
                "9702_s22_23_q05_b_iii"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_s22_23_q05_b_iii",
                "anchor": "as shown in Fig. 5.2."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s22_23_q05_a"]
    p_a["question_text"] = (
        "Parallel light rays from the Sun are incident normally on a magnifying glass. The magnifying glass directs the light to an area A of radius r, as shown in Fig. 5.1.\n"
        "The magnifying glass is circular in cross‑section with a radius of 5.5 cm. The intensity of the light from the Sun incident on the magnifying glass is 1.3 kW m^{-2}.\n"
        "Assume that all of the light incident on the magnifying glass is transmitted through it."
    )
    p_a["question_text_latex"] = (
        "Parallel light rays from the Sun are incident normally on a magnifying glass. The magnifying glass directs the light to an area A of radius $r$, as shown in Fig. 5.1.\n"
        "The magnifying glass is circular in cross‑section with a radius of $5.5\\text{ cm}$. The intensity of the light from the Sun incident on the magnifying glass is $1.3\\text{ kW m}^{-2}$.\n"
        "Assume that all of the light incident on the magnifying glass is transmitted through it."
    )

    p_ai = parts_by_id["9702_s22_23_q05_a_i"]
    p_ai["question_text"] = "Calculate the power of the light from the Sun incident on the magnifying glass.\npower = W"
    p_ai["question_text_latex"] = "Calculate the power of the light from the Sun incident on the magnifying glass.\n$$\\text{power} = \\text{.................................................... W}$$"
    p_ai["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q05_a_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q05_a_i_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "power",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{W}"
                        }
                    }
                ]
            }
        ]
    }

    p_aii = parts_by_id["9702_s22_23_q05_a_ii"]
    p_aii["question_text"] = "The value of r is 1.5 mm.\nCalculate the intensity of the light on area A.\nintensity = W m^{-2}"
    p_aii["question_text_latex"] = "The value of $r$ is $1.5\\text{ mm}$.\nCalculate the intensity of the light on area A.\n$$\\text{intensity} = \\text{.................................................... W m}^{-2}$$"
    p_aii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q05_a_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q05_a_ii_value",
                        "control": "quantity",
                        "role": "answer",
                        "label": "intensity",
                        "required": True,
                        "unit": {
                            "unit_latex": "\\text{W m}^{-2}"
                        }
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_s22_23_q05_b"]
    p_b["question_text"] = "A laser emits a beam of electromagnetic waves of frequency 3.7 × 10^{15} Hz in a vacuum."
    p_b["question_text_latex"] = "A laser emits a beam of electromagnetic waves of frequency $3.7 \\times 10^{15}\\text{ Hz}$ in a vacuum."

    p_bi = parts_by_id["9702_s22_23_q05_b_i"]
    p_bi["question_text"] = "Show that the wavelength of the waves is 8.1 × 10^{-8} m."
    p_bi["question_text_latex"] = "Show that the wavelength of the waves is $8.1 \\times 10^{-8}\\text{ m}$."
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q05_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q05_b_i_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Proof",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_s22_23_q05_b_ii"]
    p_bii["question_text"] = "State the region of the electromagnetic spectrum to which these waves belong."
    p_bii["question_text_latex"] = "State the region of the electromagnetic spectrum to which these waves belong."
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q05_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q05_b_ii_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Region of spectrum",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_biii = parts_by_id["9702_s22_23_q05_b_iii"]
    p_biii["question_text"] = (
        "The beam from the laser now passes through a diffraction grating with 2400 lines per millimetre. "
        "A detector sensitive to the waves emitted by the laser is moved through an arc of 180° in order to detect the maxima produced by the waves passing through the grating, as shown in Fig. 5.2.\n"
        "Calculate the number of maxima detected as the detector moves through 180° along the line shown in Fig. 5.2. Show your working.\n"
        "number of maxima detected ="
    )
    p_biii["question_text_latex"] = (
        "The beam from the laser now passes through a diffraction grating with $2400\\text{ lines per millimetre}$. "
        "A detector sensitive to the waves emitted by the laser is moved through an arc of $180^\\circ$ in order to detect the maxima produced by the waves passing through the grating, as shown in Fig. 5.2.\n"
        "Calculate the number of maxima detected as the detector moves through $180^\\circ$ along the line shown in Fig. 5.2. Show your working.\n"
        "$$\\text{number of maxima detected} = \\text{....................................................}$$"
    )
    p_biii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q05_b_iii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q05_b_iii_value",
                        "control": "short_text",
                        "role": "answer",
                        "label": "number of maxima detected",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_biv = parts_by_id["9702_s22_23_q05_b_iv"]
    p_biv["question_text"] = (
        "The laser is now replaced with one that emits electromagnetic waves with a wavelength of 300 nm.\n"
        "Explain, without calculation, what happens to the number of maxima now detected.\n"
        "Assume that the detector is also sensitive to this wavelength of electromagnetic waves."
    )
    p_biv["question_text_latex"] = (
        "The laser is now replaced with one that emits electromagnetic waves with a wavelength of $300\\text{ nm}$.\n"
        "Explain, without calculation, what happens to the number of maxima now detected.\n"
        "Assume that the detector is also sensitive to this wavelength of electromagnetic waves."
    )
    p_biv["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q05_b_iv_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q05_b_iv_answer",
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
    ed_parts["9702_s22_23_q05_b_i"]["mapping"]["outcome_ids"] = ["9702_t07_m04_o01"]

    finalize_enrichment(ed)
    save_json(enr_path, ed)


def repair_s22_23_q06():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s22_qp_23/question_06.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s22_23_q06.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["figures"] = [
        {
            "id": "fig_6_1",
            "label": "Fig. 6.1",
            "file": "figure_6_1.png",
            "introduced_by": "9702_s22_23_q06_a_i",
            "referenced_by": [
                "9702_s22_23_q06_a_i"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "response_background",
                "part_id": "9702_s22_23_q06_a_i",
                "anchor": "On Fig. 6.1, sketch the I–V characteristic of a filament lamp."
            }
        },
        {
            "id": "fig_6_2",
            "label": "Fig. 6.2",
            "file": "figure_6_2.png",
            "introduced_by": "9702_s22_23_q06_c",
            "referenced_by": [
                "9702_s22_23_q06_c"
            ],
            "mapping_method": "explicit_text_reference",
            "mapping_confidence": 1.0,
            "placement": {
                "scope": "part",
                "position": "after_text",
                "part_id": "9702_s22_23_q06_c",
                "anchor": "The circuit is shown in Fig. 6.2."
            }
        }
    ]

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_ai = parts_by_id["9702_s22_23_q06_a_i"]
    p_ai["question_text"] = "On Fig. 6.1, sketch the I–V characteristic of a filament lamp."
    p_ai["question_text_latex"] = "On Fig. 6.1, sketch the $I\\text{--}V$ characteristic of a filament lamp."
    p_ai["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q06_a_i_canvas",
                "type": "canvas",
                "background_figure_id": "fig_6_1"
            }
        ]
    }

    p_aii = parts_by_id["9702_s22_23_q06_a_ii"]
    p_aii["question_text"] = "Explain the shape of the line in (a)(i)."
    p_aii["question_text_latex"] = "Explain the shape of the line in (a)(i)."
    p_aii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q06_a_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q06_a_ii_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Explanation",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_s22_23_q06_b"]
    p_b["question_text"] = (
        "A conducting wire has length 5.8 m and cross‑sectional area 3.4 × 10^{-8} m^{2}. "
        "The resistivity of the metal of the wire is 5.6 × 10^{-8} Ω m.\n"
        "Calculate the resistance of the wire.\n"
        "resistance = Ω"
    )
    p_b["question_text_latex"] = (
        "A conducting wire has length $5.8\\text{ m}$ and cross‑sectional area $3.4 \\times 10^{-8}\\text{ m}^{2}$. "
        "The resistivity of the metal of the wire is $5.6 \\times 10^{-8}\\,\\Omega\\text{ m}$.\n"
        "Calculate the resistance of the wire.\n"
        "$$\\text{resistance} = \\text{.................................................... }\\Omega$$"
    )
    p_b["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q06_b_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q06_b_value",
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

    p_c = parts_by_id["9702_s22_23_q06_c"]
    p_c["question_text"] = (
        "A resistor of resistance R is placed in a circuit with a cell of negligible internal resistance, two switches S_{1} and S_{2}, "
        "a second resistor of resistance 2R and three ammeters X, Y and Z. The circuit is shown in Fig. 6.2.\n"
        "The reading on X is 1.0 A when S_{1} is open and S_{2} is closed.\n"
        "Complete Table 6.1.\n"
        "Table 6.1\n"
        "position of switches | reading on X / A | reading on Y / A | reading on Z / A\n"
        "S_{1} open, S_{2} open | 0 | 0 | 0\n"
        "S_{1} open, S_{2} closed | 1.0 | | \n"
        "S_{1} closed, S_{2} open | | | \n"
        "S_{1} closed, S_{2} closed | | | "
    )
    p_c["question_text_latex"] = (
        "A resistor of resistance $R$ is placed in a circuit with a cell of negligible internal resistance, two switches $S_{1}$ and $S_{2}$, "
        "a second resistor of resistance $2R$ and three ammeters X, Y and Z. The circuit is shown in Fig. 6.2.\n"
        "The reading on X is $1.0\\text{ A}$ when $S_{1}$ is open and $S_{2}$ is closed.\n"
        "Complete Table 6.1.\n"
        "Table 6.1\n"
        "position of switches | reading on X / A | reading on Y / A | reading on Z / A\n"
        "$S_{1}$ open, $S_{2}$ open | 0 | 0 | 0\n"
        "$S_{1}$ open, $S_{2}$ closed | 1.0 | | \n"
        "$S_{1}$ closed, $S_{2}$ open | | | \n"
        "$S_{1}$ closed, $S_{2}$ closed | | | "
    )
    p_c["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q06_c_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q06_c_row2_y",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Row 2: reading on Y / A",
                        "required": True
                    },
                    {
                        "field_id": "9702_s22_23_q06_c_row2_z",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Row 2: reading on Z / A",
                        "required": True
                    },
                    {
                        "field_id": "9702_s22_23_q06_c_row3_x",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Row 3: reading on X / A",
                        "required": True
                    },
                    {
                        "field_id": "9702_s22_23_q06_c_row3_y",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Row 3: reading on Y / A",
                        "required": True
                    },
                    {
                        "field_id": "9702_s22_23_q06_c_row3_z",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Row 3: reading on Z / A",
                        "required": True
                    },
                    {
                        "field_id": "9702_s22_23_q06_c_row4_x",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Row 4: reading on X / A",
                        "required": True
                    },
                    {
                        "field_id": "9702_s22_23_q06_c_row4_y",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Row 4: reading on Y / A",
                        "required": True
                    },
                    {
                        "field_id": "9702_s22_23_q06_c_row4_z",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Row 4: reading on Z / A",
                        "required": True
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    ed_parts = {p["part_id"]: p for p in ed["parts"]}
    ed_parts["9702_s22_23_q06_c"]["mapping"]["primary_topic_id"] = "9702_t10"
    ed_parts["9702_s22_23_q06_c"]["mapping"]["primary_module_id"] = "9702_t10_m02"
    ed_parts["9702_s22_23_q06_c"]["mapping"]["outcome_ids"] = ["9702_t10_m02_o01", "9702_t10_m02_o07"]

    finalize_enrichment(ed)
    save_json(enr_path, ed)


def repair_s22_23_q07():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s22_qp_23/question_07.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s22_23_q07.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s22_23_q07_a"]
    p_a["question_text"] = (
        "Fluorine‑18 (^{18}_{9}F) is an isotope that decays to an isotope of oxygen (O) by the emission of a β^{+} particle."
    )
    p_a["question_text_latex"] = (
        "Fluorine‑18 ($^{18}_{9}\\text{F}$) is an isotope that decays to an isotope of oxygen (O) by the emission of a $\\beta^{+}$ particle."
    )

    p_ai = parts_by_id["9702_s22_23_q07_a_i"]
    p_ai["question_text"] = "Complete the nuclear equation for the decay, including all the particles involved.\n^{18}_{9}F →"
    p_ai["question_text_latex"] = "Complete the nuclear equation for the decay, including all the particles involved.\n$$^{18}_{9}\\text{F} \\rightarrow \\text{....................................................}$$"
    p_ai["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q07_a_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q07_a_i_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "Decay equation",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_aii = parts_by_id["9702_s22_23_q07_a_ii"]
    p_aii["question_text"] = (
        "A quark in the fluorine‑18 nucleus changes flavour during the decay. State this change of flavour.\n"
        "quark to quark."
    )
    p_aii["question_text_latex"] = (
        "A quark in the fluorine‑18 nucleus changes flavour during the decay. State this change of flavour.\n"
        "$$\\text{.................................................... quark to .................................................... quark}$$"
    )
    p_aii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q07_a_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q07_a_ii_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Quark flavour change",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_b = parts_by_id["9702_s22_23_q07_b"]
    p_b["question_text"] = "A hadron has a charge of –2e, where e is the elementary charge."
    p_b["question_text_latex"] = "A hadron has a charge of $-2e$, where $e$ is the elementary charge."

    p_bi = parts_by_id["9702_s22_23_q07_b_i"]
    p_bi["question_text"] = "State and explain whether the hadron is a meson or a baryon."
    p_bi["question_text_latex"] = "State and explain whether the hadron is a meson or a baryon."
    p_bi["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q07_b_i_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q07_b_i_answer",
                        "control": "long_text",
                        "role": "answer",
                        "label": "State and explanation",
                        "required": True
                    }
                ]
            }
        ]
    }

    p_bii = parts_by_id["9702_s22_23_q07_b_ii"]
    p_bii["question_text"] = "State a possible quark composition for the hadron."
    p_bii["question_text_latex"] = "State a possible quark composition for the hadron.\n$$\\text{quark composition: ....................................................}$$"
    p_bii["response_schema"] = {
        "version": "0.1",
        "blocks": [
            {
                "block_id": "9702_s22_23_q07_b_ii_response",
                "type": "fields",
                "fields": [
                    {
                        "field_id": "9702_s22_23_q07_b_ii_answer",
                        "control": "short_text",
                        "role": "answer",
                        "label": "Quark composition",
                        "required": True
                    }
                ]
            }
        ]
    }

    finalize_question(qd)
    save_json(q_path, qd)

    finalize_enrichment(ed)
    save_json(enr_path, ed)


def main():
    print("=== Repairing 9702_s22_22 ===")
    repair_s22_22_q01()
    repair_s22_22_q02()
    repair_s22_22_q03()
    repair_s22_22_q04()
    repair_s22_22_q05()
    repair_s22_22_q06()
    repair_s22_22_q07()

    print("\n=== Repairing 9702_s22_23 ===")
    repair_s22_23_q01()
    repair_s22_23_q02()
    repair_s22_23_q03()
    repair_s22_23_q04()
    repair_s22_23_q05()
    repair_s22_23_q06()
    repair_s22_23_q07()
    print("\nDone!")

if __name__ == "__main__":
    main()
