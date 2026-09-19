"""
generate_9702_s18_13.py

Generates P1 enrichment files for Cambridge AS Level Physics 9702 paper 9702_s18_13 (Q01-Q40).
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "subjects/physics/9702/enrichment/p1"
OUT_DIR.mkdir(parents=True, exist_ok=True)

data = [
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q01",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "definition",
      "property_identification"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m01",
    "skill_id": "9702_skill_identify_scalar_vector_common_properties",
    "accepted_answer": "B",
    "hints": [
      "Recall the standard definition of a physical quantity in physics.",
      "Consider what two fundamental components are essential to quantify any physical measurement (such as 5.0 kg or 12 m s^{-1}), whether scalar or vector."
    ],
    "walkthrough": [
      "A physical quantity is defined as a property of an object or phenomenon that can be quantified by measurement, consisting of a numerical magnitude and a unit.",
      "While vector quantities additionally include a specified direction, every physical quantity—both scalar and vector—fundamentally possesses a magnitude and an associated unit, corresponding to option B.",
      "Option A is incorrect because physical quantities require units. Option C describes only scalar quantities and excludes vectors. Option D is incorrect because a physical quantity must possess a numerical magnitude."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q02",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "classification",
      "property_identification"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m04",
    "skill_id": "9702_skill_classify_scalars_vectors",
    "accepted_answer": "B",
    "hints": [
      "Recall the distinction between scalar quantities (magnitude only) and vector quantities (magnitude and direction).",
      "Classify each quantity in the pairs: displacement, acceleration, force, kinetic energy, power, speed, work, and potential energy."
    ],
    "walkthrough": [
      "A vector quantity requires both magnitude and direction, whereas a scalar quantity is completely specified by its magnitude and unit.",
      "Evaluating the given pairs: In option B, force is a vector quantity (requiring direction) and kinetic energy is a scalar quantity (energy has no spatial direction). Thus, option B contains one vector and one scalar.",
      "Option A contains two vectors (displacement and acceleration). Option C contains two scalars (power and speed). Option D contains two scalars (work and potential energy)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q03",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "vector_diagram_construction",
      "equation_derivation"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m04",
    "skill_id": "9702_skill_resolve_force_components",
    "accepted_answer": "A",
    "hints": [
      "Resolve the force vector $F$ into components along the horizontal and vertical axes using right-angled trigonometry.",
      "Use trigonometric identities to relate $\\sin\\theta$ to $\\cos(90^\\circ - \\theta)$."
    ],
    "walkthrough": [
      "For a force $F$ acting at an angle $\\theta$ to the horizontal, the horizontal component adjacent to the angle is $F_x = F \\cos\\theta$.",
      "The vertical component opposite the angle is $F_y = F \\sin\\theta$. Using the complementary angle identity $\\sin\\theta = \\cos(90^\\circ - \\theta)$, the vertical component can be expressed as $F \\cos(90^\\circ - \\theta)$, matching option A.",
      "Option B gives a vertical component of $F \\sin(90^\\circ - \\theta) = F \\cos\\theta$, which is the horizontal component. Options C and D incorrectly use $F \\sin\\theta$ for the horizontal component."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q04",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "explanation",
      "property_identification"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m03",
    "skill_id": "9702_skill_identify_systematic_error_sources",
    "accepted_answer": "A",
    "hints": [
      "Distinguish between systematic errors (which cause readings to deviate from the true value by a consistent amount in the same direction) and random errors (which cause unpredictable fluctuations).",
      "Consider which technique corrects a fixed instrument offset or zero error directly rather than averaging out random fluctuations."
    ],
    "walkthrough": [
      "Systematic errors arise from experimental flaws or instrument calibration offsets (such as zero error) that consistently bias measurements in one direction.",
      "Adjusting the needle of a voltmeter to read zero when no potential difference is applied removes a zero error, directly eliminating a systematic error (option A).",
      "Options B and D (repeating and averaging measurements, or timing multiple oscillations) reduce the impact of random uncertainties. Option C reduces parallax error, but zero-point calibration in option A is the standard method for eliminating a systematic instrument offset."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q05",
    "component": "P1",
    "difficulty": 3,
    "question_patterns": [
      "uncertainty_analysis",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m03",
    "skill_id": "9702_skill_combine_percentage_uncertainties",
    "accepted_answer": "D",
    "hints": [
      "Apply the rules for combining fractional or percentage uncertainties for products, quotients, and powers using the formula $E = \\frac{4 m g l}{\\pi d^2 e}$.",
      "Calculate $\\frac{\\Delta E}{E} = \\frac{\\Delta m}{m} + \\frac{\\Delta l}{l} + 2\\frac{\\Delta d}{d} + \\frac{\\Delta e}{e}$, then multiply by the calculated value $E = 1.61 \\times 10^{10}\\text{ N m}^{-2}$."
    ],
    "walkthrough": [
      "From the Young modulus formula $E = \\frac{4 m g l}{\\pi d^2 e}$, the total fractional uncertainty is $\\frac{\\Delta E}{E} = \\frac{\\Delta m}{m} + \\frac{\\Delta l}{l} + 2\\left(\\frac{\\Delta d}{d}\\right) + \\frac{\\Delta e}{e}$.",
      "Calculate the individual fractional uncertainties: $\\frac{\\Delta m}{m} = \\frac{0.002}{2.300} \\approx 0.00087$, $\\frac{\\Delta l}{l} = \\frac{0.005}{2.864} \\approx 0.00175$, $2\\frac{\\Delta d}{d} = 2 \\times \\frac{0.01}{0.82} \\approx 0.02439$, and $\\frac{\\Delta e}{e} = \\frac{0.2}{7.6} \\approx 0.02632$.",
      "Summing these gives $\\frac{\\Delta E}{E} \\approx 0.00087 + 0.00175 + 0.02439 + 0.02632 = 0.05333$ (or 5.33%).",
      "The absolute uncertainty is $\\Delta E = 0.05333 \\times 1.61 \\times 10^{10}\\text{ N m}^{-2} \\approx 0.086 \\times 10^{10}\\text{ N m}^{-2} \\approx 0.09 \\times 10^{10}\\text{ N m}^{-2}$. Thus $E = (1.61 \\pm 0.09) \\times 10^{10}\\text{ N m}^{-2}$, matching option D.",
      "Options A, B, and C underestimate the total uncertainty, typically by forgetting the factor of 2 on the diameter term or omitting one of the fractional uncertainty components."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q06",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "equation_recall"
    ],
    "topic_id": "9702_t02",
    "module_id": "9702_t02_m01",
    "skill_id": "9702_skill_apply_constant_acceleration",
    "accepted_answer": "B",
    "hints": [
      "Select the constant acceleration equation relating initial velocity $u$, final velocity $v$ at the maximum height, displacement $h$, and acceleration $g$.",
      "Substitute $u = 9.4\\text{ m s}^{-1}$, $v = 0\\text{ m s}^{-1}$, and $h = 12\\text{ m}$ into $v^2 = u^2 - 2gh$."
    ],
    "walkthrough": [
      "At maximum height $h = 12\\text{ m}$, the vertical velocity of the rock momentarily becomes $v = 0\\text{ m s}^{-1}$.",
      "Using the kinematic equation $v^2 = u^2 - 2gh$, we have $0 = (9.4)^2 - 2g(12) = 88.36 - 24g$.",
      "Solving for $g$ yields $g = \\frac{88.36}{24} \\approx 3.68\\text{ m s}^{-2} \\approx 3.7\\text{ m s}^{-2}$, which corresponds to option B.",
      "Option A ($g = 0.39\\text{ m s}^{-2}$) results from dividing 9.4 by 24. Option C ($g = 7.4\\text{ m s}^{-2}$) omits the factor of 2 in the denominator ($9.4^2 / 12$). Option D ($g = 9.8\\text{ m s}^{-2}$) is Earth gravitational acceleration."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q07",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "equation_derivation",
      "comparison"
    ],
    "topic_id": "9702_t03",
    "module_id": "9702_t03_m01",
    "skill_id": "9702_skill_balance_collinear_forces_with_resultant",
    "accepted_answer": "C",
    "hints": [
      "Resolve the weight of mass $M$ into components parallel and perpendicular to the slope.",
      "For mass $M$ to accelerate down the slope, compare the parallel downward force component $M g \\sin\\theta$ with the upward tension provided by mass $m$."
    ],
    "walkthrough": [
      "The component of the weight of mass $M$ acting down the frictionless slope is $W_{\\parallel} = M g \\sin\\theta$.",
      "For mass $M$ to accelerate down the slope and lift mass $m$, the downward driving force along the string must exceed the opposing weight of mass $m$: $M g \\sin\\theta > m g$.",
      "Dividing both sides by $M g$ gives $\\sin\\theta > \\frac{m}{M}$, which matches option C.",
      "Option A ($\\sin\\theta < m/M$) would cause mass $M$ to move up the slope. Options B and D incorrectly use $\\cos\\theta$ rather than $\\sin\\theta$ for the component of weight parallel to the incline."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q08",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "explanation"
    ],
    "topic_id": "9702_t03",
    "module_id": "9702_t03_m02",
    "skill_id": "9702_skill_analyse_resistive_force_motion",
    "accepted_answer": "B",
    "hints": [
      "Recall that the gradient of a displacement-time graph ($s-t$) represents instantaneous velocity ($v = \\frac{ds}{dt}$).",
      "Consider how the velocity of the sky-diver changes: starting from rest ($v=0$), accelerating with increasing speed, and eventually reaching a constant terminal velocity when drag equals weight."
    ],
    "walkthrough": [
      "The gradient of the displacement-time graph represents the velocity of the sky-diver.",
      "At $t = 0$, the sky-diver is released from rest, so the initial gradient is zero. As she falls, downward acceleration increases her speed, meaning the gradient of the graph increases (curves upwards).",
      "As air resistance increases and balances her weight, the resultant force becomes zero and she reaches a constant terminal velocity. The displacement-time graph therefore transitions into a straight line of constant positive gradient, as shown in graph B.",
      "Graph A shows a decreasing gradient (deceleration). Graph C shows constant velocity from the start. Graph D shows a decreasing displacement curve."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q09",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "vector_diagram_construction",
      "direct_calculation"
    ],
    "topic_id": "9702_t03",
    "module_id": "9702_t03_m03",
    "skill_id": "9702_skill_apply_momentum_conservation",
    "accepted_answer": "C",
    "hints": [
      "Apply the principle of conservation of linear momentum independently in the $x$-direction and $y$-direction.",
      "Calculate $p_x = m_1 u_1$ and $p_y = m_2 u_2$, then use $\\tan\\theta = \\frac{p_y}{p_x}$ to find the trajectory angle relative to the $x$-direction."
    ],
    "walkthrough": [
      "Linear momentum is conserved in both perpendicular directions during the collision.",
      "Initial momentum along the $x$-direction: $p_x = (0.20\\text{ kg}) \\times (0.50\\text{ m s}^{-1}) = 0.10\\text{ kg m s}^{-1}$. Initial momentum along the $y$-direction: $p_y = (0.30\\text{ kg}) \\times (0.40\\text{ m s}^{-1}) = 0.12\\text{ kg m s}^{-1}$.",
      "After the collision, the combined mass moves with momentum components $P_x = 0.10\\text{ kg m s}^{-1}$ and $P_y = 0.12\\text{ kg m s}^{-1}$. The angle $\\theta$ to the $x$-direction is given by $\\tan\\theta = \\frac{P_y}{P_x} = \\frac{0.12}{0.10} = 1.20$.",
      "Calculating the angle gives $\\theta = \\arctan(1.20) \\approx 50.2^\\circ \\approx 50^\\circ$, matching option C.",
      "Option A (yielding angle $\\theta = 39^\\circ$) and Option B (yielding angle $\\theta = 40^\\circ$) result from calculating the angle relative to the $y$-direction ($\\arctan(0.10/0.12) \\approx 39.8^\\circ$)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q10",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "comparison",
      "property_identification"
    ],
    "topic_id": "9702_t04",
    "module_id": "9702_t04_m03",
    "skill_id": "9702_skill_apply_archimedes_principle",
    "accepted_answer": "A",
    "hints": [
      "Recall Archimedes principle: upthrust is equal to the weight of the fluid displaced by the submerged object.",
      "Check whether the volume of fluid displaced differs between the cuboids given that they have identical dimensions and are fully immersed."
    ],
    "walkthrough": [
      "Archimedes principle states that the upthrust $U$ acting on a submerged body equals the weight of the displaced liquid: $U = \\rho_{\\text{fluid}} V_{\\text{submerged}} g$.",
      "Since all four cuboids have identical dimensions and are completely immersed in water of density $\\rho$, each cuboid displaces exactly the same volume of water $V$. Therefore, the upthrust $U = \\rho V g$ is identical on all four cuboids, matching option A.",
      "Options B, C, and D confuse the upthrust with the gravitational force (weight) of the cuboids or the net resultant force on them."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q11",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t04",
    "module_id": "9702_t04_m03",
    "skill_id": "9702_skill_apply_pressure_force",
    "accepted_answer": "D",
    "hints": [
      "Recall that pressure is force per unit area ($P = \\frac{F}{A} = \\frac{W}{A}$). To maximize pressure, choose the face with the minimum contact area.",
      "Alternatively, use $P = \\rho g h$ and select the maximum vertical dimension of the block ($h = 15.0\\text{ cm} = 0.150\\text{ m}$)."
    ],
    "walkthrough": [
      "The pressure exerted by a solid block on a flat surface is $P = \\frac{W}{A} = \\frac{\\rho V g}{A} = \\rho g h$, where $h$ is the vertical height of the block.",
      "To obtain the maximum pressure, the block must rest on its smallest face (area  = 0.120\text{ m} \times 0.100\text{ m}$), giving maximum height  = 15.0\text{ cm} = 0.150\text{ m}$.",
      "Calculate maximum pressure: $P_{\\text{max}} = \\rho g h = (1.13 \\times 10^4\\text{ kg m}^{-3}) \\times (9.81\\text{ m s}^{-2}) \\times (0.150\\text{ m}) \\approx 16628\\text{ Pa} \\approx 16.6\\text{ kPa}$, matching option D.",
      "Option A ($P = 1.13\\text{ kPa}$) and Option B ($P = 1.70\\text{ kPa}$) result from power-of-ten conversion errors. Option C ($P = 11.1\\text{ kPa}$) corresponds to placing the block on its largest face ($h = 10.0\\text{ cm}$), giving minimum pressure."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q12",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "classification",
      "property_identification"
    ],
    "topic_id": "9702_t04",
    "module_id": "9702_t04_m01",
    "skill_id": "9702_skill_define_torque_of_couple",
    "accepted_answer": "D",
    "hints": [
      "Recall the physics definition of a couple: a pair of equal and opposite parallel forces that do not act along the same line of action.",
      "Examine the force vectors in each diagram for equal magnitude, opposite direction, and non-collinear lines of action."
    ],
    "walkthrough": [
      "A couple is defined as a pair of equal in magnitude, opposite in direction, parallel forces whose lines of action are separated by a perpendicular distance, creating a pure turning effect.",
      "In diagram D, both forces have magnitude $F$, act in opposite directions perpendicular to the rod, and are separated along the rod, forming a valid couple.",
      "Diagram A shows forces in the same direction (producing linear acceleration). Diagram B and Diagram C show forces acting along the same line of action or towards each other, which produce no net torque."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q13",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t04",
    "module_id": "9702_t04_m03",
    "skill_id": "9702_skill_apply_density",
    "accepted_answer": "B",
    "hints": [
      "Calculate the volume of fat-free milk (96.0% of total volume) and the volume of fat (4.00% of total volume).",
      "Determine the mass of fat-free milk from its density and volume, subtract this from the total mass to find the mass of fat, and divide by the fat volume."
    ],
    "walkthrough": [
      "Total volume $V = 1.000 \\times 10^{-3}\\text{ m}^3$. The volume of fat is $V_{\\text{fat}} = 0.0400 \\times 1.000 \\times 10^{-3} = 4.00 \\times 10^{-5}\\text{ m}^3$, and the volume of fat-free milk is $V_{\\text{milk}} = 0.960 \\times 1.000 \\times 10^{-3} = 9.60 \\times 10^{-4}\\text{ m}^3$.",
      "The mass of the fat-free milk is $m_{\\text{milk}} = \\rho_{\\text{milk}} \\times V_{\\text{milk}} = (1.040 \\times 10^3\\text{ kg m}^{-3}) \\times (9.60 \\times 10^{-4}\\text{ m}^3) = 0.9984\\text{ kg}$.",
      "The mass of fat is $m_{\\text{fat}} = m_{\\text{total}} - m_{\\text{milk}} = 1.035\\text{ kg} - 0.9984\\text{ kg} = 0.0366\\text{ kg}$.",
      "The density of fat is $\\rho_{\\text{fat}} = \\frac{m_{\\text{fat}}}{V_{\\text{fat}}} = \\frac{0.0366\\text{ kg}}{4.00 \\times 10^{-5}\\text{ m}^3} = 915\\text{ kg m}^{-3} = 9.15 \\times 10^2\\text{ kg m}^{-3}$, matching option B.",
      "Option A ($1.25 \\times 10^2\\text{ kg m}^{-3}$) and Option C ($9.28 \\times 10^2\\text{ kg m}^{-3}$) arise from arithmetic errors or misinterpreting mass fractions. Option D ($1.16 \\times 10^3\\text{ kg m}^{-3}$) exceeds the density of fat-free milk."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q14",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "equation_derivation",
      "definition"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m01",
    "skill_id": "9702_skill_define_work_done",
    "accepted_answer": "A",
    "hints": [
      "Recall that work done by a gas against an external constant pressure is given by $W = p_{\\text{ext}} \\Delta V$.",
      "Identify the change in volume $\\Delta V$ during the expansion from position P to position Q in terms of the piston area $A$ and distance moved $r$."
    ],
    "walkthrough": [
      "The work done against the atmosphere is defined as $W = F_{\\text{atm}} \\times \\Delta x$, where $F_{\\text{atm}} = p_{\\text{atm}} A$ is the opposing force exerted by atmospheric pressure.",
      "During the expansion from position P to position Q, the piston moves through distance $r$, so the change in volume against the atmosphere is $\\Delta V = A r$.",
      "Hence, the work done against the atmosphere is $W = (\\text{atmospheric pressure}) \\times A r$, which corresponds to option A.",
      "Options B and D incorrectly use the total column length $s$ rather than the expansion distance $r$. Options C and D use internal gas pressure, which includes work done overcoming piston friction."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q15",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m01",
    "skill_id": "9702_skill_apply_efficiency",
    "accepted_answer": "D",
    "hints": [
      "Calculate the input power from the gravitational potential energy delivered per second: $P_{\\text{in}} = \\frac{\\Delta m}{\\Delta t} g h$.",
      "Calculate the output electrical power using $P_{\\text{out}} = V I$, then determine efficiency as $\\eta = \\frac{P_{\\text{out}}}{P_{\\text{in}}} \\times 100\\%$."
    ],
    "walkthrough": [
      "The input power supplied by the falling water is $P_{\\text{in}} = \\left(\\frac{m}{t}\\right) g h = (510\\text{ kg s}^{-1}) \\times (9.81\\text{ m s}^{-2}) \\times (280\\text{ m}) \\approx 1.401 \\times 10^6\\text{ W} = 1.401\\text{ MW}$.",
      "The electrical output power generated is $P_{\\text{out}} = V I = (5800\\text{ V}) \\times (205\\text{ A}) = 1.189 \\times 10^6\\text{ W} = 1.189\\text{ MW}$.",
      "Efficiency is $\\eta = \\frac{P_{\\text{out}}}{P_{\\text{in}}} \\times 100\\% = \\frac{1.189 \\times 10^6}{1.401 \\times 10^6} \\times 100\\% \\approx 84.9\\% \\approx 85\\%$, matching option D.",
      "Option A (efficiency 8.3%) and Option B (efficiency 12%) result from inverted ratios or unit scale mismatches. Option C (efficiency 83%) results from using $g = 10\\text{ m s}^{-2}$ with inaccurate rounding."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q16",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "comparison",
      "property_identification"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m02",
    "skill_id": "9702_skill_compare_gravitational_potential_and_kinetic_energy",
    "accepted_answer": "B",
    "hints": [
      "Carefully note that the question asks for the statement that is NOT correct.",
      "Evaluate the gravitational potential energy at the midpoint ($h/2$) compared to the initial total kinetic energy at the launch position."
    ],
    "walkthrough": [
      "At the starting position ($h = 0$), the total mechanical energy is purely kinetic energy $E_{k,\\text{initial}}$. At maximum height $h$, all kinetic energy has been converted to gravitational potential energy: $E_{p,\\text{top}} = m g h$.",
      "At the midpoint of the path ($h/2$), the gravitational potential energy is $E_p = m g \\left(\\frac{h}{2}\\right) = \\frac{1}{2} m g h = \\frac{1}{2} E_{p,\\text{top}}$, which is half of the initial kinetic energy, not equal to it. Therefore, statement B is incorrect (false), making B the correct option.",
      "Statement A correctly states energy conversion from KE to GPE. Statement C is correct because the ball is instantaneously at rest at the top ($v=0$). Statement D is correct because work done against air resistance causes total mechanical energy to decrease over time."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q17",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m01",
    "skill_id": "9702_skill_apply_mechanical_power",
    "accepted_answer": "B",
    "hints": [
      "Find the total upward force required to lift both the hook and the load at constant velocity ($F_{\\text{total}} = F_{\\text{hook}} + m_{\\text{load}} g$).",
      "Calculate mechanical power using $P = F_{\\text{total}} v$ with $v = 0.50\\text{ m s}^{-1}$."
    ],
    "walkthrough": [
      "The weight of the load is $W_{\\text{load}} = m g = (1000\\text{ kg}) \\times (9.81\\text{ m s}^{-2}) = 9810\\text{ N}$.",
      "The total upward force required to lift both the hook (requiring $F_{\\text{hook}} = 1000\\text{ N}$) and the load at constant velocity is $F_{\\text{total}} = 1000\\text{ N} + 9810\\text{ N} = 10810\\text{ N}$.",
      "The power needed is $P = F_{\\text{total}} \\times v = (10810\\text{ N}) \\times (0.50\\text{ m s}^{-1}) = 5405\\text{ W} = 5.4\\text{ kW}$, matching option B.",
      "Option A ($P = 4.9\\text{ kW}$) neglects the force needed to lift the hook ($W_{\\text{load}} \\times v = 9810 \\times 0.50 = 4905\\text{ W}$). Options C and D result from dividing force by velocity ($F / v$) instead of multiplying."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q18",
    "component": "P1",
    "difficulty": 3,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t06",
    "module_id": "9702_t06_m01",
    "skill_id": "9702_skill_apply_young_modulus",
    "accepted_answer": "D",
    "hints": [
      "Determine the cross-sectional area $A = \\frac{\\pi d^2}{4}$ and tensile stress $\\sigma = \\frac{T}{A}$.",
      "Calculate the strain $\\varepsilon = \\frac{\\sigma}{E}$, which represents the fractional contraction $\\frac{\\Delta l}{l}$, and convert it to a percentage by multiplying by 100%."
    ],
    "walkthrough": [
      "The cross-sectional area of the wire is $A = \\frac{\\pi d^2}{4} = \\frac{\\pi (5.0 \\times 10^{-4}\\text{ m})^2}{4} \\approx 1.963 \\times 10^{-7}\\text{ m}^2$.",
      "The tensile stress in the wire under tension $T = 20\\text{ N}$ is $\\sigma = \\frac{T}{A} = \\frac{20\\text{ N}}{1.963 \\times 10^{-7}\\text{ m}^2} \\approx 1.019 \\times 10^8\\text{ Pa}$.",
      "The elastic strain is $\\varepsilon = \\frac{\\sigma}{E} = \\frac{1.019 \\times 10^8\\text{ Pa}}{2.0 \\times 10^{11}\\text{ Pa}} \\approx 5.09 \\times 10^{-4}$.",
      "The percentage contraction when the wire snaps is $\\varepsilon \\times 100\\% = 5.09 \\times 10^{-4} \\times 100\\% \\approx 5.1 \\times 10^{-2}\\%$, matching option D.",
      "Option C ($1.3 \\times 10^{-2}\\%$) results from using radius instead of diameter or omitting $\\pi/4$. Options A and B represent power-of-ten errors from failing to convert strain to percentage."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q19",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "direct_calculation"
    ],
    "topic_id": "9702_t06",
    "module_id": "9702_t06_m02",
    "skill_id": "9702_skill_apply_elastic_potential_energy",
    "accepted_answer": "C",
    "hints": [
      "Recall that strain energy stored in a stretched spring is represented by the area under the force-extension graph ($E_p = \\frac{1}{2} F x$).",
      "Carefully convert the axis units: extension $x = 4.0\\text{ cm} = 4.0 \\times 10^{-2}\\text{ m}$ and force $F = 30\\text{ kN} = 30 \\times 10^3\\text{ N}$."
    ],
    "walkthrough": [
      "The strain energy stored in the spring is given by the triangular area under the force-extension graph: $E_p = \\frac{1}{2} F x$.",
      "From the graph, at an extension of $x = 4.0\\text{ cm} = 0.040\\text{ m}$, the force is $F = 30\\text{ kN} = 30000\\text{ N}$.",
      "Calculate strain energy: $E_p = \\frac{1}{2} \\times (30000\\text{ N}) \\times (0.040\\text{ m}) = 600\\text{ J}$, which matches option C.",
      "Option D ($E_p = 1200\\text{ J}$) omits the factor of $\\frac{1}{2}$ ($F x$). Options A ($E_p = 60\\text{ J}$) and B ($E_p = 120\\text{ J}$) result from unit conversion errors in kilonewtons or centimetres."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q20",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "direct_calculation"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m01",
    "skill_id": "9702_skill_determine_phase_difference_from_wave_profile",
    "accepted_answer": "C",
    "hints": [
      "Find the spatial distance between point X (first crest) and point Y (second trough) in terms of wavelength $\\lambda$.",
      "Relate spatial separation $\\Delta x$ to phase difference $\\Delta \\phi$ using $\\Delta \\phi = \\frac{\\Delta x}{\\lambda} \\times 360^\\circ = \\frac{\\Delta x}{\\lambda} \\times 2 \\times 180^\\circ$."
    ],
    "walkthrough": [
      "On the displacement-distance graph, point X is located at the first wave crest ($x_X = 0.25\\lambda$) and point Y is located at the second wave trough ($x_Y = 1.75\\lambda$).",
      "The distance separating points X and Y is $\\Delta x = 1.75\\lambda - 0.25\\lambda = 1.5\\lambda$.",
      "The phase difference corresponding to a spatial separation of $\\Delta x$ is $\\Delta \\phi = \\left(\\frac{\\Delta x}{\\lambda}\\right) \\times 360^\\circ = 1.5 \\times 360^\\circ = 540^\\circ = (180 \\times 3.0)^\\circ$. Thus $n = 3.0$, matching option C.",
      "Option A ($n = 1.5$) represents the distance in wavelengths rather than multiplying by 2 for the 180-degree factor. Option B ($n = 2.5$) miscounts the number of half-cycles. Option D ($n = 6.0$) counts quarter-wavelengths incorrectly."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q21",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "property_identification"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m01",
    "skill_id": "9702_skill_read_wave_amplitude_from_displacement_graph",
    "accepted_answer": "D",
    "hints": [
      "Check the horizontal axis variable: a displacement-distance graph ($d-x$) shows wavelength $\\lambda$, while a displacement-time graph ($d-t$) shows period $T$.",
      "Verify that amplitude $a$ is defined as the maximum displacement from the equilibrium position (zero line to crest), not the peak-to-peak distance."
    ],
    "walkthrough": [
      "On a displacement-time ($d-t$) graph, the time between consecutive crests represents the wave period $T$, and the distance from the equilibrium line to a peak represents the amplitude $a$. Graph D correctly labels both quantities.",
      "Graph A incorrectly labels the peak-to-peak distance on a distance ($x$) axis as period $T$ instead of wavelength $\\lambda$.",
      "Graph B correctly labels wavelength $\\lambda$ on the distance axis, but incorrectly defines amplitude $a$ as peak-to-trough displacement ($2a$).",
      "Graph C incorrectly labels the cycle duration on a time ($t$) axis as wavelength $\\lambda$ instead of period $T$."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q22",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "direct_calculation"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m01",
    "skill_id": "9702_skill_interpret_oscilloscope_traces",
    "accepted_answer": "B",
    "hints": [
      "Measure the horizontal distance across several full cycles on the oscilloscope grid to determine the divisions per cycle.",
      "Calculate the period $T = (\\text{divisions per cycle}) \\times (\\text{time-base setting})$, then calculate frequency $f = \\frac{1}{T}$."
    ],
    "walkthrough": [
      "From the oscilloscope grid, 3 complete wave cycles occupy approximately 8.4 horizontal divisions, which gives $2.8\\text{ divisions per cycle}$.",
      "Using the time-base setting of $5.0\\text{ ms/div}$, the period of the wave is $T = 2.8\\text{ div} \\times 5.0\\text{ ms/div} = 14.0\\text{ ms} = 1.40 \\times 10^{-2}\\text{ s}$.",
      "The frequency of the sound wave is $f = \\frac{1}{T} = \\frac{1}{1.40 \\times 10^{-2}\\text{ s}} \\approx 71.4\\text{ Hz} \\approx 71\\text{ Hz}$, matching option B.",
      "Option A ($f = 57\\text{ Hz}$) results from overestimating the period (e.g. 3.5 divisions per cycle). Options C ($f = 114\\text{ Hz}$) and D ($f = 143\\text{ Hz}$) arise from taking half-cycle measurements or double counting frequency."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q23",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "equation_recall"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m03",
    "skill_id": "9702_skill_apply_doppler_effect",
    "accepted_answer": "D",
    "hints": [
      "Use the Doppler effect formula for a moving source approaching a stationary observer: $f_o = f_s \\left( \\frac{v}{v - v_s} \\right)$.",
      "Substitute emitted frequency $f_s = 2000\\text{ Hz}$, speed of sound $v = 340\\text{ m s}^{-1}$, and car speed $v_s = 30.0\\text{ m s}^{-1}$."
    ],
    "walkthrough": [
      "When a source moves towards a stationary observer, the observed sound waves are compressed, resulting in an observed frequency $f_o = f_s \\left( \\frac{v}{v - v_s} \\right)$.",
      "Substitute the given values: $f_o = 2000 \\times \\left( \\frac{340}{340 - 30.0} \\right) = 2000 \\times \\frac{340}{310} = 2000 \\times 1.0968 \\approx 2193.5\\text{ Hz} \\approx 2190\\text{ Hz}$.",
      "This matches option D.",
      "Option A ($f = 1840\\text{ Hz}$) results from using the formula for a source moving away ($v + v_s$). Option B ($f = 2000\\text{ Hz}$) is the unshifted emitted frequency. Option C ($f = 2180\\text{ Hz}$) comes from the approximation $f_o = f_s(1 + v_s/v) = 2176\\text{ Hz}$."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q24",
    "component": "P1",
    "difficulty": 3,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t08",
    "module_id": "9702_t08_m01",
    "skill_id": "9702_skill_determine_stationary_wave_spacing",
    "accepted_answer": "B",
    "hints": [
      "In a resonance tube with stationary sound waves, the difference in water height between successive resonances corresponds to half a wavelength ($\\Delta h = \\frac{\\lambda}{2}$).",
      "Calculate $\\lambda = 2 \\times \\Delta h$, then use the wave equation $v = f \\lambda$ to determine the frequency $f = \\frac{v}{\\lambda}$."
    ],
    "walkthrough": [
      "Successive resonance positions in an air column closed at one end occur at odd multiples of a quarter-wavelength ($\\frac{\\lambda}{4}, \\frac{3\\lambda}{4}$). The distance between two consecutive resonance levels is therefore $\\Delta h = \\frac{\\lambda}{2}$.",
      "The change in water level between the first and second resonance is $\\Delta h = 67.3\\text{ cm} - 2.9\\text{ cm} = 64.4\\text{ cm} = 0.644\\text{ m}$.",
      "Therefore, the wavelength is $\\lambda = 2 \\times 0.644\\text{ m} = 1.288\\text{ m}$.",
      "Using the wave speed equation $f = \\frac{v}{\\lambda} = \\frac{330\\text{ m s}^{-1}}{1.288\\text{ m}} \\approx 256.2\\text{ Hz} \\approx 256\\text{ Hz}$, which matches option B.",
      "Option A ($f = 128\\text{ Hz}$) treats $\\Delta h$ as a full wavelength. Options C ($f = 512\\text{ Hz}$) and D ($f = 1024\\text{ Hz}$) result from treating $\\Delta h$ as a quarter-wavelength or eighth-wavelength."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q25",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "property_identification",
      "explanation"
    ],
    "topic_id": "9702_t08",
    "module_id": "9702_t08_m02",
    "skill_id": "9702_skill_define_diffraction",
    "accepted_answer": "D",
    "hints": [
      "Recall the condition for significant diffraction when a wave passes through a gap: the spreading angle depends on the ratio $\\frac{\\lambda}{b}$.",
      "Identify which wave and obstacle characteristics appear in this ratio and whether wave amplitude influences the geometric spreading angle."
    ],
    "walkthrough": [
      "Diffraction is the spreading of waves as they pass through an aperture or around an obstacle. The extent of diffraction is determined by the ratio of the wavelength $\\lambda$ to the gap width $b$ (diffraction angle $\\theta \\approx \\frac{\\lambda}{b}$).",
      "Therefore, the angle of diffraction depends solely on the wavelength of the incident wave and the width of the gap, corresponding to option D.",
      "Options A, B, and C are incorrect because the wave amplitude has no effect on the geometric angle or extent of diffraction."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q26",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "comparison"
    ],
    "topic_id": "9702_t08",
    "module_id": "9702_t08_m03",
    "skill_id": "9702_skill_apply_double_slit_interference",
    "accepted_answer": "A",
    "hints": [
      "Use the double-slit interference formula $x = \\frac{\\lambda D}{a}$ to determine the relationship between fringe spacing $x$ and wavelength $\\lambda$.",
      "Set up the proportionality $x \\propto \\lambda$ and calculate $x_{\\text{blue}} = x_{\\text{red}} \\times \\frac{\\lambda_{\\text{blue}}}{\\lambda_{\\text{red}}}$."
    ],
    "walkthrough": [
      "In a double-slit experiment, fringe separation is given by $x = \\frac{\\lambda D}{a}$. For fixed slit separation $a$ and screen distance $D$, fringe separation is directly proportional to wavelength ($x \\propto \\lambda$).",
      "Using the ratio of fringe spacings: $\\frac{x_{\\text{blue}}}{x_{\\text{red}}} = \\frac{\\lambda_{\\text{blue}}}{\\lambda_{\\text{red}}}$.",
      "Substitute the given values: $x_{\\text{blue}} = 3.5\\text{ mm} \\times \\left(\\frac{4.5 \\times 10^{-7}\\text{ m}}{7.0 \\times 10^{-7}\\text{ m}}\\right) = 3.5 \\times \\frac{4.5}{7.0} = 2.25\\text{ mm} \\approx 2.3\\text{ mm}$, which matches option A.",
      "Option C ($5.4\\text{ mm}$) incorrectly inverts the wavelength ratio ($3.5 \\times 7.0 / 4.5$). Option B ($3.5\\text{ mm}$) assumes fringe spacing is independent of wavelength. Option D ($9.0\\text{ mm}$) is twice Option C."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q27",
    "component": "P1",
    "difficulty": 3,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m02",
    "skill_id": "9702_skill_apply_uniform_electric_field",
    "accepted_answer": "A",
    "hints": [
      "Find the potential difference $\\Delta V$ between the top plate ($V = 800\\text{ V}$) and bottom plate ($V = 300\\text{ V}$), and calculate the electric field strength $E = \\frac{\\Delta V}{d}$.",
      "Determine the downward electric force on the positively charged proton ($F = qE$) and compute acceleration using $a = \\frac{F}{m_p}$."
    ],
    "walkthrough": [
      "The potential difference between the plates is $\\Delta V = 800\\text{ V} - 300\\text{ V} = 500\\text{ V}$. With plate separation $d = 20\\text{ cm} = 0.20\\text{ m}$, the uniform electric field strength is $E = \\frac{\\Delta V}{d} = \\frac{500\\text{ V}}{0.20\\text{ m}} = 2500\\text{ V m}^{-1}$.",
      "Because the top plate is at a higher potential ($V = 800\\text{ V}$) than the bottom plate ($V = 300\\text{ V}$), the electric field points downwards from the top plate to the bottom plate.",
      "A proton carries positive charge $q = +1.60 \\times 10^{-19}\\text{ C}$ and mass $m_p = 1.67 \\times 10^{-27}\\text{ kg}$. The electric force on the proton is directed downwards along the field lines with magnitude $F = q E = (1.60 \\times 10^{-19}\\text{ C}) \\times (2500\\text{ V m}^{-1}) = 4.00 \\times 10^{-16}\\text{ N}$.",
      "The resulting acceleration is $a = \\frac{F}{m_p} = \\frac{4.00 \\times 10^{-16}\\text{ N}}{1.67 \\times 10^{-27}\\text{ kg}} \\approx 2.4 \\times 10^{11}\\text{ m s}^{-2}$ downwards, matching option A.",
      "Option B gives the correct magnitude but incorrect upward direction. Options C and D ($a = 5.3 \\times 10^{11}\\text{ m s}^{-2}$) incorrectly use the sum of potentials ($V = 1100\\text{ V}$) instead of the potential difference ($V = 500\\text{ V}$)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q28",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "equation_derivation",
      "comparison"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m02",
    "skill_id": "9702_skill_apply_uniform_electric_field",
    "accepted_answer": "B",
    "hints": [
      "Derive an expression for the transverse deflection $d = \\frac{1}{2} a t^2$ in terms of particle mass $m$, charge $q$, field $E$, speed $v$, and field length $L$.",
      "Compare how doubling the mass to $2m$ while keeping charge $q$ and speed $v$ unchanged alters the acceleration and resulting deflection."
    ],
    "walkthrough": [
      "The time spent traversing the electric field of horizontal length $L$ at horizontal speed $v$ is $t = \\frac{L}{v}$.",
      "The transverse acceleration produced by the electric field is $a = \\frac{F}{m} = \\frac{q E}{m}$. The transverse deflection is $d = \\frac{1}{2} a t^2 = \\frac{1}{2} \\left(\\frac{q E}{m}\\right) \\left(\\frac{L}{v}\\right)^2 = \\frac{q E L^2}{2 m v^2}$.",
      "For the second particle, the mass is doubled to $2m$ while charge $+q$ and speed $v$ remain unchanged. The new deflection is $d_{\\text{new}} = \\frac{q E L^2}{2(2m)v^2} = \\frac{1}{2} d = \\frac{d}{2}$, matching option B.",
      "Option A ($d/4$) would occur if speed were also doubled ($v \\to 2v$). Options C ($2d$) and D ($4d$) incorrectly assume deflection is directly proportional to mass."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q29",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "property_identification"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m01",
    "skill_id": "9702_skill_apply_charge_quantisation",
    "accepted_answer": "C",
    "hints": [
      "Recall the principle of quantisation of electric charge: any observed net charge must be an integer multiple of the elementary charge $e = 1.60 \\times 10^{-19}\\text{ C}$ ($Q = n e$).",
      "Divide each candidate charge by $e = 1.60 \\times 10^{-19}\\text{ C}$ to identify which value gives an exact integer $n$."
    ],
    "walkthrough": [
      "Electric charge is quantised, meaning any observable charge on an isolated particle must equal an integer multiple of the elementary charge: $Q = n e$, where $e = 1.60 \\times 10^{-19}\\text{ C}$ and $n$ is an integer.",
      "Testing the options: Option A gives $n = \\frac{6.40 \\times 10^{-20}}{1.60 \\times 10^{-19}} = 0.40$ (not an integer). Option B gives $n = \\frac{4.00 \\times 10^{-19}}{1.60 \\times 10^{-19}} = 2.50$ (not an integer).",
      "Option C gives $n = \\frac{1.12 \\times 10^{-18}\\text{ C}}{1.60 \\times 10^{-19}\\text{ C}} = 7.00$, which is an exact integer ($n = 7$), matching option C.",
      "Option D gives $n = \\frac{9.11 \\times 10^{-18}}{1.60 \\times 10^{-19}} \\approx 56.94$ (non-integer; 9.11 is the mantissa of the electron mass in kilograms)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q30",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m01",
    "skill_id": "9702_skill_apply_drift_current",
    "accepted_answer": "A",
    "hints": [
      "Use the drift current equation $I = n A v q$ and rearrange to solve for average drift velocity $v = \\frac{I}{n A q}$.",
      "Convert the cross-sectional area $A = 1.0\\text{ cm}^2 = 1.0 \\times 10^{-4}\\text{ m}^2$ and number density $n = 2.0 \\times 10^{13}\\text{ cm}^{-3} = 2.0 \\times 10^{19}\\text{ m}^{-3}$ into consistent SI units."
    ],
    "walkthrough": [
      "The electric current in terms of drift velocity is given by $I = n A v q$, which rearranges to $v = \\frac{I}{n A q}$.",
      "Converting all parameters into standard SI units: $I = 56\\text{ }\\mu\\text{A} = 5.6 \\times 10^{-5}\\text{ A}$, $q = e = 1.60 \\times 10^{-19}\\text{ C}$, $A = 1.0\\text{ cm}^2 = 1.0 \\times 10^{-4}\\text{ m}^2$, and $n = 2.0 \\times 10^{13}\\text{ cm}^{-3} = 2.0 \\times 10^{19}\\text{ m}^{-3}$.",
      "Substitute into the drift velocity equation: $v = \\frac{5.6 \\times 10^{-5}\\text{ A}}{(2.0 \\times 10^{19}\\text{ m}^{-3}) \\times (1.0 \\times 10^{-4}\\text{ m}^2) \\times (1.60 \\times 10^{-19}\\text{ C})} = \\frac{5.6 \\times 10^{-5}}{3.20 \\times 10^{-4}} = 0.175\\text{ m s}^{-1} \\approx 0.18\\text{ m s}^{-1}$, which matches option A.",
      "Options B ($v = 18\\text{ m s}^{-1}$), C ($v = 180\\text{ m s}^{-1}$), and D ($v = 1800\\text{ m s}^{-1}$) result from power-of-ten errors when converting $\\text{cm}^2$ and $\\text{cm}^{-3}$ into $\\text{m}^2$ and $\\text{m}^{-3}$."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q31",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "equation_derivation",
      "direct_calculation"
    ],
    "topic_id": "9702_t10",
    "module_id": "9702_t10_m01",
    "skill_id": "9702_skill_calculate_series_circuit_current_with_internal_resistance",
    "accepted_answer": "B",
    "hints": [
      "Determine the total resistance of the circuit including internal resistance $r$, and write an expression for the circuit current $I$.",
      "Substitute the current $I$ into the power formula $P = I^2 R$ for the external resistor."
    ],
    "walkthrough": [
      "The total resistance of the series circuit is $R_{\\text{total}} = R + r$. By Ohm law, the current flowing through the circuit is $I = \\frac{E}{R + r}$.",
      "The power dissipated specifically in the external resistor of resistance $R$ is given by $P = I^2 R = \\left(\\frac{E}{R + r}\\right)^2 R = \\frac{E^2 R}{(R + r)^2}$, matching option B.",
      "Option A ($\\frac{E^2(R+r)}{R^2}$) is dimensionally incorrect. Option C ($\\frac{E^2(R+r)}{r^2}$) is also incorrect. Option D ($\\frac{E^2 r}{(R+r)^2}$) represents the power dissipated internally inside the cell."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q32",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "graph_interpretation",
      "classification"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m03",
    "skill_id": "9702_skill_apply_ohms_law",
    "accepted_answer": "D",
    "hints": [
      "Examine the $I-V$ characteristic: negligible current for negative voltages and low positive voltages, followed by a sharp increase above a forward threshold voltage.",
      "Recall which electronic component conducts current in only one direction above a turn-on threshold."
    ],
    "walkthrough": [
      "The graph displays virtually zero current in reverse bias (negative $V$) and in forward bias below a knee voltage, after which current increases rapidly with increasing potential difference.",
      "This asymmetric, non-linear behaviour is the characteristic $I-V$ curve of a semiconductor diode, which allows current to flow primarily in one direction (option D).",
      "Option A (filament lamp) exhibits a symmetric S-shaped curve with decreasing gradient due to heating. Options B (metallic conductor at constant temperature) and C (fixed resistor) have straight-line graphs passing through the origin."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q33",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "direct_calculation",
      "equation_recall"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m03",
    "skill_id": "9702_skill_apply_resistivity",
    "accepted_answer": "B",
    "hints": [
      "Recall the resistivity equation relating resistance $R$, resistivity $\\rho$, length $L$, and cross-sectional area $A$: $R = \\frac{\\rho L}{A}$.",
      "Substitute $\\rho = 1.7 \\times 10^{-8}\\text{ }\\Omega\\text{ m}$, $L = 1.4\\text{ m}$, and $A = 7.8 \\times 10^{-7}\\text{ m}^2$."
    ],
    "walkthrough": [
      "The electrical resistance of a uniform conductor is given by $R = \\frac{\\rho L}{A}$.",
      "Substitute the given values into the formula: $R = \\frac{(1.7 \\times 10^{-8}\\text{ }\\Omega\\text{ m}) \\times (1.4\\text{ m})}{7.8 \\times 10^{-7}\\text{ m}^2} = \\frac{2.38 \\times 10^{-8}}{7.8 \\times 10^{-7}} \\approx 0.0305\\text{ }\\Omega \\approx 0.031\\text{ }\\Omega$.",
      "This result matches option B.",
      "Option A ($R = 0.016\\text{ }\\Omega$) is approximately half the correct value. Options C ($R = 33\\text{ }\\Omega$) and D ($R = 64\\text{ }\\Omega$) result from inverting the formula ($A / \\rho L$) or large power-of-ten errors."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q34",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "circuit_analysis",
      "direct_calculation"
    ],
    "topic_id": "9702_t10",
    "module_id": "9702_t10_m01",
    "skill_id": "9702_skill_calculate_series_parallel_circuit_current",
    "accepted_answer": "A",
    "hints": [
      "Determine the required total equivalent resistance of the circuit using $R_{\\text{total}} = \\frac{E}{I} = \\frac{6.0\\text{ V}}{0.67\\text{ A}}$.",
      "Calculate the equivalent resistance for each combination of three $6.0\\text{ }\\Omega$ resistors to identify which equals $9.0\\text{ }\\Omega$."
    ],
    "walkthrough": [
      "For a battery of e.m.f. $E = 6.0\\text{ V}$ to deliver a current of $I = 0.67\\text{ A}$ (or $\\frac{2}{3}\\text{ A}$), the total equivalent resistance must be $R_{\\text{total}} = \\frac{E}{I} = \\frac{6.0\\text{ V}}{\\frac{2}{3}\\text{ A}} = 9.0\\text{ }\\Omega$.",
      "Evaluating Circuit A: A $6.0\\text{ }\\Omega$ resistor in series with a parallel pair of $6.0\\text{ }\\Omega$ resistors gives $R_{\\text{total}} = 6.0 + \\left(\\frac{6.0 \\times 6.0}{6.0 + 6.0}\\right) = 6.0 + 3.0 = 9.0\\text{ }\\Omega$. This produces $I = \\frac{6.0\\text{ V}}{9.0\\text{ }\\Omega} = 0.67\\text{ A}$, matching option A.",
      "Circuit B has three resistors in series: $R = 18\\text{ }\\Omega \\implies I = 0.33\\text{ A}$. Circuit C has two in series in parallel with one: $R = \\frac{12 \\times 6}{12 + 6} = 4.0\\text{ }\\Omega \\implies I = 1.5\\text{ A}$. Circuit D has three in parallel: $R = 2.0\\text{ }\\Omega \\implies I = 3.0\\text{ A}$."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q35",
    "component": "P1",
    "difficulty": 3,
    "question_patterns": [
      "circuit_analysis",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t10",
    "module_id": "9702_t10_m01",
    "skill_id": "9702_skill_calculate_parallel_resistance",
    "accepted_answer": "C",
    "hints": [
      "First, use the known resistance between Y and Z ($R_{YZ} = 2.5\\text{ }\\Omega$) to determine the unknown resistance $R$, noting that the branch across Y-Z consists of the $5.0\\text{ }\\Omega$ resistor in parallel with $(R + R)$.",
      "Second, find the equivalent resistance between X and Y by combining the direct branch $R$ in parallel with the branch $(R + 5.0\\text{ }\\Omega)$."
    ],
    "walkthrough": [
      "Between terminals Y and Z, the circuit consists of a direct $5.0\\text{ }\\Omega$ resistor in parallel with the series combination of two identical resistors of resistance $R$ (total resistance $2R$).",
      "Equating the parallel resistance to the given value: $R_{YZ} = \\frac{5.0 \\times 2R}{5.0 + 2R} = 2.5\\text{ }\\Omega$. Solving for $R$: cross-multiplying yields $5.0(2R) = 2.5(5.0 + 2R) \\implies 10.0 R = 12.5 + 5.0 R \\implies 5.0 R = 12.5 \\implies R = 2.5\\text{ }\\Omega$.",
      "To find the resistance between terminals X and Y: the direct branch has resistance $R = 2.5\\text{ }\\Omega$, while the alternative path through Z has resistance $R + 5.0 = 2.5 + 5.0 = 7.5\\text{ }\\Omega$.",
      "The equivalent resistance between X and Y is $R_{XY} = \\frac{2.5 \\times 7.5}{2.5 + 7.5} = \\frac{18.75}{10.0} = 1.875\\text{ }\\Omega \\approx 1.9\\text{ }\\Omega$, matching option C.",
      "Options A ($R_{XY} = 0.30\\text{ }\\Omega$), B ($R_{XY} = 0.53\\text{ }\\Omega$), and D ($R_{XY} = 3.3\\text{ }\\Omega$) result from incorrect parallel/series combinations or using $R = 5.0\\text{ }\\Omega$."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q36",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "circuit_analysis",
      "explanation"
    ],
    "topic_id": "9702_t10",
    "module_id": "9702_t10_m01",
    "skill_id": "9702_skill_analyse_circuits",
    "accepted_answer": "D",
    "hints": [
      "Consider how reducing the resistance of the variable resistor affects the total resistance of the single series loop.",
      "Apply Ohm law to determine the change in total circuit current (ammeter reading) and the resulting potential difference across the fixed resistor (voltmeter reading)."
    ],
    "walkthrough": [
      "In a series circuit, the total resistance is $R_{\\text{total}} = R_{\\text{fixed}} + R_{\\text{variable}}$. When the resistance of the variable resistor is reduced, $R_{\\text{total}}$ decreases.",
      "By Ohm law, the circuit current $I = \\frac{E}{R_{\\text{total}}}$ increases, so the ammeter reading increases.",
      "The voltmeter measures the potential difference across the fixed resistor: $V = I R_{\\text{fixed}}$. Since current $I$ increases while $R_{\\text{fixed}}$ remains constant, the voltmeter reading also increases, corresponding to option D.",
      "Options A, B, and C incorrectly suggest that the ammeter or voltmeter reading decreases, which contradicts the inverse relationship between circuit resistance and current."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q37",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "circuit_analysis",
      "direct_calculation"
    ],
    "topic_id": "9702_t10",
    "module_id": "9702_t10_m03",
    "skill_id": "9702_skill_calculate_series_circuit_potential_difference",
    "accepted_answer": "D",
    "hints": [
      "Use the potential divider principle: the total supply e.m.f. ($E = 9.0\\text{ V}$) is split between the top resistor ($R_1 = 160\\text{ }\\Omega$) and resistor $R$.",
      "Calculate the potential difference across the top resistor as $9.0\\text{ V} - 4.0\\text{ V} = 5.0\\text{ V}$, then set up the ratio $\\frac{R}{R_1} = \\frac{4.0}{5.0}$."
    ],
    "walkthrough": [
      "In this potential divider circuit, the output voltage across resistor $R$ is $V_{\\text{out}} = 4.0\\text{ V}$. Since total e.m.f. is $E = 9.0\\text{ V}$, the potential difference across the top resistor is $V_1 = 9.0\\text{ V} - 4.0\\text{ V} = 5.0\\text{ V}$.",
      "Because both resistors carry the identical series current $I$, the potential differences are proportional to resistances: $\\frac{R}{R_1} = \\frac{V_R}{V_1} = \\frac{4.0\\text{ V}}{5.0\\text{ V}} = 0.80$.",
      "Solving for $R$ with $R_1 = 160\\text{ }\\Omega$: $R = 160 \\times 0.80 = 128\\text{ }\\Omega$, which matches option D.",
      "Option A ($R = 32\\text{ }\\Omega$) and Option B ($R = 49\\text{ }\\Omega$) result from incorrectly calculating ratios (e.g. $R_1 \\times 4.0 / 9.0$ or similar misapplications). Option C ($R = 71\\text{ }\\Omega$) comes from using $R = R_1 \\times (4.0/9.0) / (1 - 4.0/9.0)$ inverted."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q38",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "circuit_analysis",
      "equation_derivation"
    ],
    "topic_id": "9702_t10",
    "module_id": "9702_t10_m03",
    "skill_id": "9702_skill_apply_potentiometer_balance",
    "accepted_answer": "D",
    "hints": [
      "When the lamp S is off, no current passes through the central connection, establishing a balanced Wheatstone bridge condition.",
      "Relate the potential difference ratio $\\frac{V_1}{V_2}$ across resistors $R_1$ and $R_2$ to the ratio of wire lengths on either side of the sliding contact J ($x$ and $L - x$)."
    ],
    "walkthrough": [
      "When the lamp S is extinguished, zero current flows through the central branch, meaning the electric potential at contact J equals the potential at the junction between $R_1$ and $R_2$ (null balance condition).",
      "The uniform resistance wire XY of length $L$ is divided into two sections: length $x$ (from X to J) and length $L - x$ (from J to Y).",
      "The potential differences across these wire sections are proportional to their lengths: $V_{\\text{XJ}} \\propto x$ and $V_{\\text{JY}} \\propto (L - x)$.",
      "At balance, the potential drop across $R_1$ equals $V_{\\text{XJ}}$ and that across $R_2$ equals $V_{\\text{JY}}$, giving the ratio $\\frac{V_1}{V_2} = \\frac{x}{L - x}$, matching option D.",
      "Option A ($L/x$) and Option B ($x/L$) represent fractional lengths of the whole wire. Option C ($\\frac{L-x}{x}$) is the inverted ratio $\\frac{V_2}{V_1}$."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q39",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "equation_completion",
      "classification"
    ],
    "topic_id": "9702_t11",
    "module_id": "9702_t11_m01",
    "skill_id": "9702_skill_complete_nuclear_equations",
    "accepted_answer": "C",
    "hints": [
      "Apply conservation of nucleon number (mass number $A$) and proton number (atomic number $Z$) across the decay equation: ${}^{23}_{12}\\text{Mg} \\rightarrow {}^{A}_{Z}\\text{X} + {}^{0}_{+1}\\beta + \\nu_e$.",
      "Recall that a $\\beta^+$ particle is a positron with charge $+1$ and nucleon number $0$, while the electron neutrino $\\nu_e$ has $A = 0$ and $Z = 0$."
    ],
    "walkthrough": [
      "In $\\beta^+$ decay, a proton inside the magnesium nucleus transforms into a neutron, emitting a positron (${}^{0}_{+1}\\beta$) and an electron neutrino ($\\nu_e$).",
      "Applying nucleon number conservation: $A_{\\text{parent}} = A_X + 0 + 0 \\implies 23 = A_X \\implies A_X = 23$.",
      "Applying proton number conservation: $Z_{\\text{parent}} = Z_X + (+1) + 0 \\implies 12 = Z_X + 1 \\implies Z_X = 11$.",
      "The element with atomic number $Z = 11$ is sodium ($\\text{Na}$). Therefore, nucleus X is ${}^{23}_{11}\\text{Na}$, matching option C.",
      "Option A (${}^{22}_{11}\\text{Na}$) incorrectly reduces nucleon number. Options B (${}^{22}_{13}\\text{Al}$) and D (${}^{23}_{13}\\text{Al}$) increase the proton number, which occurs in $\\beta^-$ decay rather than $\\beta^+$ decay."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_s18_13_q40",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "classification",
      "property_identification"
    ],
    "topic_id": "9702_t11",
    "module_id": "9702_t11_m02",
    "skill_id": "9702_skill_classify_leptons",
    "accepted_answer": "A",
    "hints": [
      "Recall the standard classification of fundamental particles: leptons are fundamental particles not subject to the strong interaction (e.g. electrons, neutrinos, positrons, muons).",
      "Identify which particles in the lists are hadrons/baryons composed of quarks (such as protons and neutrons) and eliminate any list containing them."
    ],
    "walkthrough": [
      "Leptons are fundamental particles that do not experience the strong nuclear force. The lepton family includes electrons, positrons (anti-electrons), muons, tau particles, and their corresponding neutrinos.",
      "Protons and neutrons are composite particles (hadrons / baryons) composed of triplets of quarks ($uud$ and $udd$), so they are not leptons.",
      "Evaluating the lists: Option A contains electron, neutrino, and positron—all of which are fundamental leptons.",
      "Options B, C, and D all contain protons or neutrons (baryons), making them incorrect."
    ]
  }
]

def main():
    print(f"Generating {len(data)} enrichment files for 9702_s18_13...")
    for item in data:
        qid = item["question_id"]
        out_file = OUT_DIR / f"{qid}.enrichment.json"
        out_file.write_text(json.dumps(item, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"  Wrote {out_file.name}")
    print("Done!")

if __name__ == "__main__":
    main()
