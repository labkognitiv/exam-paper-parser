#!/usr/bin/env python3
import json
import re
from pathlib import Path

enrichments = {
    1: {
        "difficulty": 2,
        "question_patterns": ["physical_quantity_estimation", "property_identification"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m01",
        "skill_id": "9702_skill_estimate_physical_quantities",
        "accepted_answer": "D",
        "hints": [
            "Estimate the mass of an adult racehorse in kilograms, then multiply by gravitational acceleration $g \\approx 9.81\\text{ m s}^{-2}$ to determine its weight.",
            "Compare the calculated weight of a horse (typically around $ 400\\text{ to } 600\\text{ kg} $) with the proposed value of $ 6 \\times 10^2\\text{ N} $."
        ],
        "walkthrough": [
            "A typical electric kettle operates at around $ 2\\text{ kW} = 2 \\times 10^3\\text{ W} $, a medium swimming pool contains several hundred cubic metres of water ($ 400\\text{ m}^3 $), and a loaded lorry with mass $ 20\\text{ tonnes} $ moving at $ 25\\text{ m s}^{-1} $ has momentum $p = mv = 2 \\times 10^4 \\times 25 = 5 \\times 10^5\\text{ N s} $. These are all realistic physical estimates.",
            "An adult racehorse has a mass of approximately $ 500\\text{ kg} $. Its weight is $W = mg \\approx 500\\text{ kg} \\times 9.81\\text{ N kg}^{-1} \\approx 5000\\text{ N} = 5 \\times 10^3\\text{ N} $. A weight of $ 6 \\times 10^2\\text{ N} = 600\\text{ N} $ corresponds to a mass of roughly $ 60\\text{ kg} $, which is the mass of a human jockey rather than a fully grown racehorse.",
            "Therefore, option D represents an unreasonable underestimate."
        ]
    },
    2: {
        "difficulty": 2,
        "question_patterns": ["equation_derivation", "classification"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m02",
        "skill_id": "9702_skill_derive_si_base_units",
        "accepted_answer": "B",
        "hints": [
            "Recall that newton-metres ($\\text{N m}$) is the unit of mechanical work or energy, which is equivalent to joules ($\\text{J}$).",
            "Relate potential difference $V$ to energy $W$ and electric charge $Q$ using the formula $V = \\frac{W}{Q}$, and substitute to find the unit $\\text{J V}^{-1}$."
        ],
        "walkthrough": [
            "The unit newton-metre ($\\text{N m}$) is equivalent to the joule ($\\text{J}$), which is the unit of energy or work done ($W = F \\times d$).",
            "Electric potential difference is defined as work done per unit charge, $V = \\frac{W}{Q}$, which means $ 1\\text{ V} = 1\\text{ J C}^{-1} $. Rearranging this gives $ 1\\text{ C} = 1\\text{ J V}^{-1} = 1\\text{ N m V}^{-1} $. Thus, $\\text{N m V}^{-1}$ is the unit of electric charge.",
            "Options A (acceleration, $\\text{m s}^{-2}$), C (current, $\\text{A} = \\text{C s}^{-1}$), and D (resistance, $\\Omega = \\text{V A}^{-1}$) do not correspond to $\\text{N m V}^{-1}$."
        ]
    },
    3: {
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "vector_diagram_construction"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m04",
        "skill_id": "9702_skill_resolve_vector_components",
        "accepted_answer": "D",
        "hints": [
            "Resolve the $ 6\\text{ N} $ force into perpendicular horizontal and vertical components relative to the vertical $ 10\\text{ N} $ force.",
            "Combine vertical components algebraically, then use Pythagoras' theorem and trigonometry to determine the magnitude and direction of the resultant vector."
        ],
        "walkthrough": [
            "Let the upward direction be positive vertical. The $ 10\\text{ N} $ force acts upwards. The $ 6\\text{ N} $ force acts downwards at an angle of $ 40^\\circ $ to the vertical, giving a downward vertical component of $ 6\\cos(40^\\circ) = 6(0.7660) = 4.60\\text{ N} $ and a horizontal component of $ 6\\sin(40^\\circ) = 6(0.6428) = 3.86\\text{ N} $.",
            "The net vertical component is $F_y = 10 - 4.60 = 5.40\\text{ N}$ upwards, and the net horizontal component is $F_x = 3.86\\text{ N}$.",
            "The magnitude of the resultant force is $R = \\sqrt{F_x^2 + F_y^2} = \\sqrt{3.86^2 + 5.40^2} = \\sqrt{14.90 + 29.16} = \\sqrt{44.06} \\approx 6.6\\text{ N}$. The angle $\\theta$ to the vertical is $\\theta = \\arctan\\left(\\frac{3.86}{5.40}\\right) = \\arctan(0.7148) \\approx 36^\\circ$, matching option D."
        ]
    },
    4: {
        "difficulty": 2,
        "question_patterns": ["measurement_selection", "direct_calculation"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m03",
        "skill_id": "9702_skill_measurement",
        "accepted_answer": "D",
        "hints": [
            "Determine the value represented by each minor scale division across the full range of $ 0\\text{ to } 250\\text{ mA} $.",
            "Identify the pointer's position on the scale and multiply the division count by the value per division."
        ],
        "walkthrough": [
            "The analogue ammeter has a full-scale deflection of $ 250\\text{ mA} $ across $ 50 $ small subdivisions, meaning each small subdivision represents $\\frac{250\\text{ mA}}{50} = 5\\text{ mA}$ (or each major numbered interval represents $ 50\\text{ mA} $).",
            "The pointer indicates 38 small subdivisions from zero, giving a measured current of $ 38 \\times 5\\text{ mA} = 190\\text{ mA} $.",
            "Options A, B, and C arise from misinterpreting the scale markings or reading the dial without scaling properly to the $ 250\\text{ mA} $ full-scale range."
        ]
    },
    5: {
        "difficulty": 2,
        "question_patterns": ["classification", "property_identification"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m03",
        "skill_id": "9702_skill_explain_systematic_random_error_effects",
        "accepted_answer": "D",
        "hints": [
            "Recall that precision is characterized by a small spread/scatter in repeated measurements, while accuracy means the average of the readings is close to the true value $V$.",
            "Evaluate each distribution curve X, Y, and Z for its width (spread) and the position of its peak/mean relative to the true value $V$."
        ],
        "walkthrough": [
            "Equipment X produces a narrow distribution centered on the true value $V$, so it is both precise (small spread) and accurate (mean equals $V$).",
            "Equipment Y produces a narrow distribution whose mean is shifted away from $V$, so it is precise (small spread) but not accurate due to systematic error. Equipment Z produces a broad distribution centered on $V$, so it is accurate (mean equals $V$) but not precise (large spread).",
            "Thus, there are 2 precise pieces of equipment (X and Y) and 2 accurate pieces of equipment (X and Z), which corresponds to option D."
        ]
    },
    6: {
        "difficulty": 1,
        "question_patterns": ["graph_interpretation", "property_identification"],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_construct_constant_acceleration_velocity_time_graph",
        "accepted_answer": "D",
        "hints": [
            "Consider the forces acting on an object falling in a vacuum where there is no air resistance.",
            "Recall that uniform acceleration produces a constant gradient on a velocity-time ($v-t$) graph."
        ],
        "walkthrough": [
            "In a vacuum, air resistance is zero. The only force acting on the falling object is its weight, resulting in a constant downward acceleration equal to the acceleration of free fall $g$.",
            "From the kinematic equation $v = u + gt = gt$, velocity increases linearly with time from rest. This is represented on a velocity-time graph by a straight line passing through the origin with a constant positive gradient, as shown in graph D.",
            "Curves A, B, and C represent non-constant acceleration (such as falling in air where drag causes the acceleration to decrease towards terminal velocity)."
        ]
    },
    7: {
        "difficulty": 2,
        "question_patterns": ["equation_derivation", "multi_step_calculation"],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_resolve_velocity_components",
        "accepted_answer": "B",
        "hints": [
            "Resolve the initial velocity $V$ into horizontal component $V\\cos\\theta$ and vertical component $V\\sin\\theta$.",
            "Use the vertical motion to find the total time of flight $T$, then multiply by the horizontal velocity to obtain the range $R$."
        ],
        "walkthrough": [
            "The initial horizontal and vertical velocity components are $u_x = V\\cos\\theta$ and $u_y = V\\sin\\theta$.",
            "For projectile motion over level ground, the vertical displacement at landing is zero: $s_y = u_y T - \\frac{1}{2}g T^2 = 0$. Solving for total flight time yields $T = \\frac{2V\\sin\\theta}{g}$.",
            "Since horizontal acceleration is zero, the horizontal range is $R = u_x T = (V\\cos\\theta) \\left(\\frac{2V\\sin\\theta}{g}\\right) = \\frac{2V^2\\sin\\theta\\cos\\theta}{g}$, which matches option B."
        ]
    },
    8: {
        "difficulty": 2,
        "question_patterns": ["explanation", "property_identification"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_explain_newtons_third_law",
        "accepted_answer": "C",
        "hints": [
            "Identify the two interacting bodies involved when considering the weight of the book.",
            "Newton's third law force pairs must be of the same type (gravitational), equal in magnitude, opposite in direction, and act on the other interacting object."
        ],
        "walkthrough": [
            "The weight $W$ of the book is the gravitational force exerted by the Earth on the book, directed downwards.",
            "According to Newton's third law, the reaction force must be of identical physical nature (gravitational), equal in magnitude, opposite in direction (upwards), and exerted by the book on the Earth. Therefore, the reaction force is the gravitational force $W$ acting upwards on the Earth from the book.",
            "Option B describes the normal contact force exerted by the table on the book, which balances the weight in equilibrium (Newton's first law) but is an electrostatic contact force acting on the same body, not a Newton's third law pair."
        ]
    },
    9: {
        "difficulty": 3,
        "question_patterns": ["comparison", "explanation"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m02",
        "skill_id": "9702_skill_analyse_resistive_force_motion",
        "accepted_answer": "B",
        "hints": [
            "Recall that air resistance force depends on cross-sectional area $A \\propto D^2$ and the square of velocity.",
            "Formulate the net downward acceleration $a = g - \\frac{F_D}{m}$ and compare the ratio $\\frac{m}{D^2}$ for each ball to determine which experiences the least deceleration from drag."
        ],
        "walkthrough": [
            "The drag force acting on a sphere moving through air is proportional to its cross-sectional area $A = \\frac{\\pi D^2}{4}$, so $F_D = k D^2 v^2$.",
            "Applying Newton's second law gives downward acceleration $a = \\frac{mg - F_D}{m} = g - \\frac{k D^2 v^2}{m}$. The ball with the largest ratio of $\\frac{m}{D^2}$ will have the largest terminal velocity and maintain higher acceleration throughout its descent.",
            "Evaluating $\\frac{m}{D^2}$ for each option: A gives $\\frac{M}{D^2} = 1$, B gives $\\frac{4M}{D^2} = 4$, C gives $\\frac{M}{(2D)^2} = 0.25$, and D gives $\\frac{4M}{(2D)^2} = 1$. Ball B has the highest ratio, so it experiences the least deceleration from air resistance and reaches the ground first."
        ]
    },
    10: {
        "difficulty": 3,
        "question_patterns": ["multi_step_calculation", "vector_diagram_construction"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m03",
        "skill_id": "9702_skill_apply_momentum_conservation",
        "accepted_answer": "D",
        "hints": [
            "Apply conservation of linear momentum in the direction perpendicular to the original path of molecule P.",
            "Since initial perpendicular momentum is zero and the two molecules have identical mass, equate the perpendicular momentum components: $ 180\\sin(55^\\circ) = v\\sin(34^\\circ) $."
        ],
        "walkthrough": [
            "Since no external forces act on the system, total linear momentum is conserved in all directions. Both nitrogen molecules have equal mass $m$.",
            "Before the collision, molecule P moves purely horizontally and Q is stationary, so the initial total momentum perpendicular to P's original path is zero.",
            "After the collision, the vertical components of momentum must sum to zero: $ m(180)\\sin(55^\\circ) - m v\\sin(34^\\circ) = 0 $. Solving for $v$: $v = \\frac{180\\sin(55^\\circ)}{\\sin(34^\\circ)} = \\frac{180 \\times 0.8192}{0.5592} \\approx 264\\text{ m s}^{-1} \\approx 260\\text{ m s}^{-1}$, corresponding to option D."
        ]
    },
    11: {
        "difficulty": 1,
        "question_patterns": ["classification", "property_identification"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_analyse_electric_force",
        "accepted_answer": "A",
        "hints": [
            "Consider the direction of the force exerted by an electric field on positive and negative charges.",
            "Recall that the gravitational force on any mass is always in the direction of the gravitational field, whereas an electric force on a negative charge acts opposite to the electric field."
        ],
        "walkthrough": [
            "The electric field direction is defined as the direction of the force acting on a stationary positive test charge ($F = qE$).",
            "For a negatively charged particle ($q < 0$), the electric force vector acts in the direction opposite to the electric field lines ($F = -|q|E$).",
            "In contrast, gravitational force is always parallel and in the same direction as the gravitational field because mass is strictly positive. Therefore, the field is electric and the charge on the particle is negative, which corresponds to option A."
        ]
    },
    12: {
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "definition"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_apply_torque_of_couple",
        "accepted_answer": "C",
        "hints": [
            "Recall the definition of the torque of a couple as the product of one of the forces and the perpendicular distance between the lines of action of the forces.",
            "Identify the perpendicular distance between the two forces acting tangentially at opposite sides of the circular disc of radius $r$."
        ],
        "walkthrough": [
            "A couple consists of two parallel forces of equal magnitude $F$ acting in opposite directions along different lines of action.",
            "The torque of a couple is defined as $\\tau = F \\times d$, where $d$ is the perpendicular distance between the lines of action of the two forces.",
            "For two forces acting tangentially at opposite ends of a disc of radius $r$, the perpendicular distance between their lines of action is the diameter $d = 2r$. Thus, the torque is $\\tau = F \\times (2r) = 2Fr$, matching option C."
        ]
    },
    13: {
        "difficulty": 3,
        "question_patterns": ["multi_step_calculation", "explanation"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_apply_principle_of_moments",
        "accepted_answer": "B",
        "hints": [
            "Locate the centre of gravity of the square sign and calculate its perpendicular distance to the hinge when tilted at an angle $\\theta$ to the vertical.",
            "Equate the gravitational moment about the hinge to the maximum frictional torque exerted by the hinge ($ 6.0\\text{ N m} $)."
        ],
        "walkthrough": [
            "The sign is a uniform square of side length $ 0.80\\text{ m} $ and weight $W = 40\\text{ N}$. Its centre of gravity is at the geometric centre, a distance $L = 0.40\\text{ m}$ from the top hinge.",
            "When displaced at an angle $\\theta$ from the vertical, the perpendicular distance from the line of action of the weight to the hinge axis is $d_\\perp = 0.40\\sin\\theta$. The gravitational restoring torque is $\\tau_g = W d_\\perp = 40 \\times 0.40\\sin\\theta = 16\\sin\\theta\\text{ N m}$.",
            "The sign remains stationary when the gravitational restoring torque equals the maximum resisting frictional torque of the hinge ($ 6.0\\text{ N m} $): $ 16\\sin\\theta = 6.0 \\implies \\sin\\theta = \\frac{6.0}{16} = 0.375 $. Thus, $\\theta = \\arcsin(0.375) \\approx 22.0^\\circ$, which corresponds to option B."
        ]
    },
    14: {
        "difficulty": 2,
        "question_patterns": ["multi_step_calculation", "direct_calculation"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m03",
        "skill_id": "9702_skill_define_pressure",
        "accepted_answer": "C",
        "hints": [
            "Calculate the total weight of the elephant and divide by 4 to determine the normal force on each foot.",
            "Find the cross-sectional area of a foot using the circumference $C = 2\\pi r = 1.4\\text{ m}$ ($A = \\frac{C^2}{4\\pi}$), and compute pressure $P = \\frac{F}{A}$."
        ],
        "walkthrough": [
            "The total weight of the elephant is $W = mg = 5400\\text{ kg} \\times 9.81\\text{ N kg}^{-1} \\approx 52974\\text{ N}$.",
            "With the weight evenly distributed across all 4 feet, the downward force per foot is $F_1 = \\frac{52974}{4} \\approx 13244\\text{ N}$.",
            "From the circumference $C = 1.4\\text{ m}$, the cross-sectional area of each foot is $A = \\frac{C^2}{4\\pi} = \\frac{1.4^2}{4\\pi} = \\frac{1.96}{12.566} \\approx 0.156\\text{ m}^2$. The pressure exerted by each foot is $P = \\frac{F_1}{A} = \\frac{13244}{0.156} \\approx 84900\\text{ Pa} \\approx 85\\text{ kPa}$, matching option C."
        ]
    },
    15: {
        "difficulty": 1,
        "question_patterns": ["classification", "property_identification"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_conservation_of_energy",
        "accepted_answer": "A",
        "hints": [
            "Note that at terminal velocity, speed is constant, meaning the stone's kinetic energy does not change.",
            "As the stone falls, its vertical height decreases. Consider what form of energy the lost gravitational potential energy is converted into due to air resistance."
        ],
        "walkthrough": [
            "Because the stone falls at constant terminal velocity, its kinetic energy ($E_k = \\frac{1}{2}mv^2$) remains constant throughout the fall.",
            "As the stone descends, its gravitational potential energy decreases ($E_p = mgh$). Since kinetic energy is unchanged, all work done against air resistance is dissipated as thermal energy in the stone and surrounding air.",
            "Therefore, the overall energy transformation is gravitational potential energy to thermal energy, matching option A."
        ]
    },
    16: {
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "definition"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_calculate_work_from_force_displacement",
        "accepted_answer": "A",
        "hints": [
            "Work done on an object is defined as the product of the upward force exerted on the object and its vertical displacement.",
            "Identify the weight of the object and the distance it moved in the direction of the supporting force, ensuring units are converted to metres."
        ],
        "walkthrough": [
            "The upward force exerted on the object to lift it slowly at constant speed is equal to its weight, $F = 12\\text{ N}$.",
            "The object moves vertically upwards by a displacement of $s = 0.50\\text{ cm} = 0.50 \\times 10^{-2}\\text{ m} = 0.0050\\text{ m}$.",
            "The work done on the object is $W = F \\times s = 12\\text{ N} \\times 0.0050\\text{ m} = 0.060\\text{ J}$, which corresponds to option A. (The displacement of the plunger describes work input on the gas, not work done on the object itself)."
        ]
    },
    17: {
        "difficulty": 2,
        "question_patterns": ["equation_derivation", "comparison"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m02",
        "skill_id": "9702_skill_apply_gravitational_potential_energy",
        "accepted_answer": "D",
        "hints": [
            "Express the vertical height gained $\\Delta h$ in terms of distance along the slope $s$ and slope angle $\\alpha$.",
            "Divide the expression for gravitational potential energy gained ($mg\\Delta h$) by the expression for work done by force $F$ ($Fs$)."
        ],
        "walkthrough": [
            "When the car moves a distance $s$ along an incline of angle $\\alpha$, the vertical height gained is $\\Delta h = s\\sin\\alpha$.",
            "The gain in gravitational potential energy of the car is $\\Delta E_p = mg\\Delta h = mg(s\\sin\\alpha) = mgs\\sin\\alpha$.",
            "The work done by the pulling force $F$ over the displacement $s$ along the incline is $W = Fs$.",
            "The required ratio is $\\frac{\\text{gravitational potential energy gained}}{\\text{work done by force } F} = \\frac{mgs\\sin\\alpha}{Fs} = \\frac{mg\\sin\\alpha}{F}$, which is option D."
        ]
    },
    18: {
        "difficulty": 1,
        "question_patterns": ["definition", "property_identification"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_define_power",
        "accepted_answer": "D",
        "hints": [
            "Recall the standard definition of power in mechanics and thermodynamics.",
            "Consider the rate of energy transfer or work done per unit time."
        ],
        "walkthrough": [
            "Power is defined as the rate of doing work, or the rate of energy transferred with respect to time ($P = \\frac{W}{t} = \\frac{\\Delta E}{\\Delta t}$).",
            "While $P = Fv$ represents an equation for power when a constant force moves an object at velocity $v$, it is a formula rather than the fundamental defining statement of power.",
            "Thus, option D correctly gives the definition: power is the rate at which work is done."
        ]
    },
    19: {
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "comparison"],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m01",
        "skill_id": "9702_skill_apply_stress",
        "accepted_answer": "A",
        "hints": [
            "Recall that tensile stress is defined as $\\sigma = \\frac{T}{A}$, where $A$ is the cross-sectional area.",
            "Express the cross-sectional area in terms of diameter ($A = \\frac{\\pi D^2}{4}$) and find how stress scales when diameter doubles under the same tension $T$."
        ],
        "walkthrough": [
            "Both portions of the steel bar are in series under the same tensile force $T$.",
            "Tensile stress is defined as $\\sigma = \\frac{T}{A}$. For a circular cross-section, $A = \\frac{\\pi D^2}{4}$, so $\\sigma = \\frac{4T}{\\pi D^2} \\propto \\frac{1}{D^2}$.",
            "The wide portion has twice the diameter of the narrow portion ($D_w = 2D_n$), so its area is $A_w = 4A_n$.",
            "The ratio of stress in the wide portion to that in the narrow portion is $\\frac{\\sigma_w}{\\sigma_n} = \\frac{A_n}{A_w} = \\left(\\frac{D_n}{D_w}\\right)^2 = \\left(\\frac{1}{2}\\right)^2 = 0.25$, matching option A."
        ]
    },
    20: {
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "comparison"],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m02",
        "skill_id": "9702_skill_apply_elastic_potential_energy",
        "accepted_answer": "D",
        "hints": [
            "Recall that the elastic strain energy stored in a stretched material obeying Hooke's law is given by $E = \\frac{1}{2}Fx$.",
            "Calculate the strain energy for string X ($F, x$) and string Y ($2F, 2x$) and determine the ratio $\\frac{E_X}{E_Y}$."
        ],
        "walkthrough": [
            "For a material obeying Hooke's law, the strain energy stored is equal to the area under the force-extension graph: $E = \\frac{1}{2} F x$.",
            "For string X, the strain energy is $E_X = \\frac{1}{2} F x$.",
            "For string Y, the force is $2F$ and the extension is $2x$, so its strain energy is $E_Y = \\frac{1}{2} (2F) (2x) = 4 \\left(\\frac{1}{2} F x\\right) = 4 E_X$.",
            "The ratio $\\frac{\\text{strain energy in string X}}{\\text{strain energy in string Y}} = \\frac{E_X}{4E_X} = \\frac{1}{4}$, which corresponds to option D."
        ]
    },
    21: {
        "difficulty": 1,
        "question_patterns": ["property_identification", "classification"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m04",
        "skill_id": "9702_skill_identify_electromagnetic_spectrum_region",
        "accepted_answer": "B",
        "hints": [
            "Recall that all electromagnetic waves travel at the same speed $c$ in a vacuum.",
            "Consider what physical parameter uniquely distinguishes different colours in the visible spectrum."
        ],
        "walkthrough": [
            "In a vacuum, all electromagnetic waves travel at the exact same invariant speed $c = 3.00 \\times 10^8\\text{ m s}^{-1}$, eliminating option D.",
            "The colour of visible light is determined by its wavelength and frequency ($c = f\\lambda$). Red light has a longer wavelength (around $ 650\\text{ nm} $) and lower frequency than green light (around $ 530\\text{ nm} $). Therefore, the frequencies of the two lasers must be different, which is option B.",
            "The amplitude and intensity depend on the output power of the lasers and beam geometry, so they could easily be equal."
        ]
    },
    22: {
        "difficulty": 3,
        "question_patterns": ["graph_interpretation", "property_identification"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m02",
        "skill_id": "9702_skill_define_longitudinal_wave",
        "accepted_answer": "A",
        "hints": [
            "Observe the phase relationship between the two displacement-time graphs.",
            "Notice that the two particles are in antiphase (phase difference $\\pi\\text{ rad}$ or $ 180^\\circ $), which corresponds to a spatial separation of half a wavelength $\\frac{\\lambda}{2}$."
        ],
        "walkthrough": [
            "The displacement-time graphs show that when one particle has maximum positive displacement, the other has maximum negative displacement. This indicates that the two particles oscillate completely in antiphase ($ 180^\\circ $ or $\\pi\\text{ rad}$ out of phase).",
            "In a progressive wave, points separated by distance $x = 10\\text{ cm}$ that oscillate in antiphase are separated by half a wavelength: $\\frac{\\lambda}{2} = 10\\text{ cm} \\implies \\lambda = 20\\text{ cm}$.",
            "In a longitudinal wave, the distance between the centre of a compression and the centre of the nearest rarefaction is exactly half a wavelength ($\\frac{\\lambda}{2} = 10\\text{ cm}$). This matches option A.",
            "Option B incorrectly states the compression-rarefaction distance as $ 20\\text{ cm} $, while option C describes a peak-to-trough distance of $ 20\\text{ cm} $ for a transverse wave with $\\lambda = 20\\text{ cm}$ (which should be $ 10\\text{ cm} $)."
        ]
    },
    23: {
        "difficulty": 2,
        "question_patterns": ["measurement_selection", "direct_calculation"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_interpret_oscilloscope_traces",
        "accepted_answer": "B",
        "hints": [
            "Count the number of horizontal divisions corresponding to one full cycle (or multiple full cycles for greater precision) on the cathode-ray oscilloscope screen.",
            "Multiply the horizontal division count by the time-base setting ($ 20\\ \\mu\\text{s div}^{-1} $) to find period $T$, then calculate frequency $f = \\frac{1}{T}$."
        ],
        "walkthrough": [
            "From the CRO display, 3 complete wave cycles occupy 10 horizontal divisions, so one complete oscillation occupies $\\frac{10}{3} \\approx 3.33\\text{ divisions}$.",
            "With the time-base setting of $ 20\\ \\mu\\text{s div}^{-1} = 20 \\times 10^{-6}\\text{ s div}^{-1} $, the period of one cycle is $T = \\frac{10}{3} \\times 20 \\times 10^{-6}\\text{ s} = 6.67 \\times 10^{-5}\\text{ s}$.",
            "The frequency is $f = \\frac{1}{T} = \\frac{1}{6.67 \\times 10^{-5}\\text{ s}} = 15000\\text{ Hz} = 15\\text{ kHz}$, which matches option B."
        ]
    },
    24: {
        "difficulty": 3,
        "question_patterns": ["multi_step_calculation", "direct_calculation"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m03",
        "skill_id": "9702_skill_apply_doppler_effect",
        "accepted_answer": "A",
        "hints": [
            "Set up Doppler effect equations for an approaching source ($f_o = f_s \\frac{v}{v - v_s}$) and a receding source ($f_o' = f_s \\frac{v}{v + v_s}$).",
            "Divide the two equations to eliminate source frequency $f_s$, and solve the resulting linear equation for the train speed $v_s$ using $v = 340\\text{ m s}^{-1}$."
        ],
        "walkthrough": [
            "For an approaching source, the observed frequency is $f_1 = f_s \\left(\\frac{v}{v - v_s}\\right) = 1690\\text{ Hz}$.",
            "For a receding source, the observed frequency is $f_2 = f_s \\left(\\frac{v}{v + v_s}\\right) = 1500\\text{ Hz}$.",
            "Dividing $f_1$ by $f_2$ eliminates $f_s$: $\\frac{1690}{1500} = \\frac{v + v_s}{v - v_s} \\implies \\frac{169}{150} = \\frac{340 + v_s}{340 - v_s}$.",
            "Cross-multiplying gives $ 169(340 - v_s) = 150(340 + v_s) \\implies 169 \\times 340 - 169v_s = 150 \\times 340 + 150v_s $.",
            "Rearranging: $(169 - 150) \\times 340 = (169 + 150) v_s \\implies 19 \\times 340 = 319 v_s \\implies v_s = \\frac{6460}{319} \\approx 20.25\\text{ m s}^{-1} \\approx 20\\text{ m s}^{-1}$, corresponding to option A."
        ]
    },
    25: {
        "difficulty": 1,
        "question_patterns": ["classification", "property_identification"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m04",
        "skill_id": "9702_skill_identify_electromagnetic_spectrum_region",
        "accepted_answer": "B",
        "hints": [
            "Recall the order of the electromagnetic spectrum arranged from highest energy/frequency to lowest.",
            "Verify that frequency decreases from gamma rays through ultraviolet and infrared down to radio waves."
        ],
        "walkthrough": [
            "The electromagnetic spectrum arranged in order of decreasing frequency (increasing wavelength) is: gamma rays $\\rightarrow$ X-rays $\\rightarrow$ ultraviolet $\\rightarrow$ visible light $\\rightarrow$ infrared $\\rightarrow$ microwaves $\\rightarrow$ radio waves.",
            "Checking sequence B: gamma-rays (highest frequency, $\\sim 10^{20}\\text{ Hz}$) $\\rightarrow$ ultraviolet ($\\sim 10^{15}\\text{ Hz}$) $\\rightarrow$ infrared ($\\sim 10^{13}\\text{ Hz}$) $\\rightarrow$ radio waves (lowest frequency, $\\sim 10^{6}\\text{ Hz}$).",
            "This sequence strictly decreases in frequency, matching option B."
        ]
    },
    26: {
        "difficulty": 2,
        "question_patterns": ["equation_derivation", "property_identification"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m01",
        "skill_id": "9702_skill_explain_stationary_waves",
        "accepted_answer": "C",
        "hints": [
            "State the boundary conditions for a pipe closed at one end and open at the other: a displacement node at the closed end and a displacement antinode at the open end.",
            "Write the formula for the allowed resonant lengths $L = (2n - 1)\\frac{\\lambda}{4}$ (for $n = 1, 2, 3, \\dots$) and solve for allowed wavelengths $\\lambda$."
        ],
        "walkthrough": [
            "For a pipe of length $L$ closed at one end and open at the other, a stationary wave forms with a displacement node at the closed end and a displacement antinode at the open end.",
            "The possible pipe lengths for resonance are odd quarter-wavelengths: $L = \\frac{\\lambda}{4}, \\frac{3\\lambda}{4}, \\frac{5\\lambda}{4}, \\dots = (2n-1)\\frac{\\lambda}{4}$, where $n = 1, 2, 3, \\dots$",
            "Rearranging for the allowed wavelengths gives $\\lambda = \\frac{4L}{2n - 1}$: for $n = 1$, $\\lambda = 4L$; for $n = 2$, $\\lambda = \\frac{4}{3}L$; for $n = 3$, $\\lambda = \\frac{4}{5}L$.",
            "Comparing with the options, $\\lambda = \\frac{4}{3}L$ matches option C."
        ]
    },
    27: {
        "difficulty": 1,
        "question_patterns": ["graph_interpretation", "property_identification"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m02",
        "skill_id": "9702_skill_explain_diffraction",
        "accepted_answer": "B",
        "hints": [
            "Recall that diffraction occurs when waves encounter an obstacle or gap, with maximum spreading occurring when the gap size is comparable to the wavelength.",
            "Check that the wavelength (spacing between successive wavefronts) remains constant before and after passing through the gap."
        ],
        "walkthrough": [
            "When straight parallel wavefronts pass through a narrow slit whose width is comparable to the wavelength, they spread out into circular/curved wavefronts that extend into the geometric shadow region behind the barrier.",
            "Because the speed and frequency of the water waves do not change during diffraction, the wavelength (distance between adjacent wavefronts) must remain identical before and after passing through the gap.",
            "Diagram B correctly depicts circular spreading with unchanged wavefront spacing, while other diagrams incorrectly show straight uncurved waves or incorrect wave curvature."
        ]
    },
    28: {
        "difficulty": 1,
        "question_patterns": ["definition", "property_identification"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m03",
        "skill_id": "9702_skill_define_coherence",
        "accepted_answer": "B",
        "hints": [
            "Recall the standard AS Physics definition of coherence for wave sources.",
            "Distinguish between having a constant phase difference and strictly being in phase (zero phase difference)."
        ],
        "walkthrough": [
            "Two wave sources are defined as coherent if they maintain a constant phase difference between them over time.",
            "Option A is a special case (zero phase difference), but coherence only requires the phase difference to be constant, not necessarily zero.",
            "Options C (same amplitude) and D (interference condition) are not parts of the definition of coherence. Thus, option B is correct."
        ]
    },
    29: {
        "difficulty": 3,
        "question_patterns": ["multi_step_calculation", "interference_analysis"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m04",
        "skill_id": "9702_skill_apply_diffraction_grating",
        "accepted_answer": "C",
        "hints": [
            "Apply the grating equation $d\\sin\\theta = n\\lambda$ to both wavelengths at the overlapping angle $\\theta = 31^\\circ$.",
            "Equate $n_1 \\lambda_1 = n_2 \\lambda_2$ to find the smallest non-zero integer orders ($n_1, n_2$), then solve for grating spacing $d$."
        ],
        "walkthrough": [
            "The diffraction grating equation is $d\\sin\\theta = n\\lambda$. For maxima of two wavelengths $\\lambda_1 = 420\\text{ nm}$ and $\\lambda_2 = 630\\text{ nm}$ to coincide at angle $\\theta$, their path differences must match: $n_1 \\lambda_1 = n_2 \\lambda_2$.",
            "This gives the ratio $\\frac{n_1}{n_2} = \\frac{\\lambda_2}{\\lambda_1} = \\frac{630\\text{ nm}}{420\\text{ nm}} = \\frac{3}{2}$. The lowest non-zero integer orders that overlap are $n_1 = 3$ and $n_2 = 2$.",
            "At $\\theta = 31^\\circ$: $d\\sin(31^\\circ) = 3 \\times 420 \\times 10^{-9}\\text{ m} = 1.26 \\times 10^{-6}\\text{ m}$.",
            "Solving for line spacing: $d = \\frac{1.26 \\times 10^{-6}\\text{ m}}{\\sin(31^\\circ)} = \\frac{1.26 \\times 10^{-6}}{0.5150} \\approx 2.45 \\times 10^{-6}\\text{ m} = 2.4\\ \\mu\\text{m}$, which matches option C."
        ]
    },
    30: {
        "difficulty": 2,
        "question_patterns": ["explanation", "property_identification"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_describe_uniform_electric_field_lines",
        "accepted_answer": "A",
        "hints": [
            "Recall what evenly spaced parallel field lines indicate about the electric field strength $E$.",
            "Relate the electric force $F = qE$ on particle P to the electric field strength across the region."
        ],
        "walkthrough": [
            "Evenly spaced, parallel field lines represent a uniform electric field, where the electric field strength $E$ is constant in both magnitude and direction throughout the region.",
            "The electric force acting on a point charge $q$ is given by $F = qE$. Since $E$ is uniform everywhere, moving the particle a small distance in any direction does not change the magnitude or direction of the electric force acting on it.",
            "Statements B, C, and D incorrectly claim the force increases when displaced along specific directions, which would only occur in non-uniform fields. Hence, option A is correct."
        ]
    },
    31: {
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "property_identification"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_apply_uniform_electric_field",
        "accepted_answer": "D",
        "hints": [
            "Calculate the electric field magnitude between parallel plates using $E = \\frac{\\Delta V}{d}$.",
            "Determine the direction of the electric field by remembering that field lines always point from higher electric potential to lower electric potential."
        ],
        "walkthrough": [
            "The potential difference between plates P ($-700\\text{ V}$) and Q ($0\\text{ V}$) is $\\Delta V = 700\\text{ V}$, and the plate separation is $d = 5.0\\text{ mm} = 5.0 \\times 10^{-3}\\text{ m}$.",
            "The magnitude of the uniform electric field is $E = \\frac{\\Delta V}{d} = \\frac{700\\text{ V}}{5.0 \\times 10^{-3}\\text{ m}} = 1.4 \\times 10^5\\text{ V m}^{-1} = 1.4 \\times 10^5\\text{ N C}^{-1}$.",
            "Electric field lines point in the direction of decreasing potential (from higher potential to lower potential). Since Plate Q is at $0\\text{ V}$ and Plate P is at $-700\\text{ V}$, the field points from Q towards P.",
            "This combination of magnitude and direction corresponds to option D."
        ]
    },
    32: {
        "difficulty": 2,
        "question_patterns": ["graph_interpretation", "equation_derivation"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m01",
        "skill_id": "9702_skill_sketch_drift_speed_from_varying_area",
        "accepted_answer": "A",
        "hints": [
            "Recall the microscopic drift velocity formula $I = n A v q$ and solve for $v$.",
            "Analyze how the cross-sectional area $A$ varies from narrow end X to wider end Y, and deduce how drift velocity $v$ varies with distance $x$."
        ],
        "walkthrough": [
            "The current $I$ is constant along the entire length of the series conductor. The drift velocity is related to current by $I = n A v q$, so $v = \\frac{I}{n A q} \\propto \\frac{1}{A}$.",
            "The wedge conductor has uniform thickness, but its width increases linearly with distance $x$ from end X, so the cross-sectional area increases linearly with $x$: $A(x) = kx + c$.",
            "Therefore, drift velocity varies inversely with distance: $v(x) \\propto \\frac{1}{kx + c}$. At end X ($x = 0$), $A$ is smallest, so $v$ is at its maximum. As $x$ increases towards Y, $v$ decreases non-linearly with an asymptotic curve concave upwards, matching graph A.",
            "Graphs B and D show incorrect linear variations, while C shows velocity increasing with distance."
        ]
    },
    33: {
        "difficulty": 2,
        "question_patterns": ["multi_step_calculation", "circuit_analysis"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_calculate_electrical_power",
        "accepted_answer": "A",
        "hints": [
            "Calculate the circuit current using the supply power and voltage: $I = \\frac{P_{\\text{supply}}}{V_{\\text{supply}}}$.",
            "Calculate the total voltage drop in the two connecting wires ($V_{\\text{wires}} = I \\times R_{\\text{wires}}$) and subtract from the supply voltage to find the p.d. across the kettle, then calculate the power delivered to the kettle."
        ],
        "walkthrough": [
            "The current leaving the supply is $I = \\frac{P_{\\text{supply}}}{V_{\\text{supply}}} = \\frac{2.4 \\times 10^3\\text{ W}}{240\\text{ V}} = 10\\text{ A}$.",
            "The two connecting wires each have a resistance of $0.50\\ \\Omega$, so the total wire resistance is $R_{\\text{wires}} = 0.50 + 0.50 = 1.0\\ \\Omega$.",
            "The potential difference dropped across the connecting wires is $V_{\\text{wires}} = I R_{\\text{wires}} = 10\\text{ A} \\times 1.0\\ \\Omega = 10\\text{ V}$.",
            "The p.d. across the kettle is $V_{\\text{kettle}} = 240\\text{ V} - 10\\text{ V} = 230\\text{ V}$. The power delivered to the kettle is $P_{\\text{kettle}} = I V_{\\text{kettle}} = 10\\text{ A} \\times 230\\text{ V} = 2300\\text{ W} = 2.3\\text{ kW}$. This matches row A."
        ]
    },
    34: {
        "difficulty": 2,
        "question_patterns": ["graph_interpretation", "classification"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m03",
        "skill_id": "9702_skill_analyse_filament_lamp_resistance",
        "accepted_answer": "B",
        "hints": [
            "Identify the linear $I-V$ characteristic of an Ohmic metallic conductor at constant temperature.",
            "Recall how the resistance of a filament lamp increases with temperature (causing the $I-V$ gradient to decrease), and recognize the threshold turn-on behavior of a semiconductor diode."
        ],
        "walkthrough": [
            "Component Z displays a straight line passing through the origin, indicating constant resistance ($I \\propto V$), which is characteristic of an Ohmic metallic conductor at constant temperature.",
            "Component Y exhibits negligible current below a threshold forward voltage and then conducts strongly, which is characteristic of a semiconductor diode.",
            "Component X has a decreasing gradient $\\frac{\\Delta I}{\\Delta V}$ as $V$ increases, indicating that resistance $R = \\frac{V}{I}$ increases due to filament heating, characteristic of a filament lamp.",
            "Matching the components: semiconductor diode is Y, filament lamp is X, and metallic conductor is Z, which corresponds to option B."
        ]
    },
    35: {
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "multi_step_calculation"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m03",
        "skill_id": "9702_skill_apply_resistivity",
        "accepted_answer": "A",
        "hints": [
            "Calculate the circular cross-sectional area of the wire from its diameter $d = 0.280\\text{ mm} = 2.80 \\times 10^{-4}\\text{ m}$.",
            "Use the resistivity formula $R = \\frac{\\rho L}{A}$ and rearrange to solve for the length $L = \\frac{R A}{\\rho}$."
        ],
        "walkthrough": [
            "The cross-sectional area of the wire is $A = \\frac{\\pi d^2}{4} = \\frac{\\pi (0.280 \\times 10^{-3}\\text{ m})^2}{4} \\approx 6.158 \\times 10^{-8}\\text{ m}^2$.",
            "Using the resistivity equation $R = \\frac{\\rho L}{A}$, rearrange for length: $L = \\frac{R A}{\\rho}$.",
            "Substituting the given values: $L = \\frac{9.55\\ \\Omega \\times 6.158 \\times 10^{-8}\\text{ m}^2}{4.90 \\times 10^{-7}\\ \\Omega\\text{ m}} = \\frac{5.881 \\times 10^{-7}}{4.90 \\times 10^{-7}} \\approx 1.20\\text{ m}$, which matches option A."
        ]
    },
    36: {
        "difficulty": 3,
        "question_patterns": ["circuit_analysis", "explanation"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_explain_emf_internal_resistance",
        "accepted_answer": "C",
        "hints": [
            "Determine whether moving sliding contact Z towards X increases or decreases the total resistance of the external circuit.",
            "Apply the terminal potential difference formula $V = E - Ir$ and analyze how changes in circuit current $I$ affect the terminal p.d. measured across the cell."
        ],
        "walkthrough": [
            "Moving the sliding contact Z towards end X increases the length and therefore the resistance of the potentiometer wire connected in series with the circuit.",
            "As total external resistance increases, the total current $I = \\frac{E}{R_{\\text{ext}} + r}$ drawn from the cell decreases.",
            "The voltmeter measures terminal potential difference across the cell, given by $V = E - Ir$. As current $I$ decreases, the lost volts ($Ir$) decrease, which causes the terminal potential difference $V$ to increase.",
            "This corresponds to statement C: the voltmeter reading increases because the current through the cell decreases."
        ]
    },
    37: {
        "difficulty": 1,
        "question_patterns": ["definition", "equation_recall"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m02",
        "skill_id": "9702_skill_define_kirchhoffs_first_law",
        "accepted_answer": "A",
        "hints": [
            "Recall that Kirchhoff's first law expresses the principle of conservation of electric charge at any circuit junction.",
            "Equate the sum of currents entering the junction to the sum of currents leaving the junction."
        ],
        "walkthrough": [
            "Kirchhoff's first law states that the total current entering a junction must equal the total current leaving that junction, which is a consequence of charge conservation ($\\Sigma I_{\\text{in}} = \\Sigma I_{\\text{out}}$).",
            "In the given circuit, current $I_1$ enters the parallel junction and splits into branch currents $I_2$ and $I_3$, so $I_1 = I_2 + I_3$.",
            "This equation is given by option A. (Options C and D represent Kirchhoff's second law / potential statements)."
        ]
    },
    38: {
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "circuit_analysis"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m03",
        "skill_id": "9702_skill_calculate_series_circuit_potential_difference",
        "accepted_answer": "C",
        "hints": [
            "Determine the potential difference across resistor $R$ when the $ 12\\text{ k}\\Omega $ resistor has $ 1.0\\text{ V} $ across it from a total supply of $ 6.0\\text{ V} $.",
            "Use the potential divider ratio $\\frac{V_R}{V_{12\\text{k}}} = \\frac{R}{12\\text{ k}\\Omega}$ to solve for resistance $R$."
        ],
        "walkthrough": [
            "In a series circuit connected to a $ 6.0\\text{ V} $ supply, the total potential difference is shared between the two resistors: $V_{\\text{supply}} = V_R + V_{12\\text{k}}$.",
            "If the p.d. across the $ 12\\text{ k}\\Omega $ resistor is $V_{12\\text{k}} = 1.0\\text{ V}$, then the p.d. across the variable resistor is $V_R = 6.0\\text{ V} - 1.0\\text{ V} = 5.0\\text{ V}$.",
            "Since the same current passes through both resistors in series, $\\frac{V_R}{V_{12\\text{k}}} = \\frac{R}{12\\text{ k}\\Omega} \\implies \\frac{5.0\\text{ V}}{1.0\\text{ V}} = \\frac{R}{12\\text{ k}\\Omega}$.",
            "Solving for $R$ gives $R = 5.0 \\times 12\\text{ k}\\Omega = 60\\text{ k}\\Omega$, which is option C."
        ]
    },
    39: {
        "difficulty": 1,
        "question_patterns": ["equation_completion", "property_identification"],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m01",
        "skill_id": "9702_skill_complete_nuclear_equations",
        "accepted_answer": "C",
        "hints": [
            "Apply conservation of nucleon number (top numbers) and conservation of proton number / charge (bottom numbers) across the nuclear decay.",
            "Note that a $\\beta^+$ particle (positron) has nucleon number $0$ and proton number $+1$ (${^0_1}\\beta^+$)."
        ],
        "walkthrough": [
            "In the $\\beta^+$ decay reaction $^{23}_{12}\\text{Mg} \\rightarrow {^P_Q}\\text{X} + {^0_1}\\beta^+$, both total nucleon number and total proton number are conserved.",
            "Conserving nucleon number (mass number): $ 23 = P + 0 \\implies P = 23 $.",
            "Conserving proton number (atomic number / charge): $ 12 = Q + 1 \\implies Q = 12 - 1 = 11 $.",
            "Therefore, $P = 23$ and $Q = 11$, which corresponds to option C (forming sodium-23, $^{23}_{11}\\text{Na}$)."
        ]
    },
    40: {
        "difficulty": 1,
        "question_patterns": ["particle_model_application", "property_identification"],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m02",
        "skill_id": "9702_skill_describe_beta_decay_quark_change",
        "accepted_answer": "A",
        "hints": [
            "Recall the quark composition of a neutron ($udd$) and a proton ($uud$).",
            "Identify the specific quark transformation that converts a neutron into a proton during $\\beta^-$ decay."
        ],
        "walkthrough": [
            "A neutron has a quark structure of $udd$ (one up quark and two down quarks), whereas a proton has a quark structure of $uud$ (two up quarks and one down quark).",
            "During $\\beta^-$ decay, a neutron converts into a proton via the weak interaction: $d \\rightarrow u + e^- + \\bar{\\nu}_e$.",
            "This means one down quark transforms into an up quark, so the number of down quarks decreases by one (and the number of up quarks increases by one).",
            "Statement A correctly states that the number of down quarks decreases by one."
        ]
    }
}

target_dir = Path("subjects/physics/9702/enrichment/p1")
target_dir.mkdir(parents=True, exist_ok=True)

paper_code = "9702_s21_12"

# Pre-check for any PID artifacts
for qnum, data in enrichments.items():
    full_text = " ".join(data["hints"]) + " " + " ".join(data["walkthrough"])
    pid_matches = re.findall(r'[\$]{1,2}\d{2,}', full_text)
    if pid_matches:
        print(f"Warning: Q{qnum} has pid matches: {pid_matches}")

for qnum in range(1, 41):
    q_id = f"{paper_code}_q{qnum:02d}"
    data = enrichments[qnum]
    record = {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": q_id,
        "component": "P1",
        "difficulty": data["difficulty"],
        "question_patterns": data["question_patterns"],
        "topic_id": data["topic_id"],
        "module_id": data["module_id"],
        "skill_id": data["skill_id"],
        "accepted_answer": data["accepted_answer"],
        "hints": data["hints"],
        "walkthrough": data["walkthrough"]
    }
    
    out_file = target_dir / f"{q_id}.enrichment.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2, ensure_ascii=False)
        f.write("\n")

print("Generated all 40 files cleanly.")
