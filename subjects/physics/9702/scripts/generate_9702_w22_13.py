#!/usr/bin/env python3
"""
generate_9702_w22_13.py

Generates flat enrichment JSON records for 9702_w22_13 (Questions 01 to 40)
matching schema 9702_p1_enrichment_v1.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENRICH_DIR = ROOT / 'subjects/physics/9702/enrichment/p1'
ENRICH_DIR.mkdir(parents=True, exist_ok=True)

data = [
    {
        "question_id": "9702_w22_13_q01",
        "difficulty": 2,
        "question_patterns": ["physical_quantity_estimation", "direct_calculation"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m01",
        "skill_id": "9702_skill_physical_estimations",
        "accepted_answer": "B",
        "hints": [
            "Convert the train's speed from km h⁻¹ to the SI unit m s⁻¹ by multiplying by 1000/3600.",
            "Use the kinetic energy formula E_k = (1/2)mv² and find the power of 10 that best approximates the calculated value."
        ],
        "walkthrough": [
            "First convert the speed v = 100 km h⁻¹ into SI base units: v = (100 × 10³ m) / 3600 s ≈ 27.8 m s⁻¹.",
            "Calculate the kinetic energy: E_k = (1/2) m v² = (1/2) × (600 000 kg) × (27.8 m s⁻¹)² ≈ 300 000 × 771.6 ≈ 2.3 × 10⁸ J.",
            "The order of magnitude is the power of 10 closest to 2.3 × 10⁸ J, which is 10⁸ J, corresponding to option B."
        ]
    },
    {
        "question_id": "9702_w22_13_q02",
        "difficulty": 2,
        "question_patterns": ["equation_derivation", "property_identification"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m02",
        "skill_id": "9702_skill_si_units_homogeneity",
        "accepted_answer": "B",
        "hints": [
            "Recall that electromotive force (e.m.f.) is defined as energy transferred per unit charge: E = W / Q.",
            "Express work/energy W = F × d and charge Q = I × t in terms of SI base units (kg, m, s, A)."
        ],
        "walkthrough": [
            "Electromotive force is energy converted per unit charge: e.m.f. = W / Q.",
            "The base units of work (energy) are kg m² s⁻² (from force × distance = kg m s⁻² × m) and charge is A s (from I × t).",
            "Dividing work by charge gives (kg m² s⁻²) / (A s) = kg m² s⁻³ A⁻¹, which matches option B."
        ]
    },
    {
        "question_id": "9702_w22_13_q03",
        "difficulty": 3,
        "question_patterns": ["uncertainty_analysis", "direct_calculation"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m03",
        "skill_id": "9702_skill_errors_uncertainties",
        "accepted_answer": "C",
        "hints": [
            "Find the central (mean) reading from the fluctuating range and calculate the half-range uncertainty due to fluctuation.",
            "Add the meter's percentage accuracy uncertainty (1% of the central reading) to the fluctuation uncertainty to find the total absolute uncertainty."
        ],
        "walkthrough": [
            "The central value of the fluctuating meter reading is the mean: (3.04 + 3.08) / 2 = 3.06 A.",
            "The uncertainty due to reading fluctuation is the half-range: (3.08 - 3.04) / 2 = 0.02 A.",
            "The meter calibration/accuracy uncertainty is ±1% of 3.06 A: 0.01 × 3.06 = 0.0306 A ≈ 0.03 A.",
            "The total absolute uncertainty is the sum of both independent sources of uncertainty: 0.02 + 0.0306 = 0.0506 A ≈ 0.05 A. Thus, the current is (3.06 ± 0.05) A, which corresponds to option C."
        ]
    },
    {
        "question_id": "9702_w22_13_q04",
        "difficulty": 1,
        "question_patterns": ["classification", "property_identification"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m04",
        "skill_id": "9702_skill_scalars_vectors",
        "accepted_answer": "D",
        "hints": [
            "Recall the distinction between scalar quantities (magnitude only) and vector quantities (magnitude and direction).",
            "Identify which of the given quantities is a gravitational force acting towards the center of a mass."
        ],
        "walkthrough": [
            "A vector quantity possesses both magnitude and direction.",
            "Density, mass, and volume are scalar quantities because they are completely specified by a magnitude and a unit without direction.",
            "Weight is the gravitational force acting on a mass directed towards the center of the Earth, making it a vector quantity (option D)."
        ]
    },
    {
        "question_id": "9702_w22_13_q05",
        "difficulty": 1,
        "question_patterns": ["graph_interpretation", "property_identification"],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_projectile_motion",
        "accepted_answer": "A",
        "hints": [
            "Consider the horizontal and vertical motions independently: horizontal acceleration is zero when air resistance is negligible.",
            "Identify how vertical velocity varies with time under constant downward gravitational acceleration g starting from rest (v_V = 0 at t = 0)."
        ],
        "walkthrough": [
            "With negligible air resistance, there is no horizontal resultant force, so the horizontal component of velocity v_H remains constant with time, appearing as a horizontal straight line.",
            "In the vertical direction, the stone accelerates downwards under uniform gravity g, so vertical velocity increases linearly from zero according to v_V = g t, appearing as a straight line through the origin with constant positive slope.",
            "Graph A correctly displays a constant non-zero horizontal velocity v_H and a linearly increasing vertical velocity v_V starting from zero."
        ]
    },
    {
        "question_id": "9702_w22_13_q06",
        "difficulty": 2,
        "question_patterns": ["equation_derivation", "comparison"],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_kinematics_equations",
        "accepted_answer": "B",
        "hints": [
            "Use the kinematic equation h = ut + (1/2)gt² with initial velocity u = 0 to express fall time t in terms of distance h and acceleration g.",
            "Form the ratio T_E / T_M and substitute g_E / g_M = 6."
        ],
        "walkthrough": [
            "For an object falling from rest through vertical distance h, h = (1/2) g t² which gives t = √(2h / g).",
            "Taking the ratio of the times: T_E / T_M = √(2h / g_E) / √(2h / g_M) = √(g_M / g_E).",
            "Since g_E / g_M = 6, the inverse ratio is g_M / g_E = 1/6, giving T_E / T_M = √(1/6) = 1/√6, which corresponds to option B."
        ]
    },
    {
        "question_id": "9702_w22_13_q07",
        "difficulty": 2,
        "question_patterns": ["explanation", "property_identification"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m02",
        "skill_id": "9702_skill_drag_terminal_velocity",
        "accepted_answer": "D",
        "hints": [
            "At maximum (terminal) speed, the forward driving force equals the total resistive forces.",
            "Consider what condition would increase the total forward propelling force without reducing pedaling effort."
        ],
        "walkthrough": [
            "At maximum speed, the cyclist is in equilibrium where forward driving force equals the resistive forces (air drag and friction).",
            "When travelling downhill, the component of weight along the slope (W sin θ) adds to the pedaling force, increasing the net forward force.",
            "As a result, a higher speed is required for drag to balance the total forward force, leading to an increased maximum speed (option D). Options A, B, and C all increase resistive drag or reduce efficiency, which would decrease speed."
        ]
    },
    {
        "question_id": "9702_w22_13_q08",
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "multi_step_calculation"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_impulse_force_time",
        "accepted_answer": "D",
        "hints": [
            "Recall Newton's second law in terms of momentum: F = Δp / Δt = m(v - u) / Δt.",
            "Remember that velocity is a vector: if initial velocity is +12 m s⁻¹, the rebound velocity is in the opposite direction (-8 m s⁻¹)."
        ],
        "walkthrough": [
            "Choose the initial direction of motion as positive: u = +12 m s⁻¹. After bouncing back, the final velocity is v = -8 m s⁻¹.",
            "The change in momentum is Δp = m(v - u) = 0.5 kg × (-8 - 12) m s⁻¹ = 0.5 × (-20) = -10 kg m s⁻¹.",
            "The magnitude of average force exerted on the ball is F = |Δp| / Δt = 10 N s / 0.10 s = 100 N, which corresponds to option D."
        ]
    },
    {
        "question_id": "9702_w22_13_q09",
        "difficulty": 2,
        "question_patterns": ["explanation", "property_identification"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m02",
        "skill_id": "9702_skill_drag_terminal_velocity",
        "accepted_answer": "A",
        "hints": [
            "Determine the direction of each force: upthrust X acts upwards, weight acts downwards, and the viscous drag force opposes the upward motion (acts downwards).",
            "At terminal velocity, the bubble is in equilibrium with zero resultant force: upward forces equal downward forces."
        ],
        "walkthrough": [
            "As the bubble rises upwards at constant velocity, upthrust X acts upwards, while the bubble's weight Y acts downwards and viscous drag Z acts downwards opposing motion.",
            "Because the bubble moves at terminal (constant) velocity, the acceleration is zero and the net force is zero: X = Y + Z.",
            "Therefore, Z is the viscous drag force, Y is the weight, and X = Y + Z, which correctly matches option A."
        ]
    },
    {
        "question_id": "9702_w22_13_q10",
        "difficulty": 3,
        "question_patterns": ["comparison", "equation_derivation"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m03",
        "skill_id": "9702_skill_linear_momentum_collisions",
        "accepted_answer": "B",
        "hints": [
            "Use conservation of linear momentum for each collision: compare the momentum imparted to the wooden block versus the steel block.",
            "Notice that in the collision with the steel block, the ball rebounds backwards, causing a greater change in the ball's momentum."
        ],
        "walkthrough": [
            "Let m be the mass of the steel ball and M be the mass of each block. For the wooden block (inelastic collision): initial momentum p_i = m v = (M + m) v_wood, giving v_wood = (m v) / (M + m).",
            "For the steel block: the ball rebounds with velocity -v/2. The change in momentum of the ball is Δp_ball = -m(v/2) - m v = -1.5 m v.",
            "By conservation of momentum, the steel block gains momentum +1.5 m v = M v_steel, so v_steel = 1.5 m v / M.",
            "Comparing the speeds: (1.5 m v) / M > (m v) / (M + m), so the steel block must travel faster than the wooden block (option B)."
        ]
    },
    {
        "question_id": "9702_w22_13_q11",
        "difficulty": 1,
        "question_patterns": ["definition", "property_identification"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_moments_couples",
        "accepted_answer": "D",
        "hints": [
            "Recall the definition of a couple: a pair of equal and opposite parallel forces whose lines of action do not coincide.",
            "Check each diagram to ensure the two forces of magnitude F point in opposite directions with parallel lines of action."
        ],
        "walkthrough": [
            "A couple consists of two parallel forces that are equal in magnitude, opposite in direction, and separated by a perpendicular distance so their lines of action do not coincide.",
            "In diagram D, the two forces have equal magnitude F, are parallel, point in opposite directions, and act at different points along the rod to produce a net torque.",
            "Diagrams A and C show forces in the same direction or collinear lines of action, and diagram B does not represent a pure couple (option D is correct)."
        ]
    },
    {
        "question_id": "9702_w22_13_q12",
        "difficulty": 1,
        "question_patterns": ["definition", "property_identification"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_moments_couples",
        "accepted_answer": "D",
        "hints": [
            "Recall the principle of moments for a body in rotational equilibrium.",
            "Consider whether clockwise and anticlockwise moments must be evaluated about the same pivot point."
        ],
        "walkthrough": [
            "The principle of moments states that for a body in rotational equilibrium, the sum of clockwise moments about any chosen point must equal the sum of anticlockwise moments about that exact same point.",
            "Taking moments about two different arbitrary points (X and Y) yields unrelated moment sums unless X and Y are identical.",
            "Therefore, the condition that makes the student's statement correct is that X and Y are the same point on the object (option D)."
        ]
    },
    {
        "question_id": "9702_w22_13_q13",
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "multi_step_calculation"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_moments_couples",
        "accepted_answer": "B",
        "hints": [
            "Take moments about the hinge at the wall to eliminate the unknown hinge reaction force.",
            "Equate the clockwise moment of the uniform rod's weight (acting at its midpoint 15 cm) to the anticlockwise moment of the vertical component of tension (T sin 40° at 30 cm)."
        ],
        "walkthrough": [
            "For rotational equilibrium about the hinge: Σ M = 0.",
            "The clockwise moment produced by the rod's weight W = 5.2 N acting at its center of gravity (0.15 m from hinge) is M_cw = 5.2 N × 0.15 m = 0.78 N m.",
            "The anticlockwise moment produced by the wire tension T at the end (0.30 m from hinge) is M_acw = (T sin 40°) × 0.30 m.",
            "Equating moments: T sin 40° × 0.30 = 0.78, which gives T = 0.78 / (0.30 × sin 40°) = 2.6 / sin 40° ≈ 4.045 N ≈ 4.0 N (option B)."
        ]
    },
    {
        "question_id": "9702_w22_13_q14",
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "multi_step_calculation"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m03",
        "skill_id": "9702_skill_density_pressure",
        "accepted_answer": "C",
        "hints": [
            "Calculate the volume of 100 kg of water using density ρ = 1000 kg m⁻³, then find the volume flow rate ΔV / Δt.",
            "Relate volume flow rate to nozzle cross-sectional area A = π d² / 4 and flow speed v using ΔV / Δt = A v."
        ],
        "walkthrough": [
            "Volume of water moved is V = m / ρ = 100 kg / (1000 kg m⁻³) = 0.10 m³.",
            "Volume flow rate is V / t = 0.10 m³ / 2.0 s = 0.050 m³ s⁻¹.",
            "Cross-sectional area of the circular nozzle is A = π d² / 4 = π (0.050 m)² / 4 ≈ 1.9635 × 10⁻³ m².",
            "Flow speed is v = (V / t) / A = 0.050 / (1.9635 × 10⁻³) ≈ 25.46 m s⁻¹ ≈ 25 m s⁻¹ (option C)."
        ]
    },
    {
        "question_id": "9702_w22_13_q15",
        "difficulty": 1,
        "question_patterns": ["equation_derivation", "property_identification"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m03",
        "skill_id": "9702_skill_density_pressure",
        "accepted_answer": "B",
        "hints": [
            "Express pressure as P = F / A, where force F is the weight W = mg = ρ V g.",
            "Substitute volume V = L³ and base area A = L² for a cube of side length L."
        ],
        "walkthrough": [
            "Pressure is defined as force per unit area: P = W / A = (mg) / A.",
            "For a solid cube of side length L and density ρ, the volume is V = L³ and the base contact area is A = L², so m = ρ V = ρ L³.",
            "Substituting into the pressure formula yields P = (ρ L³ g) / L² = ρ g L, which is the product of acceleration of free fall, density, and side length (option B)."
        ]
    },
    {
        "question_id": "9702_w22_13_q16",
        "difficulty": 1,
        "question_patterns": ["equation_recall", "property_identification"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_power_efficiency",
        "accepted_answer": "B",
        "hints": [
            "Recall the fundamental definition of mechanical power as work done per unit time.",
            "Substitute the definition of work done (W = force × displacement) into the power formula."
        ],
        "walkthrough": [
            "Power is defined as the rate of energy transfer or work done per unit time: P = W / t.",
            "Since work done by a constant force in the direction of motion is W = force × displacement, power can be expressed as (force × displacement) / time.",
            "This matches option B. Option A has an incorrect electrical power formula (I² R, not I²/R), option C has incorrect squaring (I² R, not I R²), and option D is weight over time (which has units of force per second)."
        ]
    },
    {
        "question_id": "9702_w22_13_q17",
        "difficulty": 2,
        "question_patterns": ["property_identification", "explanation"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_conservation_of_energy",
        "accepted_answer": "C",
        "hints": [
            "Identify the conditions under which gravitational potential energy, kinetic energy, and elastic potential energy are each non-zero.",
            "Consider when the jumper is still moving downwards (non-zero speed) while the cord is stretched (non-zero extension)."
        ],
        "walkthrough": [
            "Gravitational potential energy E_p is non-zero whenever the jumper is above the ground reference level.",
            "Kinetic energy E_k is non-zero when the jumper is moving (v > 0). Elastic potential energy E_elastic is non-zero only after the bungee cord starts to extend beyond its natural length (x > 0).",
            "As the jumper decelerates on the way down, the cord is actively extending (E_elastic > 0), the jumper is moving downwards (E_k > 0), and the jumper is above the ground (E_p > 0), making all three non-zero (option C)."
        ]
    },
    {
        "question_id": "9702_w22_13_q18",
        "difficulty": 1,
        "question_patterns": ["property_identification", "explanation"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m02",
        "skill_id": "9702_skill_kinetic_potential_energy",
        "accepted_answer": "B",
        "hints": [
            "Recall that gravitational potential energy in a uniform field depends only on vertical displacement: ΔE_p = mg Δh.",
            "Determine whether moving horizontally across vertical field lines changes the vertical height."
        ],
        "walkthrough": [
            "In a uniform vertical gravitational field, the change in gravitational potential energy is given by ΔE_p = mg Δh, where Δh is the vertical displacement.",
            "A horizontal displacement is perpendicular to the vertical gravitational force, meaning no work is done against gravity (Δh = 0).",
            "Therefore, the gravitational potential energy does not change with horizontal displacement (option B)."
        ]
    },
    {
        "question_id": "9702_w22_13_q19",
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "multi_step_calculation"],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m01",
        "skill_id": "9702_skill_young_modulus",
        "accepted_answer": "C",
        "hints": [
            "Use the Young modulus formula E = (F L) / (A x) rearranged for extension: x = (F L) / (A E).",
            "Calculate the cross-sectional area A = π d² / 4 with d = 1.22 × 10⁻³ m."
        ],
        "walkthrough": [
            "Young modulus is defined as E = stress / strain = (F/A) / (x/L) = (F L) / (A x), so extension x = (F L) / (A E).",
            "Calculate the cross-sectional area: A = π d² / 4 = π (1.22 × 10⁻³ m)² / 4 ≈ 1.169 × 10⁻⁶ m².",
            "Substitute the given parameters: x = (37 N × 3.6 m) / ((1.169 × 10⁻⁶ m²) × (1.17 × 10¹¹ Pa)) = 133.2 / (1.368 × 10⁵) ≈ 9.74 × 10⁻⁴ m = 0.97 mm, which matches option C."
        ]
    },
    {
        "question_id": "9702_w22_13_q20",
        "difficulty": 2,
        "question_patterns": ["equation_derivation", "comparison"],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m02",
        "skill_id": "9702_skill_hookes_law_elastic_energy",
        "accepted_answer": "A",
        "hints": [
            "For two identical springs connected in parallel, determine the combined spring constant k_p.",
            "Use x_p = F / k_p to find extension and E_total = (1/2) F x_p to find the total elastic potential energy."
        ],
        "walkthrough": [
            "When two identical springs of spring constant k are connected in parallel, each spring supports half the load (F/2), so the equivalent spring constant is k_p = 2k.",
            "The resulting extension under the same total force F is x_p = F / (2k) = (1/2) x.",
            "The total elastic potential energy is E_total = (1/2) F x_p = (1/2) F ((1/2) x) = (1/2) ((1/2) F x) = (1/2) E_P.",
            "This matches row A: extension is (1/2) x and total elastic potential energy is (1/2) E_P."
        ]
    },
    {
        "question_id": "9702_w22_13_q21",
        "difficulty": 2,
        "question_patterns": ["graph_interpretation", "property_identification"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_progressive_wave_properties",
        "accepted_answer": "A",
        "hints": [
            "For a particle at a wave crest (maximum displacement), consider its instantaneous velocity.",
            "Shift the progressive waveform slightly to the right to see whether the wave profile at point P moves up or down."
        ],
        "walkthrough": [
            "Point Q is at the crest (maximum positive displacement) where the particle momentarily stops to reverse direction, so point Q is stationary.",
            "The transverse wave travels from left to right. Drawing the wave profile a small time interval Δt later shifts the wave to the right, placing the trough that was to the left of P at P's position, so point P must move downwards.",
            "Therefore, point P moves downwards and point Q is stationary (option A)."
        ]
    },
    {
        "question_id": "9702_w22_13_q22",
        "difficulty": 1,
        "question_patterns": ["direct_calculation", "property_identification"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m04",
        "skill_id": "9702_skill_electromagnetic_spectrum",
        "accepted_answer": "C",
        "hints": [
            "Calculate frequency using f = 1 / T with period T = 1.0 ns = 1.0 × 10⁻⁹ s.",
            "Calculate wavelength using λ = c / f where speed in vacuum is c = 3.0 × 10⁸ m s⁻¹."
        ],
        "walkthrough": [
            "Frequency is the reciprocal of the period: f = 1 / T = 1 / (1.0 × 10⁻⁹ s) = 1.0 × 10⁹ Hz.",
            "In a vacuum, electromagnetic waves travel at c = 3.0 × 10⁸ m s⁻¹. The wavelength is λ = c / f = (3.0 × 10⁸ m s⁻¹) / (1.0 × 10⁹ Hz) = 0.30 m.",
            "This matches row C: frequency is 1.0 × 10⁹ Hz and wavelength is 0.30 m."
        ]
    },
    {
        "question_id": "9702_w22_13_q23",
        "difficulty": 1,
        "question_patterns": ["property_identification", "explanation"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m03",
        "skill_id": "9702_skill_doppler_effect",
        "accepted_answer": "B",
        "hints": [
            "Apply the Doppler effect formula for a moving source at constant speed v_s: f_o = f × v / (v ∓ v_s).",
            "Consider whether the observed frequency remains constant or changes while the train approaches at constant speed, and while it recedes at constant speed."
        ],
        "walkthrough": [
            "When a sound source moves towards a stationary observer at constant speed v_s, the observed frequency is f_o = f × v / (v - v_s), which is constant and higher than the source frequency f.",
            "When the source moves away at constant speed v_s, the observed frequency is f_o = f × v / (v + v_s), which is constant and lower than the source frequency f.",
            "Thus the observer hears a constant sound of higher frequency than f as the train approaches and a constant sound of lower frequency than f as it moves away (option B)."
        ]
    },
    {
        "question_id": "9702_w22_13_q24",
        "difficulty": 1,
        "question_patterns": ["property_identification", "physical_quantity_estimation"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m04",
        "skill_id": "9702_skill_electromagnetic_spectrum",
        "accepted_answer": "A",
        "hints": [
            "Recall the range of wavelengths for visible light in free space: approximately 400 nm to 700 nm.",
            "Convert the given lengths into nanometres to identify which length falls within this visible spectrum."
        ],
        "walkthrough": [
            "The wavelength range of visible light in vacuum/free space extends from approximately 400 nm (0.4 μm) at the violet end to 700 nm (0.7 μm) at the red end.",
            "Algae of length 0.5 μm = 500 nm falls squarely within the visible range (green light).",
            "The other options (5.0 μm, 50 μm, 100 μm) lie in the infrared region and are much larger than visible wavelengths (option A is correct)."
        ]
    },
    {
        "question_id": "9702_w22_13_q25",
        "difficulty": 1,
        "question_patterns": ["definition", "property_identification"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m01",
        "skill_id": "9702_skill_stationary_waves",
        "accepted_answer": "C",
        "hints": [
            "Recall the formation mechanism of a stationary (standing) wave.",
            "Consider the direction of travel required for the two overlapping progressive waves."
        ],
        "walkthrough": [
            "A stationary wave is produced by the superposition of two progressive waves of the same type, frequency, and similar amplitude travelling in opposite directions along the same line.",
            "Stationary waves can be formed from either transverse or longitudinal waves, and do not require polarisation.",
            "Therefore, travelling in opposite directions is the essential condition among the given choices (option C)."
        ]
    },
    {
        "question_id": "9702_w22_13_q26",
        "difficulty": 2,
        "question_patterns": ["explanation", "property_identification"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m01",
        "skill_id": "9702_skill_stationary_waves",
        "accepted_answer": "B",
        "hints": [
            "In a stationary sound wave inside a tube, distinguish between displacement nodes and displacement antinodes.",
            "Consider where the vibrating air molecules have maximum movement to push powder away and where they remain undisturbed."
        ],
        "walkthrough": [
            "In Kundt's tube, stationary longitudinal sound waves form nodes (points of zero or minimum particle displacement amplitude) and antinodes (points of maximum displacement amplitude).",
            "At the antinodes, vigorous vibration of air molecules agitates and sweeps away the fine powder towards regions of stillness.",
            "The powder settles into piles at the displacement nodes where the air molecules vibrate with minimum amplitude (option B)."
        ]
    },
    {
        "question_id": "9702_w22_13_q27",
        "difficulty": 2,
        "question_patterns": ["property_identification", "explanation"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m02",
        "skill_id": "9702_skill_wave_diffraction",
        "accepted_answer": "C",
        "hints": [
            "Recall the condition for significant wave diffraction through an aperture: the ratio λ / d should be as close to 1 (or larger) as possible.",
            "Relate frequency f to wavelength λ using v = f λ at constant sound speed v."
        ],
        "walkthrough": [
            "Diffraction increases when the wavelength λ is closer in size to or greater than the aperture width d (i.e. increasing the ratio λ/d).",
            "Since wave speed v in air is constant, halving the frequency f doubles the wavelength λ (0.50 m → 1.0 m), making λ equal to the doorway width d = 1.0 m.",
            "This increases diffraction significantly (option C). Doubling doorway width decreases λ/d, and changing amplitude has no effect on diffraction."
        ]
    },
    {
        "question_id": "9702_w22_13_q28",
        "difficulty": 2,
        "question_patterns": ["graph_interpretation", "interference_analysis"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m03",
        "skill_id": "9702_skill_two_source_interference",
        "accepted_answer": "C",
        "hints": [
            "Use the double-slit fringe separation formula x = (λ D) / a to compare fringe spacing for red light (x_R) and violet light (x_V).",
            "Note that at the central zero-order maximum (distance = 0), both red and violet light have maximum intensity."
        ],
        "walkthrough": [
            "In double-slit interference, fringe separation is x = (λ D) / a. Because λ_R ≈ 2 λ_V, the fringe separation for red light is roughly twice that for violet light (x_R ≈ 2 x_V).",
            "At the center of the pattern (distance = 0), zero path difference produces overlapping central maxima for both colours.",
            "Moving away from the centre, violet fringes are twice as dense as red fringes (two violet cycles occur for every single red cycle), which is accurately depicted in graph C."
        ]
    },
    {
        "question_id": "9702_w22_13_q29",
        "difficulty": 1,
        "question_patterns": ["definition", "property_identification"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m04",
        "skill_id": "9702_skill_diffraction_grating",
        "accepted_answer": "D",
        "hints": [
            "Recall the diffraction grating equation: d sin θ = n λ.",
            "Identify which wave property can be calculated directly by measuring diffraction angles θ."
        ],
        "walkthrough": [
            "A diffraction grating produces sharp interference maxima at angles θ satisfying d sin θ = n λ, where d is the grating spacing and n is the order number.",
            "By measuring the angles of diffraction for known grating lines per millimetre, the wavelength λ of the incident light wave is directly and accurately determined.",
            "Therefore, wavelength is the property determined (option D)."
        ]
    },
    {
        "question_id": "9702_w22_13_q30",
        "difficulty": 1,
        "question_patterns": ["property_identification", "equation_recall"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m01",
        "skill_id": "9702_skill_electric_current_drift_speed",
        "accepted_answer": "D",
        "hints": [
            "Recall the formula relating electric current to drift speed: I = n A v q.",
            "Rearrange for drift speed v in terms of current I, cross-sectional area A, carrier density n, and elementary charge q."
        ],
        "walkthrough": [
            "The microscopic current equation is I = n A v q, where n is number density of charge carriers, A is cross-sectional area, v is drift speed, and q is charge.",
            "Rearranging gives v = I / (n A q), showing that drift speed v is directly proportional to current I.",
            "This matches statement D. Drift speed is inversely proportional to A, independent of length, and typically on the order of 10⁻⁴ m s⁻¹ (far below speed of light)."
        ]
    },
    {
        "question_id": "9702_w22_13_q31",
        "difficulty": 3,
        "question_patterns": ["multi_step_calculation", "direct_calculation"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_emf_internal_resistance",
        "accepted_answer": "D",
        "hints": [
            "Calculate the energy supplied to the external resistor using W_R = I² R t.",
            "Add the internal energy dissipation to find total energy supplied by the battery, then calculate e.m.f. using E = W_total / Q = W_total / (I t)."
        ],
        "walkthrough": [
            "Energy supplied to the external resistor in t = 60 s is W_R = I² R t = (40 × 10⁻³ A)² × 250 Ω × 60 s = 0.0016 × 15000 = 24 J.",
            "Total electrical energy supplied by the battery is the sum of external energy and internal energy dissipated: W_total = 24 J + 6.0 J = 30 J.",
            "Total charge passed through the battery is Q = I t = (0.040 A) × (60 s) = 2.4 C.",
            "The electromotive force (e.m.f.) is E = W_total / Q = 30 J / 2.4 C = 12.5 V, matching row D (24 J, 12.5 V)."
        ]
    },
    {
        "question_id": "9702_w22_13_q32",
        "difficulty": 1,
        "question_patterns": ["graph_interpretation", "property_identification"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m03",
        "skill_id": "9702_skill_iv_characteristics",
        "accepted_answer": "A",
        "hints": [
            "Observe that the I–V graph is symmetrical about the origin and the gradient ΔI / ΔV decreases as |V| increases.",
            "Relate decreasing gradient to increasing resistance due to heating as current flows in either direction."
        ],
        "walkthrough": [
            "The graph shows a symmetrical non-ohmic characteristic passing through the origin where current increases less rapidly at higher voltages, indicating that resistance R = V / I increases with temperature.",
            "In a metallic filament lamp, heating caused by higher current increases lattice vibrations, scattering conduction electrons and raising resistance, which bends the I–V curve towards the voltage axis.",
            "This corresponds to a filament lamp (option A). An ohmic conductor is a straight line through the origin, and a diode conducts only in the forward direction above a threshold."
        ]
    },
    {
        "question_id": "9702_w22_13_q33",
        "difficulty": 2,
        "question_patterns": ["equation_derivation", "comparison"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m03",
        "skill_id": "9702_skill_resistivity",
        "accepted_answer": "C",
        "hints": [
            "Express resistance in terms of resistivity ρ, length L, and diameter d: R = (ρ L) / (π d² / 4).",
            "Equate R_P = R_Q using ρ_Q = 2 ρ_P and d_Q = 2 d_P to solve for the ratio L_P / L_Q."
        ],
        "walkthrough": [
            "Resistance of a uniform wire is R = (ρ L) / A = (4 ρ L) / (π d²).",
            "Setting R_P = R_Q gives (ρ_P L_P) / (d_P)² = (ρ_Q L_Q) / (d_Q)².",
            "Substitute ρ_Q = 2 ρ_P and d_Q = 2 d_P: (ρ_P L_P) / (d_P)² = (2 ρ_P L_Q) / (2 d_P)² = (2 ρ_P L_Q) / (4 d_P)² = (ρ_P L_Q) / (2 d_P)².",
            "Dividing both sides by ρ_P / (d_P)² yields L_P = L_Q / 2, which gives L_P / L_Q = 1/2, corresponding to option C."
        ]
    },
    {
        "question_id": "9702_w22_13_q34",
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "circuit_analysis"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_emf_internal_resistance",
        "accepted_answer": "B",
        "hints": [
            "The open-circuit reading is the electromotive force: E = 9.000 V.",
            "Find the circuit current using I = V / R = 8.800 V / 11.0 Ω and determine internal resistance from E - V = I r."
        ],
        "walkthrough": [
            "An ideal voltmeter across the disconnected battery measures the open-circuit e.m.f.: E = 9.000 V.",
            "When the 11.0 Ω resistor is connected, terminal potential difference is V = 8.800 V. Current in the circuit is I = V / R = 8.800 V / 11.0 Ω = 0.800 A.",
            "The lost volts across the internal resistance are V_lost = E - V = 9.000 - 8.800 = 0.200 V.",
            "The internal resistance is r = V_lost / I = 0.200 V / 0.800 A = 0.250 Ω, which corresponds to option B."
        ]
    },
    {
        "question_id": "9702_w22_13_q35",
        "difficulty": 1,
        "question_patterns": ["property_identification", "definition"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m02",
        "skill_id": "9702_skill_kirchhoffs_laws",
        "accepted_answer": "C",
        "hints": [
            "Recall that Kirchhoff's first law deals with currents meeting at a junction.",
            "Recall that Kirchhoff's second law deals with electromotive forces and potential drops around a closed loop."
        ],
        "walkthrough": [
            "Kirchhoff's first law states that the sum of currents entering a junction equals the sum of currents leaving (Σ I = 0), which is an expression of conservation of electric charge.",
            "Kirchhoff's second law states that the sum of e.m.f.s around any closed loop equals the sum of potential drops (Σ E = Σ I R), which is an expression of conservation of energy.",
            "Therefore, the conserved quantities are charge for the first law and energy for the second law (option C)."
        ]
    },
    {
        "question_id": "9702_w22_13_q36",
        "difficulty": 3,
        "question_patterns": ["circuit_analysis", "multi_step_calculation"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m02",
        "skill_id": "9702_skill_kirchhoffs_laws",
        "accepted_answer": "C",
        "hints": [
            "Write Kirchhoff's second law for the single closed loop PQR containing three batteries (9.6 V, 8.4 V, 6.3 V) and three identical resistors R.",
            "Determine the potential drop I R across one resistor, then find the potential difference V_PQ along the branch from P to Q."
        ],
        "walkthrough": [
            "Let current I flow clockwise around the single closed circuit loop PQR with three identical resistors R.",
            "Applying Kirchhoff's second law around the loop: net e.m.f. is Σ E = 9.6 V - 8.4 V + 6.3 V = 7.5 V.",
            "Total resistance of the loop is 3R, so the potential drop across each individual resistor is I R = 7.5 V / 3 = 2.5 V.",
            "Starting at P and moving to Q through the branch containing the 9.6 V battery and one resistor: V_P - 9.6 V + I R = V_Q, which gives V_P - V_Q = 9.6 V - 2.5 V = 7.1 V.",
            "Thus the magnitude of potential difference between P and Q is 7.1 V, which corresponds to option C."
        ]
    },
    {
        "question_id": "9702_w22_13_q37",
        "difficulty": 3,
        "question_patterns": ["circuit_analysis", "property_identification"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m03",
        "skill_id": "9702_skill_potentiometer_circuits",
        "accepted_answer": "B",
        "hints": [
            "Consider the potential gradient along the 1.0 m wire: with a 2 V driver cell, the gradient is 2 V m⁻¹, making the balance length for 8 mV impractically short (4 mm).",
            "To obtain higher precision, the potential gradient must be greatly reduced so that 8 mV corresponds to a much larger fraction of the wire's length."
        ],
        "walkthrough": [
            "Originally, the 2 V cell across the 1.0 m wire of resistance 10 Ω creates a potential gradient of 2.0 V m⁻¹ = 2000 mV m⁻¹.",
            "Balancing an e.m.f. of only 8 mV gives a balance length of L = 8 mV / (2000 mV m⁻¹) = 0.004 m = 4 mm, which is too small to measure with high percentage precision.",
            "Adding a large series resistor (1000 Ω) to the driver circuit reduces the p.d. across the 10 Ω wire to V_wire = 2 V × (10 / 1010) ≈ 19.8 mV, giving a potential gradient of ≈ 19.8 mV m⁻¹.",
            "The new balance length becomes L ≈ 8 mV / (19.8 mV m⁻¹) ≈ 0.40 m = 40 cm, which significantly improves measurement precision (option B)."
        ]
    },
    {
        "question_id": "9702_w22_13_q38",
        "difficulty": 1,
        "question_patterns": ["explanation", "property_identification"],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m01",
        "skill_id": "9702_skill_nuclear_atom_scattering",
        "accepted_answer": "A",
        "hints": [
            "Recall the Rutherford alpha-scattering experiment results and the deductions made from them.",
            "Which observation proved that positive charge and mass are concentrated in a tiny central nucleus rather than spread out uniformly?"
        ],
        "walkthrough": [
            "In the Rutherford scattering experiment, most alpha-particles passed straight through the gold foil with little deflection, demonstrating that the atom is mostly empty space.",
            "However, a tiny fraction (about 1 in 8000) was deflected through very large angles (>90°), which could only occur if the alpha-particles encountered a massive, concentrated positive core exerting intense repulsive electrostatic forces.",
            "This large-angle scattering provided conclusive evidence for the existence of the nucleus (option A)."
        ]
    },
    {
        "question_id": "9702_w22_13_q39",
        "difficulty": 2,
        "question_patterns": ["equation_completion", "classification"],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m02",
        "skill_id": "9702_skill_fundamental_particles_interactions",
        "accepted_answer": "D",
        "hints": [
            "Recall that during β⁺ decay, a proton converts into a neutron, releasing a positron and an electron neutrino.",
            "Apply conservation of proton number (charge): Z_X = Z_Y + 1."
        ],
        "walkthrough": [
            "In β⁺ (positron) decay, a proton decays according to p → n + e⁺ + ν_e. To conserve lepton number (L = -1 for e⁺), the emitted neutral lepton P must be a neutrino ν_e (with L = +1).",
            "Applying conservation of charge/atomic number: Z_X = Z_Y + (+1) + 0 = Z + 1.",
            "Therefore, particle P is a neutrino and the proton number of nucleus X is Z + 1, which matches row D."
        ]
    },
    {
        "question_id": "9702_w22_13_q40",
        "difficulty": 1,
        "question_patterns": ["property_identification", "direct_calculation"],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m02",
        "skill_id": "9702_skill_quark_model_hadrons",
        "accepted_answer": "D",
        "hints": [
            "Recall the fractional charges of the fundamental quarks: up (u) and charm (c).",
            "Sum the individual quark charges for the combination (uuc)."
        ],
        "walkthrough": [
            "The up quark (u) has a charge of +(2/3)e and the charm quark (c) has a charge of +(2/3)e.",
            "A baryon with quark structure (uuc) has total charge Q = (+(2/3)e) + (+(2/3)e) + (+(2/3)e) = +(6/3)e = +2e.",
            "This corresponds to +2e (option D)."
        ]
    }
]

def main():
    print(f"Generating {len(data)} enrichment files for 9702_w22_13...")
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
