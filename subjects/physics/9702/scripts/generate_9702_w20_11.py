import json
from pathlib import Path

TARGET_DIR = Path('subjects/physics/9702/enrichment/p1')
TARGET_DIR.mkdir(parents=True, exist_ok=True)

ENRICHMENTS = [
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q01",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "definition",
      "classification"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m01",
    "skill_id": "9702_skill_si_units_homogeneity",
    "accepted_answer": "C",
    "hints": [
      "Recall that a physical quantity is defined as a property of an object or system that can be measured and quantified with both a numerical magnitude and a unit.",
      "Check the units of each listed quantity: atomic number, efficiency, and strain are all dimensionless ratios or pure numbers, whereas number density has units of m⁻³."
    ],
    "walkthrough": [
      "A physical quantity consists of a numerical magnitude and a physical unit. Number density of charge carriers $n$ is defined as the number of charge carriers per unit volume, which has the SI unit m⁻³.",
      "Atomic number is a pure count of protons, efficiency is a dimensionless ratio of energy output to input, and strain is a dimensionless ratio of extension to original length ($\\Delta L / L$). Thus, only number density of charge carriers is a physical quantity with physical units (option C)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q02",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "comparison",
      "direct_calculation"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m02",
    "skill_id": "9702_skill_si_units_homogeneity",
    "accepted_answer": "B",
    "hints": [
      "Convert each time interval into seconds using standard SI unit prefixes: $\\text{m} = 10^{-3}$, $\\mu = 10^{-6}$, $\\text{n} = 10^{-9}$, and $\\text{p} = 10^{-12}$.",
      "Compare the values in scientific notation: $0.05\\text{ ms} = 5.0 \\times 10^{-5}\\text{ s}$, $t_B = 50\\text{ ns} = 5.0 \\times 10^{-8}\\text{ s}$, $t_C = 500\\,000\\text{ ps} = 5.0 \\times 10^{-7}\\text{ s}$, and $0.5\\text{ }\\mu\\text{s} = 5.0 \\times 10^{-7}\\text{ s}$."
    ],
    "walkthrough": [
      "Convert all values to seconds in standard scientific notation: $0.05\\text{ ms} = 0.05 \\times 10^{-3}\\text{ s} = 5.0 \\times 10^{-5}\\text{ s}$, $t_B = 50\\text{ ns} = 5.0 \\times 10^{-8}\\text{ s}$, $t_C = 500\\,000\\text{ ps} = 5.0 \\times 10^{-7}\\text{ s}$, and $0.5\\text{ }\\mu\\text{s} = 0.5 \\times 10^{-6}\\text{ s} = 5.0 \\times 10^{-7}\\text{ s}$.",
      "Comparing the powers of ten, $5.0 \\times 10^{-8}\\text{ s}$ is the smallest value, making 50 ns the shortest time interval (option B)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q03",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "vector_diagram_construction",
      "property_identification"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m04",
    "skill_id": "9702_skill_scalars_vectors",
    "accepted_answer": "A",
    "hints": [
      "Rearrange the vector relationship $\\vec{X} = \\vec{P} - \\vec{R}$ to form a vector addition equation: $\\vec{R} + \\vec{X} = \\vec{P}$.",
      "Using the head-to-tail vector addition method, the head of $\\vec{R}$ connects to the tail of $\\vec{X}$, and the resultant vector $\\vec{P}$ goes from the tail of $\\vec{R}$ to the head of $\\vec{X}$."
    ],
    "walkthrough": [
      "From the vector definition $\\vec{X} = \\vec{P} - \\vec{R}$, we can rearrange to get $\\vec{P} = \\vec{R} + \\vec{X}$. In vector addition, placing $\\vec{R}$ and $\\vec{X}$ head-to-tail means $\\vec{P}$ starts at the tail of $\\vec{R}$ and ends at the head of $\\vec{X}$.",
      "Diagram A correctly shows vector $\\vec{X}$ drawn from the tip of $\\vec{R}$ to the tip of $\\vec{P}$, completing the vector triangle $\\vec{R} + \\vec{X} = \\vec{P}$."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q04",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "direct_calculation"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m01",
    "skill_id": "9702_skill_oscilloscope_traces",
    "accepted_answer": "D",
    "hints": [
      "Count the number of complete wave cycles displayed across the full 10.0 cm horizontal length of the CRO trace.",
      "Divide the total length of the screen ($L = 10.0\\text{ cm}$) by the number of complete cycles ($n = 3.5\\text{ cycles}$) to find the horizontal length of one cycle, then multiply by the time-base setting ($5\\text{ ms cm}^{-1}$)."
    ],
    "walkthrough": [
      "The oscilloscope display shows $3.5$ complete waves across the total horizontal length of $L = 10.0\\text{ cm}$. Therefore, the length corresponding to one complete cycle is $\\lambda_{\\text{screen}} = \\frac{10.0\\text{ cm}}{3.5} \\approx 2.86\\text{ cm}$.",
      "Multiply this cycle length by the time-base setting: $T = 2.86\\text{ cm} \\times 5\\text{ ms cm}^{-1} = 14.3\\text{ ms} = 1.4 \\times 10^{-2}\\text{ s}$, which matches option D."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q05",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "uncertainty_analysis",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m03",
    "skill_id": "9702_skill_errors_uncertainties",
    "accepted_answer": "D",
    "hints": [
      "Calculate the central value of volume using $V = \\frac{1}{6}\\pi d^3$ with $d = 4.11\\text{ cm}$.",
      "Apply fractional uncertainty propagation for a power relationship: $\\frac{\\Delta V}{V} = 3\\frac{\\Delta d}{d}$, find $\\Delta V$, and round the uncertainty to 1 significant figure with matching precision in $V$."
    ],
    "walkthrough": [
      "Calculate the central value of the volume: $V = \\frac{1}{6}\\pi (4.11\\text{ cm})^3 \\approx 36.352\\text{ cm}^3$.",
      "Using the fractional uncertainty rule for $V \\propto d^3$: $\\frac{\\Delta V}{V} = 3\\frac{\\Delta d}{d} = 3\\left(\\frac{0.01}{4.11}\\right) \\approx 0.00730$. Thus, $\\Delta V = 36.352 \\times 0.00730 \\approx 0.265\\text{ cm}^3 \\approx 0.3\\text{ cm}^3$. Rounding the volume to match the decimal places of uncertainty gives $(36.4 \\pm 0.3)\\text{ cm}^3$ (option D)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q06",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "comparison"
    ],
    "topic_id": "9702_t02",
    "module_id": "9702_t02_m01",
    "skill_id": "9702_skill_motion_graphs",
    "accepted_answer": "D",
    "hints": [
      "Note that the graph represents distance travelled (a scalar that never decreases), not displacement from home.",
      "The gradient of a distance–time graph represents speed: initial uphill speed has moderate gradient, the 5-minute stop has zero gradient, and the return downhill journey at twice the speed must have twice the gradient and take half the time (5 minutes)."
    ],
    "walkthrough": [
      "Distance travelled is an accumulated scalar quantity, so the graph must never decrease. From $t = 0$ to $t = 10\\text{ min}$, distance increases linearly up to $d = 1\\text{ km}$.",
      "From $t = 10\\text{ min}$ to $t = 15\\text{ min}$, the cyclist is stationary in the shop, so the distance remains constant (flat line). For the return journey, cycling at twice the speed means the 1 km return takes half the time (5 minutes, from $t = 15\\text{ min}$ to $t = 20\\text{ min}$) with twice the slope, reaching a total distance of $d = 2\\text{ km}$ at $t = 20\\text{ min}$, which is correctly depicted in graph D."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q07",
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
      "Calculate the displacement travelled by car X in $t = 20\\text{ s}$ using $s_X = v_X t$.",
      "Calculate the displacement travelled by car Y in $t = 20\\text{ s}$ using $s_Y = u_Y t + \\frac{1}{2}a t^2$, then find the initial separation $d = s_Y - s_X$."
    ],
    "walkthrough": [
      "Car X travels at constant speed $v_X = 6.0\\text{ m s}^{-1}$, so its displacement in $t = 20\\text{ s}$ is $s_X = 6.0 \\times 20 = 120\\text{ m}$.",
      "Car Y accelerates from $u_Y = 4.0\\text{ m s}^{-1}$ with $a_Y = 0.50\\text{ m s}^{-2}$. Its displacement is $s_Y = (4.0)(20) + \\frac{1}{2}(0.50)(20)^2 = 80 + 100 = 180\\text{ m}$. The initial separation is $d = s_Y - s_X = 180 - 120 = 60\\text{ m}$ (option B)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q08",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "graph_interpretation",
      "property_identification"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m02",
    "skill_id": "9702_skill_kinetic_potential_energy",
    "accepted_answer": "C",
    "hints": [
      "Look at the shape of the graph: it is a straight line passing through the origin (0, 0), which represents direct proportionality ($P \\propto Q$).",
      "Identify which pair of quantities satisfies a strictly linear relationship $P = k Q$ throughout the motion."
    ],
    "walkthrough": [
      "Gravitational potential energy is given by $E_p = mgh$. In a uniform gravitational field where $g$ and $m$ are constant, $E_p$ is directly proportional to height $h$, producing a straight line passing through the origin.",
      "For the other options: air resistance increases as acceleration decreases (non-zero intercept and negative correlation), kinetic energy against time is non-linear and plateaus at terminal velocity, and work against air resistance varies non-linearly with speed. Thus, C is the only correct match."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q09",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "multi_step_calculation",
      "property_identification"
    ],
    "topic_id": "9702_t03",
    "module_id": "9702_t03_m03",
    "skill_id": "9702_skill_linear_momentum_collisions",
    "accepted_answer": "B",
    "hints": [
      "Determine the vector change in momentum of rock R: $\\Delta \\vec{p}_R = m_R (\\vec{v}_f - \\vec{v}_i)$, remembering that the direction reverses.",
      "Apply conservation of linear momentum: the change in momentum of star S is equal and opposite to that of rock R, so $\\Delta v_S = \\frac{|\\Delta p_R|}{m_S}$."
    ],
    "walkthrough": [
      "Since rock R reverses direction with unchanged speed $u = 1.0 \\times 10^4\\text{ m s}^{-1}$, its change in velocity is $\\Delta v_R = -u - u = -2u = -2.0 \\times 10^4\\text{ m s}^{-1}$. Its change in momentum has magnitude $|\\Delta p_R| = m_R |\\Delta v_R| = (1.0 \\times 10^{27}\\text{ kg})(2.0 \\times 10^4\\text{ m s}^{-1}) = 2.0 \\times 10^{31}\\text{ N s}$.",
      "By conservation of momentum for the isolated system, $|\\Delta p_S| = |\\Delta p_R| = 2.0 \\times 10^{31}\\text{ N s}$. Therefore, the magnitude of the change in velocity of the star is $\\Delta v_S = \\frac{|\\Delta p_S|}{m_S} = \\frac{2.0 \\times 10^{31}\\text{ N s}}{1.0 \\times 10^{30}\\text{ kg}} = 20\\text{ m s}^{-1}$ (option B)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q10",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t03",
    "module_id": "9702_t03_m03",
    "skill_id": "9702_skill_linear_momentum_collisions",
    "accepted_answer": "B",
    "hints": [
      "Calculate the total initial kinetic energy of the two trolleys before collision using $E_k = \\frac{1}{2}mv^2$ for each trolley.",
      "Use conservation of linear momentum to find the common velocity $v$ after the collision, compute the final kinetic energy, and find the difference."
    ],
    "walkthrough": [
      "Initial total kinetic energy: $E_{k,\\text{initial}} = \\frac{1}{2}(2.0\\text{ kg})(4.0\\text{ m s}^{-1})^2 + \\frac{1}{2}(4.0\\text{ kg})(1.0\\text{ m s}^{-1})^2 = 16\\text{ J} + 2\\text{ J} = 18\\text{ J}$.",
      "By conservation of linear momentum: $(2.0)(4.0) + (4.0)(1.0) = (2.0 + 4.0)v \\implies 12 = 6.0v \\implies v = 2.0\\text{ m s}^{-1}$. The final kinetic energy is $E_{k,\\text{final}} = \\frac{1}{2}(6.0\\text{ kg})(2.0\\text{ m s}^{-1})^2 = 12\\text{ J}$. Thus, kinetic energy lost is $\\Delta E_k = 18\\text{ J} - 12\\text{ J} = 6\\text{ J}$ (option B)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q11",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "particle_model_application",
      "classification"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m02",
    "skill_id": "9702_skill_uniform_electric_fields",
    "accepted_answer": "B",
    "hints": [
      "Recall that electric field lines point in the direction of the force on a positive test charge (from high potential to low potential).",
      "A negatively charged particle experiences an electric force in the direction opposite to the electric field lines, accelerating towards the positively charged plate."
    ],
    "walkthrough": [
      "Electric field lines point away from positive plate X toward negative plate Y. A positively charged particle (proton, alpha-particle) would experience a force in the direction of the field lines (towards Y), while a neutral neutron experiences no force.",
      "An electron carries a negative charge, so it experiences an electrostatic force opposite to the direction of the electric field lines, accelerating towards plate X (option B)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q12",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "equation_recall",
      "direct_calculation"
    ],
    "topic_id": "9702_t04",
    "module_id": "9702_t04_m01",
    "skill_id": "9702_skill_moments_couples",
    "accepted_answer": "B",
    "hints": [
      "Recall the definition of the moment of a force: $\\text{moment} = \\text{force} \\times \\text{perpendicular distance to pivot} = F d \\sin\\theta$.",
      "Both people push in directions that tend to rotate the gate in the same rotational sense (opening it), so their moments add together."
    ],
    "walkthrough": [
      "The moment produced by force $F_1$ about the hinge is the product of distance $d_1$ and the perpendicular component of force $F_1 \\sin\\theta_1$, giving $\\tau_1 = d_1 F_1 \\sin\\theta_1$.",
      "Similarly, force $F_2$ produces a moment $\\tau_2 = d_2 F_2 \\sin\\theta_2$ in the same rotational direction. The total moment is therefore $(d_1 \\times F_1 \\sin\\theta_1) + (d_2 \\times F_2 \\sin\\theta_2)$ (option B)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q13",
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
      "Since the ball moves at constant speed in a straight line, the net resultant force acting on it is zero (equilibrium condition).",
      "In a closed vector triangle for equilibrium, the three force vectors must follow head-to-tail in a closed loop, with weight pointing vertically downwards, normal contact perpendicular to the slope, and friction opposing motion up the slope."
    ],
    "walkthrough": [
      "Because the ball moves at constant velocity, the vector sum of weight $\\vec{W}$, normal contact force $\\vec{N}$, and friction force $\\vec{F}$ must be zero ($\\vec{W} + \\vec{N} + \\vec{F} = \\vec{0}$).",
      "This requires the three vectors to form a continuous closed triangle when placed head-to-tail. Diagram D correctly shows $\\vec{W}$ vertically downwards, $\\vec{N}$ perpendicular to the inclined surface, and $\\vec{F}$ acting up the slope, forming a complete closed loop."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q14",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t04",
    "module_id": "9702_t04_m03",
    "skill_id": "9702_skill_density_pressure",
    "accepted_answer": "D",
    "hints": [
      "Calculate the difference in water column heights: $\\Delta h = 31.4\\text{ cm} - 10.2\\text{ cm} = 0.212\\text{ m}$.",
      "Determine the excess hydrostatic pressure using $\\Delta p = \\rho g \\Delta h$, then add atmospheric pressure ($p_{\\text{atm}} = 101\\text{ kPa}$) to obtain the gas pressure."
    ],
    "walkthrough": [
      "The difference in water levels between the open limb and the gas limb is $\\Delta h = 31.4\\text{ cm} - 10.2\\text{ cm} = 21.2\\text{ cm} = 0.212\\text{ m}$.",
      "The pressure difference is $\\Delta p = \\rho g \\Delta h = (1000\\text{ kg m}^{-3})(9.81\\text{ m s}^{-2})(0.212\\text{ m}) \\approx 2080\\text{ Pa} = 2.08\\text{ kPa}$. The gas pressure is therefore $p_{\\text{gas}} = p_{\\text{atm}} + \\Delta p = 101\\text{ kPa} + 2.08\\text{ kPa} = 103.08\\text{ kPa} \\approx 103\\text{ kPa}$ (option D)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q15",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "direct_calculation",
      "property_identification"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m01",
    "skill_id": "9702_skill_conservation_of_energy",
    "accepted_answer": "B",
    "hints": [
      "Use the principle of conservation of energy: initial total energy equals final total energy plus energy dissipated against friction.",
      "Write the energy balance equation: $E_{k,P} + \\Delta E_p = E_{k,Q} + W_{\\text{friction}}$, where the loss in potential energy is 50 kJ."
    ],
    "walkthrough": [
      "The total energy at point P is $E_{\\text{total}, P} = E_{k,P} + E_{p,P}$. As the trolley moves to Q, the loss in potential energy converts into kinetic energy and work done against friction: $\\Delta E_p = (E_{k,Q} - E_{k,P}) + W_{\\text{friction}}$.",
      "Substitute the given values: $\\Delta E_p = 50\\text{ kJ} = (E_{k,Q} - 5\\text{ kJ}) + 10\\text{ kJ} \\implies E_{k,Q} = 50 + 5 - 10 = 45\\text{ kJ}$ (option B)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q16",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m02",
    "skill_id": "9702_skill_power_efficiency",
    "accepted_answer": "C",
    "hints": [
      "Calculate the input power from the rate of loss of gravitational potential energy: $P_{\\text{in}} = \\left(\\frac{m}{t}\\right) g h$.",
      "Calculate the efficiency using $\\eta = \\frac{P_{\\text{out}}}{P_{\\text{in}}} \\times 100\\%$."
    ],
    "walkthrough": [
      "The rate of gravitational potential energy input is $P_{\\text{in}} = \\left(\\frac{m}{t}\\right) g h = (1.5 \\times 10^5\\text{ kg s}^{-1})(9.81\\text{ m s}^{-2})(120\\text{ m}) = 1.766 \\times 10^8\\text{ W} = 176.6\\text{ MW}$.",
      "The efficiency of the power station is $\\eta = \\frac{P_{\\text{out}}}{P_{\\text{in}}} = \\frac{100\\text{ MW}}{176.6\\text{ MW}} \\approx 0.566 = 57\\%$ (option C)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q17",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "comparison",
      "direct_calculation"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m01",
    "skill_id": "9702_skill_work_done",
    "accepted_answer": "A",
    "hints": [
      "Calculate the energy for each option using the appropriate formulas: $E_p = mgh$, $E = Pt$, $E_k = \\frac{1}{2}mv^2$, and $W = p\\Delta V$.",
      "Notice that option A gives $\\Delta E_p = 60 \\times 9.81 \\times 40 \\approx 23\\,500\\text{ J} = 23.5\\text{ kJ}$, which is roughly 10 times larger than 2400 J."
    ],
    "walkthrough": [
      "Evaluate option A: $\\Delta E_p = mgh = (60\\text{ kg})(9.81\\text{ m s}^{-2})(40\\text{ m}) \\approx 23\\,544\\text{ J} \\approx 24\\text{ kJ} \\neq 2400\\text{ J}$.",
      "Options B, C, and D all equal $E_{\\text{val}} = 2400\\text{ J}$: $E = 160\\text{ W} \\times 15\\text{ s} = 2400\\text{ J}$, $E_k = \\frac{1}{2}(12\\text{ kg})(20\\text{ m s}^{-1})^2 = 2400\\text{ J}$, and $W = (120 \\times 10^3\\text{ Pa})(0.020\\text{ m}^3) = 2400\\text{ J}$. Thus, A is the correct answer."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q18",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m02",
    "skill_id": "9702_skill_power_efficiency",
    "accepted_answer": "B",
    "hints": [
      "Recall that the rate of increase of kinetic energy is given by $\\frac{\\mathrm{d}E_k}{\\mathrm{d}t} = F_{\\text{net}} v = m a v$.",
      "Multiply mass, acceleration, and instantaneous velocity: $P_{\\text{net}} = (300\\,000\\text{ kg})(0.80\\text{ m s}^{-2})(5.0\\text{ m s}^{-1})$."
    ],
    "walkthrough": [
      "The rate of increase of kinetic energy is the work done per unit time by the resultant force: $\\frac{\\mathrm{d}E_k}{\\mathrm{d}t} = F_{\\text{net}} v = (m a) v$.",
      "Substituting the given values gives $P = (300\\,000\\text{ kg})(0.80\\text{ m s}^{-2})(5.0\\text{ m s}^{-1}) = 1.2 \\times 10^6\\text{ W} = 1.2\\text{ MW}$ (option B). Note that total engine power would include overcoming resistive force ($F_{\\text{engine}}v = (240 + 15)\\text{ kN} \\times 5.0\\text{ m s}^{-1} = 1.275\\text{ MW}$), but the question specifically asks for the rate of increase of kinetic energy."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q19",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t06",
    "module_id": "9702_t06_m01",
    "skill_id": "9702_skill_young_modulus",
    "accepted_answer": "C",
    "hints": [
      "Relate Young modulus, force, cross-sectional area, and strain: $E = \\frac{\\sigma}{\\epsilon} = \\frac{F/A}{\\epsilon}$.",
      "Rearrange for cross-sectional area $A = \\frac{F}{E \\epsilon}$, then calculate radius using $r = \\sqrt{\\frac{A}{\\pi}}$."
    ],
    "walkthrough": [
      "Tensile stress is $\\sigma = E \\epsilon = (2.5 \\times 10^{11}\\text{ Pa})(6.0 \\times 10^{-5}) = 1.5 \\times 10^7\\text{ Pa}$. Cross-sectional area is $A = \\frac{F}{\\sigma} = \\frac{34\\text{ N}}{1.5 \\times 10^7\\text{ Pa}} \\approx 2.267 \\times 10^{-6}\\text{ m}^2$.",
      "Since the wire has a circular cross-section $A = \\pi r^2$, the radius is $r = \\sqrt{\\frac{A}{\\pi}} = \\sqrt{\\frac{2.267 \\times 10^{-6}\\text{ m}^2}{\\pi}} \\approx 8.5 \\times 10^{-4}\\text{ m}$ (option C)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q20",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "graph_interpretation",
      "property_identification"
    ],
    "topic_id": "9702_t06",
    "module_id": "9702_t06_m02",
    "skill_id": "9702_skill_elastic_plastic_behaviour",
    "accepted_answer": "C",
    "hints": [
      "The area under the loading curve represents the work done in stretching the rubber cord.",
      "The area under the unloading curve represents the elastic energy released during contraction; the enclosed area between curves represents the net energy lost as internal/thermal energy."
    ],
    "walkthrough": [
      "The area under loading curve P is the total work done in extending the rubber cord, while the area under unloading curve Q is the elastic potential energy recovered when the force is removed.",
      "The enclosed hysteresis loop area represents the net energy that is not recovered mechanically and is dissipated as thermal energy (heat) within the rubber material (option C)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q21",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "comparison"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m01",
    "skill_id": "9702_skill_progressive_wave_properties",
    "accepted_answer": "C",
    "hints": [
      "Use the wave equation $v = f \\lambda$ rearranged as $f = \\frac{v}{\\lambda}$ to determine the shape of the $f$ versus $\\lambda$ curve.",
      "Because $f \\propto \\frac{1}{\\lambda}$, the graph is a curve with negative decreasing slope (inverse curve). At any fixed wavelength $\\lambda$, higher wave speed produces a higher frequency, so the string curve ($v_{\\text{string}} = 440\\text{ m s}^{-1}$) lies above the air curve ($v_{\\text{air}} = 330\\text{ m s}^{-1}$)."
    ],
    "walkthrough": [
      "The relationship between frequency and wavelength is $f = \\frac{v}{\\lambda}$. This is an inverse relationship, producing a curve that asymptotically decreases towards zero as $\\lambda$ increases.",
      "Since the wave speed in the string ($v = 440\\text{ m s}^{-1}$) is greater than in air ($v = 330\\text{ m s}^{-1}$), for any given wavelength $\\lambda$, the frequency in the string must be higher than in air ($f_{\\text{string}} > f_{\\text{air}}$), which is correctly represented in graph C."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q22",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "graph_interpretation",
      "comparison"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m01",
    "skill_id": "9702_skill_progressive_wave_properties",
    "accepted_answer": "B",
    "hints": [
      "Compare the peak displacement from equilibrium of wave Y with that of wave X to determine the amplitude.",
      "Compare the period (time for one complete oscillation) of wave Y with that of wave X, then use $f = \\frac{1}{T}$ to find frequency."
    ],
    "walkthrough": [
      "The maximum displacement from equilibrium for wave Y is twice that of wave X, so the amplitude of wave Y is $2A$.",
      "The period of wave Y ($T_Y$) is twice the period of wave X ($T_X = \\frac{1}{f}$). Since frequency is the inverse of period ($f = \\frac{1}{T}$), the frequency of wave Y is $f_Y = \\frac{1}{T_Y} = \\frac{1}{2T_X} = \\frac{1}{2}f$, giving option B."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q23",
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
      "Recall that in a resonance tube with one closed end, stationary sound waves form with a node at the water surface and an antinode near the open top.",
      "Successive resonance positions occur whenever the tube length increases by half a wavelength ($\\frac{\\lambda}{2}$), regardless of any end correction."
    ],
    "walkthrough": [
      "For a tube closed at one end, consecutive resonant lengths occur at odd quarter-wavelengths: $x = \\frac{1}{4}\\lambda - c$ and $y = \\frac{3}{4}\\lambda - c$ (where $c$ is the end correction at the open end).",
      "Subtracting these two lengths eliminates the end correction: $y - x = \\frac{3}{4}\\lambda - \\frac{1}{4}\\lambda = \\frac{1}{2}\\lambda$. Rearranging gives the wavelength $\\lambda = 2(y - x)$ (option C)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q24",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "equation_recall"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m03",
    "skill_id": "9702_skill_doppler_effect",
    "accepted_answer": "A",
    "hints": [
      "Use the Doppler effect equation for a sound source moving towards a stationary observer: $f_o = \\frac{f_s v}{v - v_s}$.",
      "Substitute the given values ($f_o = 1500\\text{ Hz}$, $f_s = 1000\\text{ Hz}$, $v = 330\\text{ m s}^{-1}$) and solve for source speed $v_s$."
    ],
    "walkthrough": [
      "The observed frequency for an approaching source is given by $f_o = f_s \\left(\\frac{v}{v - v_s}\\right)$, where $v = 330\\text{ m s}^{-1}$ is the speed of sound and $v_s$ is the speed of the source.",
      "Substitute the given quantities: $f_o = 1500 = 1000 \\left(\\frac{330}{330 - v_s}\\right) \\implies 1.5(330 - v_s) = 330 \\implies 495 - 1.5 v_s = 330 \\implies 1.5 v_s = 165 \\implies v_s = 110\\text{ m s}^{-1}$ (option A)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q25",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "graph_interpretation",
      "classification"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m04",
    "skill_id": "9702_skill_electromagnetic_spectrum",
    "accepted_answer": "C",
    "hints": [
      "Read the wavelength corresponding to the maximum intensity peak from the horizontal axis of the graph.",
      "Recall the wavelength boundaries of the electromagnetic spectrum: visible light is roughly 400 nm to 700 nm, while ultraviolet spans roughly 10 nm to 400 nm."
    ],
    "walkthrough": [
      "The graph shows a peak emission intensity at a wavelength of approximately $\\lambda \\approx 250\\text{ nm}$.",
      "The visible spectrum covers approximately 400 nm to 700 nm. Wavelengths from about 10 nm to 400 nm belong to the ultraviolet region, so the maximum intensity occurs in the ultraviolet (option C)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q26",
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
      "Recall the defining characteristics of stationary waves regarding phase relationship between nodes.",
      "All particles situated between two adjacent nodes pass through equilibrium and reach their crests simultaneously (in phase), whilst particles on opposite sides of a node are in antiphase (180°)."
    ],
    "walkthrough": [
      "In a stationary wave, all vibrating particles situated between any two adjacent nodes move in the same direction at the same time and reach their maximum displacements simultaneously, meaning they oscillate in phase (statement A).",
      "Option B is incorrect because antinode amplitude is $2A$ (twice the individual wave amplitude). Option C is incorrect because adjacent node separation is $\\frac{\\lambda}{2}$. Option D is incorrect because antinodes undergo maximum displacement."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q27",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "physical_quantity_estimation",
      "explanation"
    ],
    "topic_id": "9702_t08",
    "module_id": "9702_t08_m02",
    "skill_id": "9702_skill_wave_diffraction",
    "accepted_answer": "A",
    "hints": [
      "Recall the condition for observable wave diffraction: the wavelength must be of the same order of magnitude as the aperture width ($\\lambda \\approx d$).",
      "A standard doorway has a width of about 0.8 m to 1.0 m. Compare this size with the typical wavelengths of sound versus electromagnetic waves."
    ],
    "walkthrough": [
      "Significant diffraction occurs when the wavelength of a wave is comparable to the width of the gap through which it passes ($\\lambda \\approx d$). A typical doorway has a width of order 1 m.",
      "Audible sound waves have wavelengths ranging from a few centimetres up to several metres (e.g., $f = 330\\text{ Hz} \\implies \\lambda = 1.0\\text{ m}$), which matches the doorway dimension. In contrast, UV, visible light, and X-rays have wavelengths much smaller than 1 mm and undergo negligible diffraction around doorways (option A)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q28",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "property_identification",
      "explanation"
    ],
    "topic_id": "9702_t08",
    "module_id": "9702_t08_m03",
    "skill_id": "9702_skill_two_source_interference",
    "accepted_answer": "A",
    "hints": [
      "Consider what creates a stationary position of zero sound (destructive interference): the waves must be coherent (constant phase difference) and have similar amplitudes.",
      "A constant phase difference does not need to be zero (in phase) to produce fixed positions of cancellation; non-zero constant phase simply shifts the spatial positions of nodes."
    ],
    "walkthrough": [
      "For stable destructive interference to produce a fixed point of zero sound, the two sources must be coherent (same frequency and wavelength, hence constant phase difference) and have equal or similar amplitudes for complete cancellation.",
      "The initial phase difference between the sources does not have to be zero. As long as the phase difference is constant over time, stationary nodal points will exist along the line, so emitting strictly in phase (option A) is not a necessary condition."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q29",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "equation_recall"
    ],
    "topic_id": "9702_t08",
    "module_id": "9702_t08_m04",
    "skill_id": "9702_skill_diffraction_grating",
    "accepted_answer": "B",
    "hints": [
      "Use the diffraction grating formula $d \\sin\\theta = n\\lambda$.",
      "Since the maxima coincide at the same angle $\\theta$, set $n_1 \\lambda_1 = n_2 \\lambda_2$ and solve for $\\lambda_2$."
    ],
    "walkthrough": [
      "The condition for diffraction maxima from a grating is $d \\sin\\theta = n\\lambda$. For two wavelengths coinciding at the same diffraction angle $\\theta$, the product $n\\lambda$ must be identical: $n_1 \\lambda_1 = n_2 \\lambda_2$.",
      "Substitute the given values: $4 \\times 600\\text{ nm} = 5 \\times \\lambda_{\\text{blue}} \\implies \\lambda_{\\text{blue}} = \\frac{2400\\text{ nm}}{5} = 480\\text{ nm}$ (option B)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q30",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "electric_field_line_construction",
      "property_identification"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m02",
    "skill_id": "9702_skill_uniform_electric_fields",
    "accepted_answer": "A",
    "hints": [
      "Electric field lines point in the direction of the force on a positive charge (from positive to negative).",
      "An electron carries a negative charge, so the electric force acting on it is directed tangentially opposite to the direction of the field lines at that point (towards the positive sphere)."
    ],
    "walkthrough": [
      "Electric field lines indicate the direction of the force experienced by a positive test charge, radiating outwards from the positive sphere and terminating on the negative sphere.",
      "Because an electron has a negative charge ($q = -e$), the electric force vector $\\vec{F} = q\\vec{E}$ is oriented tangent to the local field line but in the opposite direction (towards the positive charge). Electron A correctly shows this force arrow pointing towards the positive sphere."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q31",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "equation_derivation",
      "direct_calculation"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m02",
    "skill_id": "9702_skill_uniform_electric_fields",
    "accepted_answer": "A",
    "hints": [
      "Equate the upward electric force $F_E = qE$ to the downward gravitational weight $W = mg$ for a stationary oil drop.",
      "Substitute the uniform electric field strength $E = \\frac{V}{d}$ and rearrange for the charge-to-mass ratio $\\frac{q}{m}$."
    ],
    "walkthrough": [
      "For the oil drop to remain stationary in equilibrium, the upward electrostatic force must balance its weight: $F_E = W \\implies q E = m g$.",
      "The electric field strength between parallel plates separated by distance $d$ with potential difference $V$ is $E = \\frac{V}{d}$. Substituting gives $q\\left(\\frac{V}{d}\\right) = m g \\implies \\frac{q}{m} = \\frac{g d}{V}$ (option A)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q32",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m01",
    "skill_id": "9702_skill_electric_current_drift_speed",
    "accepted_answer": "A",
    "hints": [
      "Use the drift velocity formula $I = n A v q = n (\\pi r^2) v e$ for both copper wires.",
      "Set up the ratio $\\frac{v_Y}{v_X} = \\left(\\frac{I_Y}{I_X}\\right)\\left(\\frac{r_X}{r_Y}\\right)^2$ since number density $n$ and elementary charge $e$ are identical for copper."
    ],
    "walkthrough": [
      "From the electric current formula $I = n A v e = n (\\pi r^2) v e$, drift speed is $v = \\frac{I}{n e \\pi r^2}$. Since both wires are made of copper, $n$ and $e$ are constant.",
      "Taking the ratio: $\\frac{v_Y}{v_X} = \\left(\\frac{I_Y}{I_X}\\right) \\left(\\frac{r_X}{r_Y}\\right)^2 = \\left(\\frac{2.0\\text{ A}}{3.0\\text{ A}}\\right) \\left(\\frac{5.0 \\times 10^{-5}\\text{ m}}{1.0 \\times 10^{-4}\\text{ m}}\\right)^2 = \\frac{2}{3} \\times \\left(\\frac{1}{2}\\right)^2 = \\frac{2}{12} = \\frac{1}{6}$. Thus, $v_Y = \\frac{2.8 \\times 10^{-2}\\text{ m s}^{-1}}{6} \\approx 4.7 \\times 10^{-3}\\text{ m s}^{-1}$ (option A)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q33",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "definition",
      "property_identification"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m02",
    "skill_id": "9702_skill_potential_difference_power",
    "accepted_answer": "D",
    "hints": [
      "Recall the fundamental standard definition of electrical potential difference in terms of energy and charge.",
      "Potential difference $V$ across a component is defined as the work done (or electrical energy transferred) per unit charge passed through the component ($V = \\frac{W}{Q}$)."
    ],
    "walkthrough": [
      "By definition, potential difference (p.d.) between two points is the energy transferred from electrical to other forms per unit charge (or work done per unit charge) moving between those two points: $V = \\frac{W}{Q}$.",
      "Options A, B, and C describe mathematical relations or special cases (such as Ohm's law or uniform fields), but only option D states the correct fundamental definition."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q34",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m03",
    "skill_id": "9702_skill_resistivity",
    "accepted_answer": "A",
    "hints": [
      "Find the total voltage dropped across the connecting wires: $V_{\\text{cable}} = 12.0\\text{ V} - 10.5\\text{ V} = 1.50\\text{ V}$, and compute the total resistance using $R = \\frac{V}{I}$.",
      "Remember that a cable of length $L$ contains two wires (total length $2L$). Use $R = \\frac{\\rho (2L)}{A}$ and solve for $L$."
    ],
    "walkthrough": [
      "The voltage drop across the connecting cable is $V_{\\text{cable}} = 12.0\\text{ V} - 10.5\\text{ V} = 1.50\\text{ V}$. With current $I = 2.50\\text{ A}$, the total resistance of the cable is $R_{\\text{total}} = \\frac{1.50\\text{ V}}{2.50\\text{ A}} = 0.60\\text{ }\\Omega$.",
      "The cable consists of two identical wires of length $L$, giving total length $l_{\\text{total}} = 2L$. Using the resistivity formula $R = \\frac{\\rho l_{\\text{total}}}{A}$: $2L = \\frac{R A}{\\rho} = \\frac{(0.60\\text{ }\\Omega)(6.00 \\times 10^{-7}\\text{ m}^2)}{1.70 \\times 10^{-8}\\text{ }\\Omega\\text{ m}} \\approx 21.18\\text{ m} \\implies L = \\frac{21.18\\text{ m}}{2} \\approx 10.6\\text{ m}$ (option A)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q35",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "circuit_analysis",
      "property_identification"
    ],
    "topic_id": "9702_t10",
    "module_id": "9702_t10_m03",
    "skill_id": "9702_skill_potential_dividers",
    "accepted_answer": "B",
    "hints": [
      "To achieve a voltage that can be smoothly reduced all the way down to zero (0 V), the lamp must be connected to a potential divider (potentiometer) configuration, not merely a simple series rheostat.",
      "To prevent the maximum output voltage from exceeding the lamp's rated operating voltage when the supply e.m.f. is larger, a fixed resistor must be included in series with the potentiometer track."
    ],
    "walkthrough": [
      "A potentiometer connection allows the output voltage across the lamp to vary continuously down to 0 V when the sliding contact is at the zero-potential rail, unlike a series variable resistor which cannot reach zero voltage.",
      "To ensure the maximum voltage across the lamp does not exceed its rated operating voltage despite the supply e.m.f. being higher, a fixed series resistor is placed in series with the potentiometer track (circuit B) to drop the excess potential."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q36",
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
      "Determine how the total equivalent resistance of the circuit changes when switch S connects lamp L3 in parallel with L2.",
      "Analyse the resulting change in total circuit current (affecting L1) and the change in potential difference across the parallel pair (affecting L2)."
    ],
    "walkthrough": [
      "When switch S is open, L1 and L2 are in series, so total resistance is $2R$, the current is $I = \\frac{V}{2R}$, and each lamp receives voltage $0.5V$.",
      "Closing switch S places L3 in parallel with L2, reducing their combined resistance to $0.5R$ and total circuit resistance to $1.5R$. The total current increases to $I' = \\frac{V}{1.5R} = \\frac{2}{3}\\frac{V}{R}$, making lamp L1 brighter. The potential difference across the parallel combination becomes $\\frac{1}{3}V$, which is less than $0.5V$, making lamp L2 dimmer (option B)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q37",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "circuit_analysis",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t10",
    "module_id": "9702_t10_m01",
    "skill_id": "9702_skill_resistor_networks",
    "accepted_answer": "A",
    "hints": [
      "Calculate the equivalent resistance of the parallel combination of $R_2$ (100 kΩ) and the voltmeter (100 kΩ).",
      "Find the total circuit current, calculate the potential difference across the parallel combination, and then find the current specifically flowing through $R_2$."
    ],
    "walkthrough": [
      "The voltmeter (100 kΩ) in parallel with $R_2$ (100 kΩ) gives an equivalent resistance $R_p = \\frac{100\\text{ k}\\Omega}{2} = 50\\text{ k}\\Omega$. Total circuit resistance is $R_{\\text{total}} = R_1 + R_p = 100\\text{ k}\\Omega + 50\\text{ k}\\Omega = 150\\text{ k}\\Omega$.",
      "The total circuit current is $I_{\\text{total}} = \\frac{6.0\\text{ V}}{150\\text{ k}\\Omega} = 40\\text{ }\\mu\\text{A}$. This current splits equally between the identical resistances of $R_2$ and the voltmeter, so the current in $R_2$ is $I_2 = \\frac{40\\text{ }\\mu\\text{A}}{2} = 20\\text{ }\\mu\\text{A}$ (option A)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q38",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "definition",
      "property_identification"
    ],
    "topic_id": "9702_t11",
    "module_id": "9702_t11_m01",
    "skill_id": "9702_skill_nuclear_atom_scattering",
    "accepted_answer": "D",
    "hints": [
      "Recall that isotopes of an element have the same atomic number $Z$ (same number of protons) but different mass/nucleon numbers $A$ (different number of neutrons).",
      "In an electrically neutral uncharged atom, the number of electrons equals the number of protons ($Z$)."
    ],
    "walkthrough": [
      "Isotopes are nuclei of the same chemical element that contain the same number of protons ($Z$) but different numbers of neutrons ($N$).",
      "Because an uncharged neutral atom has zero net charge, its total number of orbital electrons must equal its proton number $Z$. Since both isotopes have the identical proton number, their uncharged atoms have the same number of electrons (statement D)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q39",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "equation_completion",
      "direct_calculation"
    ],
    "topic_id": "9702_t11",
    "module_id": "9702_t11_m01",
    "skill_id": "9702_skill_nuclear_decay_equations",
    "accepted_answer": "A",
    "hints": [
      "Recall that an alpha-particle is a helium nucleus: ${^{4}_{2}\\alpha}$.",
      "Apply conservation of nucleon number ($A$) and conservation of proton number ($Z$) across the nuclear reaction."
    ],
    "walkthrough": [
      "The nuclear equation is ${{^{32}_{16}\\text{S}} + {^{94}_{42}\\text{Mo}} \\rightarrow {^{A}_{Z}\\text{X}} + {^{4}_{2}\\alpha}}$.",
      "Applying conservation of nucleon number: $A_{\\text{total}} = 32 + 94 = A + 4 \\implies A = 126 - 4 = 122$. Applying conservation of proton number: $Z_{\\text{total}} = 16 + 42 = Z + 2 \\implies Z = 58 - 2 = 56$. Thus, the nucleus is ${^{122}_{56}\\text{X}}$ (option A)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w20_11_q40",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "particle_model_application",
      "property_identification"
    ],
    "topic_id": "9702_t11",
    "module_id": "9702_t11_m02",
    "skill_id": "9702_skill_quark_model_hadrons",
    "accepted_answer": "A",
    "hints": [
      "Recall the quark composition of a standard neutron ($u d d$).",
      "An antineutron is the antimatter counterpart of a neutron, consisting of the corresponding antiquarks: $\\bar{u} \\bar{d} \\bar{d}$."
    ],
    "walkthrough": [
      "A neutron is composed of one up quark ($u$) and two down quarks ($d$), giving a total charge of $+\\frac{2}{3} - \\frac{1}{3} - \\frac{1}{3} = 0$.",
      "Its antiparticle, the antineutron, is made of the corresponding antiquarks: one up antiquark ($\\bar{u}$) and two down antiquarks ($\\bar{d}$), which is correctly depicted in diagram A."
    ]
  }
]

def main():
    for i, item in enumerate(ENRICHMENTS, 1):
        filename = f'9702_w20_11_q{i:02d}.enrichment.json'
        (TARGET_DIR / filename).write_text(json.dumps(item, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

if __name__ == '__main__':
    main()
