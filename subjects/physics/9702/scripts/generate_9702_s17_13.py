#!/usr/bin/env python3
"""
generate_9702_s17_13.py

Generates high-quality canonical enrichment JSON files for Cambridge AS Physics 9702 Paper 1 May/June 2017 Variant 13 (9702_s17_13).
All 40 questions (q01-q40).
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "subjects/physics/9702/enrichment/p1"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

enrichments = [
    # Q01
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q01",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "physical_quantity_estimation",
            "direct_calculation"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m01",
        "skill_id": "9702_skill_estimate_physical_quantities",
        "accepted_answer": "B",
        "hints": [
            "Estimate typical values for the mass of a family car and convert the given speed of $v = 50\\text{ km h}^{-1}$ into standard SI units of $\\text{m s}^{-1}$.",
            "A standard family car has a mass of approximately $m = 1000\\text{ kg}$ to $m = 1500\\text{ kg}$. Calculate kinetic energy using $E_k = \\frac{1}{2}mv^2$ to determine the order of magnitude."
        ],
        "walkthrough": [
            "First, convert the speed to SI base units: $v = \\frac{50\\text{ km}}{1\\text{ h}} = \\frac{50 \\times 10^3\\text{ m}}{3600\\text{ s}} \\approx 13.9\\text{ m s}^{-1}$. A typical family car has a mass $m \\approx 1200\\text{ kg}$ to $m \\approx 1500\\text{ kg}$.",
            "Using the kinetic energy formula: $E_k = \\frac{1}{2} m v^2 \\approx \\frac{1}{2} \\times 1500\\text{ kg} \\times (13.9\\text{ m s}^{-1})^2 \\approx 0.5 \\times 1500 \\times 193 \\approx 1.45 \\times 10^5\\text{ J} \\approx 1.5 \\times 10^5\\text{ J}$ (Option B).",
            "Option A ($1.5 \\times 10^3\\text{ J}$) is on the scale of a moving bicycle or running human. Options C ($1.5 \\times 10^7\\text{ J}$) and D ($1.5 \\times 10^9\\text{ J}$) represent trains or high-speed commercial aircraft."
        ]
    },
    # Q02
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q02",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "vector_diagram_construction",
            "direct_calculation"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m04",
        "skill_id": "9702_skill_add_vectors",
        "accepted_answer": "B",
        "hints": [
            "Recall that vector subtraction $\\vec{X} - \\vec{Y}$ is equivalent to vector addition $\\vec{X} + (-\\vec{Y})$.",
            "Invert the direction of vector $\\vec{Y}$ from downwards to upwards, then use Pythagoras' theorem for magnitude and trigonometry $\\tan\\theta = \\frac{|-Y|}{|X|}$ for the angle relative to $\\vec{X}$."
        ],
        "walkthrough": [
            "Vector $\\vec{X}$ has magnitude $8.0\\text{ N}$ directed horizontally to the right, and vector $\\vec{Y}$ has magnitude $6.0\\text{ N}$ directed vertically downwards. The negative vector $-\\vec{Y}$ has magnitude $6.0\\text{ N}$ directed vertically upwards.",
            "The magnitude of the resultant vector $\\vec{R} = \\vec{X} - \\vec{Y}$ is given by Pythagoras' theorem: $|\\vec{R}| = \\sqrt{X^2 + (-Y)^2} = \\sqrt{8.0^2 + 6.0^2} = \\sqrt{64 + 36} = \\sqrt{100} = 10.0\\text{ N}$.",
            "The direction relative to vector $\\vec{X}$ is calculated using $\\tan\\theta = \\frac{6.0}{8.0} = 0.75$, giving $\\theta = \\arctan(0.75) \\approx 36.9^\\circ \\approx 37^\\circ$ upwards from the direction of $\\vec{X}$ (Option B).",
            "Options C and D incorrectly add the scalar magnitudes ($8.0 + 6.0 = 14.0\\text{ N}$), and Option A gives the downward direction corresponding to $\\vec{X} + \\vec{Y}$ rather than $\\vec{X} - \\vec{Y}$."
        ]
    },
    # Q03
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q03",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "definition",
            "equation_derivation"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m02",
        "skill_id": "9702_skill_derive_si_base_units",
        "accepted_answer": "D",
        "hints": [
            "Relate the volt to basic physical definitions of electric potential difference: $V = \\frac{W}{Q}$ (energy transferred per unit charge) or $P = V I$.",
            "Express the joule ($\\text{J} = \\text{N m} = \\text{kg m}^2\\text{ s}^{-2}$) and the coulomb ($\\text{C} = \\text{A s}$) in terms of SI base units, then take their quotient."
        ],
        "walkthrough": [
            "Electric potential difference is defined as work done per unit charge: $1\\text{ V} = 1\\text{ J C}^{-1}$.",
            "Work done (energy) has base units: $\\text{J} = \\text{N m} = (\\text{kg m s}^{-2})(\\text{m}) = \\text{kg m}^2\\text{ s}^{-2}$. Electric charge has base units: $\\text{C} = \\text{A s}$.",
            "Dividing base units yields: $\\frac{\\text{kg m}^2\\text{ s}^{-2}}{\\text{A s}} = \\text{kg m}^2\\text{ s}^{-3}\\text{ A}^{-1}$ (Option D).",
            "Options A and C omit factors in the negative power of seconds ($\\text{s}^{-1}$ instead of $\\text{s}^{-3}$), and Option B has incorrect powers for meters and seconds."
        ]
    },
    # Q04
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q04",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "definition",
            "comparison"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m03",
        "skill_id": "9702_skill_distinguish_accuracy_precision",
        "accepted_answer": "C",
        "hints": [
            "Recall that accuracy refers to how close a measured value is to the true reference value, while precision refers to the degree of exactness or number of significant figures/decimal places of the measurement.",
            "Compare the deviations $|2.33 - 2.321|$ and $|2.344 - 2.321|$, as well as the resolution (decimal places) of both values."
        ],
        "walkthrough": [
            "The true reference value is $2.321\\text{ V}$. Comparing the closeness of each measurement to the true value: $|2.33\\text{ V} - 2.321\\text{ V}| = 0.009\\text{ V}$, whereas $|2.344\\text{ V} - 2.321\\text{ V}| = 0.023\\text{ V}$. Because $2.33\\text{ V}$ has a smaller difference from the true value, it is more accurate than $2.344\\text{ V}$.",
            "Precision is determined by the smallest division or number of decimal places: $2.344\\text{ V}$ is recorded to 3 decimal places ($0.001\\text{ V}$ resolution), whereas $2.33\\text{ V}$ is recorded to 2 decimal places ($0.01\\text{ V}$ resolution). Thus, $2.33\\text{ V}$ is less precise.",
            "Combining these findings: $2.33\\text{ V}$ is more accurate and less precise than $2.344\\text{ V}$ (Option C)."
        ]
    },
    # Q05
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q05",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_apply_constant_acceleration",
        "accepted_answer": "B",
        "hints": [
            "In the absence of an atmosphere, the trajectory is symmetric. Determine the time taken to reach the maximum height $h = 170\\text{ m}$.",
            "The time to reach maximum height (where $v = 0$) is half the total flight time: $t = \\frac{12.5\\text{ s}}{2} = 6.25\\text{ s}$. Apply $s = ut + \\frac{1}{2}at^2$ or $s = \\frac{1}{2}gt^2$ considering downward fall from the peak."
        ],
        "walkthrough": [
            "Due to symmetric vertical projectile motion without air resistance, the time taken to fall from maximum height ($h = 170\\text{ m}$) back to the ground from rest ($u = 0$) is $t = \\frac{12.5\\text{ s}}{2} = 6.25\\text{ s}$.",
            "Using the kinematic equation for downward motion: $s = ut + \\frac{1}{2} g t^2 = 0 + \\frac{1}{2} g t^2$.",
            "Substitute $s = 170\\text{ m}$ and $t = 6.25\\text{ s}$: $h = \\frac{1}{2} g (6.25)^2 = 19.53125 g \\implies g = \\frac{170}{19.53125} \\approx 8.704\\text{ m s}^{-2} \\approx 8.7\\text{ m s}^{-2}$ (Option B).",
            "Distractor A ($g = 2.2\\text{ m s}^{-2}$) arises from incorrectly using the full flight time of $T = 12.5\\text{ s}$ squared in $s = \\frac{1}{2}gt^2$ without halving the time. Distractors C and D arise from arithmetic errors or doubling/halving factors incorrectly."
        ]
    },
    # Q06
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q06",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "comparison"
        ],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_construct_graphs",
        "accepted_answer": "A",
        "hints": [
            "Recall that velocity is the gradient of the displacement–time graph ($v = \\frac{\\Delta s}{\\Delta t}$).",
            "Calculate the numerical gradient for each linear segment: from $t = 0\\text{ to }2\\text{ s}$, $2\\text{ to }4\\text{ s}$, $4\\text{ to }6\\text{ s}$, and $6\\text{ to }10\\text{ s}$."
        ],
        "walkthrough": [
            "Analyze the gradient $\\frac{\\Delta s}{\\Delta t}$ for each interval on the displacement–time graph:",
            "1. From $t = 0\\text{ s}$ to $t = 2\\text{ s}$: $\\Delta s = 2 - 0 = 2\\text{ m}$, gradient $v = \\frac{2\\text{ m}}{2\\text{ s}} = +1.0\\text{ m s}^{-1}$.\n2. From $t = 2\\text{ s}$ to $t = 4\\text{ s}$: displacement is constant at $2\\text{ m}$, so gradient $v = 0\\text{ m s}^{-1}$.\n3. From $t = 4\\text{ s}$ to $t = 6\\text{ s}$: $\\Delta s = -2 - 2 = -4\\text{ m}$, gradient $v = \\frac{-4\\text{ m}}{2\\text{ s}} = -2.0\\text{ m s}^{-1}$.\n4. From $t = 6\\text{ s}$ to $t = 10\\text{ s}$: $\\Delta s = 2 - (-2) = 4\\text{ m}$, gradient $v = \\frac{4\\text{ m}}{4\\text{ s}} = +1.0\\text{ m s}^{-1}$.",
            "Graph A accurately displays these four constant velocity levels ($+1, 0, -2, +1\\text{ m s}^{-1}$). Graphs B, C, and D have incorrect velocity signs, values, or non-zero velocities during stationary intervals."
        ]
    },
    # Q07
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q07",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": [
            "graph_interpretation",
            "explanation"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m02",
        "skill_id": "9702_skill_analyse_resistive_force_motion",
        "accepted_answer": "D",
        "hints": [
            "Relate the resultant braking force to acceleration using Newton's second law, $F = ma$, and consider the gradient of the speed–time graph, which represents acceleration/deceleration.",
            "As time progresses, the braking force increases linearly from zero to a maximum value at time $t$. How does the rate of decrease of speed (gradient magnitude) change over time?"
        ],
        "walkthrough": [
            "According to Newton's second law ($F = ma$), the deceleration $a = \\frac{F}{m}$ is directly proportional to the resultant braking force. The magnitude of the gradient of the speed–time graph is $|\\text{gradient}| = |a| = \\frac{F}{m}$.",
            "At $t = 0$, the braking force is zero, so the deceleration is zero and the speed–time curve starts with a horizontal tangent (gradient $= 0$). As time increases towards $t$, the braking force increases continuously, so deceleration increases and the speed–time curve becomes increasingly steep downwards.",
            "The car comes to rest at time $t$ with maximum steepness. This concave-downwards curve matches Graph D.",
            "Graph A shows a decreasing deceleration (concave upwards), Graph B shows constant deceleration (straight line), and Graph C shows speed increasing."
        ]
    },
    # Q08
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q08",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "explanation"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_conservation_of_energy",
        "accepted_answer": "C",
        "hints": [
            "Notice that the body is falling at constant (terminal) velocity. What happens to its kinetic energy and acceleration during terminal velocity?",
            "At terminal velocity, kinetic energy is constant ($\\Delta E_k = 0$) and acceleration is zero ($a = 0$). By conservation of energy, all gravitational potential energy lost is converted into thermal energy due to work done against air resistance."
        ],
        "walkthrough": [
            "When falling at terminal velocity, speed is constant, meaning the body's kinetic energy does not change ($\\Delta E_k = 0$) and acceleration is zero. Air resistance equals weight ($F_{\\text{drag}} = mg$).",
            "As the body falls through a height $\\Delta h$, the loss of gravitational potential energy is $\\Delta E_p = mg\\Delta h$. The work done against air resistance is $W_{\\text{drag}} = F_{\\text{drag}} \\Delta h = mg\\Delta h$. Therefore, $W_{\\text{drag}} = \\Delta E_p$.",
            "A graph of work done against air resistance ($y$) against loss of potential energy ($x$) is a straight line through the origin with gradient $1$ (Option C).",
            "Option A is incorrect because acceleration remains zero while air resistance is constant. Option B is incorrect because gain in kinetic energy is zero throughout. Option D is incorrect because velocity is constant, which would give a horizontal line."
        ]
    },
    # Q09
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q09",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_apply_force_momentum_rate",
        "accepted_answer": "D",
        "hints": [
            "Assign directional signs to the velocities before and after collision to calculate the change in linear momentum: $\\Delta p = m(v - u)$.",
            "Use Newton's second law in terms of momentum: average force $F = \\frac{|\\Delta p|}{\\Delta t}$, remembering to convert collision time from milliseconds to seconds ($t = 150\\text{ ms} = 0.150\\text{ s}$)."
        ],
        "walkthrough": [
            "Let the initial direction of motion be positive: $u = +4.0\\text{ m s}^{-1}$. Since the ball rebounds in the opposite direction, its final velocity is $v = -2.8\\text{ m s}^{-1}$.",
            "The change in momentum of the ball is: $\\Delta p = m(v - u) = 2.0\\text{ kg} \\times (-2.8 - 4.0)\\text{ m s}^{-1} = 2.0 \\times (-6.8) = -13.6\\text{ N s}$.",
            "The average force exerted during the collision is: $F = \\frac{|\\Delta p|}{\\Delta t} = \\frac{13.6\\text{ N s}}{150 \\times 10^{-3}\\text{ s}} = \\frac{13.6}{0.150} \\approx 90.67\\text{ N} \\approx 91\\text{ N}$ (Option D).",
            "Distractor A ($F = 16\\text{ N}$) results from subtracting the speeds ($4.0 - 2.8 = 1.2\\text{ m s}^{-1}$) instead of accounting for velocity reversal: $\\frac{2.0 \\times 1.2}{0.15} = 16\\text{ N}$."
        ]
    },
    # Q10
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q10",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_apply_newtons_second_law",
        "accepted_answer": "A",
        "hints": [
            "Convert the mass of the puck to kilograms: $m = 150\\text{ g} = 0.150\\text{ kg}$.",
            "Use either work-energy balance ($F s = \\frac{1}{2}mv^2$) or kinematic equations ($v^2 = u^2 + 2as$) combined with $F = ma$ to solve for the frictional force."
        ],
        "walkthrough": [
            "Method 1 (Work-Energy): The work done against friction equals the initial kinetic energy of the puck: $W = F \\times s = \\frac{1}{2} m u^2$.",
            "Substitute the values: $F \\times 30\\text{ m} = \\frac{1}{2} \\times 0.150\\text{ kg} \\times (2.0\\text{ m s}^{-1})^2 = 0.5 \\times 0.150 \\times 4.0 = 0.30\\text{ J}$.",
            "Solving for friction: $F = \\frac{0.30\\text{ J}}{30\\text{ m}} = 0.010\\text{ N}$ (Option A).",
            "Method 2 (Kinematics): Using $v^2 = u^2 + 2as \\implies 0 = (2.0)^2 + 2a(30) \\implies a = -\\frac{4.0}{60} = -\\frac{1}{15}\\text{ m s}^{-2}$. Then $F = m|a| = 0.150 \\times \\frac{1}{15} = 0.010\\text{ N}$.",
            "Distractor B ($0.020\\text{ N}$) forgets the factor of $\\frac{1}{2}$ in kinetic energy, and Distractor D ($0.44\\text{ N}$) leaves mass in grams."
        ]
    },
    # Q11
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q11",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_calculate_resultant_moment",
        "accepted_answer": "D",
        "hints": [
            "Identify the position of the centre of gravity of the uniform beam relative to the pivot P and compute the weight of each component ($W = mg$ using $g = 9.81\\text{ m s}^{-2}$).",
            "Sum clockwise and anticlockwise moments about the pivot P: the beam's centre of mass is at $0.30\\text{ m}$ from the left end ($0.10\\text{ m}$ to the right of P)."
        ],
        "walkthrough": [
            "The uniform beam has length $0.60\\text{ m}$, so its centre of mass is $0.30\\text{ m}$ from each end. Since pivot P is $0.20\\text{ m}$ from the left end, the centre of mass is $0.30 - 0.20 = 0.10\\text{ m}$ to the right of P.",
            "Weight of beam: $W_{\\text{beam}} = 1.4\\text{ kg} \\times 9.81\\text{ m s}^{-2} = 13.734\\text{ N}$ acting $0.10\\text{ m}$ to the right of P.",
            "Weight of $3.0\\text{ kg}$ load: $W_1 = 3.0 \\times 9.81 = 29.43\\text{ N}$ acting $0.35\\text{ m}$ to the right of P.",
            "Weight of $6.0\\text{ kg}$ load: $W_2 = 6.0 \\times 9.81 = 58.86\\text{ N}$ acting $0.15\\text{ m}$ to the left of P.",
            "Total clockwise moment about P: $\\Sigma M_{\\text{CW}} = (13.734 \\times 0.10) + (29.43 \\times 0.35) = 1.3734 + 10.3005 = 11.6739\\text{ N m}$.",
            "Total anticlockwise moment about P: $\\Sigma M_{\\text{ACW}} = 58.86 \\times 0.15 = 8.829\\text{ N m}$.",
            "The net unbalanced moment is: $\\tau_{\\text{net}} = 11.6739 - 8.829 = 2.8449\\text{ N m} \\approx 2.8\\text{ N m}$ clockwise. To maintain equilibrium, an equal and opposite restoring torque of $2.8\\text{ N m}$ must be applied (Option D)."
        ]
    },
    # Q12
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q12",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "force_diagram_construction",
            "comparison"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m02",
        "skill_id": "9702_skill_identify_fluid_upthrust",
        "accepted_answer": "A",
        "hints": [
            "Determine the directions of each of the three forces: upthrust $U$, weight $W$, and viscous drag $D$ for an air bubble moving upwards.",
            "Because the bubble rises at constant speed, the resultant force must be zero: equate upward and downward forces ($U = W + D$)."
        ],
        "walkthrough": [
            "Upthrust $U$ acts vertically upwards due to hydrostatic pressure difference. Weight $W$ acts vertically downwards due to gravity.",
            "Because the bubble is rising upwards through the liquid, the viscous drag force $D$ opposes the motion and acts vertically downwards.",
            "At constant velocity, the acceleration is zero, so the forces are in equilibrium: $U = W + D$. Thus, the upward arrow $U$ must have a magnitude equal to the sum of the magnitudes of the downward arrows $W$ and $D$.",
            "Diagram A correctly illustrates $U$ pointing upwards, both $D$ and $W$ pointing downwards, with the vector length of $U$ equaling the combined length of $D$ and $W$.",
            "Diagrams B, C, and D incorrectly orient the drag force upwards or depict unbalanced magnitudes."
        ]
    },
    # Q13
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q13",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "explanation",
            "comparison"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m03",
        "skill_id": "9702_skill_apply_hydrostatic_pressure",
        "accepted_answer": "A",
        "hints": [
            "Recall that hydrostatic pressure in a fluid increases with depth according to $p = \\rho g h$.",
            "Compare the depth of the top of the sphere (where downward force $P$ acts) with the bottom (where upward force $R$ acts), and compare the depths of opposing sides (forces $Q$ and $S$)."
        ],
        "walkthrough": [
            "Hydrostatic pressure in an incompressible fluid is given by $p = \\rho g h$, where $h$ is the depth below the surface. The pressure force acting perpendicular to an area element is $F = p A$.",
            "The top of the sphere (force $P$) is at a shallower depth than the bottom of the sphere (force $R$). Therefore, the downward pressure at the top is less than the upward pressure at the bottom, so $P < R$. (This pressure difference gives rise to net upthrust).",
            "The horizontal points on the left (force $Q$) and right (force $S$) are at identical horizontal depths, so the horizontal pressures are equal, giving $S = Q$.",
            "Therefore, $P < R$ and $S = Q$ (Option A)."
        ]
    },
    # Q14
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q14",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "definition",
            "explanation"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_define_work_done",
        "accepted_answer": "A",
        "hints": [
            "Consider the definition of work done by a force: $W = F s \\cos\\theta$, and analyze whether the force and displacement are in the same or opposing directions.",
            "When a diver falls downwards, the gravitational force acts downwards in the same direction as displacement, so work is done by gravity on the diver, not by the diver against the field."
        ],
        "walkthrough": [
            "In statement A, as the girl falls from the diving board towards the water, displacement and gravitational force are in the same downward direction. The gravitational field does positive work on the girl. The girl does not do work against the gravitational field during downward free fall. Hence, row A is incorrect and is the required answer.",
            "In row B, pushing a car forward against opposing resistive forces means the man does work against friction (correct).",
            "In row C, an electric field exerts a force on an electron accelerating it towards a positive plate, doing work on the electron (correct).",
            "In row D, expanding gas exerts pressure on a piston against external atmospheric pressure, doing work on the atmosphere (correct)."
        ]
    },
    # Q15
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q15",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "definition",
            "equation_recall"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_apply_efficiency",
        "accepted_answer": "D",
        "hints": [
            "Recall the general physics definition of efficiency in terms of power transfer.",
            "Efficiency is the ratio of useful output power to total input power: $\\eta = \\frac{P_{\\text{useful}}}{P_{\\text{total}}}$."
        ],
        "walkthrough": [
            "The efficiency $\\eta$ of any energy conversion device is defined as the useful output power divided by the total input power: $\\eta = \\frac{P_O}{P_I}$.",
            "Here, $P_I$ is the input power, $P_O$ is the useful output power delivered to the generator, and $P_L$ is the power loss ($P_I = P_O + P_L$).",
            "Therefore, the efficiency is $\\frac{P_O}{P_I}$ (Option D).",
            "Option A ($\\frac{P_L}{P_I}$) is the fractional power loss, Option B is the inverse of efficiency, and Option C is an invalid ratio."
        ]
    },
    # Q16
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q16",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "equation_derivation",
            "comparison"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m02",
        "skill_id": "9702_skill_derive_kinetic_energy_from_work_and_motion",
        "accepted_answer": "C",
        "hints": [
            "Relate the work done by the constant force over the fixed distance $s$ to the kinetic energy gained by the block from rest: $W = F s = \\frac{1}{2}mv^2$.",
            "Since $F$ and $s$ are constant, $W$ is constant. Express $v$ in terms of $m$ and determine the proportionality."
        ],
        "walkthrough": [
            "The constant force $F$ acts over a fixed distance $s$ on a frictionless surface, doing work $W = F s$, which is constant.",
            "From the work-energy theorem, this work is entirely converted into kinetic energy: $F s = \\frac{1}{2} m v^2$.",
            "Rearranging for final speed $v$: $v^2 = \\frac{2 F s}{m} \\implies v = \\sqrt{\\frac{2 F s}{m}} = \\sqrt{2 F s} \\times \\frac{1}{\\sqrt{m}}$.",
            "Since $F$ and $s$ are constant, $v \\propto \\frac{1}{\\sqrt{m}}$ (Option C).",
            "Option A ($v \\propto m$), Option B ($v \\propto \\sqrt{m}$), and Option D ($v \\propto \\frac{1}{m}$) represent incorrect powers of mass."
        ]
    },
    # Q17
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q17",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_apply_mechanical_power",
        "accepted_answer": "B",
        "hints": [
            "Recall that useful power is the rate at which gravitational potential energy is gained: $P = \\frac{\\Delta E_p}{\\Delta t} = \\frac{m g \\Delta h}{\\Delta t} = m g v$.",
            "Convert the average upward speed to SI units ($v = 50\\text{ cm s}^{-1} = 0.50\\text{ m s}^{-1}$) and use $g = 9.81\\text{ m s}^{-2}$."
        ],
        "walkthrough": [
            "The useful work done by the man is lifting his own body against gravity, gaining potential energy at a rate $P = m g v$.",
            "Substitute $m = 80\\text{ kg}$, $g = 9.81\\text{ m s}^{-2}$, and $v = 0.50\\text{ m s}^{-1}$: $P = 80\\text{ kg} \\times 9.81\\text{ m s}^{-2} \\times 0.50\\text{ m s}^{-1} = 392.4\\text{ W}$.",
            "Expressed in kilowatts: $P = 0.3924\\text{ kW} \\approx 0.39\\text{ kW}$ (Option B).",
            "Distractor A ($P = 40\\text{ W}$) results from using $m \\times v = 80 \\times 0.5 = 40$ without multiplying by $g$. Distractor C ($4.0\\text{ kW}$) and D ($P = 39\\text{ kW}$) arise from power-of-ten unit conversion errors."
        ]
    },
    # Q18
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q18",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "comparison",
            "classification"
        ],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m01",
        "skill_id": "9702_skill_apply_young_modulus",
        "accepted_answer": "D",
        "hints": [
            "Recall the definition of Young modulus: $E = \\frac{\\text{stress}}{\\text{strain}} = \\frac{F/A}{e/L} = \\frac{F L}{A e}$.",
            "Identify which parameters are identical for both wires ($E, A, e$) and which are different ($L, F$). Check the expressions $E$, $\\frac{e}{L}$, $\\frac{F L}{A e}$, and $\\frac{F}{A}$."
        ],
        "walkthrough": [
            "Let us evaluate the quantities in the table:\n1. Young modulus $E$: Stated as the same for both wires (same).\n2. Strain $\\varepsilon = \\frac{e}{L}$: Since extension $e$ is identical but original lengths $L$ are different, the strain $\\frac{e}{L}$ is different for the two wires (different).\n3. Expression $\\frac{F L}{A e}$: By definition, $\\frac{F L}{A e} = E$. Because $E$ is identical, this quantity must be the same for both wires (same).\n4. Stress $\\sigma = \\frac{F}{A}$: Since $\\sigma = E \\times \\varepsilon = E \\frac{e}{L}$, and $\\frac{e}{L}$ differs between the wires while $E$ is identical, tensile stress is different.",
            "Matching the rows in the table: $E$ is same, $\\frac{e}{L}$ is different, $\\frac{F L}{A e}$ is same (Option D)."
        ]
    },
    # Q19
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q19",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "comparison"
        ],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m02",
        "skill_id": "9702_skill_apply_elastic_potential_energy",
        "accepted_answer": "B",
        "hints": [
            "Calculate the spring constant $k = \\frac{F}{x}$ for spring X and spring Y from their respective linear force–extension graphs.",
            "Use the elastic strain energy formula $E_p = \\frac{1}{2} k x^2$ for the case of equal extension, comparing the ratio $\\frac{E_Y}{E_X}$."
        ],
        "walkthrough": [
            "From the graph for spring X: at extension $x = 10\\text{ cm} = 0.10\\text{ m}$, force $F = 20\\text{ N}$, so spring constant $k_X = \\frac{20\\text{ N}}{0.10\\text{ m}} = 200\\text{ N m}^{-1}$ (or $k_X = 2.0\\text{ N cm}^{-1}$).",
            "From the graph for spring Y: at extension $x = 5\\text{ cm} = 0.05\\text{ m}$, force $F = 80\\text{ N}$, so spring constant $k_Y = \\frac{80\\text{ N}}{0.05\\text{ m}} = 1600\\text{ N m}^{-1}$ (or $k_Y = 16.0\\text{ N cm}^{-1}$).",
            "The ratio of the spring constants is $\\frac{k_Y}{k_X} = \\frac{1600}{200} = 8$.",
            "For the same extension $x$: $E_X = \\frac{1}{2} k_X x^2$ and $E_Y = \\frac{1}{2} k_Y x^2$, so $\\frac{E_Y}{E_X} = \\frac{k_Y}{k_X} = 8$. Thus, the energy stored in Y is 8 times the energy stored in X (Option B).",
            "For the same force $F$, energy is $E = \\frac{F^2}{2k}$, which would make $E_Y = \\frac{1}{8} E_X$, eliminating options C and D."
        ]
    },
    # Q20
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q20",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": [
            "graph_interpretation",
            "direct_calculation"
        ],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m02",
        "skill_id": "9702_skill_estimate_work_from_force_extension_graph",
        "accepted_answer": "A",
        "hints": [
            "Recall that the work done to stretch and break the wire equals the total area under the force–extension graph up to the breaking point.",
            "Divide the area into a triangular/trapezoidal elastic region and count the grid squares or approximate the curved plastic region, ensuring extension is converted from millimetres to metres ($1\\text{ mm} = 10^{-3}\\text{ m}$)."
        ],
        "walkthrough": [
            "Work done is represented by the area under the force–extension graph: $W = \\int F\\, dx$.",
            "From the graph: the linear elastic region extends to roughly $x = 7.0\\text{ mm}$ at $F = 200\\text{ N}$, having triangular area $A_1 = \\frac{1}{2} \\times 200\\text{ N} \\times (7.0 \\times 10^{-3}\\text{ m}) = 0.70\\text{ J}$.",
            "The plastic region from $x = 7.0\\text{ mm}$ to the breaking point at $x = 13.0\\text{ mm}$ forms a curved region with average force approximately $F_{\\text{avg}} \\approx 230\\text{ N}$: $A_2 \\approx 230\\text{ N} \\times (6.0 \\times 10^{-3}\\text{ m}) = 1.38\\text{ J}$.",
            "Total area / work done: $W = A_1 + A_2 \\approx 0.70 + 1.38 = 2.08\\text{ J} \\approx 2.1\\text{ J}$ (Option A).",
            "Options B ($2.3\\text{ J}$), C ($2.4\\text{ J}$), and D ($2.5\\text{ J}$) overestimate the area under the curve by treating the entire region as a rectangle of maximum force."
        ]
    },
    # Q21
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q21",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "property_identification",
            "explanation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m04",
        "skill_id": "9702_skill_apply_wave_speed",
        "accepted_answer": "B",
        "hints": [
            "Recall that all electromagnetic waves travel at the same constant speed in a vacuum: $c = 3.00 \\times 10^8\\text{ m s}^{-1}$.",
            "Use the wave speed equation $c = f \\lambda$ to determine the relationship between frequency $f$ and wavelength $\\lambda$ when $c$ is constant."
        ],
        "walkthrough": [
            "In a vacuum, all electromagnetic waves travel at a constant speed $c = 3.00 \\times 10^8\\text{ m s}^{-1}$, independent of wavelength or frequency.",
            "From the wave equation $c = f \\lambda$, rearranging gives $f = \\frac{c}{\\lambda}$, which shows that frequency $f$ is inversely proportional to wavelength $\\lambda$ ($f \\propto \\frac{1}{\\lambda}$) (Option B).",
            "Option A is incorrect because wave speed is a property of the medium (vacuum) and is independent of amplitude. Option C is incorrect because intensity is proportional to the square of amplitude ($I \\propto A^2$). Option D is incorrect because speed in vacuum is constant, not proportional to wavelength."
        ]
    },
    # Q22
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q22",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": [
            "graph_interpretation",
            "explanation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m02",
        "skill_id": "9702_skill_analyse_wave_particle_motion",
        "accepted_answer": "A",
        "hints": [
            "Consider a transverse wave moving to the right. Sketch the wave profile at a slightly later time $t + \\Delta t$ by shifting the whole curve slightly to the right.",
            "Determine which position has a particle moving upwards from its current position towards the new position with maximum rate of change."
        ],
        "walkthrough": [
            "For a progressive transverse wave travelling in the $+x$ direction, the displacement is given by $y(x,t) = y_0 \\sin(\\omega t - kx)$. The particle velocity is $v_y = \\frac{\\partial y}{\\partial t} = -v_{\\text{wave}} \\frac{\\partial y}{\\partial x}$.",
            "Maximum upwards particle velocity occurs where displacement is zero ($y = 0$) and the spatial gradient $\\frac{\\partial y}{\\partial x}$ is maximum negative (steepest downward slope).",
            "At $x = 0.5\\text{ m}$, the wave profile passes through $y = 0$ with a negative slope. Shifting the wave profile slightly to the right moves the particle at $x = 0.5\\text{ m}$ upwards into a positive displacement, meaning its velocity is vertically upwards and at a maximum magnitude (Option A).",
            "At $x = 1.0\\text{ m}$ (trough) and $x = 2.0\\text{ m}$ (crest), the particles are at instantaneous rest ($v_y = 0$). At $x = 1.5\\text{ m}$, the slope is positive, meaning the particle has maximum downward velocity."
        ]
    },
    # Q23
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q23",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "direct_calculation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_interpret_oscilloscope_traces",
        "accepted_answer": "C",
        "hints": [
            "Determine the peak amplitude from the centre line to the crest in centimetres, then multiply by the Y-gain ($2.0\\text{ V cm}^{-1}$).",
            "Measure the horizontal length of one complete wave cycle on the screen, multiply by the time-base setting ($2.5\\text{ ms cm}^{-1}$) to find period $T$, and calculate frequency $f = \\frac{1}{T}$."
        ],
        "walkthrough": [
            "Amplitude measurement: The peak displacement from the central equilibrium axis is $2.0\\text{ cm}$. Using the Y-gain of $2.0\\text{ V cm}^{-1}$: $\\text{Amplitude} = 2.0\\text{ cm} \\times 2.0\\text{ V cm}^{-1} = 4.0\\text{ V}$.",
            "Period measurement: One complete cycle occupies $1.5\\text{ cm}$ horizontally on the graticule. With a time-base setting of $2.5\\text{ ms cm}^{-1}$: $T = 1.5\\text{ cm} \\times 2.5\\text{ ms cm}^{-1} = 3.75\\text{ ms} = 3.75 \\times 10^{-3}\\text{ s}$.",
            "Frequency calculation: $f = \\frac{1}{T} = \\frac{1}{3.75 \\times 10^{-3}\\text{ s}} \\approx 266.7\\text{ Hz} \\approx 267\\text{ Hz}$.",
            "Thus, frequency is $f = 267\\text{ Hz}$ and amplitude is $4.0\\text{ V}$ (Option C).",
            "Options A and B confuse the period $T = 0.00375\\text{ s}$ with the frequency, and Option D uses the peak-to-peak voltage ($8.0\\text{ V}$) rather than amplitude."
        ]
    },
    # Q24
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q24",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m03",
        "skill_id": "9702_skill_apply_doppler_effect",
        "accepted_answer": "D",
        "hints": [
            "Recall the Doppler formula for a source moving towards a stationary observer: $f_o = f_s \\left(\\frac{v}{v - v_s}\\right)$.",
            "Substitute $f_s = 250\\text{ Hz}$, speed of sound $v = 340\\text{ m s}^{-1}$, and train speed $v_s = 80\\text{ m s}^{-1}$."
        ],
        "walkthrough": [
            "As the sound source approaches a stationary observer, the observed wavelength is compressed, leading to an increased observed frequency given by the Doppler equation: $f_o = f_s \\left(\\frac{v}{v - v_s}\\right)$.",
            "Substitute the given parameters: $f_o = 250\\text{ Hz} \\times \\left(\\frac{340\\text{ m s}^{-1}}{340\\text{ m s}^{-1} - 80\\text{ m s}^{-1}}\\right) = 250 \\times \\frac{340}{260} = 250 \\times 1.3077 \\approx 326.9\\text{ Hz} \\approx 330\\text{ Hz}$ (Option D).",
            "Distractor B ($f_o \\approx 200\\text{ Hz}$) incorrectly uses the formula for a receding source: $f_o = 250 \\times \\frac{340}{340 + 80} = 202\\text{ Hz}$. Distractor A and C result from arithmetic errors."
        ]
    },
    # Q25
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q25",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "classification",
            "property_identification"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m04",
        "skill_id": "9702_skill_identify_electromagnetic_spectrum_region",
        "accepted_answer": "D",
        "hints": [
            "Recall the order of the electromagnetic spectrum by increasing frequency: radio $\\rightarrow$ microwaves $\\rightarrow$ infrared $\\rightarrow$ visible $\\rightarrow$ ultraviolet $\\rightarrow$ X-rays $\\rightarrow$ gamma rays.",
            "Recall representative frequencies in Hz: microwaves $\\approx 10^{10}\\text{ Hz}$, infrared $\\approx 10^{14}\\text{ Hz}$, ultraviolet $\\approx 10^{15}\\text{ Hz}$, X-rays $\\approx 10^{18}\\text{ Hz}$."
        ],
        "walkthrough": [
            "In the electromagnetic spectrum, radiations arranged in order of increasing frequency are: microwaves ($f \\sim 10^9\\text{ to }10^{11}\\text{ Hz}$) $\\rightarrow$ infrared ($f \\sim 10^{11}\\text{ to }10^{14}\\text{ Hz}$) $\\rightarrow$ ultraviolet ($f \\sim 10^{15}\\text{ to }10^{16}\\text{ Hz}$) $\\rightarrow$ X-rays ($f \\sim 10^{17}\\text{ to }10^{20}\\text{ Hz}$).",
            "Evaluating Row D:\n- X-rays: $f \\sim 10^{18}\\text{ Hz}$ (typical hard/soft X-ray)\n- Ultraviolet: $f \\sim 10^{15}\\text{ Hz}$ (typical UV)\n- Microwaves: $f \\sim 10^{10}\\text{ Hz}$ (typical radar/microwave)\n- Infra-red: $f \\sim 10^{14}\\text{ Hz}$ (typical near IR).",
            "This correctly matches all four radiation bands (Option D). Rows A, B, and C scramble the frequency bands."
        ]
    },
    # Q26
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q26",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "property_identification",
            "direct_calculation"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m01",
        "skill_id": "9702_skill_explain_stationary_waves",
        "accepted_answer": "A",
        "hints": [
            "For an air column in a pipe open at both ends, displacement antinodes must exist at both open ends.",
            "The resonant condition for an open-open pipe of length $L = 100\\text{ cm}$ is $L = n \\frac{\\lambda}{2}$, meaning allowed wavelengths are $\\lambda = \\frac{2L}{n} = \\frac{200\\text{ cm}}{n}$ for integer $n = 1, 2, 3, 4, \\dots$."
        ],
        "walkthrough": [
            "In an acoustic pipe open at both ends, displacement antinodes form at both open ends. The standing wave condition is that the length $L$ accommodates an integer number of half-wavelengths: $L = n \\frac{\\lambda}{2} \\implies \\lambda = \\frac{2L}{n}$, where $n \\in \\{1, 2, 3, \\dots\\}$.",
            "With $L = 100\\text{ cm}$, the possible resonant wavelengths are:\n- $n = 1$: $\\lambda = \\frac{200}{1} = 200\\text{ cm}$\n- $n = 2$: $\\lambda = \\frac{200}{2} = 100\\text{ cm}$\n- $n = 3$: $\\lambda = \\frac{200}{3} \\approx 66.7\\text{ cm}$\n- $n = 4$: $\\lambda = \\frac{200}{4} = 50\\text{ cm}$.",
            "Among the given options (50 cm, 75 cm, 150 cm, 300 cm), only $\\lambda = 50\\text{ cm}$ corresponds to an allowed harmonic mode ($n = 4$) (Option A).",
            "Values of 75 cm, 150 cm, and 300 cm do not satisfy the boundary conditions for an open-open tube."
        ]
    },
    # Q27
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q27",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "comparison",
            "interference_analysis"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m04",
        "skill_id": "9702_skill_apply_diffraction_grating",
        "accepted_answer": "B",
        "hints": [
            "Recall the diffraction grating equation: $d \\sin\\theta = n \\lambda$, where $d$ is the slit spacing ($d = \\frac{1}{N}$, where $N$ is lines per millimetre).",
            "Determine how doubling $N$ affects $d$, the angular separation between orders ($\\theta_2 - \\theta_1$), and the maximum possible order $n_{\\max} \\le \\frac{d}{\\lambda}$."
        ],
        "walkthrough": [
            "Replacing the grating with one having twice as many lines per millimetre halves the line spacing $d$ ($d' = \\frac{d}{2}$).",
            "1. Angular separation: From $d \\sin\\theta = n \\lambda \\implies \\sin\\theta = \\frac{n \\lambda}{d}$. As $d$ decreases, $\\sin\\theta$ increases for every order $n$, spreading the diffracted beams wider. Consequently, the angle between the first and second orders ($\\theta_2 - \\theta_1$) increases.",
            "2. Number of visible orders: The maximum observable order is given by $n_{\\max} < \\frac{d}{\\lambda}$ (since $\\sin\\theta \\le 1$ for angles up to $\\theta = 90^\\circ$). When $d$ is halved, $n_{\\max}$ is halved, so fewer orders of diffraction fit within the observable range.",
            "Thus, the number of orders visible decreases and the angle between first and second orders increases (Option B)."
        ]
    },
    # Q28
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q28",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "interference_analysis",
            "equation_recall"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m03",
        "skill_id": "9702_skill_apply_double_slit_interference",
        "accepted_answer": "C",
        "hints": [
            "Recall the condition for destructive interference (dark fringes) in a two-slit interference pattern in terms of path difference $S_2P - S_1P$.",
            "Dark fringes occur at half-wavelength path differences: for the $1^{\\text{st}}$ dark fringe ($n = 1$), path difference is $\\frac{1}{2}\\lambda$; for the $2^{\\text{nd}}$ dark fringe ($n = 2$), path difference is $\\frac{3}{2}\\lambda$."
        ],
        "walkthrough": [
            "In Young's double-slit experiment, destructive interference occurs when waves from $S_1$ and $S_2$ arrive in antiphase (phase difference of $\\pi$ radians), corresponding to a path difference of an odd number of half-wavelengths.",
            "The path difference for dark fringes is given by: $S_2P - S_1P = \\left(n - \\frac{1}{2}\\right)\\lambda$, where $n = 1, 2, 3, \\dots$.\n- For the $1^{\\text{st}}$ dark fringe ($n = 1$): $S_2P - S_1P = \\frac{1}{2}\\lambda$.\n- For the $2^{\\text{nd}}$ dark fringe ($n = 2$): $S_2P - S_1P = \\frac{3}{2}\\lambda$.",
            "This general formula holds for all positive integers $n$, matching Option C.",
            "Option B ($S_2P - S_1P = n\\lambda$) gives the condition for bright fringes (constructive interference). Option D would give $\\frac{3}{2}\\lambda$ for $n=1$, skipping the first dark fringe."
        ]
    },
    # Q29
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q29",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "property_identification",
            "explanation"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m01",
        "skill_id": "9702_skill_analyse_electric_force",
        "accepted_answer": "D",
        "hints": [
            "Determine the direction of the electric field $\\vec{E}$ at point X due to the positive and negative charges of the dipole.",
            "Recall that the electric force on a charged particle is $\\vec{F} = q \\vec{E}$. Consider the sign of the charge on an electron ($q = -e$)."
        ],
        "walkthrough": [
            "The electric field lines of a dipole point away from the positive charge ($+$) and towards the negative charge ($-$). At point X (above the midpoint of the dipole), the field line is directed horizontally to the right (towards the negative charge).",
            "The electric force acting on a particle with charge $q$ in an electric field $\\vec{E}$ is $\\vec{F} = q \\vec{E}$.",
            "Because an electron has a negative charge ($q = -1.60 \\times 10^{-19}\\text{ C}$), the force on the electron acts in the direction opposite to the electric field $\\vec{E}$.",
            "Since $\\vec{E}$ points to the right, the force $\\vec{F}$ on the electron acts horizontally to the left, which is direction D (Option D).",
            "Directions A, B, and C represent incorrect orientations or the force on a positive test charge."
        ]
    },
    # Q30
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q30",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "property_identification",
            "classification"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m01",
        "skill_id": "9702_skill_describe_uniform_electric_field_lines",
        "accepted_answer": "D",
        "hints": [
            "Recall the definition and graphical representation of a uniform electric field.",
            "In a uniform field, the electric field strength is constant in magnitude and direction at all points."
        ],
        "walkthrough": [
            "A uniform electric field is defined as an electric field whose magnitude and direction are constant everywhere in the region.",
            "Graphically, a uniform field is represented by straight, parallel, and equally spaced field lines (Option D).",
            "Statement A is incorrect because the force $F = qE$ depends on the particle's charge $q$. Statement B is incorrect because acceleration $a = \\frac{qE}{m}$ depends on the charge-to-mass ratio and velocity depends on initial conditions. Statement C is incorrect because field lines are directed away from positive charges towards negative charges."
        ]
    },
    # Q31
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q31",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m01",
        "skill_id": "9702_skill_calculate_charge_from_current",
        "accepted_answer": "B",
        "hints": [
            "Calculate the transit time $t$ for a single electron to travel the distance $d = 30\\text{ cm} = 0.30\\text{ m}$ at speed $v = 1.5 \\times 10^6\\text{ m s}^{-1}$.",
            "Since exactly one electron is between the plates at any instant, one electron of charge $e = 1.60 \\times 10^{-19}\\text{ C}$ transfers across every time interval $t$. Use $I = \\frac{Q}{t}$."
        ],
        "walkthrough": [
            "The time taken for one electron to travel across the $0.30\\text{ m}$ gap at constant speed $v = 1.5 \\times 10^6\\text{ m s}^{-1}$ is: $t = \\frac{d}{v} = \\frac{0.30\\text{ m}}{1.5 \\times 10^6\\text{ m s}^{-1}} = 2.0 \\times 10^{-7}\\text{ s}$.",
            "Because there is always exactly one electron in flight between the plates, an electric charge equal to the elementary charge $e = 1.60 \\times 10^{-19}\\text{ C}$ arrives at the second plate every $2.0 \\times 10^{-7}\\text{ s}$.",
            "The resulting electric current is: $I = \\frac{Q}{t} = \\frac{1.60 \\times 10^{-19}\\text{ C}}{2.0 \\times 10^{-7}\\text{ s}} = 8.0 \\times 10^{-13}\\text{ A}$ (Option B).",
            "Distractor A results from incorrect powers of ten, Distractor C uses half the transit time, and Distractor D is the transit time itself in seconds."
        ]
    },
    # Q32
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q32",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "circuit_analysis",
            "direct_calculation"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_calculate_electrical_power",
        "accepted_answer": "B",
        "hints": [
            "Calculate the total potential drop across the connecting cables using $V_{\\text{cable}} = I R_{\\text{cable}}$, where $R_{\\text{cable}} = 2\\,\\Omega$ ($1\\,\\Omega$ each).",
            "Subtract the cable voltage drop from the generator output ($V_{\\text{gen}} = 240\\text{ V}$) to find the p.d. $V$ across the floodlights, then calculate power $P = V I$ delivered to the floodlights."
        ],
        "walkthrough": [
            "The circuit current is $I = 10\\text{ A}$ and the total resistance of the supply cables is $R_{\\text{cables}} = 1\\,\\Omega + 1\\,\\Omega = 2\\,\\Omega$.",
            "The potential drop across the cables is: $V_{\\text{drop}} = I R_{\\text{cables}} = 10\\text{ A} \\times 2\\,\\Omega = 20\\text{ V}$.",
            "The terminal p.d. across the floodlights is: $V = V_{\\text{gen}} - V_{\\text{drop}} = 240\\text{ V} - 20\\text{ V} = 220\\text{ V}$.",
            "The power delivered to the floodlights is: $P = V \\times I = 220\\text{ V} \\times 10\\text{ A} = 2200\\text{ W}$ (Option B).",
            "Option A incorrectly uses an estimated power of $P = 2000\\text{ W}$, and Options C and D calculate drops using only one single $1\\,\\Omega$ cable lead ($V = 230\\text{ V}$)."
        ]
    },
    # Q33
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q33",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "comparison"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m03",
        "skill_id": "9702_skill_apply_resistivity",
        "accepted_answer": "C",
        "hints": [
            "Recall the resistivity formula for electrical resistance: $R = \\rho \\frac{L}{A}$.",
            "Express length $L$ and cross-sectional area $A$ in terms of side length $a$ for the original cube, and in terms of $3a$ for the enlarged cube."
        ],
        "walkthrough": [
            "For a solid cube of side length $a$, the length of the conduction path between opposite faces is $L = a$ and the cross-sectional area is $A = a^2$. Its resistance is: $R = \\rho \\frac{L}{A} = \\rho \\frac{a}{a^2} = \\frac{\\rho}{a}$.",
            "For a scaled cube of side length $3a$ made of the same metal, the length is $L' = 3a$ and the cross-sectional area is $A' = (3a)^2 = 9a^2$.",
            "Its new resistance between opposite faces is: $R' = \\rho \\frac{L'}{A'} = \\rho \\frac{3a}{9a^2} = \\frac{\\rho}{3a} = \\frac{1}{3} \\left(\\frac{\\rho}{a}\\right) = \\frac{R}{3}$ (Option C).",
            "Distractor A ($9R$) and Distractor B ($3R$) treat resistance as scaling directly with volume or length without considering the quadratic increase in cross-sectional area."
        ]
    },
    # Q34
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q34",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "comparison"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_sketch_terminal_potential_difference_current_graph",
        "accepted_answer": "B",
        "hints": [
            "Relate the terminal potential difference $V$ to e.m.f. $E$, current $I$, and internal resistance $r$ using the equation $V = E - I r$.",
            "Identify what the y-intercept (at $I = 0$) and the gradient represent: y-intercept $= E$, gradient $= -r$."
        ],
        "walkthrough": [
            "The equation for terminal potential difference as a function of current is $V = E - I r$. Comparing this to the straight-line equation $y = mx + c$, the vertical intercept on the $V$-axis is the e.m.f. $E$, and the gradient is $-r$ (magnitude of slope equals internal resistance $r$).",
            "As the cell nears the end of its useful life:\n1. Its e.m.f. $E$ decreases, which shifts the vertical intercept downwards.\n2. Its internal resistance $r$ increases, which makes the negative gradient steeper (magnitude of slope $|-r|$ increases).",
            "Graph B correctly illustrates a lower vertical intercept and a steeper downward slope than the original graph.",
            "Graph A has a less steep slope (smaller $r$), Graph C has an increased e.m.f., and Graph D has both increased e.m.f. and reduced internal resistance."
        ]
    },
    # Q35
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q35",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "circuit_analysis",
            "direct_calculation"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m02",
        "skill_id": "9702_skill_apply_kirchhoffs_second_law",
        "accepted_answer": "C",
        "hints": [
            "Apply Kirchhoff's second law (sum of potential rises equals sum of potential drops around any closed loop) to the different parallel branches.",
            "The total supply voltage is $V_0 = 20\\text{ V}$. For the top branch containing L ($7\\text{ V}$) and M, find $V_M$. For the path through L ($7\\text{ V}$), N ($4\\text{ V}$), and Q, find $V_Q$."
        ],
        "walkthrough": [
            "Using Kirchhoff's second law for closed loops:\n1. Top loop across the $V_0 = 20\\text{ V}$ supply through resistors L and M: $V_{\\text{supply}} = V_L + V_M \\implies V_{\\text{tot}} = 7\\text{ V} + V_M = 20\\text{ V} \\implies V_M = 20 - 7 = 13\\text{ V}$.\n2. Path across the supply through L, N, and Q: $V_{\\text{supply}} = V_L + V_N + V_Q \\implies 20\\text{ V} = 7\\text{ V} + 4\\text{ V} + V_Q \\implies V_Q = 20 - 11 = 9\\text{ V}$.\n3. Resistor P is in parallel across the combination of L and N (or $V_P + V_Q = 20\\text{ V}$): $V_P = V_L + V_N = 7\\text{ V} + 4\\text{ V} = 11\\text{ V}$ (or $V_P = 20 - 9 = 11\\text{ V}$).",
            "Thus, the potential drops are: $V_M = 13\\text{ V}$, $V_P = 11\\text{ V}$, and $V_Q = 9\\text{ V}$ (Option C).",
            "Rows A, B, and D fail Kirchhoff's voltage law around one or more closed loops."
        ]
    },
    # Q36
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q36",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "circuit_analysis",
            "explanation"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m03",
        "skill_id": "9702_skill_calculate_series_circuit_potential_difference",
        "accepted_answer": "A",
        "hints": [
            "Recall the potential divider equation for the output voltage across $R_2$: $V = V_0 \\left(\\frac{R_2}{R_1 + R_2}\\right)$.",
            "Analyze the effect on output $V$ when $R_1$ increases: consider both the fraction of total voltage dropped across $R_1$ and $R_2$."
        ],
        "walkthrough": [
            "The output voltage across resistor $R_2$ is given by the potential divider formula: $V = V_0 \\frac{R_2}{R_1 + R_2} = \\frac{V_0}{1 + \\frac{R_1}{R_2}}$.",
            "When $R_1$ increases while $R_2$ remains constant, the ratio $\\frac{R_1}{R_1 + R_2}$ increases, meaning resistor $R_1$ takes a larger share of the total supply voltage $V_0$.",
            "Because $V_0 = V_1 + V$, an increase in $V_1$ necessitates a decrease in the output potential difference $V$ across $R_2$ (Option A).",
            "Statement B is false because while current decreases, $V = I R_2$ also decreases, not increases. Statements C and D give incorrect directions for the potential division."
        ]
    },
    # Q37
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q37",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "equation_completion",
            "direct_calculation"
        ],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m01",
        "skill_id": "9702_skill_complete_nuclear_equations",
        "accepted_answer": "A",
        "hints": [
            "Set up conservation equations for nucleon number (mass number $A$) and proton number (atomic number $Z$) across the decay chain $^{238}_{92}\\text{U} \\rightarrow {}^{206}_{82}\\text{Pb} + N_\\alpha (^4_2\\alpha) + N_\\beta (^0_{-1}\\beta)$.",
            "First find the number of $\\alpha$-particles $N_\\alpha$ using nucleon number conservation, then use proton number conservation to find the number of $\\beta^-$ particles $N_\\beta$."
        ],
        "walkthrough": [
            "Let $N_\\alpha$ be the number of emitted $\\alpha$-particles ($^4_2\\text{He}$) and $N_\\beta$ be the number of emitted $\\beta^-$ particles ($^0_{-1}\\text{e}$).",
            "1. Conservation of nucleon number $A$:\n$A_{\\text{initial}} = A_{\\text{final}} \\implies 238 = 206 + 4 N_\\alpha + 0 N_\\beta \\implies 4 N_\\alpha = 238 - 206 = 32 \\implies N_\\alpha = 8$.",
            "2. Conservation of proton number $Z$:\n$Z_{\\text{initial}} = Z_{\\text{final}} \\implies 92 = 82 + 2 N_\\alpha - 1 N_\\beta \\implies 92 = 82 + 2(8) - N_\\beta \\implies 92 = 82 + 16 - N_\\beta = 98 - N_\\beta$.\nSolving for $N_\\beta$: $N_\\beta = 98 - 92 = 6$.",
            "Thus, a total of $6$ $\\beta^-$ particles are emitted (Option A).",
            "Option B ($8$) is the number of $\\alpha$-particles emitted. Options C and D arise from sign errors in the beta-minus charge equation."
        ]
    },
    # Q38
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q38",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "property_identification",
            "classification"
        ],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m01",
        "skill_id": "9702_skill_distinguish_alpha_beta_energy_spectra",
        "accepted_answer": "D",
        "hints": [
            "Recall the physical properties of alpha particles: charge ($+2e = +3.20 \\times 10^{-19}\\text{ C}$), energy spectrum (discrete line spectrum), ionising power (strongly ionising), and typical emission speeds.",
            "Alpha particles are emitted with discrete kinetic energies of around $4\\text{ to }8\\text{ MeV}$, giving emission speeds on the order of $v \\sim 10^7\\text{ m s}^{-1}$ (around $5\\%$ the speed of light)."
        ],
        "walkthrough": [
            "Alpha particles are emitted from a specific nuclear transition with discrete (monochromatic) energy values, unlike beta decay which produces a continuous energy spectrum. Thus statement A is incorrect.",
            "Because of their $+2e$ charge and larger mass, alpha particles have significantly higher ionising power than beta particles. Thus statement B is incorrect.",
            "The charge of an $\\alpha$-particle (a helium-4 nucleus) is $+2e = +2(1.60 \\times 10^{-19}\\text{ C}) = +3.20 \\times 10^{-19}\\text{ C}$. Thus statement C is incorrect.",
            "Alpha particles typically have kinetic energies of $5\\text{ MeV}$, giving speeds of $v = \\sqrt{\\frac{2E}{m}} \\approx \\sqrt{\\frac{2 \\times 5 \\times 10^6 \\times 1.6 \\times 10^{-19}}{6.64 \\times 10^{-27}}} \\approx 1.5 \\times 10^7\\text{ m s}^{-1}$ (about $5\\%$ the speed of light). Thus statement D is correct (Option D)."
        ]
    },
    # Q39
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q39",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "equation_completion",
            "particle_model_application"
        ],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m02",
        "skill_id": "9702_skill_identify_beta_decay_products",
        "accepted_answer": "A",
        "hints": [
            "Recall the fundamental process occurring in $\\beta^-$ (beta-minus) decay: a down quark changes to an up quark ($d \\rightarrow u + e^- + \\bar{\\nu}_e$), converting a neutron into a proton.",
            "Check lepton number conservation: before decay, total lepton number is $0$. After decay, the electron has lepton number $+1$, so an antilepton with lepton number $-1$ must be emitted."
        ],
        "walkthrough": [
            "In beta-minus ($\\beta^-$) decay of carbon-14 ($^{14}_6\\text{C} \\rightarrow {}^{14}_7\\text{N} + {}^0_{-1}\\beta + \\dots$), a neutron inside the nucleus transforms into a proton, an electron, and an electron antineutrino: $n \\rightarrow p + e^- + \\bar{\\nu}_e$.",
            "Lepton number conservation requires: $L_{\\text{initial}} = 0 = L_{\\text{final}} = (+1)_{e^-} + (-1)_{\\bar{\\nu}_e} = 0$.",
            "Therefore, the missing particle is an antineutrino (Option A).",
            "Option C (neutrino) is emitted during $\\beta^+$ decay, Option B (electron) is already included as $\\beta^-$, and Option D (positron) is the antiparticle emitted in $\\beta^+$ decay."
        ]
    },
    # Q40
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_13_q40",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "classification",
            "definition"
        ],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m02",
        "skill_id": "9702_skill_define_fundamental_particle",
        "accepted_answer": "A",
        "hints": [
            "Recall the definition of a fundamental particle: a particle that has no known internal structure and cannot be broken down into smaller constituents.",
            "Distinguish between leptons (which are fundamental) and hadrons (which are composite particles made of quarks)."
        ],
        "walkthrough": [
            "A fundamental (elementary) particle is a subatomic particle with no substructure, meaning it is not composed of smaller particles.",
            "Electrons belong to the lepton family and are fundamental particles (Option A).",
            "Hadrons (Option B) are composite particles bound together by the strong force. Protons (Option D, composed of $uud$ quarks) and neutrons (Option C, composed of $udd$ quarks) are baryons, which are types of hadrons, and are therefore not fundamental particles."
        ]
    }
]

def main():
    print(f"Generating {len(enrichments)} enrichment files for 9702_s17_13...")
    for item in enrichments:
        qid = item["question_id"]
        out_path = OUTPUT_DIR / f"{qid}.enrichment.json"
        out_path.write_text(json.dumps(item, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"  Wrote {out_path.name}")
    print("Done!")

if __name__ == "__main__":
    main()
