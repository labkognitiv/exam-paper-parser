import json
import re
from pathlib import Path

enrichments = [
    # Q01
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q01",
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
            "Estimate the typical winning time for an Olympic female sprinter completing a 100 m race.",
            "A world-class female sprinter runs 100 m in approximately 10 to 11 seconds. Use v = s / t to estimate the average speed."
        ],
        "walkthrough": [
            "The winning time for a female Olympic athlete in the 100 m sprint is typically around 10.5 s to 11.0 s.",
            "Using the definition of average speed, v = s / t ≈ (100 m) / (11 s) ≈ 9.1 m s⁻¹, which is closest to 9 m s⁻¹ (Option B).",
            "Option A (6 m s⁻¹) corresponds to a time of roughly 16.7 s, which is too slow for an Olympic final. Options C (12 m s⁻¹) and D (15 m s⁻¹) correspond to impossible 100 m times of 8.3 s and 6.7 s respectively."
        ]
    },
    # Q02
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q02",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "vector_diagram_construction",
            "direct_calculation"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m04",
        "skill_id": "9702_skill_add_vectors",
        "accepted_answer": "A",
        "hints": [
            "Observe the lines of action of the 3 N upward force and the 4 N rightward force relative to the disc's centre.",
            "Since both lines of action pass through the centre of the disc, the resultant force line of action must also pass through the centre. Find its magnitude and angle with the horizontal."
        ],
        "walkthrough": [
            "The 3 N vertical force acts upwards along the vertical line through the centre of the disc, and the 4 N horizontal force acts along the horizontal line through the centre. Because both lines of action pass through the centre, their resultant must also pass through the centre.",
            "The magnitude of the resultant force is R = √(3² + 4²) = 5 N. The angle θ above the horizontal is given by tan θ = 3/4 = 0.75, which gives θ ≈ 37° (less than 45°).",
            "Diagram A correctly displays the 5 N resultant force acting through the centre at an angle below 45° to the horizontal. Diagram C shows an angle greater than 45°, while Diagrams B and D show lines of action that do not pass through the centre."
        ]
    },
    # Q03
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q03",
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
            "Recall the definition of electric potential difference: V = W / Q, where W is work done (energy) and Q is electric charge.",
            "Express the joule (1 J = 1 N m = 1 kg m² s⁻²) and coulomb (1 C = 1 A s) in terms of fundamental SI base units, then evaluate the quotient."
        ],
        "walkthrough": [
            "Potential difference (volt) is defined as energy transferred per unit charge: 1 V = 1 J C⁻¹.",
            "In SI base units, work done (energy) has units kg m² s⁻², and electric charge Q = I t has units A s. Dividing energy by charge gives: (kg m² s⁻²) / (A s) = kg m² s⁻³ A⁻¹.",
            "This matches Option D. Options A and B use derived units (ohm Ω and watt W) rather than base units, and Option C has an incorrect power for seconds (s⁻¹ instead of s⁻³)."
        ]
    },
    # Q04
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q04",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": [
            "uncertainty_analysis",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m03",
        "skill_id": "9702_skill_combine_percentage_uncertainties",
        "accepted_answer": "C",
        "hints": [
            "Determine the dimensions of the block: the length along the current path is L = 15.0 mm, and the cross-sectional area is A = 15.0 mm × 30.0 mm.",
            "Calculate resistivity using ρ = (V A) / (I L), and sum the fractional uncertainties from all five measured quantities (V, I, w, h, L) to find the absolute uncertainty Δρ."
        ],
        "walkthrough": [
            "The current flows through a length L = 15.0 mm = 0.0150 m. The cross-sectional area perpendicular to the current is A = 15.0 mm × 30.0 mm = 4.50 × 10⁻⁴ m². Using ρ = (V A) / (I L): ρ = (10.0 V × 4.50 × 10⁻⁴ m²) / (30.0 × 10⁻³ A × 15.0 × 10⁻³ m) = 10.0 Ω m.",
            "The fractional uncertainty is the sum of fractional uncertainties: Δρ/ρ = ΔV/V + ΔI/I + Δw/w + Δh/h + ΔL/L = 0.1/10.0 + 0.1/30.0 + 0.2/15.0 + 0.2/30.0 + 0.2/15.0 = 0.0100 + 0.00333 + 0.01333 + 0.00667 + 0.01333 = 0.0467 (or 4.67%).",
            "The absolute uncertainty is Δρ = 10.0 × 0.0467 ≈ 0.47 Ω m ≈ 0.5 Ω m. Thus ρ = 10.0 ± 0.5 Ω m (Option C). Options A, B, and D result from neglecting dimensions or combining uncertainties incorrectly."
        ]
    },
    # Q05
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q05",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "measurement_selection",
            "direct_calculation"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m01",
        "skill_id": "9702_skill_measurement",
        "accepted_answer": "B",
        "hints": [
            "Read the main sleeve scale including the half-millimetre mark visible after the 3 mm line, then add the thimble reading.",
            "Use the measured diameter d to calculate the cross-sectional area using A = (π d²) / 4."
        ],
        "walkthrough": [
            "The main sleeve scale shows 3.0 mm plus an exposed bottom half-millimetre mark, giving 3.5 mm. The rotating thimble scale aligns at 31 divisions (0.31 mm). The total measured diameter is d = 3.5 mm + 0.31 mm = 3.81 mm.",
            "The cross-sectional area of the rod is A = (π d²) / 4 = (π × (3.81 mm)²) / 4 ≈ 11.4 mm² (Option B).",
            "Option A (3.81 mm²) mistakenly gives the diameter value with units of area. Option D (45.6 mm²) incorrectly calculates π d² without dividing by 4, and Option C (22.8 mm²) is double the actual cross-sectional area."
        ]
    },
    # Q06
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q06",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "comparison"
        ],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_determine_acceleration_from_velocity_time_graph",
        "accepted_answer": "A",
        "hints": [
            "Analyze the acceleration along each frictionless segment: constant deceleration up PQ, zero acceleration along horizontal QR, and constant acceleration down RS.",
            "Compare the slope magnitudes: RS is steeper than PQ, so the magnitude of acceleration on RS is greater than on PQ. In addition, since P and S are at the same horizontal level, what must be true about the final speed at S?"
        ],
        "walkthrough": [
            "On the frictionless incline PQ, the component of gravity down the slope produces a constant deceleration a₁ = g sin θ_PQ, so speed decreases linearly with time. On the horizontal flat section QR, no net horizontal force acts, so speed is constant (a flat horizontal line).",
            "Descending slope RS, the ball experiences a constant acceleration a₂ = g sin θ_RS. Because slope RS is steeper than PQ (θ_RS > θ_PQ), the magnitude of acceleration is greater, represented by a steeper upward gradient on the v-t graph.",
            "By conservation of mechanical energy on a frictionless track, because point S is at the exact same vertical level as point P, the final speed at S must equal the initial speed at P. Graph A satisfies all these features. Graph C shows a final speed higher than initial speed, Graph B shows decreasing speed along QR, and Graph D shows non-linear acceleration starting from rest."
        ]
    },
    # Q07
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q07",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "explanation"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_apply_newtons_second_law",
        "accepted_answer": "C",
        "hints": [
            "Consider the contact force between the ball and table: at the initial moment of contact and the final moment of detachment, what is the value of the force?",
            "As the ball deforms, the upward normal force increases to a maximum when the ball is at maximum deformation, then decreases back to zero as the ball rebounds."
        ],
        "walkthrough": [
            "When the ball first makes contact with the table at t = 0, deformation is zero, so the contact force F starts at 0. As the ball compresses elastically and decelerates, the contact force increases smoothly to a maximum at maximum deformation (when the vertical velocity is momentarily zero).",
            "During the rebound phase, the ball expands back to its original shape, and the contact force decreases smoothly back to 0 as the ball loses contact with the table surface. This produces a smooth, peaked curve starting and ending at zero (Graph C).",
            "Graph A incorrectly shows force increasing continuously. Graph B depicts non-zero initial force decreasing and increasing. Graph D incorrectly depicts an instantaneous maximum force decaying linearly."
        ]
    },
    # Q08
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q08",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "equation_derivation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_apply_momentum",
        "accepted_answer": "B",
        "hints": [
            "Find the speed just before impact v₁ and speed just after rebound v₂ in terms of heights h₁ and h₂ using conservation of energy or equations of motion.",
            "Recall that momentum is a vector quantity. Because the ball reverses its direction of motion upon bouncing, how do the initial downward and final upward momenta combine to give Δp = p₂ - p₁?"
        ],
        "walkthrough": [
            "Falling from height h₁, the speed just before hitting the surface is v₁ = √(2gh₁). Defining the upward direction as positive, the initial momentum is p₁ = -m√(2gh₁).",
            "Rebounding to height h₂, the speed just after leaving the surface is v₂ = √(2gh₂), so the final momentum is p₂ = +m√(2gh₂).",
            "The change in momentum is Δp = p₂ - p₁ = m√(2gh₂) - (-m√(2gh₁)) = m√(2gh₁) + m√(2gh₂) (Option B). Option A incorrectly subtracts scalar speeds ignoring direction change, while Options C and D improperly combine heights inside the radical."
        ]
    },
    # Q09
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q09",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "explanation",
            "property_identification"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_explain_newtons_third_law",
        "accepted_answer": "C",
        "hints": [
            "Identify the two interacting bodies and the nature of the gravitational force described as the weight of the book.",
            "According to Newton's third law, if the Earth pulls the book downwards with gravitational force W, what force must the book exert in return?"
        ],
        "walkthrough": [
            "Newton's third law states that if body A exerts a force on body B, body B exerts an equal and opposite force of the same type on body A.",
            "The weight W of the book is the gravitational force exerted by the Earth on the book directed downwards. The corresponding Newton's third law reaction force is the gravitational force of magnitude W exerted by the book on the Earth directed upwards (Option C).",
            "Option B describes the normal contact force from the table on the book, which balances weight to provide equilibrium (Newton's first law), but is an electrostatic contact force rather than a third-law pair to gravity. Options A and D describe forces between other pairs of bodies."
        ]
    },
    # Q10
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q10",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "explanation",
            "comparison"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m03",
        "skill_id": "9702_skill_explain_upthrust",
        "accepted_answer": "A",
        "hints": [
            "Recall that upthrust on a submerged body is caused by the difference in hydrostatic pressure between its bottom and top surfaces.",
            "For a fully submerged cylinder of height h, the pressure difference Δp = ρ g h is independent of the depth of submersion. Relate this to tension in equilibrium: T = W - U."
        ],
        "walkthrough": [
            "When the metal cylinder is completely submerged (positions P and Q), the upthrust U = ρ g V is equal to the weight of the displaced water. This upthrust originates from the pressure difference between the lower and upper faces of the cylinder: Δp = p_bottom - p_top = ρ g h_cylinder.",
            "Because Δp and submerged volume are identical at positions P and Q, the upthrust U is identical. In vertical equilibrium, T = W - U; since both W and U are constant, tension T is the same at P and Q (Option A).",
            "Option B is incorrect because although absolute pressure increases with depth, the pressure difference across the cylinder remains constant. Option C is incorrect because at R the cylinder is only partially submerged, so upthrust is smaller and tension is greater than at P. Option D is incorrect because atmospheric pressure acts on all exposed surfaces."
        ]
    },
    # Q11
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q11",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_apply_torque_of_couple",
        "accepted_answer": "C",
        "hints": [
            "The torque of each couple is equal to the force magnitude multiplied by the perpendicular distance between the pair of forces (d = 2r).",
            "Determine the direction of rotation (anticlockwise or clockwise) for each of the four couples and calculate their algebraic sum."
        ],
        "walkthrough": [
            "The torque of a couple is τ = F × 2r. For the 50 N couple at r = 4.0 cm = 0.040 m (d = 0.080 m), the torque acts anticlockwise: τ₁ = +50 × 0.080 = +4.0 N m. For the 30 N couple at r = 6.5 cm = 0.065 m (d = 0.130 m), the torque acts clockwise: τ₂ = -30 × 0.130 = -3.9 N m. For the 16 N couple at r = 10 cm = 0.100 m (d = 0.200 m), the torque acts anticlockwise: τ₃ = +16 × 0.200 = +3.2 N m. For the 25 N couple at r = 12 cm = 0.120 m (d = 0.240 m), the torque acts anticlockwise: τ₄ = +25 × 0.240 = +6.0 N m.",
            "Summing all torques: Στ = +4.0 - 3.9 + 3.2 + 6.0 = +9.3 N m (Option C).",
            "Option D (17.1 N m) is obtained if the clockwise 30 N couple is added instead of subtracted. Options A (4.7 N m) and B (8.6 N m) result from using radius rather than diameter or sign errors."
        ]
    },
    # Q12
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q12",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_apply_principle_of_moments",
        "accepted_answer": "D",
        "hints": [
            "Locate the center of gravity of the uniform 1.0 m beam at 0.5 m from the left end, which is 0.1 m to the left of pivot P (position B).",
            "Calculate total anticlockwise moments and clockwise moments about P, then determine where an additional 20 N weight must be placed to balance them."
        ],
        "walkthrough": [
            "The uniform beam has a total length of 0.6 m + 0.4 m = 1.0 m. Its weight of 100 N acts at its midpoint (0.5 m from the left end), which is 0.1 m to the left of pivot P.",
            "Taking moments about pivot P: Anticlockwise moment = (10 N × 0.6 m) + (100 N × 0.1 m) = 6.0 N m + 10.0 N m = 16.0 N m. Clockwise moment from existing attached weight = 20 N × 0.4 m = 8.0 N m.",
            "To achieve rotational equilibrium, an extra clockwise moment of 16.0 - 8.0 = 8.0 N m is needed. For an additional 20 N weight, distance from P to the right is d = (8.0 N m) / (20 N) = 0.4 m, which is exactly at the right-hand end, position D (Option D)."
        ]
    },
    # Q13
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q13",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "definition",
            "equation_derivation"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m02",
        "skill_id": "9702_skill_derive_si_base_units",
        "accepted_answer": "D",
        "hints": [
            "Express the SI base units of pressure (N m⁻²) and density (kg m⁻³).",
            "Divide the base units of pressure by the base units of density and simplify the indices: (kg m⁻¹ s⁻²) / (kg m⁻³)."
        ],
        "walkthrough": [
            "Pressure is force per unit area: Pa = N m⁻² = (kg m s⁻²) m⁻² = kg m⁻¹ s⁻².",
            "Density is mass per unit volume: kg m⁻³. Dividing pressure by density: (kg m⁻¹ s⁻²) / (kg m⁻³) = m² s⁻² (Option D).",
            "Options A, B, and C contain incorrect base unit combinations for kg and metres."
        ]
    },
    # Q14
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q14",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "classification",
            "property_identification"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m03",
        "skill_id": "9702_skill_classify_collision_elasticity",
        "accepted_answer": "C",
        "hints": [
            "Total energy and linear momentum are always conserved in any closed system undergoing a collision.",
            "An inelastic collision is defined by whether kinetic energy is conserved or partially converted into other energy forms."
        ],
        "walkthrough": [
            "In all collisions within a closed isolated system, total energy is conserved (first law of thermodynamics) and total linear momentum is conserved (Newton's third law).",
            "In an inelastic collision, some macroscopic kinetic energy is converted into thermal energy, sound, or work done during plastic deformation, meaning kinetic energy is not conserved.",
            "Therefore: kinetic energy is not conserved, total energy is conserved, and linear momentum is conserved, matching Row C. Rows A, B, and D incorrectly classify the conservation of kinetic energy, total energy, or momentum."
        ]
    },
    # Q15
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q15",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "multi_step_calculation",
            "direct_calculation"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_conservation_of_energy",
        "accepted_answer": "B",
        "hints": [
            "Calculate the work done against friction over the 20 m distance: W_f = f × d.",
            "Apply conservation of energy at constant speed: Total energy supplied = Increase in GPE + Work done against friction."
        ],
        "walkthrough": [
            "The work done against the resisting frictional force is W_friction = F_friction × d = 8.0 N × 20 m = 160 J.",
            "Because the speed is constant, the kinetic energy does not change (ΔE_k = 0). By conservation of energy, the total energy used (450 J) equals the gain in gravitational potential energy plus work against friction: E_total = ΔE_p + W_friction.",
            "Therefore, ΔE_p = 450 J - 160 J = 290 J (Option B). Option A (160 J) is only the work against friction, while Option D (610 J) erroneously adds the work against friction to the total energy."
        ]
    },
    # Q16
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q16",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "equation_derivation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_determine_average_resistive_force",
        "accepted_answer": "C",
        "hints": [
            "Apply energy conservation: Loss of gravitational potential energy = Gain in kinetic energy + Work done against air resistance (F_drag × h).",
            "Write mgh = 0.5 m v² + F_drag × h and solve for F_drag."
        ],
        "walkthrough": [
            "During the fall through height h, the decrease in gravitational potential energy is ΔE_p = mgh and the increase in kinetic energy is E_k = 0.5 m v².",
            "The work done against average air resistance is W_drag = F_drag × h = mgh - 0.5 m v².",
            "Dividing by h gives F_drag = (mgh - 0.5 m v²) / h = mg - (m v²) / (2h) = m(g - v² / (2h)) (Option C). Option B has an inverted sign and missing factor of 2, while Option D has dimensions of energy rather than force."
        ]
    },
    # Q17
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q17",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "direct_calculation"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m02",
        "skill_id": "9702_skill_apply_kinetic_energy",
        "accepted_answer": "C",
        "hints": [
            "Convert the total mass into kilograms (1 tonne = 1000 kg).",
            "The useful work done on the train from rest equals its final kinetic energy: W = 0.5 m v²."
        ],
        "walkthrough": [
            "The mass of the train in kilograms is m = 1200 tonnes = 1200 × 10³ kg = 1.20 × 10⁶ kg.",
            "The work done to accelerate the train from rest to v = 75 m s⁻¹ equals its kinetic energy: W = 0.5 m v² = 0.5 × (1.20 × 10⁶ kg) × (75 m s⁻¹)² = 0.60 × 10⁶ × 5625 = 3.375 × 10⁹ J ≈ 3.4 × 10⁹ J (Option C).",
            "Option A (3.4 × 10⁶ J) forgets the 10³ conversion factor from tonnes to kg. Options B and D omit the factor of 0.5."
        ]
    },
    # Q18
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q18",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "equation_derivation",
            "explanation"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_apply_mechanical_power",
        "accepted_answer": "A",
        "hints": [
            "Start with the definition of power as rate of doing work: power = (work done) / (time taken).",
            "Substitute work done = force × displacement and recall that (displacement) / (time taken) = velocity."
        ],
        "walkthrough": [
            "By definition, power = (work done) / (time taken). When a constant force acts on an object undergoing displacement in the direction of the force, work done = force × displacement.",
            "Substituting work done into the power equation yields: power = (force × displacement) / (time taken) = force × ((displacement) / (time taken)) = force × velocity (Option A).",
            "Option B uses distance rather than displacement, giving speed rather than velocity. Options C and D incorrectly define work done as force divided by displacement/distance."
        ]
    },
    # Q19
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q19",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "multi_step_calculation",
            "graph_interpretation"
        ],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m02",
        "skill_id": "9702_skill_apply_elastic_potential_energy",
        "accepted_answer": "A",
        "hints": [
            "The increase in strain energy is the area under the force-extension graph between extension 47 mm and 57 mm.",
            "Calculate the area of this trapezoidal region: ΔE = ((F₁ + F₂) / 2) × Δx, converting millimetres to metres."
        ],
        "walkthrough": [
            "The increase in strain energy equals the area under the force-extension curve from extension x₁ = 47 mm to x₂ = 57 mm.",
            "The extension increment is Δx = (57 - 47) mm = 10 mm = 0.010 m. The average force over this interval is F_avg = (19.3 × 10⁵ N + 23.3 × 10⁵ N) / 2 = 21.3 × 10⁵ N.",
            "The area of the trapezium is ΔW = F_avg × Δx = (21.3 × 10⁵ N) × (0.010 m) = 2.13 × 10⁴ J ≈ 21 kJ (Option A). Options B, C, and D arise from taking total strain energy or forgetting the 0.5 prefactor."
        ]
    },
    # Q20
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q20",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "property_identification",
            "classification"
        ],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m01",
        "skill_id": "9702_skill_define_young_modulus",
        "accepted_answer": "D",
        "hints": [
            "Recall the definitions of tensile stress (σ = F / A), tensile strain (ε = ΔL / L), and Young modulus (E = σ / ε).",
            "Determine the SI unit for force per unit area and note that a ratio of two lengths has no unit."
        ],
        "walkthrough": [
            "Stress is defined as force per unit cross-sectional area (N m⁻²), which is equivalent to the pascal (Pa).",
            "Strain is defined as change in length per unit original length (m / m), which is a dimensionless ratio and therefore has no unit.",
            "The Young modulus is stress divided by strain. Since strain is dimensionless, the Young modulus has the same unit as stress: the pascal (Pa). This corresponds to Row D. Rows A, B, and C incorrectly assign newtons to stress or metres to strain."
        ]
    },
    # Q21
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q21",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "explanation"
        ],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m02",
        "skill_id": "9702_skill_assess_elastic_deformation",
        "accepted_answer": "B",
        "hints": [
            "Work done on the rubber band during stretching is the total area under the loading curve OPQ down to the extension axis.",
            "Sum the labeled areas under OPQ: Area X (enclosed loop) + Area Y (under unloading curve QRO)."
        ],
        "walkthrough": [
            "The total work done on the band to stretch it to extension e is represented by the entire area under the loading curve OPQ down to the horizontal axis, which equals (Area X + Area Y). Hence, this is the minimum energy required to stretch the band to extension e (Statement B).",
            "During unloading along curve QRO, the energy released (work done by the band) is Area Y. The difference between work in and work out is the enclosed Area X, which represents the net thermal energy dissipated as heat over the complete cycle.",
            "Statement A is incorrect because Area X is dissipated over the complete stretch-relax cycle, not during stretching alone. Statement C is incorrect because elastic energy stored at e is Area X + Area Y. Statement D is incorrect because the net work done is Area X, not (Area Y - Area X)."
        ]
    },
    # Q22
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q22",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_apply_wave_speed",
        "accepted_answer": "C",
        "hints": [
            "Convert the period T = 1.0 ns to seconds (1.0 × 10⁻⁹ s) and calculate frequency f = 1 / T.",
            "Use the wave speed equation c = f λ with c = 3.0 × 10⁸ m s⁻¹ to solve for wavelength λ."
        ],
        "walkthrough": [
            "The period is T = 1.0 ns = 1.0 × 10⁻⁹ s. The frequency is f = 1 / T = 1 / (1.0 × 10⁻⁹ s) = 1.0 × 10⁹ Hz.",
            "All electromagnetic waves travel at the speed of light in free space, c = 3.0 × 10⁸ m s⁻¹. Using the wave equation c = f λ: λ = c / f = (3.0 × 10⁸ m s⁻¹) / (1.0 × 10⁹ Hz) = 0.30 m.",
            "Row C correctly identifies f = 1.0 × 10⁹ Hz and λ = 0.30 m. Rows A, B, and D use incorrect powers of ten for the prefix nano."
        ]
    },
    # Q23
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q23",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "property_identification",
            "classification"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m02",
        "skill_id": "9702_skill_define_longitudinal_wave",
        "accepted_answer": "B",
        "hints": [
            "Recall the distinction between progressive waves and stationary (standing) waves.",
            "Nodes and antinodes are characteristic features of stationary waves formed by superposition, not progressive waves."
        ],
        "walkthrough": [
            "Progressive longitudinal waves transfer energy through a medium via particle oscillations parallel to the direction of wave propagation.",
            "Nodes (positions of zero displacement amplitude) and antinodes (positions of maximum displacement amplitude) are fixed spatial features formed by the interference of counter-propagating waves in a stationary wave, not in a progressive wave.",
            "Therefore, statement B is incorrect (and the correct answer to the question). Statements A, C, and D are all accurate physical descriptions of progressive longitudinal waves."
        ]
    },
    # Q24
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q24",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "multi_step_calculation",
            "direct_calculation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_apply_wave_speed",
        "accepted_answer": "A",
        "hints": [
            "Determine the vibration frequency: 50 teeth hitting the strip per revolution, rotating 10 times per second.",
            "Use the wave speed equation v = f λ with v = 330 m s⁻¹ to find the emitted sound wavelength."
        ],
        "walkthrough": [
            "The metal strip is struck by 50 teeth in each complete revolution. Rotating 10 times each second produces a vibration frequency of f = 50 × 10 s⁻¹ = 500 Hz.",
            "Using the wave equation v = f λ with speed of sound v = 330 m s⁻¹: λ = v / f = (330 m s⁻¹) / (500 Hz) = 0.66 m (Option A).",
            "Option B (1.5 m) comes from taking 500 / 330. Option C (6.6 m) arises from forgetting the factor of 10 in frequency calculation (f = 50 Hz). Option D (500 m) confuses frequency with wavelength."
        ]
    },
    # Q25
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q25",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "multi_step_calculation",
            "direct_calculation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m03",
        "skill_id": "9702_skill_apply_doppler_effect",
        "accepted_answer": "D",
        "hints": [
            "Apply the Doppler formula for a moving source: f_o = f_s (v / (v ∓ v_s)), with minus for approaching source and plus for receding source.",
            "Calculate f_towards = 2000 × (340 / (340 - 30.0)) and f_away = 2000 × (340 / (340 + 30.0)), paying close attention to table column headers."
        ],
        "walkthrough": [
            "For a source moving towards a stationary observer at v_s = 30.0 m s⁻¹, the observed frequency is higher: f_towards = f_s (v / (v - v_s)) = 2000 Hz × (340 m s⁻¹ / (340 m s⁻¹ - 30.0 m s⁻¹)) = 2000 × (340 / 310) ≈ 2193.5 Hz ≈ 2190 Hz.",
            "For a source moving away from the observer, the observed frequency is lower: f_away = f_s (v / (v + v_s)) = 2000 Hz × (340 m s⁻¹ / (340 m s⁻¹ + 30.0 m s⁻¹)) = 2000 × (340 / 370) ≈ 1837.8 Hz ≈ 1840 Hz.",
            "In the table, Column 1 is frequency heard moving towards (2190 Hz) and Column 2 is frequency heard moving away (1840 Hz), which corresponds to Row D. Row B reverses the two column headings, while Rows A and C use incorrect Doppler approximations."
        ]
    },
    # Q26
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q26",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "property_identification",
            "classification"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m04",
        "skill_id": "9702_skill_identify_electromagnetic_spectrum_region",
        "accepted_answer": "B",
        "hints": [
            "Convert each frequency to wavelength using λ = c / f with c = 3.0 × 10⁸ m s⁻¹.",
            "Compare the resulting wavelengths with standard electromagnetic spectrum bands: microwave (1 mm to 1 m), infra-red (700 nm to 1 mm), visible (400 nm to 700 nm)."
        ],
        "walkthrough": [
            "Calculate the wavelengths in free space using λ = c / f: For P (f = 3 × 10¹⁰ Hz), λ = (3.0 × 10⁸) / (3 × 10¹⁰) = 1.0 × 10⁻² m = 1 cm (microwave region). For Q (f = 3 × 10¹³ Hz), λ = (3.0 × 10⁸) / (3 × 10¹³) = 1.0 × 10⁻⁵ m = 10 µm (infra-red region). For R (f = 6 × 10¹⁴ Hz), λ = (3.0 × 10⁸) / (6 × 10¹⁴) = 5.0 × 10⁻⁷ m = 500 nm (visible light region).",
            "Matching these values identifies P as microwave, Q as infra-red, and R as visible light (Row B).",
            "Rows A, C, and D misidentify the spectral regions by assigning incorrect frequency orders of magnitude."
        ]
    },
    # Q27
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q27",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "property_identification",
            "explanation"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m01",
        "skill_id": "9702_skill_determine_stationary_wave_phase_relationship",
        "accepted_answer": "D",
        "hints": [
            "In a stationary wave, what is the phase difference between particles located in adjacent inter-node segments separated by a single node?",
            "Consider the spatial symmetry of the amplitude envelope A(x) = A₀ |sin(kx)| when two points are separated by exactly Δx = λ / 2."
        ],
        "walkthrough": [
            "In a stationary wave, adjacent loops are separated by a node at intervals of λ / 2. Any two points separated by λ / 2 are in adjacent loops and therefore oscillate in anti-phase with a phase difference of 180° (π rad).",
            "The amplitude of oscillation varies with position according to A(x) = A₀ |sin(kx)|. Shifting position by half a wavelength gives A(x + λ/2) = A₀ |sin(kx + π)| = A₀ |-sin(kx)| = A₀ |sin(kx)| = A(x). Thus, the two particles have identical amplitudes.",
            "Therefore, the phase difference is 180° and the amplitude is the same (Row D). Rows A and B incorrectly suggest a 90° phase difference, while Row C incorrectly assumes differing amplitudes."
        ]
    },
    # Q28
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q28",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "multi_step_calculation",
            "direct_calculation"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m04",
        "skill_id": "9702_skill_apply_diffraction_grating",
        "accepted_answer": "B",
        "hints": [
            "Find the slit separation d using d = (1 mm) / 400.",
            "Use the diffraction grating formula d sin θ = n λ with sin θ ≤ 1 to find the highest integer order n_max, then count all orders N = 2 n_max + 1."
        ],
        "walkthrough": [
            "The line spacing of the grating is d = (1.0 × 10⁻³ m) / 400 = 2.50 × 10⁻⁶ m.",
            "Using d sin θ = n λ at the physical limit sin θ ≤ 1: n ≤ d / λ = (2.50 × 10⁻⁶ m) / (700 × 10⁻⁹ m) = 3.57. The highest observable integer diffraction order is n_max = 3.",
            "The total number of intensity maxima includes the central order (n = 0) and three orders on either side (n = 1, 2, 3): N_total = 2(3) + 1 = 7 (Option B). Option A (6) omits the central maximum, while Options C and D improperly round 3.57 up to 4."
        ]
    },
    # Q29
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q29",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "interference_analysis",
            "direct_calculation"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m03",
        "skill_id": "9702_skill_interference",
        "accepted_answer": "B",
        "hints": [
            "Relate phase difference Δϕ to path difference Δx: (Δϕ / 360°) = (Δx / λ).",
            "Substitute Δϕ = 90° and solve for path difference Δx."
        ],
        "walkthrough": [
            "For two sources emitting in phase, a full phase cycle of 360° (2π rad) corresponds to a path difference of one whole wavelength λ.",
            "The relationship between phase difference Δϕ and path difference Δx is Δx = (Δϕ / 360°) λ. For Δϕ = 90°: Δx = (90° / 360°) λ = λ / 4 (Option B).",
            "Option A (λ / 8) corresponds to a 45° phase difference. Option C (λ / 2) corresponds to 180° (anti-phase), and Option D (λ) corresponds to 360° (in phase)."
        ]
    },
    # Q30
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q30",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "electric_field_line_construction",
            "property_identification"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_construct_electric_field_lines",
        "accepted_answer": "C",
        "hints": [
            "Recall the definition of electric field direction: the direction of the force exerted on a positive test charge.",
            "Electric field lines point radially outwards from positive point charges and radially inwards towards negative point charges."
        ],
        "walkthrough": [
            "The direction of an electric field line represents the direction of the electric force on a positive test charge. Because like charges repel, a positive test charge placed near an isolated positive charge experiences a repulsive radial force directed away from the charge.",
            "Therefore, the electric field lines around an isolated positive point charge form radial straight lines directed outwards (Diagram C).",
            "Diagram D shows radial lines pointing inwards, which represents a negative point charge. Diagrams A and B show concentric circular lines, which is characteristic of magnetic fields around a current-carrying wire rather than electrostatic fields."
        ]
    },
    # Q31
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q31",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "multi_step_calculation",
            "equation_derivation"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_apply_uniform_electric_field",
        "accepted_answer": "C",
        "hints": [
            "Express the transverse acceleration of an electron in a uniform field between plates of separation d and potential difference V: a = (e E) / m = (e V) / (m d).",
            "The vertical deflection is x = 0.5 a t² where time t = L / v. How does x change when plate separation d is halved while V, L, v remain constant?"
        ],
        "walkthrough": [
            "The horizontal motion has constant velocity v, giving time inside the plates t = L / v. The vertical acceleration is a = F / m = (e E) / m = (e V) / (m d), where V is potential difference and d is plate separation.",
            "The vertical deflection at the exit is x = 0.5 a t² = 0.5 × ((e V) / (m d)) × (L / v)² = (e V L²) / (2 m v² d), showing that deflection x is inversely proportional to plate separation d (x ∝ 1/d).",
            "When the plate separation is halved (d' = d / 2) with V and v unchanged, the new deflection is x' = x / (1/2) = 2x (Option C). Options A, B, and D misidentify the inverse-linear scaling with separation."
        ]
    },
    # Q32
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q32",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m01",
        "skill_id": "9702_skill_apply_charge_quantisation",
        "accepted_answer": "A",
        "hints": [
            "Calculate total charge passing per second using Q = I t with I = 2.00 µA = 2.00 × 10⁻⁶ A and t = 1.0 s.",
            "Use charge quantisation Q = N e with elementary charge e = 1.60 × 10⁻¹⁹ C to find the number of electrons N."
        ],
        "walkthrough": [
            "In one second (t = 1.0 s), the charge passing through the component is Q = I t = (2.00 × 10⁻⁶ A)(1.0 s) = 2.00 × 10⁻⁶ C.",
            "Using Q = N e with elementary charge e = 1.60 × 10⁻¹⁹ C: N = Q / e = (2.00 × 10⁻⁶ C) / (1.60 × 10⁻¹⁹ C) = 1.25 × 10¹³ electrons per second (Option A).",
            "Option B (1.25 × 10¹⁶) corresponds to a current of 2.00 mA. Option C (1.25 × 10¹⁹) corresponds to 2.00 A. Option D (1.25 × 10²⁵) results from improperly adding positive exponents."
        ]
    },
    # Q33
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q33",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_calculate_electrical_power",
        "accepted_answer": "A",
        "hints": [
            "Calculate the operating hot resistance of the lamp from its rating (240 V, 100 W) using P = V² / R_hot.",
            "Since the filament resistance increases by a factor of 16 from room temperature, divide R_hot by 16 to find R_room."
        ],
        "walkthrough": [
            "The resistance of the lamp at its hot operating temperature is R_hot = V² / P = (240 V)² / (100 W) = 57600 / 100 = 576 Ω.",
            "Heating increases the filament resistance by a factor of 16 (R_hot = 16 × R_room). Thus, the cold resistance at room temperature is R_room = R_hot / 16 = 576 Ω / 16 = 36 Ω (Option A).",
            "Option B (580 Ω) is the operating resistance itself. Option D (9.2 kΩ) erroneously multiplies 576 Ω by 16 instead of dividing."
        ]
    },
    # Q34
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q34",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "multi_step_calculation",
            "direct_calculation"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m03",
        "skill_id": "9702_skill_apply_resistivity",
        "accepted_answer": "C",
        "hints": [
            "Write the formula for wire resistance in terms of resistivity, length, and diameter: R = (ρ L) / A = (4 ρ L) / (π d²).",
            "Since R and L are equal for both wires, (ρ_X / d_X²) = (ρ_Y / d_Y²), which gives d_Y = d_X √(ρ_Y / ρ_X)."
        ],
        "walkthrough": [
            "The resistance of a uniform wire is R = (ρ L) / A = (ρ L) / (π d² / 4) = (4 ρ L) / (π d²). For wires of identical resistance R and length L, the ratio ρ / d² is constant: (ρ_X / d_X²) = (ρ_Y / d_Y²).",
            "Rearranging for d_Y: d_Y = d_X √(ρ_Y / ρ_X) = 0.315 mm × √((5.6 × 10⁻⁸ Ω m) / (1.7 × 10⁻⁸ Ω m)) = 0.315 mm × √(3.294) = 0.315 × 1.815 ≈ 0.572 mm ≈ 0.57 mm (Option C).",
            "Option A (0.17 mm) comes from incorrectly dividing by the root ratio (0.315 / 1.815). Option B (0.33 mm) and Option D (1.0 mm) arise from neglecting the square root on the resistivity ratio."
        ]
    },
    # Q35
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q35",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "explanation",
            "property_identification"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_explain_emf_internal_resistance",
        "accepted_answer": "A",
        "hints": [
            "Recall the relationship for terminal potential difference: V = E - I r, where E is e.m.f. and r is internal resistance.",
            "When external resistance decreases, circuit current increases, so more energy per unit charge (I r) is dissipated within the internal resistance of the cell."
        ],
        "walkthrough": [
            "The terminal potential difference of a cell is V = E - I r, where E is constant e.m.f. and r is internal resistance. Decreasing the variable resistance R increases total circuit current I = E / (R + r).",
            "The term I r represents the lost volts—the work done per unit charge in driving charge through the internal resistance of the cell. As current increases, this internal energy loss per unit charge increases, leaving less potential difference across the external terminals (V decreases).",
            "This corresponds to Statement A. Statement B is incorrect because current increases. Statements C and D are incorrect because terminal p.d. decreases rather than increases."
        ]
    },
    # Q36
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q36",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "circuit_analysis",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_calculate_parallel_resistance",
        "accepted_answer": "B",
        "hints": [
            "Measuring between any two junctions divides the four resistors into two parallel branches whose resistances sum to 2 + 4 + 6 + 8 = 20 Ω.",
            "Calculate R_eq = (R₁ R₂) / (R₁ + R₂) = (R₁(20 - R₁)) / 20 for each of the four terminal pairs to find the greatest equivalent resistance."
        ],
        "walkthrough": [
            "The total loop resistance around the square is R_total = 2 + 4 + 6 + 8 = 20 Ω. For any pair of terminals, the circuit consists of two parallel branches of resistances R₁ and R₂ = 20 - R₁, with combined resistance R = (R₁ R₂) / 20.",
            "Evaluating each option: Between P and Q (Option A): R₁ = 2 Ω, R₂ = 18 Ω => R_PQ = (2 × 18) / 20 = 1.8 Ω. Between Q and S (Option B): R₁ = 2 + 8 = 10 Ω, R₂ = 4 + 6 = 10 Ω => R_QS = (10 × 10) / 20 = 5.0 Ω. Between R and S (Option C): R₁ = 6 Ω, R₂ = 14 Ω => R_RS = (6 × 14) / 20 = 4.2 Ω. Between S and P (Option D): R₁ = 8 Ω, R₂ = 12 Ω => R_SP = (8 × 12) / 20 = 4.8 Ω.",
            "The maximum parallel resistance occurs when the two branch resistances are equal (10 Ω and 10 Ω), giving 5.0 Ω between junctions Q and S (Option B)."
        ]
    },
    # Q37
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q37",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "circuit_analysis",
            "explanation"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m03",
        "skill_id": "9702_skill_calculate_series_circuit_potential_difference",
        "accepted_answer": "B",
        "hints": [
            "Voltmeter P measures the potential difference across the fixed resistor (V_P = I R). How does V_P change when current I decreases?",
            "Apply Kirchhoff's second law: the total circuit voltage is shared between the two resistors (E = V_P + V_Q). If V_P decreases, what must happen to V_Q?"
        ],
        "walkthrough": [
            "Voltmeter P is connected across a fixed resistor of constant resistance R, so V_P = I R. When the variable resistor is adjusted so that the ammeter reading I decreases, the potential difference V_P across the fixed resistor decreases.",
            "By Kirchhoff's second law, the total supply electromotive force is E = V_P + V_Q. As V_P decreases, the remaining potential difference across the variable resistor V_Q = E - V_P must increase.",
            "Therefore, the reading on voltmeter P decreases while the reading on voltmeter Q increases (Row B). Rows A, C, and D violate Ohm's law or Kirchhoff's loop rule."
        ]
    },
    # Q38
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q38",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "particle_model_application",
            "explanation"
        ],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m01",
        "skill_id": "9702_skill_infer_atomic_structure_from_alpha_scattering",
        "accepted_answer": "A",
        "hints": [
            "Consider what the large low-density hay bale and tiny dense cannon balls represent in atomic models.",
            "Most bullets pass through the empty hay undeflected, while a tiny fraction hitting the dense cannon balls rebound, mirroring Rutherford's alpha-particle scattering experiment."
        ],
        "walkthrough": [
            "In Rutherford's alpha-particle scattering experiment, alpha particles were fired at a gold foil. Most passed straight through with negligible deflection because atoms are mostly empty space, while a tiny fraction were deflected through large angles by the small, massive, dense nucleus.",
            "In this model, the bullets represent alpha particles, the large light hay bale represents the low-density outer atom/electron cloud, and the tiny, heavy iron cannon balls represent atomic nuclei.",
            "Therefore, the demonstration illustrates α-particle scattering (Option A). Option B (β⁻ decay) involves nucleon transmutation and neutrino emission, Option C (conservation of momentum) is a general mechanic law not specific to this structure, and Option D (double-slit interference) involves wave superposition."
        ]
    },
    # Q39
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q39",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "definition",
            "classification"
        ],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m01",
        "skill_id": "9702_skill_determine_nuclear_composition",
        "accepted_answer": "B",
        "hints": [
            "Recall the definition of isotopes: nuclides of the same element with the same proton number Z but different neutron numbers N.",
            "Identify which row has proton number Z = 92 and a neutron number different from 143."
        ],
        "walkthrough": [
            "Isotopes are nuclides of the same chemical element that contain identical numbers of protons (Z = 92 for uranium) but differing numbers of neutrons (N).",
            "Examining the table: Row A has Z = 91 (protactinium). Row B has Z = 92, N = 144, nucleon number A = 92 + 144 = 236, which is the isotope uranium-236. Row C has Z = 94 (plutonium). Row D has Z = 95 (americium).",
            "Nuclide B has proton number 92 and neutron number 144, making it an isotope of uranium-235 (Row B). Rows A, C, and D represent different chemical elements."
        ]
    },
    # Q40
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s17_12_q40",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "property_identification",
            "classification"
        ],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m02",
        "skill_id": "9702_skill_describe_beta_decay_quark_change",
        "accepted_answer": "A",
        "hints": [
            "In β⁻ decay, a neutron converts to a proton (n -> p + e⁻ + ν̅_e). Write out the quark compositions (n = udd, p = uud).",
            "Determine the single quark change (d -> u) and identify the neutral lepton emitted to conserve lepton number."
        ],
        "walkthrough": [
            "During β⁻ decay, a neutron decays into a proton, an electron (β⁻ particle), and an electron antineutrino: n -> p + e⁻ + ν̅_e.",
            "In terms of quark composition, a neutron (udd) transforms into a proton (uud), which involves a down quark changing into an up quark (d -> u, down to up).",
            "To conserve lepton number (L = 0 before decay, L = +1 for electron), an electron antineutrino (L = -1) is emitted. Thus, the change is down to up and the other particle is an antineutrino (Row A). Row B lists a neutrino (which is emitted in β⁺ decay), and Rows C and D show the reverse quark transition."
        ]
    }
]

out_dir = Path('subjects/physics/9702/enrichment/p1')
out_dir.mkdir(parents=True, exist_ok=True)

for item in enrichments:
    qid = item['question_id']
    fpath = out_dir / f"{qid}.enrichment.json"
    fpath.write_text(json.dumps(item, indent=2) + "\n", encoding='utf-8')
    print(f"Wrote {fpath.name}")

print(f"\nSuccessfully wrote {len(enrichments)} enrichment files.")
