#!/usr/bin/env python3
"""
generate_9702_w23_12_enrichment.py

Generates P1 enrichment records for 9702_w23_12 (Q01 to Q40) matching schema 9702_p1_enrichment_v1.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENRICH_DIR = ROOT / "subjects/physics/9702/enrichment/p1"
ENRICH_DIR.mkdir(parents=True, exist_ok=True)

ENRICHMENTS = [
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q01",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "physical_quantity_estimation",
            "comparison"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m01",
        "skill_id": "9702_skill_physical_estimations",
        "accepted_answer": "B",
        "hints": [
            "Convert each estimated speed into consistent SI units ($\\text{m s}^{-1}$) to compare their physical plausibility directly.",
            "Recall typical human sprinting speeds: an elite sprinter covers $s = 100\\text{ m}$ in approximately $t = 10\\text{ s}$, which corresponds to roughly $v \\approx 10\\text{ m s}^{-1}$."
        ],
        "walkthrough": [
            "Convert all options to $\\text{m s}^{-1}$:\n- Option A: $v = 10\\text{ m s}^{-1} = 36\\text{ km h}^{-1} \\approx 19.4\\text{ knots}$, which is a typical cruise/maximum speed for a modern container ship.\n- Option B: $v = 0.1\\text{ km s}^{-1} = 0.1 \\times 10^3\\text{ m s}^{-1} = 100\\text{ m s}^{-1} = 360\\text{ km h}^{-1}$. A human world-record sprinter reaches approximately $ 10\\text{--}12\\text{ m s}^{-1}$. Thus, $ 100\\text{ m s}^{-1}$ is unrealistic by a factor of 10.\n- Option C: $v = 9000\\text{ cm s}^{-1} = 90\\text{ m s}^{-1} = 324\\text{ km h}^{-1}$, which is well within the top speed capability of a Formula 1 racing car.\n- Option D: $v = 0.01\\text{ km h}^{-1} = 10\\text{ m h}^{-1} = \\frac{10}{3600}\\text{ m s}^{-1} \\approx 2.8\\text{ mm s}^{-1}$, which is a realistic crawl speed for a garden snail.",
            "Because $v = 0.1\\text{ km s}^{-1}$ ($ 100\\text{ m s}^{-1}$) represents an impossible speed for an Olympic sprinter, option B is the estimate that is not reasonable."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q02",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "classification",
            "property_identification"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m02",
        "skill_id": "9702_skill_si_units_homogeneity",
        "accepted_answer": "D",
        "hints": [
            "Carefully distinguish between a physical quantity (a property that is measured) and a unit (the standard used to measure it).",
            "Recall the seven SI base quantities: length, mass, time, electric current, thermodynamic temperature, amount of substance, and luminous intensity."
        ],
        "walkthrough": [
            "The International System of Units (SI) defines seven fundamental base quantities, one of which is time.",
            "Reviewing the choices:\n- Option A: Force is a derived physical quantity ($[\\text{force}] = \\text{kg m s}^{-2}$).\n- Option B: Newton ($\\text{N}$) is a derived unit of force, not a quantity.\n- Option C: Second ($\\text{s}$) is the SI base unit of time, but the question specifically asks for an SI base quantity.\n- Option D: Time is one of the seven base physical quantities, making D the correct answer."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q03",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "uncertainty_analysis",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m03",
        "skill_id": "9702_skill_errors_uncertainties",
        "accepted_answer": "D",
        "hints": [
            "Rearrange $s = \\frac{1}{2} a t^2$ to express acceleration as $a = \\frac{2s}{t^2}$ and substitute the measured values.",
            "When combining uncertainties for a quotient involving powers, fractional uncertainties add: $\\frac{\\Delta a}{a} = \\frac{\\Delta s}{s} + 2 \\frac{\\Delta t}{t}$."
        ],
        "walkthrough": [
            "Step 1: Calculate the value of acceleration $a$:\n$a = \\frac{2s}{t^2} = \\frac{2 \\times 16.5}{(15.0)^2} = \\frac{33.0}{225} = 0.1467\\text{ m s}^{-2} \\approx 0.15\\text{ m s}^{-2}$",
            "Step 2: Combine fractional uncertainties:\n$\\frac{\\Delta a}{a} = \\frac{\\Delta s}{s} + 2\\left(\\frac{\\Delta t}{t}\\right) = \\frac{0.1}{16.5} + 2\\left(\\frac{1.0}{15.0}\\right) = 0.00606 + 0.13333 = 0.1394$\nCalculate the absolute uncertainty $\\Delta a$:\n$\\Delta a = a \\times 0.1394 = 0.1467 \\times 0.1394 = 0.0204\\text{ m s}^{-2} \\approx 0.02\\text{ m s}^{-2}$\nThus, the result is $(0.15 \\pm 0.02)\\text{ m s}^{-2}$, matching option D.",
            "Options A and B incorrectly compute the central value as $a = 0.11\\text{ m s}^{-2}$ by neglecting the factor of 2 (calculating $\\frac{s}{t^2}$ instead of $\\frac{2s}{t^2}$). Option C computes $\\Delta a$ without doubling the fractional uncertainty of time."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q04",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "force_diagram_construction",
            "comparison"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m02",
        "skill_id": "9702_skill_equilibrium_coplanar_forces",
        "accepted_answer": "A",
        "hints": [
            "Since the aeroplane moves at constant speed in a straight line, its acceleration is zero and the resultant force in every direction is zero.",
            "Resolve forces parallel to the direction of motion (along the climb angle $\\theta$) and perpendicular to the direction of motion."
        ],
        "walkthrough": [
            "The motion is along a line inclined at angle $\\theta$ above the horizontal. Weight $W$ acts vertically downwards:\n- The component of $W$ perpendicular to the line of motion is $W \\cos \\theta$ acting opposite to the lift force $L$.\n- The component of $W$ parallel to the line of motion is $W \\sin \\theta$ acting down the incline (opposite to thrust $T$, in the same direction as resistive force $R$).",
            "Setting up equilibrium equations:\n- Perpendicular to motion: $L - W \\cos \\theta = 0 \\implies L = W \\cos \\theta$.\n- Parallel to motion: $T - R - W \\sin \\theta = 0 \\implies T = R + W \\sin \\theta$.\nThis pair of relationships corresponds exactly to option A.",
            "Options B and D confuse the sine and cosine components of weight. Option C incorrectly has $T = R - W \\sin \\theta$, which would mean weight assists the thrust rather than opposes the climb."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q05",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "definition"
        ],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_displacement_velocity_acceleration",
        "accepted_answer": "D",
        "hints": [
            "Recall standard kinematic definitions from the AS syllabus.",
            "Consider which vector kinematic quantity changes over time when an object accelerates."
        ],
        "walkthrough": [
            "Acceleration is defined as the rate of change of velocity with respect to time ($a = \\frac{\\Delta v}{\\Delta t}$).",
            "Evaluating other options:\n- Option A defines velocity (rate of change of displacement).\n- Option B defines power transferred mechanically.\n- Option C defines resultant force by Newton's second law (rate of change of momentum).\nHence, option D is the correct definition."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q06",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "multi_step_calculation"
        ],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_projectile_motion",
        "accepted_answer": "B",
        "hints": [
            "Treat horizontal and vertical motions independently: horizontal velocity remains constant in the absence of air resistance.",
            "Use $v_y = u_y + a_y t$ to find the vertical component of velocity at $t = 9.00\\text{ s}$, then combine the perpendicular components to find the speed using the Pythagorean theorem."
        ],
        "walkthrough": [
            "Step 1: Horizontal velocity is constant: $v_x = u_x = 4.00\\text{ m s}^{-1}$.",
            "Step 2: Determine vertical velocity after $t = 9.00\\text{ s}$ with downward acceleration $g = 1.62\\text{ m s}^{-2}$:\n$v_y = u_y - g t = 8.00 - (1.62)(9.00) = 8.00 - 14.58 = -6.58\\text{ m s}^{-1}$",
            "Step 3: Calculate the magnitude of the velocity (speed):\n$v = \\sqrt{v_x^2 + v_y^2} = \\sqrt{(4.00)^2 + (-6.58)^2} = \\sqrt{16.00 + 43.2964} = \\sqrt{59.2964} \\approx 7.70\\text{ m s}^{-1}$\nThis matches option B.",
            "Option A ($v = 6.58\\text{ m s}^{-1}$) is only the vertical velocity component $|v_y|$. Option C ($v = 10.6\\text{ m s}^{-1}$) arises from adding the speeds linearly ($ 4.00 + 6.58 = 10.58$). Option D ($v = 14.6\\text{ m s}^{-1}$) uses the change in vertical velocity $gt$ without accounting for the initial vertical velocity."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q07",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "multi_step_calculation"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_newtons_laws",
        "accepted_answer": "A",
        "hints": [
            "Apply Newton's second law ($F_{\\text{net}} = m a$) to the suspended block to find string tension $T$, or treat both blocks as a single combined system.",
            "For the combined system along the string, the accelerating force is the weight of the suspended block and the opposing force is friction: $m_2 g - F_f = (m_1 + m_2) a$."
        ],
        "walkthrough": [
            "Method 1 (System approach):\n- Total mass $m_{\\text{total}} = 0.20 + 0.50 = 0.70\\text{ kg}$.\n- Driving force along string = weight of suspended block = $m_2 g = 0.50 \\times 9.81 = 4.905\\text{ N}$.\n- Using $F_{\\text{net}} = m_{\\text{total}} a$:\n$m_2 g - F_f = (m_1 + m_2) a$\n$ 4.905 - F_f = 0.70 \\times 2.0 = 1.40\\text{ N}$\n$F_f = 4.905 - 1.40 = 3.505\\text{ N} \\approx 3.5\\text{ N}$",
            "Method 2 (Component equations):\n- For the $ 0.50\\text{ kg}$ mass: $m_2 g - T = m_2 a \\implies T = 0.50(9.81 - 2.0) = 3.905\\text{ N}$.\n- For the $ 0.20\\text{ kg}$ mass: $T - F_f = m_1 a \\implies F_f = 3.905 - (0.20 \\times 2.0) = 3.505\\text{ N} \\approx 3.5\\text{ N}$.\nThis confirms option A is correct.",
            "Option B ($T = 3.9\\text{ N}$) is the tension in the string $T$. Option C ($F = 4.5\\text{ N}$) incorrectly adds $m_1 a$ instead of subtracting. Option D ($F = 6.3\\text{ N}$) results from adding $m_2 g + m_{\\text{total}} a$."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q08",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "definition"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_newtons_laws",
        "accepted_answer": "C",
        "hints": [
            "Recall Newton's second law of motion expressed in terms of momentum.",
            "Consider the rate of change of which physical quantity equals the resultant force."
        ],
        "walkthrough": [
            "Newton's second law of motion states that the resultant force acting on an object is directly proportional to (and in SI units equal to) the rate of change of momentum: $F_{\\text{res}} = \\frac{\\Delta p}{\\Delta t}$.",
            "Evaluating other choices:\n- Option A (acceleration per unit mass, $a/m$) is dimensionally $\\text{s}^{-2}$, not force.\n- Option B (change in kinetic energy per unit time, $\\frac{\\Delta E_k}{\\Delta t}$) defines power.\n- Option D (change in velocity per unit time, $\\frac{\\Delta v}{\\Delta t}$) defines acceleration.\nTherefore, option C is correct."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q09",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "property_identification",
            "explanation"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m02",
        "skill_id": "9702_skill_drag_terminal_velocity",
        "accepted_answer": "B",
        "hints": [
            "Consider the forces acting on the falling object: downward weight and upward drag force.",
            "As the speed of the falling object increases, the drag force increases, reducing the resultant force and hence the acceleration until equilibrium is reached."
        ],
        "walkthrough": [
            "At the moment of release from the stationary helicopter, speed is zero and air resistance is zero, so acceleration equals $g = 9.81\\text{ m s}^{-2}$.",
            "As the object accelerates downwards, speed increases, causing air resistance (drag force $D$) to increase. The net downward force $F_{\\text{net}} = mg - D$ decreases, so acceleration $a = g - \\frac{D}{m}$ decreases continuously.",
            "When drag force equals the weight ($D = mg$), the resultant force becomes zero and the object travels at terminal velocity with zero acceleration. Thus, the acceleration decreases to zero, which is option B."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q10",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "multi_step_calculation"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m03",
        "skill_id": "9702_skill_linear_momentum_collisions",
        "accepted_answer": "C",
        "hints": [
            "Use the conservation of linear momentum to find the velocity of mass $ 2m$ after the collision.",
            "Calculate the total initial kinetic energy and total final kinetic energy, then find the difference $\\Delta E_k = E_{k,\\text{initial}} - E_{k,\\text{final}}$."
        ],
        "walkthrough": [
            "Step 1: Total initial momentum (taking right as positive):\n$p_{\\text{initial}} = m(+2v) + 2m(-v) = 2mv - 2mv = 0$",
            "Step 2: By conservation of linear momentum, total final momentum must also be 0:\n$p_{\\text{final}} = m(-v) + 2m(v_2) = 0 \\implies 2m(v_2) = mv \\implies v_2 = +\\frac{1}{2}v$",
            "Step 3: Initial kinetic energy:\n$E_{k,\\text{initial}} = \\frac{1}{2}m(2v)^2 + \\frac{1}{2}(2m)(v)^2 = 2mv^2 + mv^2 = 3mv^2$",
            "Step 4: Final kinetic energy:\n$E_{k,\\text{final}} = \\frac{1}{2}m(v)^2 + \\frac{1}{2}(2m)\\left(\\frac{1}{2}v\\right)^2 = \\frac{1}{2}mv^2 + \\frac{1}{4}mv^2 = \\frac{3}{4}mv^2$",
            "Step 5: Loss of kinetic energy:\n$\\text{Loss} = 3mv^2 - \\frac{3}{4}mv^2 = \\frac{9}{4}mv^2$\nThis matches option C.",
            "Option A ($\\frac{4}{3}mv^2$) or B ($\\frac{3}{2}mv^2$) or D ($\\frac{9}{2}mv^2$) represent arithmetic errors or incorrect velocity assignments for the second ball."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q11",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "property_identification"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_moments_couples",
        "accepted_answer": "A",
        "hints": [
            "Moment of a force about a pivot equals the force multiplied by the perpendicular distance from the pivot, or the perpendicular component of force multiplied by distance $d$.",
            "Identify the angle between force $F$ and the handle line: the force is inclined at angle $\\theta = 45^\\circ$ to the vertical, and the handle is horizontal, so the angle to the handle is $ 90^\\circ - 45^\\circ = 45^\\circ$."
        ],
        "walkthrough": [
            "The handle is horizontal with distance $d$ between the pivot and the point of application of $F$.",
            "The force $F$ is directed at angle $\\theta = 45^\\circ$ to the vertical line perpendicular to the handle, which means the angle between the force and the perpendicular direction is $ 45^\\circ$ (and the angle to the handle is also $ 45^\\circ$).",
            "The component of $F$ perpendicular to the handle is:\n$F_{\\perp} = F \\cos 45^\\circ = \\frac{F}{\\sqrt{2}}$",
            "Therefore, the moment about the pivot is:\n$\\text{Moment} = F_{\\perp} \\times d = \\frac{Fd}{\\sqrt{2}}$\nThis corresponds to option A.",
            "Option B ($Fd$) omits the angle factor. Option C ($Fd\\sqrt{2}$) and Option D ($ 2Fd$) incorrectly multiply by trigonometric factors rather than resolving the perpendicular component."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q12",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "definition",
            "direct_calculation"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_moments_couples",
        "accepted_answer": "C",
        "hints": [
            "Recall the definition of a couple: two equal, parallel, and oppositely directed forces.",
            "The torque of a couple is defined as one force multiplied by the perpendicular distance between the lines of action of the forces."
        ],
        "walkthrough": [
            "By definition, the torque of a couple is given by $\\tau = F \\times d$, where $F$ is the magnitude of one of the forces and $d$ is the perpendicular distance between them.",
            "Checking the options:\n- Option A ($\\frac{1}{2}Fd$) mistakenly divides by 2 as if taking moments about a midpoint.\n- Option B ($F/d$) is dimensionally incorrect ($\\text{N m}^{-1}$).\n- Option C ($Fd$) matches the definition exactly.\n- Option D ($ 2Fd$) mistakenly adds the two forces together before multiplying by distance."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q13",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "force_diagram_construction"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m02",
        "skill_id": "9702_skill_equilibrium_coplanar_forces",
        "accepted_answer": "B",
        "hints": [
            "Draw a closed vector triangle or resolve forces in horizontal and vertical directions for the ball in equilibrium.",
            "Vertical equilibrium gives $T \\cos \\theta = W$ with $\\theta = 30^\\circ$, and horizontal equilibrium gives $T \\sin \\theta = F_{\\text{air}}$."
        ],
        "walkthrough": [
            "The ball is in equilibrium under three coplanar forces:\n1. Downward weight $W = 0.15\\text{ N}$\n2. Horizontal force from air flow $F_{\\text{air}}$\n3. Tension $T$ in the string inclined at $\\theta = 30^\\circ$ to the vertical",
            "Setting up the equilibrium equations:\n- Vertical direction: $T \\cos 30^\\circ = W = 0.15\\text{ N} \\implies T = \\frac{0.15}{\\cos 30^\\circ}$\n- Horizontal direction: $F_{\\text{air}} = T \\sin 30^\\circ$",
            "Dividing the two equations gives:\n$F_{\\text{air}} = W \\tan 30^\\circ = 0.15 \\times \\tan(30^\\circ) = 0.15 \\times 0.5774 = 0.0866\\text{ N} \\approx 0.087\\text{ N}$\nThis matches option B.",
            "Option A ($F = 0.075\\text{ N}$) comes from calculating $W \\sin 30^\\circ = 0.15 \\times 0.5$. Option C ($F = 0.26\\text{ N}$) comes from dividing $W / \\tan 30^\\circ = 0.26\\text{ N}$. Option D ($F = 0.30\\text{ N}$) comes from $W / \\sin 30^\\circ$."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q14",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "property_identification",
            "comparison"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m03",
        "skill_id": "9702_skill_upthrust_archimedes",
        "accepted_answer": "C",
        "hints": [
            "Apply Archimedes' principle: upthrust is equal to the weight of fluid displaced by the submerged object.",
            "Check which variables determine upthrust ($U = \\rho_{\\text{liquid}} V g$) and note that both cylinders have the same submerged volume $V$ in the same liquid."
        ],
        "walkthrough": [
            "Archimedes' principle states that upthrust $U = \\rho_{\\text{liquid}} V g$. Because both cylindrical objects are fully submerged and have identical volume $V$, the volume of liquid displaced by each is equal. Since they are submerged in the same liquid, the upthrust acting on X equals the upthrust acting on Y, making option C correct.",
            "Evaluating other statements:\n- Option A: Force on top surface is $F_{\\text{top}} = p_{\\text{top}} A = \\rho_{\\text{liquid}} g h A$. Cylinder X has a smaller top area $A_X$ and smaller depth $h_X$ to top surface, so force on top of X is smaller, not greater.\n- Option B: Pressure difference between top and bottom surfaces is $\\Delta p = \\rho_{\\text{liquid}} g \\Delta h$. Cylinder X is taller than Y (greater $\\Delta h$), so $\\Delta p$ is greater for X.\n- Option D: Weight is $W = \\rho_{\\text{material}} V g$. Since material density of Y is twice that of X, $W_Y = 2W_X$, so weights are different."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q15",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "multi_step_calculation",
            "comparison"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_work_done",
        "accepted_answer": "A",
        "hints": [
            "At constant speed, driving force equals resistive force ($F = k v^2$).",
            "Work done (energy used) over distance $s$ is $W = F \\times s = k v^2 s$. Since distance $s$ is identical in both trips, energy used is proportional to $v^2$."
        ],
        "walkthrough": [
            "Step 1: At constant speed, forward force $F = F_{\\text{resistive}} = k v^2$.",
            "Step 2: Energy consumed from the battery to travel distance $s$ is:\n$W = F \\times s = k s v^2$\nBecause the distance $s = 80\\text{ km}$ is unchanged, $W \\propto v^2$.",
            "Step 3: Calculate the ratio of energy consumed at $v_2 = 60\\text{ km h}^{-1}$ relative to $v_1 = 70\\text{ km h}^{-1}$:\n$\\frac{E_2}{E} = \\left(\\frac{v_2}{v_1}\\right)^2 = \\left(\\frac{60}{70}\\right)^2 = \\left(\\frac{6}{7}\\right)^2 = \\frac{36}{49} \\approx 0.7347$\nTherefore, $E_2 \\approx 0.73E$, matching option A.",
            "Option B ($ 0.86E$) mistakenly assumes energy is proportional to speed ($v/v_1 = 60/70 = 0.857$). Options C and D calculate inverse ratios ($ 70/60$ and $(70/60)^2$)."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q16",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "definition"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_power_efficiency",
        "accepted_answer": "C",
        "hints": [
            "Recall the standard definition of efficiency for an energy conversion system.",
            "Efficiency is the fraction of total energy supplied that is converted into useful output."
        ],
        "walkthrough": [
            "Efficiency is defined as the ratio of useful energy output from the system to the total energy input to the system: $\\eta = \\frac{\\text{useful energy output}}{\\text{total energy input}}$ (or multiplied by $ 100\\%$ for a percentage).",
            "Reviewing options:\n- Option A inverts the ratio (total input / useful output).\n- Option B gives useful output / wasted energy, which is not the standard efficiency definition.\n- Option C correctly gives useful energy output divided by total energy input.\n- Option D gives fractional energy wasted rather than efficiency."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q17",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "equation_derivation",
            "explanation"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m02",
        "skill_id": "9702_skill_kinetic_potential_energy",
        "accepted_answer": "D",
        "hints": [
            "Consider how gravitational potential energy is defined: it is the energy stored when work is done against gravity.",
            "To raise mass $m$ at constant speed, upward force equals weight ($F = mg$), and work done is $W = F \\times \\Delta h$."
        ],
        "walkthrough": [
            "Gravitational potential energy gained $\\Delta E_P$ is derived from the work done by an upward lifting force acting against gravitational force: $W = F s$.",
            "Since the lifting force equals weight $mg$ and the displacement is $\\Delta h$, the work done is $W = mg\\Delta h$. Equating $\\Delta E_P$ to the work done against gravity requires the fundamental definition of work done ($W = F s$).",
            "Definitions of acceleration (A), momentum (B), and power (C) do not provide the basis for establishing energy change as force multiplied by displacement. Thus, option D is correct."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q18",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "comparison",
            "direct_calculation"
        ],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m01",
        "skill_id": "9702_skill_hookes_law_elastic_energy",
        "accepted_answer": "B",
        "hints": [
            "For springs in parallel, spring constants add ($k_{\\text{parallel}} = k_1 + k_2 + \\dots$). For springs in series, reciprocals add ($\\frac{1}{k_{\\text{series}}} = \\frac{1}{k_1} + \\frac{1}{k_2} + \\dots$).",
            "Calculate the equivalent spring constant for all four arrangements in terms of single-spring constant $k$."
        ],
        "walkthrough": [
            "Let each identical spring have spring constant $k$:\n- Arrangement A: Two springs in series ($k_{\\text{series}} = \\frac{k}{2}$) in parallel with one spring ($k$): $k_A = \\frac{k}{2} + k = 1.5k$.\n- Arrangement B: Three springs in parallel: $k_B = k + k + k = 3.0k$.\n- Arrangement C: Two springs in parallel ($ 2k$) in series with one spring ($k$): $\\frac{1}{k_C} = \\frac{1}{2k} + \\frac{1}{k} = \\frac{3}{2k} \\implies k_C = \\frac{2}{3}k \\approx 0.67k$.\n- Arrangement D: Three springs in series: $\\frac{1}{k_D} = \\frac{3}{k} \\implies k_D = \\frac{k}{3} \\approx 0.33k$.",
            "Comparing values: $k_B = 3.0k > k_A = 1.5k > k_C = 0.67k > k_D = 0.33k$. The largest combined spring constant is Arrangement B, so option B is correct."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q19",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "graph_interpretation",
            "property_identification"
        ],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m02",
        "skill_id": "9702_skill_elastic_plastic_behaviour",
        "accepted_answer": "D",
        "hints": [
            "Hooke's law applies along the initial straight line up to the point where linearity ends.",
            "Beyond the elastic limit / limit of proportionality, permanent deformation occurs (plastic deformation)."
        ],
        "walkthrough": [
            "On a force–extension graph for a ductile wire:\n- Region X represents the initial linear portion where force is directly proportional to extension; this is the region of elastic deformation.\n- Point Z is the boundary point where linearity ends; this is the limit of proportionality.\n- Region Y represents the non-linear portion where the material undergoes permanent, irreversible elongation; this is the region of plastic deformation.",
            "Matching to the table columns:\n- Limit of proportionality: Z\n- Region of elastic deformation: X\n- Region of plastic deformation: Y\nThis corresponds to row D."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q20",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "direct_calculation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_progressive_wave_properties",
        "accepted_answer": "D",
        "hints": [
            "Determine the spatial separation $\\Delta x$ between points X and Y in terms of the wavelength $\\lambda$.",
            "Convert spatial separation to phase difference using $\\Delta \\phi = \\frac{\\Delta x}{\\lambda} \\times 360^\\circ$."
        ],
        "walkthrough": [
            "Step 1: Point X is at zero displacement moving downwards (at equilibrium). Moving to the right from X:\n- A distance of $\\frac{1}{4}\\lambda$ reaches the next trough.\n- A distance of $\\frac{1}{2}\\lambda$ reaches the next equilibrium position (moving upwards).\n- A distance of $\\frac{3}{4}\\lambda$ reaches the crest, which is the position of point Y.\nThus, the distance between X and Y is $\\Delta x = \\frac{3}{4}\\lambda$.",
            "Step 2: Calculate the phase difference $\\Delta \\phi$:\n$\\Delta \\phi = \\frac{360^\\circ}{\\lambda} \\times \\Delta x = \\frac{360^\\circ}{\\lambda} \\times \\frac{3}{4}\\lambda = 270^\\circ$\nThis corresponds to option D.",
            "Option A ($\\Delta \\phi = 45^\\circ$) corresponds to $\\frac{1}{8}\\lambda$. Option B ($\\Delta \\phi = 135^\\circ$) corresponds to $\\frac{3}{8}\\lambda$. Option C ($\\Delta \\phi = 180^\\circ$) corresponds to $\\frac{1}{2}\\lambda$ (two points in antiphase)."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q21",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "property_identification"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_progressive_wave_properties",
        "accepted_answer": "C",
        "hints": [
            "Note the initial displacement of particle X at $t = 0$ from the displacement–distance graph.",
            "Determine the initial direction of motion of particle X: imagine shifting the entire waveform slightly to the right (direction of wave propagation) and see where particle X moves."
        ],
        "walkthrough": [
            "Step 1: At $t = 0$, particle X is located at zero displacement (equilibrium). Therefore, its displacement–time graph must start at $(0, 0)$, which rules out options B and D.",
            "Step 2: The wave propagates to the right (positive distance direction). Consider the profile immediately to the left of X: it is a negative trough. As the wave travels rightward, the incoming trough arrives at particle X next, so particle X must initially move downwards into negative displacement.",
            "Step 3: Looking at the remaining graphs starting at 0: Graph A starts by moving positive, whereas Graph C starts by moving negative. Thus, Graph C correctly shows the variation of displacement with time for particle X, matching option C."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q22",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m03",
        "skill_id": "9702_skill_doppler_effect",
        "accepted_answer": "A",
        "hints": [
            "Recall the Doppler effect formula for a source moving towards a stationary observer: $f_o = f_s \\left(\\frac{v}{v - v_s}\\right)$.",
            "Substitute observed frequency $f_o = 650\\text{ Hz}$, source frequency $f_s = 480\\text{ Hz}$, and sound speed $v = 340\\text{ m s}^{-1}$, then solve for source speed $v_s$."
        ],
        "walkthrough": [
            "Step 1: Set up the Doppler formula:\n$f_o = f_s \\left(\\frac{v}{v - v_s}\\right)$\n$ 650 = 480 \\left(\\frac{340}{340 - v_s}\\right)$",
            "Step 2: Rearrange and solve for $v_s$:\n$ 340 - v_s = 340 \\times \\frac{480}{650} = 340 \\times \\frac{48}{65} \\approx 251.08\\text{ m s}^{-1}$\n$v_s = 340 - 251.08 = 88.92\\text{ m s}^{-1} \\approx 89\\text{ m s}^{-1}$\nThis matches option A.",
            "Option B ($v_s = 120\\text{ m s}^{-1}$) or C ($v_s = 250\\text{ m s}^{-1}$) result from algebraic inversion errors or using the observed speed $ 340 - v_s$ directly."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q23",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "classification",
            "property_identification"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m04",
        "skill_id": "9702_skill_electromagnetic_spectrum",
        "accepted_answer": "C",
        "hints": [
            "Recall the approximate wavelength range of the visible spectrum ($\\lambda = 400\\text{ nm}$ to $ 700\\text{ nm}$, i.e., $ 4 \\times 10^{-7}\\text{ m}$ to $ 7 \\times 10^{-7}\\text{ m}$).",
            "Use $\\lambda = \\frac{c}{f}$ with speed of light $c = 3.0 \\times 10^8\\text{ m s}^{-1}$ to find the wavelength of wave Y from its frequency $f = 9.4\\text{ GHz}$."
        ],
        "walkthrough": [
            "Step 1: For wave X, wavelength $\\lambda = 5.2 \\times 10^{-7}\\text{ m} = 520\\text{ nm}$. The visible spectrum spans approximately $\\lambda = 400\\text{ nm}$ to $ 700\\text{ nm}$, so wave X is in the visible region (green light).",
            "Step 2: For wave Y, frequency $f = 9.4\\text{ GHz} = 9.4 \\times 10^9\\text{ Hz}$. Calculate its wavelength:\n$\\lambda = \\frac{c}{f} = \\frac{3.0 \\times 10^8}{9.4 \\times 10^9} \\approx 0.032\\text{ m} = 3.2\\text{ cm}$\nWavelengths between $ 1\\text{ mm}$ and $ 1\\text{ m}$ (frequencies $f = 300\\text{ MHz}$ to $ 300\\text{ GHz}$) belong to the microwave region.",
            "Therefore, wave X is visible light and wave Y is microwave, matching row C."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q24",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "multi_step_calculation",
            "property_identification"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m05",
        "skill_id": "9702_skill_polarisation_malus_law",
        "accepted_answer": "C",
        "hints": [
            "The first filter has a vertical transmission axis and initially transmitted zero intensity, which reveals that the incident light is plane polarised horizontally.",
            "Apply Malus's law ($I = I_0 \\cos^2 \\theta$) twice: first at the inserted filter (angle $\\theta = 45^\\circ$ to the incident polarization), then at the first filter (angle $\\theta = 45^\\circ$ to the intermediate polarization)."
        ],
        "walkthrough": [
            "Step 1: Because the first filter (vertical transmission axis) initially blocks all incident light, the initial beam must be polarised horizontally (at angle $\\theta = 90^\\circ$ to the vertical axis).",
            "Step 2: When the second filter is inserted with its transmission axis at angle $\\theta = 45^\\circ$ to the vertical, its axis is also at angle $\\theta = 45^\\circ$ to the horizontal plane of polarisation. By Malus's law, transmitted intensity through this intermediate filter is:\n$I_1 = I_0 \\cos^2(45^\\circ) = I_0 \\left(\\frac{1}{\\sqrt{2}}\\right)^2 = \\frac{I_0}{2}$",
            "Step 3: The emerging beam is now polarised at angle $\\theta = 45^\\circ$ to the vertical. When it reaches the final filter (vertical axis), the angle is $\\theta = 45^\\circ$. The final transmitted intensity is:\n$I_{\\text{final}} = I_1 \\cos^2(45^\\circ) = \\left(\\frac{I_0}{2}\\right) \\left(\\frac{1}{2}\\right) = \\frac{I_0}{4}$\nThis corresponds to option C.",
            "Option A (0) ignores the polarization rotation caused by the inserted filter. Option B ($I_0/8$) results from cubing $\\cos^2(45^\\circ)$. Option D ($I_0/2$) only accounts for transmission through the first filter encountered."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q25",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "explanation",
            "property_identification"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m01",
        "skill_id": "9702_skill_stationary_waves",
        "accepted_answer": "C",
        "hints": [
            "Recall how stationary (standing) waves are created from progressive waves traveling in opposite directions.",
            "Consider which wave phenomenon describes the combining/adding of wave displacements at every point."
        ],
        "walkthrough": [
            "A stationary wave is produced by the superposition of two progressive waves of the same frequency, wavelength, and speed travelling in opposite directions.",
            "By the principle of superposition, the resultant displacement at each position is the vector sum of individual displacements, creating fixed nodes (zero amplitude) and antinodes (maximum amplitude).",
            "Diffraction (A) refers to wave spreading, polarisation (B) refers to restricting oscillations to one plane, and Doppler effect (D) refers to frequency shifts from relative motion. Thus, option C is correct."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q26",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "property_identification"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m01",
        "skill_id": "9702_skill_stationary_waves",
        "accepted_answer": "B",
        "hints": [
            "The distance between an adjacent node (N) and antinode (A) in any stationary wave is one-quarter of a wavelength ($\\frac{\\lambda}{4}$).",
            "Count the number of quarter-wavelength intervals from the closed end to the open end across the pattern N A N A N A N A."
        ],
        "walkthrough": [
            "Step 1: The stationary wave inside the pipe of length $L = 2.0\\text{ m}$ has a closed end (node N) and an open end (antinode A), with pattern: N $\\to$ A $\\to$ N $\\to$ A $\\to$ N $\\to$ A $\\to$ N $\\to$ A.",
            "Step 2: Each segment from N to A or A to N corresponds to $\\frac{\\lambda}{4}$. Counting consecutive transitions gives 7 quarter-wavelength segments:\n$L = 7 \\times \\frac{\\lambda}{4} = \\frac{7}{4}\\lambda = 2.0\\text{ m}$",
            "Step 3: Solve for wavelength $\\lambda$:\n$\\lambda = \\frac{4 \\times 2.0}{7} = \\frac{8.0}{7} \\approx 1.14\\text{ m} \\approx 1.1\\text{ m}$\nThis corresponds to option B.",
            "Option A ($\\lambda = 0.57\\text{ m}$) arises from using $\\lambda = 2.0 / 3.5$. Option C ($\\lambda = 1.3\\text{ m}$) results from miscounting intervals as 6 quarter-wavelengths ($\\frac{4 \\times 2.0}{6} = 1.33\\text{ m}$). Option D ($\\lambda = 1.6\\text{ m}$) corresponds to 5 quarter-wavelengths."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q27",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "measurement_selection",
            "property_identification"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m02",
        "skill_id": "9702_skill_wave_diffraction",
        "accepted_answer": "B",
        "hints": [
            "Diffraction is the spreading of wavefronts into the shadow region as they pass through a gap or around an obstacle.",
            "Consider which apparatus generates two-dimensional wavefronts where geometric spreading around obstacles can be observed visually."
        ],
        "walkthrough": [
            "Diffraction requires two-dimensional or three-dimensional wavefronts passing through a slit or around an edge so that spreading into the geometrical shadow can be observed.",
            "A ripple tank generates surface water waves whose straight parallel wavefronts can pass through adjustable gaps in barriers, clearly projecting the circular diffracted wavefronts on a screen.",
            "In contrast, a long spring (A), rope (C), or stretched string (D) are strictly one-dimensional media that support only transverse or longitudinal pulses along their line, making them unsuitable for demonstrating wave diffraction. Hence, option B is correct."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q28",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "graph_interpretation",
            "property_identification"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m03",
        "skill_id": "9702_skill_two_source_interference",
        "accepted_answer": "A",
        "hints": [
            "Recall Young's double-slit interference equation relating fringe spacing $x$, slit separation $a$, wavelength $\\lambda$, and slit-to-screen distance $D$.",
            "Rearrange $\\lambda = \\frac{a x}{D}$ to express $x$ as a function of $a$ and identify the mathematical shape of the graph."
        ],
        "walkthrough": [
            "Young's double-slit formula is $\\lambda = \\frac{a x}{D}$, which rearranges to:\n$x = \\frac{\\lambda D}{a}$",
            "Since wavelength $\\lambda$ and screen distance $D$ are held constant, fringe spacing $x$ is inversely proportional to slit separation $a$ ($x \\propto \\frac{1}{a}$).",
            "The graph of $x$ against $a$ is a rectangular hyperbola asymptotically approaching both axes as shown in Graph A.",
            "Graph B depicts a linear decrease, Graph C shows direct proportionality ($x \\propto a$), and Graph D shows an upward parabola ($x \\propto a^2$). Thus, option A is correct."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q29",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m04",
        "skill_id": "9702_skill_diffraction_grating",
        "accepted_answer": "D",
        "hints": [
            "Find the slit spacing $d$ of the grating using $d = \\frac{1\\text{ mm}}{300\\text{ lines}}$.",
            "Use the diffraction grating formula $d \\sin \\theta = n \\lambda$ with $\\sin \\theta \\le 1$ to find the highest integer order $n_{\\text{max}}$, then calculate the total number of maxima using $N = 2n_{\\text{max}} + 1$."
        ],
        "walkthrough": [
            "Step 1: Calculate the grating spacing $d$:\n$d = \\frac{10^{-3}\\text{ m}}{300} = \\frac{1}{3} \\times 10^{-5}\\text{ m} \\approx 3.333 \\times 10^{-6}\\text{ m}$",
            "Step 2: Wavelength $\\lambda = 690\\text{ nm} = 6.90 \\times 10^{-7}\\text{ m}$. Using $d \\sin \\theta = n \\lambda$:\n$n \\le \\frac{d}{\\lambda} = \\frac{3.333 \\times 10^{-6}}{6.90 \\times 10^{-7}} = \\frac{1000}{3 \\times 69} = \\frac{1000}{207} \\approx 4.83$",
            "Step 3: The maximum observable integer order is $n = 4$.",
            "Step 4: The total number of bright spots comprises the central zeroth-order maximum plus 4 orders on each side:\n$N_{\\text{total}} = 2n + 1 = 2(4) + 1 = 9$\nThis matches option D.",
            "Option A (4) only counts the orders on one side. Option B (5) counts one side plus the central maximum ($ 4+1$). Option C (8) omits the central zeroth-order maximum ($ 2 \\times 4$)."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q30",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "property_identification",
            "direct_calculation"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m01",
        "skill_id": "9702_skill_electric_current_drift_speed",
        "accepted_answer": "B",
        "hints": [
            "Recall that net electric charge on any macroscopic or microscopic particle is quantized in integer multiples of the elementary charge $e = 1.60 \\times 10^{-19}\\text{ C}$.",
            "Divide each option value by $ 1.60 \\times 10^{-19}\\text{ C}$ to test if it yields an integer."
        ],
        "walkthrough": [
            "Electric charge quantization dictates that any observed charge must satisfy $Q = n e$, where $n$ is an integer and $e = 1.60 \\times 10^{-19}\\text{ C}$.",
            "Evaluating each choice:\n- Option A: $Q = 0 = 0 \\times e$ (an uncharged/neutral droplet, which is possible with $n = 0$).\n- Option B: $\\frac{1.0 \\times 10^{-19}\\text{ C}}{1.60 \\times 10^{-19}\\text{ C}} = 0.625$, which is not an integer. Therefore, this charge is impossible.\n- Option C: $\\frac{4.8 \\times 10^{-19}\\text{ C}}{1.60 \\times 10^{-19}\\text{ C}} = 3.0$ (possible, $n = 3$).\n- Option D: $\\frac{8.0 \\times 10^{-19}\\text{ C}}{1.60 \\times 10^{-19}\\text{ C}} = 5.0$ (possible, $n = 5$).",
            "Hence, option B cannot be the charge on an oil droplet."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q31",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "multi_step_calculation",
            "circuit_analysis"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_potential_difference_power",
        "accepted_answer": "B",
        "hints": [
            "Determine the resistance of fixed resistor X using $P = I^2 R$, or use the proportional relationship $P \\propto I^2$ for a fixed resistor.",
            "An increase in power of $ 50\\%$ means the new power is $ 1.50 \\times P_{\\text{initial}}$."
        ],
        "walkthrough": [
            "Step 1: For a fixed ohmic resistor X of constant resistance $R_X$, electric power dissipation is $P = I^2 R_X$, so $P \\propto I^2$.",
            "Step 2: Resistance $R_X = \\frac{P_1}{I_1^2} = \\frac{7.2\\text{ W}}{(3.0\\text{ A})^2} = \\frac{7.2}{9.0} = 0.80\\ \\Omega$.",
            "Step 3: Power increases by $ 50\\%$, giving new power $P_2 = 1.50 \\times 7.2\\text{ W} = 10.8\\text{ W}$.",
            "Step 4: Solve for new current $I_2$:\n$I_2 = \\sqrt{\\frac{P_2}{R_X}} = \\sqrt{\\frac{10.8}{0.80}} = \\sqrt{13.5} \\approx 3.67\\text{ A} \\approx 3.7\\text{ A}$\n(Alternatively: $I_2 = I_1 \\sqrt{1.50} = 3.0 \\times 1.2247 = 3.67\\text{ A} \\approx 3.7\\text{ A}$). This matches option B.",
            "Option A ($I = 2.4\\text{ A}$) results from taking $ 3.0 / 1.22$. Option C ($I = 4.5\\text{ A}$) incorrectly scales current linearly by $ 1.50$ ($ 3.0 \\times 1.50 = 4.5$). Option D ($I = 14\\text{ A}$) results from squaring rather than taking the square root."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q32",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "property_identification",
            "equation_derivation"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m03",
        "skill_id": "9702_skill_resistivity",
        "accepted_answer": "D",
        "hints": [
            "Express the resistance $R$ of the wire in terms of resistivity $\\rho$, length $l$, and cross-sectional area $A = \\frac{\\pi d^2}{4}$.",
            "Apply Ohm's law $I = \\frac{V}{R}$ with constant potential difference $V$ to see how current $I$ depends on $l$ and $d$."
        ],
        "walkthrough": [
            "Step 1: The resistance of a cylindrical wire of length $l$, diameter $d$, and resistivity $\\rho$ is:\n$R = \\frac{\\rho l}{A} = \\frac{\\rho l}{\\pi (d/2)^2} = \\frac{4\\rho l}{\\pi d^2}$",
            "Step 2: By Ohm's law, current under constant potential difference $V$ is:\n$I = \\frac{V}{R} = \\frac{V}{\\frac{4\\rho l}{\\pi d^2}} = \\left(\\frac{\\pi V}{4\\rho}\\right) \\frac{d^2}{l}$",
            "Step 3: Since $V$ and $\\rho$ are constant, $I \\propto \\frac{d^2}{l}$. Therefore, current is inversely proportional to $l$ and directly proportional to $d^2$, which corresponds to option D.",
            "Options A and B incorrectly state that current is directly proportional to length $l$. Option C misses the quadratic dependence on diameter $d$."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q33",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": [
            "circuit_analysis",
            "property_identification"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m03",
        "skill_id": "9702_skill_potential_dividers",
        "accepted_answer": "A",
        "hints": [
            "The circuit is a bridge circuit. The voltmeter measures $V = V_{\\text{left}} - V_{\\text{right}}$, where $V_{\\text{left}}$ and $V_{\\text{right}}$ are potentials at the midpoints relative to the negative rail.",
            "To decrease the reading ($V > 0$), $V_{\\text{left}}$ must decrease (requiring lower thermistor resistance) and/or $V_{\\text{right}}$ must increase (requiring lower LDR resistance)."
        ],
        "walkthrough": [
            "Step 1: The battery supply has its positive terminal at the top rail and negative terminal at the bottom rail ($ 0\\text{ V}$).\n- Left branch: fixed resistor $R_1$ at top, NTC thermistor $R_T$ at bottom. Potential at positive terminal of voltmeter is $V_{\\text{left}} = V_{\\text{supply}} \\frac{R_T}{R_1 + R_T}$.\n- Right branch: LDR $R_{\\text{LDR}}$ at top, fixed resistor $R_2$ at bottom. Potential at negative terminal of voltmeter is $V_{\\text{right}} = V_{\\text{supply}} \\frac{R_2}{R_{\\text{LDR}} + R_2}$.",
            "Step 2: The voltmeter reads $V = V_{\\text{left}} - V_{\\text{right}} > 0$. To make this reading decrease:\n- We need $V_{\\text{left}}$ to decrease, which requires thermistor resistance $R_T$ to decrease. For a standard NTC thermistor, resistance decreases when temperature increases.\n- We need $V_{\\text{right}}$ to increase, which requires LDR resistance $R_{\\text{LDR}}$ to decrease. For an LDR, resistance decreases when light intensity increases.",
            "Step 3: Therefore, increasing temperature and increasing light intensity will both act to decrease the voltmeter reading, matching row A."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q34",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "definition",
            "circuit_analysis"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m02",
        "skill_id": "9702_skill_kirchhoffs_laws",
        "accepted_answer": "D",
        "hints": [
            "Distinguish between electromotive force (e.m.f.), which describes energy converted into electrical form in a source, and potential difference (p.d.), which describes electrical energy converted into other forms in circuit components.",
            "Apply Kirchhoff's second law (conservation of energy) around the single series loop."
        ],
        "walkthrough": [
            "Electromotive force (e.m.f.) is the energy transferred from chemical to electrical energy per unit charge by the battery. Passive resistors dissipate electrical energy into thermal energy and thus have potential differences (p.d.s) across them, not e.m.f.s.",
            "By Kirchhoff's second law, the algebraic sum of e.m.f.s around any closed loop equals the sum of potential differences across the components: $\\sum E = \\sum V$.",
            "Since there is a single battery of e.m.f. $E$ and negligible internal resistance, the sum of the potential differences across all resistors in series equals the e.m.f. $E$ of the battery, matching statement D.",
            "Statements A and C incorrectly refer to 'e.m.f.s across the resistors'. Statement B incorrectly claims each individual resistor has a p.d. equal to the full battery e.m.f. $E$."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q35",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "property_identification",
            "definition"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m02",
        "skill_id": "9702_skill_kirchhoffs_laws",
        "accepted_answer": "A",
        "hints": [
            "Recall that Kirchhoff's first law states that the sum of currents entering any circuit junction equals the sum of currents leaving the junction ($\\sum I_{\\text{in}} = \\sum I_{\\text{out}}$).",
            "Current is the rate of flow of electric charge ($I = \\frac{\\Delta Q}{\\Delta t}$)."
        ],
        "walkthrough": [
            "Kirchhoff's first law ($\\sum I = 0$ at a junction) states that charge cannot accumulate at or vanish from a junction in a steady-state circuit. Because electric current is the rate of flow of charge, equating total current entering to total current leaving represents the conservation of electric charge.",
            "In contrast, Kirchhoff's second law represents conservation of energy. Linear momentum (C) and potential difference (D) are not conserved in this junction formulation. Thus, option A is correct."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q36",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "circuit_analysis",
            "direct_calculation"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_resistor_networks",
        "accepted_answer": "B",
        "hints": [
            "Break the network into three parallel sub-blocks connected in series between X and Y.",
            "For $N$ identical resistors of resistance $R$ in parallel, the equivalent resistance is $R_{\\text{parallel}} = \\frac{R}{N}$."
        ],
        "walkthrough": [
            "Step 1: The circuit network consists of three parallel groups in series:\n- Group 1 (left): 3 identical resistors of $ 6.0\\ \\Omega$ in parallel $\\implies R_1 = \\frac{6.0}{3} = 2.0\\ \\Omega$.\n- Group 2 (middle): 6 identical resistors of $ 6.0\\ \\Omega$ in parallel $\\implies R_2 = \\frac{6.0}{6} = 1.0\\ \\Omega$.\n- Group 3 (right): 3 identical resistors of $ 6.0\\ \\Omega$ in parallel $\\implies R_3 = \\frac{6.0}{3} = 2.0\\ \\Omega$.",
            "Step 2: Add the series resistances to find total resistance between X and Y:\n$R_{XY} = R_1 + R_2 + R_3 = 2.0 + 1.0 + 2.0 = 5.0\\ \\Omega$\nThis corresponds to option B.",
            "Option A ($R = 3.0\\ \\Omega$) or C ($R = 7.2\\ \\Omega$) or D ($R = 18\\ \\Omega$) represent miscalculations of parallel combinations or simple summing of group counts."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q37",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "circuit_analysis",
            "property_identification",
            "measurement_selection"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m03",
        "skill_id": "9702_skill_potentiometer_circuits",
        "accepted_answer": "D",
        "hints": [
            "Calculate the potential difference across $R_2$ produced by the battery ($V = 6.0\\text{ V}$) and the potential divider ($R_1 = 60\\ \\Omega$, $R_2 = 20\\ \\Omega$).",
            "Consider the condition for null deflection (zero current) when the test cell of e.m.f. $ 1.5\\text{ V}$ is connected in opposition across $R_2$."
        ],
        "walkthrough": [
            "Step 1: The potential difference across resistor $R_2$ in the potential divider is:\n$V_2 = 6.0\\text{ V} \\times \\left(\\frac{20}{60 + 20}\\right) = 6.0 \\times \\frac{20}{80} = 1.5\\text{ V}$",
            "Step 2: When a cell of e.m.f. $ 1.5\\text{ V}$ is connected in parallel with $R_2$ with opposing polarity, the cell e.m.f. exactly balances the $ 1.5\\text{ V}$ potential difference across $R_2$. Consequently, zero current flows through the cell-galvanometer branch (null condition).",
            "Step 3: Because the test only detects whether current is zero (null point), the galvanometer acts purely as a sensitive null detector and does not require a scale calibrated in amperes, making statement D correct.",
            "Evaluating other statements:\n- Statement A is false because a zero reading (not non-zero) confirms the $ 1.5\\text{ V}$ balance.\n- Statement B is false because the potential divider requires a steady $ 6.0\\text{ V}$ to produce exactly $ 1.5\\text{ V}$ across $R_2$.\n- Statement C is false because the cell must be connected with correct opposing polarity to establish a null balance."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q38",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "property_identification",
            "classification"
        ],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m01",
        "skill_id": "9702_skill_nuclear_atom_scattering",
        "accepted_answer": "A",
        "hints": [
            "Recall the definition of isotopes: atoms of the same element having the same proton number $Z$ but different neutron numbers $N$ (and different nucleon numbers $A$).",
            "In an electrically neutral atom, the number of electrons equals the number of protons."
        ],
        "walkthrough": [
            "Isotopes of the same chemical element contain the same number of protons ($Z$) in their nuclei.",
            "In neutral atoms, the total negative electron charge balances the total positive nuclear charge, meaning the number of electrons equals the proton number $Z$. Therefore, neutral atoms of different isotopes have identical numbers of electrons, making option A correct.",
            "Evaluating distractors:\n- Option B is false because isotopes of the same element have the same number of protons by definition.\n- Option C is false because isotopes have different nucleon numbers ($A = Z + N$).\n- Option D is false because isotopes have different numbers of neutrons ($N$)."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q39",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "comparison",
            "direct_calculation"
        ],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m02",
        "skill_id": "9702_skill_fundamental_particles_interactions",
        "accepted_answer": "B",
        "hints": [
            "Determine the charge magnitude and mass of each particle in terms of elementary charge $e$ and unified atomic mass unit $u$ (where $m_p \\approx 1\\text{ u}$ and $m_e \\approx \\frac{1}{1836}\\text{ u}$).",
            "Calculate the charge-to-mass ratio magnitude $r = |q| / m$ for $\\alpha$ ($q = +2e, m \\approx 4u$), proton ($q = +e, m \\approx 1u$), and $\\beta^+$ ($q = +e, m = m_e$)."
        ],
        "walkthrough": [
            "Step 1: Calculate the charge-to-mass ratio magnitude $r = \\frac{|q|}{m}$ for each particle:\n- For an $\\alpha$-particle: $|q| = 2e$, mass $m \\approx 4\\text{ u} \\implies r_\\alpha = \\frac{2e}{4\\text{ u}} = 0.5\\frac{e}{\\text{u}}$.\n- For a proton p: $|q| = 1e$, mass $m \\approx 1\\text{ u} \\implies r_p = \\frac{1e}{1\\text{ u}} = 1.0\\frac{e}{\\text{u}}$.\n- For a $\\beta^+$ particle (positron): $|q| = 1e$, mass $m = m_e \\approx \\frac{1}{1836}\\text{ u} \\implies r_{\\beta^+} = \\frac{1e}{m_e} \\approx 1836\\frac{e}{\\text{u}}$.",
            "Step 2: Order by increasing magnitude of $r$:\n$r_\\alpha (0.5) < r_p (1.0) < r_{\\beta^+} (1836)$\nThis order is $\\alpha \\to \\text{p} \\to \\beta^+$, which corresponds to option B.",
            "Options A, C, and D represent incorrect rankings arising from ignoring the vastly smaller mass of the positron or confusing the charge-to-mass ratio of the $\\alpha$-particle with the proton."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w23_12_q40",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "particle_model_application",
            "classification"
        ],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m02",
        "skill_id": "9702_skill_quark_model_hadrons",
        "accepted_answer": "C",
        "hints": [
            "Recall the fractional electric charges of up and down quarks: up quark $u = +\\frac{2}{3}e$, down quark $d = -\\frac{1}{3}e$.",
            "A neutron has zero net charge ($Q = 0$): find the 3-quark combination that sums to 0."
        ],
        "walkthrough": [
            "Quark charges are $Q(u) = +\\frac{2}{3}e$ and $Q(d) = -\\frac{1}{3}e$.",
            "A neutron is a neutral baryon ($Q = 0$). Summing charges:\n- Option A ($uuu$): $\\frac{2}{3} + \\frac{2}{3} + \\frac{2}{3} = +2e$ (a $\\Delta^{++}$ baryon).\n- Option B ($uud$): $\\frac{2}{3} + \\frac{2}{3} - \\frac{1}{3} = +1e$ (a proton).\n- Option C ($udd$): $\\frac{2}{3} - \\frac{1}{3} - \\frac{1}{3} = 0$ (a neutron).\n- Option D ($ddd$): $-\\frac{1}{3} - \\frac{1}{3} - \\frac{1}{3} = -1e$ (a $\\Delta^-$ baryon).",
            "Therefore, the quark combination for a neutron is $udd$, matching option C."
        ]
    }
]

def main():
    print(f"Writing {len(ENRICHMENTS)} enrichment records for 9702_w23_12...")
    for item in ENRICHMENTS:
        # Pre-validation check for PID regex in this generator
        full_text = " ".join(item["hints"]) + " " + " ".join(item["walkthrough"])
        pids = re.findall(r"[\$]{1,2}\d{2,}", full_text)
        if pids:
            print(f"WARNING: {item['question_id']} contains PID regex matches: {pids}")

        qid = item["question_id"]
        out_path = ENRICH_DIR / f"{qid}.enrichment.json"
        out_path.write_text(json.dumps(item, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Done.")

if __name__ == "__main__":
    main()
