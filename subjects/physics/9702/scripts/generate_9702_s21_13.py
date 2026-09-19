import json
import re
from pathlib import Path

enrichment_data = [
    # Q01
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q01",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "physical_quantity_estimation",
            "direct_calculation"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m01",
        "skill_id": "9702_skill_estimate_physical_quantities",
        "accepted_answer": "C",
        "hints": [
            "Estimate realistic orders of magnitude for the mass of an adult sprinter and their running speed during a 100 m race.",
            "Use the kinetic energy formula $E_\\text{k} = \\frac{1}{2}mv^2$ with an estimated mass of $m \\approx 70\\text{--}80\\text{ kg}$ and a sprinting speed of approximately $v \\approx 10\\text{ m s}^{-1}$."
        ],
        "walkthrough": [
            "An Olympic sprinter completes a 100 m race in approximately 10 s, corresponding to an average speed of $v = \\frac{100\\text{ m}}{10\\text{ s}} = 10\\text{ m s}^{-1}$ (with top speeds around $v \\approx 11\\text{--}12\\text{ m s}^{-1}$). A typical adult male athlete has a mass of $m \\approx 70\\text{--}80\\text{ kg}$.",
            "Substituting these estimates into the kinetic energy equation gives $E_\\text{k} = \\frac{1}{2}mv^2 \\approx \\frac{1}{2} \\times 80\\text{ kg} \\times (10\\text{ m s}^{-1})^2 = 4000\\text{ J} = 4\\text{ kJ}$.",
            "Option A (40 J) is far too small, corresponding to an 80 kg person moving at only $1\\text{ m s}^{-1}$. Option B (400 J) corresponds to walking speed ($v \\approx 3.2\\text{ m s}^{-1}$). Option D (40 000 J) would require a speed of $v \\approx 31.6\\text{ m s}^{-1}$ ($v \\approx 114\\text{ km h}^{-1}$), which is highway driving speed for a car."
        ]
    },
    # Q02
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q02",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "property_identification",
            "equation_recall"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m02",
        "skill_id": "9702_skill_derive_si_base_units",
        "accepted_answer": "C",
        "hints": [
            "Recall the definition of linear momentum ($p = mv$) and the impulse-momentum theorem ($\\Delta p = F\\Delta t$).",
            "Determine the unit of force multiplied by time, or express newtons in SI base units to verify the unit of momentum."
        ],
        "walkthrough": [
            "Linear momentum is defined as the product of mass and velocity, $p = mv$, giving SI base units of $\\text{kg m s}^{-1}$. From Newton's second law, resultant force is the rate of change of momentum ($F = \\frac{\\Delta p}{\\Delta t}$), so impulse is $\\Delta p = F\\Delta t$, which gives the equivalent unit $\\text{N s}$.",
            "Substituting the base units of the newton ($1\\text{ N} = 1\\text{ kg m s}^{-2}$) confirms that $1\\text{ N s} = (1\\text{ kg m s}^{-2}) \\times 1\\text{ s} = 1\\text{ kg m s}^{-1}$.",
            "Option A ($\\text{kg m s}^{-2}$) is the unit of force (the newton). Option B ($\\text{N s}^{-1}$) is the rate of change of force ($\text{kg m s}^{-3}$). Option D ($\\text{kg s m}^{-1}$) has incorrect physical dimensions."
        ]
    },
    # Q03
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q03",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "direct_calculation"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m04",
        "skill_id": "9702_skill_resolve_vector_components",
        "accepted_answer": "A",
        "hints": [
            "Identify the angle between the 20 N force vector and the horizontal axis.",
            "Use the cosine trigonometric ratio to find the adjacent horizontal component: $F_x = F \\cos\\theta$."
        ],
        "walkthrough": [
            "The force vector of magnitude $F = 20\\text{ N}$ acts at an angle $\\theta = 53^\\circ$ to the horizontal. The horizontal component is adjacent to the angle $\\theta$.",
            "Resolving horizontally: $F_x = F \\cos(53^\\circ) = 20\\text{ N} \\times \\cos(53^\\circ) \\approx 20 \\times 0.6018 = 12.04\\text{ N} \\approx 12\\text{ N}$.",
            "Option B (16 N) corresponds to the vertical component $F_y = 20 \\sin(53^\\circ) \\approx 16.0\\text{ N}$. Options C (25 N) and D (27 N) exceed the magnitude of the parent vector, which is impossible for an orthogonal component."
        ]
    },
    # Q04
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q04",
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
            "Carefully determine both readings by reading the main sleeve scale (including whole mm above and 0.5 mm marks below the datum line) and the thimble scale.",
            "Subtract reading 1 from reading 2: $\\Delta x = \\text{reading 2} - \\text{reading 1}$."
        ],
        "walkthrough": [
            "For reading 1: The sleeve shows the 1.0 mm mark above the line with no half-millimeter mark exposed below. The thimble aligns at 14 divisions ($0.14\\text{ mm}$). Thus, $\\text{reading 1} = 1.00\\text{ mm} + 0.14\\text{ mm} = 1.14\\text{ mm}$.",
            "For reading 2: The sleeve shows the 12.0 mm mark above the line and a visible 0.5 mm sub-division line below the datum line (giving $x_\\text{sleeve} = 12.50\\text{ mm}$). The thimble aligns at 48 divisions ($0.48\\text{ mm}$). Thus, $\\text{reading 2} = 12.50\\text{ mm} + 0.48\\text{ mm} = 12.98\\text{ mm}$.",
            "The difference between the two readings is $\\Delta x = 12.98\\text{ mm} - 1.14\\text{ mm} = 11.84\\text{ mm}$.",
            "Option A (10.34 mm) misses the 1.5 mm on reading 2. Options C (12.34 mm) and D (12.84 mm) arise from misidentifying the half-millimeter sleeve graduations."
        ]
    },
    # Q05
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q05",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "uncertainty_analysis",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m03",
        "skill_id": "9702_skill_uncertainty",
        "accepted_answer": "B",
        "hints": [
            "Calculate the area of the circular disc from its diameter using $A = \\frac{\\pi d^2}{4}$.",
            "For $A \\propto d^2$, find the fractional uncertainty $\\frac{\\Delta A}{A} = 2 \\times \\frac{\\Delta d}{d}$, then compute absolute uncertainty $\\Delta A$ and round to 1 significant figure."
        ],
        "walkthrough": [
            "The area of the circular disc of diameter $d = 7.0\\text{ mm}$ is $A = \\frac{\\pi d^2}{4} = \\frac{\\pi \\times (7.0)^2}{4} \\approx 38.48\\text{ mm}^2$.",
            "Since area depends on the square of diameter ($A \\propto d^2$), the fractional uncertainty is $\\frac{\\Delta A}{A} = 2\\left(\\frac{\\Delta d}{d}\\right) = 2 \\times \\left(\\frac{0.1}{7.0}\\right) = \\frac{0.2}{7.0} \\approx 0.02857$.",
            "The absolute uncertainty in area is $\\Delta A = 38.48\\text{ mm}^2 \\times 0.02857 \\approx 1.10\\text{ mm}^2 \\approx 1\\text{ mm}^2$. Expressing the result to the appropriate number of significant figures gives $A = (38 \\pm 1)\\text{ mm}^2$.",
            "Option A ($A = 38.5 \\pm 0.5\\text{ mm}^2$) omits the factor of 2 in power propagation and retains excessive decimal precision. Options C and D ($A = 154\\text{ mm}^2$) incorrectly treat the diameter as the radius ($A = \\pi d^2$)."
        ]
    },
    # Q06
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q06",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "graph_interpretation",
            "direct_calculation"
        ],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_determine_displacement_from_velocity_time_graph",
        "accepted_answer": "D",
        "hints": [
            "Recall that the distance travelled by an object is represented by the area under its velocity–time graph.",
            "Calculate the area of the trapezium under the graph line from $t = 0\\text{ s}$ to $t = 4.0\\text{ s}$ using $\\text{Area} = \\frac{u + v}{2} \\times t$."
        ],
        "walkthrough": [
            "The total distance travelled is equal to the area under the velocity–time graph between $t = 0\\text{ s}$ and $t = 4.0\\text{ s}$.",
            "From the graph, the initial velocity is $u = 2.0\\text{ m s}^{-1}$ and the final velocity is $v = 12.0\\text{ m s}^{-1}$. Since acceleration is constant (straight line), the area is a trapezium: $\\text{Distance} = \\frac{u + v}{2} \\times t = \\frac{2.0 + 12.0}{2} \\times 4.0 = 7.0 \\times 4.0 = 28\\text{ m}$.",
            "Alternatively, splitting the shape into a lower rectangle and an upper triangle gives $\\text{Area} = (2.0 \\times 4.0) + \\frac{1}{2}(12.0 - 2.0)(4.0) = 8.0 + 20.0 = 28\\text{ m}$.",
            "Option A (2.5 m) and Option B (3.0 m) confuse distance with acceleration (gradient $= 2.5\\text{ m s}^{-2}$) or other rate quantities. Option C (20 m) calculates only the upper triangular area, omitting the initial $2.0\\text{ m s}^{-1}$ baseline velocity rectangle."
        ]
    },
    # Q07
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q07",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "equation_derivation"
        ],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_apply_constant_acceleration",
        "accepted_answer": "C",
        "hints": [
            "Write down the kinematic equation connecting displacement $h$, initial velocity $u = 0$, acceleration $a$, and time $t$.",
            "Compare $h = \\frac{1}{2}at^2$ to the linear form $y = mx$, where $y = h$ and $x = t^2$, to express acceleration $a$ in terms of gradient $G$."
        ],
        "walkthrough": [
            "For a body dropped from rest ($u = 0$) under constant acceleration $a$, the equation of motion is $s = ut + \\frac{1}{2}at^2 \\implies h = \\frac{1}{2}at^2$.",
            "When plotting $h$ on the vertical $y$-axis against $t^2$ on the horizontal $x$-axis, the graph is a straight line through the origin of the form $y = Gx$, where gradient $G = \\frac{1}{2}a$.",
            "Rearranging for acceleration gives $a = 2G$.",
            "Option A ($\\frac{2}{G}$) inverts the relation. Option B ($G$) overlooks the factor of $\\frac{1}{2}$ in the kinematic equation. Option D ($G^2$) incorrectly squares the gradient."
        ]
    },
    # Q08
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q08",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "comparison",
            "direct_calculation"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_apply_newtons_second_law",
        "accepted_answer": "C",
        "hints": [
            "Resolve forces parallel to the frictionless slope for mass $M$, and identify the tension force provided by hanging mass $m$.",
            "For mass $M$ to accelerate downwards along the slope, the component of its weight along the slope must exceed the opposing gravitational force on mass $m$."
        ],
        "walkthrough": [
            "The component of the gravitational force on mass $M$ acting down the slope is $W_\\parallel = Mg \\sin\\theta$. The hanging mass $m$ is suspended vertically, connected via an inextensible string over a frictionless pulley.",
            "Applying Newton's second law to the system accelerating down the slope with acceleration $a > 0$: $(M + m)a = Mg \\sin\\theta - mg$.",
            "For acceleration to be down the slope ($a > 0$), the net driving force must be positive: $Mg \\sin\\theta > mg \\implies \\sin\\theta > \\frac{m}{M}$.",
            "Option A ($\\sin\\theta < \\frac{m}{M}$) would cause mass $M$ to accelerate up the slope (mass $m$ falling). Options B and D incorrectly use $\\cos\\theta$ instead of $\\sin\\theta$ for the component of weight parallel to the incline."
        ]
    },
    # Q09
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q09",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "comparison",
            "direct_calculation"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_apply_newtons_second_law",
        "accepted_answer": "D",
        "hints": [
            "Recall the relationship between weight $W$, mass $m$, and acceleration of free fall $g$: $g = \\frac{W}{m}$.",
            "Convert all weights to newtons (N) and all masses to kilograms (kg) before evaluating $g$ for each planet."
        ],
        "walkthrough": [
            "The surface acceleration of free fall is given by $g = \\frac{W}{m}$. We calculate $g$ in $\\text{N kg}^{-1}$ (or $\\text{m s}^{-2}$) for each planet:",
            "Planet A: $g = \\frac{40 \\times 10^{-3}\\text{ N}}{6.0 \\times 10^{-3}\\text{ kg}} = \\frac{40}{6.0} \\approx 6.67\\text{ m s}^{-2}$.",
            "Planet B: $g = \\frac{3.0\\text{ N}}{0.500\\text{ kg}} = 6.0\\text{ m s}^{-2}$.",
            "Planet C: $g = \\frac{10\\text{ N}}{1\\text{ kg}} = 10\\text{ m s}^{-2}$.",
            "Planet D: $g = \\frac{2.6 \\times 10^3\\text{ N}}{750\\text{ kg}} = \\frac{2600}{750} \\approx 3.47\\text{ m s}^{-2}$.",
            "Comparing the calculated values, Planet D has the lowest value of $g$ ($3.47\\text{ m s}^{-2}$)."
        ]
    },
    # Q10
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q10",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "particle_model_application",
            "comparison"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m03",
        "skill_id": "9702_skill_apply_momentum_conservation",
        "accepted_answer": "B",
        "hints": [
            "Identify the direction of the initial total linear momentum of the rock–spacecraft system.",
            "Apply the principle of conservation of linear momentum: the total final momentum vector must equal the initial forward momentum vector."
        ],
        "walkthrough": [
            "Prior to the collision, the rock travels towards the star (defined as positive direction, $+p_0$) and the spacecraft is stationary ($p_\\text{craft} = 0$). Thus, the initial total momentum of the isolated system is strictly positive: $p_\\text{total} = +p_0 > 0$.",
            "By conservation of linear momentum, the total momentum after the collision must also be $+p_0 > 0$.",
            "In Option B, both the rock and the spacecraft move away from the star, meaning both have negative velocities and negative momenta. The sum of two negative momenta cannot equal a positive initial momentum, making this outcome impossible.",
            "Option A is possible in an elastic collision with equal masses. Option C is possible if the rock rebounds while the spacecraft carries a large forward momentum. Option D is possible when both objects continue moving towards the star."
        ]
    },
    # Q11
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q11",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "comparison",
            "explanation"
        ],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m02",
        "skill_id": "9702_skill_analyse_resistive_force_motion",
        "accepted_answer": "A",
        "hints": [
            "Compare the magnitude of upthrust in air to the weight of a dense steel ball using their densities.",
            "At terminal speed, acceleration is zero, so the downward weight is balanced by the sum of upward forces: $\\text{Weight} = \\text{Upthrust} + \\text{Viscous drag}$."
        ],
        "walkthrough": [
            "A steel ball is dense ($\\rho_\\text{steel} \\approx 7800\\text{ kg m}^{-3}$) compared to air ($\\rho_\\text{air} \\approx 1.2\\text{ kg m}^{-3}$). The upthrust $U = \\rho_\\text{air}Vg$ is several orders of magnitude smaller than the weight $W = \\rho_\\text{steel}Vg$, so $U \\ll W$.",
            "At constant terminal speed, the resultant vertical force is zero: $W = U + F_\\text{drag}$. Because upthrust is tiny, viscous drag must provide nearly the entire upward balancing force ($F_\\text{drag} = W - U \\approx W$).",
            "Therefore, the forces in order of increasing magnitude are upthrust $\\rightarrow$ viscous drag $\\rightarrow$ weight.",
            "Option B incorrectly places viscous drag below upthrust. Options C and D place weight as smallest or in the middle, which contradicts the downward equilibrium balance."
        ]
    },
    # Q12
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q12",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "definition"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_define_torque_of_couple",
        "accepted_answer": "B",
        "hints": [
            "Recall the formal definition of a couple in terms of force magnitudes, directions, and lines of action.",
            "A couple creates pure turning (torque) without producing any linear translation."
        ],
        "walkthrough": [
            "In mechanics, a couple is defined as a pair of forces that are equal in magnitude, opposite in direction, and act along parallel, non-coincident lines of action.",
            "Because the forces are equal and opposite, their vector sum (resultant force) is zero, but because their lines of action are separated by a perpendicular distance, they produce a non-zero resultant torque.",
            "Option A describes forces in the same direction (non-zero resultant force). Option C describes full translational and rotational equilibrium. Option D describes collinear unequal forces causing net translation."
        ]
    },
    # Q13
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q13",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "comparison",
            "direct_calculation"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_calculate_moment_from_line_of_action",
        "accepted_answer": "A",
        "hints": [
            "Calculate the moment of each force about point P using $\\text{Moment} = F \\times d \\times \\sin\\theta$, where $d$ is the distance from P to the application point.",
            "Compare the numerical magnitudes of the moments for forces A, B, C, and D."
        ],
        "walkthrough": [
            "The moment of a force about pivot P is given by $\\tau = F \\times d \\times \\sin\\theta$, where $d$ is the distance from P along the rod and $\\theta$ is the angle between the force and the rod:",
            "Force A: $F = 10\\text{ N}$, $d = 1.0\\text{ m}$, $\\theta = 90^\\circ \\implies \\tau_\\text{A} = 10 \\times 1.0 \\times \\sin(90^\\circ) = 10.0\\text{ N m}$.",
            "Force B: $F = 6\\text{ N}$, $d = 2.0\\text{ m}$, $\\theta = 30^\\circ \\implies \\tau_\\text{B} = 6 \\times 2.0 \\times \\sin(30^\\circ) = 6 \\times 2.0 \\times 0.5 = 6.0\\text{ N m}$.",
            "Force C: $F = 2\\text{ N}$, $d = 3.0\\text{ m}$, $\\theta = 90^\\circ \\implies \\tau_\\text{C} = 2 \\times 3.0 \\times \\sin(90^\\circ) = 6.0\\text{ N m}$.",
            "Force D: $F = 4\\text{ N}$, $d = 4.0\\text{ m}$, $\\theta = 30^\\circ \\implies \\tau_\\text{D} = 4 \\times 4.0 \\times \\sin(30^\\circ) = 4 \\times 4.0 \\times 0.5 = 8.0\\text{ N m}$.",
            "Comparing these values, Force A produces the greatest moment ($\\tau = 10.0\\text{ N m}$).",
            "Options B, C, and D produce smaller moments ($6.0\\text{ N m}$, $6.0\\text{ N m}$, and $8.0\\text{ N m}$ respectively)."
        ]
    },
    # Q14
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q14",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "explanation"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_apply_principle_of_moments",
        "accepted_answer": "A",
        "hints": [
            "Find the position of the centre of gravity of the uniform rectangular book of width $a$ and height $b$.",
            "Determine the perpendicular horizontal distance from the hand's grip point at the top edge/corner to the vertical line of action of weight $W$, then deduce the direction of torque the hand must apply to prevent rotation."
        ],
        "walkthrough": [
            "The book is a uniform rectangle of width $a$ (horizontal) and height $b$ (vertical). Its centre of gravity is at its geometric centre, which is located a horizontal distance of $\\frac{a}{2}$ from the side edges.",
            "The weight $W$ acts vertically downwards through the centre of gravity. With the hand holding the top edge/corner at horizontal position $x = a$, the perpendicular distance between the hand's contact point and the vertical line of action of $W$ is $\\frac{a}{2}$.",
            "The gravitational force creates an anticlockwise moment of $W \\times \\frac{a}{2} = \\frac{Wa}{2}$ about the hand. To maintain equilibrium, the hand must exert an equal and opposite balancing torque of $\\frac{Wa}{2}$ clockwise.",
            "Option B uses the vertical height $b$ (which is parallel to the line of action of weight). Options C and D omit the factor of $\\frac{1}{2}$ needed for the distance to the centre of mass."
        ]
    },
    # Q15
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q15",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "equation_derivation",
            "property_identification"
        ],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m03",
        "skill_id": "9702_skill_apply_hydrostatic_pressure",
        "accepted_answer": "B",
        "hints": [
            "Review the steps used to derive hydrostatic pressure $\\Delta p = \\rho g \\Delta h$ from the weight of a vertical fluid column of cross-sectional area $A$ and height $\\Delta h$.",
            "Identify which expression among the choices is never used when relating fluid mass, weight, and pressure."
        ],
        "walkthrough": [
            "The derivation of hydrostatic pressure $\\Delta p = \\rho g \\Delta h$ proceeds as follows:",
            "1. Volume of fluid column: $V = A\\Delta h$, so mass is $m = \\rho V = \\rho A\\Delta h$ (using $\\text{density} = \\frac{\\text{mass}}{\\text{volume}}$).",
            "2. Force at the base is the weight of the fluid column: $W = mg = \\rho A\\Delta h g$ (using $\\text{weight} = \\text{mass} \\times g$).",
            "3. Pressure is force per unit area: $\\Delta p = \\frac{W}{A} = \\frac{\\rho A\\Delta h g}{A} = \\rho g \\Delta h$ (using $\\text{pressure} = \\frac{\\text{force}}{\\text{area}}$).",
            "At no stage in this static force balance derivation is gravitational potential energy ($E_\\text{p} = mgh$) used.",
            "Options A, C, and D are essential relationships directly used in the steps of the derivation."
        ]
    },
    # Q16
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q16",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "property_identification",
            "explanation"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_define_elastic_potential_energy",
        "accepted_answer": "D",
        "hints": [
            "Recall that the elastic potential energy stored in an ideal spring deformed by displacement $x$ from its equilibrium length is $E_\\text{p} = \\frac{1}{2}kx^2$.",
            "Consider whether work is done on the spring when stretching ($x > 0$) or compressing ($x < 0$) it from the unstrained state ($x = 0$)."
        ],
        "walkthrough": [
            "When the spring is neither compressed nor extended ($x = 0$), its elastic potential energy is at its minimum baseline value ($E_\\text{p} = 0$).",
            "Extending the spring increases extension $x > 0$. Work is done by an applied force against the restoring tension, increasing stored elastic potential energy $E_\\text{p} = \\frac{1}{2}kx^2$.",
            "Compressing the spring ($x < 0$) also requires work to be done against compressive restoring forces. Since $(-x)^2 = x^2 > 0$, the stored elastic potential energy $E_\\text{p} = \\frac{1}{2}kx^2$ increases.",
            "Therefore, elastic potential energy increases when extended and increases when compressed.",
            "Options A, B, and C incorrectly suggest that compressing or extending an unstrained spring can decrease its stored elastic potential energy."
        ]
    },
    # Q17
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q17",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_calculate_work_from_force_displacement",
        "accepted_answer": "C",
        "hints": [
            "Use the relationship for work done by a gas at constant pressure: $W = p\\Delta V$.",
            "Because the gas does work on its surroundings, its volume increases ($\\Delta V > 0$). Add $\\Delta V$ to the initial volume $V_1$."
        ],
        "walkthrough": [
            "The work done by an expanding gas at constant pressure $p$ is $W = p\\Delta V = p(V_2 - V_1)$.",
            "Rearranging for the increase in volume: $\\Delta V = \\frac{W}{p} = \\frac{14.4\\text{ J}}{1.80 \\times 10^5\\text{ Pa}} = 8.00 \\times 10^{-5}\\text{ m}^3 = 0.80 \\times 10^{-4}\\text{ m}^3$.",
            "Because the gas does positive work, it expands, so the final volume is $V_2 = V_1 + \\Delta V = 2.40 \\times 10^{-4}\\text{ m}^3 + 0.80 \\times 10^{-4}\\text{ m}^3 = 3.20 \\times 10^{-4}\\text{ m}^3$.",
            "Option A ($0.80 \\times 10^{-4}\\text{ m}^3$) is only the volume change $\\Delta V$. Option B ($1.60 \\times 10^{-4}\\text{ m}^3$) incorrectly subtracts $\\Delta V$. Option D ($4.00 \\times 10^{-4}\\text{ m}^3$) is an arithmetic error."
        ]
    },
    # Q18
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q18",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "multi_step_calculation"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_conservation_of_energy",
        "accepted_answer": "B",
        "hints": [
            "Calculate the loss in gravitational potential energy of the car from X to Y using $\\Delta E_\\text{p} = mgh$.",
            "Calculate the gain in kinetic energy using $E_\\text{k} = \\frac{1}{2}mv^2$, then determine the energy dissipated by taking $\\Delta E_\\text{p} - E_\\text{k}$."
        ],
        "walkthrough": [
            "The gravitational potential energy lost by the car descending a vertical height $h = 30\\text{ m}$ is $\\Delta E_\\text{p} = mgh = 500\\text{ kg} \\times 9.81\\text{ m s}^{-2} \\times 30\\text{ m} = 147150\\text{ J} \\approx 1.47 \\times 10^5\\text{ J}$.",
            "The kinetic energy gained from rest to $v = 11\\text{ m s}^{-1}$ is $E_\\text{k} = \\frac{1}{2}mv^2 = \\frac{1}{2} \\times 500\\text{ kg} \\times (11\\text{ m s}^{-1})^2 = 250 \\times 121 = 30250\\text{ J} \\approx 3.03 \\times 10^4\\text{ J}$.",
            "By conservation of energy, the energy dissipated by frictional forces is $E_\\text{dissipated} = \\Delta E_\\text{p} - E_\\text{k} = 147150\\text{ J} - 30250\\text{ J} = 116900\\text{ J} \\approx 1.2 \\times 10^5\\text{ J}$.",
            "Option A ($3.0 \\times 10^4\\text{ J}$) is only the final kinetic energy. Option C ($1.5 \\times 10^5\\text{ J}$) is the initial GPE without subtracting kinetic energy. Option D ($1.8 \\times 10^5\\text{ J}$) incorrectly adds GPE and KE."
        ]
    },
    # Q19
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q19",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "equation_recall",
            "definition"
        ],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_define_power",
        "accepted_answer": "D",
        "hints": [
            "Recall the standard definitions of power as the rate of doing work ($P = \\frac{W}{t}$) and as force times velocity ($P = Fv$).",
            "Check the base units and dimensional formula of each expression to find which one does not equal the watt ($\\text{J s}^{-1}$)."
        ],
        "walkthrough": [
            "Power is defined as the rate of energy transfer or work done: $P = \\frac{\\text{work done}}{\\text{time}}$ (Option C).",
            "Since work done is force multiplied by displacement ($W = F \\times s$), substituting this gives $P = \\frac{F \\times s}{t} = F \\times \\frac{s}{t} = Fv$ (Options A and B).",
            "Option D gives $\\text{work done} \\times \\text{velocity} = Wv$, which has units of $\\text{J} \\times \\text{m s}^{-1} = \\text{N m}^2\\text{s}^{-1} = \\text{W m}$, not watts (W). Hence, Option D cannot be used to calculate power."
        ]
    },
    # Q20
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q20",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "equation_derivation",
            "definition"
        ],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m01",
        "skill_id": "9702_skill_define_young_modulus",
        "accepted_answer": "D",
        "hints": [
            "Recall the definition of the Young modulus: $E = \\frac{\\text{stress}}{\\text{strain}} = \\frac{\\sigma}{\\varepsilon}$.",
            "Substitute $\\sigma = \\frac{F}{A}$ directly into the definition of the Young modulus."
        ],
        "walkthrough": [
            "The Young modulus $E$ of a material is defined as the ratio of tensile stress to tensile strain: $E = \\frac{\\sigma}{\\varepsilon}$.",
            "Substituting the expression for stress $\\sigma = \\frac{F}{A}$ directly into the definition gives $E = \\frac{F/A}{\\varepsilon} = \\frac{F}{A\\varepsilon}$.",
            "Option A ($\\frac{\\varepsilon}{\\sigma}$) inverts the ratio. Option B ($\\frac{Fx}{AL}$) inverts the strain substitution (the correct formula in terms of $x$ and $L$ is $\\frac{FL}{Ax}$). Option C ($\\frac{x/L}{\\sigma}$) divides strain by stress."
        ]
    },
    # Q21
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q21",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "definition",
            "classification"
        ],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m02",
        "skill_id": "9702_skill_assess_elastic_deformation",
        "accepted_answer": "C",
        "hints": [
            "Distinguish between elastic deformation (temporary) and plastic deformation (permanent).",
            "Look for the scenario where an object retains a permanent change in shape after the deforming load is removed."
        ],
        "walkthrough": [
            "Plastic deformation occurs when a material is stressed beyond its elastic limit, so that it does not return to its original shape or dimensions after the deforming load is removed, resulting in permanent deformation.",
            "In Option C, when the heavy toolbox is removed, the wooden plank remains permanently bent and is no longer straight, which is a clear example of plastic deformation.",
            "Option A (rubber ball bouncing back) is an example of elastic deformation. Option B describes an acoustic impact with no permanent distortion. Option D describes a scale spring compressing within its reversible elastic region."
        ]
    },
    # Q22
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q22",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "direct_calculation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_determine_phase_difference_from_wave_profile",
        "accepted_answer": "B",
        "hints": [
            "Use the sinusoidal wave equation $y = y_0 \\sin\\left(\\frac{2\\pi}{\\lambda}x\\right)$ or the mirror symmetry about the first crest at $x = \\frac{\\lambda}{4}$.",
            "Find the position on the falling side of the crest that has $+y_1$, and then add one full wavelength $\\lambda$ to the initial position $x = \\frac{\\lambda}{8}$ for the next cycle."
        ],
        "walkthrough": [
            "The wave profile is a sine wave: $y(x) = y_0 \\sin\\left(\\frac{2\\pi}{\\lambda}x\\right)$. At $x_1 = \\frac{\\lambda}{8}$, the displacement is $y_1 = y_0 \\sin\\left(\\frac{\\pi}{4}\\right) = \\frac{y_0}{\\sqrt{2}}$.",
            "1. By symmetry about the peak at $x = \\frac{\\lambda}{4}$, the displacement is next equal to $+y_1$ at $x_2 = \\frac{\\lambda}{2} - \\frac{\\lambda}{8} = \\frac{3\\lambda}{8}$.",
            "2. The third position with displacement $+y_1$ occurs in the next wave cycle, exactly one full wavelength $\\lambda$ past the first point: $x_3 = \\frac{\\lambda}{8} + \\lambda = \\frac{9\\lambda}{8}$.",
            "Thus, the next two values of $x$ where $y = +y_1$ are $\\frac{3\\lambda}{8}$ and $\\frac{9\\lambda}{8}$.",
            "Option A includes $\\frac{5\\lambda}{8}$ (which gives displacement $-y_1$). Option C omits the symmetric point $\\frac{3\\lambda}{8}$. Option D skips both points within the first two wave periods."
        ]
    },
    # Q23
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q23",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "multi_step_calculation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_apply_wave_speed",
        "accepted_answer": "A",
        "hints": [
            "Read the time period $T$ between consecutive peaks from the displacement–time graph.",
            "Use the wave speed equation $\\lambda = vT = \\frac{v}{f}$ with speed of sound $v = 330\\text{ m s}^{-1}$."
        ],
        "walkthrough": [
            "From the displacement–time graph, successive peaks occur at $t = 10\\text{ ms}$, $t = 30\\text{ ms}$, and $t = 50\\text{ ms}$. The period of the wave is therefore $T = 30\\text{ ms} - 10\\text{ ms} = 20\\text{ ms} = 2.0 \\times 10^{-2}\\text{ s}$.",
            "The frequency of the sound wave is $f = \\frac{1}{T} = \\frac{1}{0.020\\text{ s}} = 50\\text{ Hz}$.",
            "Using the wave relationship $v = f\\lambda$, the wavelength is $\\lambda = vT = 330\\text{ m s}^{-1} \\times 0.020\\text{ s} = 6.6\\text{ m}$.",
            "Option B (8.3 m) results from misidentifying a half-period or calculating $T$ as 25 ms. Option C (20 m) confuses period (20 ms) with wavelength. Option D (25 m) incorrectly reads from a trough to a node."
        ]
    },
    # Q24
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q24",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "direct_calculation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_interpret_oscilloscope_traces",
        "accepted_answer": "A",
        "hints": [
            "Determine the horizontal length in centimeters on the CRO screen that corresponds to one complete wave cycle.",
            "Multiply by the time-base setting ($1.0\\text{ ms cm}^{-1}$) to find the period $T$, then calculate $f = \\frac{1}{T}$."
        ],
        "walkthrough": [
            "On the cathode-ray oscilloscope screen, one full wave cycle (from one peak to the next) occupies 4 grid squares horizontally ($4.0\\text{ cm}$).",
            "With the time-base set to $1.0\\text{ ms cm}^{-1}$, the period of the sound wave is $T = 4.0\\text{ cm} \\times 1.0\\text{ ms cm}^{-1} = 4.0\\text{ ms} = 4.0 \\times 10^{-3}\\text{ s}$.",
            "The frequency of the wave is $f = \\frac{1}{T} = \\frac{1}{4.0 \\times 10^{-3}\\text{ s}} = 250\\text{ Hz}$.",
            "Option B (500 Hz) results from using half a cycle ($2.0\\text{ cm}$). Option C (670 Hz) comes from misreading 3 divisions. Option D (4000 Hz) results from a unit conversion error."
        ]
    },
    # Q25
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q25",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": [
            "multi_step_calculation"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m03",
        "skill_id": "9702_skill_apply_doppler_effect",
        "accepted_answer": "D",
        "hints": [
            "Apply the Doppler formula for a moving source: $f_\\text{obs} = f_\\text{s} \\left(\\frac{v}{v \\mp v_\\text{s}}\\right)$ for approach ($-$) and recession ($+$).",
            "Compute the observed frequency before the train passes ($f_\\text{approach}$) and after it passes ($f_\\text{recede}$), then find their difference $\\Delta f$."
        ],
        "walkthrough": [
            "When the train approaches the stationary observer at $v_\\text{s} = 20\\text{ m s}^{-1}$, the observed frequency is $f_\\text{approach} = f_\\text{s}\\left(\\frac{v}{v - v_\\text{s}}\\right) = 500\\text{ Hz} \\times \\left(\\frac{330}{330 - 20}\\right) = 500 \\times \\frac{330}{310} \\approx 532.26\\text{ Hz}$.",
            "When the train recedes from the observer at $v_\\text{s} = 20\\text{ m s}^{-1}$, the observed frequency is $f_\\text{recede} = f_\\text{s}\\left(\\frac{v}{v + v_\\text{s}}\\right) = 500\\text{ Hz} \\times \\left(\\frac{330}{330 + 20}\\right) = 500 \\times \\frac{330}{350} \\approx 471.43\\text{ Hz}$.",
            "The difference between the two heard frequencies is $\\Delta f = f_\\text{approach} - f_\\text{recede} = 532.26\\text{ Hz} - 471.43\\text{ Hz} = 60.83\\text{ Hz} \\approx 61\\text{ Hz}$.",
            "Option A (29 Hz) is the shift between source and receding frequency ($f_\\text{s} - f_\\text{recede} = 500 - 471.4 = 28.6\\text{ Hz}$). Option B (32 Hz) is the shift on approach ($f_\\text{approach} - f_\\text{s} = 532.3 - 500 = 32.3\\text{ Hz}$). Option C (40 Hz) is an approximation based on $2v_s$."
        ]
    },
    # Q26
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q26",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "classification",
            "property_identification"
        ],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m04",
        "skill_id": "9702_skill_identify_electromagnetic_spectrum_region",
        "accepted_answer": "B",
        "hints": [
            "Recall the order of the regions in the electromagnetic spectrum by wavelength.",
            "Gamma-rays have the shortest wavelengths and highest frequencies, while microwaves have long wavelengths relative to visible light."
        ],
        "walkthrough": [
            "The regions of the electromagnetic spectrum in order of increasing wavelength (decreasing frequency) are: gamma-rays ($\\lambda < 10^{-11}\\text{ m}$) $\\rightarrow$ X-rays ($\\lambda \\approx 10^{-11}\\text{--}10^{-8}\\text{ m}$) $\\rightarrow$ ultraviolet $\\rightarrow$ visible light ($\\lambda \\approx 4 \\times 10^{-7}\\text{--}7 \\times 10^{-7}\\text{ m}$) $\\rightarrow$ infrared $\\rightarrow$ microwaves ($\\lambda \\approx 10^{-3}\\text{--}10^{-1}\\text{ m}$) $\\rightarrow$ radio waves ($\\lambda > 10^{-1}\\text{ m}$).",
            "Arranging the four listed regions in order of increasing wavelength yields: gamma-rays $\\rightarrow$ X-rays $\\rightarrow$ visible light $\\rightarrow$ microwaves.",
            "Option A represents the reverse order (decreasing wavelength). Option C and Option D misplace X-rays and visible light."
        ]
    },
    # Q27
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q27",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "property_identification",
            "explanation"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m01",
        "skill_id": "9702_skill_explain_stationary_waves",
        "accepted_answer": "C",
        "hints": [
            "Recall the conditions required for two progressive waves to superpose and form a standing wave.",
            "Consider that both waves travel in the same medium and have identical frequency, then apply the wave equation $v = f\\lambda$."
        ],
        "walkthrough": [
            "A stationary (standing) wave is formed by the superposition of two progressive waves of identical frequency and similar amplitude travelling in opposite directions in the same medium.",
            "Because both waves travel through the same medium, their wave speeds must be identical ($v_1 = v_2$). Since their frequencies are equal ($f_1 = f_2$), the wave relationship $v = f\\lambda$ dictates that their wavelengths must also be identical ($\\lambda_1 = \\lambda_2$).",
            "Therefore, the two waves must have equal speeds, equal frequencies, and equal wavelengths.",
            "Options A, B, and D propose differing speeds, wavelengths, or frequencies, which would fail to produce fixed spatial nodes and antinodes."
        ]
    },
    # Q28
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q28",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "property_identification"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m02",
        "skill_id": "9702_skill_explain_diffraction",
        "accepted_answer": "B",
        "hints": [
            "Calculate the wavelength of the sound wave using $\\lambda = \\frac{v}{f}$ with $v = 330\\text{ m s}^{-1}$ and $f = 0.44\\text{ kHz}$.",
            "Diffraction is most significant when the size of the architectural feature is of the same order of magnitude as the wavelength."
        ],
        "walkthrough": [
            "Using the wave speed equation $v = f\\lambda$, the wavelength of sound in air is $\\lambda = \\frac{v}{f} = \\frac{330\\text{ m s}^{-1}}{0.44 \\times 10^3\\text{ Hz}} = \\frac{330}{440} = 0.75\\text{ m} = 750\\text{ mm}$.",
            "Significant diffraction occurs when the dimensions of an aperture or obstacle are roughly equal to the wavelength of the wave ($d \\approx \\lambda$). Therefore, features of size $d = 750\\text{ mm}$ will best diffract this sound wave.",
            "Option A (1.3 mm) is far too small ($d \\ll \\lambda$). Options C (7.5 m) and D (17 m) are much larger than the wavelength ($d \\gg \\lambda$), resulting in minimal wave spreading and sharp shadow zones."
        ]
    },
    # Q29
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q29",
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
            "Recall Young's double-slit interference formula: $x = \\frac{\\lambda D}{a}$.",
            "For unchanged slit separation $a$ and screen distance $D$, fringe spacing is directly proportional to wavelength: $\\frac{x_\\text{blue}}{x_\\text{red}} = \\frac{\\lambda_\\text{blue}}{\\lambda_\\text{red}}$."
        ],
        "walkthrough": [
            "The double-slit fringe spacing is given by $x = \\frac{\\lambda D}{a}$. With the apparatus geometry ($a$ and $D$) kept constant, fringe spacing is directly proportional to wavelength: $x \\propto \\lambda$.",
            "Setting up the ratio: $x_\\text{blue} = x_\\text{red} \\times \\left(\\frac{\\lambda_\\text{blue}}{\\lambda_\\text{red}}\\right)$.",
            "Substituting the values: $x_\\text{blue} = 3.5\\text{ mm} \\times \\left(\\frac{4.5 \\times 10^{-7}\\text{ m}}{7.0 \\times 10^{-7}\\text{ m}}\\right) = 3.5\\text{ mm} \\times \\frac{4.5}{7.0} = 3.5 \\times 0.6429 = 2.25\\text{ mm} \\approx 2.3\\text{ mm}$.",
            "Option B (3.5 mm) assumes fringe spacing is independent of wavelength. Option C (5.4 mm) mistakenly multiplies by the inverted ratio $\\frac{7.0}{4.5}$. Option D (9.0 mm) is an arithmetic miscalculation."
        ]
    },
    # Q30
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q30",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "graph_interpretation",
            "equation_derivation"
        ],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m04",
        "skill_id": "9702_skill_apply_diffraction_grating",
        "accepted_answer": "B",
        "hints": [
            "Write down the diffraction grating equation for normal incidence: $d\\sin\\theta = n\\lambda$.",
            "Rearrange the equation to match the linear form $y = mx$, and determine how the gradient relates to wavelength $\\lambda$ when $y = n$ and $x = d\\sin\\theta$."
        ],
        "walkthrough": [
            "The diffraction grating equation for light incident normally is $d\\sin\\theta = n\\lambda$, where $d$ is slit spacing, $\\theta$ is diffraction angle, and $n$ is diffraction order.",
            "Rearranging the formula with $n$ on the vertical $y$-axis gives $n = \\left(\\frac{1}{\\lambda}\\right)(d\\sin\\theta)$.",
            "Comparing this with $y = mx$ shows that plotting $y = n$ against $x = d\\sin\\theta$ gives a straight line through the origin with gradient $m = \\frac{1}{\\lambda}$. Hence, the wavelength is determined from $\\lambda = \\frac{1}{\\text{gradient}}$.",
            "Option A states $\\lambda = \\text{gradient}$, which is the inverse of the true relation. Options C and D propose non-linear forms that do not yield a constant gradient directly related to wavelength."
        ]
    },
    # Q31
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q31",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "direct_calculation",
            "property_identification"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_define_electric_field_strength",
        "accepted_answer": "D",
        "hints": [
            "Use the relationship between electric field strength $E$, electric force $F$, and electric charge $q$: $E = \\frac{F}{q}$.",
            "Recall that the direction of an electric field is the direction of the force on a positive test charge."
        ],
        "walkthrough": [
            "Electric field strength is defined as force per unit positive charge: $E = \\frac{F}{q}$.",
            "Substituting $F = 1.0 \\times 10^{-2}\\text{ N}$ and $q = +2.0\\text{ mC} = +2.0 \\times 10^{-3}\\text{ C}$: $E = \\frac{1.0 \\times 10^{-2}\\text{ N}}{2.0 \\times 10^{-3}\\text{ C}} = 5.0\\text{ N C}^{-1} = 5.0\\text{ V m}^{-1}$.",
            "Because the particle carries a positive charge ($+2.0\\text{ mC}$) and the electric force on it acts upwards, the electric field must also be directed upwards.",
            "Options A and B ($0.20\\text{ V m}^{-1}$) result from dividing charge by force. Option C ($5.0\\text{ V m}^{-1}$ downwards) assigns the field direction opposite to the force on a positive charge."
        ]
    },
    # Q32
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q32",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "comparison",
            "direct_calculation"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_apply_uniform_electric_field",
        "accepted_answer": "A",
        "hints": [
            "Recall the formula for the uniform electric field between parallel plates: $E = \\frac{V}{d}$.",
            "Note that in steady state, no current flows onto the plates, so the potential difference across the plates equals the power supply voltage regardless of the series resistor."
        ],
        "walkthrough": [
            "The electric field strength between two parallel plates separated by distance $d$ with a potential difference $V$ across them is $E = \\frac{V}{d}$.",
            "Since no steady current flows in this open-circuit capacitor branch, there is zero potential drop across the series resistor ($V_\\text{resistor} = 0$), so the full supply voltage appears across the plates ($V_\\text{plates} = V_\\text{supply}$).",
            "Increasing the plate separation distance $d$ increases the denominator in $E = \\frac{V}{d}$, causing a decrease in the electric field strength.",
            "Option B (increasing $V$) increases $E$. Option C (increasing resistance) has no effect on steady-state plate voltage. Option D (increasing plate area) changes plate capacitance but leaves field strength $E = \\frac{V}{d}$ unchanged."
        ]
    },
    # Q33
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q33",
        "component": "P1",
        "difficulty": 3,
        "question_patterns": [
            "multi_step_calculation"
        ],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m01",
        "skill_id": "9702_skill_apply_drift_current",
        "accepted_answer": "C",
        "hints": [
            "Relate the total number of free electrons $N$ in a wire of length $L$ and area $A$ to the number density: $n = \\frac{N}{AL}$.",
            "Substitute $n$ into the drift-current equation $I = nAvq$ so that cross-sectional area $A$ cancels, yielding $I = \\frac{Nvq}{L}$."
        ],
        "walkthrough": [
            "The macroscopic current in a conductor is related to average drift speed $v$ by $I = nAvq$, where $n$ is free electron number density and $q = e = 1.60 \\times 10^{-19}\\text{ C}$.",
            "The total number of free electrons in the wire volume $V = AL$ is $N = nAL \\implies nA = \\frac{N}{L}$.",
            "Substituting into the current equation: $I = \\left(\\frac{N}{L}\\right)vq = \\frac{N v e}{L}$.",
            "With $N = 5.1 \\times 10^{22}$, $v = 4.0 \\times 10^{-6}\\text{ m s}^{-1}$, $e = 1.60 \\times 10^{-19}\\text{ C}$, and $L = 0.12\\text{ m}$:",
            "$I = \\frac{5.1 \\times 10^{22} \\times 4.0 \\times 10^{-6} \\times 1.60 \\times 10^{-19}}{0.12} = \\frac{3.264 \\times 10^{-2}}{0.12} = 0.272\\text{ A} \\approx 0.27\\text{ A}$.",
            "Options A (0.0027 A) and B (0.0039 A) result from power-of-ten errors. Option D (0.39 A) arises from an arithmetic calculation mistake."
        ]
    },
    # Q34
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q34",
        "component": "P1",
        "difficulty": 1,
        "question_patterns": [
            "definition",
            "property_identification"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_define_electromotive_force",
        "accepted_answer": "A",
        "hints": [
            "Recall the definition of electromotive force (e.m.f.) as energy converted to electrical form per unit charge driven around a complete circuit.",
            "Differentiate between energy supplied to the entire circuit (including internal resistance) and potential difference across external components."
        ],
        "walkthrough": [
            "The electromotive force (e.m.f.) of a source is defined as the chemical energy converted into electrical energy per unit charge driven around a complete (whole) circuit: $E = \\frac{W}{Q}$.",
            "A battery rated at 9.0 V therefore converts and supplies 9.0 J of electrical energy to the whole circuit for every 1.0 C of charge passing through it.",
            "Option B describes terminal potential difference, which only accounts for energy delivered to the external load circuit ($V < E$ when current flows). Options C and D are false because terminal potential difference varies with load current due to internal resistance ($V = E - Ir$)."
        ]
    },
    # Q35
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q35",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "circuit_analysis",
            "direct_calculation"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_determine_current_in_opposing_emf_loop",
        "accepted_answer": "A",
        "hints": [
            "Trace the closed loop to see whether the two batteries drive current in the same direction or oppose one another.",
            "Calculate the resultant e.m.f. and total resistance, then find current using $I = \\frac{\\Sigma E}{\\Sigma R}$."
        ],
        "walkthrough": [
            "In the single closed loop, both batteries have their positive terminals connected towards the right. Tracing around the loop, the 12.0 V battery and the 8.0 V battery oppose each other.",
            "The net electromotive force around the loop is $E_\\text{net} = 12.0\\text{ V} - 8.0\\text{ V} = 4.0\\text{ V}$ in the direction driven by the larger 12.0 V battery.",
            "The total resistance of the series loop is the sum of the two internal resistances: $R_\\text{total} = 1.0\\ \\Omega + 0.5\\ \\Omega = 1.5\\ \\Omega$.",
            "The circuit current is $I = \\frac{E_\\text{net}}{R_\\text{total}} = \\frac{4.0\\text{ V}}{1.5\\ \\Omega} = 2.67\\text{ A} \\approx 2.7\\text{ A}$.",
            "Option B (4.0 A) divides 4.0 V by only 1.0 $\\Omega$. Option C (8.0 A) divides 4.0 V by only 0.5 $\\Omega$. Option D (13 A) mistakenly adds the two e.m.f.s ($\\Sigma E / \\Sigma R = 20.0\\text{ V} / 1.5\\ \\Omega \\approx 13.3\\text{ A}$)."
        ]
    },
    # Q36
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q36",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "circuit_analysis",
            "comparison"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_analyse_parallel_branch_resistance_change",
        "accepted_answer": "C",
        "hints": [
            "Determine how adding an identical resistor in parallel changes the equivalent external load resistance.",
            "Analyze the effect on total circuit current (ammeter) and on the terminal potential difference $V = E - Ir$ (voltmeter)."
        ],
        "walkthrough": [
            "Connecting a second identical resistor in parallel with $R$ reduces the equivalent external circuit resistance to $R_\\text{new} = \\frac{R}{2}$.",
            "The total circuit resistance is now $R_\\text{total} = \\frac{R}{2} + r$, which is lower than before. As a result, the total circuit current supplied by the cell $I = \\frac{E}{R_\\text{total}}$ increases, so the ammeter reading increases.",
            "The voltmeter measures the terminal potential difference $V = E - Ir$. Because the circuit current $I$ has increased, the internal potential drop ('lost volts' $Ir$) increases, which decreases the terminal potential difference $V$.",
            "Therefore, the ammeter reading increases and the voltmeter reading decreases.",
            "Options A and B incorrectly assume circuit current decreases. Option D overlooks the internal resistance of the cell, assuming terminal p.d. remains constant."
        ]
    },
    # Q37
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q37",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "circuit_analysis",
            "equation_derivation"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m02",
        "skill_id": "9702_skill_apply_kirchhoffs_second_law",
        "accepted_answer": "B",
        "hints": [
            "Apply Kirchhoff's second law ($\\Sigma E = \\Sigma IR$) to the closed loop formed by the two parallel resistor branches ($R_1, R_2$ and $R_3, R_4$).",
            "Trace clockwise around the loop, noting the directions of currents $I_1$ and $I_2$ and observing that no source of e.m.f. is enclosed in this inner loop."
        ],
        "walkthrough": [
            "Consider the closed inner loop composed exclusively of the two parallel resistor branches (left branch containing $R_1, R_2$ and right branch containing $R_3, R_4$).",
            "Because this closed loop does not include the battery, the net electromotive force around the loop is $\\Sigma E = 0$.",
            "Tracing clockwise around the loop: moving downwards through the left branch in the direction of $I_1$ gives potential changes $+I_1 R_1 + I_1 R_2 = +I_1(R_1 + R_2)$. Continuing upwards through the right branch opposite to $I_2$ gives potential changes $-I_2 R_4 - I_2 R_3 = -I_2(R_3 + R_4)$.",
            "By Kirchhoff's second law: $0 = I_1(R_1 + R_2) - I_2(R_3 + R_4)$.",
            "Option A has an incorrect plus sign between terms. Options C and D mistakenly incorporate the battery e.m.f. $E$ into a loop that does not pass through the battery branch."
        ]
    },
    # Q38
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q38",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "circuit_analysis",
            "direct_calculation"
        ],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m03",
        "skill_id": "9702_skill_apply_potentiometer_balance",
        "accepted_answer": "C",
        "hints": [
            "Find the resistance of the lower and upper sections of the potentiometer (total resistance $R_\\text{pot} = 120\\ \\Omega$) when the slider is $\\frac{1}{4}$ of the way from the lower end.",
            "For the voltmeter to read $0\\text{ V}$, the potential divider ratios in both parallel branches must be equal: $\\frac{R}{150\\ \\Omega} = \\frac{R_\\text{lower}}{R_\\text{upper}}$."
        ],
        "walkthrough": [
            "With the potentiometer slider at $\\frac{1}{4}$ of the distance from the lower end, the resistance of the lower segment is $R_\\text{lower} = \\frac{1}{4} \\times 120\\ \\Omega = 30\\ \\Omega$, and the upper segment is $R_\\text{upper} = \\frac{3}{4} \\times 120\\ \\Omega = 90\\ \\Omega$.",
            "A voltmeter reading of $0\\text{ V}$ signifies that the potential at the slider equals the potential at the junction between the 150 $\\Omega$ and $R$ resistors (Wheatstone bridge null condition).",
            "Equating the ratio of the lower to upper resistances in both branches gives $\\frac{R}{150\\ \\Omega} = \\frac{R_\\text{lower}}{R_\\text{upper}} = \\frac{30\\ \\Omega}{90\\ \\Omega} = \\frac{1}{3}$.",
            "Solving for $R$ yields $R = \\frac{150\\ \\Omega}{3} = 50\\ \\Omega$.",
            "Option A (30 $\\Omega$) is just the lower potentiometer segment. Option B (38 $\\Omega$) and Option D (450 $\\Omega$) come from taking $\\frac{90}{30} \\times 150 = 450\\ \\Omega$ (inverting the ratio)."
        ]
    },
    # Q39
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q39",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "explanation",
            "particle_model_application"
        ],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m01",
        "skill_id": "9702_skill_infer_atomic_structure_from_alpha_scattering",
        "accepted_answer": "C",
        "hints": [
            "Consider conservation of linear momentum and kinetic energy during an elastic collision between a small projectile and a heavy target.",
            "Compare the mass of an $\\alpha$-particle ($A = 4$) with the mass of a gold nucleus ($A = 197$)."
        ],
        "walkthrough": [
            "An $\\alpha$-particle has a mass of approximately $m_\\alpha \\approx 4\\text{ u}$, whereas a gold nucleus has a mass of approximately $M_\\text{Au} \\approx 197\\text{ u}$, which is nearly 50 times larger.",
            "In an elastic head-on collision of a light particle of mass $m$ with a stationary massive target of mass $M \\gg m$, the target's recoil velocity is $V_\\text{recoil} = \\left(\\frac{2m}{m + M}\\right)u_0 \\approx \\frac{2 \\times 4}{201}u_0 \\approx 0.04u_0$, while the light particle rebounds with speed $v \\approx -u_0$.",
            "Because the gold nucleus has a much greater mass than the $\\alpha$-particle ($M \\gg m$), it gains only a very small recoil velocity.",
            "Option A describes the nuclear atom cross-section (most foil is empty space), not the kinematic recoil speed. Option B describes the Coulomb force mechanism without explaining mass-dependent velocities. Option D is incorrect because kinetic energy and momentum are conserved in elastic scattering."
        ]
    },
    # Q40
    {
        "schema_version": "9702_p1_enrichment_v1",
        "question_id": "9702_s21_13_q40",
        "component": "P1",
        "difficulty": 2,
        "question_patterns": [
            "particle_model_application",
            "classification"
        ],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m02",
        "skill_id": "9702_skill_calculate_hadron_charge_from_quarks",
        "accepted_answer": "D",
        "hints": [
            "Recall the fractional electric charges of the individual quarks: up $u = +\\frac{2}{3}e$, down $d = -\\frac{1}{3}e$, and strange $s = -\\frac{1}{3}e$.",
            "Sum the three quark charges in each option to find which combination has a non-zero net charge."
        ],
        "walkthrough": [
            "The electric charges of the quarks are: $u = +\\frac{2}{3}e$, $d = -\\frac{1}{3}e$, and $s = -\\frac{1}{3}e$.",
            "Evaluating the net charge for each proposed three-quark combination:",
            "Option A (down, down, up): $q = -\\frac{1}{3} - \\frac{1}{3} + \\frac{2}{3} = 0$ (neutral baryon, e.g. neutron).",
            "Option B (down, up, strange): $q = -\\frac{1}{3} + \\frac{2}{3} - \\frac{1}{3} = 0$ (neutral baryon, e.g. $\\Lambda^0$ or $\\Sigma^0$).",
            "Option C (up, strange, strange): $q = +\\frac{2}{3} - \\frac{1}{3} - \\frac{1}{3} = 0$ (neutral baryon, e.g. $\\Xi^0$).",
            "Option D (up, up, strange): $q = +\\frac{2}{3} + \\frac{2}{3} - \\frac{1}{3} = +1e$ (charged baryon, e.g. $\\Sigma^+$).",
            "Since the question specifies that the hadron has a net electric charge, Option D is the only possible combination."
        ]
    }
]

out_dir = Path('subjects/physics/9702/enrichment/p1')
out_dir.mkdir(parents=True, exist_ok=True)

# First test for any PID artifacts or unbalanced dollars
for item in enrichment_data:
    qid = item['question_id']
    full_text = ' '.join(item['hints']) + ' ' + ' '.join(item['walkthrough'])
    dollar_count = full_text.count('$')
    assert dollar_count % 2 == 0, f"Unbalanced dollars in {qid}: {dollar_count}"
    pid_artifacts = re.findall(r'[\$]{1,2}\d{2,}', full_text)
    assert not pid_artifacts, f"PID artifacts in {qid}: {pid_artifacts}"

for item in enrichment_data:
    qid = item['question_id']
    fname = f"{qid}.enrichment.json"
    fpath = out_dir / fname
    fpath.write_text(json.dumps(item, indent=2, ensure_ascii=False) + "\n", encoding='utf-8')
    print(f"Wrote {fname}")

print(f"Done. Wrote {len(enrichment_data)} files successfully.")
