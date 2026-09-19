import json
from pathlib import Path

TARGET_DIR = Path('subjects/physics/9702/enrichment/p1')
TARGET_DIR.mkdir(parents=True, exist_ok=True)

ENRICHMENTS = [
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q01",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "definition",
      "property_identification"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m01",
    "skill_id": "9702_skill_si_units_homogeneity",
    "accepted_answer": "B",
    "hints": [
      "Recall the fundamental definition of a physical quantity in physics.",
      "Every physical quantity must be expressed as the product of a numerical value (number) and an appropriate unit."
    ],
    "walkthrough": [
      "A physical quantity is defined as a property that can be measured and quantified. By definition, a complete measurement of a physical quantity consists of a numerical magnitude (a number) and a unit.",
      "While SI units are commonly used in scientific contexts, non-SI units or derived units are still valid units for physical quantities. Therefore, what is strictly essential is having both a unit and a number (option B)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q02",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "direct_calculation",
      "equation_derivation"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m02",
    "skill_id": "9702_skill_si_units_homogeneity",
    "accepted_answer": "B",
    "hints": [
      "Express each quantity on the right-hand side of $\\mu = \\frac{e \\tau}{m}$ in its SI base units.",
      "Electric charge $e$ has base units of $\\text{A s}$, mass $m$ is in $\\text{kg}$, and time interval $\\tau$ is in $\\text{s}$."
    ],
    "walkthrough": [
      "The base units for each variable in the equation $\\mu = \\frac{e\\tau}{m}$ are: charge $e$ is measured in coulombs ($\\text{C} = \\text{A s}$), time $\\tau$ is in seconds ($\\text{s}$), and mass $m$ is in kilograms ($\\text{kg}$).",
      "Substituting these into the formula gives $[\\mu] = \\frac{(\\text{A s}) \\times \\text{s}}{\\text{kg}} = \\text{A s}^2\\text{ kg}^{-1}$, which corresponds to option B."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q03",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "vector_diagram_construction",
      "direct_calculation"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m04",
    "skill_id": "9702_skill_scalars_vectors",
    "accepted_answer": "A",
    "hints": [
      "Set up the vector addition: $\\vec{v}_{\\text{resultant}} = \\vec{v}_{\\text{air}} + \\vec{v}_{\\text{wind}}$. Since the resultant is due North, the horizontal (east-west) components must cancel to zero.",
      "Use $\\sin\\theta = \\frac{200}{800}$ to find $\\theta$, and use Pythagoras' theorem or $v_R = 800\\cos\\theta$ to find the resultant velocity."
    ],
    "walkthrough": [
      "The resultant velocity $\\vec{v}_R$ is directed due north, meaning the westward wind velocity ($v_{\\text{wind}} = 200\\text{ km h}^{-1}$) is exactly balanced by the eastward component of the aircraft's airspeed: $v_{\\text{air}}\\sin\\theta = 800\\sin\\theta = 200$. Solving for $\\theta$: $\\sin\\theta = \\frac{200}{800} = 0.25 \\implies \\theta = \\arcsin(0.25) \\approx 14.5^\\circ \\approx 14^\\circ$.",
      "The northward component represents the resultant speed: $v_R = \\sqrt{800^2 - 200^2} = \\sqrt{600000} \\approx 775\\text{ km h}^{-1} \\approx 770\\text{ km h}^{-1}$. Thus, $\\theta = 14^\\circ$ and $v_R = 770\\text{ km h}^{-1}$, matching option A."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q04",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "direct_calculation"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m01",
    "skill_id": "9702_skill_oscilloscope_traces",
    "accepted_answer": "A",
    "hints": [
      "Calculate the period $T$ of the sound wave from its given frequency $f = 2000\\text{ Hz}$ using $T = \\frac{1}{f}$.",
      "Determine the horizontal distance (in cm) on the grid corresponding to one complete cycle, then find the time-base setting as $\\frac{T}{\\text{distance per cycle}}$."
    ],
    "walkthrough": [
      "The period $T$ of the wave is $T = \\frac{1}{f} = \\frac{1}{2000\\text{ Hz}} = 5.0 \\times 10^{-4}\\text{ s} = 500\\text{ }\\mu\\text{s}$.",
      "From the oscilloscope grid, one complete wave cycle spans $4\\text{ cm}$ horizontally. Therefore, the time-base setting is $\\frac{500\\text{ }\\mu\\text{s}}{4\\text{ cm}} = 125\\text{ }\\mu\\text{s cm}^{-1}$, which is option A."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q05",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "classification",
      "property_identification"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m03",
    "skill_id": "9702_skill_errors_uncertainties",
    "accepted_answer": "B",
    "hints": [
      "Recall that random errors cause unpredictable scatter about the true value, whereas systematic errors cause readings to deviate consistently in one direction or by a fixed proportion.",
      "Parallax from varying viewing angles (1) and unpredictable friction sticking (3) cause random fluctuations; a fixed percentage scale error (2) and zero offset (4) consistently bias measurements."
    ],
    "walkthrough": [
      "Random errors produce unpredictable variations with no constant sign or magnitude. Parallax errors from reading an analogue meter at fluctuating angles (1) and intermittent needle sticking due to friction (3) create random fluctuations.",
      "Systematic errors consistently shift all readings in the same direction by a predictable amount or proportion. A meter measuring 5% high (2) and a zero error (4) are systematic errors. Hence, random errors are 1 and 3, and systematic errors are 2 and 4 (option B)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q06",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "motion_path_representation"
    ],
    "topic_id": "9702_t02",
    "module_id": "9702_t02_m01",
    "skill_id": "9702_skill_projectile_motion",
    "accepted_answer": "B",
    "hints": [
      "Analyze the equations for projectile motion with negligible air resistance: $s_x = v_x t$ and $s_y = u_y t - \\frac{1}{2}g t^2$.",
      "A constant horizontal velocity gives a straight line graph of displacement against time with constant gradient ($q$), while gravitational acceleration gives a quadratic/parabolic curve of vertical displacement against time ($r$)."
    ],
    "walkthrough": [
      "In the absence of air resistance, the horizontal acceleration is zero, so horizontal velocity is constant. The horizontal displacement is $s_x = u_x t$, which varies linearly with time and corresponds to the straight line through the origin in graph $q$.",
      "The vertical motion is subject to uniform downward acceleration due to gravity $g$, giving $s_y = u_y t - \\frac{1}{2}g t^2$. This produces a parabolic curve that increases, peaks, and decreases, which corresponds to graph $r$. Thus, horizontal displacement is $q$ and vertical displacement is $r$ (option B)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q07",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "direct_calculation",
      "comparison"
    ],
    "topic_id": "9702_t02",
    "module_id": "9702_t02_m01",
    "skill_id": "9702_skill_kinematics_equations",
    "accepted_answer": "D",
    "hints": [
      "Consider the relative velocity between car X and car Y, or write expressions for the position of each car as a function of time $t$.",
      "The relative speed is $v_{\\text{rel}} = 30 - 20 = 10\\text{ m s}^{-1}$, and car X must close an initial gap of 50 m."
    ],
    "walkthrough": [
      "Let the starting position of car X be $x_X(0) = 0$ and car Y be $x_Y(0) = 50\\text{ m}$. At time $t$, their positions are $x_X(t) = 30t$ and $x_Y(t) = 50 + 20t$.",
      "Car X catches up with car Y when $x_X(t) = x_Y(t)$: $x_X = x_Y \\implies 30t = 50 + 20t \\implies 10t = 50 \\implies t = 5.0\\text{ s}$, which corresponds to option D."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q08",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "graph_interpretation",
      "property_identification"
    ],
    "topic_id": "9702_t03",
    "module_id": "9702_t03_m01",
    "skill_id": "9702_skill_newtons_laws",
    "accepted_answer": "C",
    "hints": [
      "Recall Newton's second law relating resultant force to momentum: $F = \\frac{\\Delta p}{\\Delta t}$.",
      "Since the resultant force $F$ is constant and in the direction of motion, the gradient of the $p-t$ graph must be constant and positive."
    ],
    "walkthrough": [
      "According to Newton's second law, resultant force is the rate of change of momentum: $F = \\frac{dp}{dt}$. This means the slope (gradient) of a momentum-time ($p-t$) graph represents the resultant force.",
      "Because the resultant force is constant and in the direction of velocity, the gradient $\\frac{dp}{dt}$ is constant and positive. This corresponds to a straight line with a constant positive slope, shown in graph C."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q09",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "definition",
      "property_identification"
    ],
    "topic_id": "9702_t03",
    "module_id": "9702_t03_m01",
    "skill_id": "9702_skill_newtons_laws",
    "accepted_answer": "B",
    "hints": [
      "Recall the definition of weight: $W = mg$, where $g$ is the gravitational field strength.",
      "A gravitational field exerts a gravitational force (weight) on any object that possesses mass, regardless of whether the object is accelerating or at rest on a surface."
    ],
    "walkthrough": [
      "A gravitational field is a region of space where a mass experiences a force. The weight of an object is defined as the gravitational force acting on its mass: $W = mg$.",
      "If an object has mass in a gravitational field, it must experience weight. It does not necessarily accelerate because other forces (e.g., support force from the ground) may keep it in equilibrium. Therefore, statement B is the only statement that must be true."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q10",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t03",
    "module_id": "9702_t03_m01",
    "skill_id": "9702_skill_impulse_force_time",
    "accepted_answer": "D",
    "hints": [
      "Remember that momentum is a vector quantity, so taking the rebound direction into account gives a change in velocity of $\\Delta v = v - u = -15 - 20 = -35\\text{ m s}^{-1}$.",
      "Use Newton's second law: $F_{\\text{avg}} = \\frac{\\Delta p}{\\Delta t} = \\frac{m \\Delta v}{\\Delta t}$, remembering to convert $1.0\\text{ ms}$ into seconds ($1.0 \\times 10^{-3}\\text{ s}$)."
    ],
    "walkthrough": [
      "Taking the initial direction of motion as positive, the initial velocity is $u = +20\\text{ m s}^{-1}$ and the rebound velocity is $v = -15\\text{ m s}^{-1}$. The change in velocity is $\\Delta v = -15 - 20 = -35\\text{ m s}^{-1}$.",
      "The magnitude of the change in momentum is $|\\Delta p| = m |\\Delta v| = 0.16\\text{ kg} \\times 35\\text{ m s}^{-1} = 5.6\\text{ N s}$. The average force is $F = \\frac{|\\Delta p|}{\\Delta t} = \\frac{5.6\\text{ N s}}{1.0 \\times 10^{-3}\\text{ s}} = 5600\\text{ N}$ (option D)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q11",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "property_identification",
      "comparison"
    ],
    "topic_id": "9702_t04",
    "module_id": "9702_t04_m03",
    "skill_id": "9702_skill_upthrust_archimedes",
    "accepted_answer": "C",
    "hints": [
      "Recall Archimedes' principle: upthrust is equal to the weight of the fluid displaced, $U = \\rho_{\\text{fluid}} V g$.",
      "Upthrust depends on fluid density and submerged volume of the block, not on the block's own density or its orientation."
    ],
    "walkthrough": [
      "By Archimedes' principle, the upthrust force is given by $U = \\rho_{\\text{water}} V g$, where $V = x^2 y$ is the volume of the submerged block.",
      "The upthrust depends only on the volume of the liquid displaced and the density of the liquid. It does not depend on the block's density or orientation. Increasing dimension $y$ increases the volume $V$ of the block, thereby increasing the upthrust (option C)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q12",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "direct_calculation",
      "force_diagram_construction"
    ],
    "topic_id": "9702_t04",
    "module_id": "9702_t04_m01",
    "skill_id": "9702_skill_moments_couples",
    "accepted_answer": "A",
    "hints": [
      "The moment of a force about a pivot is defined as the force multiplied by the perpendicular distance to the line of action of the force, or $\\text{perpendicular component of force} \\times \\text{distance}$.",
      "Resolve the 15 N tension force perpendicular to the shelf: $F_\\perp = 15\\sin(30^\\circ) = 7.5\\text{ N}$, then multiply by the length $0.40\\text{ m}$."
    ],
    "walkthrough": [
      "The moment of a force about a pivot is given by $\\tau = F_\\perp \\times d$, where $F_\\perp$ is the component of the force perpendicular to the lever arm and $d$ is the distance from the pivot.",
      "Here, the perpendicular component of the tension is $F_\\perp = 15\\text{ N} \\times \\sin(30^\\circ) = 7.5\\text{ N}$. Multiplying by the shelf length of $0.40\\text{ m}$ gives $\\tau = 7.5\\text{ N} \\times 0.40\\text{ m} = 3.0\\text{ N m}$ (option A)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q13",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "definition",
      "property_identification"
    ],
    "topic_id": "9702_t04",
    "module_id": "9702_t04_m01",
    "skill_id": "9702_skill_moments_couples",
    "accepted_answer": "D",
    "hints": [
      "Recall the formal definition of the principle of moments for rotational equilibrium.",
      "When calculating clockwise and anticlockwise moments to test equilibrium, both sets of moments must be evaluated about the identical reference pivot/point."
    ],
    "walkthrough": [
      "The Principle of Moments states that for a body in rotational equilibrium, the sum of clockwise moments about any chosen pivot must equal the sum of anticlockwise moments about that very same pivot.",
      "Taking moments about different points would invalidate the torque balance equation; hence moments must be taken about 'the same point' (option D)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q14",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t04",
    "module_id": "9702_t04_m03",
    "skill_id": "9702_skill_density_pressure",
    "accepted_answer": "D",
    "hints": [
      "The absolute pressure at depth $h$ is the sum of the atmospheric pressure at the surface and the hydrostatic pressure exerted by the fluid: $P = P_{\\text{atm}} + \\rho g h$.",
      "Calculate the hydrostatic pressure $\\Delta P = \\rho g h = 1000\\text{ kg m}^{-3} \\times 9.81\\text{ m s}^{-2} \\times 1.50\\text{ m} = 14.7\\text{ kPa}$ and add it to atmospheric pressure 101 kPa."
    ],
    "walkthrough": [
      "The total pressure at a depth $h$ in a liquid is given by $P = P_{\\text{atm}} + \\rho g h$, where $P_{\\text{atm}} = 101\\text{ kPa}$, $\\rho = 1000\\text{ kg m}^{-3}$, $g = 9.81\\text{ m s}^{-2}$, and $h = 1.50\\text{ m}$.",
      "The hydrostatic pressure of the water column is $\\Delta P = 1000 \\times 9.81 \\times 1.50 = 14715\\text{ Pa} \\approx 14.7\\text{ kPa}$. Adding atmospheric pressure gives $P = 101\\text{ kPa} + 14.7\\text{ kPa} = 115.7\\text{ kPa} \\approx 116\\text{ kPa}$ (option D)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q15",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "definition",
      "property_identification"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m01",
    "skill_id": "9702_skill_conservation_of_energy",
    "accepted_answer": "D",
    "hints": [
      "Recall the Principle of Conservation of Energy: total energy in any closed system is always conserved.",
      "Friction causes work to be converted into internal (thermal) energy, but it cannot destroy or reduce the total amount of energy."
    ],
    "walkthrough": [
      "According to the principle of conservation of energy, energy cannot be created or destroyed; it can only be transformed from one form to another. Therefore, total energy is always constant.",
      "When friction acts, useful mechanical energy is converted into thermal energy dissipated to the surroundings, but the total energy of the universe remains unchanged. Thus, saying friction reduces total energy is incorrect (option D)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q16",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m02",
    "skill_id": "9702_skill_kinetic_potential_energy",
    "accepted_answer": "C",
    "hints": [
      "Calculate the vertical distance $s$ moved by each weight using arc length $s = r\\theta$, converting the angle of $\\theta = 60^\\circ$ into radians: $\\theta = 60^\\circ \\times \\frac{\\pi}{180^\\circ} = \\frac{\\pi}{3}\\text{ rad}$.",
      "One weight is lifted by $s$ while the other is lowered by $s$. The net change in gravitational potential energy is $\\Delta E_p = (W_{\\text{lifted}} - W_{\\text{lowered}}) \\times s$."
    ],
    "walkthrough": [
      "The distance moved by the string when the pulley of radius $r = 0.40\\text{ m}$ rotates by $\\theta = 60^\\circ = \\frac{\\pi}{3}\\text{ rad}$ is $s = r\\theta = 0.40\\text{ m} \\times \\frac{\\pi}{3} \\approx 0.4189\\text{ m}$.",
      "As the pulley rotates, the 20 N weight is raised by $s$ while the 15 N weight is lowered by $s$. The net increase in gravitational potential energy is $\\Delta E_p = (20\\text{ N} \\times s) - (15\\text{ N} \\times s) = (20 - 15)\\text{ N} \\times 0.4189\\text{ m} = 5\\text{ N} \\times 0.4189\\text{ m} \\approx 2.1\\text{ J}$ (option C)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q17",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m02",
    "skill_id": "9702_skill_kinetic_potential_energy",
    "accepted_answer": "B",
    "hints": [
      "Calculate the initial kinetic energy using $E_{k1} = \\frac{1}{2}mu^2$ and add the kinetic energy gain ($3.0 \\times 10^5\\text{ J}$) to find the final kinetic energy $E_{k2}$.",
      "Solve for the final speed $v = \\sqrt{\\frac{2E_{k2}}{m}}$ and calculate the change in speed $\\Delta v = v - u$."
    ],
    "walkthrough": [
      "The initial kinetic energy of the car is $E_{k1} = \\frac{1}{2}mu^2 = \\frac{1}{2}(1500)(15^2) = 168\\,750\\text{ J}$. Adding the gain gives the final kinetic energy: $E_{k2} = 168\\,750 + 300\\,000 = 468\\,750\\text{ J}$.",
      "The final speed is $v = \\sqrt{\\frac{2E_{k2}}{m}} = \\sqrt{\\frac{2 \\times 468\\,750}{1500}} = \\sqrt{625} = 25\\text{ m s}^{-1}$. The change in speed is $\\Delta v = 25 - 15 = 10\\text{ m s}^{-1}$ (option B)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q18",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "multi_step_calculation",
      "force_diagram_construction"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m01",
    "skill_id": "9702_skill_power_efficiency",
    "accepted_answer": "A",
    "hints": [
      "Resolve forces parallel to the inclined plane: the forward driving force $F_{\\text{engine}}$ and the downhill component of weight $mg\\sin\\theta$ together overcome the total resistive force $F_{\\text{resist}}$.",
      "Find $F_{\\text{engine}} = F_{\\text{resist}} - mg\\sin\\theta$, then compute engine power using $P = F_{\\text{engine}} v$."
    ],
    "walkthrough": [
      "Because the car moves at constant velocity down the slope, the net force along the slope is zero: $F_{\\text{engine}} + mg\\sin(6.0^\\circ) = F_{\\text{resist}}$. The downhill component of weight is $mg\\sin(6.0^\\circ) = 1500\\text{ kg} \\times 9.81\\text{ m s}^{-2} \\times \\sin(6.0^\\circ) \\approx 1538\\text{ N}$.",
      "The engine driving force is $F_{\\text{engine}} = 2000\\text{ N} - 1538\\text{ N} = 462\\text{ N}$. The engine power output is $P = F_{\\text{engine}} v = 462\\text{ N} \\times 30\\text{ m s}^{-1} = 13860\\text{ W} \\approx 14\\text{ kW}$ (option A)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q19",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "definition",
      "equation_recall"
    ],
    "topic_id": "9702_t06",
    "module_id": "9702_t06_m01",
    "skill_id": "9702_skill_young_modulus",
    "accepted_answer": "C",
    "hints": [
      "Recall the fundamental definition of the Young modulus $E$ in terms of tensile stress $\\sigma$ and tensile strain $\\epsilon$.",
      "Young modulus is defined as the ratio of tensile stress to tensile strain: $E = \\frac{\\sigma}{\\epsilon}$."
    ],
    "walkthrough": [
      "By definition, the Young modulus $E$ of a material within its elastic limit is the ratio of stress to strain: $E = \\frac{\\sigma}{\\epsilon}$.",
      "Since stress $\\sigma = \\frac{F}{A}$ and strain $\\epsilon = \\frac{\\Delta L}{l}$, the ratio $\\frac{\\sigma}{\\epsilon}$ already accounts for cross-sectional area and length. Thus, the Young modulus is simply $\\frac{\\sigma}{\\epsilon}$ (option C)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q20",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "direct_calculation"
    ],
    "topic_id": "9702_t06",
    "module_id": "9702_t06_m02",
    "skill_id": "9702_skill_hookes_law_elastic_energy",
    "accepted_answer": "A",
    "hints": [
      "Because the two identical springs are connected in parallel, each spring supports half of the total 8.0 N weight ($F = 4.0\\text{ N}$).",
      "Read the unstretched length (at $F=0$) and stretched length (at $F=4.0\\text{ N}$) from the graph to find extension $e$, then calculate elastic potential energy $E_p = \\frac{1}{2} F e$."
    ],
    "walkthrough": [
      "With two identical parallel springs supporting a total load of $8.0\\text{ N}$, each spring experiences a tensile force of $F = \\frac{8.0\\text{ N}}{2} = 4.0\\text{ N}$.",
      "From the force-length graph for one spring, the unstretched length at $F = 0$ is $4.0\\text{ cm}$, and the length at $F = 4.0\\text{ N}$ is $7.0\\text{ cm}$, giving an extension $e = 7.0 - 4.0 = 3.0\\text{ cm} = 0.030\\text{ m}$. The strain energy stored in one spring is $E = \\frac{1}{2} F e = \\frac{1}{2} \\times 4.0\\text{ N} \\times 0.030\\text{ m} = 0.060\\text{ J}$ (option A)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q21",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m01",
    "skill_id": "9702_skill_progressive_wave_properties",
    "accepted_answer": "D",
    "hints": [
      "The distance between a crest and an adjacent trough is half a wavelength ($\\frac{\\lambda}{2} = 0.90\\text{ m}$), from which you can find $\\lambda$.",
      "Calculate the phase difference using $\\Delta \\phi = \\frac{\\Delta x}{\\lambda} \\times 360^\\circ$ where $\\Delta x = 1.30\\text{ m}$."
    ],
    "walkthrough": [
      "The distance between consecutive crest and trough corresponds to half a wavelength: $\\frac{\\lambda}{2} = 0.90\\text{ m} \\implies \\lambda = 1.80\\text{ m}$.",
      "The phase difference $\\Delta \\phi$ between two points separated by distance $\\Delta x = 1.30\\text{ m}$ is $\\Delta \\phi = \\frac{\\Delta x}{\\lambda} \\times 360^\\circ = \\frac{1.30\\text{ m}}{1.80\\text{ m}} \\times 360^\\circ = 260^\\circ$ (option D)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q22",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "classification",
      "property_identification"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m02",
    "skill_id": "9702_skill_progressive_wave_properties",
    "accepted_answer": "B",
    "hints": [
      "Consider the nature of longitudinal mechanical waves such as sound waves and whether they require a material medium.",
      "Longitudinal waves propagate via collisions and oscillations of particles in a medium; without particles (in a vacuum), they cannot propagate."
    ],
    "walkthrough": [
      "Longitudinal waves, such as sound waves, require a physical medium with particles to transmit vibrations parallel to the direction of energy transfer.",
      "In a vacuum, there are no particles to support mechanical compressions and rarefactions, so longitudinal waves cannot travel in a vacuum. Therefore, statement B is incorrect."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q23",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "property_identification"
    ],
    "topic_id": "9702_t08",
    "module_id": "9702_t08_m01",
    "skill_id": "9702_skill_stationary_waves",
    "accepted_answer": "D",
    "hints": [
      "For a pipe closed at one end, a node forms at the closed end and an antinode at the open end.",
      "Recall that a pipe closed at one end only supports odd harmonics: $f_1 = f_0$, $f_3 = 3f_0$, $f_5 = 5f_0$, etc."
    ],
    "walkthrough": [
      "For a tube closed at one end and open at the other, stationary wave resonance occurs when the length of the tube $L$ equals an odd multiple of quarter-wavelengths: $L = (2n-1)\\frac{\\lambda}{4}$.",
      "The fundamental mode ($n=1$) has $L = \\frac{\\lambda_0}{4}$ and frequency $f_0$. The next permissible stationary wave mode ($n=2$) has $L = \\frac{3\\lambda}{4}$, giving a frequency $f = 3f_0 = 3.00 f_0$ (option D)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q24",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "definition",
      "classification"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m03",
    "skill_id": "9702_skill_doppler_effect",
    "accepted_answer": "A",
    "hints": [
      "Recall the definition and general applicability of the Doppler effect across different types of wave motion.",
      "The Doppler effect occurs whenever there is relative motion between a wave source and an observer, applying to mechanical waves as well as electromagnetic waves."
    ],
    "walkthrough": [
      "The Doppler effect is the observed change in frequency or wavelength of a wave due to relative motion between the source of the wave and the observer.",
      "It is a universal wave phenomenon that occurs with all wave types, including all mechanical waves (such as sound and water waves) and all electromagnetic waves (such as light and radio waves). Therefore, option A is correct."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q25",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "classification",
      "property_identification"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m04",
    "skill_id": "9702_skill_electromagnetic_spectrum",
    "accepted_answer": "D",
    "hints": [
      "Convert $0.5\\text{ nm}$ to meters: $0.5\\text{ nm} = 5 \\times 10^{-10}\\text{ m}$.",
      "Recall the typical wavelength ranges in the electromagnetic spectrum: X-rays typically range from about $\\lambda \\sim 10^{-11}\\text{ m}$ to $\\lambda \\sim 10^{-8}\\text{ m}$ (0.01 nm to 10 nm)."
    ],
    "walkthrough": [
      "The given wavelength is $0.5\\text{ nm} = 5.0 \\times 10^{-10}\\text{ m}$.",
      "In the electromagnetic spectrum, ultraviolet radiation ranges from approximately 400 nm down to 10 nm, and X-rays span approximately 10 nm down to 10⁻³ nm ($\\lambda \\sim 10^{-8}\\text{ m}$ to $\\lambda \\sim 10^{-11}\\text{ m}$). Therefore, $0.5\\text{ nm}$ is characteristic of X-rays (option D)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q26",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "comparison"
    ],
    "topic_id": "9702_t08",
    "module_id": "9702_t08_m01",
    "skill_id": "9702_skill_stationary_waves",
    "accepted_answer": "A",
    "hints": [
      "Both sections of string have the same length $L$ and are driven at the same frequency $f$ by the central oscillator M.",
      "Use $v = f\\lambda$: since $v_{PM} = 2v_{MQ}$, the wavelength on PM is twice that on MQ ($\\lambda_{PM} = 2\\lambda_{MQ}$), meaning string PM has half as many loops as string MQ."
    ],
    "walkthrough": [
      "Both string segments have equal length $L$ and oscillate at the same frequency $f$. From the wave equation $v = f\\lambda$, the wavelength is directly proportional to wave speed: $\\lambda_{PM} = \\frac{v_{PM}}{f} = \\frac{2v_{MQ}}{f} = 2\\lambda_{MQ}$.",
      "Since the number of loops (half-wavelengths) on a fixed length $L$ is $n = \\frac{L}{\\lambda/2} = \\frac{2L}{\\lambda}$, string PM will have half the number of loops of string MQ (e.g., 1 loop on PM and 2 loops on MQ). Diagram A accurately represents this stationary wave pattern."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q27",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "property_identification",
      "comparison"
    ],
    "topic_id": "9702_t08",
    "module_id": "9702_t08_m02",
    "skill_id": "9702_skill_wave_diffraction",
    "accepted_answer": "D",
    "hints": [
      "Recall the condition for significant diffraction when a wave passes through an aperture or slit.",
      "The extent of diffraction spreading depends on the ratio of wavelength $\\lambda$ to gap width $a$ ($\\frac{\\lambda}{a}$)."
    ],
    "walkthrough": [
      "Diffraction is the spreading of waves as they pass through an opening or around an obstacle.",
      "The degree of diffraction spreading is governed by the ratio $\\frac{\\lambda}{a}$, where $\\lambda$ is the wavelength of the wave and $a$ is the width of the gap. Amplitude has no effect on the diffraction angle. Thus, the two factors are wavelength and gap width (option D)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q28",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "equation_recall",
      "interference_analysis"
    ],
    "topic_id": "9702_t08",
    "module_id": "9702_t08_m03",
    "skill_id": "9702_skill_two_source_interference",
    "accepted_answer": "C",
    "hints": [
      "Recall the condition for destructive interference (dark fringes) in terms of path difference and wavelength.",
      "The 1st dark fringe ($n=1$) occurs when path difference is $\\frac{1}{2}\\lambda$. Test $n=1$ in each option to see which produces $\\frac{1}{2}\\lambda$."
    ],
    "walkthrough": [
      "Destructive interference occurs when the path difference between two coherent wave sources equals an odd integer multiple of half-wavelengths: $\\Delta x = \\left(n - \\frac{1}{2}\\right)\\lambda$ for $n = 1, 2, 3, \\dots$.",
      "For the 1st dark fringe ($n=1$), the path difference is $\\frac{1}{2}\\lambda$; for the 2nd ($n=2$), it is $\\frac{3}{2}\\lambda$. The formula that yields these values for all positive integers $n$ is $S_2P - S_1P = \\left(n - \\frac{1}{2}\\right)\\lambda$ (option C)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q29",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "property_identification",
      "comparison"
    ],
    "topic_id": "9702_t08",
    "module_id": "9702_t08_m04",
    "skill_id": "9702_skill_diffraction_grating",
    "accepted_answer": "C",
    "hints": [
      "Use the diffraction grating equation: $d\\sin\\theta = n\\lambda$, where the linear separation of maxima on a screen at distance $D$ is $x \\approx \\frac{n\\lambda D}{d} = n N \\lambda D$.",
      "Fewer slits per unit length $N$ means a larger slit spacing $d = \\frac{1}{N}$, which decreases the diffraction angle $\\theta$ and the separation of maxima on the screen."
    ],
    "walkthrough": [
      "The diffraction grating equation is $d \\sin\\theta = n\\lambda$, where $d$ is the slit spacing and $N = \\frac{1}{d}$ is the number of slits per unit length. The linear separation between adjacent maxima on a distant screen is approximately $x = \\frac{\\lambda D}{d} = N\\lambda D$.",
      "To decrease $x$, one must either decrease $\\lambda$, decrease $D$, or decrease $N$ (which increases $d$). Replacing the grating with one having fewer slits per unit length decreases $N$, thereby reducing the fringe separation (option C)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q30",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "definition",
      "property_identification"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m02",
    "skill_id": "9702_skill_uniform_electric_fields",
    "accepted_answer": "B",
    "hints": [
      "Recall the formal definition of electric field strength $E$ in physics.",
      "Electric field strength is defined as the electrostatic force experienced per unit positive charge: $E = \\frac{F}{q}$."
    ],
    "walkthrough": [
      "Electric field strength $E$ at a point in an electric field is defined as the force $F$ per unit positive charge $q$ acting on a stationary test charge placed at that point ($E = \\frac{F}{q}$).",
      "The test charge must be positive and sufficiently small so that it does not perturb the existing electric field. Thus, option B is the correct definition."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q31",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m02",
    "skill_id": "9702_skill_uniform_electric_fields",
    "accepted_answer": "A",
    "hints": [
      "The magnitude of the force on a charge $e$ in a uniform electric field is $F = eE = e\\frac{\\Delta V}{d}$.",
      "Calculate the electric field strengths: $E_X = \\frac{500 - 200\\text{ V}}{2.0\\text{ cm}} = 150\\text{ V cm}^{-1}$ and $E_Y = \\frac{200 - 0\\text{ V}}{1.0\\text{ cm}} = 200\\text{ V cm}^{-1}$, then find the ratio $\\frac{E_X}{E_Y}$."
    ],
    "walkthrough": [
      "In a uniform electric field between parallel plates, the electric field strength is $E = \\frac{\\Delta V}{d}$, and the force on an electron is $F = eE$.",
      "For region X: $E_X = \\frac{500 - 200\\text{ V}}{2.0\\text{ cm}} = 150\\text{ V cm}^{-1}$. For region Y: $E_Y = \\frac{200 - 0\\text{ V}}{1.0\\text{ cm}} = 200\\text{ V cm}^{-1}$. The ratio of forces is $\\frac{F_X}{F_Y} = \\frac{E_X}{E_Y} = \\frac{150}{200} = 0.75$ (option A)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q32",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "equation_derivation",
      "property_identification"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m01",
    "skill_id": "9702_skill_electric_current_drift_speed",
    "accepted_answer": "C",
    "hints": [
      "Trace the standard textbook derivation of the microscopic current equation $I = nAvq$ step by step.",
      "Check the dimensions of relationship C: number density ($n$) has units $\\text{m}^{-3}$ and area ($A$) has units $\\text{m}^2$, so their product gives $\\text{m}^{-1}$, not a pure dimensionless number."
    ],
    "walkthrough": [
      "In deriving $I = nAvq$: in time $t$, charges travel a length $L = vt$ (relationship B), sweeping out a volume $V = AL$ (relationship D). The total number of charges is $N = nV = nAL$, and total charge is $Q = Nq = nALq$, giving $I = \\frac{Q}{t} = nAvq$ (relationship A).",
      "The total number of electrons is $N = \\text{number density} \\times \\text{volume}$, not $\\text{number density} \\times \\text{area}$. Therefore, relationship C is not used in the derivation."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q33",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "multi_step_calculation",
      "circuit_analysis"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m02",
    "skill_id": "9702_skill_potential_difference_power",
    "accepted_answer": "D",
    "hints": [
      "Determine the potential difference across resistor P using $V_P = \\frac{P}{I}$.",
      "Determine the potential difference across resistor Q using $V_Q = \\frac{W}{Q}$, then sum $V_P + V_Q$ to find the total e.m.f. of the series power supply."
    ],
    "walkthrough": [
      "For resistor P, the potential difference is $V_P = \\frac{P}{I} = \\frac{18\\text{ W}}{2.0\\text{ A}} = 9.0\\text{ V}$.",
      "For resistor Q, the potential difference is $V_Q = \\frac{W}{Q} = \\frac{240\\text{ J}}{40\\text{ C}} = 6.0\\text{ V}$. Since P and Q are connected in series across the supply with negligible internal resistance, the total e.m.f. is $E = V_P + V_Q = 9.0\\text{ V} + 6.0\\text{ V} = 15\\text{ V}$ (option D)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q34",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "comparison"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m03",
    "skill_id": "9702_skill_iv_characteristics",
    "accepted_answer": "A",
    "hints": [
      "Read the voltages corresponding to $I = 0.5\\text{ A}$ for both components from the $I-V$ characteristic graph.",
      "Calculate the power $P = VI$ for each component at $I = 0.5\\text{ A}$: $V_P = 2.0\\text{ V} \\implies P_P = 1.0\\text{ W}$ and $V_Q = 4.0\\text{ V} \\implies P_Q = 2.0\\text{ W}$."
    ],
    "walkthrough": [
      "From the graph, at a current of $I = 0.5\\text{ A}$, the potential difference across component P is $V_P = 2.0\\text{ V}$ and across component Q is $V_Q = 4.0\\text{ V}$.",
      "Using power $P = VI$, the power dissipated in P is $P_P = 0.5\\text{ A} \\times 2.0\\text{ V} = 1.0\\text{ W}$, while the power dissipated in Q is $P_Q = 0.5\\text{ A} \\times 4.0\\text{ V} = 2.0\\text{ W}$. Thus, the power in Q is double that in P (option A)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q35",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "comparison"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m03",
    "skill_id": "9702_skill_resistivity",
    "accepted_answer": "D",
    "hints": [
      "Recall that resistance is inversely proportional to cross-sectional area: $R = \\frac{\\rho L}{A} \\propto \\frac{1}{d^2}$.",
      "Since the wires are in parallel, the potential difference $V$ is identical across both wires, so current $I = \\frac{V}{R} \\propto A \\propto d^2$."
    ],
    "walkthrough": [
      "The resistance of a wire is given by $R = \\frac{\\rho L}{A} = \\frac{4\\rho L}{\\pi d^2}$, meaning resistance is inversely proportional to the square of diameter ($R \\propto \\frac{1}{d^2}$).",
      "Because both wires are in parallel, they have the same potential difference $V$. Thus, current $I = \\frac{V}{R} \\propto d^2$. The ratio of currents is $\\frac{I_S}{I_T} = \\left(\\frac{d_S}{d_T}\\right)^2 = \\left(\\frac{3.0\\text{ mm}}{1.5\\text{ mm}}\\right)^2 = 2^2 = 4$ (option D)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q36",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "property_identification",
      "classification"
    ],
    "topic_id": "9702_t10",
    "module_id": "9702_t10_m01",
    "skill_id": "9702_skill_resistor_networks",
    "accepted_answer": "C",
    "hints": [
      "Recall standard Cambridge AS Physics / IEC circuit symbols for measuring instruments.",
      "An oscilloscope (CRO) is represented in circuit diagrams by a circle containing a small sinusoidal waveform / screen representation."
    ],
    "walkthrough": [
      "In standard circuit diagrams, an oscilloscope (cathode-ray oscilloscope) is represented by a circle enclosing an oscillating waveform / sine trace.",
      "Diagram C correctly displays the standard circuit symbol for an oscilloscope (option C)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q37",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "circuit_analysis",
      "direct_calculation"
    ],
    "topic_id": "9702_t10",
    "module_id": "9702_t10_m02",
    "skill_id": "9702_skill_emf_internal_resistance",
    "accepted_answer": "A",
    "hints": [
      "Find the circulating current $I$ in the closed loop containing the three identical series-aiding cells using $I = \\frac{\\Sigma E}{\\Sigma r}$.",
      "Apply the terminal potential difference formula $V_{XY} = E - I r$ across the cell connected between points X and Y."
    ],
    "walkthrough": [
      "The three identical cells are connected in series aiding in a complete closed circuit with no external resistors. The total e.m.f. is $\\Sigma E = 3E$ and the total internal resistance is $\\Sigma r = 3r$, producing a circulating current of $I = \\frac{3E}{3r} = \\frac{E}{r}$.",
      "The potential difference across the terminals of one cell between points X and Y is given by $V_{XY} = E - Ir = E - \\left(\\frac{E}{r}\\right)r = E - E = 0$ (option A)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q38",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "circuit_analysis",
      "direct_calculation"
    ],
    "topic_id": "9702_t10",
    "module_id": "9702_t10_m03",
    "skill_id": "9702_skill_potentiometer_circuits",
    "accepted_answer": "A",
    "hints": [
      "On a uniform potentiometer wire, potential difference is directly proportional to balance length: $V \\propto L$.",
      "The p.d. across $R_1$ corresponds to a length of $L_1 = 60\\text{ cm}$, while the p.d. across the series combination $(R_1 + R_2)$ corresponds to $L_2 = 80\\text{ cm}$, giving the p.d. across $R_2$ as $\\Delta L = (80 - 60)\\text{ cm} = 20\\text{ cm}$."
    ],
    "walkthrough": [
      "Because the potentiometer wire is uniform, the potential difference across any segment is proportional to its length ($V \\propto L$). The potential difference across resistor $R_1$ is balanced at $L_1 = 60\\text{ cm}$, so $V_{R1} \\propto 60\\text{ cm}$.",
      "Point Y taps across the series combination of $R_1$ and $R_2$, balancing at $L_2 = 80\\text{ cm}$, so $V_{R1+R2} \\propto 80\\text{ cm}$. Hence, the p.d. across $R_2$ is $V_{R2} \\propto (80 - 60)\\text{ cm} = 20\\text{ cm}$. Since $R_1$ and $R_2$ carry the same current in series, $\\frac{R_2}{R_1} = \\frac{V_{R2}}{V_{R1}} = \\frac{20}{60} = \\frac{1}{3}$ (option A)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q39",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "equation_completion",
      "classification"
    ],
    "topic_id": "9702_t11",
    "module_id": "9702_t11_m01",
    "skill_id": "9702_skill_nuclear_decay_equations",
    "accepted_answer": "C",
    "hints": [
      "Track the change in nucleon number ($A$) and proton number ($Z$): $\\Delta A = 234 - 238 = -4$ and $\\Delta Z = 92 - 92 = 0$.",
      "An $\\alpha$-decay decreases $A$ by 4 and $Z$ by 2 ($^4_2\\text{He}$); each $\\beta^-$ decay leaves $A$ unchanged and increases $Z$ by 1 ($^0_{-1}\\text{e}$)."
    ],
    "walkthrough": [
      "The transformation from $^{238}_{92}\\text{U}$ to $^{234}_{92}\\text{U}$ requires a decrease of 4 in nucleon number ($A$) and zero net change in proton number ($Z$).",
      "The emission of one $\\alpha$-particle ($^4_2\\alpha$) reduces $A$ by 4 and $Z$ by 2 (producing $^{234}_{90}\\text{Th}$). The subsequent emission of two $\\beta^-$ particles ($^0_{-1}\\beta$) increases $Z$ by $2 \\times (+1) = +2$ with no change in $A$, returning the proton number to 92 ($^{234}_{92}\\text{U}$). Therefore, one $\\alpha$ and two $\\beta^-$ particles are emitted (option C)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_w21_11_q40",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "classification",
      "property_identification"
    ],
    "topic_id": "9702_t11",
    "module_id": "9702_t11_m02",
    "skill_id": "9702_skill_quark_model_hadrons",
    "accepted_answer": "B",
    "hints": [
      "Recall the fractional electric charges of the first-generation quarks: up ($u$) has charge $+\\frac{2}{3}e$ and down ($d$) has charge $-\\frac{1}{3}e$.",
      "A proton has a net charge of $+1e$. Find the combination of three quarks ($u$ and $d$) whose charges sum to $+1e$."
    ],
    "walkthrough": [
      "Quarks carry fractional elementary charges: an up quark $u$ has charge $+\\frac{2}{3}e$ and a down quark $d$ has charge $-\\frac{1}{3}e$.",
      "A proton is a baryon with total charge $+1e$. The combination $uud$ has total charge $\\left(+\\frac{2}{3} + \\frac{2}{3} - \\frac{1}{3}\\right)e = +1e$. Thus, a proton consists of $uud$ (option B)."
    ]
  }
]

def main():
    print(f"Generating {len(ENRICHMENTS)} enrichment files...")
    for item in ENRICHMENTS:
        qid = item["question_id"]
        out_file = TARGET_DIR / f"{qid}.enrichment.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(item, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(f"  Wrote {out_file.name}")
    print("Done!")

if __name__ == "__main__":
    main()
