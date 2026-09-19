#!/usr/bin/env python3
"""
generate_9702_w21_12.py

Generates flat enrichment JSON records for 9702_w21_12 (Questions 01 to 40)
matching schema 9702_p1_enrichment_v1.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENRICH_DIR = ROOT / 'subjects/physics/9702/enrichment/p1'
ENRICH_DIR.mkdir(parents=True, exist_ok=True)

data = [
    {
        "question_id": "9702_w21_12_q01",
        "difficulty": 1,
        "question_patterns": ["definition", "property_identification"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m01",
        "skill_id": "9702_skill_si_units_homogeneity",
        "accepted_answer": "C",
        "hints": [
            "Recall that every physical quantity consists of a numerical magnitude and an appropriate unit.",
            "Consider whether scalar quantities (such as mass, time, or temperature) possess direction."
        ],
        "walkthrough": [
            "A physical quantity is defined as any property of an object or system that can be quantified by measurement; it always consists of a numerical magnitude and a unit.",
            "Direction is only a property of vector quantities (e.g. force, velocity), whereas scalar quantities (e.g. temperature, mass) do not have direction.",
            "Therefore, all physical quantities must possess magnitude and a unit, but do not necessarily have direction, which corresponds to row C."
        ]
    },
    {
        "question_id": "9702_w21_12_q02",
        "difficulty": 1,
        "question_patterns": ["direct_calculation", "property_identification"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m02",
        "skill_id": "9702_skill_si_units_homogeneity",
        "accepted_answer": "A",
        "hints": [
            "Recall the standard SI prefix multipliers: deci (d) is 10⁻¹, milli (m) is 10⁻³, and mega (M) is 10⁶.",
            "Convert 43 dJ to base joules first, then convert into millijoules (mJ)."
        ],
        "walkthrough": [
            "The prefix deci (d) corresponds to a factor of 10⁻¹. Thus, 43 dJ = 43 × 10⁻¹ J = 4.3 J.",
            "To express 4.3 J in millijoules (mJ), where 1 mJ = 10⁻³ J, divide by 10⁻³: 4.3 J / 10⁻³ J mJ⁻¹ = 4.3 × 10³ mJ.",
            "This matches option A. Options B and D mistakenly use mega (M), and option C has an incorrect negative exponent."
        ]
    },
    {
        "question_id": "9702_w21_12_q03",
        "difficulty": 1,
        "question_patterns": ["equation_derivation", "property_identification"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m04",
        "skill_id": "9702_skill_scalars_vectors",
        "accepted_answer": "D",
        "hints": [
            "Use the Pythagorean theorem for the perpendicular velocity components: v² = v_x² + v_y².",
            "Rearrange the relationship to express the horizontal component v_x in terms of total speed v and vertical component v_y."
        ],
        "walkthrough": [
            "The total velocity vector v resolves into perpendicular horizontal (v_x) and vertical (v_y) components such that v² = v_x² + v_y².",
            "Rearranging for the magnitude of the horizontal component yields v_x² = v² - v_y², which gives v_x = (v² - v_y²)^(1/2).",
            "This corresponds to option D. Option A gives v sin θ, which represents the vertical component v_y, while options B and C are incorrect trigonometric combinations."
        ]
    },
    {
        "question_id": "9702_w21_12_q04",
        "difficulty": 2,
        "question_patterns": ["graph_interpretation", "comparison"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_oscilloscope_traces",
        "accepted_answer": "A",
        "hints": [
            "Determine the period T of each waveform by multiplying the number of horizontal divisions per full cycle by the corresponding time-base setting (T = divisions × time-base).",
            "Identify which two screens have identical period values T, as frequency is related to period by f = 1/T."
        ],
        "walkthrough": [
            "For screen 1, one complete wave cycle spans 4 horizontal divisions with a time-base setting of 0.02 s/div, giving period T₁ = 4 × 0.02 s = 0.08 s.",
            "For screen 2, one complete cycle spans 2 horizontal divisions with a time-base setting of 0.04 s/div, giving period T₂ = 2 × 0.04 s = 0.08 s.",
            "Since f = 1/T, both waveforms 1 and 2 have identical periods (0.08 s) and therefore identical frequencies (f = 12.5 Hz), making option A correct."
        ]
    },
    {
        "question_id": "9702_w21_12_q05",
        "difficulty": 2,
        "question_patterns": ["uncertainty_analysis", "multi_step_calculation"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m03",
        "skill_id": "9702_skill_errors_uncertainties",
        "accepted_answer": "D",
        "hints": [
            "Rearrange the pendulum formula T = 2π √(l/g) for g: g = 4π² l / T².",
            "Combine the percentage uncertainties: %Δg = %Δl + 2(%ΔT)."
        ],
        "walkthrough": [
            "Squaring the pendulum period equation T = 2π √(l/g) and rearranging gives g = 4π² l / T².",
            "The fractional uncertainty in g is the sum of fractional uncertainties in l and twice that of T: Δg/g = Δl/l + 2(ΔT/T).",
            "Calculating individual percentage uncertainties: %Δl = (0.001 / 0.420) × 100% ≈ 0.24% and 2 × %ΔT = 2 × (0.1 / 1.3) × 100% ≈ 15.38%.",
            "Summing these contributions gives %Δg = 0.24% + 15.38% = 15.62% ≈ 16%, which corresponds to option D."
        ]
    },
    {
        "question_id": "9702_w21_12_q06",
        "difficulty": 2,
        "question_patterns": ["graph_interpretation", "direct_calculation"],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_motion_graphs",
        "accepted_answer": "C",
        "hints": [
            "Recall that instantaneous acceleration on a velocity–time graph equals the gradient of the tangent to the curve at that time.",
            "Construct a tangent line to the curve at t = 3.0 s and calculate its slope Δv / Δt."
        ],
        "walkthrough": [
            "Acceleration is the gradient of the velocity–time graph (a = dv/dt).",
            "Drawing a tangent to the curve at t = 3.0 s, the tangent passes through approximately (0 s, 4.0 m s⁻¹) and (6.0 s, 12.0 m s⁻¹).",
            "The gradient of this tangent line is a = (12.0 - 4.0) / (6.0 - 0) = 8.0 m s⁻¹ / 6.0 s ≈ 1.33 m s⁻² ≈ 1.3 m s⁻², matching option C."
        ]
    },
    {
        "question_id": "9702_w21_12_q07",
        "difficulty": 1,
        "question_patterns": ["direct_calculation"],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_kinematics_equations",
        "accepted_answer": "B",
        "hints": [
            "At maximum height, the vertical speed of the stone reaches zero (v = 0).",
            "Use the kinematic equation v² = u² + 2as with u = 15 m s⁻¹ and a = -9.81 m s⁻²."
        ],
        "walkthrough": [
            "At the maximum height of vertical motion, the instantaneous velocity is v = 0 m s⁻¹.",
            "Applying the equation of uniformly accelerated motion v² = u² + 2as with initial velocity u = 15 m s⁻¹ and downward acceleration a = -g = -9.81 m s⁻²: 0 = 15² - 2(9.81)s.",
            "Solving for height s: s = 225 / (2 × 9.81) ≈ 11.47 m ≈ 11 m, which matches option B."
        ]
    },
    {
        "question_id": "9702_w21_12_q08",
        "difficulty": 1,
        "question_patterns": ["definition", "property_identification"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_newtons_laws",
        "accepted_answer": "A",
        "hints": [
            "Recall the definition of mass in terms of inertia and resistance to acceleration.",
            "Distinguish mass (an intrinsic property resisting change in motion) from weight (the gravitational force acting on it)."
        ],
        "walkthrough": [
            "Mass is fundamentally defined as the property of an object that resists changes in its state of rest or motion (inertia).",
            "Options B and D describe weight (the gravitational pull on the object), while option C refers to the quantity of matter/atoms rather than the physical definition of mass in dynamics. Statement A is correct."
        ]
    },
    {
        "question_id": "9702_w21_12_q09",
        "difficulty": 2,
        "question_patterns": ["comparison", "equation_derivation"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_newtons_laws",
        "accepted_answer": "B",
        "hints": [
            "Apply Newton's second law for a falling body with upward air resistance: F_net = mg - D = ma.",
            "Express acceleration as a = g - D/m and substitute m_Y = 2m_X and D_Y = 2D_X."
        ],
        "walkthrough": [
            "For a falling parachutist subjected to downward gravitational force W = mg and upward drag force D, the equation of motion is mg - D = ma, which simplifies to a = g - D/m.",
            "For parachutist X, the acceleration is a_X = g - D_X / m_X.",
            "For parachutist Y, substituting m_Y = 2m_X and D_Y = 2D_X: a_Y = g - 2D_X / (2m_X) = g - D_X / m_X = a_X.",
            "Since the drag-to-mass ratio is identical for both parachutists, their accelerations are the same, confirming option B."
        ]
    },
    {
        "question_id": "9702_w21_12_q10",
        "difficulty": 2,
        "question_patterns": ["comparison", "property_identification"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m03",
        "skill_id": "9702_skill_relative_speed_elastic_collision",
        "accepted_answer": "D",
        "hints": [
            "In a perfectly elastic collision, both total linear momentum and total kinetic energy are conserved.",
            "Check that relative speed of approach equals relative speed of separation: |u₁ - u₂| = |v₂ - v₁|."
        ],
        "walkthrough": [
            "A collision is defined as perfectly elastic if and only if total kinetic energy is conserved before and after the collision (E_k,before = E_k,after).",
            "For two equal masses undergoing an elastic collision, relative speed of approach equals relative speed of separation.",
            "In collision D, both linear momentum and total kinetic energy are completely conserved, confirming that collision D is perfectly elastic."
        ]
    },
    {
        "question_id": "9702_w21_12_q11",
        "difficulty": 1,
        "question_patterns": ["equation_derivation", "property_identification"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m03",
        "skill_id": "9702_skill_upthrust_archimedes",
        "accepted_answer": "B",
        "hints": [
            "Recall that upthrust is the resultant upward force exerted by fluid pressure on the top and bottom faces of the cylinder.",
            "The upward force on the bottom is p_b A and the downward force on the top is p_t A."
        ],
        "walkthrough": [
            "Upthrust is defined as the net upward force exerted by a fluid on an immersed object due to the hydrostatic pressure difference between its bottom and top surfaces.",
            "The fluid exerts a downward force on the top face equal to F_top = p_t A and an upward force on the bottom face equal to F_bottom = p_b A.",
            "The net upward force (upthrust) is F_bottom - F_top = (p_b - p_t)A, matching option B. The weight W of the block is a separate downward force and does not enter the definition of the upthrust from the liquid."
        ]
    },
    {
        "question_id": "9702_w21_12_q12",
        "difficulty": 1,
        "question_patterns": ["definition", "direct_calculation"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_moments_couples",
        "accepted_answer": "C",
        "hints": [
            "Recognize that the two equal and opposite parallel forces form a couple.",
            "The torque of a couple is equal to the product of one of the forces and the perpendicular distance between their lines of action."
        ],
        "walkthrough": [
            "A couple consists of a pair of equal and opposite parallel forces whose lines of action do not coincide.",
            "The torque of a couple is given by τ = F × d, where F is the magnitude of one force and d is the perpendicular distance between the lines of action of the two forces.",
            "In this diagram, the two forces act tangentially on opposite edges of a disc of diameter s, so the perpendicular separation is s. The torque is therefore F s, which corresponds to option C."
        ]
    },
    {
        "question_id": "9702_w21_12_q13",
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "multi_step_calculation"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_moments_couples",
        "accepted_answer": "C",
        "hints": [
            "Calculate the weight of the 500 g mass in newtons: W = mg = 0.500 × 9.81 N.",
            "Determine the perpendicular distance from the pivot to the mass: d = 1.50 m - 0.25 m = 1.25 m."
        ],
        "walkthrough": [
            "The weight of the attached mass is W = mg = 0.500 kg × 9.81 m s⁻² = 4.905 N.",
            "The rod has a total length of 1.50 m, and the pivot is located 25 cm = 0.25 m from the opposite end. The distance from the pivot to the mass is therefore d = 1.50 m - 0.25 m = 1.25 m.",
            "The moment about the pivot is Moment = W × d = 4.905 N × 1.25 m ≈ 6.13 N m ≈ 6.1 N m, which is option C."
        ]
    },
    {
        "question_id": "9702_w21_12_q14",
        "difficulty": 2,
        "question_patterns": ["multi_step_calculation", "force_diagram_construction"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m02",
        "skill_id": "9702_skill_equilibrium_coplanar_forces",
        "accepted_answer": "D",
        "hints": [
            "Consider the equilibrium of forces acting at joint Q in the vertical direction.",
            "Resolve the thrust force along beam QR vertically: F_beam sin(30°) = 4.0 kN."
        ],
        "walkthrough": [
            "At joint Q, three coplanar forces are in equilibrium: the downward load W = 4.0 kN, the horizontal tension in wire PQ, and the compressive force F along beam QR inclined at 30° to the horizontal.",
            "Resolving forces vertically at point Q: the upward component of the force exerted by the beam must balance the downward load: F sin(30°) = 4.0 kN.",
            "Solving for F: F = 4.0 kN / sin(30°) = 4.0 kN / 0.50 = 8.0 kN, which corresponds to option D."
        ]
    },
    {
        "question_id": "9702_w21_12_q15",
        "difficulty": 2,
        "question_patterns": ["graph_interpretation", "property_identification"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m03",
        "skill_id": "9702_skill_upthrust_archimedes",
        "accepted_answer": "C",
        "hints": [
            "The newton meter reading is R = W - U, where W is the true weight and U = ρ g V_sub is the upthrust.",
            "While fully submerged, U is constant so R is constant. As the cylinder emerges over distance L, U decreases linearly so R increases linearly to W."
        ],
        "walkthrough": [
            "The tension reading on the newton meter is R = W - U, where W is the weight of the metal cylinder and U = ρ_water g V_submerged is the upthrust.",
            "While the cylinder remains completely submerged below the water surface, the submerged volume is constant, so U is constant and the reading R is horizontal (constant).",
            "As the cylinder emerges through the surface over a distance equal to its height L, the submerged volume decreases uniformly with distance, causing U to decrease linearly and R to increase with a constant positive gradient.",
            "Once fully out of the water, U = 0 and the reading R remains constant at the true weight W. This sequence matches graph C."
        ]
    },
    {
        "question_id": "9702_w21_12_q16",
        "difficulty": 1,
        "question_patterns": ["property_identification", "comparison"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m02",
        "skill_id": "9702_skill_kinetic_potential_energy",
        "accepted_answer": "B",
        "hints": [
            "Consider how gravitational potential energy changes with height (E_p = mgh).",
            "At the midpoint of the vertical ascent (h = 0.5 h_max), gravitational potential energy is only half of its maximum value, so it cannot equal the full initial kinetic energy."
        ],
        "walkthrough": [
            "As the ball rises, kinetic energy is converted into gravitational potential energy according to E_p = mgh. At the top of the path (h = h_max), vertical speed is zero, so kinetic energy is zero (confirming statement C).",
            "At the midpoint of its path (h = 0.5 h_max), the gravitational potential energy is E_p = mg(0.5 h_max) = 0.5 E_p,max <= 0.5 E_k,initial. Thus, E_p at the midpoint is only half of the initial kinetic energy, not equal to it.",
            "Therefore, statement B is incorrect and is the correct answer. Statements A, C, and D are valid physical descriptions."
        ]
    },
    {
        "question_id": "9702_w21_12_q17",
        "difficulty": 1,
        "question_patterns": ["direct_calculation"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_work_done",
        "accepted_answer": "C",
        "hints": [
            "Use the definition of work done by a constant force: W = F s cos θ.",
            "The angle between the horizontal force of 2.1 N and the 4.0 m displacement vector is 30°."
        ],
        "walkthrough": [
            "Work done by a constant force is defined as W = F s cos θ, where F is the force magnitude, s is the displacement magnitude, and θ is the angle between the force and displacement vectors.",
            "Substituting F = 2.1 N, s = 4.0 m, and θ = 30°: W = 2.1 N × 4.0 m × cos(30°).",
            "Calculating the result: W = 8.4 × 0.8660 J ≈ 7.27 J ≈ 7.3 J, which corresponds to option C."
        ]
    },
    {
        "question_id": "9702_w21_12_q18",
        "difficulty": 1,
        "question_patterns": ["definition", "equation_recall"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_power_efficiency",
        "accepted_answer": "A",
        "hints": [
            "Recall that overall efficiency is the ratio of useful energy output to total energy input.",
            "Identify the initial primary energy input to the power station and the final useful energy output."
        ],
        "walkthrough": [
            "The efficiency of any energy conversion system is given by efficiency = (useful energy output) / (total energy input).",
            "For a fossil fuel power station, the total initial energy input is the chemical energy W of the fuel, and the final useful output is the electrical energy Y.",
            "Therefore, the overall efficiency is Y / W, which corresponds to option A."
        ]
    },
    {
        "question_id": "9702_w21_12_q19",
        "difficulty": 1,
        "question_patterns": ["comparison", "direct_calculation"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m02",
        "skill_id": "9702_skill_kinetic_potential_energy",
        "accepted_answer": "A",
        "hints": [
            "Recall the equation for kinetic energy: E_k = 0.5 m v².",
            "Substitute m_X = 2 m_Y and v_X = 0.5 v_Y into the kinetic energy formula for car X."
        ],
        "walkthrough": [
            "Kinetic energy is given by E_k = 0.5 m v².",
            "For car Y, E_k,Y = 0.5 m_Y v_Y².",
            "For car X with mass m_X = 2 m_Y and speed v_X = 0.5 v_Y: E_k,X = 0.5 × (2 m_Y) × (0.5 v_Y)² = 0.5 × (2 m_Y) × (0.25 v_Y²) = 0.5 × (0.5 m_Y v_Y²) = 0.5 E_k,Y.",
            "Thus, car X has half the kinetic energy of car Y, confirming option A."
        ]
    },
    {
        "question_id": "9702_w21_12_q20",
        "difficulty": 2,
        "question_patterns": ["multi_step_calculation", "force_diagram_construction"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_power_efficiency",
        "accepted_answer": "B",
        "hints": [
            "Find the total opposing force that the motorbike must overcome: resistive drag plus the downhill component of weight (W sin(30°)).",
            "Use the power equation P = F v to calculate the steady speed v = P / F_total."
        ],
        "walkthrough": [
            "At constant speed up the slope, the forward driving force F equals the sum of resistive forces and the component of weight acting parallel to the incline: F = F_resistive + W sin(30°).",
            "Substituting the given parameters: F = 2400 N + 1800 N × sin(30°) = 2400 N + 900 N = 3300 N.",
            "Using the power relation P = F v: v = P / F = 36000 W / 3300 N ≈ 10.91 m s⁻¹ ≈ 11 m s⁻¹, which matches option B."
        ]
    },
    {
        "question_id": "9702_w21_12_q21",
        "difficulty": 2,
        "question_patterns": ["multi_step_calculation", "equation_derivation"],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m02",
        "skill_id": "9702_skill_hookes_law_elastic_energy",
        "accepted_answer": "A",
        "hints": [
            "Calculate the extension of the parallel pair P and Q supporting total load W: each spring supports a force of W/2.",
            "Calculate the extension of spring R with spring constant 3k supporting load W, then sum the two extensions."
        ],
        "walkthrough": [
            "Springs P and Q are connected in parallel and equally share the total applied load W, so each spring supports a force of W/2. With spring constant k, the extension of this parallel stage is x_PQ = (W/2) / k = W / (2k).",
            "Spring R is in series with the combination and supports the entire load W. With spring constant 3k, the extension of spring R is x_R = W / (3k).",
            "The total increase in overall length is x_total = x_PQ + x_R = W / (2k) + W / (3k) = (3/6 + 2/6)(W/k) = 5W / (6k), matching option A."
        ]
    },
    {
        "question_id": "9702_w21_12_q22",
        "difficulty": 1,
        "question_patterns": ["graph_interpretation", "equation_derivation"],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m01",
        "skill_id": "9702_skill_young_modulus",
        "accepted_answer": "D",
        "hints": [
            "Express stress as σ = F/A and strain as ε = x/L.",
            "Multiply stress and strain in the area formula: 0.5 × σ × ε = (0.5 F x) / (A L)."
        ],
        "walkthrough": [
            "The area under the linear region of a stress–strain graph is given by Area = 0.5 × stress × strain.",
            "Substituting stress σ = F/A and strain ε = x/L: Area = 0.5 × (F/A) × (x/L) = (0.5 F x) / (A L).",
            "Since 0.5 F x is the strain energy stored in the wire and A L is the original volume of the wire, the area represents the strain energy per unit volume, corresponding to option D."
        ]
    },
    {
        "question_id": "9702_w21_12_q23",
        "difficulty": 1,
        "question_patterns": ["classification", "property_identification"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m02",
        "skill_id": "9702_skill_progressive_wave_properties",
        "accepted_answer": "D",
        "hints": [
            "Recall that transverse waves have oscillations perpendicular to the direction of energy transfer, while longitudinal waves oscillate parallel to it.",
            "All electromagnetic waves (gamma-rays, X-rays, UV) are transverse, whereas sound waves in fluids are longitudinal."
        ],
        "walkthrough": [
            "In transverse waves, oscillations are perpendicular to the direction of wave propagation and energy transfer. In longitudinal waves, oscillations are parallel to the direction of energy transfer.",
            "Electromagnetic waves, including X-rays and gamma-rays, are transverse waves, whereas sound waves in air are longitudinal.",
            "Row D correctly pairs oscillations perpendicular to energy transfer with X-rays, making option D the correct choice."
        ]
    },
    {
        "question_id": "9702_w21_12_q24",
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "multi_step_calculation"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m01",
        "skill_id": "9702_skill_stationary_waves",
        "accepted_answer": "D",
        "hints": [
            "The distance between two consecutive intensity minima (nodes) in a stationary wave is λ / 2.",
            "Count the number of nodal intervals between point X (initial minimum) and point Y (fifth subsequent minimum): there are 5 intervals across 70.0 cm."
        ],
        "walkthrough": [
            "In a stationary sound wave formed by reflection, intensity minima occur at displacement nodes, which are spaced by a distance of λ / 2.",
            "Starting at the first minimum at X and passing through four intermediate minima to reach the 5th minimum at Y spans exactly 5 nodal intervals.",
            "Therefore, 5 × (λ / 2) = 70.0 cm, which gives λ = (2 × 70.0 cm) / 5 = 28.0 cm (option D)."
        ]
    },
    {
        "question_id": "9702_w21_12_q25",
        "difficulty": 2,
        "question_patterns": ["multi_step_calculation", "direct_calculation"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m03",
        "skill_id": "9702_skill_doppler_effect",
        "accepted_answer": "C",
        "hints": [
            "Use the Doppler formula for a moving source: f_o = f_s × [v / (v ± v_s)], with minus for approaching and plus for receding.",
            "Calculate observed frequencies for both approach and departure, then compute their difference."
        ],
        "walkthrough": [
            "When the train approaches the stationary observer, the observed frequency is f_approach = f_s × [v / (v - v_s)] = 2400 × [340 / (340 - 30)] = 2400 × (340 / 310) ≈ 2632.26 Hz.",
            "When the train moves away from the observer, the observed frequency is f_recede = f_s × [v / (v + v_s)] = 2400 × [340 / (340 + 30)] = 2400 × (340 / 370) ≈ 2205.41 Hz.",
            "The maximum frequency difference is Δf = f_approach - f_recede = 2632.26 Hz - 2205.41 Hz ≈ 426.85 Hz ≈ 430 Hz, which matches option C."
        ]
    },
    {
        "question_id": "9702_w21_12_q26",
        "difficulty": 1,
        "question_patterns": ["classification", "property_identification"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m04",
        "skill_id": "9702_skill_electromagnetic_spectrum",
        "accepted_answer": "A",
        "hints": [
            "Convert frequency to wavelength in vacuum using λ = c / f, where c = 3.0 × 10⁸ m s⁻¹ and 1 THz = 10¹² Hz.",
            "Compare the resulting wavelength to the known spectral regions (infrared spans roughly 700 nm to 1 mm)."
        ],
        "walkthrough": [
            "The frequency is f = 30 THz = 30 × 10¹² Hz = 3.0 × 10¹³ Hz.",
            "The wavelength in vacuum is λ = c / f = (3.0 × 10⁸ m s⁻¹) / (3.0 × 10¹³ Hz) = 1.0 × 10⁻⁵ m = 10 µm.",
            "Wavelengths in the range 7 × 10⁻⁷ m to 1 × 10⁻³ m lie in the infrared region of the electromagnetic spectrum, confirming option A."
        ]
    },
    {
        "question_id": "9702_w21_12_q27",
        "difficulty": 2,
        "question_patterns": ["graph_interpretation", "direct_calculation"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m01",
        "skill_id": "9702_skill_stationary_waves",
        "accepted_answer": "C",
        "hints": [
            "Count the number of loops (half-wavelengths) across the string length of 1.35 m.",
            "Find λ from 3 × (λ / 2) = 1.35 m, then use v = f λ with v = 450 m s⁻¹."
        ],
        "walkthrough": [
            "The stationary wave diagram shows 3 complete loops (harmonics n = 3) between the two fixed ends.",
            "The relationship between length and wavelength is L = 3(λ / 2) = 1.35 m, which gives λ = (2 × 1.35 m) / 3 = 0.90 m.",
            "Applying the wave equation v = f λ: f = v / λ = 450 m s⁻¹ / 0.90 m = 500 Hz, which matches option C."
        ]
    },
    {
        "question_id": "9702_w21_12_q28",
        "difficulty": 1,
        "question_patterns": ["property_identification", "motion_path_representation"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m02",
        "skill_id": "9702_skill_wave_diffraction",
        "accepted_answer": "B",
        "hints": [
            "Recall that diffraction causes waves to spread out perpendicularly to the narrow edges of an aperture.",
            "For a narrow vertical slit, diffraction spreading occurs predominantly in the horizontal direction on the screen."
        ],
        "walkthrough": [
            "When monochromatic laser light passes through a narrow aperture, diffraction causes the light beam to spread out in the direction where the aperture dimension is comparable to the wavelength.",
            "Because the slit is narrow horizontally and tall vertically, significant diffraction spreading occurs horizontally across the screen.",
            "This produces a horizontal line of diffraction maxima and minima on the screen, matching diagram B."
        ]
    },
    {
        "question_id": "9702_w21_12_q29",
        "difficulty": 2,
        "question_patterns": ["definition", "property_identification"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m03",
        "skill_id": "9702_skill_two_source_interference",
        "accepted_answer": "A",
        "hints": [
            "For the positions of interference minima to remain stationary over time, the two waves must maintain a constant phase difference (coherence).",
            "For total destructive interference to result in zero resultant displacement at all times at the minima, the amplitudes of the two interfering waves must be equal."
        ],
        "walkthrough": [
            "To produce a stable, stationary interference pattern, the two interfering waves must be coherent (maintaining a constant phase difference over time).",
            "For the displacement to remain identically zero at the minima at all times, complete destructive cancellation must occur where the waves arrive in antiphase (A_min = |A₁ - A₂| = 0).",
            "This complete cancellation requires that the two waves have identical amplitudes (A₁ = A₂). Thus, the waves must be coherent and of the same amplitude, confirming option A."
        ]
    },
    {
        "question_id": "9702_w21_12_q30",
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "multi_step_calculation"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m04",
        "skill_id": "9702_skill_diffraction_grating",
        "accepted_answer": "A",
        "hints": [
            "The total angle between the two second-order maxima (n = 2) on opposite sides of the normal is 80°, so the diffraction angle is θ = 40°.",
            "Use the diffraction grating equation d sin θ = n λ with n = 2 to find slit spacing d, then calculate N = 1/d."
        ],
        "walkthrough": [
            "The angle between the two second-order maxima is 2θ = 80°, giving a diffraction angle from the central maximum of θ = 40°.",
            "Using the diffraction grating equation d sin θ = n λ for order n = 2: d = (2 × 5.5 × 10⁻⁷ m) / sin(40°) = (1.10 × 10⁻⁶ m) / 0.6428 ≈ 1.711 × 10⁻⁶ m.",
            "The number of lines per metre is N = 1 / d = 1 / (1.711 × 10⁻⁶ m) ≈ 5.84 × 10⁵ m⁻¹ ≈ 5.8 × 10⁵ lines per metre, which corresponds to option A."
        ]
    },
    {
        "question_id": "9702_w21_12_q31",
        "difficulty": 1,
        "question_patterns": ["electric_field_line_construction", "property_identification"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_uniform_electric_fields",
        "accepted_answer": "A",
        "hints": [
            "Recall that electric field lines represent the direction of the force exerted on a positive test charge.",
            "Electric field lines always originate on positive charges (+) and terminate on negative charges (-) without crossing."
        ],
        "walkthrough": [
            "Electric field lines indicate the direction of the electrostatic force that a positive test charge would experience at any point.",
            "Field lines always start on positive charges (+) and end on negative charges (-).",
            "In diagram A, all field lines correctly emanate outwards from the positive charge and converge inwards onto the negative charge, making option A correct."
        ]
    },
    {
        "question_id": "9702_w21_12_q32",
        "difficulty": 1,
        "question_patterns": ["property_identification", "motion_path_representation"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_uniform_electric_fields",
        "accepted_answer": "C",
        "hints": [
            "Determine the direction of the electric field: electric fields point from regions of high potential (+10 V) to low potential (0 V).",
            "A positive proton experiences an electrostatic force in the direction of the electric field (to the left), opposing its rightward entry velocity."
        ],
        "walkthrough": [
            "The electric field between parallel plates points from the region of higher potential (+10 V, right plate) to lower potential (0 V, left plate), which is directed horizontally to the left.",
            "A positively charged proton entering horizontally to the right experiences an electrostatic force F = qE directed to the left, directly opposing its initial velocity.",
            "This opposing force causes a deceleration in its direction of motion, so its speed immediately decreases (option C)."
        ]
    },
    {
        "question_id": "9702_w21_12_q33",
        "difficulty": 1,
        "question_patterns": ["definition", "property_identification"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m01",
        "skill_id": "9702_skill_electric_current_drift_speed",
        "accepted_answer": "B",
        "hints": [
            "Recall the relationship between charge, current, and time: Q = I t.",
            "State the SI definition of one coulomb (1 C = 1 A s)."
        ],
        "walkthrough": [
            "Electric charge Q is related to current I and time t by Q = I t.",
            "One coulomb (1 C) is defined as the amount of electric charge transported by a steady current of one ampere flowing for one second (1 C = 1 A s).",
            "This directly matches the statement in option B. Option C defines the electronvolt."
        ]
    },
    {
        "question_id": "9702_w21_12_q34",
        "difficulty": 2,
        "question_patterns": ["circuit_analysis", "comparison"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_emf_internal_resistance",
        "accepted_answer": "B",
        "hints": [
            "Use the potential divider formula for terminal potential difference: V = E × [R / (R + r)].",
            "Evaluate how increasing the load resistance R from 5.0 Ω to 50 Ω alters the terminal p.d."
        ],
        "walkthrough": [
            "The potential difference across the load resistor is given by V = E × [R / (R + r)].",
            "Initially, with R = 5.0 Ω and r = 5.0 Ω: V = 10 × [5.0 / (5.0 + 5.0)] = 5.0 V.",
            "When the load is replaced by R = 50 Ω: V = 10 × [50 / (50 + 5.0)] ≈ 9.09 V.",
            "The potential difference across the load resistor increases from 5.0 V to 9.1 V, confirming option B. Circuit current and power dissipation both decrease."
        ]
    },
    {
        "question_id": "9702_w21_12_q35",
        "difficulty": 1,
        "question_patterns": ["graph_interpretation", "classification"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m03",
        "skill_id": "9702_skill_iv_characteristics",
        "accepted_answer": "B",
        "hints": [
            "Identify the linear I–V characteristic of an ohmic conductor at constant temperature.",
            "Distinguish between the non-linear curves for a forward-biased diode (sharp turn-on) and a filament lamp (decreasing gradient due to temperature rise)."
        ],
        "walkthrough": [
            "Graph Y is a straight line through the origin (I ∝ V), indicating constant resistance obeying Ohm's law, which represents a metal wire at constant temperature.",
            "Graph X exhibits near-zero conduction until a threshold forward voltage is reached, followed by a rapid rise in current, characteristic of a semiconductor diode.",
            "Graph Z displays a decreasing gradient (I/V) as V increases, indicating increasing resistance caused by filament heating, characteristic of a filament lamp.",
            "Matching the components to the table columns gives row B (metal wire: Y, semiconductor diode: X, filament lamp: Z)."
        ]
    },
    {
        "question_id": "9702_w21_12_q36",
        "difficulty": 1,
        "question_patterns": ["definition", "comparison"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_potential_difference_power",
        "accepted_answer": "C",
        "hints": [
            "Recall that both e.m.f. and p.d. are defined in terms of energy transfer per unit charge (W/Q).",
            "E.m.f. represents chemical to electrical energy conversion per unit charge in the cell, while p.d. represents electrical to other forms (thermal) per unit charge in the load resistor."
        ],
        "walkthrough": [
            "Electromotive force (e.m.f.) is defined as the energy transferred from chemical (or non-electrical) energy to electrical energy per unit charge that passes through the cell (E = W/Q).",
            "Potential difference (p.d.) is defined as the energy transferred from electrical energy to thermal (or other non-electrical) forms per unit charge across the component (V = W/Q).",
            "Option C correctly includes both the energy direction distinction and the essential requirement of 'per unit charge'."
        ]
    },
    {
        "question_id": "9702_w21_12_q37",
        "difficulty": 1,
        "question_patterns": ["circuit_analysis", "direct_calculation"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m02",
        "skill_id": "9702_skill_kirchhoffs_laws",
        "accepted_answer": "A",
        "hints": [
            "Apply Kirchhoff's first law (current conservation) at the junction entering the parallel pair: I_total = I₁ + I₂.",
            "Apply Kirchhoff's second law around the closed loop: the total e.m.f. equals the sum of the p.d. across the parallel combination and the series resistor."
        ],
        "walkthrough": [
            "By Kirchhoff's first law, total current entering the parallel branch junction equals total current leaving it. With I_total = 0.4 A and one branch carrying 0.3 A, the other branch carries I₂ = 0.4 A - 0.3 A = 0.1 A.",
            "By Kirchhoff's second law, the total e.m.f. around the loop equals the sum of potential differences across the series elements: e.m.f. = V_parallel + V_series = 2 V + 2 V = 4 V.",
            "This corresponds to row A (0.1 A, 4 V)."
        ]
    },
    {
        "question_id": "9702_w21_12_q38",
        "difficulty": 2,
        "question_patterns": ["circuit_analysis", "direct_calculation"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m03",
        "skill_id": "9702_skill_potential_dividers",
        "accepted_answer": "A",
        "hints": [
            "Find the total circuit resistance: R_total = r + R_fixed + R_potentiometer = 1.0 + 5.0 + 3.0 = 9.0 Ω.",
            "Calculate the circuit current I = E / R_total, then find the maximum potential difference across the 3.0 Ω potentiometer: V_max = I × 3.0 Ω."
        ],
        "walkthrough": [
            "The total resistance of the series circuit is R_total = r + R_fixed + R_pot = 1.0 Ω + 5.0 Ω + 3.0 Ω = 9.0 Ω.",
            "The current in the circuit is I = E / R_total = 9.0 V / 9.0 Ω = 1.0 A.",
            "The voltmeter measures the potential difference across the tapped portion of the potentiometer (ranging from 0 Ω to 3.0 Ω). The maximum measured voltage occurs when the full resistance is included: V_max = 1.0 A × 3.0 Ω = 3.0 V (option A)."
        ]
    },
    {
        "question_id": "9702_w21_12_q39",
        "difficulty": 1,
        "question_patterns": ["property_identification", "classification"],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m01",
        "skill_id": "9702_skill_nuclear_decay_equations",
        "accepted_answer": "C",
        "hints": [
            "Recall the universal conservation laws in nuclear physics (conservation of mass–energy, charge, and nucleon number).",
            "In β⁺ decay, a proton converts into a neutron, releasing a positron and an electron neutrino (not an antineutrino)."
        ],
        "walkthrough": [
            "In every radioactive decay process, the total mass–energy of the system is strictly conserved, making statement C correct.",
            "In β⁺ (positron) decay, a proton decays into a neutron, emitting a positron (β⁺) and an electron neutrino (ν_e): p → n + e⁺ + ν_e.",
            "Statements A and B are incorrect because a neutrino (not an antineutrino) is emitted and a proton converts into a neutron. Statement D is false because nucleon number is always conserved in radioactive decays."
        ]
    },
    {
        "question_id": "9702_w21_12_q40",
        "difficulty": 1,
        "question_patterns": ["classification", "property_identification"],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m02",
        "skill_id": "9702_skill_quark_model_hadrons",
        "accepted_answer": "B",
        "hints": [
            "Recall that leptons (such as electrons, muons, and neutrinos) are fundamental particles without quark substructure.",
            "Particles composed of a quark and an antiquark are mesons (hadrons), not leptons."
        ],
        "walkthrough": [
            "Electrons and neutrinos belong to the lepton family and are fundamental particles with no internal quark substructure.",
            "A composite particle composed of a quark and an antiquark is a meson (a type of hadron), such as a pion or kaon.",
            "Therefore, statement B is incorrect and provides the required answer. Statements A, C, and D are all scientifically correct."
        ]
    }
]

def main():
    print(f"Generating {len(data)} enrichment files for 9702_w21_12...")
    for item in data:
        qid = item["question_id"]
        out_file = ENRICH_DIR / f"{qid}.enrichment.json"
        record = {
            "schema_version": "9702_p1_enrichment_v1",
            "question_id": qid,
            "component": "P1",
            "difficulty": item["difficulty"],
            "question_patterns": item["question_patterns"],
            "topic_id": item["topic_id"],
            "module_id": item["module_id"],
            "skill_id": item["skill_id"],
            "accepted_answer": item["accepted_answer"],
            "hints": item["hints"],
            "walkthrough": item["walkthrough"]
        }
        out_file.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {out_file.name}")
    print("Done!")

if __name__ == '__main__':
    main()
