#!/usr/bin/env python3
"""Repair script for Physics 9702 papers 9702_s25_24 and 9702_w25_21."""

import json
from pathlib import Path

repo = Path(__file__).resolve().parent.parent

def ordered_unique(values: list) -> list:
    seen = set()
    result = []
    for v in values:
        if v not in seen and v is not None:
            seen.add(v)
            result.append(v)
    return result

def repair_s25_24():
    paper = "9702_s25_24"
    stem = "9702_s25"
    var = "24"

    # --- Q01 ---
    q1_path = repo / f"subjects/physics/9702/papers/p2/questions/{stem}_qp_{var}/question_01.json"
    q1 = json.loads(q1_path.read_text())
    for p in q1["parts"]:
        if p["id"] == "9702_s25_24_q01_b":
            p["response_schema"] = None
            p["question_text"] = (
                "A trapdoor has a hinge at end A, as shown in Fig. 1.1.\n"
                "The trapdoor has length 80 cm and weight 75 N. The mass of the trapdoor is uniformly distributed along its length.\n"
                "A force F acts at right angles to the trapdoor at end B so that the trapdoor is held in equilibrium at an angle of 42° to the horizontal."
            )
            p["question_text_latex"] = (
                "A trapdoor has a hinge at end A, as shown in Fig. 1.1.\n"
                "The trapdoor has length 80 cm and weight 75 N. The mass of the trapdoor is uniformly distributed along its length.\n"
                "A force F acts at right angles to the trapdoor at end B so that the trapdoor is held in equilibrium at an angle of 42° to the horizontal."
            )
        elif p["id"] == "9702_s25_24_q01_b_ii":
            p["question_text_latex"] = (
                "Calculate the component of the weight that is perpendicular to the trapdoor.\n"
                "$\\text{component of weight} = \\text{N}$"
            )
        elif p["id"] == "9702_s25_24_q01_b_iii":
            p["question_text"] = "Calculate the magnitude of the force F.\nF = N"
            p["question_text_latex"] = "Calculate the magnitude of the force F.\n$F = \\text{N}$"
    q1_path.write_text(json.dumps(q1, indent=2) + "\n")

    e1_path = repo / f"subjects/physics/9702/enrichment/p2/{paper}_q01.enrichment.json"
    e1 = json.loads(e1_path.read_text())
    e1["numerical_values_checked"] = False
    e1["question_patterns"] = ordered_unique([p for part in e1["parts"] for p in part.get("question_patterns", [])])
    e1["mapping"]["topic_ids"] = ordered_unique([part["mapping"]["primary_topic_id"] for part in e1["parts"]])
    e1["mapping"]["module_ids"] = ordered_unique([part["mapping"]["primary_module_id"] for part in e1["parts"]])
    e1["mapping"]["outcome_ids"] = ordered_unique([o for part in e1["parts"] for o in part["mapping"].get("outcome_ids", [])])
    e1_path.write_text(json.dumps(e1, indent=2) + "\n")

    # --- Q02 ---
    q2_path = repo / f"subjects/physics/9702/papers/p2/questions/{stem}_qp_{var}/question_02.json"
    q2 = json.loads(q2_path.read_text())
    for p in q2["parts"]:
        if p["id"] == "9702_s25_24_q02_b":
            p["question_text_latex"] = (
                "Calculate the change in momentum of the object from time t = 0 to t = 12 s.\n"
                "$\\text{change in momentum} = \\text{kg}\\ \\text{m}\\ \\text{s}^{-1}$"
            )
        elif p["id"] == "9702_s25_24_q02_c":
            p["question_text_latex"] = (
                "Calculate the magnitude of the resultant force acting on the object.\n"
                "$\\text{force} = \\text{N}$"
            )
        elif p["id"] == "9702_s25_24_q02_e":
            p["question_text"] = (
                "By reference to Fig. 2.1, explain why the resultant force acting on the object during the first 8.0 s of its motion cannot be due to air resistance."
            )
            p["question_text_latex"] = (
                "By reference to Fig. 2.1, explain why the resultant force acting on the object during the first 8.0 s of its motion cannot be due to air resistance."
            )
    q2_path.write_text(json.dumps(q2, indent=2) + "\n")

    e2_path = repo / f"subjects/physics/9702/enrichment/p2/{paper}_q02.enrichment.json"
    e2 = json.loads(e2_path.read_text())
    e2["numerical_values_checked"] = False
    for ep in e2["parts"]:
        if ep["part_id"] == "9702_s25_24_q02_f":
            ep["mapping"]["primary_topic_id"] = "9702_t02"
            ep["mapping"]["primary_module_id"] = "9702_t02_m01"
            ep["mapping"]["outcome_ids"] = ["9702_t02_m01_o02"]
            ep["skills"]["primary_skill_id"] = "9702_skill_motion_graphs"
            ep["knowledge_refs"]["formula_ids"] = []
            ep["knowledge_refs"]["formula_empty_justification"] = "This graphical sketching task determines displacement from the area under a velocity-time graph without requiring a separate algebraic formula."
    e2["question_patterns"] = ordered_unique([p for part in e2["parts"] for p in part.get("question_patterns", [])])
    e2["mapping"]["topic_ids"] = ordered_unique([part["mapping"]["primary_topic_id"] for part in e2["parts"]])
    e2["mapping"]["module_ids"] = ordered_unique([part["mapping"]["primary_module_id"] for part in e2["parts"]])
    e2["mapping"]["outcome_ids"] = ordered_unique([o for part in e2["parts"] for o in part["mapping"].get("outcome_ids", [])])
    e2_path.write_text(json.dumps(e2, indent=2) + "\n")

    # --- Q03 ---
    q3_path = repo / f"subjects/physics/9702/papers/p2/questions/{stem}_qp_{var}/question_03.json"
    q3 = json.loads(q3_path.read_text())
    for p in q3["parts"]:
        if p["id"] == "9702_s25_24_q03_a":
            p["question_text_latex"] = (
                "The block has kinetic energy 110 J as it makes contact with the spring.\n"
                "Calculate the speed of the block as it makes contact with the spring.\n"
                "$\\text{speed} = \\text{m}\\ \\text{s}^{-1}$"
            )
        elif p["id"] == "9702_s25_24_q03_b":
            p["question_text"] = (
                "The gravitational potential energy of the block decreases by 20 J as the spring is compressed to its maximum compression x₀.\n"
                "Show that x₀ is 0.37 m."
            )
            p["question_text_latex"] = (
                "The gravitational potential energy of the block decreases by 20 J as the spring is compressed to its maximum compression $x_{0}$.\n"
                "Show that $x_{0}$ is 0.37 m."
            )
        elif p["id"] == "9702_s25_24_q03_c":
            p["question_text"] = (
                "Assume that, as the spring compresses, all of the energy lost by the block is converted into the elastic potential energy of the spring.\n"
                "Use the data from (a) and (b) to determine the maximum elastic potential energy of the spring.\n"
                "Show your working."
            )
            p["question_text_latex"] = (
                "Assume that, as the spring compresses, all of the energy lost by the block is converted into the elastic potential energy of the spring.\n"
                "Use the data from (a) and (b) to determine the maximum elastic potential energy of the spring.\n"
                "Show your working."
            )
        elif p["id"] == "9702_s25_24_q03_d":
            p["question_text"] = (
                "The variation of the force F acting on the spring with the compression x of the spring is shown in Fig. 3.2.\n"
                "Use the information in (b) and your answer in (c) to show that the maximum force F₀ exerted on the spring by the block is 700 N."
            )
            p["question_text_latex"] = (
                "The variation of the force F acting on the spring with the compression x of the spring is shown in Fig. 3.2.\n"
                "Use the information in (b) and your answer in (c) to show that the maximum force $F_{0}$ exerted on the spring by the block is 700 N."
            )
        elif p["id"] == "9702_s25_24_q03_e":
            p["response_schema"] = None
            p["question_text"] = (
                "Use the information in (d) to determine, for the instant that the block is first brought to rest by the spring, the magnitude of:"
            )
            p["question_text_latex"] = (
                "Use the information in (d) to determine, for the instant that the block is first brought to rest by the spring, the magnitude of:"
            )
        elif p["id"] == "9702_s25_24_q03_e_i":
            p["question_text_latex"] = (
                "the resultant force acting on the block\n"
                "$\\text{resultant force} = \\text{N}$"
            )
        elif p["id"] == "9702_s25_24_q03_e_ii":
            p["question_text_latex"] = (
                "the acceleration of the block.\n"
                "$\\text{acceleration} = \\text{m}\\ \\text{s}^{-2}$"
            )
    q3_path.write_text(json.dumps(q3, indent=2) + "\n")

    e3_path = repo / f"subjects/physics/9702/enrichment/p2/{paper}_q03.enrichment.json"
    e3 = json.loads(e3_path.read_text())
    e3["numerical_values_checked"] = False
    e3["question_patterns"] = ordered_unique([p for part in e3["parts"] for p in part.get("question_patterns", [])])
    e3["mapping"]["topic_ids"] = ordered_unique([part["mapping"]["primary_topic_id"] for part in e3["parts"]])
    e3["mapping"]["module_ids"] = ordered_unique([part["mapping"]["primary_module_id"] for part in e3["parts"]])
    e3["mapping"]["outcome_ids"] = ordered_unique([o for part in e3["parts"] for o in part["mapping"].get("outcome_ids", [])])
    e3_path.write_text(json.dumps(e3, indent=2) + "\n")

    # --- Q04 ---
    q4_path = repo / f"subjects/physics/9702/papers/p2/questions/{stem}_qp_{var}/question_04.json"
    q4 = json.loads(q4_path.read_text())
    for p in q4["parts"]:
        if p["id"] == "9702_s25_24_q04_a":
            p["response_schema"] = None
            p["question_text"] = (
                "A source oscillates with frequency f to produce a progressive wave of wavelength λ. The source takes time t to produce n complete oscillations."
            )
            p["question_text_latex"] = (
                "A source oscillates with frequency f to produce a progressive wave of wavelength $\\lambda$. The source takes time t to produce n complete oscillations."
            )
        elif p["id"] == "9702_s25_24_q04_a_ii":
            p["question_text"] = (
                "State expressions, in terms of some or all of f, λ and n, for:\n"
                "● the distance moved by a wavefront in time t\n"
                "distance =\n"
                "● time t.\n"
                "time t ="
            )
            p["question_text_latex"] = (
                "State expressions, in terms of some or all of f, $\\lambda$ and n, for:\n"
                "● the distance moved by a wavefront in time t\n"
                "$\\text{distance} =$\n"
                "● time t.\n"
                "$\\text{time } t =$"
            )
        elif p["id"] == "9702_s25_24_q04_a_iii":
            p["question_text"] = (
                "Use your answers in (ii) to determine an expression for the speed v of the wave in terms of f and λ."
            )
            p["question_text_latex"] = (
                "Use your answers in (ii) to determine an expression for the speed v of the wave in terms of f and $\\lambda$."
            )
        elif p["id"] == "9702_s25_24_q04_b":
            p["response_schema"] = None
            p["question_text"] = (
                "Two identical microwave sources X and Y emit waves in phase. The sources are separated by a distance of 30 cm, as shown in Fig. 4.1.\n"
                "The intensity of the microwaves is to be investigated at points P and Q.\n"
                "Line PQ is parallel to line XY. Distance XP is equal to distance YP. Distance YQ is 72 cm and angle XYQ is 90°.\n"
                "The wavelength of the microwaves is 4.0 cm."
            )
            p["question_text_latex"] = (
                "Two identical microwave sources X and Y emit waves in phase. The sources are separated by a distance of 30 cm, as shown in Fig. 4.1.\n"
                "The intensity of the microwaves is to be investigated at points P and Q.\n"
                "Line PQ is parallel to line XY. Distance XP is equal to distance YP. Distance YQ is 72 cm and angle XYQ is 90°.\n"
                "The wavelength of the microwaves is 4.0 cm."
            )
        elif p["id"] == "9702_s25_24_q04_b_i":
            p["question_text_latex"] = (
                "Calculate the frequency, in GHz, of the microwaves.\n"
                "$\\text{frequency} = \\text{GHz}$"
            )
        elif p["id"] == "9702_s25_24_q04_b_iv":
            p["response_schema"] = None
            p["question_text"] = "A microwave detector is positioned at P and connected to a cathode-ray oscilloscope (CRO)."
            p["question_text_latex"] = "A microwave detector is positioned at P and connected to a cathode-ray oscilloscope (CRO)."
        elif p["id"] == "9702_s25_24_q04_cro":
            p["question_text"] = (
                "The controls of the CRO are adjusted so that a waveform is shown on the screen.\n"
                "Describe the changes to the amplitude of the waveform as the detector is moved from P to Q."
            )
            p["question_text_latex"] = (
                "The controls of the CRO are adjusted so that a waveform is shown on the screen.\n"
                "Describe the changes to the amplitude of the waveform as the detector is moved from P to Q."
            )
    q4_path.write_text(json.dumps(q4, indent=2) + "\n")

    e4_path = repo / f"subjects/physics/9702/enrichment/p2/{paper}_q04.enrichment.json"
    e4 = json.loads(e4_path.read_text())
    e4["numerical_values_checked"] = False
    for ep in e4["parts"]:
        if ep["part_id"] == "9702_s25_24_q04_b_i":
            ep["skills"]["primary_skill_id"] = "9702_skill_electromagnetic_spectrum"
    e4["question_patterns"] = ordered_unique([p for part in e4["parts"] for p in part.get("question_patterns", [])])
    e4["mapping"]["topic_ids"] = ordered_unique([part["mapping"]["primary_topic_id"] for part in e4["parts"]])
    e4["mapping"]["module_ids"] = ordered_unique([part["mapping"]["primary_module_id"] for part in e4["parts"]])
    e4["mapping"]["outcome_ids"] = ordered_unique([o for part in e4["parts"] for o in part["mapping"].get("outcome_ids", [])])
    e4_path.write_text(json.dumps(e4, indent=2) + "\n")

    # --- Q05 ---
    q5_path = repo / f"subjects/physics/9702/papers/p2/questions/{stem}_qp_{var}/question_05.json"
    q5 = json.loads(q5_path.read_text())
    for p in q5["parts"]:
        if p["id"] == "9702_s25_24_q05_a":
            p["response_schema"] = None
        elif p["id"] == "9702_s25_24_q05_a_i":
            p["question_text"] = (
                "State and explain the effect, if any, on the resistance of a filament wire in a lamp as the current in the wire decreases."
            )
            p["question_text_latex"] = (
                "State and explain the effect, if any, on the resistance of a filament wire in a lamp as the current in the wire decreases."
            )
        elif p["id"] == "9702_s25_24_q05_b":
            p["response_schema"] = None
            p["question_text"] = (
                "A battery of electromotive force (e.m.f.) E and negligible internal resistance is connected in parallel with two filament lamps A and B, as shown in Fig. 5.2.\n"
                "The current in the battery is 3.3 A and the current in lamp A is 1.5 A. The power dissipated in lamp A is 18 W."
            )
            p["question_text_latex"] = (
                "A battery of electromotive force (e.m.f.) E and negligible internal resistance is connected in parallel with two filament lamps A and B, as shown in Fig. 5.2.\n"
                "The current in the battery is 3.3 A and the current in lamp A is 1.5 A. The power dissipated in lamp A is 18 W."
            )
        elif p["id"] == "9702_s25_24_q05_b_i":
            p["question_text_latex"] = (
                "Calculate the e.m.f. E of the battery.\n"
                "$E = \\text{V}$"
            )
        elif p["id"] == "9702_s25_24_q05_b_ii":
            p["question_text"] = (
                "The filament wire of lamp B has a cross-sectional area of 1.4 × 10⁻⁹ m². The number of free (conduction) electrons per unit volume in the metal of the filament wire is 3.4 × 10²⁸ m⁻³.\n"
                "Calculate the average drift speed of the free electrons in the filament wire of lamp B.\n"
                "average drift speed = m s⁻¹"
            )
            p["question_text_latex"] = (
                "The filament wire of lamp B has a cross-sectional area of $1.4 \\times 10^{-9}\\,\\text{m}^{2}$. The number of free (conduction) electrons per unit volume in the metal of the filament wire is $3.4 \\times 10^{28}\\,\\mathrm{m}^{-3}$.\n"
                "Calculate the average drift speed of the free electrons in the filament wire of lamp B.\n"
                "$\\text{average drift speed} = \\text{m}\\ \\text{s}^{-1}$"
            )
    q5_path.write_text(json.dumps(q5, indent=2) + "\n")

    e5_path = repo / f"subjects/physics/9702/enrichment/p2/{paper}_q05.enrichment.json"
    e5 = json.loads(e5_path.read_text())
    e5["numerical_values_checked"] = False
    for ep in e5["parts"]:
        if ep["part_id"] == "9702_s25_24_q05_b_i":
            ep["skills"]["primary_skill_id"] = "9702_skill_potential_difference_power"
        elif ep["part_id"] == "9702_s25_24_q05_b_ii":
            ep["mapping"]["outcome_ids"] = ["9702_t09_m01_o04"]
    e5["question_patterns"] = ordered_unique([p for part in e5["parts"] for p in part.get("question_patterns", [])])
    e5["mapping"]["topic_ids"] = ordered_unique([part["mapping"]["primary_topic_id"] for part in e5["parts"]])
    e5["mapping"]["module_ids"] = ordered_unique([part["mapping"]["primary_module_id"] for part in e5["parts"]])
    e5["mapping"]["outcome_ids"] = ordered_unique([o for part in e5["parts"] for o in part["mapping"].get("outcome_ids", [])])
    e5_path.write_text(json.dumps(e5, indent=2) + "\n")

    # --- Q06 ---
    q6_path = repo / f"subjects/physics/9702/papers/p2/questions/{stem}_qp_{var}/question_06.json"
    q6 = json.loads(q6_path.read_text())
    for p in q6["parts"]:
        if p["id"] == "9702_s25_24_q06_a":
            p["question_text_latex"] = "Determine R.\n$R = \\Omega$"
        elif p["id"] == "9702_s25_24_q06_b":
            p["question_text"] = (
                "Explain why the potential difference V between any two points on wire XY is proportional to the distance L between those points."
            )
            p["question_text_latex"] = (
                "Explain why the potential difference V between any two points on wire XY is proportional to the distance L between those points."
            )
        elif p["id"] == "9702_s25_24_q06_c":
            p["response_schema"] = None
        elif p["id"] == "9702_s25_24_q06_c_i":
            p["question_text_latex"] = "Calculate E.\n$E = \\text{V}$"
        elif p["id"] == "9702_s25_24_q06_c_ii":
            p["question_text"] = (
                "The value of R is now decreased.\n"
                "State and explain the change that must be made to the position of P on wire XY so that the galvanometer reads zero again."
            )
            p["question_text_latex"] = (
                "The value of R is now decreased.\n"
                "State and explain the change that must be made to the position of P on wire XY so that the galvanometer reads zero again."
            )
    q6_path.write_text(json.dumps(q6, indent=2) + "\n")

    e6_path = repo / f"subjects/physics/9702/enrichment/p2/{paper}_q06.enrichment.json"
    e6 = json.loads(e6_path.read_text())
    e6["numerical_values_checked"] = False
    for ep in e6["parts"]:
        if ep["part_id"] == "9702_s25_24_q06_c_ii":
            ep["mapping"]["outcome_ids"] = ["9702_t10_m03_o02"]
    e6["question_patterns"] = ordered_unique([p for part in e6["parts"] for p in part.get("question_patterns", [])])
    e6["mapping"]["topic_ids"] = ordered_unique([part["mapping"]["primary_topic_id"] for part in e6["parts"]])
    e6["mapping"]["module_ids"] = ordered_unique([part["mapping"]["primary_module_id"] for part in e6["parts"]])
    e6["mapping"]["outcome_ids"] = ordered_unique([o for part in e6["parts"] for o in part["mapping"].get("outcome_ids", [])])
    e6_path.write_text(json.dumps(e6, indent=2) + "\n")

    # --- Q07 ---
    q7_path = repo / f"subjects/physics/9702/papers/p2/questions/{stem}_qp_{var}/question_07.json"
    q7 = json.loads(q7_path.read_text())
    for p in q7["parts"]:
        if p["id"] == "9702_s25_24_q07_a":
            p["question_text"] = "State the names of two different leptons."
            p["question_text_latex"] = "State the names of two different leptons."
    q7_path.write_text(json.dumps(q7, indent=2) + "\n")

    e7_path = repo / f"subjects/physics/9702/enrichment/p2/{paper}_q07.enrichment.json"
    e7 = json.loads(e7_path.read_text())
    e7["numerical_values_checked"] = False
    e7["question_patterns"] = ordered_unique([p for part in e7["parts"] for p in part.get("question_patterns", [])])
    e7["mapping"]["topic_ids"] = ordered_unique([part["mapping"]["primary_topic_id"] for part in e7["parts"]])
    e7["mapping"]["module_ids"] = ordered_unique([part["mapping"]["primary_module_id"] for part in e7["parts"]])
    e7["mapping"]["outcome_ids"] = ordered_unique([o for part in e7["parts"] for o in part["mapping"].get("outcome_ids", [])])
    e7_path.write_text(json.dumps(e7, indent=2) + "\n")

