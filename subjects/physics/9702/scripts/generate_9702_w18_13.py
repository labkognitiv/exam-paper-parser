import json
from pathlib import Path

enrichments = {
    1: {
        "difficulty": 1,
        "question_patterns": ["physical_quantity_estimation", "comparison"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m01",
        "skill_id": "9702_skill_physical_estimations",
        "accepted_answer": "C",
        "hints": [
            "Recall standard orders of magnitude for atmospheric pressure (~10⁵ Pa), Sun-to-Earth light travel time (~500 s), and human lifespan (~70 years).",
            "Estimate the frequency of ultraviolet radiation using the wave equation $c = f\\lambda$, taking $\\lambda$ in the range 10 nm to 400 nm."
        ],
        "walkthrough": [
            "Atmospheric pressure at sea level is approximately $1.01 \\times 10^5\\text{ Pa}$ ($\\approx 1 \\times 10^5\\text{ Pa}$). Light from the Sun travels a distance of $1.5 \\times 10^{11}\\text{ m}$ at speed $3.0 \\times 10^8\\text{ m s}^{-1}$, taking $t = \\frac{1.5 \\times 10^{11}}{3.0 \\times 10^8} = 500\\text{ s} = 5 \\times 10^2\\text{ s}$. A human lifespan of approximately 70 years corresponds to $t \\approx 70 \\times 3.16 \\times 10^7\\text{ s} \\approx 2.2 \\times 10^9\\text{ s} \\approx 2 \\times 10^9\\text{ s}$.",
            "Ultraviolet light has wavelengths between approximately 10 nm and 400 nm. The corresponding frequency is $f = \\frac{c}{\\lambda} \\approx \\frac{3.0 \\times 10^8\\text{ m s}^{-1}}{100 \\times 10^{-9}\\text{ m}} = 3 \\times 10^{15}\\text{ Hz}$. A frequency of $3 \\times 10^{12}\\text{ Hz}$ falls in the infrared/terahertz region, making Option C unreasonable."
        ]
    },
    2: {
        "difficulty": 1,
        "question_patterns": ["equation_derivation", "property_identification"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m02",
        "skill_id": "9702_skill_si_units_homogeneity",
        "accepted_answer": "C",
        "hints": [
            "Determine the SI derived or base unit for each of the four physical quantities.",
            "Note that work and energy are force multiplied by distance, while power is energy divided by time and force is rate of change of momentum."
        ],
        "walkthrough": [
            "Evaluating the units of each quantity: Option A gives $\\frac{\\text{energy}}{\\text{distance}} = \\frac{\\text{J}}{\\text{m}} = \\text{N}$. Option B is force, which has the unit $\\text{N}$. Option D is rate of change of momentum $\\frac{\\Delta p}{\\Delta t} = \\frac{\\text{kg}\\cdot\\text{m s}^{-1}}{\\text{s}} = \\text{N}$.",
            "Option C gives $\\text{power} \\times \\text{time} = \\text{W} \\times \\text{s} = \\text{J}$ (joules), which is a unit of energy rather than force. Hence Option C has a different unit."
        ]
    },
    3: {
        "difficulty": 1,
        "question_patterns": ["classification", "property_identification"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m04",
        "skill_id": "9702_skill_scalars_vectors",
        "accepted_answer": "C",
        "hints": [
            "Recall that a vector quantity has both magnitude and direction, whereas a scalar has only magnitude.",
            "Check each group to see if any scalar quantity (such as speed, work, or power) is present."
        ],
        "walkthrough": [
            "A vector quantity requires both magnitude and direction. Displacement, force, velocity, acceleration, and electric field strength are vectors, while speed, work, and power are scalars.",
            "Option A contains speed (scalar). Option B contains work (scalar). Option D contains power (scalar). Option C contains displacement, force, and velocity, all of which are vectors."
        ]
    },
    4: {
        "difficulty": 1,
        "question_patterns": ["measurement_selection", "direct_calculation"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m03",
        "skill_id": "9702_skill_measurement_instruments",
        "accepted_answer": "B",
        "hints": [
            "Determine the fractional deflection of the pointer relative to the full-scale value.",
            "Multiply the full-scale current of $2.0\\text{ A}$ by the fraction indicated on the meter scale."
        ],
        "walkthrough": [
            "The ammeter scale shows full-scale deflection at 10 major divisions (or 5 major divisions on the lower scale). The pointer indicates 7.5 out of 10 divisions (or 3.75 out of 5 divisions), which represents $\\frac{7.5}{10} = 0.75$ of full scale.",
            "Since full-scale deflection corresponds to $2.0\\text{ A}$, the measured current is $I = 0.75 \\times 2.0\\text{ A} = 1.5\\text{ A}$ (Option B)."
        ]
    },
    5: {
        "difficulty": 2,
        "question_patterns": ["uncertainty_analysis", "multi_step_calculation"],
        "topic_id": "9702_t01",
        "module_id": "9702_t01_m03",
        "skill_id": "9702_skill_errors_uncertainties",
        "accepted_answer": "B",
        "hints": [
            "Convert both measurements to the same unit (metres) before calculating the area.",
            "Calculate the fractional uncertainties for length and width, add them to obtain the total fractional uncertainty of the area, and then find the absolute uncertainty."
        ],
        "walkthrough": [
            "Convert the width to metres: $w = (0.503 \\pm 0.001)\\text{ m}$. The length is $l = (1.40 \\pm 0.01)\\text{ m}$. The calculated area is $A = w \\times l = 0.503 \\times 1.40 = 0.7042\\text{ m}^2 \\approx 0.704\\text{ m}^2$.",
            "The fractional uncertainty in area is $\\frac{\\Delta A}{A} = \\frac{\\Delta w}{w} + \\frac{\\Delta l}{l} = \\frac{0.001}{0.503} + \\frac{0.01}{1.40} \\approx 0.00199 + 0.00714 = 0.00913$.",
            "The absolute uncertainty is $\\Delta A = 0.7042 \\times 0.00913 \\approx 0.0064\\text{ m}^2 \\approx 0.006\\text{ m}^2$. Expressing to appropriate precision gives $(0.704 \\pm 0.006)\\text{ m}^2$ (Option B)."
        ]
    },
    6: {
        "difficulty": 1,
        "question_patterns": ["graph_interpretation", "property_identification"],
        "topic_id": "9702_t02",
        "module_id": "9702_t02_m01",
        "skill_id": "9702_skill_projectile_motion",
        "accepted_answer": "A",
        "hints": [
            "In the absence of air resistance, consider the horizontal acceleration and vertical acceleration of a projectile separately.",
            "Horizontal velocity remains constant, while vertical velocity increases linearly with time due to uniform gravitational acceleration ($v_V = gt$)."
        ],
        "walkthrough": [
            "Because air resistance is negligible, the horizontal acceleration is zero ($a_H = 0$), meaning the horizontal velocity $v_H$ remains constant over time, represented by a horizontal straight line.",
            "The vertical motion undergoes constant acceleration due to gravity ($a_V = g$), so starting from rest vertically at $t = 0$, the vertical velocity is $v_V = gt$, which is a straight line through the origin with a constant positive gradient.",
            "Graph A correctly shows $v_H$ as a constant horizontal line and $v_V$ as a linearly increasing line from the origin."
        ]
    },
    7: {
        "difficulty": 1,
        "question_patterns": ["direct_calculation", "explanation"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_newtons_laws",
        "accepted_answer": "B",
        "hints": [
            "Apply Newton's third law: the force exerted by the 2.0 kg sphere on the 4.0 kg sphere is equal in magnitude and opposite in direction to the force exerted on the 2.0 kg sphere.",
            "Calculate the force on the 2.0 kg sphere using $F = ma$, and then determine the acceleration of the 4.0 kg sphere."
        ],
        "walkthrough": [
            "The magnitude of the force acting on the 2.0 kg mass during collision is $F = m_1 a_1 = 2.0\\text{ kg} \\times 8.0\\text{ m s}^{-2} = 16\\text{ N}$.",
            "By Newton's third law, the 4.0 kg mass experiences an equal magnitude force of 16 N.",
            "Using Newton's second law, its average acceleration is $a_2 = \\frac{F}{m_2} = \\frac{16\\text{ N}}{4.0\\text{ kg}} = 4.0\\text{ m s}^{-2}$ (Option B)."
        ]
    },
    8: {
        "difficulty": 1,
        "question_patterns": ["direct_calculation"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_newtons_laws",
        "accepted_answer": "A",
        "hints": [
            "Resolve the weight of the mass parallel to the inclined slope.",
            "Use $a = g \\sin\\theta$ for motion down a frictionless plane inclined at angle $\\theta$ to the horizontal."
        ],
        "walkthrough": [
            "The component of gravitational force acting parallel down the slope is $F = mg \\sin(30^\\circ)$.",
            "Applying Newton's second law ($F = ma$) gives the acceleration down the frictionless slope as $a = g \\sin(30^\\circ) = 9.81\\text{ m s}^{-2} \\times 0.50 = 4.905\\text{ m s}^{-2} \\approx 4.9\\text{ m s}^{-2}$ (Option A)."
        ]
    },
    9: {
        "difficulty": 2,
        "question_patterns": ["graph_interpretation", "property_identification"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m02",
        "skill_id": "9702_skill_drag_terminal_velocity",
        "accepted_answer": "A",
        "hints": [
            "Before the parachute opens, the parachutist accelerates from rest towards a first terminal velocity where drag equals weight.",
            "When the parachute opens, drag suddenly becomes much larger than weight, causing rapid deceleration to a new, much lower terminal velocity."
        ],
        "walkthrough": [
            "Initially, the parachutist accelerates from rest with decreasing acceleration (decreasing gradient) until reaching a first terminal speed.",
            "When the parachute opens, the large surface area creates a drag force much greater than weight, causing a sharp decrease in speed (steep negative gradient).",
            "As speed drops, drag decreases until drag again equals weight, establishing a new, lower constant terminal velocity. Graph A correctly depicts this complete progression."
        ]
    },
    10: {
        "difficulty": 2,
        "question_patterns": ["multi_step_calculation"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m01",
        "skill_id": "9702_skill_impulse_force_time",
        "accepted_answer": "C",
        "hints": [
            "Use the impulse-momentum theorem $F \\Delta t = \\Delta p = m \\Delta v$ to calculate the time in seconds.",
            "Convert the resulting time from seconds into minutes by dividing by 60."
        ],
        "walkthrough": [
            "The change in momentum required to bring the ship to rest from $u = 16.4\\text{ m s}^{-1}$ is $\\Delta p = m u = 8.4 \\times 10^7\\text{ kg} \\times 16.4\\text{ m s}^{-1} = 1.3776 \\times 10^9\\text{ N s}$.",
            "The time required under a constant stopping force of 920 000 N is $\\Delta t = \\frac{\\Delta p}{F} = \\frac{1.3776 \\times 10^9\\text{ N s}}{9.2 \\times 10^5\\text{ N}} \\approx 1497.4\\text{ s}$.",
            "Converting to minutes: $t = \\frac{1497.4}{60} \\approx 24.96\\text{ minutes} \\approx 25\\text{ minutes}$ (Option C)."
        ]
    },
    11: {
        "difficulty": 2,
        "question_patterns": ["graph_interpretation", "property_identification"],
        "topic_id": "9702_t03",
        "module_id": "9702_t03_m02",
        "skill_id": "9702_skill_drag_terminal_velocity",
        "accepted_answer": "A",
        "hints": [
            "Identify the net force at the instant of release when velocity is zero.",
            "Consider how the viscous drag force changes as the sphere speeds up upward, and what happens to the acceleration."
        ],
        "walkthrough": [
            "At release ($t = 0$), velocity is zero, so viscous drag is zero. The net upward force is constant at $F_{\\text{net}} = U - W > 0$, giving a maximum initial upward acceleration (steep initial gradient on the $v-t$ graph).",
            "As the upward velocity $v$ increases, the downward resistive drag force increases, so the net upward force $F_{\\text{net}} = U - W - F_D$ decreases, causing the upward acceleration (gradient) to continuously decrease towards zero as terminal velocity is approached.",
            "Graph A correctly shows an increasing velocity curve with a decreasing gradient that approaches a constant terminal velocity."
        ]
    },
    12: {
        "difficulty": 2,
        "question_patterns": ["property_identification", "explanation"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m01",
        "skill_id": "9702_skill_moments_couples",
        "accepted_answer": "B",
        "hints": [
            "A system that produces 'only a torque' must have zero resultant linear force (i.e. forms a couple).",
            "Calculate the net force and total torque about the centre of the disc for each arrangement."
        ],
        "walkthrough": [
            "For a system to produce only a torque (no resultant linear force), the vector sum of all applied forces must be zero ($\\Sigma F = 0$), forming a pure couple.",
            "In arrangement B, two forces of equal magnitude $F$ act tangentially in opposite directions on opposite ends of a diameter (perpendicular distance $2R$).",
            "The resultant force is $F - F = 0$, and the torque produced about the centre is $\\tau = F \\times 2R = 2FR$, satisfying both conditions (Option B)."
        ]
    },
    13: {
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "vector_diagram_construction"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m02",
        "skill_id": "9702_skill_equilibrium_coplanar_forces",
        "accepted_answer": "D",
        "hints": [
            "The tension in the cable is uniform throughout and equals the load of 1830 N.",
            "Resolve the tension forces from both sections of the cable along the line of the jib to balance force $R$."
        ],
        "walkthrough": [
            "Since the pulley is frictionless, the tension in both cable segments is $T = 1830\\text{ N}$. Both segments make an angle of 35° with the axis of the jib.",
            "The total component of tension pulling inward along the line of the jib is $F_{\\text{jib}} = 2 \\times T \\cos(35^\\circ)$.",
            "For equilibrium, the reaction force $R$ along the jib equals $R = 2 \\times 1830 \\times \\cos(35^\\circ) = 3660 \\times 0.81915 \\approx 2998\\text{ N} \\approx 3000\\text{ N}$ (Option D)."
        ]
    },
    14: {
        "difficulty": 1,
        "question_patterns": ["property_identification", "classification"],
        "topic_id": "9702_t04",
        "module_id": "9702_t04_m03",
        "skill_id": "9702_skill_density_pressure",
        "accepted_answer": "D",
        "hints": [
            "Recall that density is defined as mass per unit volume ($\\rho = \\frac{m}{V}$).",
            "Check which option represents a unit of mass divided by a unit of volume."
        ],
        "walkthrough": [
            "Density has dimensions of $[\\text{mass}] \\times [\\text{length}]^{-3}$. In SI and derived units, mass can be measured in micrograms ($\\mu\\text{g}$) and volume in cubic millimetres ($\\text{mm}^3$).",
            "Option A ($\\text{N m}^{-3}$) is force per unit volume. Option B ($\\text{g mm}^{-1}$) is mass per unit length. Option C ($\\text{kg cm}^{-2}$) is mass per unit area. Option D ($\\mu\\text{g mm}^{-3}$) is mass per unit volume, which is a valid unit of density."
        ]
    },
    15: {
        "difficulty": 1,
        "question_patterns": ["property_identification", "explanation"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_conservation_of_energy",
        "accepted_answer": "D",
        "hints": [
            "Recall the law of conservation of energy: energy cannot be created or destroyed, only transferred or transformed.",
            "Consider whether friction destroys energy or simply converts mechanical work into thermal energy."
        ],
        "walkthrough": [
            "According to the principle of conservation of energy, the total energy in any closed system remains constant. In inelastic collisions, kinetic energy is converted to internal energy/sound, but total energy is conserved.",
            "When friction opposes motion in a machine, it transforms mechanical work into thermal energy (heat). Friction does not reduce or destroy total energy, making statement D incorrect."
        ]
    },
    16: {
        "difficulty": 1,
        "question_patterns": ["multi_step_calculation"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m01",
        "skill_id": "9702_skill_power_efficiency",
        "accepted_answer": "B",
        "hints": [
            "Calculate total electrical energy input using $E_{\\text{in}} = P \\times t$, converting time to seconds.",
            "Multiply the total input energy by the efficiency (0.650) to find the useful energy transferred to the water."
        ],
        "walkthrough": [
            "The time in seconds is $t = 2.00\\text{ minutes} \\times 60\\text{ s} = 120\\text{ s}$. The total electrical energy input is $E_{\\text{in}} = P_{\\text{in}} \\times t = 1.50 \\times 10^3\\text{ W} \\times 120\\text{ s} = 1.80 \\times 10^5\\text{ J} = 180\\text{ kJ}$.",
            "The useful energy transferred to the water is $E_{\\text{useful}} = \\text{efficiency} \\times E_{\\text{in}} = 0.650 \\times 180\\text{ kJ} = 117\\text{ kJ}$ (Option B)."
        ]
    },
    17: {
        "difficulty": 1,
        "question_patterns": ["multi_step_calculation", "direct_calculation"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m02",
        "skill_id": "9702_skill_work_done",
        "accepted_answer": "C",
        "hints": [
            "Calculate force $F$ using work done: $W = F d$.",
            "Use $F = mg$ to find the gravitational field strength $g$ from the calculated force."
        ],
        "walkthrough": [
            "Work done by the gravitational field is $W = F d$. Rearranging gives $F = \\frac{W}{d} = \\frac{450\\text{ J}}{30\\text{ m}} = 15\\text{ N}$.",
            "The gravitational force on mass $m = 6.0\\text{ kg}$ is $F = mg$, so the acceleration of free fall is $g = \\frac{F}{m} = \\frac{15\\text{ N}}{6.0\\text{ kg}} = 2.5\\text{ m s}^{-2}$.",
            "Thus $F = 15\\text{ N}$ and $g = 2.5\\text{ m s}^{-2}$ (Option C)."
        ]
    },
    18: {
        "difficulty": 1,
        "question_patterns": ["multi_step_calculation"],
        "topic_id": "9702_t05",
        "module_id": "9702_t05_m02",
        "skill_id": "9702_skill_power_efficiency",
        "accepted_answer": "C",
        "hints": [
            "Find the total vertical height gained by multiplying the number of steps by the height of each step in metres.",
            "Calculate the useful work done against gravity ($W = mgh$) and divide by time to determine average power."
        ],
        "walkthrough": [
            "The total vertical height climbed is $h = 20 \\times 0.25\\text{ m} = 5.0\\text{ m}$.",
            "The useful work done against gravity is $\\Delta E_p = mgh = 50\\text{ kg} \\times 9.81\\text{ m s}^{-2} \\times 5.0\\text{ m} = 2452.5\\text{ J}$.",
            "The useful average power output is $P = \\frac{\\Delta E_p}{t} = \\frac{2452.5\\text{ J}}{7.0\\text{ s}} \\approx 350.4\\text{ W} \\approx 350\\text{ W}$ (Option C)."
        ]
    },
    19: {
        "difficulty": 2,
        "question_patterns": ["graph_interpretation", "multi_step_calculation"],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m01",
        "skill_id": "9702_skill_young_modulus",
        "accepted_answer": "D",
        "hints": [
            "Calculate the cross-sectional area of the wire from its diameter $d = 0.25\\text{ mm}$ using $A = \\frac{\\pi d^2}{4}$.",
            "Determine the gradient or extension $\\Delta x$ for a change in force $\\Delta F$ from the scale reading graph, then use $E = \\frac{F L}{A \\Delta x}$."
        ],
        "walkthrough": [
            "The cross-sectional area of the wire is $A = \\frac{\\pi d^2}{4} = \\frac{\\pi (0.25 \\times 10^{-3}\\text{ m})^2}{4} \\approx 4.909 \\times 10^{-8}\\text{ m}^2$.",
            "From the graph, for an applied force increase of $\\Delta F = 10\\text{ N}$, the marker position increases by $\\Delta x = 3.44\\text{ mm} = 3.44 \\times 10^{-3}\\text{ m}$.",
            "Using the Young modulus formula $E = \\frac{\\sigma}{\\varepsilon} = \\frac{\\Delta F \\times L}{A \\times \\Delta x}$ with initial length $L = 3.70\\text{ m}$ gives $E = \\frac{10\\text{ N} \\times 3.70\\text{ m}}{4.909 \\times 10^{-8}\\text{ m}^2 \\times 3.44 \\times 10^{-3}\\text{ m}} \\approx 2.19 \\times 10^{11}\\text{ Pa} \\approx 2.2 \\times 10^{11}\\text{ Pa}$ (Option D)."
        ]
    },
    20: {
        "difficulty": 1,
        "question_patterns": ["graph_interpretation", "property_identification"],
        "topic_id": "9702_t06",
        "module_id": "9702_t06_m02",
        "skill_id": "9702_skill_elastic_plastic_behaviour",
        "accepted_answer": "B",
        "hints": [
            "Recall the physical meaning of the area under a force-extension graph.",
            "Distinguish between total work done during deformation and recoverable elastic strain energy when plastic deformation occurs."
        ],
        "walkthrough": [
            "The total area under any force-extension graph represents the work done in stretching the material ($\\int F \\, dx$).",
            "Beyond the elastic limit (from Q to R), deformation is plastic, so not all of this work is stored as recoverable strain energy (some is dissipated as heat). Therefore, statement B is definitively correct while A is incorrect."
        ]
    },
    21: {
        "difficulty": 1,
        "question_patterns": ["direct_calculation", "property_identification"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_wave_intensity_amplitude",
        "accepted_answer": "D",
        "hints": [
            "Recall the proportionality relationship between the intensity $I$ and amplitude $x_0$ of a progressive wave.",
            "Calculate the new intensity when the amplitude is scaled by a factor of 3."
        ],
        "walkthrough": [
            "The intensity $I$ of a progressive wave is directly proportional to the square of its amplitude: $I \\propto A^2$.",
            "When the amplitude increases by a factor of 3 from $x_0$ to $3x_0$, the intensity increases by a factor of $3^2 = 9$.",
            "Thus, the new intensity is $9I$ (Option D)."
        ]
    },
    22: {
        "difficulty": 2,
        "question_patterns": ["graph_interpretation", "motion_path_representation"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m02",
        "skill_id": "9702_skill_progressive_wave_properties",
        "accepted_answer": "B",
        "hints": [
            "Find the time period $T$ of the wave using $T = \\frac{1}{f}$ and compare $t = 1\\text{ s}$ to $T$.",
            "Remember that in a transverse wave, particles only oscillate vertically (perpendicular to wave propagation), not horizontally."
        ],
        "walkthrough": [
            "The period of the wave is $T = \\frac{1}{f} = \\frac{1}{0.5\\text{ Hz}} = 2.0\\text{ s}$. The elapsed time $t = 1.0\\text{ s}$ corresponds to half a period ($t = \\frac{T}{2}$).",
            "In a transverse wave, particle X only oscillates vertically up and down at fixed position $x$. In half a cycle ($\\pi$ radians phase change), a particle at a positive peak moves to the opposite extreme displacement (a negative trough).",
            "This corresponds to position B directly below the original position of X."
        ]
    },
    23: {
        "difficulty": 1,
        "question_patterns": ["graph_interpretation", "direct_calculation"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m01",
        "skill_id": "9702_skill_oscilloscope_traces",
        "accepted_answer": "B",
        "hints": [
            "Determine the number of horizontal divisions occupied by one full wave cycle on the oscilloscope screen.",
            "Multiply the number of divisions by the time-base setting ($0.20\\text{ ms/div}$) to find the period $T$, then compute $f = \\frac{1}{T}$."
        ],
        "walkthrough": [
            "From the trace on the c.r.o. screen, one complete wave cycle spans 4.0 horizontal divisions.",
            "With the time-base set to $0.20\\text{ ms per division}$, the time period is $T = 4.0\\text{ div} \\times 0.20\\text{ ms div}^{-1} = 0.80\\text{ ms} = 8.0 \\times 10^{-4}\\text{ s}$.",
            "The frequency is $f = \\frac{1}{T} = \\frac{1}{8.0 \\times 10^{-4}\\text{ s}} = 1250\\text{ Hz}$ (Option B)."
        ]
    },
    24: {
        "difficulty": 1,
        "question_patterns": ["direct_calculation"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m03",
        "skill_id": "9702_skill_doppler_effect",
        "accepted_answer": "D",
        "hints": [
            "Use the Doppler effect formula for an approaching source: $f_o = f_s \\left(\\frac{v}{v - v_s}\\right)$.",
            "Substitute the speed of sound $v = 330\\text{ m s}^{-1}$, source speed $v_s = 25.0\\text{ m s}^{-1}$, and source frequency $f_s = 40.0\\text{ kHz}$."
        ],
        "walkthrough": [
            "The observed frequency for a source moving directly towards a stationary observer is given by $f_o = f_s \\left(\\frac{v}{v - v_s}\\right)$.",
            "Substituting the given values: $f_o = 40.0\\text{ kHz} \\times \\left(\\frac{330\\text{ m s}^{-1}}{330\\text{ m s}^{-1} - 25.0\\text{ m s}^{-1}}\\right) = 40.0 \\times \\frac{330}{305} \\approx 43.28\\text{ kHz} \\approx 43.3\\text{ kHz}$.",
            "Thus, the detector records a frequency of 43.3 kHz (Option D)."
        ]
    },
    25: {
        "difficulty": 1,
        "question_patterns": ["classification", "property_identification"],
        "topic_id": "9702_t07",
        "module_id": "9702_t07_m04",
        "skill_id": "9702_skill_electromagnetic_spectrum",
        "accepted_answer": "B",
        "hints": [
            "Recall the approximate wavelength boundaries of the electromagnetic spectrum in metres.",
            "Compare $\\lambda = 1.0 \\times 10^{-7}\\text{ m} = 100\\text{ nm}$ against visible light (400 nm to 700 nm) and ultraviolet light (10 nm to 400 nm)."
        ],
        "walkthrough": [
            "Visible light spans wavelengths from approximately 400 nm ($4 \\times 10^{-7}\\text{ m}$) to 700 nm ($7 \\times 10^{-7}\\text{ m}$).",
            "The ultraviolet region spans from about 10 nm ($\\sim 10^{-8}\\text{ m}$) to 400 nm ($4 \\times 10^{-7}\\text{ m}$).",
            "A wavelength of $1.0 \\times 10^{-7}\\text{ m} = 100\\text{ nm}$ lies directly in the ultraviolet region (Option B)."
        ]
    },
    26: {
        "difficulty": 2,
        "question_patterns": ["property_identification", "explanation"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m01",
        "skill_id": "9702_skill_stationary_waves",
        "accepted_answer": "D",
        "hints": [
            "Recall that in a stationary wave, the amplitude of vibration depends on position, varying from 0 at nodes to maximum at antinodes.",
            "Consider the symmetry of sinusoidal loop profiles on either side of node $N_2$."
        ],
        "walkthrough": [
            "In a stationary wave, all particles oscillate with the same frequency. Particles between consecutive nodes vibrate in phase, while particles in adjacent loops vibrate in antiphase (phase difference $\\pi$).",
            "Because the waveform profile is symmetric around node $N_2$, points placed at equal distances on either side of $N_2$ experience identical vibration amplitudes.",
            "Thus, points equidistant from $N_2$ vibrate with the same frequency and the same amplitude (Option D)."
        ]
    },
    27: {
        "difficulty": 1,
        "question_patterns": ["definition", "classification"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m02",
        "skill_id": "9702_skill_wave_diffraction",
        "accepted_answer": "C",
        "hints": [
            "Recall the standard physics definition of wave diffraction.",
            "Identify the option describing a wave spreading into the geometrical shadow when encountering an aperture or obstacle."
        ],
        "walkthrough": [
            "Diffraction is defined as the spreading of waves as they pass through an aperture or around the edge of an obstacle.",
            "Option A describes reflection, Option B describes refraction, and Option D describes interference/superposition. Option C describes diffraction."
        ]
    },
    28: {
        "difficulty": 1,
        "question_patterns": ["explanation", "interference_analysis"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m03",
        "skill_id": "9702_skill_two_source_interference",
        "accepted_answer": "C",
        "hints": [
            "Consider what happens when two coherent sound waves from identical loudspeakers overlap in space.",
            "Alternating loud and quiet regions arise from path difference creating constructive and destructive superposition."
        ],
        "walkthrough": [
            "The two loudspeakers connected to the same signal generator act as coherent sound sources.",
            "As the observer walks along line PQ, the path difference from the two speakers changes continuously, resulting in alternating regions of constructive interference (loud) and destructive interference (quiet).",
            "This variation in loudness is caused by two-source wave interference (Option C)."
        ]
    },
    29: {
        "difficulty": 1,
        "question_patterns": ["direct_calculation", "equation_derivation"],
        "topic_id": "9702_t08",
        "module_id": "9702_t08_m04",
        "skill_id": "9702_skill_diffraction_grating",
        "accepted_answer": "B",
        "hints": [
            "Use the diffraction grating equation $d \\sin\\theta = n \\lambda$.",
            "Equate $d \\sin\\theta$ for the second-order ($n_1 = 2$) and third-order ($n_2 = 3$) wavelengths at the same angle $\\theta$."
        ],
        "walkthrough": [
            "The diffraction grating equation is $d \\sin\\theta = n \\lambda$. For overlapping spectral lines at the same diffraction angle $\\theta$, the product $n \\lambda$ is equal.",
            "Setting $n_1 \\lambda_1 = n_2 \\lambda_2$ with $n_1 = 2$, $\\lambda_1 = 600\\text{ nm}$, and $n_2 = 3$: $2 \\times 600\\text{ nm} = 3 \\times \\lambda_2$.",
            "Solving for $\\lambda_2$ gives $\\lambda_2 = \\frac{1200\\text{ nm}}{3} = 400\\text{ nm}$ (Option B)."
        ]
    },
    30: {
        "difficulty": 1,
        "question_patterns": ["electric_field_line_construction", "property_identification"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_uniform_electric_fields",
        "accepted_answer": "B",
        "hints": [
            "Recall the directional convention for electric field lines relative to electric potential.",
            "Electric field lines point in the direction of decreasing potential (from high potential to low potential) and are uniform (parallel and equally spaced) between parallel plates."
        ],
        "walkthrough": [
            "The electric field between two parallel conducting plates is uniform, represented by parallel, equally spaced straight lines perpendicular to the plates.",
            "Electric field lines always point from higher electric potential towards lower electric potential (i.e. from $+1300\\text{ V}$ towards $+800\\text{ V}$).",
            "Diagram B correctly represents parallel field lines directed from the $+1300\\text{ V}$ plate towards the $+800\\text{ V}$ plate."
        ]
    },
    31: {
        "difficulty": 2,
        "question_patterns": ["direct_calculation", "property_identification"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m02",
        "skill_id": "9702_skill_uniform_electric_fields",
        "accepted_answer": "D",
        "hints": [
            "Calculate the electric field strength using $E = \\frac{V}{d}$, with $d$ in metres.",
            "Determine the direction of the electric field by remembering that field lines point from higher potential ($0\\text{ V}$ at plate Q) to lower potential ($-700\\text{ V}$ at plate P)."
        ],
        "walkthrough": [
            "The magnitude of the uniform electric field is $E = \\frac{\\Delta V}{d} = \\frac{700\\text{ V}}{5.0 \\times 10^{-3}\\text{ m}} = 1.4 \\times 10^5\\text{ V m}^{-1} = 1.4 \\times 10^5\\text{ N C}^{-1}$.",
            "Electric field lines point from higher potential to lower potential. Plate Q is at $0\\text{ V}$ and plate P is at $-700\\text{ V}$, so the field direction is from Q towards P.",
            "Therefore, the field is $1.4 \\times 10^5\\text{ N C}^{-1}$ directed from Q towards P (Option D)."
        ]
    },
    32: {
        "difficulty": 1,
        "question_patterns": ["definition", "property_identification"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m01",
        "skill_id": "9702_skill_electric_current_drift_speed",
        "accepted_answer": "A",
        "hints": [
            "Recall the microscopic current transport equation $I = Anvq$.",
            "Identify the physical meaning of each variable: $A$ is area, $n$ is charge carrier number density, $q$ is carrier charge, and $v$ is velocity."
        ],
        "walkthrough": [
            "In the transport equation $I = Anvq$, $I$ is electric current, $A$ is cross-sectional area, $n$ is number density of free charge carriers, and $q$ is charge per carrier.",
            "The symbol $v$ represents the average (mean) drift velocity of the charge carriers along the conductor (Option A)."
        ]
    },
    33: {
        "difficulty": 2,
        "question_patterns": ["circuit_analysis", "multi_step_calculation"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_resistor_networks",
        "accepted_answer": "B",
        "hints": [
            "Identify which resistor carries the maximum current and will reach its 4.0 W power limit first.",
            "Calculate the maximum allowed total circuit current from $P = I^2 R$, find the total equivalent resistance between X and Y, and compute $V = I_{\\text{total}} R_{\\text{eq}}$."
        ],
        "walkthrough": [
            "The circuit consists of a parallel pair of two 100 Ω resistors in series with a single 100 Ω resistor. The total circuit current $I$ passes entirely through the single 100 Ω series resistor, whereas each parallel resistor carries only $\\frac{I}{2}$.",
            "The series resistor reaches the maximum power rating of 4.0 W first: $P = I^2 R \\implies 4.0 = I^2 (100) \\implies I = \\sqrt{\\frac{4.0}{100}} = 0.20\\text{ A}$.",
            "The total equivalent resistance of the arrangement is $R_{\\text{eq}} = \\left(\\frac{100 \\times 100}{100 + 100}\\right) + 100 = 50 + 100 = 150\\,\\Omega$.",
            "The maximum safe voltage across XY is $V_{\\text{max}} = I \\times R_{\\text{eq}} = 0.20\\text{ A} \\times 150\\,\\Omega = 30\\text{ V}$ (Option B)."
        ]
    },
    34: {
        "difficulty": 1,
        "question_patterns": ["direct_calculation"],
        "topic_id": "9702_t09",
        "module_id": "9702_t09_m03",
        "skill_id": "9702_skill_resistivity",
        "accepted_answer": "C",
        "hints": [
            "Use the resistivity formula $R = \\frac{\\rho L}{A}$.",
            "Substitute $\\rho = 2.30 \\times 10^{-8}\\,\\Omega\\text{ m}$, $L = 2.50 \\times 10^{-3}\\text{ m}$, and $A = 6.25 \\times 10^{-8}\\text{ m}^2$."
        ],
        "walkthrough": [
            "The resistance of a uniform conductor is given by $R = \\frac{\\rho L}{A}$.",
            "Substituting the given parameters: $R = \\frac{2.30 \\times 10^{-8}\\,\\Omega\\text{ m} \\times 2.50 \\times 10^{-3}\\text{ m}}{6.25 \\times 10^{-8}\\text{ m}^2} = \\frac{5.75 \\times 10^{-11}}{6.25 \\times 10^{-8}} = 0.92 \\times 10^{-3}\\,\\Omega = 9.2 \\times 10^{-4}\\,\\Omega$ (Option C)."
        ]
    },
    35: {
        "difficulty": 2,
        "question_patterns": ["circuit_analysis", "multi_step_calculation"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_emf_internal_resistance",
        "accepted_answer": "A",
        "hints": [
            "Calculate total resistance and circuit current for both cases: when variable resistance $R_v = 0\\,\\Omega$ and when $R_v = 40\\,\\Omega$.",
            "Calculate the power dissipated in resistor X ($P = I^2 R_X$) for each case and find the difference."
        ],
        "walkthrough": [
            "Case 1 ($R_v = 0\\,\\Omega$): Total circuit resistance is $R_{\\text{total},1} = 40 + 0 + 2.0 = 42.0\\,\\Omega$. Current is $I_1 = \\frac{12\\text{ V}}{42.0\\,\\Omega} = \\frac{2}{7}\\text{ A}$. Power in X is $P_1 = I_1^2 R_X = \\left(\\frac{2}{7}\right)^2 \\times 40 = \\frac{160}{49} \\approx 3.27\\text{ W}$.",
            "Case 2 ($R_v = 40\\,\\Omega$): Total circuit resistance is $R_{\\text{total},2} = 40 + 40 + 2.0 = 82.0\\,\\Omega$. Current is $I_2 = \\frac{12\\text{ V}}{82.0\\,\\Omega} = \\frac{6}{41}\\text{ A}$. Power in X is $P_2 = I_2^2 R_X = \\left(\\frac{6}{41}\right)^2 \\times 40 = \\frac{1440}{1681} \\approx 0.86\\text{ W}$.",
            "The change in power dissipated in resistor X is $\\Delta P = P_1 - P_2 = 3.265\\text{ W} - 0.857\\text{ W} \\approx 2.41\\text{ W} \\approx 2.4\\text{ W}$ (Option A)."
        ]
    },
    36: {
        "difficulty": 2,
        "question_patterns": ["circuit_analysis", "comparison"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m01",
        "skill_id": "9702_skill_resistor_networks",
        "accepted_answer": "D",
        "hints": [
            "Calculate the total equivalent resistance for each network in terms of the individual resistance $R$.",
            "Rank the networks from lowest total resistance to highest total resistance."
        ],
        "walkthrough": [
            "Evaluating the equivalent resistance of each configuration: Network X (three identical resistors in parallel) has $R_X = \\frac{R}{3} \\approx 0.33R$.",
            "Network Y (two resistors in series connected in parallel with the third) has $R_Y = \\frac{2R \\times R}{2R + R} = \\frac{2}{3}R \\approx 0.67R$.",
            "Network Z (two resistors in parallel connected in series with the third) has $R_Z = \\frac{R}{2} + R = 1.5R$. Network W (three resistors in series) has $R_W = 3R$.",
            "In order of increasing total resistance: $R_X < R_Y < R_Z < R_W$, giving $X \\to Y \\to Z \\to W$ (Option D)."
        ]
    },
    37: {
        "difficulty": 2,
        "question_patterns": ["circuit_analysis", "multi_step_calculation"],
        "topic_id": "9702_t10",
        "module_id": "9702_t10_m03",
        "skill_id": "9702_skill_potential_dividers",
        "accepted_answer": "C",
        "hints": [
            "An ammeter reading of zero means no current passes through the detector bridge branch.",
            "Set up the potential divider equations across the branches to balance the potential difference against the branch voltage."
        ],
        "walkthrough": [
            "When the ammeter reads zero, no current flows through the ammeter branch, so the circuit functions as two independent potential dividers connected to the common reference.",
            "The potential division in the parallel branches requires the potential across the 50 Ω resistor to balance the circuit node potential: $\\frac{50}{R + 50} \\times 24\\text{ V} = V_{\\text{balance}}$.",
            "With $V_{\\text{balance}} = 2.67\\text{ V}$ established by the divider network, $\\frac{50}{R + 50} = \\frac{2.67}{24} = \\frac{1}{9} \\implies R + 50 = 450 \\implies R = 400\\,\\Omega$ (Option C)."
        ]
    },
    38: {
        "difficulty": 1,
        "question_patterns": ["equation_completion", "direct_calculation"],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m01",
        "skill_id": "9702_skill_nuclear_decay_equations",
        "accepted_answer": "C",
        "hints": [
            "Apply the law of conservation of nucleon number (mass number $A$) and proton number (atomic number $Z$).",
            "Calculate the remaining mass number and atomic number required for particle $x$."
        ],
        "walkthrough": [
            "Conservation of nucleon number requires: $A: 235 + 1 = 154 + 80 + A_x \\implies 236 = 234 + A_x \\implies A_x = 2$.",
            "Conservation of proton number requires: $Z: 92 + 0 = 60 + 32 + Z_x \\implies 92 = 92 + Z_x \\implies Z_x = 0$.",
            "A total nucleon number of 2 with an atomic number of 0 represents two neutrons ($2 \\times {}_0^1\\text{n}$), corresponding to Option C."
        ]
    },
    39: {
        "difficulty": 1,
        "question_patterns": ["definition", "classification"],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m01",
        "skill_id": "9702_skill_nuclear_atom_scattering",
        "accepted_answer": "A",
        "hints": [
            "Recall the definition of isotopes of an element.",
            "Isotopes have the same atomic number (proton number, subscript $x$) but different mass numbers (nucleon number, superscript $y$)."
        ],
        "walkthrough": [
            "Isotopes are nuclei of the same chemical element that contain the identical number of protons ($Z = x$) but different numbers of neutrons, resulting in different mass numbers ($A \\ne y$).",
            "In Option A (${}_{x}^{y-1}\\text{Q}$), the proton number remains $x$ while the nucleon number is $y - 1$, which satisfies the definition of an isotope.",
            "Options B, C, and D change the proton number $x$, which represents different chemical elements rather than isotopes."
        ]
    },
    40: {
        "difficulty": 1,
        "question_patterns": ["particle_model_application", "property_identification"],
        "topic_id": "9702_t11",
        "module_id": "9702_t11_m02",
        "skill_id": "9702_skill_fundamental_particles_interactions",
        "accepted_answer": "A",
        "hints": [
            "Recall the quark composition of a neutron ($udd$) and a proton ($uud$).",
            "Identify the specific quark transformation that occurs during $\\beta^-$ decay ($\\text{n} \\to \\text{p} + \\text{e}^- + \\bar{\\nu}_e$)."
        ],
        "walkthrough": [
            "A neutron consists of one up quark and two down quarks ($udd$), while a proton consists of two up quarks and one down quark ($uud$).",
            "During $\\beta^-$ decay, a down quark changes into an up quark: $d \\to u + \\text{e}^- + \\bar{\\nu}_e$.",
            "Consequently, inside the nucleus, the total number of down quarks decreases by one and the number of up quarks increases by one (Option A)."
        ]
    }
}

target_dir = Path("subjects/physics/9702/enrichment/p1")
target_dir.mkdir(parents=True, exist_ok=True)

for qnum in range(1, 41):
    q_id = f"9702_w18_13_q{qnum:02d}"
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

print("Successfully wrote 40 enrichment files.")

