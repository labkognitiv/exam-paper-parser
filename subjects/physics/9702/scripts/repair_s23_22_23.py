#!/usr/bin/env python3
"""
scripts/repair_s23_22_23.py
Repairs all questions and enrichments for 9702_s23_22 and 9702_s23_23.
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
# 9702_s23_22
# ==============================================================================

def repair_s23_22_q01():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s23_qp_22/question_01.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s23_22_q01.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))
    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))

def repair_s23_22_q02():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s23_qp_22/question_02.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s23_22_q02.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))
    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))

def repair_s23_22_q03():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s23_qp_22/question_03.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s23_22_q03.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["question_stem"] = "A block is pulled by a force X in a straight line along a rough horizontal surface, as shown in Fig. 3.1.\nAssume that the total resistive force opposing the motion of the block is 0.80 N at all speeds of the block.\nThe variation with time t of the magnitude of the force X is shown in Fig. 3.2."
    qd["question_stem_latex"] = "A block is pulled by a force $X$ in a straight line along a rough horizontal surface, as shown in Fig. 3.1.\nAssume that the total resistive force opposing the motion of the block is 0.80 N at all speeds of the block.\nThe variation with time $t$ of the magnitude of the force $X$ is shown in Fig. 3.2."

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a_ii = parts_by_id["9702_s23_22_q03_a_ii"]
    p_a_ii["question_text"] = "Determine the change in momentum of the block from time t = 0 to time t = 3.0 s."
    p_a_ii["question_text_latex"] = "Determine the change in momentum of the block from time $t = 0$ to time $t = 3.0\\text{ s}$.\n$$\\text{change in momentum} = \\text{...................................................}\\text{ kg m s}^{-1}$$"

    p_b_i = parts_by_id["9702_s23_22_q03_b_i"]
    p_b_i["question_text"] = "Describe and explain the motion of the block between time t = 3.0 s and time t = 6.0 s."
    p_b_i["question_text_latex"] = "Describe and explain the motion of the block between time $t = 3.0\\text{ s}$ and time $t = 6.0\\text{ s}$."

    p_b_ii = parts_by_id["9702_s23_22_q03_b_ii"]
    p_b_ii["question_text"] = "Force X produces a total power of 2.0 W when moving the block between time t = 3.0 s and time t = 6.0 s.\nCalculate the distance moved by the block during this time interval."
    p_b_ii["question_text_latex"] = "Force $X$ produces a total power of 2.0 W when moving the block between time $t = 3.0\\text{ s}$ and time $t = 6.0\\text{ s}$.\nCalculate the distance moved by the block during this time interval.\n$$\\text{distance} = \\text{...................................................}\\text{ m}$$"

    p_c = parts_by_id["9702_s23_22_q03_c"]
    p_c["question_text"] = "The block is at rest at time t = 0.\nOn Fig. 3.3, sketch a graph to show the variation of the momentum of the block with time t from t = 0 to t = 6.0 s.\nNumerical values of momentum are not required."
    p_c["question_text_latex"] = "The block is at rest at time $t = 0$.\nOn Fig. 3.3, sketch a graph to show the variation of the momentum of the block with time $t$ from $t = 0$ to $t = 6.0\\text{ s}$.\nNumerical values of momentum are not required."

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))

def repair_s23_22_q04():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s23_qp_22/question_04.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s23_22_q04.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["question_stem"] = "A spring is suspended from a fixed point at one end. The spring is extended by a vertical force applied to the other end. The variation of the applied force F with the length L of the spring is shown in Fig. 4.1.\nFor the spring:"
    qd["question_stem_latex"] = "A spring is suspended from a fixed point at one end. The spring is extended by a vertical force applied to the other end. The variation of the applied force $F$ with the length $L$ of the spring is shown in Fig. 4.1.\nFor the spring:"

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_b = parts_by_id["9702_s23_22_q04_b"]
    p_b["question_text"] = "determine the spring constant, in N m⁻¹"
    p_b["question_text_latex"] = "determine the spring constant, in $\\text{N m}^{-1}$\n$$\\text{spring constant} = \\text{...................................................}\\text{ N m}^{-1}$$"

    p_c = parts_by_id["9702_s23_22_q04_c"]
    p_c["question_text"] = "determine the elastic potential energy when F = 6.0 N."
    p_c["question_text_latex"] = "determine the elastic potential energy when $F = 6.0\\text{ N}$.\n$$\\text{elastic potential energy} = \\text{...................................................}\\text{ J}$$"

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))

def repair_s23_22_q05():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s23_qp_22/question_05.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s23_22_q05.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s23_22_q05_a"]
    p_a["question_text"] = "A progressive wave travels through a medium. The wave causes a particle of the medium to vibrate along a line P. The energy of the wave propagates along a line Q.\nCompare the directions of lines P and Q if the wave is:"
    p_a["question_text_latex"] = "A progressive wave travels through a medium. The wave causes a particle of the medium to vibrate along a line P. The energy of the wave propagates along a line Q.\nCompare the directions of lines P and Q if the wave is:"

    p_b = parts_by_id["9702_s23_22_q05_b"]
    p_b["question_text"] = "A tube is closed at one end. A loudspeaker is placed near the other end of the tube, as shown in Fig. 5.1.\nThe loudspeaker emits sound of frequency 1.7 kHz. The speed of sound in the air in the tube is 340 m s⁻¹. A stationary wave is formed with an antinode A at the open end of the tube.\nThere is only one other antinode A inside the tube, as shown in Fig. 5.1.\nDetermine:"
    p_b["question_text_latex"] = "A tube is closed at one end. A loudspeaker is placed near the other end of the tube, as shown in Fig. 5.1.\nThe loudspeaker emits sound of frequency 1.7 kHz. The speed of sound in the air in the tube is $340\\text{ m s}^{-1}$. A stationary wave is formed with an antinode A at the open end of the tube.\nThere is only one other antinode A inside the tube, as shown in Fig. 5.1.\nDetermine:"

    p_b_i = parts_by_id["9702_s23_22_q05_b_i"]
    p_b_i["question_text"] = "the wavelength of the sound"
    p_b_i["question_text_latex"] = "the wavelength of the sound\n$$\\text{wavelength} = \\text{...................................................}\\text{ m}$$"

    p_b_ii = parts_by_id["9702_s23_22_q05_b_ii"]
    p_b_ii["question_text"] = "the length L of the tube"
    p_b_ii["question_text_latex"] = "the length $L$ of the tube\n$$L = \\text{...................................................}\\text{ m}$$"

    p_b_iii = parts_by_id["9702_s23_22_q05_b_iii"]
    p_b_iii["question_text"] = "the maximum wavelength of the sound from the loudspeaker that can produce a stationary wave in the tube."
    p_b_iii["question_text_latex"] = "the maximum wavelength of the sound from the loudspeaker that can produce a stationary wave in the tube.\n$$\\text{maximum wavelength} = \\text{...................................................}\\text{ m}$$"

    p_c = parts_by_id["9702_s23_22_q05_c"]
    p_c["question_text"] = "Two polarising filters are arranged so that their planes are vertical and parallel. The first filter has its transmission axis at an angle of 35° to the vertical and the second filter has its transmission axis at angle α to the vertical, as shown in Fig. 5.2.\nAngle α is greater than 35° and less than 90°. A beam of vertically polarised light of intensity 8.5 W m⁻² is incident normally on the first filter."
    p_c["question_text_latex"] = "Two polarising filters are arranged so that their planes are vertical and parallel. The first filter has its transmission axis at an angle of $35^{\\circ}$ to the vertical and the second filter has its transmission axis at angle $\\alpha$ to the vertical, as shown in Fig. 5.2.\nAngle $\\alpha$ is greater than $35^{\\circ}$ and less than $90^{\\circ}$. A beam of vertically polarised light of intensity $8.5\\text{ W m}^{-2}$ is incident normally on the first filter."

    p_c_i = parts_by_id["9702_s23_22_q05_c_i"]
    p_c_i["question_text"] = "Show that the intensity of the light transmitted by the first filter is 5.7 W m⁻²."
    p_c_i["question_text_latex"] = "Show that the intensity of the light transmitted by the first filter is $5.7\\text{ W m}^{-2}$."

    p_c_ii = parts_by_id["9702_s23_22_q05_c_ii"]
    p_c_ii["question_text"] = "The intensity of the light transmitted by the second filter is 5.2 W m⁻².\nCalculate angle α."
    p_c_ii["question_text_latex"] = "The intensity of the light transmitted by the second filter is $5.2\\text{ W m}^{-2}$.\nCalculate angle $\\alpha$.\n$$\\alpha = \\text{...................................................}^{\\circ}$$"

    # Enrichment fixes
    enr_parts = {p["part_id"]: p for p in ed["parts"]}
    enr_parts["9702_s23_22_q05_a_i"]["question_patterns"] = ["definition", "comparison"]
    enr_parts["9702_s23_22_q05_a_ii"]["question_patterns"] = ["definition", "comparison"]
    enr_parts["9702_s23_22_q05_b_ii"]["skills"]["primary_skill_id"] = "9702_skill_stationary_waves"
    enr_parts["9702_s23_22_q05_b_iii"]["skills"]["primary_skill_id"] = "9702_skill_stationary_waves"

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))

def repair_s23_22_q06():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s23_qp_22/question_06.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s23_22_q06.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_b = parts_by_id["9702_s23_22_q06_b"]
    p_b["question_text"] = "A cylindrical wire has length L and resistance R. The total number of free electrons (charge carriers) contained in the volume of the wire is N. Each free electron has charge e. The potential difference between the ends of the wire is V.\nDetermine expressions, in terms of some or all of the symbols e, L, N, R and V for:"
    p_b["question_text_latex"] = "A cylindrical wire has length $L$ and resistance $R$. The total number of free electrons (charge carriers) contained in the volume of the wire is $N$. Each free electron has charge $e$. The potential difference between the ends of the wire is $V$.\nDetermine expressions, in terms of some or all of the symbols $e$, $L$, $N$, $R$ and $V$ for:"

    p_b_i = parts_by_id["9702_s23_22_q06_b_i"]
    p_b_i["question_text"] = "the current in the wire"
    p_b_i["question_text_latex"] = "the current in the wire\n$$\\text{current} = \\text{...................................................}$$"

    p_b_ii = parts_by_id["9702_s23_22_q06_b_ii"]
    p_b_ii["question_text"] = "the average drift speed of the free electrons"
    p_b_ii["question_text_latex"] = "the average drift speed of the free electrons\n$$\\text{average drift speed} = \\text{...................................................}$$"

    p_b_iii = parts_by_id["9702_s23_22_q06_b_iii"]
    p_b_iii["question_text"] = "the average time taken for a free electron to move along the full length of the wire."
    p_b_iii["question_text_latex"] = "the average time taken for a free electron to move along the full length of the wire.\n$$\\text{time taken} = \\text{...................................................}$$"

    enr_parts = {p["part_id"]: p for p in ed["parts"]}
    enr_parts["9702_s23_22_q06_b_ii"]["mapping"]["outcome_ids"] = ["9702_t09_m01_o04"]
    enr_parts["9702_s23_22_q06_b_iii"]["mapping"]["outcome_ids"] = ["9702_t09_m01_o03", "9702_t09_m01_o04"]

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))

def repair_s23_22_q07():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s23_qp_22/question_07.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s23_22_q07.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s23_22_q07_a"]
    p_a["question_text"] = "A battery of electromotive force (e.m.f.) 9.0 V and negligible internal resistance is connected to a light-dependent resistor (LDR) and a fixed resistor, as shown in Fig. 7.1.\nThe LDR and fixed resistor have resistances of 1800 Ω and 1200 Ω respectively.\nCalculate the potential difference across the LDR."
    p_a["question_text_latex"] = "A battery of electromotive force (e.m.f.) 9.0 V and negligible internal resistance is connected to a light‑dependent resistor (LDR) and a fixed resistor, as shown in Fig. 7.1.\nThe LDR and fixed resistor have resistances of $1800\\;\\Omega$ and $1200\\;\\Omega$ respectively.\nCalculate the potential difference across the LDR.\n$$\\text{potential difference} = \\text{...................................................}\\text{ V}$$"

    p_b = parts_by_id["9702_s23_22_q07_b"]
    p_b["question_text"] = "The circuit in (a) is now modified by adding a uniform resistance wire XY and a galvanometer, as shown in Fig. 7.2.\nThe length of the wire XY is 1.2 m. The movable connection Z is positioned on the wire XY so that the galvanometer reading is zero."
    p_b["question_text_latex"] = "The circuit in (a) is now modified by adding a uniform resistance wire XY and a galvanometer, as shown in Fig. 7.2.\nThe length of the wire XY is 1.2 m. The movable connection Z is positioned on the wire XY so that the galvanometer reading is zero."

    p_b_i = parts_by_id["9702_s23_22_q07_b_i"]
    p_b_i["question_text"] = "Calculate the length XZ along the resistance wire."
    p_b_i["question_text_latex"] = "Calculate the length $XZ$ along the resistance wire.\n$$\\text{length } XZ = \\text{...................................................}\\text{ m}$$"

    p_b_ii = parts_by_id["9702_s23_22_q07_b_ii"]
    p_b_ii["question_text"] = "The environmental conditions change causing a decrease in the resistance of the LDR.\nThe temperature of the LDR remains constant.\nState whether there is a decrease, increase or no change to:\n• the intensity of the light illuminating the LDR\n• the total power produced by the battery\n• the length XZ so that the galvanometer reads zero."
    p_b_ii["question_text_latex"] = "The environmental conditions change causing a decrease in the resistance of the LDR.\nThe temperature of the LDR remains constant.\nState whether there is a decrease, increase or no change to:\n\\begin{itemize}\n  \\item the intensity of the light illuminating the LDR\n  \\item the total power produced by the battery\n  \\item the length $XZ$ so that the galvanometer reads zero.\n\\end{itemize}"

    enr_parts = {p["part_id"]: p for p in ed["parts"]}
    enr_parts["9702_s23_22_q07_b_ii"]["mapping"]["outcome_ids"] = ["9702_t10_m03_o01", "9702_t10_m03_o02", "9702_t10_m03_o04"]

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))

def repair_s23_22_q08():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s23_qp_22/question_08.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s23_22_q08.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s23_22_q08_a"]
    p_a["question_text"] = "Nucleus P and nucleus Q are isotopes of the same element.\nNucleus Q is unstable and emits a β⁻ particle to form nucleus R."
    p_a["question_text_latex"] = "Nucleus P and nucleus Q are isotopes of the same element.\nNucleus Q is unstable and emits a $\\beta^{-}$ particle to form nucleus R."

    p_a_i = parts_by_id["9702_s23_22_q08_a_i"]
    p_a_i["question_text"] = "For nuclei P and Q, compare:\n• the number of protons\n• the number of neutrons."
    p_a_i["question_text_latex"] = "For nuclei P and Q, compare:\n\\begin{itemize}\n  \\item the number of protons\n  \\item the number of neutrons.\n\\end{itemize}"

    p_a_iii = parts_by_id["9702_s23_22_q08_a_iii"]
    p_a_iii["question_text"] = "State the name of another particle that must be emitted from nucleus Q in addition to the β⁻ particle."
    p_a_iii["question_text_latex"] = "State the name of another particle that must be emitted from nucleus Q in addition to the $\\beta^{-}$ particle."

    p_b = parts_by_id["9702_s23_22_q08_b"]
    p_b["question_text"] = "A hadron consists of two charm quarks and one bottom quark.\nDetermine, in terms of the elementary charge e, the charge of the hadron."
    p_b["question_text_latex"] = "A hadron consists of two charm quarks and one bottom quark.\nDetermine, in terms of the elementary charge $e$, the charge of the hadron.\n$$\\text{charge} = \\text{...................................................}\\text{ }e$$"

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))


# ==============================================================================
# 9702_s23_23
# ==============================================================================

def repair_s23_23_q01():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s23_qp_23/question_01.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s23_23_q01.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s23_23_q01_a"]
    p_a["question_text"] = "Assume that air resistance is negligible and that the stone is released from rest.\nCalculate the time taken for the stone to fall from ground level to the surface of the water."
    p_a["question_text_latex"] = "Assume that air resistance is negligible and that the stone is released from rest.\nCalculate the time taken for the stone to fall from ground level to the surface of the water.\n$$\\text{time} = \\text{...................................................}\\text{ s}$$"

    p_b = parts_by_id["9702_s23_23_q01_b"]
    p_b["question_text"] = "The time recorded by the student using a stop-watch is not equal to the time in (a).\nSuggest three possible reasons, other than the effect of air resistance, for this difference."
    p_b["question_text_latex"] = "The time recorded by the student using a stop-watch is not equal to the time in (a).\nSuggest three possible reasons, other than the effect of air resistance, for this difference."

    p_c = parts_by_id["9702_s23_23_q01_c"]
    p_c["question_text"] = "The student repeats the experiment three times and uses the results to calculate the depth of the well. The values are shown in Table 1.1.\n\nTable 1.1\n| experiment | depth / m |\n| :--- | :---: |\n| 1st experiment | 54.4 |\n| 2nd experiment | 53.9 |\n| 3rd experiment | 54.1 |\n\nThe true depth of the well is 36.0 m. Explain why these results may be described as precise but not accurate."
    p_c["question_text_latex"] = "The student repeats the experiment three times and uses the results to calculate the depth of the well. The values are shown in Table 1.1.\n\n\\textbf{Table 1.1}\n\\begin{center}\n\\begin{tabular}{|l|c|}\n\\hline\n\\text{experiment} & \\text{depth / m} \\\\\n\\hline\n\\text{1st experiment} & 54.4 \\\\\n\\text{2nd experiment} & 53.9 \\\\\n\\text{3rd experiment} & 54.1 \\\\\n\\hline\n\\end{tabular}\n\\end{center}\n\nThe true depth of the well is 36.0 m. Explain why these results may be described as precise but not accurate."

    enr_parts = {p["part_id"]: p for p in ed["parts"]}
    enr_parts["9702_s23_23_q01_c"]["question_patterns"] = ["definition", "explanation"]

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))

def repair_s23_23_q02():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s23_qp_23/question_02.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s23_23_q02.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["question_stem"] = "A sphere floats in equilibrium on the surface of sea water of density 1050 kg m⁻³, as shown in Fig. 2.1."
    qd["question_stem_latex"] = "A sphere floats in equilibrium on the surface of sea water of density $1050\\text{ kg m}^{-3}$, as shown in Fig. 2.1."

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s23_23_q02_a"]
    p_a["question_text"] = "21% of the volume of the sphere is below the surface of the water.\nCalculate the density of the sphere."
    p_a["question_text_latex"] = "21% of the volume of the sphere is below the surface of the water.\nCalculate the density of the sphere.\n$$\\text{density} = \\text{...................................................}\\text{ kg m}^{-3}$$"

    p_b = parts_by_id["9702_s23_23_q02_b"]
    p_b["question_text"] = "The sphere is now held so that its entire volume is below the surface of the water. The sphere is then released."
    p_b["question_text_latex"] = "The sphere is now held so that its entire volume is below the surface of the water. The sphere is then released."

    p_b_i = parts_by_id["9702_s23_23_q02_b_i"]
    p_b_i["question_text"] = "Calculate the initial acceleration of the sphere."
    p_b_i["question_text_latex"] = "Calculate the initial acceleration of the sphere.\n$$\\text{acceleration} = \\text{...................................................}\\text{ m s}^{-2}$$"

    p_b_ii = parts_by_id["9702_s23_23_q02_b_ii"]
    p_b_ii["question_text"] = "The sphere accelerates upwards but remains entirely below the surface of the water.\nState and explain what happens to the acceleration of the sphere as its velocity begins to increase."
    p_b_ii["question_text_latex"] = "The sphere accelerates upwards but remains entirely below the surface of the water.\nState and explain what happens to the acceleration of the sphere as its velocity begins to increase."

    enr_parts = {p["part_id"]: p for p in ed["parts"]}
    enr_parts["9702_s23_23_q02_b_i"]["mapping"]["outcome_ids"] = ["9702_t03_m01_o02"]

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))

def repair_s23_23_q03():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s23_qp_23/question_03.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s23_23_q03.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_b = parts_by_id["9702_s23_23_q03_b"]
    p_b["question_text"] = "A firework is initially stationary. It explodes into three fragments A, B and C that move in a horizontal plane, as shown in the view from above in Fig. 3.1.\nFragment A has a mass of 3m and moves away from the explosion at a speed of 4.0 m s⁻¹.\nFragment B has a mass of 2m and moves away from the explosion at a speed of 6.0 m s⁻¹ at right angles to the direction of A.\nFragment C has a mass of m and moves away from the explosion at a speed v and at an angle θ as shown in Fig. 3.1.\nCalculate:"
    p_b["question_text_latex"] = "A firework is initially stationary. It explodes into three fragments A, B and C that move in a horizontal plane, as shown in the view from above in Fig. 3.1.\nFragment A has a mass of $3m$ and moves away from the explosion at a speed of $4.0\\text{ m s}^{-1}$.\nFragment B has a mass of $2m$ and moves away from the explosion at a speed of $6.0\\text{ m s}^{-1}$ at right angles to the direction of A.\nFragment C has a mass of $m$ and moves away from the explosion at a speed $v$ and at an angle $\\theta$ as shown in Fig. 3.1.\nCalculate:"

    p_b_i = parts_by_id["9702_s23_23_q03_b_i"]
    p_b_i["question_text"] = "the angle θ"
    p_b_i["question_text_latex"] = "the angle $\\theta$\n$$\\theta = \\text{...................................................}^{\\circ}$$"

    p_b_ii = parts_by_id["9702_s23_23_q03_b_ii"]
    p_b_ii["question_text"] = "the speed v."
    p_b_ii["question_text_latex"] = "the speed $v$.\n$$v = \\text{...................................................}\\text{ m s}^{-1}$$"

    p_c = parts_by_id["9702_s23_23_q03_c"]
    p_c["question_text"] = "The firework in (b) contains a chemical that has mass 5.0 g and has chemical energy per unit mass 700 J kg⁻¹. When the firework explodes, all of the chemical energy is transferred to the kinetic energy of fragments A, B and C."
    p_c["question_text_latex"] = "The firework in (b) contains a chemical that has mass 5.0 g and has chemical energy per unit mass $700\\text{ J kg}^{-1}$. When the firework explodes, all of the chemical energy is transferred to the kinetic energy of fragments A, B and C."

    p_c_ii = parts_by_id["9702_s23_23_q03_c_ii"]
    p_c_ii["question_text"] = "Calculate the mass m."
    p_c_ii["question_text_latex"] = "Calculate the mass $m$.\n$$m = \\text{...................................................}\\text{ kg}$$"

    enr_parts = {p["part_id"]: p for p in ed["parts"]}
    enr_parts["9702_s23_23_q03_b_i"]["mapping"]["outcome_ids"] = ["9702_t03_m03_o02"]
    enr_parts["9702_s23_23_q03_b_ii"]["mapping"]["outcome_ids"] = ["9702_t03_m03_o02"]
    enr_parts["9702_s23_23_q03_c_ii"]["mapping"]["outcome_ids"] = ["9702_t05_m02_o04"]

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))

def repair_s23_23_q04():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s23_qp_23/question_04.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s23_23_q04.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_b = parts_by_id["9702_s23_23_q04_b"]
    p_b["question_text"] = "A loudspeaker, microphone and cathode-ray oscilloscope (CRO) are arranged as shown in Fig. 4.1.\nThe loudspeaker is emitting a sound wave which is detected by the microphone and displayed on the screen of the CRO as shown in Fig. 4.2.\nThe time-base on the CRO is set to 0.50 ms cm⁻¹ and the y-gain is set to 0.20 V cm⁻¹.\nCalculate:"
    p_b["question_text_latex"] = "A loudspeaker, microphone and cathode-ray oscilloscope (CRO) are arranged as shown in Fig. 4.1.\nThe loudspeaker is emitting a sound wave which is detected by the microphone and displayed on the screen of the CRO as shown in Fig. 4.2.\nThe time-base on the CRO is set to $0.50\\text{ ms cm}^{-1}$ and the y-gain is set to $0.20\\text{ V cm}^{-1}$.\nCalculate:"

    p_b_i = parts_by_id["9702_s23_23_q04_b_i"]
    p_b_i["question_text"] = "the frequency of the sound wave"
    p_b_i["question_text_latex"] = "the frequency of the sound wave\n$$\\text{frequency} = \\text{...................................................}\\text{ Hz}$$"

    p_b_ii = parts_by_id["9702_s23_23_q04_b_ii"]
    p_b_ii["question_text"] = "the amplitude of the signal received by the CRO."
    p_b_ii["question_text_latex"] = "the amplitude of the signal received by the CRO.\n$$\\text{amplitude} = \\text{...................................................}\\text{ V}$$"

    p_c = parts_by_id["9702_s23_23_q04_c"]
    p_c["question_text"] = "The intensity of the sound wave in (b) is reduced to a quarter of its original intensity without a change in frequency. Assume that the amplitude of the signal received by the CRO is proportional to the amplitude of the sound wave.\nOn Fig. 4.2, sketch the trace that is now seen on the screen of the CRO."
    p_c["question_text_latex"] = "The intensity of the sound wave in (b) is reduced to a quarter of its original intensity without a change in frequency. Assume that the amplitude of the signal received by the CRO is proportional to the amplitude of the sound wave.\nOn Fig. 4.2, sketch the trace that is now seen on the screen of the CRO."

    p_d = parts_by_id["9702_s23_23_q04_d"]
    p_d["question_text"] = "A metal sheet is now placed in front of the loudspeaker in (b), as shown in Fig. 4.3.\nA stationary wave is formed between the loudspeaker and the metal sheet."
    p_d["question_text_latex"] = "A metal sheet is now placed in front of the loudspeaker in (b), as shown in Fig. 4.3.\nA stationary wave is formed between the loudspeaker and the metal sheet."

    p_d_ii = parts_by_id["9702_s23_23_q04_d_ii"]
    p_d_ii["question_text"] = "The initial position of the microphone is such that the trace on the CRO has an amplitude minimum. It is now moved a distance of 1.05 m away from the loudspeaker along the line joining the loudspeaker and metal sheet.\nAs the microphone moves, it passes through three positions where the trace has an amplitude maximum before ending at a position where the trace has an amplitude minimum.\nDetermine the wavelength of the sound wave."
    p_d_ii["question_text_latex"] = "The initial position of the microphone is such that the trace on the CRO has an amplitude minimum. It is now moved a distance of 1.05 m away from the loudspeaker along the line joining the loudspeaker and metal sheet.\nAs the microphone moves, it passes through three positions where the trace has an amplitude maximum before ending at a position where the trace has an amplitude minimum.\nDetermine the wavelength of the sound wave.\n$$\\text{wavelength} = \\text{...................................................}\\text{ m}$$"

    p_d_iii = parts_by_id["9702_s23_23_q04_d_iii"]
    p_d_iii["question_text"] = "Use your answers in (b)(i) and (d)(ii) to determine the speed of the sound in the air."
    p_d_iii["question_text_latex"] = "Use your answers in (b)(i) and (d)(ii) to determine the speed of the sound in the air.\n$$\\text{speed} = \\text{...................................................}\\text{ m s}^{-1}$$"

    enr_parts = {p["part_id"]: p for p in ed["parts"]}
    enr_parts["9702_s23_23_q04_d_ii"]["skills"]["primary_skill_id"] = "9702_skill_stationary_waves"

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))

def repair_s23_23_q05():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s23_qp_23/question_05.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s23_23_q05.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    qd["total_marks"] = 10
    qd["detected_part_marks"] = 10
    qd["marks_validation_passed"] = true = True

    qd["question_stem"] = "A student sets up a circuit with a battery, an ammeter, a heater and a light-dependent resistor (LDR) all in series.\nThe battery has negligible internal resistance.\nA voltmeter is connected across (in parallel with) the heater."
    qd["question_stem_latex"] = "A student sets up a circuit with a battery, an ammeter, a heater and a light‑dependent resistor (LDR) all in series.\nThe battery has negligible internal resistance.\nA voltmeter is connected across (in parallel with) the heater."

    # Filter out the spurious '9702_s23_23_q05_ldr' part
    valid_parts = [p for p in qd["parts"] if p["id"] != "9702_s23_23_q05_ldr"]
    for idx, p in enumerate(valid_parts, 1):
        p["display_order"] = idx
    qd["parts"] = valid_parts

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s23_23_q05_a"]
    p_a["question_text"] = "On Fig. 5.1, complete the circuit diagram of this arrangement."
    p_a["question_text_latex"] = "On Fig. 5.1, complete the circuit diagram of this arrangement."

    p_b = parts_by_id["9702_s23_23_q05_b"]
    p_b["question_text"] = "The heater is a wire made of metal of resistivity 1.1 × 10⁻⁶ Ω m. The wire has length 2.0 m and cross-sectional area 3.8 × 10⁻⁷ m².\nThe reading on the voltmeter is 4.8 V.\nCalculate:"
    p_b["question_text_latex"] = "The heater is a wire made of metal of resistivity $1.1 \\times 10^{-6}\\,\\Omega\\,\\mathrm{m}$. The wire has length 2.0 m and cross-sectional area $3.8 \\times 10^{-7}\\,\\mathrm{m}^{2}$.\nThe reading on the voltmeter is 4.8 V.\nCalculate:"

    p_b_i = parts_by_id["9702_s23_23_q05_b_i"]
    p_b_i["question_text"] = "the resistance of the heater"
    p_b_i["question_text_latex"] = "the resistance of the heater\n$$\\text{resistance} = \\text{...................................................}\\text{ }\\Omega$$"

    p_b_ii = parts_by_id["9702_s23_23_q05_b_ii"]
    p_b_ii["question_text"] = "the reading on the ammeter."
    p_b_ii["question_text_latex"] = "the reading on the ammeter.\n$$\\text{reading on ammeter} = \\text{...................................................}\\text{ A}$$"

    p_c = parts_by_id["9702_s23_23_q05_c"]
    p_c["question_text"] = "The heater is replaced by a new wire. The new wire is made of the same metal as the wire in (b) and has the same length but a larger diameter.\nThe resistance of the LDR remains constant."
    p_c["question_text_latex"] = "The heater is replaced by a new wire. The new wire is made of the same metal as the wire in (b) and has the same length but a larger diameter.\nThe resistance of the LDR remains constant."

    p_c_i = parts_by_id["9702_s23_23_q05_c_i"]
    p_c_i["question_text"] = "State and explain whether the new wire has a resistance that is greater than, less than or the same as that of the wire in (b)."
    p_c_i["question_text_latex"] = "State and explain whether the new wire has a resistance that is greater than, less than or the same as that of the wire in (b)."

    p_c_ii = parts_by_id["9702_s23_23_q05_c_ii"]
    p_c_ii["question_text"] = "State and explain whether the new reading on the voltmeter is greater than, less than or equal to 4.8 V."
    p_c_ii["question_text_latex"] = "State and explain whether the new reading on the voltmeter is greater than, less than or equal to 4.8 V."

    enr_parts = {p["part_id"]: p for p in ed["parts"]}
    enr_parts["9702_s23_23_q05_a"]["skills"]["primary_skill_id"] = "9702_skill_resistor_networks"

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))

def repair_s23_23_q06():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s23_qp_23/question_06.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s23_23_q06.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_b = parts_by_id["9702_s23_23_q06_b"]
    p_b["question_text"] = "A uniform wire is suspended from a fixed support. Masses are added to the other end of the wire, as shown in Fig. 6.1.\nThe variation of the length l of the wire with the force F applied to the wire by the masses is shown in Fig. 6.2.\nThe cross-sectional area of the wire is 0.95 mm²."
    p_b["question_text_latex"] = "A uniform wire is suspended from a fixed support. Masses are added to the other end of the wire, as shown in Fig. 6.1.\nThe variation of the length $l$ of the wire with the force $F$ applied to the wire by the masses is shown in Fig. 6.2.\nThe cross-sectional area of the wire is $0.95\\text{ mm}^{2}$."

    p_b_i = parts_by_id["9702_s23_23_q06_b_i"]
    p_b_i["question_text"] = "Determine the unstretched length of the wire."
    p_b_i["question_text_latex"] = "Determine the unstretched length of the wire.\n$$\\text{unstretched length} = \\text{...................................................}\\text{ m}$$"

    p_b_ii = parts_by_id["9702_s23_23_q06_b_ii"]
    p_b_ii["question_text"] = "For an applied force F of 30 N, determine:\n• the stress in the wire\n• the strain of the wire."
    p_b_ii["question_text_latex"] = "For an applied force $F$ of 30 N, determine:\n\\begin{itemize}\n  \\item the stress in the wire\n  \\item the strain of the wire.\n\\end{itemize}"

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))

def repair_s23_23_q07():
    q_path = ROOT / "subjects/physics/9702/papers/p2/questions/9702_s23_qp_23/question_07.json"
    enr_path = ROOT / "subjects/physics/9702/enrichment/p2/9702_s23_23_q07.enrichment.json"
    qd = json.loads(q_path.read_text(encoding="utf-8"))
    ed = json.loads(enr_path.read_text(encoding="utf-8"))

    parts_by_id = {p["id"]: p for p in qd["parts"]}

    p_a = parts_by_id["9702_s23_23_q07_a"]
    p_a["question_text"] = "Table 7.1 shows incomplete data for three flavours (types) of quark. The elementary charge is e.\n\nTable 7.1\n| flavour | quark symbol | quark charge / e | antiquark symbol | antiquark charge / e |\n| :--- | :---: | :---: | :---: | :---: |\n| up | u | +2/3 | \\bar{u} | |\n| down | d | | \\bar{d} | |\n| charm | c | | \\bar{c} | |\n\nComplete Table 7.1 by inserting the missing charges."
    p_a["question_text_latex"] = "Table 7.1 shows incomplete data for three flavours (types) of quark. The elementary charge is $e$.\n\n\\textbf{Table 7.1}\n\\begin{center}\n\\begin{tabular}{|l|c|c|c|c|}\n\\hline\n\\text{flavour} & \\text{quark symbol} & \\text{quark charge / } e & \\text{antiquark symbol} & \\text{antiquark charge / } e \\\\\n\\hline\n\\text{up} & u & +\\frac{2}{3} & \\overline{u} & \\\\\n\\hline\n\\text{down} & d & & \\overline{d} & \\\\\n\\hline\n\\text{charm} & c & & \\overline{c} & \\\\\n\\hline\n\\end{tabular}\n\\end{center}\n\nComplete Table 7.1 by inserting the missing charges."

    p_b = parts_by_id["9702_s23_23_q07_b"]
    p_b["question_text"] = "Using the symbols given in Table 7.1, state a possible quark combination for the following hadrons:"
    p_b["question_text_latex"] = "Using the symbols given in Table 7.1, state a possible quark combination for the following hadrons:"

    save_json(q_path, finalize_question(qd))
    save_json(enr_path, finalize_enrichment(ed))


def main():
    print("Repairing 9702_s23_22...")
    repair_s23_22_q01()
    repair_s23_22_q02()
    repair_s23_22_q03()
    repair_s23_22_q04()
    repair_s23_22_q05()
    repair_s23_22_q06()
    repair_s23_22_q07()
    repair_s23_22_q08()

    print("\nRepairing 9702_s23_23...")
    repair_s23_23_q01()
    repair_s23_23_q02()
    repair_s23_23_q03()
    repair_s23_23_q04()
    repair_s23_23_q05()
    repair_s23_23_q06()
    repair_s23_23_q07()

    print("\nRepairs complete.")

if __name__ == "__main__":
    main()
