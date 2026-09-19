#!/usr/bin/env python3
"""
generate_9702_w19_12.py

Generates all 40 enrichment JSON records for Cambridge AS Physics 9702 Paper 1 (9702_w19_12).
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENRICH_DIR = ROOT / 'subjects/physics/9702/enrichment/p1'
ENRICH_DIR.mkdir(parents=True, exist_ok=True)

ENRICHMENTS = [
    # Q01
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q01",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "physical_quantity_estimation",
            "comparison"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m01",
        "skill_id": "9702_skill_physical_estimations",
        "accepted_answer": "D",
        "hints": [
            "Estimate reasonable typical masses: a cyclist plus bicycle has a mass of around 80 kg, while a small car has a mass of around 1000 kg to 1500 kg.",
            "Calculate the kinetic energy (0.5 × m × v²) and momentum (m × v) for each body using the given speeds (5 m s⁻¹ and 12 m s⁻¹) and identify which given estimate is orders of magnitude off."
        ],
        "walkthrough": [
            "For the cyclist (mass m ≈ 80 kg, speed v = 5 m s⁻¹), kinetic energy is E_k ≈ 0.5 × 80 × 5² = 1000 J = 1 × 10³ J and momentum is p ≈ 80 × 5 = 400 kg m s⁻¹ = 4 × 10² kg m s⁻¹. Both estimates in A and C are reasonable.",
            "For a small car (mass m ≈ 1000 kg, speed v = 12 m s⁻¹), kinetic energy is E_k ≈ 0.5 × 1000 × 12² = 7.2 × 10⁴ J ≈ 7 × 10⁴ J, which matches statement B.",
            "The momentum of the small car is p ≈ 1000 × 12 = 1.2 × 10⁴ kg m s⁻¹. The value of 2 × 10⁵ kg m s⁻¹ given in D would require a mass of nearly 17 000 kg (17 tonnes), which is unreasonable for a small car. Therefore, statement D does not give a reasonable estimate."
        ]
    },

    # Q02
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q02",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "definition",
            "classification"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m02",
        "skill_id": "9702_skill_si_units_homogeneity",
        "accepted_answer": "A",
        "hints": [
            "Recall the seven SI base quantities: mass, length, time, electric current, thermodynamic temperature, amount of substance, and luminous intensity.",
            "Express each given phrase as a formula and identify which one defines electric current."
        ],
        "walkthrough": [
            "Electric current (I) is defined as the rate of flow of electric charge, I = Q / t (charge per unit time). Electric current is one of the seven fundamental SI base quantities, making A the correct expression.",
            "Option B (force per unit area) defines pressure, which is a derived quantity (1 Pa = 1 N m⁻²).",
            "Option C (mass per unit volume) defines density, which is a derived quantity (kg m⁻³). Option D (work done per unit distance) equals force (W / d = F), which is also a derived quantity (N). Only charge per unit time corresponds to an SI base quantity."
        ]
    },

    # Q03
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q03",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "classification",
            "property_identification"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m04",
        "skill_id": "9702_skill_scalars_vectors",
        "accepted_answer": "B",
        "hints": [
            "Distinguish between scalar quantities (which possess magnitude only) and vector quantities (which have both magnitude and direction).",
            "Examine each list to check whether any vector quantities such as displacement, velocity, or momentum are present."
        ],
        "walkthrough": [
            "A scalar quantity has magnitude only, with no direction. Kinetic energy (measured in joules), speed (rate of change of distance), and power (rate of energy transfer) all have magnitude only and are scalars. Thus, the list in B contains only scalar quantities.",
            "In option A, displacement is a vector. In option C, momentum is a vector (p = m × v). In option D, velocity is a vector. Therefore, options A, C, and D all contain vector quantities."
        ]
    },

    # Q04
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q04",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "uncertainty_analysis",
            "measurement_selection"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m03",
        "skill_id": "9702_skill_errors_uncertainties",
        "accepted_answer": "C",
        "hints": [
            "Convert both the measured value (28.50 mm) and the absolute uncertainty (±0.01 mm) into standard units of meters (m).",
            "Express the measurement in scientific notation with the uncertainty factored alongside the value to the same power of ten and decimal place precision."
        ],
        "walkthrough": [
            "The measured value is 28.50 mm = 0.02850 m = 2.850 × 10⁻² m.",
            "The micrometer precision gives an absolute uncertainty of ±0.01 mm = ±0.00001 m = ±0.001 × 10⁻² m.",
            "Combining value and uncertainty with the common factor 10⁻² m yields (2.850 ± 0.001) × 10⁻² m, which matches C.",
            "Option A incorrectly quotes an uncertainty of ±0.01 m (10 mm). Option B incorrectly states ±0.001 m (1 mm). Option D uses an incorrect exponent of 10⁻³ m, which corresponds to 2.85 mm."
        ]
    },

    # Q05
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q05",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "uncertainty_analysis",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m03",
        "skill_id": "9702_skill_errors_uncertainties",
        "accepted_answer": "B",
        "hints": [
            "For a product of dimensions V = a × b × c, the percentage uncertainty in volume is the sum of the individual percentage uncertainties of the three sides.",
            "Calculate (Δa / a) × 100% for each of the three sides (20.0 mm, 40.0 mm, and 10.0 mm) with absolute uncertainty ±0.1 mm, then sum them."
        ],
        "walkthrough": [
            "The volume of the rectangular block is V = l₁ × l₂ × l₃. For multiplied quantities, fractional uncertainties add: ΔV / V = (Δl₁ / l₁) + (Δl₂ / l₂) + (Δl₃ / l₃).",
            "Calculating the percentage uncertainty for each side:",
            "(0.1 / 20.0) × 100% = 0.50%",
            "(0.1 / 40.0) × 100% = 0.25%",
            "(0.1 / 10.0) × 100% = 1.00%",
            "Total percentage uncertainty in volume = 0.50% + 0.25% + 1.00% = 1.75% ≈ 1.8%, corresponding to option B.",
            "Option A (0.3%) inappropriately adds absolute uncertainties. Option C (3.8%) results from arithmetic error or misapplying powers. Option D (30%) represents an order-of-magnitude error."
        ]
    },

    # Q06
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q06",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "multi_step_calculation",
            "direct_calculation"
        ],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_kinematics_equations",
        "accepted_answer": "B",
        "hints": [
            "Use the kinematic equation v² = u² - 2gs to find the initial upward velocity, or use s = 0.5 × g × t² to find the time taken to fall from the maximum height.",
            "Remember that the total flight time for a ball thrown upwards and returning to the same level is twice the time taken to reach the maximum height."
        ],
        "walkthrough": [
            "At the maximum height h = 12.7 m, the vertical velocity is momentarily zero (v = 0).",
            "The time to fall freely from rest from height h back to the ground is given by h = 0.5 × g × t² ==> t_down = √(2h / g) = √(2 × 12.7 / 9.81) = √(2.5892) ≈ 1.609 s.",
            "Because air resistance is negligible, the upward journey is symmetric to the downward journey (t_up = t_down).",
            "Total time in the air t_total = 2 × 1.609 s = 3.218 s ≈ 3.22 s, which is option B.",
            "Option A (1.61 s) is only the one-way time (upward or downward). Options C and D arise from incorrect formulas or arithmetic mistakes."
        ]
    },

    # Q07
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q07",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "multi_step_calculation",
            "direct_calculation"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_newtons_laws",
        "accepted_answer": "D",
        "hints": [
            "Momentum is a vector quantity. Take care with the signs: the ball rebounds in the opposite direction, so change in velocity is v - u where one velocity is negative.",
            "Use Newton's second law: average force = (change in momentum) / (contact time)."
        ],
        "walkthrough": [
            "The ball has mass m = 200 g = 0.200 kg.",
            "Taking the initial direction as positive: initial velocity u = +14.0 m s⁻¹, and rebound velocity v = -7.0 m s⁻¹.",
            "The change in velocity is Δv = v - u = -7.0 - 14.0 = -21.0 m s⁻¹.",
            "The magnitude of the change in momentum (impulse) is Δp = m|Δv| = 0.200 × 21.0 = 4.2 N s.",
            "The average force exerted on the ball is F = Δp / Δt = 4.2 N s / 0.60 s = 7.0 N, which corresponds to option D.",
            "Option C (4.2 N) is the impulse Δp without dividing by Δt. Option B (2.3 N) incorrectly subtracts speeds without accounting for vector direction (14.0 - 7.0 = 7.0, F = 0.200 × 7.0 / 0.60 = 2.33 N)."
        ]
    },

    # Q08
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q08",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "motion_path_representation"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m02",
        "skill_id": "9702_skill_drag_terminal_velocity",
        "accepted_answer": "D",
        "hints": [
            "The gradient of a displacement-time graph represents the velocity (v = ds/dt).",
            "Consider what happens to the velocity of the falling ball as air resistance increases from zero until terminal velocity is reached."
        ],
        "walkthrough": [
            "At t = 0, the ball is released from rest, so its initial velocity is zero. This corresponds to an initial gradient of zero (tangent is horizontal at the origin).",
            "As the ball accelerates downwards under gravity, its velocity increases, so the gradient ds/dt increases (the curve steepens upwards).",
            "As air resistance increases and eventually balances weight (net force = 0), the ball reaches a constant terminal velocity. On a displacement-time graph, constant velocity is represented by a straight line with a constant positive gradient.",
            "Graph D begins with zero slope at the origin, curves upwards as speed increases, and asymptotically transitions into a straight line of constant slope at large t, correctly representing the motion.",
            "Graph A shows decreasing gradient (deceleration to rest). Graph B represents constant velocity from t = 0 with no acceleration. Graph C shows continually increasing acceleration with no terminal velocity."
        ]
    },

    # Q09
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q09",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m03",
        "skill_id": "9702_skill_linear_momentum_collisions",
        "accepted_answer": "A",
        "hints": [
            "For an isolated system with no external forces, total linear momentum is conserved during the separation.",
            "Set the momentum gained by the lander equal in magnitude to the momentum gained by the orbiter in the opposite direction."
        ],
        "walkthrough": [
            "In the reference frame of the probe before separation, the initial momentum is zero.",
            "By conservation of linear momentum: m_orbiter × Δv_orbiter + m_lander × Δv_lander = 0.",
            "Substituting the given masses and velocity change of the lander: 170 × Δv_orbiter = 100 × 3.0 = 300 kg m s⁻¹.",
            "Solving for the orbiter's speed change: Δv_orbiter = 300 / 170 ≈ 1.76 m s⁻¹ ≈ 1.8 m s⁻¹, corresponding to option A.",
            "Option B (2.3 m s⁻¹) is from 3.0 × (170 - 100) / 100 or similar incorrect ratios. Option C (3.0 m s⁻¹) assumes equal speed change despite different masses. Option D (5.1 m s⁻¹) inverts the mass ratio (3.0 × 170 / 100)."
        ]
    },

    # Q10
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q10",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": [
            "graph_interpretation",
            "equation_derivation"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m02",
        "skill_id": "9702_skill_drag_terminal_velocity",
        "accepted_answer": "A",
        "hints": [
            "Set up the equilibrium equation for the forces acting on the falling droplet: downward weight equals upward electric force plus upward viscous drag.",
            "Express the terminal speed v0 as a function of the electric field strength E and examine the form of the resulting equation (linear with negative gradient)."
        ],
        "walkthrough": [
            "The droplet is positively charged (+q) and falling vertically downwards at terminal speed v₀ in an upward uniform electric field E.",
            "The forces acting on the droplet are: downward gravitational force (weight W = mg), upward electric force (F_E = qE), and upward air resistance force (F_D = k v₀, where k is a constant).",
            "At constant terminal speed, net vertical force is zero: mg = qE + k v₀.",
            "Rearranging for v₀ in terms of E: v₀ = (mg / k) - (q / k)E.",
            "This gives a straight-line relationship with a positive intercept (mg / k) at E = 0 and a constant negative gradient -(q / k), which reaches v₀ = 0 when E = mg / q. Graph A correctly displays this linear decrease.",
            "Graphs B, C, and D display non-linear variations or increasing terminal speed with E, which contradict the linear force balance equation."
        ]
    },

    # Q11
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q11",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": [
            "multi_step_calculation",
            "direct_calculation"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_moments_couples",
        "accepted_answer": "A",
        "hints": [
            "Carefully determine the perpendicular distance from the midpoint pivot to each suspended weight using the bar's total length (2.4 m).",
            "Calculate the clockwise and anticlockwise moments about the pivot; the balancing couple must equal the net moment in magnitude and oppose its direction."
        ],
        "walkthrough": [
            "The bar has length 2.4 m pivoted at its midpoint, so the distance from the pivot to each outer end is 1.2 m.",
            "The 200 N weight is hung 0.8 m to the left of the pivot, producing an anticlockwise moment = 200 N × 0.8 m = 160 N m.",
            "The diagram shows the 300 N weight positioned 0.8 m from the right-hand end of the bar. Its distance from the midpoint pivot is therefore 1.2 m - 0.8 m = 0.4 m, producing a clockwise moment = 300 N × 0.4 m = 120 N m.",
            "The net moment about the pivot is 160 N m - 120 N m = 40 N m anticlockwise.",
            "To maintain rotational equilibrium, the applied couple must provide an equal and opposite torque of 40 N m clockwise, which matches option A.",
            "Option B gives the correct magnitude but wrong direction (anticlockwise). Options C and D (80 N m) incorrectly assume the 300 N weight is 0.8 m from the pivot (300 × 0.8 - 200 × 0.8 = 80 N m)."
        ]
    },

    # Q12
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q12",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "vector_diagram_construction",
            "property_identification"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m02",
        "skill_id": "9702_skill_equilibrium_coplanar_forces",
        "accepted_answer": "D",
        "hints": [
            "To find the resultant of two vectors, use the head-to-tail triangle rule: place the tail of the second vector at the arrow-head of the first vector.",
            "The resultant vector F starts from the tail of the initial vector and points to the head of the second vector."
        ],
        "walkthrough": [
            "The two forces acting on the object are: (1) a horizontal force directed to the right, and (2) an inclined force directed upwards and to the right.",
            "By vector addition (triangle law), we place the horizontal vector starting at the origin, and then attach the tail of the inclined vector to the tip of the horizontal vector.",
            "The resultant force F is the vector drawn from the start of the horizontal vector directly to the tip of the inclined vector, pointing upwards and to the right.",
            "Diagram D correctly depicts this head-to-tail addition with the resultant vector F extending from the origin to the final tip.",
            "Diagram A shows incorrect head-to-head orientation. Diagram B draws the resultant backwards toward the start. Diagram C reverses the direction of the horizontal component."
        ]
    },

    # Q13
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q13",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "comparison",
            "direct_calculation"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m03",
        "skill_id": "9702_skill_density_pressure",
        "accepted_answer": "B",
        "hints": [
            "Hydrostatic pressure in a uniform liquid is given by p = rho × g × h, where h is the depth below the top liquid surface.",
            "Compare the depth h below the liquid surface for each of the four labeled points A, B, C, and D."
        ],
        "walkthrough": [
            "Hydrostatic gauge pressure is directly proportional to the vertical depth h below the free surface of the liquid: p = ρgh.",
            "For point A: located at the top surface of a 30 cm liquid column ==> h_A = 0 cm, so gauge pressure is 0.",
            "For point B: located 10 cm above the base in a 30 cm column ==> depth below surface h_B = 30 cm - 10 cm = 20 cm.",
            "For point C: located at the top surface of a 10 cm column ==> h_C = 0 cm, so gauge pressure is 0.",
            "For point D: located at the bottom of a 10 cm column ==> depth h_D = 10 cm.",
            "Comparing depths: h_B = 20 cm > h_D = 10 cm > h_A = h_C = 0 cm. Since point B has the greatest depth below the surface, the hydrostatic pressure is greatest at B, making B the correct choice."
        ]
    },

    # Q14
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q14",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_work_done",
        "accepted_answer": "A",
        "hints": [
            "Use the work done formula W = p × ΔV = p × A × Δx, ensuring all quantities are converted to SI base units (m² and m).",
            "Convert the cross-sectional area from cm² to m² (multiply by 10⁻⁴) and the distance from cm to m (multiply by 10⁻²)."
        ],
        "walkthrough": [
            "The work done by the expanding gas is given by W = p × ΔV = p × A × Δx.",
            "Convert area and displacement to SI base units:",
            "A = 80 cm² = 80 × 10⁻⁴ m² = 8.0 × 10⁻³ m²",
            "Δx = 25 cm = 0.25 m",
            "The volume change is ΔV = A × Δx = (8.0 × 10⁻³ m²)(0.25 m) = 2.0 × 10⁻³ m³.",
            "Calculate work done: W = (4.6 × 10⁵ Pa)(2.0 × 10⁻³ m³) = 9.2 × 10² J, which corresponds to option A.",
            "Options B, C, and D result from incorrect unit conversion factors for cm² to m² (e.g. using 10⁻² instead of 10⁻⁴)."
        ]
    },

    # Q15
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q15",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": [
            "multi_step_calculation",
            "direct_calculation"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_power_efficiency",
        "accepted_answer": "C",
        "hints": [
            "Calculate the total electrical energy output per day: E_out = P × t = (3000 MW) × (24 × 3600 s).",
            "Determine total thermal energy input using efficiency (E_in = E_out / 0.26), find total mass of coal needed using 33 MJ kg⁻¹, and divide by 20 trains."
        ],
        "walkthrough": [
            "Electrical energy produced in one day (t = 24 × 3600 s = 86 400 s) is E_out = P_out × t = (3000 × 10⁶ W) × (86 400 s) = 2.592 × 10¹⁴ J.",
            "With an efficiency η = 0.26, the total thermal input energy required per day is E_in = E_out / 0.26 = (2.592 × 10¹⁴ J) / 0.26 ≈ 9.969 × 10¹⁴ J.",
            "Each kilogram of coal releases 33 MJ = 3.3 × 10⁷ J. Total coal required per day is M_total = (9.969 × 10¹⁴ J) / (3.3 × 10⁷ J kg⁻¹) ≈ 3.021 × 10⁷ kg.",
            "Since 20 trains deliver this daily coal supply, the mass of coal brought by each train is M_train = (3.021 × 10⁷ kg) / 20 ≈ 1.51 × 10⁶ kg ≈ 1.5 × 10⁶ kg, matching option C.",
            "Option A (2.5 × 10⁴ kg) ignores seconds in a day (using hours). Option B (6.3 × 10⁴ kg) omits time conversion. Option D (3.0 × 10⁷ kg) is the total daily coal mass for all 20 trains combined."
        ]
    },

    # Q16
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q16",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "explanation",
            "property_identification"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m03",
        "skill_id": "9702_skill_upthrust_archimedes",
        "accepted_answer": "D",
        "hints": [
            "Analyze the directions of forces and displacements: the external force F acts downwards and pushes the cylinder downwards, while upthrust acts upwards.",
            "Recall the definition of work done by a force: when displacement is opposite to the force direction, work is done against the force, not by it."
        ],
        "walkthrough": [
            "As the cylinder is pushed downwards, its centre of gravity moves downward, so the cylinder loses gravitational potential energy (statement B is correct).",
            "The submerged volume increases, displacing water upwards and causing the water level to rise, so some water gains gravitational potential energy (statement A is correct).",
            "The external force F acts downwards in the direction of the downward displacement, so work is done by force F on the cylinder (statement C is correct).",
            "Upthrust acts vertically upwards, but the displacement of the cylinder is downwards. Therefore, work is done against the upthrust (or negative work is done by upthrust). Thus, statement D ('Work is done by the upthrust on the cylinder') is NOT correct, making D the accepted answer."
        ]
    },

    # Q17
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q17",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_power_efficiency",
        "accepted_answer": "B",
        "hints": [
            "Convert the lifting speed from meters per minute to meters per second by dividing by 60.",
            "Use the power formula P = F × v where F = mg is the upward lifting force acting against gravity at constant speed."
        ],
        "walkthrough": [
            "The speed of the load in SI units is v = 12 m / 60 s = 0.20 m s⁻¹.",
            "At constant vertical speed, the lifting force equals the weight of the load: F = mg = 600 kg × 9.81 m s⁻² = 5886 N.",
            "The useful power output is P = F × v = 5886 N × 0.20 m s⁻¹ = 1177.2 W ≈ 1.2 kW, which matches option B.",
            "Option A (0.12 kW) misses a factor of 10. Option C (7.2 kW) fails to convert minutes to seconds (600 × 9.81 × 12 / 1000). Option D (71 kW) multiplies incorrectly."
        ]
    },

    # Q18
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q18",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "direct_calculation"
        ],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m01",
        "skill_id": "9702_skill_hookes_law_elastic_energy",
        "accepted_answer": "A",
        "hints": [
            "Read the unstretched original length of the spring from the vertical intercept at F = 0.",
            "Determine the extension produced by 5.0 N, find the extension per unit force (or spring constant), and calculate the extension for 7.0 N."
        ],
        "walkthrough": [
            "From the graph of spring length versus force, at F = 0 the original unstretched length is L₀ = 11.0 cm.",
            "At F = 5.0 N, the total length is 14.0 cm, which gives an extension of ΔL = 14.0 - 11.0 = 3.0 cm.",
            "The spring constant is k = F / ΔL = 5.0 N / 3.0 cm = (5/3) N cm⁻¹ (or extension per newton is 0.60 cm N⁻¹).",
            "For a force of 7.0 N, the extension is x = F / k = 7.0 N × 0.60 cm N⁻¹ = 4.2 cm, which corresponds to option A.",
            "Option B (5.6 cm) uses an incorrect reference intercept. Option C (15 cm) approximates total length (11 + 4.2 = 15.2 cm) rather than extension. Option D (20 cm) is an overestimate."
        ]
    },

    # Q19
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q19",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "property_identification"
        ],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m02",
        "skill_id": "9702_skill_elastic_plastic_behaviour",
        "accepted_answer": "B",
        "hints": [
            "Recall that the area under a force-extension curve represents work done.",
            "Consider the difference between the work done stretching the rubber cord and the elastic energy released during contraction."
        ],
        "walkthrough": [
            "The area under the loading (stretching) curve represents the total work done on the rubber cord to stretch it.",
            "The area under the unloading (contraction) curve represents the work done by the rubber cord as it contracts (the elastic energy recovered).",
            "The area enclosed between the stretching and contraction curves (the hysteresis loop) is the net energy that is not recovered mechanically and is converted to internal thermal energy in the rubber cord.",
            "Therefore, the shaded area represents the thermal energy dissipated in the rubber cord, matching option B.",
            "Option A is incorrect because stored elastic potential energy is under the contraction curve. Options C and D describe the total areas under individual curves, not the enclosed loop area."
        ]
    },

    # Q20
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q20",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "motion_path_representation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_progressive_wave_properties",
        "accepted_answer": "D",
        "hints": [
            "Determine the period T of the wave from its frequency f = 2.0 Hz (T = 1 / f).",
            "In one full time period, the wave profile advances to the right by exactly one wavelength lambda."
        ],
        "walkthrough": [
            "The frequency is f = 2.0 Hz, so the period is T = 1 / f = 1 / 2.0 = 0.50 s.",
            "From the initial graph at t = 0, one full wave cycle spans from x = 0 to x = 2.0 m, so the wavelength is λ = 2.0 m.",
            "The front (leading edge) of the wave at t = 0 is located at x = 8.0 m.",
            "In a time interval of t = 0.50 s (exactly one period T), the entire wave profile travels to the right by one wavelength λ = 2.0 m.",
            "The leading edge moves to x = 8.0 m + 2.0 m = 10.0 m, maintaining the same periodic waveform between 0 and 10 m. Diagram D correctly shows the wave advancing to 10.0 m, matching the calculated position.",
            "Diagrams A, B, and C show the leading edge at incorrect distances or with inverted phase shifts."
        ]
    },

    # Q21
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q21",
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
            "Find the period T from Graph 1 (displacement-time) and the wavelength lambda from Graph 2 (displacement-distance).",
            "Calculate wave speed using v = lambda / T = f × lambda."
        ],
        "walkthrough": [
            "From Graph 1 (displacement against time), one complete oscillation cycle occurs between t = 0 and t = 0.50 s, so the period is T = 0.50 s (frequency f = 2.0 Hz).",
            "From Graph 2 (displacement against distance), the distance between successive peaks (e.g. from 0 to 60 cm) is the wavelength λ = 60 cm.",
            "The speed of the wave is v = λ / T = 60 cm / 0.50 s = 120 cm s⁻¹, which matches option D.",
            "Option A (22.5 cm s⁻¹) and Option B (30.0 cm s⁻¹) confuse half-wavelengths or quarter-periods. Option C (90.0 cm s⁻¹) misreads the distance axis."
        ]
    },

    # Q22
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q22",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "direct_calculation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_oscilloscope_traces",
        "accepted_answer": "C",
        "hints": [
            "Count the number of complete cycles displayed across the grid divisions to determine the number of divisions per cycle.",
            "Multiply the divisions per cycle by the time-base setting (2.00 ms/div) to find the period T, then calculate frequency f = 1 / T."
        ],
        "walkthrough": [
            "On the CRO screen, 4 complete wave cycles occupy exactly 8 horizontal grid divisions, which means each cycle has a horizontal length of 8 div / 4 = 2.0 divisions.",
            "Given the time-base setting of 2.00 ms / division, the period of the sound wave is T = 2.0 div × 2.00 ms / div = 4.00 ms = 4.00 × 10⁻³ s.",
            "The frequency is f = 1 / T = 1 / (4.00 × 10⁻³ s) = 250 Hz, which corresponds to option C.",
            "Option A (63 Hz) incorrectly uses the full 8 divisions for a single period. Option B (170 Hz) uses an inaccurate division estimate. Option D (500 Hz) takes half a division or inverts the period calculation."
        ]
    },

    # Q23
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q23",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": [
            "multi_step_calculation",
            "equation_derivation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m03",
        "skill_id": "9702_skill_doppler_effect",
        "accepted_answer": "C",
        "hints": [
            "The maximum observed frequency occurs when the moving sound source is travelling directly towards the observer at speed vs = 15.0 m s^-1.",
            "Apply the Doppler formula for a source moving towards a stationary observer: fo = fs × (v / (v - vs)), and solve algebraically for the speed of sound v."
        ],
        "walkthrough": [
            "When the source moves directly towards the observer at speed v_s = 15.0 m s⁻¹, the observed frequency reaches its maximum value: f_o = f_s × [v / (v - v_s)].",
            "Substitute the given values: 2097 = 2000 × [v / (v - 15.0)].",
            "Divide both sides by 2000: 2097 / 2000 = 1.0485 = v / (v - 15.0).",
            "Multiply across and solve: 1.0485 × (v - 15.0) = v ==> 1.0485v - 15.7275 = v ==> 0.0485v = 15.7275.",
            "v = 15.7275 / 0.0485 ≈ 324.28 m s⁻¹ ≈ 324 m s⁻¹, matching option C.",
            "Options A, B, and D correspond to arithmetic errors or mistakenly using the recession formula (v + v_s)."
        ]
    },

    # Q24
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q24",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "classification",
            "property_identification"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m04",
        "skill_id": "9702_skill_electromagnetic_spectrum",
        "accepted_answer": "B",
        "hints": [
            "Recall the approximate wavelength ranges of electromagnetic waves in vacuum: visible light is 400 nm to 700 nm, microwaves are 1 mm to 1 m.",
            "Convert 5.0 × 10⁻⁷ m into nanometers (500 nm) and 5.0 × 10⁻² m into centimeters (5 cm) to classify them."
        ],
        "walkthrough": [
            "A wavelength of 5.0 × 10⁻⁷ m = 500 nm falls squarely in the visible light spectrum (which ranges from roughly 400 nm violet to 700 nm red).",
            "A wavelength of 5.0 × 10⁻² m = 5.0 cm lies within the microwave band (which spans from approximately 1 mm to 1 m).",
            "Row B correctly classifies the waves as visible and microwave respectively.",
            "Option A incorrectly identifies 500 nm as ultraviolet (UV is typically < 400 nm) and 5 cm as infrared (IR is typically 700 nm to 1 mm). Options C and D contain similar misclassifications."
        ]
    },

    # Q25
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q25",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "multi_step_calculation",
            "property_identification"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m01",
        "skill_id": "9702_skill_stationary_waves",
        "accepted_answer": "C",
        "hints": [
            "Find the wavelength of the 1.00 GHz EM wave using c = f × lambda with c = 3.00 × 10⁸ m s⁻¹.",
            "In a stationary wave, nodes are separated by lambda / 2, and exactly one antinode lies between every adjacent pair of nodes."
        ],
        "walkthrough": [
            "The wavelength of the electromagnetic wave is λ = c / f = (3.00 × 10⁸ m s⁻¹) / (1.00 × 10⁹ Hz) = 0.30 m = 30 cm.",
            "The distance between adjacent nodes in a stationary wave is λ / 2 = 30 cm / 2 = 15 cm.",
            "The transmitter and the surface are separated by L = 45 cm, with a node at x = 0 cm and a node at x = 45 cm.",
            "The number of half-wavelength segments is N = 45 cm / 15 cm = 3.",
            "Each half-wavelength loop contains one antinode (located at 7.5 cm, 22.5 cm, and 37.5 cm). Therefore, there are 3 antinodes in total between the transmitter and the surface, corresponding to option C.",
            "Options A, B, and D correspond to miscounting loops or miscalculating λ."
        ]
    },

    # Q26
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q26",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "comparison",
            "property_identification"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m02",
        "skill_id": "9702_skill_progressive_wave_properties",
        "accepted_answer": "B",
        "hints": [
            "Consider the fundamental wave equation v = f × lambda and how frequency relates to wavelength at constant wave speed in a medium.",
            "Recall that sound is a longitudinal mechanical wave requiring a medium, while light is a transverse electromagnetic wave."
        ],
        "walkthrough": [
            "For any progressive wave in a given medium, wave speed v is constant, and v = f × λ ==> f = v / λ. Thus, for both light and sound waves, frequency is inversely proportional to wavelength (f ∝ 1/λ), making statement B correct.",
            "Statement A is incorrect because sound is a mechanical wave requiring particles to propagate and cannot travel through free space (vacuum).",
            "Statement C is incorrect because wave intensity is proportional to the square of amplitude (I ∝ A²), not linearly proportional to amplitude.",
            "Statement D is incorrect because only light (transverse) has oscillations perpendicular to energy transfer; sound waves in air are longitudinal with oscillations parallel to energy transfer."
        ]
    },

    # Q27
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q27",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "interference_analysis",
            "property_identification"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m03",
        "skill_id": "9702_skill_two_source_interference",
        "accepted_answer": "D",
        "hints": [
            "Wavefront lines represent wave crests (points of identical phase).",
            "Constructive interference (maximum intensity and loudest sound) occurs where two crests intersect (where two wavefront lines cross)."
        ],
        "walkthrough": [
            "The curved lines represent wavefronts (crests) emitted from the two coherent speakers.",
            "Loudest sound occurs at points of constructive interference where two wave crests meet (intersection of two solid wavefront lines), creating maximum resultant amplitude (2A) and maximum sound intensity (I ∝ (2A)² = 4A²).",
            "Looking at the diagram, point D lies directly on the intersection of a wavefront from the left speaker and a wavefront from the right speaker (crest meets crest).",
            "Point A lies on a wavefront of one speaker but halfway between wavefronts (a trough) of the other, resulting in destructive interference. Points B and C similarly lie in regions of destructive or intermediate interference. Thus, D is the position of loudest sound."
        ]
    },

    # Q28
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q28",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m04",
        "skill_id": "9702_skill_diffraction_grating",
        "accepted_answer": "B",
        "hints": [
            "Calculate the grating spacing d in meters: d = (1 cm / 5000) = (10⁻² m / 5000).",
            "Apply the diffraction grating equation d × sin(theta) = n × lambda with n = 2 and theta = 30 degrees."
        ],
        "walkthrough": [
            "The grating spacing d is d = 1 cm / 5000 = (1.0 × 10⁻² m) / 5000 = 2.0 × 10⁻⁶ m.",
            "Using the diffraction grating equation d × sin(θ) = n × λ for the second-order maximum (n = 2) at θ = 30° (where sin(30°) = 0.50):",
            "λ = [d × sin(θ)] / n = [(2.0 × 10⁻⁶ m) × 0.50] / 2 = 5.0 × 10⁻⁷ m, which matches option B.",
            "Option A (2.5 × 10⁻⁷ m) divides by 4 or uses n = 4. Option C (1.0 × 10⁻⁶ m) forgets to divide by n = 2. Option D (5.0 × 10⁻⁵ m) contains a metric conversion power-of-ten error."
        ]
    },

    # Q29
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q29",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "electric_field_line_construction",
            "property_identification"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m01",
        "skill_id": "9702_skill_uniform_electric_fields",
        "accepted_answer": "C",
        "hints": [
            "Determine the sign of charge X: since a negative test charge experiences repulsion away from X, charge X must be negative.",
            "Recall the definition of electric field direction: the direction of the force acting on a positive test charge placed at that point."
        ],
        "walkthrough": [
            "A negative test charge placed at P is repelled radially away from X (to the right). Since like charges repel, source charge X must carry a negative charge.",
            "By definition, the direction of an electric field at any point is the direction of the electrostatic force that would act on a stationary positive test charge placed at that point.",
            "A positive test charge at point P would be attracted towards the negative charge X (i.e. directed horizontally to the left).",
            "Therefore, the electric field vector at P points to the left, which is represented by arrow C.",
            "Arrow A points to the right (the direction of force on a negative charge, not positive). Arrows B and D point perpendicularly, which contradicts radial symmetry."
        ]
    },

    # Q30
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q30",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": [
            "equation_derivation",
            "property_identification"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_uniform_electric_fields",
        "accepted_answer": "B",
        "hints": [
            "The oil drop is held stationary in equilibrium, so the upward electric force balances the downward weight (qE = mg).",
            "Substitute q = n × e and E = V / d into the equilibrium condition and solve for n."
        ],
        "walkthrough": [
            "For the oil drop to remain stationary in equilibrium, the upward electric force F_E must equal the downward gravitational force (weight W = mg): F_E = mg.",
            "The charge of the oil drop with n excess electrons is q = n × e.",
            "In a uniform electric field between parallel plates separated by distance d with voltage V, the electric field strength is E = V / d.",
            "The electric force is F_E = qE = n × e × (V / d).",
            "Equating forces: n × e × (V / d) = mg ==> n = mgd / (eV), which corresponds to option B.",
            "Option A inverts the expression (eV / mgd). Options C and D have incorrect dimensional arrangements of mass and gravity."
        ]
    },

    # Q31
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q31",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": [
            "multi_step_calculation",
            "property_identification"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m01",
        "skill_id": "9702_skill_electric_current_drift_speed",
        "accepted_answer": "B",
        "hints": [
            "Use the drift speed equation for electric current: I = n × A × v × e, where e = 1.60 × 10⁻¹⁹ C.",
            "Calculate the required product (n × A) = I / (v × e) and check which row produces this product."
        ],
        "walkthrough": [
            "Electric current is given by I = nAvq, where q = e = 1.60 × 10⁻¹⁹ C is the elementary charge.",
            "Rearranging for the product of number density n and cross-sectional area A:",
            "nA = I / (ve) = 5.0 A / [(7.4 × 10⁻⁴ m s⁻¹)(1.60 × 10⁻¹⁹ C)] = 5.0 / (1.184 × 10⁻²²) ≈ 4.223 × 10²² m⁻¹.",
            "Testing the options for the product A × n:",
            "Row A: (7.2 × 10⁻⁷)(1.2 × 10²⁸) = 8.64 × 10²¹ m⁻¹",
            "Row B: (7.2 × 10⁻⁷)(5.9 × 10²⁸) = 4.248 × 10²² m⁻¹ ≈ 4.22 × 10²² m⁻¹",
            "Row C: (2.3 × 10⁻⁶)(7.3 × 10²⁶) = 1.68 × 10²¹ m⁻¹",
            "Row D: (2.3 × 10⁻⁶)(3.7 × 10²⁷) = 8.51 × 10²¹ m⁻¹",
            "Row B matches the calculated product, making B the correct choice."
        ]
    },

    # Q32
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q32",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_potential_difference_power",
        "accepted_answer": "C",
        "hints": [
            "Electric power dissipated in a fixed resistor of resistance R with current I is given by P = I² × R.",
            "Determine the new doubled current (2 × 0.20 A = 0.40 A) and calculate the new power dissipation."
        ],
        "walkthrough": [
            "The initial current is I₁ = 0.20 A. When the current is doubled, the new current is I₂ = 2 × 0.20 A = 0.40 A.",
            "The power dissipated in the resistor is given by P = I² × R.",
            "Calculating the new power: P₂ = (0.40 A)² × 12 Ω = 0.16 × 12 = 1.92 W ≈ 1.9 W, which matches option C.",
            "Option A (0.48 W) is the initial power P₁ = (0.20)² × 12 = 0.48 W. Option B (0.96 W) incorrectly assumes power is directly proportional to current (P ∝ I) instead of current squared (P ∝ I²). Option D (4.8 W) is a calculation error."
        ]
    },

    # Q33
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q33",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "property_identification",
            "equation_recall"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_potential_difference_power",
        "accepted_answer": "C",
        "hints": [
            "Recall that electrical potential difference is defined as energy transfer per unit charge (V = W / Q).",
            "Look for a formula for electrical energy that does not require time t."
        ],
        "walkthrough": [
            "By definition, potential difference V is the electrical energy W converted per unit charge Q: V = W / Q ==> W = QV.",
            "Therefore, knowing the total charge Q passing through the resistor and the potential difference V across it allows direct calculation of energy without needing the duration of current flow t, which makes C correct.",
            "For options A (I and V), B (R and I), and D (Q and R), the energy expressions are W = IVt, W = I²Rt, and W = (Q²R) / t respectively. Each of these formulas requires explicit knowledge of time t to evaluate total energy."
        ]
    },

    # Q34
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q34",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": [
            "circuit_analysis",
            "equation_derivation"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_emf_internal_resistance",
        "accepted_answer": "A",
        "hints": [
            "Express the current I in the single closed series loop in terms of total e.m.f. (E1 + E2) and total resistance (R + r1 + r2).",
            "Use the condition that terminal p.d. across cell 1 is zero (V1 = E1 - I × r1 = 0) to equate expressions for I and solve for R."
        ],
        "walkthrough": [
            "The two cells are connected in series aiding with external resistor R, so the total e.m.f. is E_total = E₁ + E₂ and the total resistance is R_total = R + r₁ + r₂.",
            "The circuit current is I = (E₁ + E₂) / (R + r₁ + r₂).",
            "The terminal potential difference across cell 1 is given by V₁ = E₁ - I r₁. Since V₁ = 0, we have I = E₁ / r₁.",
            "Equating the two expressions for current:",
            "E₁ / r₁ = (E₁ + E₂) / (R + r₁ + r₂)",
            "E₁(R + r₁ + r₂) = r₁(E₁ + E₂)",
            "E₁R + E₁r₁ + E₁r₂ = E₁r₁ + E₂r₁",
            "E₁R = E₂r₁ - E₁r₂ ==> R = (E₂r₁ - E₁r₂) / E₁, which matches option A.",
            "Options B, C, and D feature incorrect denominators or reversed algebraic signs."
        ]
    },

    # Q35
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q35",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "circuit_analysis",
            "explanation"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_emf_internal_resistance",
        "accepted_answer": "C",
        "hints": [
            "Relate terminal potential difference V to battery e.m.f. E, current I, and internal resistance r using V = E - I × r.",
            "Identify which component term represents 'lost volts' (the p.d. dropped across internal resistance r) when current I increases."
        ],
        "walkthrough": [
            "The terminal potential difference V of a battery delivering current I is given by V = E - Ir, where E is the constant e.m.f. and r is the constant internal resistance.",
            "The term Ir is the potential difference across the internal resistance r (often termed 'lost volts').",
            "When the variable resistor is decreased to allow current I to increase, the p.d. across the internal resistance (Ir) increases.",
            "Since V = E - Ir and E is constant, an increase in the p.d. across r causes the terminal potential difference V to decrease, which makes C the correct explanation.",
            "Option A is incorrect because e.m.f. is an intrinsic characteristic of the battery chemical reaction. Option B is incorrect because internal resistance r is a constant property. Option D is incorrect because increasing I requires decreasing the variable resistor."
        ]
    },

    # Q36
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q36",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "circuit_analysis",
            "comparison"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_resistor_networks",
        "accepted_answer": "C",
        "hints": [
            "Let each identical resistor have resistance R.",
            "Calculate the equivalent total resistance for network X (two in series parallel to one), network Y (three in parallel), and network Z (one in series with two in parallel), then arrange from lowest to highest."
        ],
        "walkthrough": [
            "Let the resistance of each individual resistor be R.",
            "For network X: a branch of two series resistors (2R) is in parallel with one resistor (R). Total resistance R_X = (2R × R) / (2R + R) = (2/3)R ≈ 0.67R.",
            "For network Y: all three resistors are in parallel. Total resistance R_Y = R / 3 ≈ 0.33R.",
            "For network Z: one single resistor (R) is in series with a parallel pair of resistors (R / 2). Total resistance R_Z = R + (R / 2) = (3/2)R = 1.50R.",
            "Arranging in order of increasing resistance (lowest first): R_Y (0.33R) < R_X (0.67R) < R_Z (1.50R), which gives Y --> X --> Z, corresponding to option C.",
            "Options A, B, and D give incorrect orderings of these network combinations."
        ]
    },

    # Q37
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q37",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": [
            "circuit_analysis",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m03",
        "skill_id": "9702_skill_potential_dividers",
        "accepted_answer": "A",
        "hints": [
            "When the galvanometer reads zero (null deflection), no current flows in the galvanometer branch, so the p.d. across the combination of resistor R and the 2.0 ohm resistor equals 2.0 V.",
            "Set up the potential divider ratio: V_branch / V_total = (R + 2.0) / (R + 2.0 + 10) = 2.0 / 6.0 and solve for R."
        ],
        "walkthrough": [
            "When the galvanometer reads zero, no current flows into the 2.0 V cell branch. Therefore, the main potential divider circuit carries the full current from the 6.0 V battery.",
            "The total resistance of the potential divider chain is R_total = R + 2.0 Ω + 10 Ω = R + 12 Ω.",
            "The galvanometer branch is connected across (R + 2.0 Ω). At balance, the p.d. across this section equals the e.m.f. of the lower cell (2.0 V).",
            "Applying the potential divider formula:",
            "[(R + 2.0) / (R + 12)] × 6.0 V = 2.0 V",
            "(R + 2.0) / (R + 12) = 2.0 / 6.0 = 1 / 3",
            "3(R + 2.0) = R + 12 ==> 3R + 6.0 = R + 12 ==> 2R = 6.0 ==> R = 3.0 Ω, which corresponds to option A.",
            "Options B (5.0 Ω), C (8.0 Ω), and D (18 Ω) result from setting up the resistance ratio incorrectly (e.g. omitting the 2.0 ohm resistor or dividing by 10 ohm only)."
        ]
    },

    # Q38
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q38",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "property_identification",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m01",
        "skill_id": "9702_skill_nuclear_atom_scattering",
        "accepted_answer": "B",
        "hints": [
            "For a neutral atom with proton number Z and nucleon number A: number of protons = Z, neutrons = A - Z, and electrons = Z.",
            "Total particles = protons + neutrons + electrons = Z + (A - Z) + Z = A + Z, so Z = (total particles) - A. Calculate Z for all four atoms to find which two share the same proton number."
        ],
        "walkthrough": [
            "In a neutral atom, the number of electrons equals the number of protons (Z).",
            "The nucleon number A is the sum of protons and neutrons (A = Z + N).",
            "The total number of particles is N_total = protons + neutrons + electrons = Z + (A - Z) + Z = A + Z.",
            "Therefore, the proton number is given by Z = N_total - A:",
            "For W: Z_W = 24 - 16 = 8",
            "For X: Z_X = 26 - 17 = 9",
            "For Y: Z_Y = 25 - 17 = 8",
            "For Z: Z_Z = 28 - 18 = 10",
            "Atoms W and Y both have proton number Z = 8 (and different nucleon numbers 16 and 17), so they are isotopes of the same element (oxygen). The proton number is 8, which corresponds to option B."
        ]
    },

    # Q39
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q39",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "classification",
            "property_identification"
        ],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m02",
        "skill_id": "9702_skill_fundamental_particles_interactions",
        "accepted_answer": "C",
        "hints": [
            "A fundamental particle has no internal substructure and is not made up of smaller constituent particles.",
            "Recall which particles are leptons (fundamental) and which are hadrons made up of quarks."
        ],
        "walkthrough": [
            "Fundamental particles are elementary particles that have no known sub-structure and cannot be broken down into smaller components.",
            "Electrons, neutrinos, and positrons are all leptons, which are fundamental particles.",
            "A neutron is a baryon (a hadron) composed of three quarks (one up quark and two down quarks, udd). Because it has a composite structure made of quarks, a neutron is NOT a fundamental particle.",
            "Thus, C is the correct answer.",
            "Options A, B, and D are all fundamental leptons."
        ]
    },

    # Q40
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_12_q40",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "property_identification",
            "equation_completion"
        ],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m02",
        "skill_id": "9702_skill_quark_model_hadrons",
        "accepted_answer": "B",
        "hints": [
            "In beta-minus decay, a neutron in the nucleus converts into a proton, an electron, and an electron antineutrino.",
            "Write down the quark compositions of a neutron (udd) and a proton (uud) to find the net change in up and down quarks."
        ],
        "walkthrough": [
            "During β⁻ decay, a neutron converts into a proton inside the nucleus: n --> p + e⁻ + ν̅_e.",
            "The quark composition of a neutron is udd (one up quark and two down quarks).",
            "The quark composition of a proton is uud (two up quarks and one down quark).",
            "At the quark level, this transformation occurs when one down quark changes into an up quark: d --> u + e⁻ + ν̅_e.",
            "As a result, the nucleus gains one up quark (+1) and loses one down quark (-1), which corresponds to row B.",
            "Option A assumes no down quark is lost. Option C represents β⁺ decay (u --> d). Option D indicates an increase in down quarks."
        ]
    }
]

def main():
    print(f"Generating {len(ENRICHMENTS)} enrichment records...")
    for item in ENRICHMENTS:
        qid = item['question_id']
        filename = f"{qid}.enrichment.json"
        filepath = ENRICH_DIR / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(item, f, indent=2, ensure_ascii=False)
            f.write('\n')
        print(f"Wrote {filepath.name}")
    print("Done generating enrichment records.")

if __name__ == '__main__':
    main()
