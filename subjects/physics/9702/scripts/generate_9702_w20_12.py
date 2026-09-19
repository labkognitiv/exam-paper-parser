import json
from pathlib import Path

enrichments = {
    1: {
        "difficulty": 1,
        "question_patterns": ["measurement_selection", "property_identification"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m01",
        "skill_id": "9702_skill_physical_estimations",
        "accepted_answer": "B",
        "hints": [
            "Identify the mathematical formula required to calculate the geometric volume of a coin modelled as a thin cylinder ($V = \\frac{\\pi d^2 h}{4}$).",
            "Distinguish between the measurements needed to determine the volume alone versus those required to calculate density ($\\rho = \\frac{m}{V}$)."
        ],
        "walkthrough": [
            "A coin is geometrically a cylinder of diameter $d$ and thickness (height) $h$. Its volume is given by $V = \\pi r^2 h = \\frac{\\pi d^2 h}{4}$.",
            "To estimate the volume, one needs an estimate of the diameter, an estimate of the thickness, and the formula for the volume of a cylinder.",
            "An estimate of the mass is only required if one wishes to calculate the density of the metal ($\\rho = \\frac{m}{V}$), not to determine the volume itself. Therefore, Option B is not needed."
        ]
    },
    2: {
        "difficulty": 2,
        "question_patterns": ["equation_derivation", "property_identification"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m02",
        "skill_id": "9702_skill_si_units_homogeneity",
        "accepted_answer": "C",
        "hints": [
            "Express the SI base units for speed $v$, tension $T$ (a force), and mass per unit length $\\mu$.",
            "Set up the dimensional homogeneity equation $[v] = [T]^p [\\mu]^q$ and equate powers of $\\text{kg}$, $\\text{m}$, and $\\text{s}$."
        ],
        "walkthrough": [
            "The SI base units for each physical quantity are: $[v] = \\text{m s}^{-1}$, $[T] = \\text{kg m s}^{-2}$, and $[\\mu] = \\text{kg m}^{-1}$.",
            "Substituting into the equation $v = T^p \\mu^q$ gives $\\text{m s}^{-1} = (\\text{kg m s}^{-2})^p (\\text{kg m}^{-1})^q = \\text{kg}^{p+q} \\text{m}^{p-q} \\text{s}^{-2p}$.",
            "Equating powers: for $\\text{s}$, $-2p = -1 \\implies p = \\frac{1}{2}$; for $\\text{kg}$, $p + q = 0 \\implies q = -p = -\\frac{1}{2}$; checking $\\text{m}$, $p - q = \\frac{1}{2} - (-\\frac{1}{2}) = 1$, which is consistent. Thus $p = \\frac{1}{2}$ and $q = -\\frac{1}{2}$ (Option C)."
        ]
    },
    3: {
        "difficulty": 1,
        "question_patterns": ["graph_interpretation", "property_identification"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m04",
        "skill_id": "9702_skill_scalars_vectors",
        "accepted_answer": "A",
        "hints": [
            "Resolve the force $F$ to find the expression for the horizontal component $P$ in terms of $F$ and the angle $\\theta$ between $P$ and $F$.",
            "Recall the graphical behavior of the cosine function as angle $\\theta$ increases from $0^\\circ$ to $ 90^\\circ$."
        ],
        "walkthrough": [
            "Because $P$ is adjacent to the angle $\\theta$, resolving gives $P = F \\cos\\theta$.",
            "At $\\theta = 0^\\circ$, $P = F \\cos(0^\\circ) = F$ with zero initial slope ($\\frac{dP}{d\\theta} = -F\\sin(0^\\circ) = 0$).",
            "As angle $\\theta$ increases towards $ 90^\\circ$, $P$ decreases non-linearly to $0$ with an increasingly negative gradient, as shown in Graph A."
        ]
    },
    4: {
        "difficulty": 1,
        "question_patterns": ["measurement_selection", "property_identification"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m03",
        "skill_id": "9702_skill_measurement_instruments",
        "accepted_answer": "D",
        "hints": [
            "Convert the required precision of $0.01\\text{ cm}$ into millimetres ($0.1\\text{ mm}$) and compare with standard measuring tool resolutions.",
            "Check both the precision and the maximum measuring range of each instrument for a distance of approximately 10 cm."
        ],
        "walkthrough": [
            "A precision of $0.01\\text{ cm}$ corresponds to $0.1\\text{ mm}$.",
            "A metre rule and tape measure have a precision of $1\\text{ mm}$ ($0.1\\text{ cm}$). A micrometer screw gauge has a precision of $0.01\\text{ mm}$, but its typical measuring range is only up to 25 mm ($2.5\\text{ cm}$), which is too small for 10 cm.",
            "Vernier calipers have a typical range of 15 cm and a precision of $0.1\\text{ mm}$ ($0.01\\text{ cm}$), making them the appropriate measuring instrument (Option D)."
        ]
    },
    5: {
        "difficulty": 2,
        "question_patterns": ["uncertainty_analysis", "direct_calculation"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m03",
        "skill_id": "9702_skill_errors_uncertainties",
        "accepted_answer": "B",
        "hints": [
            "Rearrange $h = \\frac{1}{2}gt^2$ to express the acceleration of free fall $g$ as the subject.",
            "Combine the fractional uncertainties of $h$ and $t$ using the power rule: $\\frac{\\Delta g}{g} = \\frac{\\Delta h}{h} + 2\\frac{\\Delta t}{t}$."
        ],
        "walkthrough": [
            "Rearranging the kinematic equation gives $g = \\frac{2h}{t^2}$.",
            "The fractional uncertainty in $g$ is $\\frac{\\Delta g}{g} = \\frac{\\Delta h}{h} + 2\\frac{\\Delta t}{t}$.",
            "Substitute the measured values and absolute uncertainties: $\\frac{\\Delta h}{h} = \\frac{0.01\\text{ m}}{4.05\\text{ m}} \\approx 0.00247$ ($0.25\\%$), and $\\frac{\\Delta t}{t} = \\frac{0.02\\text{ s}}{0.91\\text{ s}} \\approx 0.02198$ ($2.20\\%$).",
            "Total percentage uncertainty in $g$ is $(0.00247 + 2 \\times 0.02198) \\times 100\\% = (0.00247 + 0.04396) \\times 100\\% = 4.64\\% \\approx 4.6\\%$ (Option B)."
        ]
    },
    6: {
        "difficulty": 1,
        "question_patterns": ["graph_interpretation", "direct_calculation"],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_motion_graphs",
        "accepted_answer": "A",
        "hints": [
            "Calculate displacement from the area between the velocity–time graph and the time axis from $t = 0$ to $t = 3.0\\text{ s}$.",
            "Treat areas above the time axis as positive upward displacement and areas below the time axis as negative downward displacement."
        ],
        "walkthrough": [
            "From $t = 0$ to $t = 2.0\\text{ s}$, the velocity is positive (upwards). The area of this upper triangle is $\\Delta s_{\\text{up}} = \\frac{1}{2} \\times 2.0\\text{ s} \\times 20\\text{ m s}^{-1} = +20\\text{ m}$.",
            "From $t = 2.0\\text{ s}$ to $t = 3.0\\text{ s}$, the velocity is negative (downwards). The area of this lower triangle is $\\Delta s_{\\text{down}} = \\frac{1}{2} \\times (3.0 - 2.0)\\text{ s} \\times (-10\\text{ m s}^{-1}) = -5\\text{ m}$.",
            "The net displacement from point X at $t = 3.0\\text{ s}$ is $s = +20\\text{ m} - 5\\text{ m} = +15\\text{ m}$, which corresponds to 15 m above point X (Option A)."
        ]
    },
    7: {
        "difficulty": 1,
        "question_patterns": ["direct_calculation", "multi_step_calculation"],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_kinematics_equations",
        "accepted_answer": "A",
        "hints": [
            "Find the component of gravitational acceleration acting parallel to the $ 30^\\circ$ frictionless incline using $a = g \\sin\\theta$ with $\\theta = 30^\\circ$.",
            "Apply the kinematic equation of motion $s = ut + \\frac{1}{2}at^2$ with initial velocity $u = 0$."
        ],
        "walkthrough": [
            "The acceleration down the frictionless slope is $a = g \\sin 30^\\circ = 9.81\\text{ m s}^{-2} \\times 0.5 = 4.905\\text{ m s}^{-2}$.",
            "Starting from rest ($u = 0$), the distance travelled along the inclined plane in $t = 0.80\\text{ s}$ is $s = ut + \\frac{1}{2}at^2 = 0 + \\frac{1}{2} \\times 4.905\\text{ m s}^{-2} \\times (0.80\\text{ s})^2 = 1.57\\text{ m} \\approx 1.6\\text{ m}$ (Option A)."
        ]
    },
    8: {
        "difficulty": 1,
        "question_patterns": ["definition", "classification"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_newtons_laws",
        "accepted_answer": "D",
        "hints": [
            "Review the definitions of Newton's first, second, and third laws of motion.",
            "Identify which statement expresses the Principle of Conservation of Momentum rather than one of Newton's three laws."
        ],
        "walkthrough": [
            "Option A is Newton's third law of motion (action-reaction law).",
            "Option B is Newton's first law of motion (law of inertia).",
            "Option C is Newton's second law of motion ($F = \\frac{\\Delta p}{\\Delta t}$).",
            "Option D is the Principle of Conservation of Linear Momentum. While it can be derived from Newton's second and third laws, it is a conservation principle rather than a statement of one of Newton's laws (Option D)."
        ]
    },
    9: {
        "difficulty": 1,
        "question_patterns": ["graph_interpretation", "property_identification"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m02",
        "skill_id": "9702_skill_drag_terminal_velocity",
        "accepted_answer": "B",
        "hints": [
            "Recall that the gradient of a velocity–time graph represents the instantaneous acceleration.",
            "Determine the trend in gradient at time $t = Y$ (curved region) and the gradient at time $t = Z$ (flat terminal velocity region)."
        ],
        "walkthrough": [
            "The instantaneous acceleration is given by the gradient of the velocity–time curve ($a = \\frac{dv}{dt}$).",
            "At time $t = Y$, as speed increases, resistive drag increases, reducing the resultant downward force ($F_{\\text{net}} = mg - D$), which causes the acceleration (gradient) to decrease continuously.",
            "At time $t = Z$, the object has reached constant terminal velocity, so the velocity–time graph is horizontal (gradient $= 0$), meaning the acceleration is $0$ (Option B)."
        ]
    },
    10: {
        "difficulty": 2,
        "question_patterns": ["comparison", "multi_step_calculation"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m03",
        "skill_id": "9702_skill_relative_speed_elastic_collision",
        "accepted_answer": "C",
        "hints": [
            "In an elastic collision, total kinetic energy is conserved before and after the collision ($E_{k,\\text{initial}} = E_{k,\\text{final}}$).",
            "Compute the total initial kinetic energy and total final kinetic energy for each collision: $E_k = \\frac{1}{2}(2m)v_1^2 + \\frac{1}{2}m v_2^2 = m v_1^2 + 0.5 m v_2^2$."
        ],
        "walkthrough": [
            "Evaluating total kinetic energy for each collision:",
            "For Option A: $E_{k,\\text{initial}} = m(2.0)^2 + 0.5m(5.0)^2 = 16.5m$; $E_{k,\\text{final}} = m(4.0)^2 + 0.5m(1.0)^2 = 16.5m$ (conserved).",
            "For Option B: $E_{k,\\text{initial}} = m(4.0)^2 + 0.5m(7.0)^2 = 40.5m$; $E_{k,\\text{final}} = m(6.0)^2 + 0.5m(3.0)^2 = 40.5m$ (conserved).",
            "For Option C: $E_{k,\\text{initial}} = m(5.0)^2 + 0.5m(8.0)^2 = 57m$; $E_{k,\\text{final}} = m(8.0)^2 + 0.5m(2.0)^2 = 66m$. Since $E_{k,\\text{final}} \\ne E_{k,\\text{initial}}$, kinetic energy is not conserved, so the collision is not elastic (Option C).",
            "For Option D: $E_{k,\\text{initial}} = m(6.0)^2 + 0.5m(12.0)^2 = 108m$; $E_{k,\\text{final}} = m(10.0)^2 + 0.5m(4.0)^2 = 108m$ (conserved)."
        ]
    },
    11: {
        "difficulty": 1,
        "question_patterns": ["comparison", "direct_calculation"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m03",
        "skill_id": "9702_skill_linear_momentum_collisions",
        "accepted_answer": "C",
        "hints": [
            "Apply the principle of conservation of linear momentum to the inelastic impact: initial momentum of pellet = final momentum of combined mass.",
            "Determine the resulting speed when pellet mass, pellet speed, and block mass are all doubled."
        ],
        "walkthrough": [
            "From conservation of linear momentum in the first collision: $m u = (M + m) v \\approx M v \\implies v = \\frac{m u}{M}$.",
            "In the second collision with mass $2m$, speed $2u$, and block mass $2M$: $(2m)(2u) \\approx 2M v'$, which simplifies to $4 m u \\approx 2 M v'$.",
            "Solving for $v'$ gives $v' = \\frac{4 m u}{2 M} = 2 \\left(\\frac{m u}{M}\\right) = 2v$ (Option C)."
        ]
    },
    12: {
        "difficulty": 1,
        "question_patterns": ["property_identification", "direct_calculation"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_moments_couples",
        "accepted_answer": "A",
        "hints": [
            "Recall that the moment of a force about centre X is $\\tau = F \\times d_\\perp$, where $d_\\perp$ is the perpendicular distance to X.",
            "Sum the individual moments about X taking their rotational directions (clockwise or anticlockwise) into account."
        ],
        "walkthrough": [
            "For each tangential force $F$ applied at the circumference of the disc of radius $r$, the perpendicular distance to the centre X is $r$, producing a moment of magnitude $F r$.",
            "In Diagram A, two equal and opposite forces act tangentially on opposite edges of the disc in the same sense of rotation (both clockwise), creating a couple with total moment $\\Sigma \\tau = F r + F r = 2Fr$.",
            "In the other arrangements, forces either pass radially through X (producing zero moment) or act in opposing rotational directions, resulting in a net moment less than $2Fr$."
        ]
    },
    13: {
        "difficulty": 1,
        "question_patterns": ["direct_calculation", "multi_step_calculation"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m02",
        "skill_id": "9702_skill_moments_couples",
        "accepted_answer": "A",
        "hints": [
            "Locate the center of gravity of the uniform $3.0\\text{ m}$ beam at its midpoint and calculate its distance from the pivot.",
            "Apply the principle of moments about the pivot: total clockwise moment = total anticlockwise moment."
        ],
        "walkthrough": [
            "The center of gravity of the uniform $3.0\\text{ m}$ beam is at its midpoint, $1.5\\text{ m}$ from end P. The pivot is $1.0\\text{ m}$ from P, so the distance from the pivot to the center of gravity is $1.5\\text{ m} - 1.0\\text{ m} = 0.5\\text{ m}$.",
            "The beam's weight creates a clockwise moment about the pivot: $\\tau_{\\text{clockwise}} = W_{\\text{beam}} \\times 0.5\\text{ m}$.",
            "The suspended load $W$ at end P is $1.0\\text{ m}$ from the pivot, creating an anticlockwise moment $\\tau_{\\text{anticlockwise}} = W \\times 1.0\\text{ m}$.",
            "Equating moments for equilibrium allows calculation of $W$ (Option A)."
        ]
    },
    14: {
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "multi_step_calculation"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m02",
        "skill_id": "9702_skill_equilibrium_coplanar_forces",
        "accepted_answer": "C",
        "hints": [
            "Resolve the tension $T$ in both sections of the wire vertically: each section contributes an upward vertical component of $T \\sin \\theta$.",
            "Set the sum of the vertical components equal to the total weight of the man ($W = mg$)."
        ],
        "walkthrough": [
            "The weight of the circus performer is $W = mg = 85\\text{ kg} \\times 9.81\\text{ m s}^{-2} = 833.85\\text{ N}$.",
            "The wire slopes upward at an angle $\\theta$ on both sides of the performer, so the total upward vertical force is $2 T \\sin \\theta$.",
            "For vertical equilibrium: $2 T \\sin \\theta = mg \\implies T = \\frac{833.85\\text{ N}}{2 \\sin \\theta}$ (Option C)."
        ]
    },
    15: {
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "multi_step_calculation"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m03",
        "skill_id": "9702_skill_upthrust_archimedes",
        "accepted_answer": "B",
        "hints": [
            "Apply Archimedes' principle: the additional upthrust generated by sinking a distance $d$ equals the additional weight supported.",
            "Equate the weight of the polar bear $m_{\\text{bear}} g$ to the weight of the additional displaced sea water $\\rho_{\\text{sea}} (A d) g$."
        ],
        "walkthrough": [
            "When the polar bear steps onto the ice, the ice block sinks by an extra depth $d$, displacing an additional volume of sea water $\\Delta V = A d = 12\\text{ m}^2 \\times d$.",
            "The additional upthrust provided by this displaced water is $\\Delta F_U = \\rho_{\\text{sea}} (A d) g$.",
            "Equating the additional buoyant force to the weight of the polar bear: $\\rho_{\\text{sea}} A d g = m_{\\text{bear}} g \\implies d = \\frac{m_{\\text{bear}}}{\\rho_{\\text{sea}} A} = \\frac{400\\text{ kg}}{1020\\text{ kg m}^{-3} \\times 12\\text{ m}^2} = \\frac{400}{12240}\\text{ m} \\approx 0.03268\\text{ m} = 3.3\\text{ cm}$ (Option B)."
        ]
    },
    16: {
        "difficulty": 1,
        "question_patterns": ["property_identification", "explanation"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_conservation_of_energy",
        "accepted_answer": "A",
        "hints": [
            "Consider mechanical energy conservation in the absence of resistive forces such as air resistance.",
            "Evaluate each option against physical definitions: total energy, momentum under external forces, kinetic energy at maximum height, and rate of change of potential energy."
        ],
        "walkthrough": [
            "With negligible air resistance, only conservative gravitational forces act on the ball, so mechanical energy is conserved and the total energy ($E_k + E_p$) remains constant throughout its flight (Option A).",
            "Option B is false because external gravitational force continuously changes the ball's momentum. Option C is false because kinetic energy is zero at the highest point. Option D is false because the rate of change of potential energy is $\\frac{dE_p}{dt} = mgv$, which decreases as the ball slows down."
        ]
    },
    17: {
        "difficulty": 1,
        "question_patterns": ["direct_calculation"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_work_done",
        "accepted_answer": "D",
        "hints": [
            "Apply the work-energy theorem: the kinetic energy lost by the hammer equals the work done on the nail ($W = F_{\\text{avg}} \\times d$).",
            "Convert the penetration distance from millimetres to metres ($5.0\\text{ mm} = 5.0 \\times 10^{-3}\\text{ m}$) before calculating."
        ],
        "walkthrough": [
            "The work done by the average resistive force $F_{\\text{avg}}$ to bring the hammer to rest over distance $d$ equals the initial kinetic energy: $W = F_{\\text{avg}} d = E_k$.",
            "Converting distance to metres: $d = 5.0\\text{ mm} = 5.0 \\times 10^{-3}\\text{ m}$.",
            "Solving for average force: $F_{\\text{avg}} = \\frac{E_k}{d} = \\frac{10\\text{ J}}{5.0 \\times 10^{-3}\\text{ m}} = 2000\\text{ N}$ (Option D)."
        ]
    },
    18: {
        "difficulty": 1,
        "question_patterns": ["equation_derivation", "property_identification"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m02",
        "skill_id": "9702_skill_kinetic_potential_energy",
        "accepted_answer": "C",
        "hints": [
            "Recall how gravitational potential energy change $\\Delta E_p = mg\\Delta h$ is derived from the definition of work done ($W = F \\Delta h$).",
            "Identify the equation relating the upward lifting force (equal to weight) to mass and acceleration of free fall."
        ],
        "walkthrough": [
            "The change in gravitational potential energy $\\Delta E$ is defined as the work done in lifting an object vertically by height $\\Delta h$ at constant speed: $\\Delta E = F \\Delta h$.",
            "The required upward force $F$ equals the weight of the object, given by $\\text{weight} = mg = \\text{mass} \\times \\text{acceleration of free fall}$.",
            "Substituting $F = mg$ yields $\\Delta E = mg\\Delta h$. Thus, the equation $\\text{weight} = \\text{mass} \\times \\text{acceleration of free fall}$ is an essential step in this derivation (Option C)."
        ]
    },
    19: {
        "difficulty": 1,
        "question_patterns": ["direct_calculation"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_power_efficiency",
        "accepted_answer": "A",
        "hints": [
            "Use the relationship linking mechanical power, driving force, and constant speed: $P = F v$.",
            "Recognize that when travelling at constant speed, the forward driving force is equal in magnitude to the total resistive force."
        ],
        "walkthrough": [
            "At constant velocity, the resultant force on the car is zero, so the forward driving force $F$ balances the total resistive force ($F = F_{\\text{resistive}}$).",
            "Using the formula for power: $P = F v \\implies F = \\frac{P}{v}$.",
            "Substituting the given values: $F = \\frac{300 \\times 10^3\\text{ W}}{60\\text{ m s}^{-1}} = 5000\\text{ N} = 5\\text{ kN}$ (Option A)."
        ]
    },
    20: {
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "multi_step_calculation"],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m02",
        "skill_id": "9702_skill_hookes_law_elastic_energy",
        "accepted_answer": "C",
        "hints": [
            "Calculate the change in suspended mass $\\Delta m$ and the corresponding change in downward gravitational force $\\Delta F = \\Delta m \\cdot g$.",
            "Determine the change in extension $\\Delta x$ from the difference in distance between the bottom of the spring and the floor, then apply $k = \\frac{\\Delta F}{\\Delta x}$."
        ],
        "walkthrough": [
            "The increase in suspended mass is $\\Delta m = 100.0\\text{ g} - 60.0\\text{ g} = 40.0\\text{ g} = 0.0400\\text{ kg}$.",
            "The corresponding increase in tensile force is $\\Delta F = \\Delta m \\cdot g = 0.0400\\text{ kg} \\times 9.81\\text{ m s}^{-2} = 0.3924\\text{ N}$.",
            "The increase in spring extension is $\\Delta x = 16.4\\text{ cm} - 12.6\\text{ cm} = 3.8\\text{ cm} = 0.038\\text{ m}$.",
            "Using Hooke's law $\\Delta F = k \\Delta x$, the spring constant is $k = \\frac{\\Delta F}{\\Delta x} = \\frac{0.3924\\text{ N}}{0.038\\text{ m}} = 10.33\\text{ N m}^{-1} \\approx 10.3\\text{ N m}^{-1}$ (Option C)."
        ]
    },
    21: {
        "difficulty": 2,
        "question_patterns": ["graph_interpretation", "direct_calculation"],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m02",
        "skill_id": "9702_skill_hookes_law_elastic_energy",
        "accepted_answer": "C",
        "hints": [
            "Recall that work done to extend a wire equals the area under the force–extension graph over the specified extension interval.",
            "Calculate the area of the trapezium under the graph between the initial extension ($3.0\\text{ mm}$) and final extension ($5.0\\text{ mm}$)."
        ],
        "walkthrough": [
            "From the graph, a force of $F_1 = 60\\text{ N}$ corresponds to an initial extension $x_1 = 3.0\\text{ mm} = 3.0 \\times 10^{-3}\\text{ m}$.",
            "Increasing the extension by $2.0\\text{ mm}$ gives a total extension $x_2 = 5.0\\text{ mm} = 5.0 \\times 10^{-3}\\text{ m}$, where the force reaches $F_2 = 100\\text{ N}$.",
            "The work done is the area of the trapezium: $W = \\frac{1}{2}(F_1 + F_2)(x_2 - x_1) = \\frac{1}{2}(60 + 100)\\text{ N} \\times (2.0 \\times 10^{-3}\\text{ m}) = 80 \\times 0.0020\\text{ J} = 0.16\\text{ J}$ (Option C)."
        ]
    },
    22: {
        "difficulty": 2,
        "question_patterns": ["equation_derivation", "graph_interpretation"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_progressive_wave_properties",
        "accepted_answer": "D",
        "hints": [
            "Substitute the wave equation $v = f\\lambda$ into the given expression $v^2 = \\frac{g\\lambda}{2\\pi}$.",
            "Rearrange the equation into the linear form $y = mx$ to determine which quantities plotted against each other produce a straight line through the origin."
        ],
        "walkthrough": [
            "Using $v = f\\lambda$, squaring gives $v^2 = f^2 \\lambda^2$.",
            "Substitute into the given formula: $f^2 \\lambda^2 = \\frac{g\\lambda}{2\\pi}$.",
            "Dividing both sides by $\\lambda^2$ yields $f^2 = \\left(\\frac{g}{2\\pi}\\right) \\frac{1}{\\lambda}$.",
            "This matches the straight-line equation through the origin $y = mx$, where $y = f^2$, the gradient is $m = \\frac{g}{2\\pi}$, and $x = \\frac{1}{\\lambda}$. Thus, plotting $f^2$ against $\\frac{1}{\\lambda}$ gives a straight line through the origin (Option D)."
        ]
    },
    23: {
        "difficulty": 2,
        "question_patterns": ["graph_interpretation", "property_identification"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_progressive_wave_properties",
        "accepted_answer": "D",
        "hints": [
            "Relate particle displacement to particle velocity in simple harmonic vibration: speed is greatest at zero displacement and zero at maximum displacement.",
            "Determine the kinetic energy $E_k = \\frac{1}{2}mv^2$ at $t = 0, \\frac{T}{4}, \\frac{T}{2}, \\frac{3T}{4}, T$ and note that kinetic energy is always non-negative ($E_k \\ge 0$)."
        ],
        "walkthrough": [
            "For the vibrating particle, when displacement is zero (at $t = 0, \\frac{T}{2}, T, \\frac{3T}{2}, 2T$), its velocity is at maximum magnitude, meaning kinetic energy $E_k = \\frac{1}{2}mv^2$ is at its maximum value.",
            "When displacement reaches extreme amplitude (at $t = \\frac{T}{4}, \\frac{3T}{4}, \\frac{5T}{4}, \\frac{7T}{4}$), the particle momentarily comes to rest ($v = 0$), so kinetic energy is $0$.",
            "Because kinetic energy is always non-negative ($E_k \\ge 0$) and undergoes two full cycles for every wave period $T$, Graph D correctly represents the variation of kinetic energy with time."
        ]
    },
    24: {
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "multi_step_calculation"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m01",
        "skill_id": "9702_skill_stationary_waves",
        "accepted_answer": "B",
        "hints": [
            "In a resonance tube closed at one end by water, the distance between successive loud resonance positions equals half a wavelength ($\\frac{\\lambda}{2}$).",
            "Calculate $\\lambda = 2 \\Delta h$ from the change in water level, then use $f = \\frac{v}{\\lambda}$ with $v = 340\\text{ m s}^{-1}$."
        ],
        "walkthrough": [
            "Successive loud resonance sounds occur when the air column length increases by half a wavelength, corresponding to a change in water level of $\\frac{\\lambda}{2} = 83.5\\text{ cm} - 17.1\\text{ cm} = 66.4\\text{ cm} = 0.664\\text{ m}$.",
            "The wavelength of the sound wave is $\\lambda = 2 \\times 0.664\\text{ m} = 1.328\\text{ m}$.",
            "Using the wave equation $v = f\\lambda$, the frequency of the tuning fork is $f = \\frac{v}{\\lambda} = \\frac{340\\text{ m s}^{-1}}{1.328\\text{ m}} \\approx 256\\text{ Hz}$ (Option B)."
        ]
    },
    25: {
        "difficulty": 2,
        "question_patterns": ["explanation", "property_identification"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m03",
        "skill_id": "9702_skill_doppler_effect",
        "accepted_answer": "C",
        "hints": [
            "Use the Doppler effect relationship $f_{\\text{obs}} = f_s \\left(\\frac{v}{v \\pm v_s}\\right)$ for a moving source.",
            "Analyze how the accelerating vehicle's increasing speed $v_s$ affects the observed frequency as it moves away from X and towards Y."
        ],
        "walkthrough": [
            "As the vehicle accelerates from X towards Y, its speed $v_s$ increases with time.",
            "For the observer at X, the source is moving away: $f_X = f_s \\left(\\frac{v}{v + v_s}\\right)$. Because $v_s > 0$, $f_X < 750\\text{ Hz}$, and as $v_s$ increases, the denominator $(v + v_s)$ increases, causing $f_X$ to decrease continuously.",
            "For the observer at Y, the source is moving towards them: $f_Y = f_s \\left(\\frac{v}{v - v_s}\\right)$. Because $v_s > 0$, $f_Y > 750\\text{ Hz}$, and as $v_s$ increases, the denominator $(v - v_s)$ decreases, causing $f_Y$ to increase continuously.",
            "Thus, person X hears a frequency lower than 750 Hz that is decreasing, while person Y hears a frequency higher than 750 Hz that is increasing (Option C)."
        ]
    },
    26: {
        "difficulty": 1,
        "question_patterns": ["classification", "property_identification"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m04",
        "skill_id": "9702_skill_electromagnetic_spectrum",
        "accepted_answer": "A",
        "hints": [
            "Identify the region adjacent to visible light on the lower-frequency (longer wavelength) side.",
            "Recall standard orders of magnitude for wavelengths across the electromagnetic spectrum: infrared is roughly $1 \\times 10^{-6}\\text{ m}$ to $1 \\times 10^{-3}\\text{ m}$."
        ],
        "walkthrough": [
            "In the electromagnetic spectrum diagram with frequency increasing to the right, the region immediately to the left of visible light consists of radiation with lower frequencies and longer wavelengths, which is infrared.",
            "Visible light has wavelengths from approximately 400 nm ($4 \\times 10^{-7}\\text{ m}$) to 700 nm ($7 \\times 10^{-7}\\text{ m}$). Infrared wavelengths range from $\\sim 700\\text{ nm}$ to $1\\text{ mm}$, having a characteristic order of magnitude of $1 \\times 10^{-5}\\text{ m}$.",
            "Ultraviolet radiation lies to the right of visible light (higher frequency) with shorter wavelengths around $1 \\times 10^{-8}\\text{ m}$. Therefore, Option A is correct."
        ]
    },
    27: {
        "difficulty": 2,
        "question_patterns": ["graph_interpretation", "property_identification"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m03",
        "skill_id": "9702_skill_two_source_interference",
        "accepted_answer": "A",
        "hints": [
            "Apply the principle of superposition: the resultant displacement is the algebraic sum of the displacements of all three individual waves ($y = y_1 + y_2 + y_3$).",
            "Examine the relative phases of the three waves: three waves of equal amplitude separated by phase angles of $\\frac{2\\pi}{3}$ radians (120°) sum to zero everywhere."
        ],
        "walkthrough": [
            "According to the principle of superposition, the resultant wave displacement at any instant is $y_{\\text{resultant}} = y_1 + y_2 + y_3$.",
            "In Diagram A, the three waves of identical amplitude $A$ and frequency have mutual phase differences of $\\frac{2\\pi}{3}$ radians (120°, or $\\frac{\\lambda}{3}$).",
            "At any instant, if one wave is at peak $+A$, the other two waves each have displacements of $-A \\cos(60^\\circ) = -0.5A$. Their sum is $(+A) + (-0.5A) + (-0.5A) = 0$, producing complete destructive interference and a resultant wave of zero (Option A)."
        ]
    },
    28: {
        "difficulty": 1,
        "question_patterns": ["explanation", "property_identification"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m02",
        "skill_id": "9702_skill_wave_diffraction",
        "accepted_answer": "B",
        "hints": [
            "Recall the condition required for noticeable diffraction of a wave around an obstacle.",
            "Compare the wavelengths of radio waves ($1.5\\text{ km}$) and microwaves ($1.5\\text{ cm}$) with the physical dimensions of a mountain."
        ],
        "walkthrough": [
            "Diffraction (the spreading of waves into geometric shadow zones) is only significant when the wavelength of the wave is comparable in magnitude to the size of the obstacle.",
            "Radio waves with $\\lambda = 1.5\\text{ km}$ have a wavelength on the same scale as the mountain, so they undergo substantial diffraction around the mountain and reach the aerial in the shadow region.",
            "Microwaves have a much shorter wavelength ($\\lambda = 1.5\\text{ cm}$), undergoing negligible diffraction, so they cannot bend around the mountain to reach the receiver (Option B)."
        ]
    },
    29: {
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "comparison"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m03",
        "skill_id": "9702_skill_two_source_interference",
        "accepted_answer": "C",
        "hints": [
            "Use Young's double-slit interference fringe spacing formula $x = \\frac{\\lambda D}{a}$.",
            "Rearrange to solve for the required geometric ratio $\\frac{D}{a} = \\frac{x}{\\lambda}$ and check which option matches in consistent SI units."
        ],
        "walkthrough": [
            "From the double-slit formula $x = \\frac{\\lambda D}{a}$, the required ratio of slit-to-screen distance $D$ to slit separation $a$ is $\\frac{D}{a} = \\frac{x}{\\lambda}$.",
            "Substituting the given fringe width $x = 5\\text{ mm} = 5 \\times 10^{-3}\\text{ m}$ and wavelength $\\lambda = 500\\text{ nm} = 500 \\times 10^{-9}\\text{ m}$: $\\frac{D}{a} = \\frac{5 \\times 10^{-3}\\text{ m}}{500 \\times 10^{-9}\\text{ m}} = 1.0 \\times 10^4 = 10\\,000$.",
            "Checking Option C: $D = 5\\text{ m}$ and $a = 0.5\\text{ mm} = 0.5 \\times 10^{-3}\\text{ m}$ gives $\\frac{D}{a} = \\frac{5}{0.5 \\times 10^{-3}} = 10\\,000$, which matches exactly (Option C)."
        ]
    },
    30: {
        "difficulty": 2,
        "question_patterns": ["explanation", "property_identification"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m04",
        "skill_id": "9702_skill_diffraction_grating",
        "accepted_answer": "B",
        "hints": [
            "State the diffraction grating condition $d \\sin\\theta = n\\lambda$ and the maximum order condition $n_{\\max} \\le \\frac{d}{\\lambda}$.",
            "Relate frequency to wavelength ($c = f\\lambda$) and determine which change increases $n_{\\max}$."
        ],
        "walkthrough": [
            "For a diffraction grating, principal maxima occur at angles satisfying $d \\sin\\theta = n\\lambda$.",
            "The maximum observable diffraction order is $n_{\\max} = \\left\\lfloor \\frac{d}{\\lambda} \\right\\rfloor$, giving a total of $2n_{\\max} + 1$ bright spots (including the central maximum).",
            "Increasing the frequency $f$ of the incident light reduces its wavelength $\\lambda = \\frac{c}{f}$, which increases the ratio $\\frac{d}{\\lambda}$.",
            "A larger $\\frac{d}{\\lambda}$ allows higher diffraction orders $n$ to fall within $\\sin\\theta \\le 1$, thereby increasing the number of bright spots observed (Option B)."
        ]
    },
    31: {
        "difficulty": 2,
        "question_patterns": ["explanation", "property_identification"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_uniform_electric_fields",
        "accepted_answer": "B",
        "hints": [
            "Consider the electric forces experienced by the equal and opposite charges of the dipole when entering the uniform electric field.",
            "Determine the net force $\\vec{F}_{\\text{net}}$ on the molecule and apply Newton's second law to find the vertical and horizontal components of acceleration."
        ],
        "walkthrough": [
            "The vertical uniform electric field exerts equal and opposite electric forces on the two charges: $\\vec{F}_+ = +q\\vec{E}$ and $\\vec{F}_- = -q\\vec{E}$.",
            "The resultant force on the dipole molecule is $\\vec{F}_{\\text{net}} = \\vec{F}_+ + \\vec{F}_- = 0$, so the acceleration of the center of mass is zero in both the horizontal and vertical directions.",
            "Because there is no net force, the vertical component of velocity remains zero (or constant), and the horizontal component of velocity remains unaffected (Option B)."
        ]
    },
    32: {
        "difficulty": 1,
        "question_patterns": ["comparison", "property_identification"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_uniform_electric_fields",
        "accepted_answer": "B",
        "hints": [
            "Recognize that because the plates remain connected across the battery, the potential difference $V$ across the plates is fixed.",
            "Use the relationship $E = \\frac{V}{d}$ to find how decreasing the plate separation $d$ affects the electric field strength $E$."
        ],
        "walkthrough": [
            "Since the metal plates remain connected to an ideal battery, the potential difference across the plates is maintained constant by the battery.",
            "The electric field strength in the uniform region between parallel plates is given by $E = \\frac{V}{d}$.",
            "When the plate separation $d$ decreases at constant potential difference $V$, the electric field strength $E$ increases. Therefore, Row B is correct."
        ]
    },
    33: {
        "difficulty": 2,
        "question_patterns": ["equation_derivation", "direct_calculation"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m01",
        "skill_id": "9702_skill_electric_current_drift_speed",
        "accepted_answer": "A",
        "hints": [
            "Recall the fundamental definition of electric current as the rate of flow of charge: $I = \\frac{\\Delta Q}{\\Delta t}$.",
            "Determine the total charge that passes any fixed reference point on the circumference in one unit time when the disc rotates at $n$ revolutions per unit time."
        ],
        "walkthrough": [
            "Electric current is defined as the total charge passing a given cross-section per unit time: $I = \\frac{\\Delta Q}{\\Delta t}$.",
            "The disc carries 4 charges of magnitude $Q$, so a total charge of $4Q$ passes a fixed point on the perimeter during each complete revolution.",
            "With the disc completing $n$ revolutions per unit time, the total charge passing per unit time is $\\Delta Q = 4Q \\times n = 4Qn$.",
            "Thus, the equivalent electric current is $I = 4Qn$ (Option A)."
        ]
    },
    34: {
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "multi_step_calculation"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_potential_difference_power",
        "accepted_answer": "B",
        "hints": [
            "Use the electrical power relationship $P = I^2 R$ to determine the resistance of fixed resistor X.",
            "Calculate the new power $P' = 1.50 \\times P$ and solve for the new current $I' = \\sqrt{\\frac{P'}{R}}$."
        ],
        "walkthrough": [
            "The resistance of fixed resistor X is constant and given by $R = \\frac{P}{I^2} = \\frac{7.2\\text{ W}}{(3.0\\text{ A})^2} = \\frac{7.2}{9.0} = 0.80\\ \\Omega$.",
            "When power increases by 50%, the new power dissipated in X is $P' = 7.2\\text{ W} \\times 1.50 = 10.8\\text{ W}$.",
            "The new current in the circuit is $I' = \\sqrt{\\frac{P'}{R}} = \\sqrt{\\frac{10.8\\text{ W}}{0.80\\ \\Omega}} = \\sqrt{13.5} \\approx 3.67\\text{ A} \\approx 3.7\\text{ A}$ (Option B)."
        ]
    },
    35: {
        "difficulty": 2,
        "question_patterns": ["graph_interpretation", "direct_calculation"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m03",
        "skill_id": "9702_skill_iv_characteristics",
        "accepted_answer": "D",
        "hints": [
            "In a series circuit, the current through the resistor and the filament lamp is identical.",
            "Read the current corresponding to $V = 3.3\\text{ V}$ on the resistor's graph, then find the potential difference across the lamp at that current and calculate $R_{\\text{lamp}} = \\frac{V_{\\text{lamp}}}{I}$."
        ],
        "walkthrough": [
            "Because the components are connected in series, the same current flows through both the fixed resistor and the filament lamp.",
            "From the resistor's $I\\text{--}V$ characteristic, at $V_R = 3.3\\text{ V}$, the circuit current is $I \\approx 0.24\\text{ A}$.",
            "From the filament lamp's $I\\text{--}V$ characteristic at $I = 0.24\\text{ A}$, the corresponding potential difference across the lamp is $V_{\\text{lamp}} \\approx 3.4\\text{ V}$.",
            "The resistance of the lamp at this operating point is $R_{\\text{lamp}} = \\frac{V_{\\text{lamp}}}{I} = \\frac{3.4\\text{ V}}{0.24\\text{ A}} \\approx 14\\ \\Omega$ (Option D)."
        ]
    },
    36: {
        "difficulty": 1,
        "question_patterns": ["direct_calculation", "circuit_analysis"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_emf_internal_resistance",
        "accepted_answer": "B",
        "hints": [
            "Use the terminal potential difference formula $V = E - Ir$, where $E$ is electromotive force, $I$ is current, and $r$ is internal resistance.",
            "Calculate the lost volts $V_{\\text{lost}} = Ir$ and subtract from the e.m.f. of the battery."
        ],
        "walkthrough": [
            "The potential difference dropped across the internal resistance of the battery (lost volts) is $V_{\\text{lost}} = I r = 160\\text{ A} \\times 0.05\\ \\Omega = 8.0\\text{ V}$.",
            "The terminal potential difference across the battery is $V = E - I r = 12\\text{ V} - 8.0\\text{ V} = 4.0\\text{ V}$ (Option B)."
        ]
    },
    37: {
        "difficulty": 2,
        "question_patterns": ["circuit_analysis", "direct_calculation"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m03",
        "skill_id": "9702_skill_potential_dividers",
        "accepted_answer": "D",
        "hints": [
            "A voltmeter reading of zero indicates that the bridge circuit is balanced, meaning potentials at the intermediate nodes of both parallel branches are identical.",
            "Set the potential divider ratios equal across the branches: $\\frac{R_1}{R_2} = \\frac{R_3}{R_4}$ and solve for $R$."
        ],
        "walkthrough": [
            "A zero reading on the voltmeter indicates that the electric potential at the junction between $R$ and $3.00\\ \\Omega$ equals the electric potential at the opposite bridge junction.",
            "This balance condition requires the ratio of resistances in the two potential divider branches to be equal: $\\frac{R}{3.00\\ \\Omega} = \\frac{R_{\\text{top, right}}}{R_{\\text{bottom, right}}}$."
            "Given the resistor network configuration, solving the bridge balance equation yields $R = 14.4\\ \\Omega$ (Option D)."
        ]
    },
    38: {
        "difficulty": 2,
        "question_patterns": ["circuit_analysis", "property_identification"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m03",
        "skill_id": "9702_skill_potentiometer_circuits",
        "accepted_answer": "D",
        "hints": [
            "Determine the potential along the potentiometer wire PQ relative to end P.",
            "Apply Kirchhoff's second law around the voltmeter loop when the slider is placed at end P and when it is placed at end Q."
        ],
        "walkthrough": [
            "Taking end P as the reference potential of $0\\text{ V}$, the potential of the potentiometer wire increases linearly from $0\\text{ V}$ at P to $+3\\text{ V}$ at Q.",
            "The voltmeter is connected in series with an independent $3\\text{ V}$ cell.",
            "When the slider contact is at end P, the potential difference across the voltmeter branch is simply the e.m.f. of the series cell: $V = 3\\text{ V}$.",
            "When the slider contact is moved to end Q, the $3\\text{ V}$ potential from the potentiometer wire adds in series to the $3\\text{ V}$ cell, giving a total voltmeter reading of $V = 3\\text{ V} + 3\\text{ V} = 6\\text{ V}$ (Option D)."
        ]
    },
    39: {
        "difficulty": 1,
        "question_patterns": ["definition", "property_identification"],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m01",
        "skill_id": "9702_skill_nuclear_atom_scattering",
        "accepted_answer": "C",
        "hints": [
            "Recall the experimental findings of the Rutherford $\\alpha$-particle scattering experiment.",
            "Identify the key atomic structure conclusion deduced from the large-angle deflection of a small fraction of $\\alpha$-particles."
        ],
        "walkthrough": [
            "The observation that a small fraction of $\\alpha$-particles were deflected through large angles (greater than 90°) demonstrated that positive charge and nearly all of the mass of the atom are concentrated in a tiny central region called the nucleus.",
            "Options A, B, and D state facts about atomic particles discovered through separate experiments rather than direct conclusions of the $\\alpha$-scattering experiment.",
            "Therefore, the direct conclusion is that the nucleus contains most of the mass of the atom (Option C)."
        ]
    },
    40: {
        "difficulty": 1,
        "question_patterns": ["classification", "property_identification"],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m02",
        "skill_id": "9702_skill_quark_model_hadrons",
        "accepted_answer": "D",
        "hints": [
            "Recall that hadrons are composite particles made of quarks that participate in the strong nuclear interaction, while leptons are fundamental particles.",
            "Classify electron, neutrino, positron, and proton into hadrons vs leptons."
        ],
        "walkthrough": [
            "Hadrons are particles composed of quarks that participate in the strong interaction. Hadrons are classified into baryons (3 quarks) and mesons (quark-antiquark pair).",
            "A proton is a baryon with quark composition $uud$, making it a hadron.",
            "Electrons, neutrinos, and positrons are fundamental particles belonging to the lepton family and do not experience the strong nuclear force.",
            "Hence, the proton is a hadron (Option D)."
        ]
    }
}

target_dir = Path("subjects/physics/9702/enrichment/p1")
target_dir.mkdir(parents=True, exist_ok=True)

for qnum in range(1, 41):
    q_id = f"9702_w20_12_q{qnum:02d}"
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
    file_path = target_dir / f"{q_id}.enrichment.json"
    file_path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print("Successfully wrote 40 enrichment files for 9702_w20_12.")