def repair_w25_21():
    paper = "9702_w25_21"
    stem = "9702_w25"
    var = "21"

    # --- Q01 ---
    q1_path = repo / f"subjects/physics/9702/papers/p2/questions/{stem}_qp_{var}/question_01.json"
    q1 = json.loads(q1_path.read_text())
    for p in q1["parts"]:
        if p["id"] == "9702_w25_21_q01_b":
            p["response_schema"] = None
            p["question_text"] = "Fig. 1.1 shows the variation of the velocity of the rocket with time for the first 20 s after its launch."
            p["question_text_latex"] = "Fig. 1.1 shows the variation of the velocity of the rocket with time for the first 20 s after its launch."
        elif p["id"] == "9702_w25_21_q01_b_i":
            p["question_text_latex"] = (
                "Calculate the acceleration of the rocket at a time of 10 s after launch.\n"
                "$\\text{acceleration} = \\text{m}\\ \\text{s}^{-2}$"
            )
        elif p["id"] == "9702_w25_21_q01_b_ii":
            p["question_text"] = "Show that the height of the rocket above the surface of the Earth at a time of 20 s after launch is 3.2 km."
            p["question_text_latex"] = "Show that the height of the rocket above the surface of the Earth at a time of 20 s after launch is 3.2 km."
        elif p["id"] == "9702_w25_21_q01_c":
            p["response_schema"] = None
        elif p["id"] == "9702_w25_21_q01_c_i":
            p["question_text_latex"] = "the kinetic energy of the rocket\n$\\text{kinetic energy} = \\text{J}$"
        elif p["id"] == "9702_w25_21_q01_c_ii":
            p["question_text_latex"] = "the increase in the gravitational potential energy of the rocket.\n$\\text{increase in gravitational potential energy} = \\text{J}$"
        elif p["id"] == "9702_w25_21_q01_c_iii":
            p["question_text"] = (
                "Use your answers in (c)(i) and (c)(ii) to determine the average power output of the rocket engines. Assume that resistive forces are negligible.\n"
                "power = W"
            )
            p["question_text_latex"] = (
                "Use your answers in (c)(i) and (c)(ii) to determine the average power output of the rocket engines. Assume that resistive forces are negligible.\n"
                "$\\text{power} = \\text{W}$"
            )
    q1_path.write_text(json.dumps(q1, indent=2) + "\n")

    e1_path = repo / f"subjects/physics/9702/enrichment/p2/{paper}_q01.enrichment.json"
    e1 = json.loads(e1_path.read_text())
    e1["numerical_values_checked"] = False
    e1["question_patterns"] = ordered_unique([p for part in e1["parts"] for p in part.get("question_patterns", [])])
    e1["mapping"]["topic_ids"] = ordered_unique([part["mapping"]["primary_topic_id"] for part in e1["parts"]])
    e1["mapping"]["module_ids"] = ordered_unique([part["mapping"]["primary_module_id"] for part in e1["parts"]])
    e1["mapping"]["outcome_ids"] = ordered_unique([o for part in e1["parts"] for o in part["mapping"].get("outcome_ids", [])])
    e1_path.write_text(json.dumps(e1, indent=2) + "\n")

    # --- Q02 ---
    q2_path = repo / f"subjects/physics/9702/papers/p2/questions/{stem}_qp_{var}/question_02.json"
    q2 = json.loads(q2_path.read_text())
    for p in q2["parts"]:
        if p["id"] == "9702_w25_21_q02_a":
            p["response_schema"] = None
        elif p["id"] == "9702_w25_21_q02_a_ii":
            p["question_text"] = (
                "Explain how hydrostatic pressure results in an upthrust force acting on a solid object immersed in a liquid."
            )
            p["question_text_latex"] = (
                "Explain how hydrostatic pressure results in an upthrust force acting on a solid object immersed in a liquid."
            )
        elif p["id"] == "9702_w25_21_q02_b":
            p["response_schema"] = None
            p["question_text"] = (
                "A solid ball falls vertically through a stationary liquid.\n"
                "The drag force D acting on the ball is given by\n"
                "D = 6πηrv\n"
                "where r is the radius of the ball, v is the speed of the ball and η is a constant for the liquid."
            )
            p["question_text_latex"] = (
                "A solid ball falls vertically through a stationary liquid.\n"
                "The drag force D acting on the ball is given by\n"
                "$$D = 6\\pi \\eta r v$$\n"
                "where r is the radius of the ball, v is the speed of the ball and $\\eta$ is a constant for the liquid."
            )
        elif p["id"] == "9702_w25_21_q02_b_i":
            p["question_text"] = (
                "On Fig. 2.1, draw labelled arrows from the ball to show the directions of the three forces that act on the ball as it falls."
            )
            p["question_text_latex"] = (
                "On Fig. 2.1, draw labelled arrows from the ball to show the directions of the three forces that act on the ball as it falls."
            )
        elif p["id"] == "9702_w25_21_q02_b_ii":
            p["question_text"] = "Show that the SI base units of η are kg m⁻¹ s⁻¹."
            p["question_text_latex"] = "Show that the SI base units of $\\eta$ are $\\text{kg}\\ \\text{m}^{-1}\\ \\text{s}^{-1}$."
        elif p["id"] == "9702_w25_21_q02_c":
            p["response_schema"] = None
        elif p["id"] == "9702_w25_21_q02_c_i":
            p["question_text_latex"] = "the drag force acting on the ball\n$\\text{drag force} = \\text{N}$"
        elif p["id"] == "9702_w25_21_q02_c_ii":
            p["question_text_latex"] = "the terminal speed v of the ball.\n$v = \\text{m}\\ \\text{s}^{-1}$"
    q2_path.write_text(json.dumps(q2, indent=2) + "\n")

    e2_path = repo / f"subjects/physics/9702/enrichment/p2/{paper}_q02.enrichment.json"
    e2 = json.loads(e2_path.read_text())
    e2["numerical_values_checked"] = False
    e2["question_patterns"] = ordered_unique([p for part in e2["parts"] for p in part.get("question_patterns", [])])
    e2["mapping"]["topic_ids"] = ordered_unique([part["mapping"]["primary_topic_id"] for part in e2["parts"]])
    e2["mapping"]["module_ids"] = ordered_unique([part["mapping"]["primary_module_id"] for part in e2["parts"]])
    e2["mapping"]["outcome_ids"] = ordered_unique([o for part in e2["parts"] for o in part["mapping"].get("outcome_ids", [])])
    e2_path.write_text(json.dumps(e2, indent=2) + "\n")

    # --- Q03 ---
    q3_path = repo / f"subjects/physics/9702/papers/p2/questions/{stem}_qp_{var}/question_03.json"
    q3 = json.loads(q3_path.read_text())
    for p in q3["parts"]:
        if p["id"] == "9702_w25_21_q03_b":
            p["response_schema"] = None
        elif p["id"] == "9702_w25_21_q03_b_i":
            p["question_text"] = (
                "State an expression, in terms of some or all of L, A, E and ρ, for the resistance R₀ of the wire.\n"
                "R₀ ="
            )
            p["question_text_latex"] = (
                "State an expression, in terms of some or all of L, A, E and $\\rho$, for the resistance $R_{0}$ of the wire.\n"
                "$R_{0} =$"
            )
        elif p["id"] == "9702_w25_21_q03_c":
            p["response_schema"] = None
            p["question_text"] = (
                "The wire is stretched, within the limit of proportionality, by a tensile force F. Assume that any changes in the cross-sectional area of the wire are negligible."
            )
            p["question_text_latex"] = (
                "The wire is stretched, within the limit of proportionality, by a tensile force F. Assume that any changes in the cross-sectional area of the wire are negligible."
            )
        elif p["id"] == "9702_w25_21_q03_d":
            p["response_schema"] = None
            p["question_text"] = (
                "Copper has a resistivity of 1.8 × 10⁻⁸ Ω m and a Young modulus of 1.3 × 10¹¹ Pa.\n"
                "A copper wire of diameter 1.6 mm has a resistance of 0.034 Ω."
            )
            p["question_text_latex"] = (
                "Copper has a resistivity of $1.8 \\times 10^{-8}\\,\\mathrm{\\Omega}\\,\\mathrm{m}$ and a Young modulus of $1.3 \\times 10^{11}$ Pa.\n"
                "A copper wire of diameter 1.6 mm has a resistance of 0.034 $\\Omega$."
            )
        elif p["id"] == "9702_w25_21_q03_d_ii":
            p["question_text_latex"] = (
                "Use the equation in (b)(ii) to determine the spring constant of the wire.\n"
                "$\\text{spring constant} = \\text{N}\\ \\text{m}^{-1}$"
            )
    q3_path.write_text(json.dumps(q3, indent=2) + "\n")

    e3_path = repo / f"subjects/physics/9702/enrichment/p2/{paper}_q03.enrichment.json"
    e3 = json.loads(e3_path.read_text())
    e3["numerical_values_checked"] = False
    for ep in e3["parts"]:
        if ep["part_id"] == "9702_w25_21_q03_c_i":
            ep["mapping"]["outcome_ids"] = ["9702_t09_m03_o06"]
    e3["question_patterns"] = ordered_unique([p for part in e3["parts"] for p in part.get("question_patterns", [])])
    e3["mapping"]["topic_ids"] = ordered_unique([part["mapping"]["primary_topic_id"] for part in e3["parts"]])
    e3["mapping"]["module_ids"] = ordered_unique([part["mapping"]["primary_module_id"] for part in e3["parts"]])
    e3["mapping"]["outcome_ids"] = ordered_unique([o for part in e3["parts"] for o in part["mapping"].get("outcome_ids", [])])
    e3_path.write_text(json.dumps(e3, indent=2) + "\n")

    # --- Q04 ---
    q4_path = repo / f"subjects/physics/9702/papers/p2/questions/{stem}_qp_{var}/question_04.json"
    q4 = json.loads(q4_path.read_text())
    for p in q4["parts"]:
        if p["id"] == "9702_w25_21_q04_b":
            p["response_schema"] = None
            p["question_text"] = (
                "A beam of vertically polarised light of wavelength 540 nm is incident normally on a diffraction grating, as shown in Fig. 4.1.\n"
                "The diffraction grating has a line spacing of 5.0 × 10⁻⁶ m.\n"
                "The light transmitted by the diffraction grating illuminates a circular screen. The diffraction grating is at the centre X of the circle.\n"
                "The central bright fringe is formed at point O on the screen and has intensity I₀.\n"
                "P is a point on the screen where the line XP is at a variable angle θ to the line XO. The intensity I of light on the screen at P varies with θ."
            )
            p["question_text_latex"] = (
                "A beam of vertically polarised light of wavelength 540 nm is incident normally on a diffraction grating, as shown in Fig. 4.1.\n"
                "The diffraction grating has a line spacing of $5.0 \\times 10^{-6}\\,\\mathrm{m}$.\n"
                "The light transmitted by the diffraction grating illuminates a circular screen. The diffraction grating is at the centre X of the circle.\n"
                "The central bright fringe is formed at point O on the screen and has intensity $I_{0}$.\n"
                "P is a point on the screen where the line XP is at a variable angle $\\theta$ to the line XO. The intensity I of light on the screen at P varies with $\\theta$."
            )
        elif p["id"] == "9702_w25_21_q04_b_ii":
            p["question_text_latex"] = (
                "Determine the value of θ at which the second-order bright fringe is formed.\n"
                "$\\theta = ^\\circ$"
            )
        elif p["id"] == "9702_w25_21_q04_c":
            p["question_text"] = (
                "A polarising filter is placed in the path of the light beam that is incident on the diffraction grating in Fig. 4.1. The transmission axis of the filter is at 45° to the vertical.\n"
                "Suggest how the variation of intensity with θ for the light on the screen compares with the answer in (b)(iii)."
            )
            p["question_text_latex"] = (
                "A polarising filter is placed in the path of the light beam that is incident on the diffraction grating in Fig. 4.1. The transmission axis of the filter is at 45° to the vertical.\n"
                "Suggest how the variation of intensity with θ for the light on the screen compares with the answer in (b)(iii)."
            )
    q4_path.write_text(json.dumps(q4, indent=2) + "\n")

    e4_path = repo / f"subjects/physics/9702/enrichment/p2/{paper}_q04.enrichment.json"
    e4 = json.loads(e4_path.read_text())
    e4["numerical_values_checked"] = False
    e4["question_patterns"] = ordered_unique([p for part in e4["parts"] for p in part.get("question_patterns", [])])
    e4["mapping"]["topic_ids"] = ordered_unique([part["mapping"]["primary_topic_id"] for part in e4["parts"]])
    e4["mapping"]["module_ids"] = ordered_unique([part["mapping"]["primary_module_id"] for part in e4["parts"]])
    e4["mapping"]["outcome_ids"] = ordered_unique([o for part in e4["parts"] for o in part["mapping"].get("outcome_ids", [])])
    e4_path.write_text(json.dumps(e4, indent=2) + "\n")

    # --- Q05 ---
    q5_path = repo / f"subjects/physics/9702/papers/p2/questions/{stem}_qp_{var}/question_05.json"
    q5 = json.loads(q5_path.read_text())
    for p in q5["parts"]:
        if p["id"] == "9702_w25_21_q05_b":
            p["response_schema"] = None
        elif p["id"] == "9702_w25_21_q05_b_i":
            p["question_text"] = (
                "The thermistor has resistance R₀ at a temperature of 0 °C.\n"
                "On Fig. 5.2, sketch a possible variation of the resistance of the thermistor with temperature between 0 °C and 100 °C."
            )
            p["question_text_latex"] = (
                "The thermistor has resistance $R_{0}$ at a temperature of 0 °C.\n"
                "On Fig. 5.2, sketch a possible variation of the resistance of the thermistor with temperature between 0 °C and 100 °C."
            )
        elif p["id"] == "9702_w25_21_q05_b_ii":
            p["question_text"] = (
                "With reference to the current in the cell, explain why the current in resistor R decreases with increasing temperature of the thermistor."
            )
            p["question_text_latex"] = (
                "With reference to the current in the cell, explain why the current in resistor R decreases with increasing temperature of the thermistor."
            )
        elif p["id"] == "9702_w25_21_q05_c":
            p["response_schema"] = None
            p["question_text"] = (
                "The electromotive force (e.m.f.) E of the cell in Fig. 5.1 is 1.50 V. The internal resistance r of the cell is 0.12 Ω.\n"
                "Resistor R has a resistance of 6.00 Ω.\n"
                "At a particular temperature of the thermistor, the current in R is 0.200 A.\n"
                "For this temperature of the thermistor, determine:"
            )
            p["question_text_latex"] = (
                "The electromotive force (e.m.f.) E of the cell in Fig. 5.1 is 1.50 V. The internal resistance r of the cell is 0.12 $\\Omega$.\n"
                "Resistor R has a resistance of 6.00 $\\Omega$.\n"
                "At a particular temperature of the thermistor, the current in R is 0.200 A.\n"
                "For this temperature of the thermistor, determine:"
            )
        elif p["id"] == "9702_w25_21_q05_c_i":
            p["question_text_latex"] = "the current in the cell\n$\\text{current} = \\text{A}$"
        elif p["id"] == "9702_w25_21_q05_c_ii":
            p["question_text_latex"] = "the resistance of the thermistor.\n$\\text{resistance} = \\Omega$"
    q5_path.write_text(json.dumps(q5, indent=2) + "\n")

    e5_path = repo / f"subjects/physics/9702/enrichment/p2/{paper}_q05.enrichment.json"
    e5 = json.loads(e5_path.read_text())
    e5["numerical_values_checked"] = False
    for ep in e5["parts"]:
        if ep["part_id"] == "9702_w25_21_q05_b_i":
            ep["skills"]["primary_skill_id"] = "9702_skill_iv_characteristics"
        elif ep["part_id"] == "9702_w25_21_q05_c_i":
            ep["mapping"]["outcome_ids"] = ["9702_t10_m01_o05"]
        elif ep["part_id"] == "9702_w25_21_q05_c_ii":
            ep["mapping"]["outcome_ids"] = ["9702_t10_m02_o01", "9702_t10_m02_o07"]
    e5["question_patterns"] = ordered_unique([p for part in e5["parts"] for p in part.get("question_patterns", [])])
    e5["mapping"]["topic_ids"] = ordered_unique([part["mapping"]["primary_topic_id"] for part in e5["parts"]])
    e5["mapping"]["module_ids"] = ordered_unique([part["mapping"]["primary_module_id"] for part in e5["parts"]])
    e5["mapping"]["outcome_ids"] = ordered_unique([o for part in e5["parts"] for o in part["mapping"].get("outcome_ids", [])])
    e5_path.write_text(json.dumps(e5, indent=2) + "\n")

    # --- Q06 ---
    q6_path = repo / f"subjects/physics/9702/papers/p2/questions/{stem}_qp_{var}/question_06.json"
    q6 = json.loads(q6_path.read_text())
    for p in q6["parts"]:
        if p["id"] == "9702_w25_21_q06_a":
            p["response_schema"] = None
        elif p["id"] == "9702_w25_21_q06_a_i":
            p["question_text_latex"] = (
                "Determine the numbers of protons, neutrons and electrons in a neutral atom of tritium.\n"
                "$\\text{number of electrons} =$"
            )
        elif p["id"] == "9702_w25_21_q06_a_ii":
            p["question_text"] = (
                "Draw a labelled diagram to represent a simple model of the arrangement of the protons, neutrons and electrons in a tritium atom."
            )
            p["question_text_latex"] = (
                "Draw a labelled diagram to represent a simple model of the arrangement of the protons, neutrons and electrons in a tritium atom."
            )
        elif p["id"] == "9702_w25_21_q06_b":
            p["response_schema"] = None
            p["question_text"] = (
                "Tritium is radioactive and undergoes β⁻ decay to form an isotope of helium (He). Gamma radiation is not emitted during this decay."
            )
            p["question_text_latex"] = (
                "Tritium is radioactive and undergoes $\\beta^{-}$ decay to form an isotope of helium (He). Gamma radiation is not emitted during this decay."
            )
        elif p["id"] == "9702_w25_21_q06_b_i":
            p["question_text"] = (
                "Complete the equation to represent the radioactive decay of tritium.\n"
                "³₁H → ___ He + ___ β + ⁰₀X"
            )
            p["question_text_latex"] = (
                "Complete the equation to represent the radioactive decay of tritium.\n"
                "$$^{3}_{1}\\text{H} \\rightarrow \\, ^{...}_{...}\\text{He} + \\, ^{...}_{...}\\beta + \\, ^{0}_{0}\\text{X}$$"
            )
    q6_path.write_text(json.dumps(q6, indent=2) + "\n")

    e6_path = repo / f"subjects/physics/9702/enrichment/p2/{paper}_q06.enrichment.json"
    e6 = json.loads(e6_path.read_text())
    e6["numerical_values_checked"] = False
    e6["question_patterns"] = ordered_unique([p for part in e6["parts"] for p in part.get("question_patterns", [])])
    e6["mapping"]["topic_ids"] = ordered_unique([part["mapping"]["primary_topic_id"] for part in e6["parts"]])
    e6["mapping"]["module_ids"] = ordered_unique([part["mapping"]["primary_module_id"] for part in e6["parts"]])
    e6["mapping"]["outcome_ids"] = ordered_unique([o for part in e6["parts"] for o in part["mapping"].get("outcome_ids", [])])
    e6_path.write_text(json.dumps(e6, indent=2) + "\n")

if __name__ == "__main__":
    repair_s25_24()
    repair_w25_21()
    print("Repairs completed successfully.")
