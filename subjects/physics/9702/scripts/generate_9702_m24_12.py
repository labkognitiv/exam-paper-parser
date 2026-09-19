#!/usr/bin/env python3
"""
generate_9702_m24_12.py

Generates high-quality P1 MCQ enrichment records for paper 9702_m24_12 (Q01-Q40).
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "subjects/physics/9702/enrichment/p1"
OUT_DIR.mkdir(parents=True, exist_ok=True)

RECORDS = [
    # Q01
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q01",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": ["property_identification", "classification"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m02",
        "skill_id": "9702_skill_recall_si_base_units",
        "accepted_answer": "A",
        "hints": [
            "Identify which quantities belong to the seven SI base quantities and recall their standard base units.",
            "Recall that current has the SI base unit ampere ($\\text{A}$), while newton is a derived unit and gram and degree Celsius are not SI base units."
        ],
        "walkthrough": [
            "In the SI system, electric current is a fundamental base quantity with the base unit ampere (symbol $\\text{A}$). Therefore, row A correctly matches a physical quantity with its SI base unit.",
            "Evaluating the other options: force has unit newton ($\\text{N}$), which is a derived unit equivalent to $\\text{kg}\\cdot\\text{m}\\cdot\\text{s}^{-2}$; mass is a base quantity but its SI base unit is the kilogram ($\\text{kg}$), not the gram ($\\text{g}$); thermodynamic temperature is a base quantity but its SI base unit is the kelvin ($\\text{K}$), not the degree Celsius ($^\\circ\\text{C}$)."
        ]
    },
    # Q02
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q02",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": ["direct_calculation"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_apply_newtons_second_law",
        "accepted_answer": "A",
        "hints": [
            "Calculate the resultant horizontal force acting on the car by subtracting the opposing forces.",
            "Apply Newton's second law, $F_{\\text{net}} = ma$, to determine the acceleration."
        ],
        "walkthrough": [
            "The two horizontal forces act in opposite directions along a straight line, so the resultant force has magnitude $F_{\\text{net}} = 1600\\,\\text{N} - 1200\\,\\text{N} = 400\\,\\text{N}$.",
            "Using Newton's second law, $a = \\frac{F_{\\text{net}}}{m} = \\frac{400\\,\\text{N}}{850\\,\\text{kg}} \\approx 0.4706\\,\\text{m}\\,\\text{s}^{-2} \\approx 0.47\\,\\text{m}\\,\\text{s}^{-2}$. This matches option A."
        ]
    },
    # Q03
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q03",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["equation_recall", "direct_calculation"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m02",
        "skill_id": "9702_skill_derive_si_base_units",
        "accepted_answer": "D",
        "hints": [
            "Express the SI base units of mass $m$ and spring constant $k$ using fundamental SI units.",
            "Recall that $k = \\frac{F}{x}$, giving base units of $\\text{kg}\\,\\text{s}^{-2}$. Check which expression yields the base unit of time ($\\text{s}$)."
        ],
        "walkthrough": [
            "The SI base unit of mass $m$ is $\\text{kg}$. The spring constant $k$ is defined by $k = \\frac{F}{x}$, so its base units are $\\frac{\\text{kg}\\,\\text{m}\\,\\text{s}^{-2}}{\\text{m}} = \\text{kg}\\,\\text{s}^{-2}$.",
            "Evaluating the ratio $\\frac{m}{k}$ gives $\\frac{\\text{kg}}{\\text{kg}\\,\\text{s}^{-2}} = \\text{s}^2$. Taking the square root gives $\\sqrt{\\frac{m}{k}} = \\sqrt{\\text{s}^2} = \\text{s}$. Since period $T$ has the base unit of seconds ($\\text{s}$), the equation $T = 2\\pi\\sqrt{\\frac{m}{k}}$ is homogeneous with respect to base units (option D)."
        ]
    },
    # Q04
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q04",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": ["explanation", "property_identification"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_state_newtons_second_law",
        "accepted_answer": "B",
        "hints": [
            "Relate resultant force to acceleration for an object of constant mass using Newton's second law.",
            "Uniform acceleration means the acceleration is constant and non-zero over time."
        ],
        "walkthrough": [
            "According to Newton's second law of motion, the resultant force acting on a body of fixed mass $m$ is directly proportional to its acceleration: $F = ma$.",
            "Because the object moves with uniform (constant non-zero) acceleration, the resultant force $F$ must also be constant and non-zero throughout the motion. Hence, option B is correct."
        ]
    },
    # Q05
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q05",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["direct_calculation"],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_resolve_velocity_components",
        "accepted_answer": "B",
        "hints": [
            "Use trigonometry to relate the horizontal and vertical components of the launch velocity.",
            "Note that $\\tan(\\theta) = \\frac{v_y}{v_x}$ with launch angle $\\theta = 25^\\circ$ and $v_x = 13\\,\\text{m}\\,\\text{s}^{-1}$."
        ],
        "walkthrough": [
            "The launch velocity vector $v$ makes an angle of $\\theta = 25^\\circ$ with the horizontal, so its components are $v_x = v\\cos(\\theta)$ and $v_y = v\\sin(\\theta)$.",
            "Dividing the vertical component by the horizontal component gives $\\frac{v_y}{v_x} = \\tan(\\theta)$, so $v_y = v_x \\tan(25^\\circ) = 13\\,\\text{m}\\,\\text{s}^{-1} \\times \\tan(25^\\circ) \\approx 13 \\times 0.46631 = 6.062\\,\\text{m}\\,\\text{s}^{-1} \\approx 6.1\\,\\text{m}\\,\\text{s}^{-1}$. This corresponds to option B."
        ]
    },
    # Q06
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q06",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["graph_interpretation", "direct_calculation"],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_determine_displacement_from_velocity_time_graph",
        "accepted_answer": "B",
        "hints": [
            "Recall that displacement is the signed area under a velocity-time graph.",
            "Calculate the positive area from $t = 0$ to $1.0\\,\\text{s}$ and subtract the negative area from $t = 1.0\\,\\text{s}$ to $1.5\\,\\text{s}$."
        ],
        "walkthrough": [
            "The displacement of the ball is given by the area under the velocity–time graph. From $t = 0$ to $t = 1.0\\,\\text{s}$, the ball falls downwards: $\\Delta s_1 = \\frac{1}{2} \\times 1.0\\,\\text{s} \\times 10\\,\\text{m}\\,\\text{s}^{-1} = +5.00\\,\\text{m}$.",
            "From $t = 1.0\\,\\text{s}$ to $t = 1.5\\,\\text{s}$, the ball rebounds upwards with negative velocity: $\\Delta s_2 = \\frac{1}{2} \\times (1.5 - 1.0)\\,\\text{s} \\times (-5.0\\,\\text{m}\\,\\text{s}^{-1}) = -1.25\\,\\text{m}$. The total displacement from position X at $1.5\\,\\text{s}$ is $s = \\Delta s_1 + \\Delta s_2 = 5.00\\,\\text{m} - 1.25\\,\\text{m} = 3.75\\,\\text{m}$ (option B)."
        ]
    },
    # Q07
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q07",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": ["definition"],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_define_acceleration",
        "accepted_answer": "A",
        "hints": [
            "Recall the standard AS Physics definition of acceleration as a vector rate.",
            "Acceleration is the change in velocity divided by the time taken, expressed as change in velocity per unit time."
        ],
        "walkthrough": [
            "Acceleration is formally defined in physics as the rate of change of velocity, which is equivalently stated as the change in velocity per unit time ($a = \\frac{\\Delta v}{\\Delta t}$). Hence, option A is correct.",
            "Option C adds an unnecessary redundancy ('rate of change ... per unit time'), option B refers to the scalar speed rather than vector velocity, and option D states Newton's second law relation rather than the kinematic definition of acceleration."
        ]
    },
    # Q08
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q08",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["property_identification", "direct_calculation"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m03",
        "skill_id": "9702_skill_apply_momentum_conservation",
        "accepted_answer": "D",
        "hints": [
            "In a one-dimensional perfectly elastic collision between two identical masses, the colliding bodies exchange their velocities.",
            "Verify that total momentum and relative speed of approach equal relative speed of separation."
        ],
        "walkthrough": [
            "For a perfectly elastic head-on collision between two objects of equal mass $m_P = m_Q = m$, conservation of momentum and kinetic energy requires that the two bodies completely exchange their velocities.",
            "Before the collision, $u_P = +1.30\\,\\text{m}\\,\\text{s}^{-1}$ (to the right) and $u_Q = -0.50\\,\\text{m}\\,\\text{s}^{-1}$ (to the left). After the collision, ball P moves left with $v_P = -0.50\\,\\text{m}\\,\\text{s}^{-1}$ and ball Q moves right with $v_Q = +1.30\\,\\text{m}\\,\\text{s}^{-1}$. This matches diagram D."
        ]
    },
    # Q09
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q09",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["direct_calculation"],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_apply_constant_acceleration",
        "accepted_answer": "B",
        "hints": [
            "Use the kinematic equation $v^2 = u^2 + 2as$ for downward motion under gravity.",
            "Take initial speed $u = 2.4\\,\\text{m}\\,\\text{s}^{-1}$, acceleration $a = 9.81\\,\\text{m}\\,\\text{s}^{-2}$, and distance $s = 0.90\\,\\text{m}$."
        ],
        "walkthrough": [
            "The ball is hit downwards with initial velocity $u = 2.4\\,\\text{m}\\,\\text{s}^{-1}$ and accelerates downwards under gravity ($g = 9.81\\,\\text{m}\\,\\text{s}^{-2}$) through a vertical distance $s = 0.90\\,\\text{m}$.",
            "Applying $v^2 = u^2 + 2gs$: $v^2 = (2.4)^2 + 2(9.81)(0.90) = 5.76 + 17.658 = 23.418\\,\\text{m}^2\\,\\text{s}^{-2}$. Taking the square root gives $v = \\sqrt{23.418} \\approx 4.839\\,\\text{m}\\,\\text{s}^{-2} \\approx 4.8\\,\\text{m}\\,\\text{s}^{-1}$ (option B)."
        ]
    },
    # Q10
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q10",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["explanation", "property_identification"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m03",
        "skill_id": "9702_skill_explain_upthrust",
        "accepted_answer": "C",
        "hints": [
            "Recall Archimedes' principle: upthrust equals the weight of fluid displaced.",
            "Consider how fluid density and displaced volume behave as depth changes in an incompressible liquid."
        ],
        "walkthrough": [
            "According to Archimedes' principle, upthrust is given by $U = \\rho_{\\text{liquid}} V g$, where $V$ is the fully submerged volume of the ball and $\\rho_{\\text{liquid}}$ is the liquid density. Because the liquid has uniform density and the ball is incompressible, the upthrust remains constant as depth increases (option C).",
            "For a ball moving at constant terminal speed, the resultant vertical force is zero, meaning weight equals the sum of drag force and upthrust ($W = F_{\\text{drag}} + U$). Because speed is constant, the drag force also does not change with depth."
        ]
    },
    # Q11
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q11",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["multi_step_calculation"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m03",
        "skill_id": "9702_skill_apply_density",
        "accepted_answer": "C",
        "hints": [
            "Calculate how many small cubes fit along one side of the large cube, then find the total number of cubes.",
            "Find the total mass of the stacked cubes and calculate the weight using $W = mg$."
        ],
        "walkthrough": [
            "Along each edge of the large cube of side $2.0\\,\\text{m}$, the number of small cubes of side $5.0\\,\\text{cm} = 0.050\\,\\text{m}$ is $n = \\frac{2.0\\,\\text{m}}{0.050\\,\\text{m}} = 40$.",
            "The total number of small cubes making up the large solid cube is $N = 40^3 = 64\\,000$. The total mass is $M = 64\\,000 \\times 1.0\\,\\text{kg} = 6.4 \\times 10^4\\,\\text{kg}$. The weight is $W = Mg = 6.4 \\times 10^4\\,\\text{kg} \\times 9.81\\,\\text{m}\\,\\text{s}^{-2} \\approx 6.278 \\times 10^5\\,\\text{N} \\approx 0.63\\,\\text{MN}$ (option C)."
        ]
    },
    # Q12
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q12",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": ["multi_step_calculation", "direct_calculation"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m03",
        "skill_id": "9702_skill_apply_hydrostatic_pressure",
        "accepted_answer": "D",
        "hints": [
            "Express the total hydrostatic pressure at the bottom as the sum of pressures due to the oil layer and water layer.",
            "Set $P = \\rho_{\\text{oil}} g x + \\rho_{\\text{water}} g (2000 - x) = 17.5 \\times 10^6\\,\\text{Pa}$ and solve for $x$."
        ],
        "walkthrough": [
            "The total liquid pressure at the base is $P = \\rho_{\\text{oil}} g x + \\rho_{\\text{water}} g (2000 - x) = 17.5 \\times 10^6\\,\\text{Pa}$.",
            "Dividing both sides by $g = 9.81\\,\\text{m}\\,\\text{s}^{-2}$: $(830)x + 1000(2000 - x) = \\frac{17.5 \\times 10^6}{9.81} \\approx 1\\,783\\,894$. Simplifying gives $2\\,000\\,000 - 170x = 1\\,783\\,894 \\implies 170x = 216\\,106 \\implies x \\approx 1271\\,\\text{m} \\approx 1270\\,\\text{m}$ (option D)."
        ]
    },
    # Q13
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q13",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["graph_interpretation"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_calculate_moment_from_line_of_action",
        "accepted_answer": "D",
        "hints": [
            "Determine how the perpendicular distance from the pivot to the line of action of the rod's weight depends on angle $\\theta$.",
            "The perpendicular distance is $d_{\\perp} = \\frac{L}{2}\\cos(\\theta)$. Check the values of moment $M$ at angles $\\theta = 0^\\circ$, $\\theta = 90^\\circ$, and $\\theta = 180^\\circ$."
        ],
        "walkthrough": [
            "The weight $W$ of the rod acts downwards through its centre of gravity at distance $\\frac{L}{2}$ from the pivot. When the rod is tilted at angle $\\theta$ to the horizontal, the perpendicular distance from the pivot to the line of action of the weight is $d_{\\perp} = \\frac{L}{2}\\cos(\\theta)$.",
            "The magnitude of the moment is $M = W d_{\\perp} = W \\frac{L}{2} |\\cos(\\theta)|$. At $\\theta = 0^\\circ$, $M$ is maximum; at $\\theta = 90^\\circ$ (vertical rod), the line of action passes through the pivot so $M = 0$; at $\\theta = 180^\\circ$ (horizontal rod pointing opposite), $M$ is again maximum. Graph D correctly illustrates this cosine profile."
        ]
    },
    # Q14
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q14",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": ["force_diagram_construction", "comparison"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m02",
        "skill_id": "9702_skill_determine_support_force_from_vertical_equilibrium",
        "accepted_answer": "C",
        "hints": [
            "Use the principle of moments about the hinge to relate cable tension $T$ to door weight $W$.",
            "Consider horizontal and vertical force components at equilibrium to compare the magnitudes of $W$, $H$, and $T$."
        ],
        "walkthrough": [
            "Taking moments about the hinge for horizontal trapdoor length $L$: the weight acts at $\\frac{L}{2}$ while the cable pulls at angle $\\theta$ from the far end $L$. Thus $T\\sin(\\theta) \\cdot L = W \\cdot \\frac{L}{2} \\implies T\\sin(\\theta) = \\frac{W}{2}$. For shallow cable angles ($\\sin(\\theta) < 0.5$), $T > W$.",
            "At the hinge, the horizontal force component balances the horizontal cable tension ($H_x = T\\cos(\\theta)$), and vertical force balances $H_y = W - T\\sin(\\theta) = \\frac{W}{2}$. Combining components yields $W < H < T$. Thus, in increasing order of magnitude, the forces are $W, H, T$ (option C)."
        ]
    },
    # Q15
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q15",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": ["definition"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_define_force",
        "accepted_answer": "C",
        "hints": [
            "Recall Newton's second law in its most fundamental definition.",
            "Force is defined as the rate of change of momentum with respect to time."
        ],
        "walkthrough": [
            "In physics, force is fundamentally defined as the rate of change of momentum: $F = \\frac{\\Delta p}{\\Delta t}$. This directly matches option C.",
            "Option A ($ma$) is the formula for resultant force only when mass remains constant, option B defines momentum itself, and option D defines power."
        ]
    },
    # Q16
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q16",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": ["equation_recall"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_apply_mechanical_power",
        "accepted_answer": "B",
        "hints": [
            "Recall the relationship connecting mechanical power, driving force, and constant speed.",
            "When moving at constant velocity against a resistive force $F$, the forward force equals $F$, giving $P = Fv$."
        ],
        "walkthrough": [
            "To travel at constant velocity $v$, the forward driving force provided by the boat must equal the resistive drag force $F$ in magnitude to give zero net acceleration.",
            "Mechanical power is defined as the rate of doing work: $P = \\frac{W}{t} = \\frac{F \\cdot s}{t} = Fv$. Hence, the power used by the boat is $Fv$ (option B)."
        ]
    },
    # Q17
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q17",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["force_diagram_construction", "direct_calculation"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_apply_torque_of_couple",
        "accepted_answer": "D",
        "hints": [
            "Check both conditions for static equilibrium: zero resultant force and zero resultant torque.",
            "Identify the two couples formed by the opposing horizontal and vertical forces and calculate their sum."
        ],
        "walkthrough": [
            "The two horizontal forces of magnitude $F$ act in opposite directions with perpendicular separation $d$, forming a couple of torque $\\tau_1 = Fd$. The two vertical forces of magnitude $F$ also act in opposite directions with separation $d$, forming a second couple of torque $\\tau_2 = Fd$ in the same rotational sense.",
            "Although the resultant linear force is zero ($\\Sigma F_x = 0$ and $\\Sigma F_y = 0$), the total resultant torque is non-zero: $\\tau_{\\text{net}} = Fd + Fd = 2Fd$. Therefore, the disc is not in equilibrium because the resultant torque is $2Fd$ (option D)."
        ]
    },
    # Q18
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q18",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["comparison", "direct_calculation"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m02",
        "skill_id": "9702_skill_compare_gravitational_potential_and_kinetic_energy",
        "accepted_answer": "A",
        "hints": [
            "In the absence of air resistance, the change in kinetic energy between two points is equal in magnitude to the change in gravitational potential energy, $|\\Delta E_k| = mg|\\Delta h|$.",
            "Calculate the vertical height differences $|h_1 - h_2|$ for each pair of points."
        ],
        "walkthrough": [
            "By conservation of mechanical energy, the total energy $E_k + E_p$ is constant throughout the projectile motion. Therefore, the difference in kinetic energy between two points is $|\\Delta E_k| = mg |\\Delta h|$.",
            "Evaluating height differences: for A ($E_Q - E_S$), $|\\Delta h| = |1.5\\,\\text{m} - 1.6\\,\\text{m}| = 0.1\\,\\text{m}$; for B ($E_S - E_R$), $|\\Delta h| = |1.6\\,\\text{m} - 1.8\\,\\text{m}| = 0.2\\,\\text{m}$; for C ($E_T - E_Q$), $|\\Delta h| = |1.3\\,\\text{m} - 1.5\\,\\text{m}| = 0.2\\,\\text{m}$; for D ($E_T - E_R$), $|\\Delta h| = |1.3\\,\\text{m} - 1.8\\,\\text{m}| = 0.5\\,\\text{m}$. The smallest height difference is $0.1\\,\\text{m}$, making $E_Q - E_S$ the smallest kinetic energy difference (option A)."
        ]
    },
    # Q19
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q19",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["multi_step_calculation", "direct_calculation"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_apply_efficiency",
        "accepted_answer": "C",
        "hints": [
            "Calculate the total electrical input energy by multiplying power by time in seconds.",
            "Multiply the input energy by the efficiency (0.80) to find the stored energy."
        ],
        "walkthrough": [
            "The total energy supplied to the charging circuit is $E_{\\text{in}} = P \\times t = 10\\,\\text{W} \\times (2.0 \\times 3600\\,\\text{s}) = 7.2 \\times 10^4\\,\\text{J}$.",
            "With an efficiency of $\\eta = 80\\% = 0.80$, the energy stored in the battery is $E_{\\text{stored}} = 0.80 \\times 7.2 \\times 10^4\\,\\text{J} = 5.76 \\times 10^4\\,\\text{J} \\approx 5.8 \\times 10^4\\,\\text{J}$ (option C)."
        ]
    },
    # Q20
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q20",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": ["multi_step_calculation", "equation_derivation"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m03",
        "skill_id": "9702_skill_apply_momentum_conservation",
        "accepted_answer": "D",
        "hints": [
            "Apply conservation of linear momentum to relate the speed of fragment $m$ to the speed of fragment $2m$.",
            "Express total kinetic energy $E$ in terms of $m$ and $v_m$, then rearrange for $v_m$."
        ],
        "walkthrough": [
            "From conservation of linear momentum for an initially stationary body: $m v_1 = (2m) v_2$, which yields $v_2 = \\frac{v_1}{2}$.",
            "The total kinetic energy transferred is $E = \\frac{1}{2} m v_1^2 + \\frac{1}{2} (2m) v_2^2 = \\frac{1}{2} m v_1^2 + m \\left(\\frac{v_1}{2}\\right)^2 = \\frac{1}{2} m v_1^2 + \\frac{1}{4} m v_1^2 = \\frac{3}{4} m v_1^2$. Solving for $v_1$ gives $v_1^2 = \\frac{4E}{3m} \\implies v_1 = \\sqrt{\\frac{4E}{3m}}$ (option D)."
        ]
    },
    # Q21
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q21",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": ["property_identification", "equation_recall"],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m02",
        "skill_id": "9702_skill_apply_elastic_potential_energy",
        "accepted_answer": "D",
        "hints": [
            "Recall the formula for the elastic potential energy of a spring obeying Hooke's law in terms of extension $x$.",
            "Notice that $E_P = \\frac{1}{2}kx^2$, where $k$ is a constant for a given spring."
        ],
        "walkthrough": [
            "For a spring obeying Hooke's law ($F = kx$), the elastic potential energy stored is given by $E_P = \\frac{1}{2} k x^2$.",
            "Since the spring constant $k$ is constant for a particular spring, the elastic potential energy is directly proportional to the square of the extension: $E_P \\propto x^2$. Hence, option D is correct."
        ]
    },
    # Q22
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q22",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": ["definition", "property_identification"],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m02",
        "skill_id": "9702_skill_locate_limit_of_proportionality",
        "accepted_answer": "B",
        "hints": [
            "Distinguish between the limit of proportionality and the elastic limit on a force-extension graph.",
            "The limit of proportionality is the specific point where the linear relationship between force and extension ends."
        ],
        "walkthrough": [
            "Hooke's law states that force is directly proportional to extension up to the limit of proportionality. Beyond this point, the force–extension graph becomes non-linear and Hooke's law is no longer obeyed (option B).",
            "Option A describes the breaking/fracture point, while options C and D describe the elastic limit beyond which permanent plastic deformation occurs."
        ]
    },
    # Q23
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q23",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["multi_step_calculation", "direct_calculation"],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m02",
        "skill_id": "9702_skill_apply_hookes_law",
        "accepted_answer": "D",
        "hints": [
            "For two springs connected in series, the same tension force acts through both springs.",
            "Calculate the extension of each spring separately using $x = \\frac{F}{k}$ and add them together."
        ],
        "walkthrough": [
            "When springs are connected end-to-end in series, both springs support the full applied load of $F = 80\\,\\text{N}$.",
            "The extension of the top spring is $x_1 = \\frac{80\\,\\text{N}}{6.0\\,\\text{N}\\,\\text{cm}^{-1}} = 13.33\\,\\text{cm}$, and the extension of the bottom spring is $x_2 = \\frac{80\\,\\text{N}}{4.0\\,\\text{N}\\,\\text{cm}^{-1}} = 20.0\\,\\text{cm}$. The total extension of the composite spring is $x = x_1 + x_2 = 13.33\\,\\text{cm} + 20.0\\,\\text{cm} = 33.33\\,\\text{cm} \\approx 33\\,\\text{cm}$ (option D)."
        ]
    },
    # Q24
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q24",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["direct_calculation"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_apply_wave_speed",
        "accepted_answer": "D",
        "hints": [
            "Use the wave equation $v = f\\lambda$ rewritten as $\\lambda = \\frac{v}{f}$.",
            "Convert the wave speed from $\\text{km}\\,\\text{s}^{-1}$ to $\\text{m}\\,\\text{s}^{-1}$ before calculating wavelengths."
        ],
        "walkthrough": [
            "The speed of sound in seawater is $v = 1.5\\,\\text{km}\\,\\text{s}^{-1} = 1500\\,\\text{m}\\,\\text{s}^{-1}$. Using the wave equation $\\lambda = \\frac{v}{f}$:",
            "For the maximum frequency $f = 40\\,\\text{Hz}$, the minimum wavelength is $\\lambda_{\\text{min}} = \\frac{1500}{40} = 37.5\\,\\text{m} \\approx 38\\,\\text{m}$. For the minimum frequency $f = 10\\,\\text{Hz}$, the maximum wavelength is $\\lambda_{\\text{max}} = \\frac{1500}{10} = 150\\,\\text{m}$. The wavelength range is approximately $\\lambda = 38\\,\\text{m}$ to $\\lambda = 150\\,\\text{m}$ (option D)."
        ]
    },
    # Q25
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q25",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["graph_interpretation", "direct_calculation"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_interpret_oscilloscope_traces",
        "accepted_answer": "A",
        "hints": [
            "Determine the time period of the wave from its frequency $f = 2.5\\,\\text{kHz}$.",
            "Measure the horizontal distance representing one full cycle on the CRO screen and divide time period by this distance."
        ],
        "walkthrough": [
            "The time period of the sound wave is $T = \\frac{1}{f} = \\frac{1}{2500\\,\\text{Hz}} = 4.0 \\times 10^{-4}\\,\\text{s} = 0.40\\,\\text{ms}$.",
            "From the CRO grid, one full wave cycle spans $4\\,\\text{cm}$ horizontally. The time-base setting is therefore $\\frac{0.40\\,\\text{ms}}{4\\,\\text{cm}} = 0.1\\,\\text{ms}\\,\\text{cm}^{-1}$ (option A)."
        ]
    },
    # Q26
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q26",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["property_identification", "explanation"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m03",
        "skill_id": "9702_skill_define_doppler_effect",
        "accepted_answer": "C",
        "hints": [
            "Consider what happens to wavefronts emitted by a source as it moves towards an observer.",
            "The source 'catches up' with its own emitted waves, reducing the spatial distance between successive wavefronts."
        ],
        "walkthrough": [
            "As the sound source moves towards the stationary observer, successive wavefronts are emitted closer together in space in the direction of motion, so the observed wavelength is decreased: $\\lambda_{\\text{obs}} = \\frac{v - v_s}{f} < \\lambda$ (option C).",
            "Because the sound speed $v$ in the medium remains constant, the decreased wavelength results in an increased observed frequency ($f_{\\text{obs}} > f$), ruling out options A and B."
        ]
    },
    # Q27
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q27",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": ["property_identification", "classification"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m05",
        "skill_id": "9702_skill_define_longitudinal_wave",
        "accepted_answer": "B",
        "hints": [
            "Recall which wave category (transverse or longitudinal) cannot undergo polarisation.",
            "Polarisation requires oscillations to be perpendicular to the direction of propagation."
        ],
        "walkthrough": [
            "Polarisation is a phenomenon unique to transverse waves, where oscillations occur in a plane perpendicular to the direction of energy transfer.",
            "Sound waves are longitudinal waves in which particle oscillations occur parallel to the direction of wave propagation. Because longitudinal waves have only one oscillation axis along the direction of travel, they cannot be polarised (option B). Radio waves, ultraviolet waves, and X-rays are transverse electromagnetic waves and can all be polarised."
        ]
    },
    # Q28
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q28",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "multi_step_calculation"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_apply_wave_intensity",
        "accepted_answer": "B",
        "hints": [
            "Recall that wave intensity is proportional to the square of amplitude: $I \\propto X^2$.",
            "Power is intensity multiplied by cross-sectional area ($P = I \\times A$). Calculate the factor change."
        ],
        "walkthrough": [
            "The intensity $I$ of a wave is proportional to the square of its amplitude: $I \\propto X^2$. The total power of the beam is given by $P = I \\cdot A \\propto X^2 A$.",
            "When the amplitude increases to $4X$ and the area decreases to $\\frac{A}{3}$, the new power is $P_{\\text{new}} \\propto (4X)^2 \\cdot \\left(\\frac{A}{3}\\right) = 16 X^2 \\cdot \\frac{A}{3} = \\frac{16}{3} (X^2 A) = \\frac{16}{3} P \\approx 5.33 P \\approx 5.3P$ (option B)."
        ]
    },
    # Q29
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q29",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "property_identification"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m01",
        "skill_id": "9702_skill_determine_stationary_wave_spacing",
        "accepted_answer": "D",
        "hints": [
            "In a stationary wave, recall the spacing between successive antinodes (maxima).",
            "Between the 1st maximum and the 5th maximum, there are 4 node-to-node intervals, each of length $\\frac{\\lambda}{2}$."
        ],
        "walkthrough": [
            "In a stationary sound wave, adjacent amplitude maxima (antinodes) are separated by a distance of $\\frac{\\lambda}{2}$.",
            "Moving from the first maximum to the fifth maximum covers $(5 - 1) = 4$ intervals. Thus, the total distance moved is $d = 4 \\times \\left(\\frac{\\lambda}{2}\\right) = 2\\lambda = 2.0\\,\\text{m}$, which gives $\\lambda = \\frac{2.0\\,\\text{m}}{2} = 1.0\\,\\text{m}$ (option D)."
        ]
    },
    # Q30
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q30",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": ["definition"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m03",
        "skill_id": "9702_skill_define_coherence",
        "accepted_answer": "C",
        "hints": [
            "Recall the definition of coherence between two wave sources.",
            "Coherent waves must maintain a constant phase relationship over time."
        ],
        "walkthrough": [
            "By definition, two wave sources are coherent if they emit waves with a constant phase difference (and identical frequency/wavelength). Hence, option C is correct.",
            "Coherent waves do not necessarily have to be in phase (zero phase difference), nor do they require equal amplitudes or opposite directions of travel."
        ]
    },
    # Q31
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q31",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": ["interference_analysis", "property_identification"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m03",
        "skill_id": "9702_skill_apply_double_slit_interference",
        "accepted_answer": "C",
        "hints": [
            "Use the double-slit fringe separation formula $x = \\frac{\\lambda D}{a}$.",
            "Identify what the symbols in the diagram correspond to: $D = q$ and $a = r$."
        ],
        "walkthrough": [
            "The fringe separation on the screen is given by Young's double-slit formula $x = \\frac{\\lambda D}{a} = \\frac{\\lambda q}{r}$, where $q$ is the slit-to-screen distance and $r$ is the slit separation.",
            "To increase the fringe separation $x$, one must increase $\\lambda$, increase $q$, or decrease the slit separation $r$. Therefore, decreasing $r$ (option C) increases fringe separation."
        ]
    },
    # Q32
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q32",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": ["definition", "comparison"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_compare_emf_potential_difference",
        "accepted_answer": "A",
        "hints": [
            "Recall the definitions of electric potential difference and electromotive force per unit charge.",
            "Both p.d. and e.m.f. are defined as energy transferred per unit charge, $V = \\frac{W}{q}$ and $E = \\frac{W}{q}$."
        ],
        "walkthrough": [
            "Potential difference (p.d.) is defined as the energy transferred from electrical energy to other forms per unit charge: $V = \\frac{W}{q}$.",
            "Electromotive force (e.m.f.) is defined as the energy transferred from other forms into electrical energy per unit charge: $E = \\frac{W}{q}$. Both quantities are defined as $\\frac{W}{q}$, making row A correct."
        ]
    },
    # Q33
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q33",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["circuit_analysis", "multi_step_calculation"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_calculate_parallel_resistance",
        "accepted_answer": "C",
        "hints": [
            "Calculate the equivalent resistance of the two parallel resistors ($1.2\\,\\text{k}\\Omega$ and $4.7\\,\\text{k}\\Omega$).",
            "Add the series resistor ($2.2\\,\\text{k}\\Omega$) to the parallel combination resistance."
        ],
        "walkthrough": [
            "The parallel pair of resistors has equivalent resistance $R_p = \\frac{1.2\\,\\text{k}\\Omega \\times 4.7\\,\\text{k}\\Omega}{1.2\\,\\text{k}\\Omega + 4.7\\,\\text{k}\\Omega} = \\frac{5.64}{5.9} \\approx 0.9559\\,\\text{k}\\Omega$.",
            "This parallel combination is in series with the $2.2\\,\\text{k}\\Omega$ resistor, so the total combined resistance between terminals X and Y is $R_{\\text{total}} = 2.2\\,\\text{k}\\Omega + 0.9559\\,\\text{k}\\Omega \\approx 3.16\\,\\text{k}\\Omega \\approx 3.2\\,\\text{k}\\Omega$ (option C)."
        ]
    },
    # Q34
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q34",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": ["direct_calculation"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_calculate_electrical_power",
        "accepted_answer": "B",
        "hints": [
            "Use the power formula relating power $P$, potential difference $V$, and resistance $R$.",
            "Rearrange $P = \\frac{V^2}{R}$ to solve for resistance: $R = \\frac{V^2}{P}$."
        ],
        "walkthrough": [
            "The electrical power dissipated in a resistor is given by $P = \\frac{V^2}{R}$.",
            "Rearranging for resistance gives $R = \\frac{V^2}{P} = \\frac{(4.0\\,\\text{V})^2}{25\\,\\text{W}} = \\frac{16}{25} = 0.64\\,\\Omega$ (option B)."
        ]
    },
    # Q35
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q35",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": ["circuit_analysis", "property_identification"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_analyse_parallel_branch_resistance_change",
        "accepted_answer": "B",
        "hints": [
            "Consider the effect of decreasing the variable resistance on total circuit resistance and terminal potential difference $V = E - I_{\\text{total}}r$.",
            "Determine the current in the fixed resistor branch ($I_{\\text{fixed}} = \\frac{V}{R}$) and deduce the change in current $I$ through the variable resistor."
        ],
        "walkthrough": [
            "Decreasing the variable resistance reduces the combined parallel external resistance $R_{\\text{ext}}$, which decreases total circuit resistance and increases total current $I_{\\text{total}}$ delivered by the cell. As a result, the lost volts ($I_{\\text{total}}r$) increase, causing the terminal potential difference $V = E - I_{\\text{total}}r$ across the parallel branch to decrease.",
            "Because potential difference $V$ decreases, current through the fixed resistor ($I_{\\text{fixed}} = \\frac{V}{R}$) decreases. Since total current $I_{\\text{total}} = I + I_{\\text{fixed}}$ has increased while $I_{\\text{fixed}}$ has decreased, the current $I$ through the variable resistor must increase. Hence, $V$ decreases and $I$ increases (option B)."
        ]
    },
    # Q36
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q36",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["multi_step_calculation", "direct_calculation"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m01",
        "skill_id": "9702_skill_apply_charge_quantisation",
        "accepted_answer": "C",
        "hints": [
            "Find the total electric charge striking the target using $Q = I \\times t$.",
            "Divide by the charge of a single $\\alpha$-particle, which is $+2e = 2 \\times 1.60 \\times 10^{-19}\\,\\text{C}$."
        ],
        "walkthrough": [
            "The total charge transported by the beam in $3.0\\,\\text{s}$ is $Q = I \\times t = 1.5 \\times 10^{-9}\\,\\text{A} \\times 3.0\\,\\text{s} = 4.5 \\times 10^{-9}\\,\\text{C}$.",
            "An $\\alpha$-particle consists of two protons and two neutrons, carrying a net charge of $q_\\alpha = +2e = 2 \\times 1.60 \\times 10^{-19}\\,\\text{C} = 3.20 \\times 10^{-19}\\,\\text{C}$. The average number of $\\alpha$-particles is $N = \\frac{Q}{q_\\alpha} = \\frac{4.5 \\times 10^{-9}\\,\\text{C}}{3.20 \\times 10^{-19}\\,\\text{C}} \\approx 1.406 \\times 10^{10} \\approx 1.4 \\times 10^{10}$ (option C)."
        ]
    },
    # Q37
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q37",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": ["property_identification", "explanation"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m01",
        "skill_id": "9702_skill_define_charge_quantisation",
        "accepted_answer": "C",
        "hints": [
            "Recall that the elementary charge of an electron is an invariant fundamental physical constant.",
            "An applied potential difference alters the electric field and drift velocity, not the intrinsic charge of the electrons."
        ],
        "walkthrough": [
            "The electric charge of a free electron is a fundamental constant of nature with a fixed negative sign and magnitude $e = 1.60 \\times 10^{-19}\\,\\text{C}$.",
            "Applying a potential difference across the wire creates an electric field that causes drift motion of the electron sea, but it has no effect on either the sign or the magnitude of the elementary charge of individual electrons. Thus, option C is correct."
        ]
    },
    # Q38
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q38",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": ["classification", "property_identification"],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m02",
        "skill_id": "9702_skill_recall_quark_charges",
        "accepted_answer": "A",
        "hints": [
            "Recall the charges of the six quark flavours: up-type quarks have charge $+\\frac{2}{3}e$ and down-type quarks have charge $-\\frac{1}{3}e$.",
            "Up-type quarks include up, charm, and top; down-type quarks include down, strange, and bottom."
        ],
        "walkthrough": [
            "The six quark flavours are grouped into two charge categories: up-type quarks (up $u$, charm $c$, top $t$) have charge $+\\frac{2}{3}e$, while down-type quarks (down $d$, strange $s$, bottom $b$) have charge $-\\frac{1}{3}e$.",
            "Therefore, charm ($\\checkmark$) and top ($\\checkmark$) have charge $+\\frac{2}{3}e$, whereas strange ($\\times$) and bottom ($\\times$) have charge $-\\frac{1}{3}e$. This matches row A."
        ]
    },
    # Q39
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q39",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["multi_step_calculation", "property_identification"],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m01",
        "skill_id": "9702_skill_complete_nuclear_equations",
        "accepted_answer": "B",
        "hints": [
            "An isotope of an element must have the same proton number $Z$ as the original nucleus but a different nucleon number $A$.",
            "An $\\alpha$-emission decreases $Z$ by 2, while each $\\beta^-$-emission increases $Z$ by 1."
        ],
        "walkthrough": [
            "An isotope of an element is defined as a nucleus having the same proton number $Z$ but a different nucleon number $A$.",
            "Each $\\alpha$-decay decreases the proton number by 2 ($\\Delta Z = -2$), and each $\\beta^-$-decay increases the proton number by 1 ($\\Delta Z = +1$). To return to the original atomic number $Z$, emitting $1\\,\\alpha$-particle requires $2\\,\\beta^-$-particles ($\\Delta Z = -2 + 1 + 1 = 0$). The net change in nucleon number is $\\Delta A = -4$, producing a valid lighter isotope. The minimum total number of emitted particles is $1 + 2 = 3$ (option B)."
        ]
    },
    # Q40
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_m24_12_q40",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": ["particle_model_application", "property_identification"],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m02",
        "skill_id": "9702_skill_describe_beta_decay_quark_change",
        "accepted_answer": "B",
        "hints": [
            "Write the nuclear decay equation for $^{10}_{\\phantom{0}6}\\text{C} \\to {^{10}_{\\phantom{0}5}\\text{B}}$ to identify whether a proton turns into a neutron or vice versa.",
            "Recall that a proton is $uud$ and a neutron is $udd$. Deduce the single quark flavour transition."
        ],
        "walkthrough": [
            "In the decay $^{10}_{\\phantom{0}6}\\text{C} \\to {^{10}_{\\phantom{0}5}\\text{B}} + \\beta^+ + \\nu_e$, the proton number decreases from 6 to 5 while the nucleon number remains 10. This requires a proton to change into a neutron ($p \\to n + e^+ + \\nu_e$).",
            "A proton has quark composition $uud$ and a neutron has composition $udd$. Thus, in this $\\beta^+$ decay, an up quark transforms into a down quark ($u \\to d$). Row B correctly lists 'proton to neutron' and 'up becomes down'."
        ]
    }
]

def main():
    print(f"Generating {len(RECORDS)} P1 enrichment records...")
    for rec in RECORDS:
        qid = rec["question_id"]
        out_file = OUT_DIR / f"{qid}.enrichment.json"
        out_file.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"  Wrote {out_file.name}")
    print("Done!")

if __name__ == "__main__":
    main()
