import json
from pathlib import Path

TARGET_DIR = Path('subjects/physics/9702/enrichment/p1')
TARGET_DIR.mkdir(parents=True, exist_ok=True)

ENRICHMENTS = [
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q01",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "definition",
      "property_identification"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m01",
    "skill_id": "9702_skill_si_units_homogeneity",
    "accepted_answer": "C",
    "hints": [
      "Consider what two essential components are fundamentally required to define any measurement of a physical quantity.",
      "A physical quantity does not strictly have to be in base units or SI units, nor does it require scientific notation, but it must have a numerical value and a unit."
    ],
    "walkthrough": [
      "By definition in physics, every physical quantity consists of a numerical magnitude (a number) and an appropriate unit (e.g. 5 m, 20 s, 30 N). Thus, option C is correct.",
      "Options A and D are incorrect because units do not have to be base units or SI units (non-SI and derived units are also valid). Option B is incorrect because expressing the magnitude in standard form is convenient but not strictly necessary to define a physical quantity."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q02",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "direct_calculation",
      "property_identification"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m02",
    "skill_id": "9702_skill_si_units_homogeneity",
    "accepted_answer": "D",
    "hints": [
      "Apply Ohm's law $V = IR$ and convert all metric prefixes ($\\text{m} = 10^{-3}$, $\\mu = 10^{-6}$, $\\text{k} = 10^3$, $\\text{M} = 10^6$) to standard SI units.",
      "Calculate the product $I \\times R$ for each pair of options to find which one yields exactly $3.6\\text{ V}$."
    ],
    "walkthrough": [
      "Using Ohm's law $V = I \\times R$, we evaluate each option with prefix multipliers: For option D: $I = 15\\text{ }\\mu\\text{A} = 15 \\times 10^{-6}\\text{ A}$ and $R = 240\\text{ k}\\Omega = 240 \\times 10^3\\text{ }\\Omega$. The potential difference is $V = (15 \\times 10^{-6}\\text{ A}) \\times (240 \\times 10^3\\text{ }\\Omega) = 3.6\\text{ V}$, which matches the reading.",
      "Checking the distractors: For A, $V = 150 \\times 10^{-3} \\times 240 = 36\\text{ V}$. For B, $V = 15 \\times 10^{-3} \\times 2400 = 36\\text{ V}$. For C, $V = 1.5 \\times 10^{-3} \\times 240000 = 360\\text{ V}$. None of these equal $3.6\\text{ V}$."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q03",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "uncertainty_analysis",
      "direct_calculation"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m03",
    "skill_id": "9702_skill_errors_uncertainties",
    "accepted_answer": "C",
    "hints": [
      "For a relationship of the form $g = \\frac{2s}{t^2}$, write down the fractional or percentage uncertainty rule for power relationships and quotients.",
      "Constant factors like $2$ carry no uncertainty. The percentage uncertainty in $g$ is $\\frac{\\Delta g}{g} = \\frac{\\Delta s}{s} + 2\\left(\\frac{\\Delta t}{t}\\right)$."
    ],
    "walkthrough": [
      "From the formula $g = \\frac{2s}{t^2}$, the constant multiplier $2$ has zero uncertainty. Applying the rules for combining percentage uncertainties: $\\frac{\\Delta g}{g} \\times 100\\% = \\left(\\frac{\\Delta s}{s} \\times 100\\%\\right) + 2 \\left(\\frac{\\Delta t}{t} \\times 100\\%\\right)$.",
      "Substituting the given values: $\\frac{\\Delta g}{g} = 2\\% + 2(3\\%) = 2\\% + 6\\% = 8\\%$. Hence, option C is correct. (Option B incorrectly adds uncertainties without multiplying by the power 2; option A subtracts them; option D miscalculates powers)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q04",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "classification",
      "property_identification"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m04",
    "skill_id": "9702_skill_scalars_vectors",
    "accepted_answer": "A",
    "hints": [
      "Recall the distinction between scalar quantities (which have magnitude only) and vector quantities (which have both magnitude and direction).",
      "Momentum is defined as the product of mass (a scalar) and velocity (a vector)."
    ],
    "walkthrough": [
      "A vector quantity possesses both magnitude and a spatial direction. Momentum is defined as $\\vec{p} = m\\vec{v}$, which is the product of a scalar (mass) and a vector (velocity), making momentum a vector directed along the velocity vector. Therefore, option A is correct.",
      "Speed, temperature, and Young modulus are all scalar quantities defined purely by numerical magnitudes with appropriate units and have no direction."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q05",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "graph_construction"
    ],
    "topic_id": "9702_t02",
    "module_id": "9702_t02_m01",
    "skill_id": "9702_skill_motion_graphs",
    "accepted_answer": "D",
    "hints": [
      "Determine how the acceleration of the particle varies with time by inspecting the gradient of the given $v-t$ graph.",
      "A straight line $v-t$ graph through the origin means the acceleration $a$ is constant and positive as velocity $v$ increases from zero."
    ],
    "walkthrough": [
      "The gradient of a velocity-time ($v-t$) graph represents acceleration ($a = \\frac{\\Delta v}{\\Delta t}$). Since the given $v-t$ graph is a straight line through the origin, the acceleration is constant and non-zero.",
      "On a graph with velocity $v$ on the vertical axis and acceleration $a$ on the horizontal axis, a constant value of $a$ for all values of $v \\ge 0$ is represented by a vertical straight line at that fixed value of $a$, which is shown in option D."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q06",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "direct_calculation"
    ],
    "topic_id": "9702_t02",
    "module_id": "9702_t02_m01",
    "skill_id": "9702_skill_motion_graphs",
    "accepted_answer": "B",
    "hints": [
      "Identify the time on the graph at which the parachute opens (where the velocity sharply decelerates from terminal speed, around $t \\approx 13.5\\text{ s}$).",
      "Estimate the distance fallen before this time by determining the area under the velocity-time graph from $t = 0$ to $t \\approx 13.5\\text{ s}$ (e.g. by counting grid squares where each major grid square represents $v \\times \\Delta t = 20\\text{ m s}^{-1} \\times 5\\text{ s} = 100\\text{ m}$)."
    ],
    "walkthrough": [
      "The parachutist falls freely until the parachute opens at $t \\approx 13.5\\text{ s}$, after which the velocity rapidly decreases. The total distance fallen before the parachute opens is represented by the area under the $v-t$ curve between $t = 0$ and $t = 13.5\\text{ s}$.",
      "Each large grid square represents an area of $\\Delta s = 20\\text{ m s}^{-1} \\times 5\\text{ s} = 100\\text{ m}$. Counting the equivalent squares: roughly $1.2$ squares in the first $5\\text{ s}$ interval, $2.6$ squares between $t = 5\\text{ s}$ and $t = 10\\text{ s}$, and $3 \\times 0.7 = 2.1$ squares between $t = 10\\text{ s}$ and $t = 13.5\\text{ s}$. The total number of squares is $\\approx 5.7$, giving a distance of $s = 5.7 \\times 100\\text{ m} \\approx 570\\text{ m}$ (option B)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q07",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "definition",
      "equation_recall"
    ],
    "topic_id": "9702_t03",
    "module_id": "9702_t03_m01",
    "skill_id": "9702_skill_linear_momentum_collisions",
    "accepted_answer": "C",
    "hints": [
      "Recall the defining equation for linear momentum $p$ of a body with mass $m$ and velocity $v$.",
      "Linear momentum is defined as the product of mass and velocity."
    ],
    "walkthrough": [
      "By definition in classical mechanics, linear momentum $p$ is the product of an object's mass $m$ and its velocity $v$ ($p = mv$), which makes option C correct.",
      "Option B describes impulse (product of force and time), while options A and D are physically incorrect definitions."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q08",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t03",
    "module_id": "9702_t03_m01",
    "skill_id": "9702_skill_newtons_laws",
    "accepted_answer": "A",
    "hints": [
      "Calculate the initial upward tension in the spring in static equilibrium supporting both masses ($0.20\\text{ kg} + 0.10\\text{ kg}$).",
      "Immediately after the thread is cut, the spring extension and tension remain instantaneously unchanged. Find the net upward force on the $0.20\\text{ kg}$ mass and apply $F_{\\text{net}} = ma$."
    ],
    "walkthrough": [
      "In initial equilibrium, the tension provided by the spring balances the total weight of both masses: $T = (m_1 + m_2)g = (0.20 + 0.10)g = 0.30g$.",
      "Immediately after the thread is severed, the tension in the spring is still $0.30g$ upwards, while the downward gravitational force on the first mass is $m_1 g = 0.20g$. The resultant upward force on the $0.20\\text{ kg}$ mass is $F_{\\text{net}} = 0.30g - 0.20g = 0.10g$. Applying Newton's second law: $a = \\frac{F_{\\text{net}}}{m_1} = \\frac{0.10 \\times 9.81\\text{ m s}^{-2}}{0.20} = 4.9\\text{ m s}^{-2}$, corresponding to option A."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q09",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "comparison",
      "explanation"
    ],
    "topic_id": "9702_t03",
    "module_id": "9702_t03_m02",
    "skill_id": "9702_skill_drag_terminal_velocity",
    "accepted_answer": "A",
    "hints": [
      "Equate the weight $W = mg$ to the drag force at terminal velocity for both objects.",
      "Since the snowflake has greater drag at any given speed, consider which object reaches a higher terminal speed and continues accelerating for longer."
    ],
    "walkthrough": [
      "Both objects have the same mass $m$, so their weight $W = mg$ is identical. At terminal velocity, drag force equals weight ($F_D = mg$). Because the snowflake has greater drag than the raindrop at any given speed, it reaches the condition $F_D = mg$ at a lower speed and reaches it sooner.",
      "The raindrop has lower drag at all speeds, so it continues to accelerate to a higher terminal speed, meaning it takes more time to reach terminal velocity. Hence, statement A is correct. Because the raindrop achieves a higher terminal speed, it reaches the ground in less time than the snowflake, eliminating B and D."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q10",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t03",
    "module_id": "9702_t03_m03",
    "skill_id": "9702_skill_linear_momentum_collisions",
    "accepted_answer": "D",
    "hints": [
      "Apply the principle of conservation of linear momentum to determine the speed of the $1\\text{ kg}$ trolley.",
      "Calculate the total kinetic energy of both trolleys after release. The initial elastic potential energy stored in the spring is equal to the sum of their kinetic energies."
    ],
    "walkthrough": [
      "By conservation of linear momentum, the total momentum before and after release is zero: $m_1 v_1 = m_2 v_2 \\implies (1\\text{ kg}) v_1 = (2\\text{ kg})(2\\text{ m s}^{-1}) \\implies v_1 = 4\\text{ m s}^{-1}$.",
      "The total elastic potential energy originally stored in the spring is transferred entirely into the kinetic energies of both trolleys: $E_p = E_{k,1} + E_{k,2} = \\frac{1}{2}(1\\text{ kg})(4\\text{ m s}^{-1})^2 + \\frac{1}{2}(2\\text{ kg})(2\\text{ m s}^{-1})^2 = 8\\text{ J} + 4\\text{ J} = 12\\text{ J}$. This matches option D."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q11",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t04",
    "module_id": "9702_t04_m01",
    "skill_id": "9702_skill_moments_couples",
    "accepted_answer": "B",
    "hints": [
      "For a uniform square hanging freely from a corner, the centre of gravity is at the geometric centre, halfway down the diagonal.",
      "Calculate the vertical distance from the hanging vertex to the centre of gravity for both side lengths ($x$ and $2x$), and find their difference."
    ],
    "walkthrough": [
      "For a uniform square of side length $L$, the length of the diagonal is $L\\sqrt{2}$. When suspended freely from a corner, the centre of gravity lies directly below the pivot at half the diagonal length: $h = \\frac{L\\sqrt{2}}{2} = \\frac{L}{\\sqrt{2}}$.",
      "For the first board ($L = x$), the centre of gravity is at depth $h_1 = \\frac{x}{\\sqrt{2}}$. For the second board ($L = 2x$), it is at depth $h_2 = \\frac{2x}{\\sqrt{2}} = x\\sqrt{2}$. Since both nails are at the same horizontal level, the vertical distance between their centres of gravity is $\\Delta h = h_2 - h_1 = \\frac{2x}{\\sqrt{2}} - \\frac{x}{\\sqrt{2}} = \\frac{x}{\\sqrt{2}}$, which is option B."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q12",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "force_diagram_construction",
      "property_identification"
    ],
    "topic_id": "9702_t04",
    "module_id": "9702_t04_m02",
    "skill_id": "9702_skill_equilibrium_coplanar_forces",
    "accepted_answer": "A",
    "hints": [
      "Check both equilibrium conditions: the resultant force must be zero (translational equilibrium) AND the resultant torque/moment about any point must be zero (rotational equilibrium).",
      "In diagram A, check the balance of vertical forces and symmetry of moments about the centre."
    ],
    "walkthrough": [
      "For an object to be in static equilibrium, two conditions must be satisfied simultaneously: (1) $\\Sigma F = 0$ (resultant force equals zero) and (2) $\\Sigma \\tau = 0$ (resultant moment about any point equals zero).",
      "In diagram A, the upward forces sum to $\\frac{1}{2}F + \\frac{1}{2}F = F$, exactly balancing the downward force $F$ at the centre (net force $= 0$). By symmetry, taking moments about the centre gives $\\frac{1}{2}F \\times \\frac{L}{2} - \\frac{1}{2}F \\times \\frac{L}{2} = 0$ (net torque $= 0$). Thus, diagram A is in complete equilibrium."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q13",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t04",
    "module_id": "9702_t04_m01",
    "skill_id": "9702_skill_moments_couples",
    "accepted_answer": "C",
    "hints": [
      "Take moments about the pivot point X to eliminate the unknown tension in string attached to X.",
      "Equate the clockwise moment produced by the weight of the 11 kg mass ($W = mg$) to the anticlockwise moment produced by the upward force $F$ at end Y: $F \\times 75\\text{ cm} = (W = 11 \\times 9.81\\text{ N}) \\times 25\\text{ cm}$."
    ],
    "walkthrough": [
      "To find the upward force $F$ at Y, take moments about end X so the tension in string P produces zero moment: Clockwise moment $= W \\times 25\\text{ cm} = (mg) \\times 0.25\\text{ m} = (m = 11\\text{ kg} \\times 9.81\\text{ N kg}^{-1}) \\times 0.25\\text{ m} \\approx 26.98\\text{ N m}$.",
      "For rotational equilibrium, Anticlockwise moment $=$ Clockwise moment: $F \\times 0.75\\text{ m} = 26.98\\text{ N m} \\implies F = \\frac{11 \\times 9.81 \\times 0.25}{0.75} = \\frac{11 \\times 9.81}{3} \\approx 36.0\\text{ N} \\approx 36\\text{ N}$, which corresponds to option C."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q14",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t04",
    "module_id": "9702_t04_m03",
    "skill_id": "9702_skill_density_pressure",
    "accepted_answer": "D",
    "hints": [
      "Express the total mass of the mixture as $m_{\\text{total}} = \\rho_w V_w + \\rho_g V_g$ and the total volume as $V_{\\text{total}} = V_w + V_g$.",
      "Set up the equation $\\rho_{\\text{mixture}} = \\frac{\\rho_w V_w + \\rho_g V_g}{V_w + V_g} = 1.1\\text{ g cm}^{-3}$ and solve for $V_w$."
    ],
    "walkthrough": [
      "The total mass of the mixture is the sum of the individual masses: $m_{\\text{mix}} = \\rho_w V_w + \\rho_g V_g = (1.0)V_w + (1.3)(40) = V_w + 52\\text{ g}$. The total volume is $V_{\\text{mix}} = V_w + 40\\text{ cm}^3$.",
      "The mixture density is $\\rho_{\\text{mix}} = \\frac{m_{\\text{mix}}}{V_{\\text{mix}}} = 1.1\\text{ g cm}^{-3}$. Setting up the equation: $\\frac{V_w + 52}{V_w + 40} = 1.1 \\implies V_w + 52 = 1.1 V_w + 44 \\implies 0.1 V_w = 8 \\implies V_w = 80\\text{ cm}^3$ (option D)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q15",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "graph_construction"
    ],
    "topic_id": "9702_t04",
    "module_id": "9702_t04_m03",
    "skill_id": "9702_skill_upthrust_archimedes",
    "accepted_answer": "C",
    "hints": [
      "Recall Archimedes' principle: upthrust is equal to the weight of the fluid displaced, $U = \\rho g V_{\\text{submerged}}$.",
      "Consider how the submerged volume of a cube with uniform cross-sectional area changes as it enters the water (from depth $0$ to cube height $H$), and what happens to $V_{\\text{submerged}}$ once it is completely submerged."
    ],
    "walkthrough": [
      "By Archimedes' principle, upthrust is given by $U = \\rho g V_{\\text{submerged}}$. While the cube is entering the sea (depth $h$ of the lower face from $0$ to the side length of the cube $H$), the submerged volume is $V_{\\text{submerged}} = A \\times h$, where $A$ is the constant cross-sectional area. Therefore, upthrust increases linearly with depth ($U \\propto h$) from the origin.",
      "Once the box is fully submerged ($h \\ge H$), the displaced volume is constant and equal to the total volume of the cube ($V_{\\text{total}} = A \\times H$). The upthrust remains constant regardless of further increase in depth. This linear rise followed by a horizontal plateau is shown in graph C."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q16",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "property_identification",
      "explanation"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m02",
    "skill_id": "9702_skill_kinetic_potential_energy",
    "accepted_answer": "D",
    "hints": [
      "Consider what happens to the vertical position of the spring's centre of mass as it is compressed downwards.",
      "Consider what happens to the internal strain energy stored in a spring when it is deformed from its unstretched equilibrium length."
    ],
    "walkthrough": [
      "When the vertical spring is compressed downwards by the mass, its centre of mass is lowered relative to the ground. As gravitational potential energy is given by $\\Delta E_p = mg\\Delta h$, the spring loses gravitational potential energy.",
      "At the same time, work is done against the restoring forces of the spring to compress it by compression $x$. The elastic potential energy stored in the spring increases according to $E_{\\text{elastic}} = \\frac{1}{2}kx^2$. Thus, the spring loses gravitational potential energy and gains elastic potential energy (option D)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q17",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m02",
    "skill_id": "9702_skill_power_efficiency",
    "accepted_answer": "C",
    "hints": [
      "Calculate the total vertical height gained: $h = \\text{number of steps} \\times \\text{height of each step}$.",
      "Calculate the total gain in gravitational potential energy $\\Delta E_p = mgh$, then divide by the time taken to find the power $P = \\frac{\\Delta E_p}{t}$."
    ],
    "walkthrough": [
      "The total vertical height climbed by the man is $h = 30 \\times 0.20\\text{ m} = 6.0\\text{ m}$. The gain in gravitational potential energy is $\\Delta E_p = mgh = 75\\text{ kg} \\times 9.81\\text{ m s}^{-2} \\times 6.0\\text{ m} = 4414.5\\text{ J}$.",
      "The average rate of increase of gravitational potential energy (power) is $P = \\frac{\\Delta E_p}{\\Delta t} = \\frac{4414.5\\text{ J}}{7.0\\text{ s}} \\approx 630.6\\text{ W} \\approx 630\\text{ W}$, which matches option C."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q18",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m02",
    "skill_id": "9702_skill_kinetic_potential_energy",
    "accepted_answer": "C",
    "hints": [
      "Recall the kinetic energy formula $E_k = \\frac{1}{2}mv^2$ and the mass of an $\\alpha$-particle ($m_\\alpha = 4u = 4 \\times 1.66 \\times 10^{-27}\\text{ kg}$).",
      "Rearrange to solve for speed: $v = \\sqrt{\\frac{2E_k}{m_\\alpha}}$."
    ],
    "walkthrough": [
      "An alpha particle consists of 2 protons and 2 neutrons, giving a mass $m_\\alpha = 4u = 4 \\times (1.66 \\times 10^{-27}\\text{ kg}) = 6.64 \\times 10^{-27}\\text{ kg}$.",
      "Using the formula for kinetic energy $E_k = \\frac{1}{2}m v^2$: $v = \\sqrt{\\frac{2E_k}{m_\\alpha}} = \\sqrt{\\frac{2 \\times 2.2 \\times 10^{-13}\\text{ J}}{6.64 \\times 10^{-27}\\text{ kg}}} = \\sqrt{6.627 \\times 10^{13}} \\approx 8.1 \\times 10^6\\text{ m s}^{-1}$, corresponding to option C."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q19",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "circuit_analysis",
      "direct_calculation"
    ],
    "topic_id": "9702_t06",
    "module_id": "9702_t06_m01",
    "skill_id": "9702_skill_hookes_law_elastic_energy",
    "accepted_answer": "C",
    "hints": [
      "Recall the combination rules for spring constants: springs in parallel add ($k_p = k_1 + k_2$), while springs in series combine reciprocally ($\\frac{1}{k_s} = \\frac{1}{k_1} + \\frac{1}{k_2}$).",
      "Calculate the equivalent spring constant for each configuration in terms of $k$."
    ],
    "walkthrough": [
      "For a single spring of constant $k$, we evaluate the four combinations: (A) Two springs in series: $k_A = \\frac{k}{2}$. (B) Two springs in parallel: $k_B = 2k$.",
      "For (C), each parallel branch has two springs in series ($k_{\\text{branch}} = \\frac{k}{2}$). Connecting two such branches in parallel gives $k_C = \\frac{k}{2} + \\frac{k}{2} = k$. For (D), two parallel springs ($2k$) in series with one spring ($k$) gives $k_D = \\frac{2k \\times k}{2k + k} = \\frac{2}{3}k$. Thus, configuration C has the same spring constant as a single spring."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q20",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t06",
    "module_id": "9702_t06_m01",
    "skill_id": "9702_skill_hookes_law_elastic_energy",
    "accepted_answer": "D",
    "hints": [
      "Use the elastic potential energy formula $E_p = \\frac{1}{2} F x$ to determine the extension $x$ produced by the $1.5\\text{ N}$ force.",
      "Add the calculated extension $x$ to the original unstretched length $L_0 = 2.0\\text{ cm}$ to find the total stretched length."
    ],
    "walkthrough": [
      "The elastic potential energy stored in a Hookean spring is given by $E_p = \\frac{1}{2} F x$, where $F$ is the tensile force and $x$ is the extension. Rearranging for extension: $x = \\frac{2 E_p}{F} = \\frac{2 \\times 0.045\\text{ J}}{1.5\\text{ N}} = 0.060\\text{ m} = 6.0\\text{ cm}$.",
      "The question asks for the total stretched length, which is the unstretched length plus the extension: $L = L_0 + x = 2.0\\text{ cm} + 6.0\\text{ cm} = 8.0\\text{ cm}$ (option D). Note that $6.0\\text{ cm}$ (option C) is a trap representing only the extension."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q21",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "property_identification",
      "explanation"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m01",
    "skill_id": "9702_skill_progressive_wave_properties",
    "accepted_answer": "A",
    "hints": [
      "Recall how wave speed $v = f\\lambda$, period $T = \\frac{1}{f}$, and intensity $I \\propto A^2$ relate the fundamental wave parameters.",
      "Consider whether the amplitude (set by the amplifier/loudness) depends intrinsically on the wavelength (set by the frequency of the source and medium speed)."
    ],
    "walkthrough": [
      "For sound waves in air, the wave speed $v$ is constant, so $v = f\\lambda$ means frequency is inversely proportional to wavelength ($f = \\frac{v}{\\lambda}$, option B is correct). Period is by definition $T = \\frac{1}{f}$ (option D is correct), and intensity is proportional to amplitude squared ($I \\propto A^2$, option C is correct).",
      "Amplitude represents the maximum displacement of the particles and is determined by the power/gain of the amplifier, independent of the wavelength or frequency of the sound. Therefore, the claim that amplitude is proportional to wavelength is false, making option A the correct answer."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q22",
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
      "Identify the wavelength $\\lambda$ by measuring the distance between two consecutive centres of compression (regions of maximum particle density).",
      "Use the wave equation $v = f\\lambda$ with $v = 340\\text{ m s}^{-1}$ to calculate the frequency $f$."
    ],
    "walkthrough": [
      "In a longitudinal wave, the wavelength $\\lambda$ is the distance between consecutive centres of compression. From the diagram, the first compression is located at $x = 0.0\\text{ m}$ and the next compression is centred at $x \\approx 0.50\\text{ m}$, giving a wavelength $\\lambda \\approx 0.50\\text{ m}$.",
      "Using the wave equation $v = f\\lambda$: $f = \\frac{v}{\\lambda} = \\frac{340\\text{ m s}^{-1}}{0.50\\text{ m}} = 680\\text{ Hz}$, which corresponds to option B."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q23",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "motion_path_representation"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m02",
    "skill_id": "9702_skill_progressive_wave_properties",
    "accepted_answer": "B",
    "hints": [
      "Determine the displacement of particle X at $t = 0$ from the equilibrium line.",
      "To find the initial direction of motion of particle X, shift the wave profile a small distance to the right (the direction of propagation) and observe which way point X moves."
    ],
    "walkthrough": [
      "At $t = 0$, particle X is located on the dotted equilibrium position, so its initial displacement is $0$. This eliminates options C and D.",
      "As the wave travels from left to right, the portion of the wave directly to the left of X (which is a downward sloping trough) will arrive at X next. Therefore, particle X will immediately move downwards towards negative displacement, forming a negative half-cycle first before oscillating for two full periods ($2T$). This corresponds to graph B."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q24",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "equation_recall"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m03",
    "skill_id": "9702_skill_doppler_effect",
    "accepted_answer": "D",
    "hints": [
      "Recall the Doppler effect formula for a stationary observer and an approaching source: $f_o = f_s \\left(\\frac{v}{v - v_s}\\right)$.",
      "Substitute $v_s = 0.80v$ and $f_s = 100\\text{ Hz}$ into the formula."
    ],
    "walkthrough": [
      "The observed frequency for a source approaching a stationary observer is given by the Doppler equation: $f_o = f_s \\left(\\frac{v}{v - v_s}\\right)$.",
      "Substituting $v_s = 0.80v$ into the equation gives $f_o = 100\\text{ Hz} \\times \\left(\\frac{v}{v - 0.80v}\\right) = 100 \\times \\left(\\frac{v}{0.20v}\\right) = 100 \\times 5 = 500\\text{ Hz}$. This matches option D."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q25",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "classification",
      "property_identification"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m04",
    "skill_id": "9702_skill_electromagnetic_spectrum",
    "accepted_answer": "A",
    "hints": [
      "Convert $2\\text{ cm}$ to metres: $2\\text{ cm} = 2 \\times 10^{-2}\\text{ m} = 0.02\\text{ m}$.",
      "Recall the characteristic wavelength orders of magnitude for regions of the electromagnetic spectrum (microwaves typically span from $1.0 \\times 10^{-3}\\text{ m}$ to $1.0 \\times 10^{-1}\\text{ m}$)."
    ],
    "walkthrough": [
      "The wavelength is $\\lambda = 2\\text{ cm} = 2 \\times 10^{-2}\\text{ m}$. In the electromagnetic spectrum, microwaves have typical wavelengths in the range of $1.0 \\times 10^{-3}\\text{ m}$ (1 mm) to $1.0 \\times 10^{-1}\\text{ m}$ (10 cm).",
      "Since $2\\text{ cm}$ lies squarely within the microwave region, the telescope is a microwave telescope (option A). (Optical is 400–700 nm, X-rays are $1.0 \\times 10^{-12}\\text{ m}$ to $1.0 \\times 10^{-8}\\text{ m}$, and typical radio astronomy waves are generally $\\ge 0.1\\text{ m}$ to metres)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q26",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "definition",
      "property_identification"
    ],
    "topic_id": "9702_t08",
    "module_id": "9702_t08_m01",
    "skill_id": "9702_skill_stationary_waves",
    "accepted_answer": "A",
    "hints": [
      "State the principle of superposition and note under what general conditions it holds.",
      "Consider whether conditions like equal frequency or amplitude are requirements for superposition itself or requirements for producing stable observable interference/standing wave patterns."
    ],
    "walkthrough": [
      "The principle of superposition states that when two or more waves of the same type meet at a point, the resultant displacement is the algebraic (vector) sum of the individual displacements of the waves.",
      "This principle applies universally at all times whenever waves overlap (option A). Conditions such as equal frequency, constant phase difference, or equal amplitude are requirements for forming steady observable interference or clean stationary waves, not for the principle of superposition to hold."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q27",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "property_identification"
    ],
    "topic_id": "9702_t08",
    "module_id": "9702_t08_m01",
    "skill_id": "9702_skill_stationary_waves",
    "accepted_answer": "A",
    "hints": [
      "Remember that amplitude $a$ is the maximum displacement magnitude from equilibrium and is always non-negative ($a \\ge 0$).",
      "Identify the positions where amplitude is zero (nodes at $x = 0$ and $x = \\frac{2}{3}L$) and where amplitude is maximum (antinodes at $x = \\frac{1}{3}L$ and $x = L$)."
    ],
    "walkthrough": [
      "Amplitude $a$ is defined as the magnitude of maximum displacement of the particles at each position, which means $a$ must always be greater than or equal to zero ($a \\ge 0$). This rules out graphs B and D which show negative values.",
      "The diagram illustrates the second harmonic / third harmonic mode of a closed pipe ($L = \\frac{3}{4}\\lambda$), having nodes (where $a = 0$) at $x = 0$ and $x = \\frac{2}{3}L$, and antinodes (where $a$ is maximum) at $x = \\frac{1}{3}L$ and the open end $x = L$. This pattern corresponds precisely to graph A."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q28",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "explanation",
      "property_identification"
    ],
    "topic_id": "9702_t08",
    "module_id": "9702_t08_m02",
    "skill_id": "9702_skill_wave_diffraction",
    "accepted_answer": "B",
    "hints": [
      "Recall how wavelength $\\lambda$ relates to frequency $f$ for waves travelling at constant speed ($v = f\\lambda$).",
      "Recall the condition for observable diffraction: diffraction is most pronounced when the wavelength is comparable to or larger than the gap size."
    ],
    "walkthrough": [
      "At constant wave speed $v$, the wavelength is inversely proportional to frequency: $\\lambda = \\frac{v}{f}$. Halving the frequency causes the wavelength of the water wave to double.",
      "Diffraction spreading is proportional to the ratio of wavelength to slit width ($\\frac{\\lambda}{d}$). As the wavelength increases while the gap width remains constant, the ratio $\\frac{\\lambda}{d}$ increases, resulting in more diffraction (greater spreading of the wavefronts), which corresponds to option B."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q29",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "explanation",
      "interference_analysis"
    ],
    "topic_id": "9702_t08",
    "module_id": "9702_t08_m03",
    "skill_id": "9702_skill_two_source_interference",
    "accepted_answer": "D",
    "hints": [
      "Consider the resultant amplitude at constructive interference ($A_{\\text{max}} = A_1 + A_2$) and destructive interference ($A_{\\text{min}} = |A_1 - A_2|$).",
      "Determine what happens to $A_{\\text{max}}$ and $A_{\\text{min}}$ when one of the amplitudes is decreased from an initially equal state."
    ],
    "walkthrough": [
      "Initially, both slits emit light of equal amplitude $A_1 = A_2 = A$. At maxima (bright fringes), constructive interference gives amplitude $A_{\\text{max}} = 2A$ (maximum brightness), and at minima (dark fringes), complete destructive interference gives $A_{\\text{min}} = A - A = 0$ (complete darkness).",
      "When the intensity (and amplitude $A_2$) of one slit is reduced so that $A_2 < A_1$: the maximum amplitude becomes $A_1 + A_2 < 2A$, so the bright fringes become darker (lower peak intensity). At minima, complete cancellation no longer occurs ($A_{\\text{min}} = A_1 - A_2 > 0$), so the minimum intensity increases, meaning the dark fringes become brighter. This matches option D."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q30",
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
      "Calculate the grating spacing $d$ using $d = \\frac{1}{N}$, where $N = 4.00 \\times 10^5\\text{ lines m}^{-1}$.",
      "Apply the diffraction grating formula $d\\sin\\theta = n\\lambda$ with order $n = 2$ and $\\lambda = 589 \\times 10^{-9}\\text{ m}$, then solve for angle $\\theta$."
    ],
    "walkthrough": [
      "The slit spacing $d$ of the grating is given by $d = \\frac{1}{N} = \\frac{1}{4.00 \\times 10^5\\text{ m}^{-1}} = 2.50 \\times 10^{-6}\\text{ m}$.",
      "Using the grating equation $d\\sin\\theta = n\\lambda$ for the second-order maximum ($n = 2$): $\\sin\\theta = \\frac{2 \\times 589 \\times 10^{-9}\\text{ m}}{2.50 \\times 10^{-6}\\text{ m}} = 0.4712$. Taking the inverse sine: $\\theta = \\arcsin(0.4712) \\approx 28.1^\\circ$, which is option C."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q31",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "explanation"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m01",
    "skill_id": "9702_skill_electric_current_drift_speed",
    "accepted_answer": "B",
    "hints": [
      "Recall that electric current is the rate of flow of charge ($I = \\frac{\\Delta Q}{\\Delta t}$) and is constant everywhere along a single series wire due to conservation of charge.",
      "Express the charge $\\Delta Q_S$ passing through end S in time $\\frac{t}{4}$ as $\\Delta Q_S = I \\times \\Delta t_S$."
    ],
    "walkthrough": [
      "By the principle of conservation of charge, the electric current $I$ must be constant along all sections of the wire regardless of changes in cross-sectional area (the drift speed changes to maintain constant current: $I = nAvq$).",
      "The steady current is $I = \\frac{Q}{t}$. In a time interval $\\Delta t' = \\frac{t}{4}$, the charge passing through end S is $Q_S = I \\times \\Delta t' = \\left(\\frac{Q}{t}\\right) \\times \\left(\\frac{t}{4}\\right) = \\frac{Q}{4}$ (option B). The variation in area affects only the electron drift velocity, not the total rate of charge flow."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q32",
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
      "Calculate the current $I$ supplied by the power source using $P = VI$.",
      "Calculate the power dissipated as heat in the connecting wires using $P_{\\text{wires}} = I^2 R_{\\text{wires}}$, and multiply by the time in seconds ($1.0\\text{ h} = 3600\\text{ s}$) to find the thermal energy."
    ],
    "walkthrough": [
      "First, determine the current in the circuit from the power supply output: $I = \\frac{P_{\\text{out}}}{V} = \\frac{3.6\\text{ W}}{12\\text{ V}} = 0.30\\text{ A}$.",
      "The rate of energy dissipation in the wires of resistance $R = 4.9\\text{ }\\Omega$ is $P_{\\text{wires}} = I^2 R = (0.30\\text{ A})^2 \\times 4.9\\text{ }\\Omega = 0.441\\text{ W}$. In $t = 1.0\\text{ h} = 3600\\text{ s}$, the total thermal energy dissipated is $E = P_{\\text{wires}} \\times t = 0.441\\text{ W} \\times 3600\\text{ s} = 1587.6\\text{ J} \\approx 1.6\\text{ kJ}$ (option C)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q33",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "equation_derivation",
      "direct_calculation"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m03",
    "skill_id": "9702_skill_resistivity",
    "accepted_answer": "A",
    "hints": [
      "Write the formula for resistance in terms of resistivity $\\rho$, length $L$, and diameter $d$: $R = \\frac{\\rho L}{A} = \\frac{4\\rho L}{\\pi d^2}$.",
      "Since $R$ and $L$ are equal for both wires, express the ratio of diameters $\\frac{d_{\\text{alloy}}}{d_{\\text{copper}}}$ in terms of the ratio of resistivities $\\frac{\\rho_{\\text{alloy}}}{\\rho_{\\text{copper}}}$."
    ],
    "walkthrough": [
      "The resistance of a wire is given by $R = \\frac{\\rho L}{A} = \\frac{\\rho L}{\\frac{\\pi d^2}{4}} = \\frac{4\\rho L}{\\pi d^2}$. Since both wires have identical resistance $R$ and length $L$, we have $\\frac{\\rho}{d^2} = \\text{constant}$, which means $d \\propto \\sqrt{\\rho}$.",
      "Given that $\\rho_{\\text{copper}} = \\frac{1}{2}\\rho_{\\text{alloy}}$, the ratio of resistivities is $\\frac{\\rho_{\\text{alloy}}}{\\rho_{\\text{copper}}} = 2$. The ratio of their diameters is therefore $\\frac{d_{\\text{alloy}}}{d_{\\text{copper}}} = \\sqrt{\\frac{\\rho_{\\text{alloy}}}{\\rho_{\\text{copper}}}} = \\sqrt{2}$, matching option A."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q34",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "circuit_analysis",
      "comparison"
    ],
    "topic_id": "9702_t10",
    "module_id": "9702_t10_m01",
    "skill_id": "9702_skill_resistor_networks",
    "accepted_answer": "B",
    "hints": [
      "Analyze the total resistance and circuit current before and after lamp Q breaks.",
      "Compare the current flowing through lamp P (half of the total current initially vs full new circuit current after) and lamp R (total initial current vs smaller new total current)."
    ],
    "walkthrough": [
      "Initially, lamps P and Q are in parallel with equivalent resistance $\\frac{r}{2}$, so the total circuit resistance is $1.5r$ and the main current is $I = \\frac{V}{1.5r} = \\frac{2V}{3r}$. Current through R is $\\frac{2}{3}\\frac{V}{r}$, while current through P is half of this, $\\frac{1}{3}\\frac{V}{r}$.",
      "When Q breaks, lamps P and R are in series with total resistance $2r$, reducing the main current to $I' = \\frac{V}{2r} = 0.5\\frac{V}{r}$. Since $I'_R = 0.5\\frac{V}{r} < \\frac{2}{3}\\frac{V}{r}$, lamp R receives less current and becomes dimmer. However, all of this current now passes through P ($I'_P = 0.5\\frac{V}{r} > \\frac{1}{3}\\frac{V}{r}$), so lamp P receives more current and becomes brighter (option B)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q35",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "definition",
      "equation_recall"
    ],
    "topic_id": "9702_t10",
    "module_id": "9702_t10_m01",
    "skill_id": "9702_skill_emf_internal_resistance",
    "accepted_answer": "C",
    "hints": [
      "Recall the definition and defining equation for electromotive force (e.m.f.) $E$.",
      "E.m.f. is measured in volts, where $1\\text{ V} = 1\\text{ J C}^{-1}$."
    ],
    "walkthrough": [
      "Electromotive force (e.m.f.) is defined as the electrical energy produced per unit charge converted from other forms of energy ($E = \\frac{W}{Q}$).",
      "The SI unit of e.m.f. is the volt ($\\text{V}$), which is equivalent to joules per coulomb ($\\text{J C}^{-1}$), representing energy transferred per unit charge (option C)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q36",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "circuit_analysis",
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t10",
    "module_id": "9702_t10_m03",
    "skill_id": "9702_skill_potential_dividers",
    "accepted_answer": "D",
    "hints": [
      "Recognize that a voltmeter reading of zero means the potential at the top node equals the potential at the bottom node (a balanced Wheatstone bridge condition).",
      "Set up the potential divider ratio $\\frac{2.0}{5.0} = \\frac{R_p}{10.0}$ to find the equivalent resistance $R_p$ of the parallel pair ($8.0\\text{ }\\Omega$ and $R$)."
    ],
    "walkthrough": [
      "For the voltmeter reading between the top and bottom junctions to be zero, the potentials at these points must be identical, which satisfies the balanced bridge condition: $\\frac{R_{\\text{top-left}}}{R_{\\text{bottom-left}}} = \\frac{R_{\\text{top-right}}}{R_{\\text{bottom-right}}} \\implies \\frac{2.0\\text{ }\\Omega}{5.0\\text{ }\\Omega} = \\frac{R_p}{10.0\\text{ }\\Omega}$, where $R_p$ is the parallel combination of the $8.0\\text{ }\\Omega$ resistor and $R$.",
      "Solving for $R_p$: $R_p = 10.0 \\times \\frac{2.0}{5.0} = 4.0\\text{ }\\Omega$. Since $R_p$ is the combination of two parallel resistors ($8.0\\text{ }\\Omega$ and $R$): $\\frac{1}{R_p} = \\frac{1}{8.0} + \\frac{1}{R} \\implies \\frac{1}{4.0} = \\frac{1}{8.0} + \\frac{1}{R} \\implies \\frac{1}{R} = \\frac{1}{8.0} \\implies R = 8.0\\text{ }\\Omega$ (option D)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q37",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "circuit_analysis",
      "explanation"
    ],
    "topic_id": "9702_t10",
    "module_id": "9702_t10_m03",
    "skill_id": "9702_skill_potential_dividers",
    "accepted_answer": "C",
    "hints": [
      "Note that the voltmeter reading is $V_X - V_Y$. For a positive reading, the electric potential at X must be greater than at Y ($V_X > V_Y$).",
      "Initially $V_X = V_Y = 3.0\\text{ V}$. Determine how changing the resistance of each sensor affects the potential divider voltages at X and Y."
    ],
    "walkthrough": [
      "The voltmeter measures the potential difference $V_{XY} = V_X - V_Y$. Initially, with all four components having equal resistance of $1.0\\text{ k}\\Omega$, $V_X = 3.0\\text{ V}$ and $V_Y = 3.0\\text{ V}$, giving $V_{XY} = 0$.",
      "For $V_{XY} > 0$, we require $V_X > V_Y$, which can be achieved either by increasing $V_X$ (above $3.0\\text{ V}$) or decreasing $V_Y$ (below $3.0\\text{ V}$). The potential at Y is $V_Y = 6.0\\text{ V} \\times \\frac{R_{\\text{therm}}}{R_{\\text{LDR}} + R_{\\text{therm}}}$. Reducing light intensity increases the resistance of the LDR ($R_{\\text{LDR}} > 1.0\\text{ k}\\Omega$), which drops $V_Y$ below $3.0\\text{ V}$ while $V_X = 3.0\\text{ V}$, resulting in a positive reading $V_X - V_Y > 0$ (option C)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q38",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "property_identification",
      "explanation"
    ],
    "topic_id": "9702_t11",
    "module_id": "9702_t11_m01",
    "skill_id": "9702_skill_nuclear_atom_scattering",
    "accepted_answer": "B",
    "hints": [
      "Consider what happens during Rutherford alpha-particle scattering by the gold nucleus.",
      "Remember that momentum is a vector quantity ($\\vec{p} = m\\vec{v}$), so changing the direction of motion changes the momentum."
    ],
    "walkthrough": [
      "During $\\alpha$-particle scattering, the deflection is caused by electrostatic (Coulomb) repulsion between the positive gold nucleus and the positively charged $\\alpha$-particle. No nuclear transmutation occurs, so the composition of the $\\alpha$-particle ($2$ protons, $2$ neutrons, nucleon number $4$, charge $+2e$) is unchanged.",
      "Because linear momentum is a vector quantity ($\\vec{p} = m\\vec{v}$), any change in the direction of velocity constitutes a change in momentum ($\\Delta \\vec{p} \\ne 0$). Therefore, the momentum changes as a result of the deflection (option B)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q39",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "equation_completion",
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t11",
    "module_id": "9702_t11_m01",
    "skill_id": "9702_skill_nuclear_decay_equations",
    "accepted_answer": "A",
    "hints": [
      "Conserve nucleon number $A$: determine the total decrease in nucleon number ($\\Delta A = 238 - 206 = 32$) and divide by 4 (since each $\\alpha$-particle carries 4 nucleons and $\\beta^-$ has $A=0$).",
      "Conserve proton number $Z$: using the number of $\\alpha$-particles, set up $Z: 92 = 82 + 2N_\\alpha - N_\\beta$ to find $N_\\beta$."
    ],
    "walkthrough": [
      "Only $\\alpha$-decay changes the nucleon number $A$ (each $\\alpha$-particle removes 4 nucleons, while $\\beta^-$ particles have $A = 0$). The total change in nucleon number is $\\Delta A = 238 - 206 = 32$. Therefore, the number of $\\alpha$-particles emitted is $N_\\alpha = \\frac{32}{4} = 8$.",
      "Applying conservation of proton number (atomic number $Z$): $Z_{\\text{initial}} = 92 = 82 + 2(N_\\alpha) - 1(N_\\beta) = 82 + 2(8) - N_\\beta = 98 - N_\\beta$. Solving for $N_\\beta$: $N_\\beta = 98 - 92 = 6$. Thus, $8\\text{ }\\alpha$-particles and $6\\text{ }\\beta^-$-particles are emitted, which is option A."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w22_11_q40",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "classification",
      "property_identification"
    ],
    "topic_id": "9702_t11",
    "module_id": "9702_t11_m02",
    "skill_id": "9702_skill_fundamental_particles_interactions",
    "accepted_answer": "D",
    "hints": [
      "Recall the definition of a fundamental particle: a particle that has no internal structure and is not composed of smaller constituents.",
      "Identify composite particles such as hadrons (mesons and baryons) and nuclei (such as alpha particles), which are made of quarks/nucleons."
    ],
    "walkthrough": [
      "Fundamental particles are elementary particles that cannot be broken down into simpler constituents. In the Standard Model, leptons (including electrons, positrons, neutrinos, and antineutrinos) and quarks are fundamental.",
      "Checking each option: (A) Mesons are hadrons composed of quark-antiquark pairs (composite). (B) Baryons are hadrons composed of three quarks (composite). (C) Alpha particles consist of two protons and two neutrons (composite). (D) Leptons, quarks, and positrons (anti-electrons) are all fundamental, making option D correct."
    ]
  }
]

def main():
    print(f"Total enrichments to write: {len(ENRICHMENTS)}")
    for item in ENRICHMENTS:
        qid = item['question_id']
        outfile = TARGET_DIR / f"{qid}.enrichment.json"
        outfile.write_text(json.dumps(item, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        print(f"Wrote {outfile.name}")

if __name__ == '__main__':
    main()
