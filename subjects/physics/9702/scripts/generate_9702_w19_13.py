import json
from pathlib import Path

enrichments = [
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q01",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "definition",
            "property_identification"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m02",
        "skill_id": "9702_skill_si_units_homogeneity",
        "accepted_answer": "C",
        "hints": [
            "Check the defining equations for each physical quantity: acceleration (a = Δv / Δt), current (I = ΔQ / Δt), potential difference (V = W / Q), and kinetic energy (Ek = 0.5 m v²).",
            "Express each unit in base SI units or standard derived units. Recall that potential difference is energy per unit charge, which gives units of joules per coulomb (J C⁻¹)."
        ],
        "walkthrough": [
            "Electric potential difference V across a component is defined as the work done (or energy transferred) per unit electric charge, V = W / Q. Therefore, the unit of potential difference can be written as joules per coulomb (J C⁻¹). A value of 8.0 J C⁻¹ represents a valid quantity and unit combination.",
            "Evaluating the other options: Acceleration is the rate of change of velocity, so its unit is m s⁻² rather than m s⁻¹ (which is velocity). Electric current has the SI base unit of ampere (A), not A s⁻¹. Kinetic energy is measured in joules (J) or newton metres (N m), not N m⁻¹ (which is the unit for spring constant or surface tension)."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q02",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "equation_derivation",
            "comparison"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m02",
        "skill_id": "9702_skill_si_units_homogeneity",
        "accepted_answer": "D",
        "hints": [
            "Express the derived unit in each pair in terms of SI base units (kg, m, s) using fundamental definitions such as F = ma, W = Fd, P = W/t, and p = F/A.",
            "Recall that 1 N = 1 kg m s⁻². Substitute this into the definition of pressure, Pa = N m⁻²."
        ],
        "walkthrough": [
            "Using Newton's second law, F = ma, one newton is 1 N = 1 kg m s⁻². Pressure is defined as force per unit area, p = F / A, so 1 Pa = 1 N m⁻² = (kg m s⁻²)(m⁻²) = kg m⁻¹ s⁻². This is not equivalent to kg m s⁻² (which is newtons, a unit of force).",
            "Checking the other pairs: In option A, N m = (kg m s⁻²)(m) = kg m² s⁻², which are equivalent units of work/energy. In option B, N s = (kg m s⁻²)(s) = kg m s⁻¹, which are equivalent units of impulse/momentum. In option C, J s⁻¹ = (kg m² s⁻²)(s⁻¹) = kg m² s⁻³, which are equivalent units of power."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q03",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "vector_diagram_construction",
            "property_identification"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m04",
        "skill_id": "9702_skill_scalars_vectors",
        "accepted_answer": "C",
        "hints": [
            "Recall the rules of vector addition: two perpendicular component vectors added head-to-tail must have a resultant vector that matches the magnitude and direction of vector R (pointing upwards and to the right).",
            "Look at each diagram to see if the vector sum of the two perpendicular components equals vector R."
        ],
        "walkthrough": [
            "Vector R is directed upwards and to the right. In resolving a vector into two perpendicular components, the vector sum of the components must equal R. In diagram C, one vector is pointing along the direction of R while the other points downwards and to the right; adding these two vectors head-to-tail produces a resultant vector that is longer than R and tilted downwards to the right, which does not equal R.",
            "In diagrams A, B, and D, the two perpendicular arrows form orthogonal components whose vector sum correctly yields vector R in both magnitude and direction."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q04",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "explanation",
            "classification"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m03",
        "skill_id": "9702_skill_errors_uncertainties",
        "accepted_answer": "B",
        "hints": [
            "Distinguish between systematic errors (constant shifts or zero errors in one direction) and random errors (unpredictable fluctuations in measurements).",
            "Consider which method directly corrects the flaw in the measurement instrument or experimental setup."
        ],
        "walkthrough": [
            "Systematic errors cause readings to deviate from the true value by a consistent amount or fraction each time (for example, zero errors or incorrect scale calibration). Careful calibration of measuring instruments against known standards identifies and removes these systematic shifts, directly reducing systematic errors.",
            "Averaging a large number of measurements (option A) and repeating measurements (option D) reduce the effect of random errors on the mean, but have no effect on systematic errors. Reducing sample size (option C) increases uncertainty and reduces reliability."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q05",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "uncertainty_analysis",
            "direct_calculation"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m03",
        "skill_id": "9702_skill_errors_uncertainties",
        "accepted_answer": "C",
        "hints": [
            "Recall the rule for combining percentage uncertainties for a formula of the form P = V² / R: add the percentage uncertainties multiplied by their respective powers.",
            "Here P = V² R⁻¹, so the percentage uncertainty in P is 2 × (% uncertainty in V) + 1 × (% uncertainty in R)."
        ],
        "walkthrough": [
            "The formula relating power, potential difference, and resistance is P = V² / R. When quantities are multiplied or divided, their fractional or percentage uncertainties add. For a quantity raised to a power n, its percentage uncertainty is multiplied by n.",
            "Calculating the overall percentage uncertainty: (ΔP / P) × 100% = 2 × ((ΔV / V) × 100%) + ((ΔR / R) × 100%) = 2(3%) + 2% = 6% + 2% = 8%.",
            "Option A (4%) comes from subtracting uncertainties or neglecting powers. Option B (7%) comes from omitting the factor of 2 on V or arithmetic errors. Option D (11%) comes from incorrectly squaring the percentage uncertainties."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q06",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_kinematics_equations",
        "accepted_answer": "B",
        "hints": [
            "Use the equation of motion s = ut + 0.5 a t². Since the sphere is released from rest, u = 0, so displacement s is directly proportional to t².",
            "Find the ratio of the times (20 s / 4.0 s) and square it to determine the scaling factor for distance."
        ],
        "walkthrough": [
            "For motion from rest under constant acceleration in a vacuum: s = 0.5 a t², meaning displacement s is proportional to t².",
            "Taking the ratio of displacements at t₂ = 20 s and t₁ = 4.0 s: (s₂ / s₁) = (t₂ / t₁)² = (20 / 4.0)² = 5² = 25.",
            "Therefore, s₂ = 25 × s₁ = 25 × 3.0 m = 75 m.",
            "Option A (15 m) incorrectly assumes distance is linearly proportional to time (5 × 3.0 m). Option C (80 m) and Option D (2000 m) result from miscalculating the acceleration or applying incorrect kinematic formulas."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q07",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "force_diagram_construction",
            "explanation"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_newtons_laws",
        "accepted_answer": "A",
        "hints": [
            "According to Newton's third law, if body A exerts a force on body B, body B exerts an equal and opposite force of the same type on body A.",
            "Identify the two interacting bodies for the weight of the box: the Earth exerts a gravitational force downwards on the box, so the third-law pair force is the gravitational force exerted by the box upwards on the Earth."
        ],
        "walkthrough": [
            "The weight W of the box is the gravitational attraction exerted by the Earth on the box, acting downwards towards the centre of the Earth. By Newton's third law, the pair force must be of the same type (gravitational), equal in magnitude, opposite in direction, and act on the other body (the Earth).",
            "Therefore, the paired force is the gravitational pull of the box on the Earth, which acts vertically upwards at the centre of the Earth, represented by arrow A.",
            "Arrow B represents the normal contact force exerted by the Earth's surface on the box (which balances W for equilibrium, but is a contact force on the same body, not a Newton's third law pair). Arrow C points downwards inside the Earth, and Arrow D is a horizontal friction/contact force."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q08",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "explanation",
            "property_identification"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m02",
        "skill_id": "9702_skill_drag_terminal_velocity",
        "accepted_answer": "D",
        "hints": [
            "Recall Newton's first law of motion: an object experiences zero acceleration when the resultant force acting on it is zero.",
            "Consider what happens to an object's motion when it is already moving downwards and the resultant force becomes zero."
        ],
        "walkthrough": [
            "When the upwards air resistance becomes equal in magnitude to the downwards weight of the snowflake, the resultant force acting on the snowflake is zero (F_net = W - D = 0). By Newton's first and second laws (F_net = ma), zero resultant force means zero acceleration.",
            "Since the snowflake is already falling, zero acceleration means it continues falling at a constant velocity (its terminal velocity).",
            "Option A and Option B are incorrect because acceleration and deceleration require a non-zero resultant force. Option C is incorrect because zero resultant force maintains existing motion rather than stopping a moving object."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q09",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "property_identification"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m03",
        "skill_id": "9702_skill_relative_speed_elastic_collision",
        "accepted_answer": "B",
        "hints": [
            "In a perfectly elastic collision, the relative speed of approach before the collision equals the relative speed of separation after the collision.",
            "Calculate the relative speed of approach from the initial velocities: u_X - u_Y = 20 m s⁻¹ - 12 m s⁻¹ = 8.0 m s⁻¹, and equate it to v_Y - v_X = v - 10 m s⁻¹."
        ],
        "walkthrough": [
            "For any perfectly elastic collision between two bodies, the relative speed of approach is equal to the relative speed of separation: u_X - u_Y = v_Y - v_X.",
            "Before collision, both objects travel to the right: u_X = 20 m s⁻¹ and u_Y = 12 m s⁻¹, giving a relative speed of approach of 20 - 12 = 8.0 m s⁻¹.",
            "After collision, object X moves to the right at v_X = 10 m s⁻¹ and object Y moves to the right at speed v. The relative speed of separation is v - 10.",
            "Setting relative speed of separation equal to relative speed of approach: v - 10 = 8.0, which gives v = 18 m s⁻¹.",
            "Option A (2.0 m s⁻¹) comes from subtracting the approach speed from 10. Option C (22 m s⁻¹) and Option D (24 m s⁻¹) result from incorrectly using the wrong velocity values or assuming equal masses without conservation of kinetic energy."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q10",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "explanation",
            "classification"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m03",
        "skill_id": "9702_skill_upthrust_archimedes",
        "accepted_answer": "B",
        "hints": [
            "Use Archimedes' principle: upthrust is equal to the weight of fluid displaced (U = ρ_water V g). Consider whether the volume of fluid displaced changes while the sphere remains fully submerged.",
            "As the sphere rises and gains speed, consider how the drag force (water resistance) changes and how that affects the resultant vertical force (F_net = U - W - F_drag)."
        ],
        "walkthrough": [
            "By Archimedes' principle, upthrust U = ρ V g, where ρ is the uniform density of water and V is the volume of the sphere. As the sphere rises while remaining fully submerged beneath the surface, the displaced volume and water density remain constant, so the upthrust on the sphere is constant.",
            "Immediately after release, the sphere accelerates upwards and its speed increases. As speed increases, the downward resistive drag force F_drag increases. The resultant upward force is F_net = U - W - F_drag. Since U and W are constant and F_drag increases, the resultant force on the sphere is decreasing.",
            "Rows A, C, and D are incorrect because upthrust does not vary with depth in an incompressible fluid of uniform density, and the resultant force decreases due to increasing resistive drag."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q11",
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
            "For a set of parallel forces, find the net resultant force by vector addition of the forces, and find the resultant torque by taking moments about a convenient point or resolving into a couple and a single force.",
            "In system X, the forces are 20 N to the right and 40 N to the left separated by 0.50 m. The resultant horizontal force is 40 - 20 = 20 N to the left."
        ],
        "walkthrough": [
            "For system X: The forces are 20 N to the right (top) and 40 N to the left (bottom) separated by d = 50 cm = 0.50 m. The net force is 40 N - 20 N = 20 N directed to the left. Resolving the forces into a couple and a single force: a couple of magnitude 20 N with separation 0.50 m gives a clockwise torque of 20 N × 0.50 m = 10 N m, with a remaining force of 20 N to the left.",
            "For system Y: The forces are 40 N to the left (top) and 20 N to the right (bottom). The net force is 40 N - 20 N = 20 N to the left, and taking moments gives an anticlockwise torque of 10 N m plus a force to the left. Hence statements C and D (which claim 30 N m) and statement B (which claims torque only with no net force) are incorrect."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q12",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "force_diagram_construction",
            "vector_diagram_construction"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m02",
        "skill_id": "9702_skill_equilibrium_coplanar_forces",
        "accepted_answer": "A",
        "hints": [
            "Identify the three forces acting on the heavy ball: weight acting vertically downwards, tension in the cable pulling upwards and rightwards along the cable, and tension in the chain pulling downwards and leftwards along the chain.",
            "For a system in equilibrium, the three coplanar force vectors must form a closed triangle when connected head-to-tail, with the right angle between the perpendicular cable and chain tensions."
        ],
        "walkthrough": [
            "The three forces acting on the ball are: (1) weight acting vertically downwards, (2) tension in the cable acting upwards and to the right, and (3) tension in the chain acting downwards and to the left perpendicular to the cable.",
            "For translational equilibrium, ΣF = 0, meaning the three vectors must form a closed triangle with arrows following head-to-tail in a single continuous loop.",
            "In diagram A, the weight arrow points downwards, the chain tension points downwards and to the left perpendicular to the cable, and the cable tension points upwards and to the right back to the start, forming a closed right-angled triangle with arrows in head-to-tail order.",
            "In diagram B, the cable tension arrow is reversed. In diagrams C and D, the right angle is incorrectly placed between the weight and chain tension rather than between the cable and chain."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q13",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m03",
        "skill_id": "9702_skill_density_pressure",
        "accepted_answer": "B",
        "hints": [
            "The pressure at sea level is equal to the total weight per unit cross-sectional area of the atmosphere: p = ρ_avg g h.",
            "Since density decreases linearly from ρ₀ = 1.3 kg m⁻³ at sea level to 0 at the top of the atmosphere, the average density of air is ρ_avg = (1.3 + 0) / 2 = 0.65 kg m⁻³."
        ],
        "walkthrough": [
            "Atmospheric pressure at sea level is produced by the weight of the column of air above it: p = ρ_avg g h, where ρ_avg is the mean density of the air and h is the height of the atmosphere.",
            "Given that the density decreases linearly from ρ₀ = 1.3 kg m⁻³ at h = 0 to 0 at height h, the average density is ρ_avg = (1.3 + 0) / 2 = 0.65 kg m⁻³.",
            "Rearranging for height: h = p / (ρ_avg g) = (100 × 10³ Pa) / (0.65 kg m⁻³ × 9.81 m s⁻²) = 100000 / 6.3765 ≈ 1.57 × 10⁴ m ≈ 16 km.",
            "Option A (7.8 km) uses the full sea-level density 1.3 kg m⁻³ instead of the average density. Option C (77 km) and Option D (150 km) result from unit conversion errors or missing factors."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q14",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "equation_derivation",
            "property_identification"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_power_efficiency",
        "accepted_answer": "A",
        "hints": [
            "Recall the definition of efficiency: efficiency = (useful energy output) / (total energy input).",
            "Find the total useful energy output in one day using power P and time S, and the total energy input from coal in one day using N, M, and E."
        ],
        "walkthrough": [
            "The useful energy output generated by the power station in one day is E_out = P × S, where P is the average power output in watts and S is the number of seconds in one day.",
            "The total mass of coal supplied per day is N × M (where N is the number of trains and M is the mass per train). Since each kilogram of coal provides energy E, the total thermal energy input per day is E_in = N × M × E.",
            "Efficiency is the ratio of useful output energy to total input energy: Efficiency = E_out / E_in = (P S) / (N M E).",
            "Options B, C, and D arrange the variables in dimensional combinations that do not represent the dimensionless ratio of output energy to input energy."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q15",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_work_done",
        "accepted_answer": "A",
        "hints": [
            "Use the formula for work done by a gas or piston against constant pressure: W = p ΔV, where ΔV = A × d.",
            "Ensure all quantities are converted to standard SI units: A = 500 cm² = 500 × 10⁻⁴ m² = 0.050 m² and d = 30 cm = 0.30 m."
        ],
        "walkthrough": [
            "The change in volume of the gas as the piston moves is ΔV = A × d = (500 × 10⁻⁴ m²) × (30 × 10⁻² m) = 0.050 m² × 0.30 m = 0.015 m³.",
            "The work done against constant pressure is W = p ΔV = 4000 Pa × 0.015 m³ = 60 J.",
            "Options B (6.0 × 10³ J), C (6.0 × 10⁵ J), and D (6.0 × 10⁷ J) arise from failing to convert centimetres and square centimetres to metres and square metres."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q16",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "property_identification"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m02",
        "skill_id": "9702_skill_kinetic_potential_energy",
        "accepted_answer": "B",
        "hints": [
            "Note that the ball is falling at constant speed: what does a constant speed imply about kinetic energy Ek = 0.5 m v² over time?",
            "Determine how height h varies with time at constant speed v (h = h₀ - vt), and substitute this into gravitational potential energy Ep = mgh."
        ],
        "walkthrough": [
            "Since the steel ball falls at a constant speed v, its kinetic energy Ek = 0.5 m v² is constant over time, which corresponds to a horizontal straight line.",
            "At constant downward velocity v, the height of the ball above the reference level decreases linearly with time: h(t) = h₀ - vt. Therefore, gravitational potential energy Ep(t) = mgh(t) = mgh₀ - mgvt, which is a straight line with a constant negative gradient.",
            "Graph B correctly shows a horizontal line for Ek and a straight line decreasing to zero for Ep.",
            "Graph A incorrectly shows Ep curving downwards (which would indicate accelerating motion). Graphs C and D incorrectly show Ek increasing from zero, which contradicts falling at constant terminal speed."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q17",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "equation_derivation",
            "direct_calculation"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_power_efficiency",
        "accepted_answer": "A",
        "hints": [
            "Recall the relationship between power, force, and velocity for an object travelling at speed v: P = F v.",
            "At maximum speed, the driving force equals the total resistive force F_resistive = k v²."
        ],
        "walkthrough": [
            "Mechanical power is related to force and velocity by P = F v.",
            "When the car reaches its maximum speed on a horizontal road, acceleration is zero, so the forward driving force F equals the total resistive force: F = k v².",
            "Substituting into the power equation: P = (k v²) v = k v³. Rearranging gives v³ = P / k.",
            "Option B (v² = P/k) neglects the velocity factor in P = Fv. Options C and D introduce incorrect powers or square root relations."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q18",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m02",
        "skill_id": "9702_skill_kinetic_potential_energy",
        "accepted_answer": "B",
        "hints": [
            "Calculate the work done in lifting each block to its new position in the vertical stack: work done on each block is mg Δh, where Δh is the vertical height through which that block is lifted.",
            "Alternatively, calculate the increase in gravitational potential energy of the entire system by tracking the change in height of the centre of gravity of the four blocks."
        ],
        "walkthrough": [
            "Initially, all 4 blocks lie on the table. In forming the stack: the bottom block (block 1) remains on the table (height change Δh₁ = 0). Block 2 is lifted by height h (work = mgh). Block 3 is lifted by height 2h (work = 2mgh). Block 4 is lifted by height 3h (work = 3mgh).",
            "The total work done on the blocks is W = 0 + mgh + 2mgh + 3mgh = 6 mgh.",
            "Alternatively, the initial height of the centre of mass of each block is h / 2. The final stack of 4 blocks has total thickness 4h and its centre of mass is at 4h / 2 = 2h. The vertical shift in centre of mass is Δh_cm = 2h - 0.5h = 1.5h. Total work done is ΔEp = (4m) g (1.5h) = 6 mgh.",
            "Option A (3 mgh) accounts only for the top block. Option C (8 mgh) and Option D (10 mgh) incorrectly calculate the individual heights or multiply total mass by the total stack height."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q19",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "direct_calculation"
        ],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m01",
        "skill_id": "9702_skill_young_modulus",
        "accepted_answer": "D",
        "hints": [
            "Recall the definition of Young modulus E: E = stress / strain in the linear (elastic) region of the graph.",
            "Read the values from the linear section of the graph: at stress = 2.1 × 10⁸ Pa, the strain is 1.4 × 10⁻³."
        ],
        "walkthrough": [
            "The Young modulus E of a material is defined as the ratio of tensile stress to tensile strain within Hooke's law limit (the linear region of the stress–strain graph): E = σ / ε.",
            "From the graph, the linear region extends up to stress σ = 2.1 × 10⁸ Pa and strain ε = 1.4 × 10⁻³.",
            "Calculating E: E = (2.1 × 10⁸ Pa) / (1.4 × 10⁻³) = 1.5 × 10¹¹ Pa.",
            "Option A (6.7 × 10⁻¹² Pa) and Option B (6.7 × 10⁻⁹ Pa) compute strain over stress with power-of-ten errors. Option C (1.5 × 10⁸ Pa) omits the 10⁻³ factor in the strain denominator."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q20",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "property_identification"
        ],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m02",
        "skill_id": "9702_skill_elastic_plastic_behaviour",
        "accepted_answer": "C",
        "hints": [
            "Recall the definition of elastic behaviour: a material is elastic if it returns to its original length (zero extension) when the deforming force is removed.",
            "Check the point on the extension axis where the unloading curve ends when the force reaches zero."
        ],
        "walkthrough": [
            "An object exhibits elastic behaviour if it returns completely to its original dimensions when the deforming force is reduced to zero. On the graph, the unloading curve returns to (0,0) when force = 0, showing that there is no permanent plastic deformation and the rubber band remains elastic over this range.",
            "Option A is incorrect because the curve clearly returns to zero extension. Option B is incorrect because Hooke's law requires force to be directly proportional to extension (a straight line through the origin), whereas rubber displays non-linear behaviour. Option D is incorrect because the shaded area inside the hysteresis loop represents thermal energy dissipated during the cycle, while the total work done in extending is the area under the loading curve."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q21",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "comparison",
            "property_identification"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m02",
        "skill_id": "9702_skill_progressive_wave_properties",
        "accepted_answer": "C",
        "hints": [
            "Consider the wave phenomena exhibited by all types of waves: reflection, refraction, diffraction, and interference.",
            "Remember that diffraction is a fundamental property of all waves (both transverse electromagnetic waves and longitudinal sound waves) when passing through an aperture or around an obstacle."
        ],
        "walkthrough": [
            "Diffraction is the spreading of waves as they pass through a gap or around an obstacle, and it is a universal property of all waves including light waves and sound waves. Therefore, the statement 'Light waves can be diffracted but sound waves cannot' is not correct.",
            "The other statements are factually correct: Option A is true because both light (astronomical redshift) and sound (pitch changes) exhibit the Doppler effect. Option B is true because light is an electromagnetic transverse wave and sound is a mechanical longitudinal wave. Option D is true because electromagnetic waves do not require a medium to propagate, whereas sound waves require a material medium."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q22",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "direct_calculation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m02",
        "skill_id": "9702_skill_progressive_wave_properties",
        "accepted_answer": "B",
        "hints": [
            "Identify the nature of sound waves in air (longitudinal or transverse) and determine the period T from the displacement–time graph.",
            "One complete wave oscillation occurs from t = 0 to t = 20 ms. Use f = 1 / T to calculate the frequency."
        ],
        "walkthrough": [
            "Sound waves propagating through air are longitudinal mechanical waves consisting of compressions and rarefactions.",
            "From the displacement–time graph, one complete oscillation takes a time period T = 20 ms = 20 × 10⁻³ s = 0.020 s.",
            "The frequency f of the wave is f = 1 / T = 1 / (0.020 s) = 50 Hz.",
            "Option A is incorrect because the period is 20 ms, not 25 ms. Options C and D are incorrect because sound waves are longitudinal, not transverse, and time on the horizontal axis represents period rather than wavelength."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q23",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "direct_calculation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_oscilloscope_traces",
        "accepted_answer": "B",
        "hints": [
            "Calculate the time period T of the wave using the frequency f = 5.0 kHz = 5000 Hz: T = 1 / f.",
            "Count how many horizontal centimetres (grid divisions) represent one full cycle on the CRO screen, then divide T by this horizontal distance to find the time-base setting."
        ],
        "walkthrough": [
            "The time period of the wave is T = 1 / f = 1 / (5.0 × 10³ Hz) = 2.0 × 10⁻⁴ s = 200 μs.",
            "From the CRO screen display, one full cycle (from one peak to the next adjacent peak) spans exactly 2 horizontal grid divisions (2 cm).",
            "The time-base setting is the time represented per centimetre: Time-base = T / (2 cm) = (200 μs) / (2 cm) = 100 μs cm⁻¹.",
            "Option A (10 μs cm⁻¹) is too small by a factor of 10. Options C (10 ms cm⁻¹) and D (100 ms cm⁻¹) confuse milliseconds with microseconds."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q24",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "equation_recall",
            "direct_calculation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m03",
        "skill_id": "9702_skill_doppler_effect",
        "accepted_answer": "B",
        "hints": [
            "Recall the Doppler effect formula for a moving source approaching a stationary observer: f_o = f_s (v / (v - v_s)).",
            "Identify the variables: source frequency f_s = 1000 Hz, wave speed v = 330 m s⁻¹, source speed v_s = 20 m s⁻¹."
        ],
        "walkthrough": [
            "When a sound source moves towards a stationary observer, the observed frequency f_o is higher than the emitted frequency f_s due to wavefront compression in the direction of motion.",
            "The Doppler formula for a source moving towards a stationary observer is f_o = f_s (v / (v - v_s)).",
            "Substituting the given values: f_s = 1000 Hz, v = 330 m s⁻¹, and v_s = 20 m s⁻¹ gives f_o = 1000 × (330 / (330 - 20)).",
            "Option A uses (330 + 20) in the denominator, which applies to a receding source. Options C and D place (330 ± 20) in the numerator, which corresponds to an observer moving rather than a moving source."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q25",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "equation_derivation",
            "property_identification"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_wave_intensity_amplitude",
        "accepted_answer": "A",
        "hints": [
            "Combine the relationship between intensity and distance from a point source (I proportional to 1 / r²) with the relationship between intensity and wave amplitude (I proportional to a²).",
            "Equate the proportionalities: a² proportional to I proportional to 1 / r², and take the square root of both sides."
        ],
        "walkthrough": [
            "The intensity I of sound at distance r from a point source of constant power P is given by I = P / (4π r²), so I is proportional to 1 / r².",
            "The intensity of a mechanical wave is also directly proportional to the square of its amplitude a, so I is proportional to a².",
            "Equating these two relationships gives a² proportional to 1 / r². Taking the square root of both sides yields a is proportional to 1 / r.",
            "Option B (a proportional to 1 / r²) confuses amplitude with intensity. Options C (a proportional to r) and D (a proportional to r²) incorrectly suggest amplitude increases with distance."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q26",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "property_identification"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m01",
        "skill_id": "9702_skill_stationary_waves",
        "accepted_answer": "C",
        "hints": [
            "In a stationary wave of wavelength λ = 4 cm, find the distance between adjacent antinodes (maxima) and between an antinode and an adjacent node (minimum).",
            "Distance between adjacent antinodes is λ / 2 = 2 cm, and distance from an antinode to a node is λ / 4 = 1 cm. Since d = 0 is an antinode, maxima occur at even distances (0, 2, 4, ... cm) and minima occur at odd distances (1, 3, 5, ... cm)."
        ],
        "walkthrough": [
            "In a stationary wave pattern with wavelength λ = 4 cm: antinodes (signal maxima) occur at intervals of λ / 2 = 2 cm, and nodes (signal minima) occur midway between antinodes at intervals of λ / 4 = 1 cm from an antinode.",
            "Given that the left-hand transmitter at d = 0 is an antinode: maxima occur at d = 0, 2, 4, ..., 46, 48 cm (even values of d), and minima occur at d = 1, 3, 5, ..., 47, 49 cm (odd values of d).",
            "In row C, d = 48 cm is an even integer (maximum) and d = 47 cm is an odd integer (minimum), which correctly matches the stationary wave positions.",
            "Rows A and B place minima or maxima at incorrect even/odd locations. Row D has a maximum at 49 cm, which is a node (minimum)."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q27",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "graph_interpretation",
            "property_identification"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_progressive_wave_properties",
        "accepted_answer": "A",
        "hints": [
            "Check the axes: the vertical axis is height (displacement) and the horizontal axis is time t.",
            "Determine what p represents (height from mean level at a general instant, not peak) and what q represents (time for one complete oscillation)."
        ],
        "walkthrough": [
            "On a displacement–time graph: p is the vertical distance from the equilibrium (mean) position to the position of the wave at a particular instant, which is defined as displacement (amplitude would be the maximum displacement from equilibrium to crest).",
            "Quantity q is the horizontal duration between two identical points in consecutive cycles (from one downward zero-crossing to the next downward zero-crossing), which represents the time period T of the wave.",
            "Therefore, p is displacement and q is period, matching row A.",
            "Rows B and D incorrectly identify q as wavelength (which would require a displacement–distance graph). Rows C and D incorrectly identify p as amplitude."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q28",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "property_identification",
            "direct_calculation"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m01",
        "skill_id": "9702_skill_stationary_waves",
        "accepted_answer": "D",
        "hints": [
            "Recognize the sketch showing an envelope of loops with fixed nodes and antinodes: this represents a stationary wave.",
            "Count the number of loops (half-wavelengths λ / 2) within the given distance of 1.0 m."
        ],
        "walkthrough": [
            "The diagram shows a stationary wave envelope formed by loops oscillating perpendicularly to the length of the string, which represents a transverse stationary wave.",
            "Between the dotted lines spanning a distance of 1.0 m, there are exactly 5 loops (half-wavelengths). Therefore: 5 × (λ / 2) = 1.0 m, which gives 2.5 λ = 1.0 m and λ = 1.0 / 2.5 = 0.40 m = 40 cm.",
            "Thus, the wave is transverse, stationary, and has a wavelength of 40 cm.",
            "Option A incorrectly identifies the wave as longitudinal with λ = 20 cm. Option B uses λ = 20 cm (the length of a single loop, which is λ / 2). Option C incorrectly describes the wave as progressive."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q29",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "interference_analysis",
            "property_identification"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m03",
        "skill_id": "9702_skill_two_source_interference",
        "accepted_answer": "C",
        "hints": [
            "The curved lines represent wavefronts (crests). Constructive interference (maxima) occurs where two crests intersect.",
            "Complete destructive interference (minima) occurs where a crest from one source meets a trough from the other source (i.e. where a curved wavefront line meets the space midway between adjacent wavefronts of the other source)."
        ],
        "walkthrough": [
            "In a wavefront representation of two-source interference, the solid arcs represent wave crests separated by one wavelength λ. Constructive interference (maxima) occurs at points where two wavefront lines intersect (crest meets crest, path difference = n λ).",
            "Destructive interference (minima) occurs where a crest from one slit meets a trough from the other slit (path difference = (n + 0.5) λ), which corresponds to a point located on a wavefront from one slit and midway between wavefronts from the other slit.",
            "Examining point C: it lies on a wavefront from the upper slit and halfway between two consecutive wavefronts from the lower slit, giving a path difference of 0.5 λ, which results in complete destructive interference.",
            "Points B and D lie on intersections of wavefronts along the central axis (path difference = 0, central maximum). Point A is near the slits and not at a position of complete destructive interference."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q30",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m04",
        "skill_id": "9702_skill_diffraction_grating",
        "accepted_answer": "C",
        "hints": [
            "Use the diffraction grating equation: d sin θ = n λ, where d = 1 mm / 400 = 2.5 × 10⁻⁶ m.",
            "Calculate the angle θ₂ for the second-order maximum (n = 2) and θ₃ for the third-order maximum (n = 3), then find their difference Δθ = θ₃ - θ₂."
        ],
        "walkthrough": [
            "The grating spacing is d = (1.0 × 10⁻³ m) / 400 = 2.5 × 10⁻⁶ m.",
            "For the second-order maximum (n = 2): sin θ₂ = (2 × (567 × 10⁻⁹ m)) / (2.5 × 10⁻⁶ m) = 0.4536, which gives θ₂ = arcsin(0.4536) ≈ 26.97°.",
            "For the third-order maximum (n = 3): sin θ₃ = (3 × (567 × 10⁻⁹ m)) / (2.5 × 10⁻⁶ m) = 0.6804, which gives θ₃ = arcsin(0.6804) ≈ 42.87°.",
            "The angle between the second-order and third-order maxima is Δθ = 42.87° - 26.97° = 15.9°.",
            "Option A (13.1°) is the first-order angle θ₁. Option B (13.9°) is the angle between first and second orders (θ₂ - θ₁). Option D (27.0°) is the second-order angle θ₂."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q31",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "electric_field_line_construction",
            "property_identification"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_uniform_electric_fields",
        "accepted_answer": "D",
        "hints": [
            "Recall the convention for electric field lines: field lines point away from positive charges and towards negative charges.",
            "The density and total number of field lines connected to a charge are proportional to the magnitude of the charge."
        ],
        "walkthrough": [
            "Electric field lines originate on positive charges and terminate on negative charges. In the diagram, field lines point outward from charge P and inward toward charge Q, so P is positively charged and Q is negatively charged.",
            "The density of electric field lines around P is substantially higher than around Q, and many field lines from P extend away to infinity rather than terminating on Q. Because the number of field lines is proportional to charge magnitude, the magnitude of charge on P is greater than that on Q.",
            "Therefore, P is positively charged and has a greater charge than Q.",
            "Options A and B incorrectly identify P as negatively charged. Option C incorrectly concludes that P has a smaller charge than Q."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q32",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "property_identification",
            "explanation"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_uniform_electric_fields",
        "accepted_answer": "D",
        "hints": [
            "Recall that parallel, equally spaced field lines represent a uniform electric field where field strength E is constant everywhere.",
            "Consider the force on a charge F = qE and the work done when a force acts over a displacement: W = F d = q E d."
        ],
        "walkthrough": [
            "In a uniform electric field, the electric field strength E is constant in magnitude and direction. A charged particle of charge q experiences a constant electrostatic force F = q E.",
            "As the particle moves from P to Q over a displacement in the direction of the field, the electric force does work on the particle given by W = F Δx = q E Δx > 0. By the work–energy theorem, this work increases the kinetic energy of the particle.",
            "Option A is incorrect because constant force produces constant acceleration (a = F / m). Option B is incorrect because work is done, so kinetic energy changes between P and Q. Option C is incorrect because the field strength and hence electrostatic force are identical at P and Q."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q33",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m01",
        "skill_id": "9702_skill_electric_current_drift_speed",
        "accepted_answer": "C",
        "hints": [
            "Use Ohm's law I = V / R to calculate the current in the conductor, where R = 5.6 kΩ = 5600 Ω and V = 9.0 V.",
            "Find the total charge Q = I × t flowing in one minute (t = 60 s), and divide by the elementary charge e = 1.60 × 10⁻¹⁹ C to find the number of electrons N = Q / e."
        ],
        "walkthrough": [
            "The electric current through the conductor is I = V / R = (9.0 V) / (5.6 × 10³ Ω) ≈ 1.607 × 10⁻³ A.",
            "The total charge passing a point in t = 1 minute = 60 s is Q = I × t = (1.607 × 10⁻³ A) × 60 s ≈ 0.09643 C.",
            "The number of electrons is N = Q / e = (0.09643 C) / (1.60 × 10⁻¹⁹ C) ≈ 6.03 × 10¹⁷ ≈ 6.0 × 10¹⁷.",
            "Option A (6.0 × 10²⁰) and Option B (1.0 × 10¹⁹) arise from power-of-ten errors in resistance or charge. Option D (1.0 × 10¹⁶) uses t = 1 s instead of 60 s."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q34",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "circuit_analysis",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_resistor_networks",
        "accepted_answer": "C",
        "hints": [
            "Calculate the equivalent resistance of the circuit: two 6.0 Ω resistors in parallel are in series with resistor R (6.0 Ω).",
            "Find the total circuit current using I = E / R_total, and then calculate the power dissipated in R using P = I² R."
        ],
        "walkthrough": [
            "The parallel pair of 6.0 Ω resistors has an equivalent resistance of R_p = (6.0 × 6.0) / (6.0 + 6.0) = 3.0 Ω.",
            "The total circuit resistance is R_total = R_p + R = 3.0 Ω + 6.0 Ω = 9.0 Ω.",
            "The total current leaving the 12 V battery (which passes entirely through resistor R) is I = (12 V) / (9.0 Ω) = 4 / 3 A ≈ 1.333 A.",
            "The power dissipated in resistor R is P = I² R = (4 / 3 A)² × 6.0 Ω = (16 / 9) × 6.0 = 32 / 3 W ≈ 10.7 W ≈ 11 W.",
            "Option A (2.7 W) is the power in one of the parallel resistors ((2 / 3)² × 6 = 2.67 W). Option B (6.0 W) assumes equal voltage split across all resistors. Option D (24 W) assumes the full 12 V drops across R."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q35",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "property_identification"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m03",
        "skill_id": "9702_skill_iv_characteristics",
        "accepted_answer": "D",
        "hints": [
            "Analyze the I–V characteristic: current is zero for all negative voltages (V < 0), which indicates a diode component.",
            "For positive voltages (V > 0), the curve conducts but bends toward the voltage axis (gradient I / V decreases), which is characteristic of a filament lamp whose resistance increases with current."
        ],
        "walkthrough": [
            "The I–V graph displays two distinct features: (1) zero conduction for reverse voltages (V < 0), which requires a semiconductor diode, and (2) non-linear conduction for forward voltages (V > 0) with a decreasing gradient, which corresponds to the characteristic of a filament lamp as its filament heats up and resistance increases.",
            "To ensure that no current flows in the reverse direction through either component, the diode must be connected in series with the filament lamp so that the reverse-biased diode blocks all current through the entire box.",
            "Therefore, a semiconductor diode and a filament lamp in series produces this characteristic.",
            "Option A and Option B lack diode rectification (they would conduct in reverse). Option C would conduct in reverse through the parallel filament lamp branch."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q36",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "comparison",
            "direct_calculation"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_emf_internal_resistance",
        "accepted_answer": "A",
        "hints": [
            "Write the current in the circuit including internal resistance: I = E / (R + r), where r = 0.5 Ω.",
            "Compare the initial current I₁ = E / (10 + 0.5) = E / 10.5 with the new current I₂ = E / (20 + 0.5) = E / 20.5."
        ],
        "walkthrough": [
            "The total circuit resistance with the initial 10 Ω resistor is R₁ + r = 10 + 0.5 = 10.5 Ω, giving initial current I₁ = E / 10.5.",
            "When the resistance is doubled to 20 Ω, the total circuit resistance becomes R₂ + r = 20 + 0.5 = 20.5 Ω, giving current I₂ = E / 20.5. Because 20.5 ≠ 21.0, the current does not halve (it is 10.5 / 20.5 ≈ 0.512 of I₁), making statement A not correct.",
            "Statements B, C, and D are all correct: The e.m.f. is a property of the cell and remains constant. Power P = I² R = (E² R) / (R + r)² decreases from 0.0907 E² to 0.0476 E². Terminal p.d. V = E - Ir increases from 0.952 E to 0.976 E because the smaller current produces a smaller internal lost volts Ir."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q37",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "definition",
            "classification"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m02",
        "skill_id": "9702_skill_kirchhoffs_laws",
        "accepted_answer": "A",
        "hints": [
            "Recall that Kirchhoff's first law deals with junction currents and is based on conservation of electric charge.",
            "Recall that Kirchhoff's second law deals with electromotive forces and potential differences around a closed loop and is based on conservation of energy."
        ],
        "walkthrough": [
            "Kirchhoff's first law states that the algebraic sum of currents entering any junction in a circuit is equal to the sum of currents leaving the junction (ΣI_in = ΣI_out). Because charge cannot accumulate at a junction, this law is a direct consequence of the principle of conservation of charge.",
            "Kirchhoff's second law states that around any closed loop in a circuit, the sum of the electromotive forces is equal to the sum of the potential differences (ΣE = ΣV). Because the total work done per unit charge by sources must equal the energy transferred per unit charge in the components, this law is a direct consequence of the principle of conservation of energy.",
            "Row A correctly matches both laws and their corresponding conservation principles.",
            "Rows B, C, and D interchange the laws or swap the conservation principles."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q38",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "circuit_analysis",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_resistor_networks",
        "accepted_answer": "B",
        "hints": [
            "All resistors have identical resistance R. Analyze the right-hand parallel section: the lower branch has two identical resistors in series, with V₂ = 1.0 V across one of them.",
            "Determine the total p.d. across the parallel section from the lower branch (1.0 V + 1.0 V = 2.0 V), which gives V₄. Then subtract from the total supply voltage V₁ = 8.0 V to find the voltage across the two identical series resistors on the left."
        ],
        "walkthrough": [
            "The right part of the circuit is a parallel network. Its lower branch consists of two identical resistors of resistance R in series. Since voltmeter V₂ across one of these resistors reads 1.0 V, the current in the lower branch produces equal p.d. across both, giving a total p.d. across the parallel network of V_parallel = 1.0 V + 1.0 V = 2.0 V.",
            "Voltmeter V₄ is connected directly across the single resistor in the upper branch of this parallel network, so V₄ = V_parallel = 2.0 V.",
            "The left part of the circuit contains two identical resistors in series. By Kirchhoff's second law, the total supply p.d. is V₁ = 8.0 V, so the p.d. across the left part is V_left = V₁ - V_parallel = 8.0 V - 2.0 V = 6.0 V.",
            "Since the two left resistors are identical and in series, the p.d. divides equally between them. Voltmeter V₃ is across one resistor, so V₃ = (6.0 V) / 2 = 3.0 V.",
            "Thus, V₃ = 3.0 V and V₄ = 2.0 V, matching row B.",
            "Rows A, C, and D result from incorrect potential divider ratios or ignoring the supply voltage constraint."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q39",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "equation_completion",
            "classification"
        ],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m01",
        "skill_id": "9702_skill_nuclear_decay_equations",
        "accepted_answer": "D",
        "hints": [
            "Recall the conservation rules for nuclear decays: nucleon number (mass number A) and proton number (atomic number Z) are conserved.",
            "In α-decay, the parent nucleus loses 4 nucleons and 2 protons (A → A - 4, Z → Z - 2). In β⁻ decay, a neutron transforms into a proton, so A remains unchanged and Z increases by 1 (A → A, Z → Z + 1)."
        ],
        "walkthrough": [
            "In beta-minus (β⁻) decay, a neutron in the nucleus decays into a proton, an electron, and an electron antineutrino (n → p + e⁻ + ν̄_e). The nucleon number A remains constant and the proton number Z increases by 1.",
            "For thorium-231 decaying to protactinium-231 (²³¹₉₀Th → ²³¹₉₁Pa + β⁻ + ν̄_e): the nucleon number is conserved (231 = 231 + 0) and the proton number is conserved (90 = 91 - 1). Thus, this decay correctly forms protactinium-231.",
            "Evaluating the other decays: In row A, radium-226 decaying by α-emission yields radon-222 (²²²₈₆Rn), not radon-224. In row B, α-decay decreases nucleon number, so uranium-238 cannot produce plutonium-242. In row C, β⁻ decay increases Z from 88 to 89 (actinium), not decreases to 87 (francium)."
        ]
    },
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_w19_13_q40",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "classification",
            "property_identification"
        ],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m02",
        "skill_id": "9702_skill_fundamental_particles_interactions",
        "accepted_answer": "A",
        "hints": [
            "Recall the classification of subatomic particles: fundamental particles (particles with no internal substructure) include leptons (electrons, neutrinos, muons) and quarks (up, down, charm, strange, top, bottom).",
            "Hadrons (such as protons and neutrons) are composite particles made of quarks, whereas leptons are fundamental."
        ],
        "walkthrough": [
            "In the Standard Model of particle physics, fundamental particles are elementary particles that are not composed of smaller constituents. Leptons, which include electrons, muons, taus, and their corresponding neutrinos, are fundamental particles with no internal quark structure.",
            "Therefore, electrons and neutrinos are fundamental particles.",
            "Option B is incorrect because electrons and neutrinos are leptons, not hadrons. Option C is incorrect because protons and neutrons are hadrons (specifically baryons composed of three quarks), not leptons. Option D is incorrect because protons and neutrons are composed of quarks (p = uud, n = udd), but are not individual quarks themselves."
        ]
    }
]

out_dir = Path("subjects/physics/9702/enrichment/p1")
out_dir.mkdir(parents=True, exist_ok=True)

for item in enrichments:
    qid = item["question_id"]
    file_path = out_dir / f"{qid}.enrichment.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(item, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Generated {len(enrichments)} enrichment files.")
