"""
generate_9702_m19_12.py

Generates P1 enrichment files for Cambridge AS Level Physics 9702 paper 9702_m19_12 (Q01-Q40).
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "subjects/physics/9702/enrichment/p1"
OUT_DIR.mkdir(parents=True, exist_ok=True)

data = [
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q01",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "direct_calculation",
      "property_identification"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m02",
    "skill_id": "9702_skill_define_period",
    "accepted_answer": "A",
    "hints": [
      "Recall the relationship between wave frequency $f$ and period $T$, namely $T = \\frac{1}{f}$.",
      "Convert the frequency from gigahertz to hertz using the SI prefix multiplier $f = 1\\text{ GHz} = 10^9\\text{ Hz}$, then express the calculated time in picoseconds ($t = 1\\text{ ps} = 10^{-12}\\text{ s}$)."
    ],
    "walkthrough": [
      "The period $T$ is the reciprocal of the frequency $f$: $T = \\frac{1}{f}$.",
      "Substitute the frequency $f = 5\\text{ GHz} = 5 \\times 10^9\\text{ Hz}$ into the equation: $T = \\frac{1}{5 \\times 10^9\\text{ s}^{-1}} = 0.2 \\times 10^{-9}\\text{ s} = 2.0 \\times 10^{-10}\\text{ s}$.",
      "Convert the period into picoseconds using the prefix $t = 1\\text{ ps} = 10^{-12}\\text{ s}$: $T = 2.0 \\times 10^{-10}\\text{ s} = 200 \\times 10^{-12}\\text{ s} = 200\\text{ ps}$, which corresponds to option A.",
      "Option B ($T = 2\\text{ ns} = 2 \\times 10^{-9}\\text{ s}$) and Option C ($T = 20\\text{ ns} = 2 \\times 10^{-8}\\text{ s}$) result from incorrect power-of-ten prefix conversions. Option D ($T = 20000\\text{ }\\mu\\text{s} = 2 \\times 10^{-2}\\text{ s}$) is much too large."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q02",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "equation_derivation",
      "direct_calculation"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m02",
    "skill_id": "9702_skill_derive_si_base_units",
    "accepted_answer": "B",
    "hints": [
      "Rearrange the given relationship $c = b T^3$ to make the constant $b$ the subject: $b = \\frac{c}{T^3}$.",
      "Convert the derived unit of specific heat capacity $\\text{J kg}^{-1}\\text{ K}^{-1}$ into SI base units by expressing the joule ($\\text{J}$) in terms of kilograms, metres, and seconds, then divide by $\\text{K}^3$."
    ],
    "walkthrough": [
      "First express the unit of energy (joule) in SI base units using the work formula $W = F s = m a s$: $1\\text{ J} = 1\\text{ N m} = (1\\text{ kg m s}^{-2}) \\times \\text{m} = 1\\text{ kg m}^2\\text{ s}^{-2}$.",
      "Next, substitute the base units of the joule into the units of specific heat capacity $c$: $[c] = \\text{J kg}^{-1}\\text{ K}^{-1} = (\\text{kg m}^2\\text{ s}^{-2})\\text{ kg}^{-1}\\text{ K}^{-1} = \\text{m}^2\\text{ s}^{-2}\\text{ K}^{-1}$.",
      "From the given equation $c = b T^3$, the constant $b$ is given by $b = \\frac{c}{T^3}$, where temperature $T$ has base unit kelvin ($\\text{K}$).",
      "Dividing the units of $c$ by $[T^3] = \\text{K}^3$ yields $[b] = \\frac{\\text{m}^2\\text{ s}^{-2}\\text{ K}^{-1}}{\\text{K}^3} = \\text{m}^2\\text{ s}^{-2}\\text{ K}^{-4}$, matching option B.",
      "Option A ($\\text{m}^2\\text{ s}^{-2}\\text{ K}^{-3}$) omits the temperature unit already present in $c$. Options C and D incorrectly retain kilograms in the base unit expression."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q03",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "vector_diagram_construction",
      "direct_calculation"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m04",
    "skill_id": "9702_skill_resolve_velocity_components",
    "accepted_answer": "D",
    "hints": [
      "Construct a velocity vector triangle where the resultant velocity relative to the ground points due north: $\\vec{v}_{\\text{ground}} = \\vec{v}_{\\text{aircraft}} + \\vec{v}_{\\text{wind}}$.",
      "The wind blows from the west (meaning eastward at speed $v_w = 85.0\\text{ km h}^{-1}$), so the aircraft must head at an angle $\\theta$ west of north such that its westward component equals $v_w = 85.0\\text{ km h}^{-1}$."
    ],
    "walkthrough": [
      "The wind blows from the west towards the east with speed $v_{\\text{wind}} = 85.0\\text{ km h}^{-1}$. To ensure the resultant motion relative to the ground is due north, the eastward velocity component contributed by the wind must be cancelled by a westward component of the aircraft airspeed.",
      "The aircraft has an airspeed of $v_{\\text{air}} = 200\\text{ km h}^{-1}$ directed at an angle $\\theta$ west of north.",
      "In the right-angled velocity triangle, the hypotenuse is the airspeed ($v_{\\text{air}} = 200\\text{ km h}^{-1}$) and the opposite side is the wind speed ($v_{\\text{wind}} = 85.0\\text{ km h}^{-1}$), giving $\\sin\\theta = \\frac{v_{\\text{wind}}}{v_{\\text{air}}} = \\frac{85.0}{200} = 0.425$.",
      "Calculate the angle: $\\theta = \\arcsin(0.425) \\approx 25.15^\\circ \\approx 25.2^\\circ$. The required heading is therefore $\\theta = 25.2^\\circ$ west of north (option D).",
      "Steering east of north (options A and C) would increase the eastward drift rather than cancelling it. Option B (heading $\\theta = 23.0^\\circ$) is obtained by incorrectly using $\\tan\\theta = \\frac{85.0}{200}$."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q04",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "property_identification"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m03",
    "skill_id": "9702_skill_interpret_graphs",
    "accepted_answer": "A",
    "hints": [
      "Identify the coordinates specified for the circuit: at weight $W = 5\\text{ N}$, current $I = 0.5\\text{ mA}$; at weight $W = 30\\text{ N}$, current $I = 2.0\\text{ mA}$.",
      "Check the behavior at zero load and inspect whether the current increases or decreases with increasing weight on each graph."
    ],
    "walkthrough": [
      "When no weight is placed on the balance ($W = 0\\text{ N}$), the output current should be zero, passing through the origin $(0, 0)$.",
      "As weight increases, the generated current must increase, reaching $I = 0.5\\text{ mA}$ at $W = 5\\text{ N}$ and $I = 2.0\\text{ mA}$ at $W = 30\\text{ N}$.",
      "In Graph A, current increases with a decreasing gradient from $(0, 0)$ to $(30\\text{ N}, 2.0\\text{ mA})$. At $W = 5\\text{ N}$ (one-sixth of the maximum weight), the current is about $I = 0.5\\text{ mA}$ (one-fourth of the maximum current), which matches the calibration data.",
      "Graphs B and D show current decreasing with weight, which contradicts the sensor operation. Graph C shows an increasing gradient (exponentially rising) where current at $W = 5\\text{ N}$ would be far lower than $0.5\\text{ mA}$.",
      "Therefore, graph A correctly represents the calibration curve."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q05",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "comparison",
      "uncertainty_analysis"
    ],
    "topic_id": "9702_t01",
    "module_id": "9702_t01_m03",
    "skill_id": "9702_skill_define_accuracy",
    "accepted_answer": "B",
    "hints": [
      "Accuracy measures how close an experimental reading is to the true value ($t_{\\text{true}} = 1.734\\text{ s}$).",
      "Calculate the absolute deviation $|t_{\\text{measured}} - t_{\\text{true}}|$ for each student to determine which reading has the smallest error."
    ],
    "walkthrough": [
      "Accuracy is defined as the closeness of agreement between a measured value and the true value ($t = 1.734\\text{ s}$).",
      "Calculate the absolute difference for each measurement from the true value:",
      "Student A ($t = 1\\text{ s}$): $|1 - 1.734| = 0.734\\text{ s}$.",
      "Student B ($t = 1.7\\text{ s}$): $|1.7 - 1.734| = 0.034\\text{ s}$.",
      "Student C ($t = 1.83\\text{ s}$): $|1.83 - 1.734| = 0.096\\text{ s}$.",
      "Student D ($t = 1.604\\text{ s}$): $|1.604 - 1.734| = 0.130\\text{ s}$.",
      "Student B has the smallest deviation ($0.034\\text{ s}$), making reading B the most accurate (option B). Note that while D has more decimal places (higher precision), precision does not guarantee accuracy."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q06",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "property_identification"
    ],
    "topic_id": "9702_t02",
    "module_id": "9702_t02_m01",
    "skill_id": "9702_skill_determine_acceleration_from_velocity_time_graph",
    "accepted_answer": "A",
    "hints": [
      "Recall that instantaneous velocity is given by the gradient of the displacement-time graph: $v = \\frac{ds}{dt}$.",
      "Inspect the gradient of the given displacement graph: at $t = 0$, the mass is at its lowest turning point where the slope is zero, then it moves upward with positive slope."
    ],
    "walkthrough": [
      "Velocity is the rate of change of displacement, represented by the gradient (slope) of the displacement-time graph.",
      "At $t = 0$, the mass is released from its maximum downward displacement where the tangent is horizontal, so initial velocity is $v = 0$.",
      "As the mass moves upward toward the equilibrium position, the gradient is positive (upward velocity) and reaches its maximum positive value when displacement crosses zero.",
      "At the top of the bounce (maximum upward displacement), the slope becomes horizontal again, meaning $v = 0$.",
      "During downward motion, the slope is negative, reaching a peak downward velocity before returning to zero at the bottom.",
      "This produces a standard positive sine waveform starting from zero at $t = 0$, which matches graph A exactly.",
      "Graph B starts at maximum velocity. Graphs C and D have incorrect frequencies or rectified shapes."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q07",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t02",
    "module_id": "9702_t02_m01",
    "skill_id": "9702_skill_recall_acceleration_of_free_fall",
    "accepted_answer": "C",
    "hints": [
      "Set upward as the positive direction: vertical displacement is $s = -12\\text{ m}$, acceleration is $a = -g = -9.81\\text{ m s}^{-2}$, and time of flight is $t = 3.4\\text{ s}$.",
      "Substitute these values into the kinematic equation $s = u t + \\frac{1}{2} a t^2$ and solve for initial speed $u$."
    ],
    "walkthrough": [
      "Taking upwards as positive, the final displacement of the stone when it reaches the sea is $s = -12\\text{ m}$.",
      "The stone accelerates under gravity with $a = -9.81\\text{ m s}^{-2}$ over a total time interval of $t = 3.4\\text{ s}$.",
      "Apply the equation of motion: $s = u t + \\frac{1}{2} a t^2$.",
      "Substitute known quantities: $-12 = u(3.4) + \\frac{1}{2}(-9.81)(3.4)^2$.",
      "Evaluate the acceleration term: $\\frac{1}{2}(-9.81)(11.56) = -56.70\\text{ m}$.",
      "Rearrange the equation: $3.4 u = -12 + 56.70 = 44.70$, which gives $u = \\frac{44.70}{3.4} \\approx 13.15\\text{ m s}^{-1} \\approx 13\\text{ m s}^{-1}$ (option C).",
      "Option A ($u = 3.5\\text{ m s}^{-1}$), Option B ($u = 6.6\\text{ m s}^{-1}$), and Option D ($u = 20\\text{ m s}^{-1}$) arise from sign errors in displacement or forgetting the quadratic time term."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q08",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "property_identification"
    ],
    "topic_id": "9702_t03",
    "module_id": "9702_t03_m03",
    "skill_id": "9702_skill_calculate_relative_speed",
    "accepted_answer": "B",
    "hints": [
      "In a perfectly elastic one-dimensional collision, the relative speed of approach equals the relative speed of separation: $u_{\\text{approach}} = v_{\\text{separation}}$.",
      "Calculate the initial relative speed of approach ($u_X - u_Y$) and equate it to $v_Y - v_X$, noting that ball Y moves to the right after impact at $v_Y = +7\\text{ m s}^{-1}$."
    ],
    "walkthrough": [
      "Define the direction to the right as positive. The initial velocities are $u_X = +5\\text{ m s}^{-1}$ (to the right) and $u_Y = -15\\text{ m s}^{-1}$ (to the left).",
      "The relative speed of approach before the collision is $u_{\\text{approach}} = u_X - u_Y = 5 - (-15) = 20\\text{ m s}^{-1}$.",
      "For a perfectly elastic collision, the relative speed of separation after the collision must equal the relative speed of approach: $v_{\\text{separation}} = v_Y - v_X = 20\\text{ m s}^{-1}$.",
      "We are given that ball Y moves to the right after the collision with velocity $v_Y = +7\\text{ m s}^{-1}$.",
      "Substitute into the separation equation: $7 - v_X = 20 \\implies v_X = 7 - 20 = -13\\text{ m s}^{-1}$.",
      "The negative sign indicates that ball X moves to the left at a speed of $v_X = 13\\text{ m s}^{-1}$ (option B)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q09",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "explanation",
      "comparison"
    ],
    "topic_id": "9702_t03",
    "module_id": "9702_t03_m02",
    "skill_id": "9702_skill_identify_fluid_drag",
    "accepted_answer": "A",
    "hints": [
      "Consider the effect of air resistance on the horizontal and vertical motions separately.",
      "A horizontal drag force opposes the forward motion causing continuous deceleration, while an upward vertical drag force opposes gravity and reduces the downward acceleration."
    ],
    "walkthrough": [
      "In the absence of air resistance, the horizontal velocity remains constant at $v$ because there is no horizontal force, and the ball falls under constant downward acceleration $g$ in time $T = \\sqrt{\\frac{2h}{g}}$.",
      "When air resistance is present, a drag force opposes the instantaneous velocity vector.",
      "The horizontal component of drag acts opposite to the horizontal motion, continuously decelerating the ball so its horizontal velocity when landing is strictly less than $v$.",
      "The vertical component of drag acts upwards against the downward fall, making the net downward acceleration $a_y < g$.",
      "Because the downward acceleration is reduced below $g$, the ball takes a longer time to descend through the vertical height $h$, so the landing time is more than $T$ seconds.",
      "Hence, the ball lands with horizontal velocity less than $v$ after more than $T$ seconds (option A)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q10",
    "component": "P1",
    "difficulty": 3,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t03",
    "module_id": "9702_t03_m03",
    "skill_id": "9702_skill_define_linear_momentum",
    "accepted_answer": "C",
    "hints": [
      "Use the conservation of linear momentum to find the velocity $v_2$ of mass $2m$ after the collision: $p_{\\text{initial}} = p_{\\text{final}}$.",
      "Calculate total initial kinetic energy $E_{k,i}$ and total final kinetic energy $E_{k,f}$, then find the difference $\\Delta E_k = E_{k,i} - E_{k,f}$."
    ],
    "walkthrough": [
      "Taking motion to the right as positive, initial velocities are $u_1 = +2v$ for mass $m$ and $u_2 = -v$ for mass $2m$.",
      "Total initial momentum is $p_i = m(2v) + (2m)(-v) = 2mv - 2mv = 0$.",
      "Total initial kinetic energy is $E_{k,i} = \\frac{1}{2}m(2v)^2 + \\frac{1}{2}(2m)(-v)^2 = 2mv^2 + mv^2 = 3mv^2$.",
      "After the collision, the ball of mass $m$ rebounds with velocity $v_1 = -v$. By conservation of momentum: $p_f = m(-v) + (2m)v_2 = 0 \\implies 2m v_2 = mv \\implies v_2 = +\\frac{1}{2}v$.",
      "Total final kinetic energy is $E_{k,f} = \\frac{1}{2}m(-v)^2 + \\frac{1}{2}(2m)\\left(\\frac{1}{2}v\\right)^2 = \\frac{1}{2}mv^2 + \\frac{1}{4}mv^2 = \\frac{3}{4}mv^2$.",
      "Loss of kinetic energy is $\\Delta E_k = E_{k,i} - E_{k,f} = 3mv^2 - \\frac{3}{4}mv^2 = \\frac{9}{4}mv^2$, which corresponds to option C."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q11",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "property_identification",
      "explanation"
    ],
    "topic_id": "9702_t04",
    "module_id": "9702_t04_m03",
    "skill_id": "9702_skill_explain_upthrust",
    "accepted_answer": "C",
    "hints": [
      "Recall Archimedes principle: upthrust is equal to the weight of fluid displaced by the submerged object ($U = \\rho_{\\text{fluid}} g V$).",
      "Check how upthrust, weight, and drag force vary with depth when the ball travels at a constant speed in an incompressible liquid."
    ],
    "walkthrough": [
      "Upthrust on a fully submerged object is given by $U = \\rho g V$, where $\\rho$ is the density of the liquid, $g$ is the acceleration of free fall, and $V$ is the submerged volume of the ball.",
      "Assuming an incompressible liquid with uniform density, the displaced volume and liquid density remain constant at all depths, so the upthrust is constant with increasing depth (option C).",
      "Option A is incorrect because drag force depends on speed ($F_d \\propto v$ or $v^2$), and speed is constant.",
      "Option B is incorrect because for downward terminal velocity, vertical equilibrium requires $\\text{Weight} = \\text{Upthrust} + \\text{Drag force}$, meaning drag force equals weight minus upthrust.",
      "Option D is incorrect because at constant speed the net force is zero, so weight equals exactly the sum of drag force and upthrust."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q12",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t04",
    "module_id": "9702_t04_m01",
    "skill_id": "9702_skill_define_torque_of_couple",
    "accepted_answer": "D",
    "hints": [
      "Calculate the resistive torque produced by one carriage using $\\tau_1 = F \\times r$, where $F = 85.0\\text{ N}$ and $r = 3.20\\text{ m}$.",
      "Sum the resistive torques for all $N = 4$ carriages to determine the total opposing torque that the motor must supply to maintain constant rotational speed."
    ],
    "walkthrough": [
      "Each carriage moves in a circular path of radius $r = 3.20\\text{ m}$ and experiences an opposing tangential air resistance force of $F = 85.0\\text{ N}$.",
      "The resistive torque exerted by a single carriage about the central pole is $\\tau_1 = F r = 85.0\\text{ N} \\times 3.20\\text{ m} = 272\\text{ N m}$.",
      "Since there are $N = 4$ identical carriages, the total resistive torque acting on the system is $\\tau_{\\text{total}} = 4 \\times 272\\text{ N m} = 1088\\text{ N m} \\approx 1090\\text{ N m}$.",
      "To keep the system rotating at constant speed, the motor must apply a driving torque equal in magnitude to the total resistive torque, giving $\\tau = 1090\\text{ N m}$ (option D).",
      "Option B ($\\tau = 272\\text{ N m}$) accounts for only one carriage. Option C ($\\tau = 544\\text{ N m}$) accounts for only two carriages."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q13",
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
      "Take moments about the hinge O to eliminate unknown reaction forces at the wall.",
      "Set the clockwise moment of the beam weight equal to the anticlockwise moment of the vertical component of the cord tension: $W \\times \\frac{L}{2} = T \\sin(\\theta) \\times L$ with $\\theta = 30^\\circ$."
    ],
    "walkthrough": [
      "The beam OX is uniform, so its weight $W = 100\\text{ N}$ acts vertically downwards at its center of gravity, a distance of $\\frac{L}{2} = 2.0\\text{ m}$ from the hinge O.",
      "The cord is attached at the end X ($L = 4.0\\text{ m}$ from O) at an angle of $\\theta = 30^\\circ$ to the horizontal beam.",
      "Taking moments about the hinge O in rotational equilibrium: $\\sum \\tau_{\\text{clockwise}} = \\sum \\tau_{\\text{anticlockwise}}$.",
      "Clockwise moment due to beam weight: $\\tau_W = 100\\text{ N} \\times 2.0\\text{ m} = 200\\text{ N m}$.",
      "Anticlockwise moment due to cord tension: $\\tau_T = T \\sin(30^\\circ) \\times 4.0\\text{ m} = T \\times 0.50 \\times 4.0\\text{ m} = 2.0 T$.",
      "Equating the two moments: $2.0 T = 200 \\implies T = \\frac{200}{2.0} = 100\\text{ N}$ (option D).",
      "Option A ($T = 50\\text{ N}$) results from neglecting the angle $\\sin(30^\\circ)$ or using the wrong moment arm."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q14",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "equation_derivation",
      "direct_calculation"
    ],
    "topic_id": "9702_t04",
    "module_id": "9702_t04_m03",
    "skill_id": "9702_skill_define_pressure",
    "accepted_answer": "D",
    "hints": [
      "Find the volume of the hemisphere ($V = \\frac{1}{2} \\times \\frac{4}{3}\\pi r^3 = \\frac{2}{3}\\pi r^3$) and express its weight as $W = m g = \\rho V g$.",
      "Divide the weight by the contact area of the flat circular base ($A = \\pi r^2$) to find the average pressure $P = \\frac{W}{A}$."
    ],
    "walkthrough": [
      "A hemisphere has half the volume of a sphere of radius $r$: $V = \\frac{1}{2}\\left(\\frac{4}{3}\\pi r^3\\right) = \\frac{2}{3}\\pi r^3$.",
      "The mass of the hemisphere is $m = \\rho V = \\frac{2}{3}\\pi \\rho r^3$, and its weight is $W = m g = \\frac{2}{3}\\pi \\rho g r^3$.",
      "The flat surface resting on the table is a circular disc of radius $r$, so its contact area is $A = \\pi r^2$.",
      "Average pressure exerted on the table is defined as $P = \\frac{W}{A} = \\frac{\\frac{2}{3}\\pi \\rho g r^3}{\\pi r^2} = \\frac{2}{3}\\rho r g$.",
      "This matches option D exactly.",
      "Option A ($\\frac{1}{3}\\rho r^2$) and Option B ($\\frac{1}{3}\\rho r^2 g$) have incorrect volume coefficients and dimensional inconsistencies. Option C ($\\frac{2}{3}\\rho r$) is missing the acceleration of free fall $g$."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q15",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "definition",
      "explanation"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m01",
    "skill_id": "9702_skill_conservation_of_energy",
    "accepted_answer": "C",
    "hints": [
      "Recall the formal definition of the principle of conservation of energy.",
      "Energy cannot be created or destroyed, only converted from one form to another, meaning the total energy in an isolated/closed system is fixed."
    ],
    "walkthrough": [
      "The principle of conservation of energy states that energy cannot be created or destroyed, but can only be transformed from one form to another.",
      "In any closed (isolated) system where no energy enters or leaves, the total amount of energy remains constant over time (option C).",
      "Option A is nonsensical as energy cannot be created. Option B describes practical energy resource management rather than a fundamental physics principle. Option D describes an ideal 100% efficient machine, which is impossible due to dissipative losses."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q16",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m01",
    "skill_id": "9702_skill_apply_efficiency",
    "accepted_answer": "D",
    "hints": [
      "Calculate useful mechanical output power using $P_{\\text{out}} = F v = m g v$, where $m = 14000\\text{ kg}$ and $v = 3.2\\text{ m s}^{-1}$.",
      "Calculate total electrical input power using $P_{\\text{in}} = V I$, then determine efficiency $\\eta = \\frac{P_{\\text{out}}}{P_{\\text{in}}} \\times 100\\%$."
    ],
    "walkthrough": [
      "Useful mechanical output power required to lift the container at constant speed is $P_{\\text{out}} = F v = m g v$.",
      "Substitute values: $P_{\\text{out}} = 14000\\text{ kg} \\times 9.81\\text{ m s}^{-2} \\times 3.2\\text{ m s}^{-1} = 439488\\text{ W}$.",
      "Electrical input power supplied to the motor is $P_{\\text{in}} = V I = 2200\\text{ V} \\times 240\\text{ A} = 528000\\text{ W}$.",
      "Calculate efficiency: $\\eta = \\frac{P_{\\text{out}}}{P_{\\text{in}}} \\times 100\\% = \\frac{439488}{528000} \\times 100\\% \\approx 83.2\\% \\approx 83\\%$ (option D).",
      "Option A ($\\eta = 8.1\\%$) and Option B ($\\eta = 8.5\\%$) result from powers-of-ten arithmetic errors in evaluating the powers."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q17",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "equation_derivation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m01",
    "skill_id": "9702_skill_define_power",
    "accepted_answer": "B",
    "hints": [
      "Express power output in watts: $P_{\\text{out}} = 150\\text{ kW} = 150 \\times 10^3\\text{ W}$.",
      "Calculate power input as energy consumed per second: $P_{\\text{in}} = \\frac{20\\text{ litres} \\times 40\\text{ MJ litre}^{-1}}{1\\text{ hour}} = \\frac{20 \\times 40 \\times 10^6\\text{ J}}{60 \\times 60\\text{ s}}$, then form the ratio $\\frac{P_{\\text{out}}}{P_{\\text{in}}}$."
    ],
    "walkthrough": [
      "The useful power output is $P_{\\text{out}} = 150\\text{ kW} = 150 \\times 10^3\\text{ W}$.",
      "The total chemical energy consumed in one hour is $E = 20\\text{ litres} \\times 40\\text{ MJ litre}^{-1} = 20 \\times 40 \\times 10^6\\text{ J}$.",
      "Converting one hour to seconds ($t = 1\\text{ h} = 60 \\times 60\\text{ s}$), the input power is $P_{\\text{in}} = \\frac{E}{t} = \\frac{20 \\times 40 \\times 10^6}{60 \\times 60}\\text{ W}$.",
      "The ratio of power output to power input is: $\\frac{P_{\\text{out}}}{P_{\\text{in}}} = \\frac{150 \\times 10^3}{\\frac{20 \\times 40 \\times 10^6}{60 \\times 60}} = \\frac{150 \\times 10^3 \\times 60 \\times 60}{20 \\times 40 \\times 10^6}$.",
      "This algebraic expression corresponds exactly to option B."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q18",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t05",
    "module_id": "9702_t05_m01",
    "skill_id": "9702_skill_define_power",
    "accepted_answer": "D",
    "hints": [
      "To move vertically upwards at constant speed, the upward force provided must equal the total weight: $F = m g$.",
      "Calculate useful output power using $P = F v = m g v$, where $m = 120\\text{ kg}$ and $v = 2.5\\text{ m s}^{-1}$."
    ],
    "walkthrough": [
      "At constant vertical speed, the system is in dynamic equilibrium, so the required upward lifting force equals the total gravitational force (weight): $F = m g = 120\\text{ kg} \\times 9.81\\text{ m s}^{-2} = 1177.2\\text{ N}$.",
      "The useful mechanical power output delivered at speed $v = 2.5\\text{ m s}^{-1}$ is $P = F v = 1177.2\\text{ N} \\times 2.5\\text{ m s}^{-1} = 2943\\text{ W} \\approx 2900\\text{ W}$ (to 2 significant figures).",
      "This matches option D.",
      "Option A ($P = 48\\text{ W}$) results from dividing mass by speed. Option B ($P = 300\\text{ W}$) multiplies mass by speed but neglects $g$. Option C ($P = 470\\text{ W}$) represents an incorrect power estimation."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q19",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "equation_derivation",
      "definition"
    ],
    "topic_id": "9702_t06",
    "module_id": "9702_t06_m01",
    "skill_id": "9702_skill_define_young_modulus",
    "accepted_answer": "B",
    "hints": [
      "Recall the definition of Young modulus: $E = \\frac{\\text{tensile stress}}{\\text{tensile strain}} = \\frac{\\sigma}{\\varepsilon}$.",
      "Express tensile stress as $\\sigma = \\frac{F}{A} = \\frac{m g}{A}$ and tensile strain as $\\varepsilon = \\frac{e}{l}$, then simplify the compound fraction."
    ],
    "walkthrough": [
      "Tensile stress is defined as force per unit cross-sectional area: $\\sigma = \\frac{F}{A} = \\frac{m g}{A}$, where the applied force is the weight $m g$ of the hung mass.",
      "Tensile strain is defined as extension per unit original length: $\\varepsilon = \\frac{e}{l}$.",
      "The Young modulus $E$ is the ratio of tensile stress to tensile strain: $E = \\frac{\\sigma}{\\varepsilon} = \\frac{\\frac{m g}{A}}{\\frac{e}{l}} = \\frac{m g l}{A e}$.",
      "This expression matches option B.",
      "Option A ($E = \\frac{m l}{A e}$) incorrectly substitutes mass $m$ instead of force (weight $m g$). Options C and D invert the ratio of length and extension."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q20",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "multi_step_calculation",
      "direct_calculation"
    ],
    "topic_id": "9702_t06",
    "module_id": "9702_t06_m02",
    "skill_id": "9702_skill_apply_hookes_law",
    "accepted_answer": "D",
    "hints": [
      "When springs are connected in series (end-to-end), each spring experiences the full suspended load of $F = 80\\text{ N}$.",
      "Calculate the extension of each spring separately using Hookes law $x = \\frac{F}{k}$, then sum their extensions to find total extension: $x_{\\text{total}} = x_1 + x_2$."
    ],
    "walkthrough": [
      "The two springs are connected in series, so the full tension force of $F = 80\\text{ N}$ acts throughout both springs.",
      "Using Hookes law $F = k x$, the extension of the first spring is $x_1 = \\frac{F}{k_1} = \\frac{80\\text{ N}}{6.0\\text{ N cm}^{-1}} = 13.33\\text{ cm}$.",
      "The extension of the second spring is $x_2 = \\frac{F}{k_2} = \\frac{80\\text{ N}}{4.0\\text{ N cm}^{-1}} = 20.0\\text{ cm}$.",
      "The total composite extension is the sum of the individual extensions: $x_{\\text{total}} = x_1 + x_2 = 13.33\\text{ cm} + 20.0\\text{ cm} = 33.33\\text{ cm} \\approx 33\\text{ cm}$ (option D).",
      "Option A ($x = 8.0\\text{ cm}$) incorrectly treats the springs as parallel with $k_{\\text{eff}} = 10.0\\text{ N cm}^{-1}$. Option B ($x = 16\\text{ cm}$) and Option C ($x = 17\\text{ cm}$) result from averaging or taking only one spring extension."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q21",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "direct_calculation"
    ],
    "topic_id": "9702_t06",
    "module_id": "9702_t06_m02",
    "skill_id": "9702_skill_estimate_work_from_force_extension_graph",
    "accepted_answer": "C",
    "hints": [
      "Recall that strain energy stored during loading equals the area under the force-extension loading curve up to the specified load of $F = 80\\text{ N}$.",
      "Count the number of grid squares under the curve up to $F = 80\\text{ N}$ (where extension is approx $x = 16.5\\text{ mm}$) and multiply by the energy represented per square ($\\Delta E = 20\\text{ N} \\times 2\\text{ mm} = 0.04\\text{ J}$)."
    ],
    "walkthrough": [
      "Strain energy stored in the rubber is equal to the area under the loading curve on the force-extension graph up to $F = 80\\text{ N}$.",
      "From the graph, at $F = 80\\text{ N}$, the extension is approximately $x = 16.5\\text{ mm} = 16.5 \\times 10^{-3}\\text{ m}$.",
      "Each major grid square has dimensions $\\Delta F = 20\\text{ N}$ and $\\Delta x = 2\\text{ mm} = 2 \\times 10^{-3}\\text{ m}$, representing an energy of $\\Delta E = 20\\text{ N} \\times 2 \\times 10^{-3}\\text{ m} = 0.04\\text{ J}$.",
      "Counting the grid squares under the loading curve up to $F = 80\\text{ N}$ gives approximately $N = 22$ complete and partial squares.",
      "Calculating total strain energy: $E_{\\text{strain}} \\approx 22 \\times 0.04\\text{ J} = 0.88\\text{ J}$ (option C).",
      "Option A ($E = 0.40\\text{ J}$) severely underestimates the area. Option B ($E = 0.64\\text{ J}$) approximates a simple triangle $\\frac{1}{2} F x = \\frac{1}{2}(80)(16 \\times 10^{-3}) = 0.64\\text{ J}$, but misses the significant area due to upward curvature. Option D ($E = 1.3\\text{ J}$) represents the full bounding rectangle."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q22",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "definition",
      "property_identification"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m01",
    "skill_id": "9702_skill_define_wavelength",
    "accepted_answer": "D",
    "hints": [
      "Recall the definition of wavelength for a longitudinal wave: the distance between two consecutive points oscillating in phase.",
      "Identify compressions (dense molecule clusters) and rarefactions (sparse molecule regions): P and R are successive compressions, while Q and S are successive rarefactions."
    ],
    "walkthrough": [
      "In a longitudinal sound wave, wavelength $\\lambda$ is the distance between any two successive points that are in the same phase of oscillation.",
      "In the molecule distribution diagram, P and R are centers of successive compressions, and Q and S are centers of successive rarefactions.",
      "The distance between two consecutive rarefactions (from Q to S) equals exactly one complete wavelength $\\lambda$, which corresponds to option D.",
      "Distance PQ (option A) and distance QR (option C) represent the distance between a compression and an adjacent rarefaction, which is half a wavelength ($\\frac{1}{2}\\lambda$). Distance PS (option B) corresponds to $1.5\\lambda$."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q23",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "definition",
      "property_identification"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m01",
    "skill_id": "9702_skill_define_amplitude",
    "accepted_answer": "C",
    "hints": [
      "Recall the definition of wave amplitude for vibrating particles in any medium.",
      "Amplitude is the maximum displacement of a particle from its undisturbed equilibrium (rest) position."
    ],
    "walkthrough": [
      "Amplitude is defined as the maximum displacement of an oscillating particle from its equilibrium (rest) position.",
      "The top row shows the particles in their undisturbed equilibrium positions at rest. The bottom row shows their displaced positions as the longitudinal wave propagates.",
      "To determine the amplitude of the oscillations, one measures the maximum distance any particle is displaced from its corresponding rest position in the top row (option C).",
      "Option A is incorrect because amplitude is the full maximum displacement from equilibrium, not half. Options B and D confuse particle separation (which relates to compression/rarefaction density) with individual particle displacement from equilibrium."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q24",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "property_identification",
      "direct_calculation"
    ],
    "topic_id": "9702_t08",
    "module_id": "9702_t08_m01",
    "skill_id": "9702_skill_explain_stationary_waves",
    "accepted_answer": "D",
    "hints": [
      "For a tube closed at one end and open at the other, resonance occurs at odd harmonics: $f_n = (2n - 1) f_1$ for $n = 1, 2, 3, 4, \\dots$.",
      "Determine the harmonic number corresponding to the fourth loudness maximum ($n = 4$)."
    ],
    "walkthrough": [
      "In a tube closed at one end and open at the other, stationary sound waves must form a displacement node at the closed end and a displacement antinode at the open end.",
      "The resonant wavelengths satisfy $L = \\frac{\\lambda_1}{4}, \\frac{3\\lambda_2}{4}, \\frac{5\\lambda_3}{4}, \\frac{7\\lambda_4}{4}, \\dots$, giving resonant frequencies in the ratio of odd integers: $f_1, 3f_1, 5f_1, 7f_1, \\dots$.",
      "First maximum (1st harmonic): $f = f_1$.",
      "Second maximum (3rd harmonic): $f = 3f_1$.",
      "Third maximum (5th harmonic): $f = 5f_1$.",
      "Fourth maximum (7th harmonic): $f = 7f_1$ (option D).",
      "Option B ($f = 2f_1$) and Option C ($f = 4f_1$) represent even harmonics, which cannot form stationary waves in a pipe closed at one end."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q25",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m03",
    "skill_id": "9702_skill_define_doppler_effect",
    "accepted_answer": "D",
    "hints": [
      "Use the Doppler effect formula for a moving sound source: $f_o = f_s \\left( \\frac{v}{v \\pm v_s} \\right)$.",
      "The maximum frequency heard by the observer occurs when the buzzer moves directly towards the observer at maximum approach speed ($v_s = 25.0\\text{ m s}^{-1}$)."
    ],
    "walkthrough": [
      "The observed frequency $f_o$ for a source moving towards a stationary observer is given by the Doppler equation: $f_o = f_s \\left( \\frac{v}{v - v_s} \\right)$.",
      "Given data: source frequency $f_s = 846\\text{ Hz}$, speed of sound $v = 340\\text{ m s}^{-1}$, and source speed $v_s = 25.0\\text{ m s}^{-1}$.",
      "Maximum frequency occurs when the buzzer velocity vector points directly toward the observer: $f_{\\text{max}} = 846 \\times \\left( \\frac{340}{340 - 25.0} \\right) = 846 \\times \\left( \\frac{340}{315} \\right)$.",
      "Calculate: $f_{\\text{max}} = 846 \\times 1.079365 \\approx 913.14\\text{ Hz} \\approx 913\\text{ Hz}$ (option D).",
      "Option B ($f = 788\\text{ Hz}$) is the minimum frequency heard when the buzzer moves directly away from the observer: $f_{\\text{min}} = 846 \\times \\frac{340}{365} = 788\\text{ Hz}$. Options A and C result from arithmetic errors."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q26",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "property_identification",
      "physical_quantity_estimation"
    ],
    "topic_id": "9702_t07",
    "module_id": "9702_t07_m04",
    "skill_id": "9702_skill_identify_electromagnetic_spectrum_region",
    "accepted_answer": "C",
    "hints": [
      "Note the arrow indicating wavelength increasing directed towards the left.",
      "Identify the standard regions from shortest to longest wavelength: gamma-rays $\\rightarrow$ X-rays (wavelength $\\lambda \\approx 10^{-10}\\text{ m}$) $\\rightarrow$ ultraviolet $\\rightarrow$ visible $\\rightarrow$ infrared $\\rightarrow$ microwaves (region Q) $\\rightarrow$ radio waves."
    ],
    "walkthrough": [
      "The electromagnetic spectrum is arranged with wavelength increasing from right to left across 7 principal bands.",
      "From right (shortest wavelength) to left (longest wavelength):",
      "Band 7 (far right): Gamma rays (wavelength $\\lambda < 10^{-11}\\text{ m}$).",
      "Band 6 (labelled $\\lambda = 10^{-10}\\text{ m}$): X-rays (wavelength range $\\lambda = 10^{-11}\\text{ m}$ to $\\lambda = 10^{-8}\\text{ m}$).",
      "Band 5: Ultraviolet (wavelength range $\\lambda = 10^{-8}\\text{ m}$ to $\\lambda = 4 \\times 10^{-7}\\text{ m}$).",
      "Band 4: Visible light (wavelength range $\\lambda = 4 \\times 10^{-7}\\text{ m}$ to $\\lambda = 7 \\times 10^{-7}\\text{ m}$).",
      "Band 3: Infrared (wavelength range $\\lambda = 7 \\times 10^{-7}\\text{ m}$ to $\\lambda = 10^{-3}\\text{ m}$).",
      "Band 2 (Region Q): Microwaves (wavelength range $\\lambda = 10^{-3}\\text{ m}$ to $\\lambda = 10^{-1}\\text{ m}$).",
      "Band 1 (far left): Radio waves (wavelength $\\lambda > 10^{-1}\\text{ m}$).",
      "A typical order of magnitude of wavelength in region Q (microwaves) is $\\lambda \\sim 10^{-2}\\text{ m}$ (option C).",
      "Option A ($\\lambda \\sim 10^{-7}\\text{ m}$) corresponds to visible light/UV. Option B ($\\lambda \\sim 10^{-5}\\text{ m}$) corresponds to infrared. Option D ($\\lambda \\sim 1\\text{ m} = 10^0\\text{ m}$) corresponds to radio waves."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q27",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "property_identification",
      "comparison"
    ],
    "topic_id": "9702_t08",
    "module_id": "9702_t08_m01",
    "skill_id": "9702_skill_determine_stationary_wave_phase_relationship",
    "accepted_answer": "C",
    "hints": [
      "Identify the nodes: P, R, and Q are nodes, dividing the string into two adjacent oscillating loops PR and RQ.",
      "Determine the amplitude at distance $x$ from node R in each loop, and recall the phase relationship between particles on opposite sides of a node."
    ],
    "walkthrough": [
      "The points P, R, and Q are nodes, which means the string oscillates in two loops of equal length (PR and RQ).",
      "Because of spatial symmetry about the central node R, points S and T located at the identical distance $x$ from R oscillate with the same amplitude.",
      "All particles within a single loop oscillate in phase with one another, but particles in adjacent loops separated by a single node oscillate in antiphase (a phase difference of $\\Delta\\phi = 180^\\circ$ or $\\pi\\text{ rad}$).",
      "Therefore, points S and T have the same amplitude and a phase difference of $\\Delta\\phi = 180^\\circ$ (option C).",
      "Option A is incorrect because points in adjacent loops are out of phase. Options B and D are incorrect because equal distance from a node guarantees identical amplitude."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q28",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "interference_analysis",
      "graph_interpretation"
    ],
    "topic_id": "9702_t08",
    "module_id": "9702_t08_m03",
    "skill_id": "9702_skill_interference",
    "accepted_answer": "A",
    "hints": [
      "The two loudspeakers act as coherent sources producing an interference pattern with alternating maxima and minima of sound intensity along line PQ.",
      "Consider the central position where path difference is zero (central maximum), and note how the total sound intensity envelope decreases towards P and Q as distance from the speakers increases."
    ],
    "walkthrough": [
      "The two identical speakers connected to the same a.c. supply emit coherent sound waves that superpose along the line PQ.",
      "At the midpoint of PQ (equidistant from both speakers), the path difference is zero, resulting in constructive interference and a central maximum.",
      "As the microphone moves toward P or Q, the overall distance from the speakers increases, which decreases the underlying sound intensity envelope.",
      "Furthermore, at points away from the center, the distances to the two speakers differ slightly, so the two waves have slightly unequal amplitudes, meaning destructive interference minima do not drop completely to zero.",
      "Graph A correctly shows the central maximum, the alternating fringes, the non-zero minima, and the decreasing envelope toward P and Q.",
      "Graphs B and D show intensity dropping to zero at minima with unrealistic envelopes. Graph C lacks the characteristic central peak."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q29",
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
      "Apply the diffraction grating equation $d \\sin\\theta = n \\lambda$ for orders $n = 1$ and $n = 2$.",
      "Use $d = 2.00\\text{ }\\mu\\text{m} = 2.00 \\times 10^{-6}\\text{ m}$ and $\\lambda = 600\\text{ nm} = 6.00 \\times 10^{-7}\\text{ m}$ to calculate $\\theta_1$ and $\\theta_2$, then find the difference $\\theta_2 - \\theta_1$."
    ],
    "walkthrough": [
      "The diffraction grating equation is $d \\sin\\theta = n \\lambda$, where $d = 2.00 \\times 10^{-6}\\text{ m}$ and $\\lambda = 600 \\times 10^{-9}\\text{ m} = 6.00 \\times 10^{-7}\\text{ m}$.",
      "For the first-order maximum ($n = 1$): $\\sin\\theta_1 = \\frac{1 \\times 6.00 \\times 10^{-7}\\text{ m}}{2.00 \\times 10^{-6}\\text{ m}} = 0.300 \\implies \\theta_1 = \\arcsin(0.300) \\approx 17.46^\\circ$.",
      "For the second-order maximum ($n = 2$): $\\sin\\theta_2 = \\frac{2 \\times 6.00 \\times 10^{-7}\\text{ m}}{2.00 \\times 10^{-6}\\text{ m}} = 0.600 \\implies \\theta_2 = \\arcsin(0.600) \\approx 36.87^\\circ$.",
      "The angular separation between the first and second order maxima is $\\Delta\\theta = \\theta_2 - \\theta_1 = 36.87^\\circ - 17.46^\\circ = 19.41^\\circ \\approx 19.4^\\circ$ (option B).",
      "Option A ($\\theta_1 = 17.5^\\circ$) is the first-order angle alone. Option C ($\\theta_2 = 36.9^\\circ$) is the second-order angle. Option D ($\\theta = 54.3^\\circ$) is the sum $\\theta_1 + \\theta_2$."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q30",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "property_identification"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m02",
    "skill_id": "9702_skill_define_electric_field_strength",
    "accepted_answer": "A",
    "hints": [
      "Recall that between uniform parallel plates, electric field strength is $E = \\frac{\\Delta V}{d}$.",
      "Electric field lines point from regions of higher potential ($V = +50\\text{ V}$) to regions of lower potential ($V = 0\\text{ V}$)."
    ],
    "walkthrough": [
      "Between two parallel conducting plates separated by distance $d = 5.0\\text{ mm} = 5.0 \\times 10^{-3}\\text{ m}$ with potential difference $\\Delta V = 50\\text{ V} - 0\\text{ V} = 50\\text{ V}$, the electric field is uniform.",
      "The magnitude of the electric field strength is $E = \\frac{\\Delta V}{d} = \\frac{50\\text{ V}}{5.0 \\times 10^{-3}\\text{ m}} = 1.0 \\times 10^4\\text{ V m}^{-1}$.",
      "Electric field lines are directed from higher potential (the upper plate at $V = +50\\text{ V}$) towards lower potential (the lower earthed plate at $V = 0\\text{ V}$), which is downwards.",
      "Therefore, the electric field strength at the midpoint (and everywhere between the plates) is $E = 1.0 \\times 10^4\\text{ V m}^{-1}$ downwards (option A).",
      "Option B gives the opposite field direction. Options C and D ($E = 2.0 \\times 10^4\\text{ V m}^{-1}$) mistakenly halve the separation distance when evaluating $E$ at the midpoint."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q31",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "property_identification",
      "comparison"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m02",
    "skill_id": "9702_skill_compare_electric_field_strength_from_line_spacing",
    "accepted_answer": "B",
    "hints": [
      "Electric field lines point radially outwards from a positive central charge; negatively charged electrons experience electrostatic forces in the direction opposite to the field lines.",
      "Electric field strength increases closer to the source charge ($E \\propto \\frac{1}{r^2}$), so compare the distances of electrons X and Y from the center."
    ],
    "walkthrough": [
      "The electric field lines point radially outwards from the center, indicating that the central point charge is positive.",
      "Electrons carry negative charge ($-e$), so the electrostatic force acting on them is directed opposite to the field lines, which is radially inwards toward the positive charge.",
      "The magnitude of the electric field strength due to a point charge decreases with distance: $E = \\frac{Q}{4\\pi\\varepsilon_0 r^2}$.",
      "From the diagram, electron X is located closer to the central charge than electron Y ($r_X < r_Y$).",
      "Consequently, the electric field strength and resulting electrostatic force $F = e E$ on X are greater than on Y.",
      "This confirms row B: direction of force is radially inwards, and magnitude of force on X is greater than force on Y."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q32",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "definition",
      "property_identification"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m01",
    "skill_id": "9702_skill_apply_drift_current",
    "accepted_answer": "D",
    "hints": [
      "Review the physical meaning of each symbol in the microscopic current formula $I = A n v q$.",
      "Recall that individual free electrons in a metal have high random thermal velocities in all directions, whereas $v$ represents their average net drift speed along the conductor."
    ],
    "walkthrough": [
      "In the transport equation $I = A n v q$:",
      "$n$ is the number density of charge carriers (number of carriers per unit volume), so statement A is correct.",
      "$n A$ represents $(\\text{carriers}/\\text{volume}) \\times \\text{area} = \\text{carriers}/\\text{length}$, which is the number of charge carriers per unit length, so statement B is correct.",
      "$q$ is the charge on each individual charge carrier (such as the elementary charge $e$), so statement C is correct.",
      "$v$ represents the average drift velocity (or mean drift speed) of the charge carriers along the wire caused by the applied potential gradient, not the actual instantaneous velocity of each individual charge carrier (which undergo rapid random thermal motion).",
      "Therefore, statement D is not correct (option D)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q33",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "circuit_analysis"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m02",
    "skill_id": "9702_skill_calculate_electrical_power",
    "accepted_answer": "C",
    "hints": [
      "For resistors connected in parallel across the same supply, the potential difference $V$ across each resistor is identical.",
      "Use the power formula $P = \\frac{V^2}{R}$ to express the ratio $P_2 : P_3 : P_4 = \\frac{1}{2} : \\frac{1}{3} : \\frac{1}{4}$, then multiply by the lowest common multiple ($N = 12$)."
    ],
    "walkthrough": [
      "Because the three resistors are connected in parallel, each resistor experiences the same potential difference $V$.",
      "The electrical power dissipated in a resistor of resistance $R$ is given by $P = \\frac{V^2}{R}$.",
      "The power dissipated in each resistor is therefore inversely proportional to its resistance: $P_2 : P_3 : P_4 = \\frac{V^2}{2} : \\frac{V^2}{3} : \\frac{V^2}{4} = \\frac{1}{2} : \\frac{1}{3} : \\frac{1}{4}$.",
      "Multiply each term in the ratio by the common denominator $N = 12$: $(12 \\times \\frac{1}{2}) : (12 \\times \\frac{1}{3}) : (12 \\times \\frac{1}{4}) = 6 : 4 : 3$.",
      "This matches option C.",
      "Option A ($2 : 3 : 4$) incorrectly assumes constant current using $P = I^2 R$. Option B ($4 : 3 : 2$) simply lists the resistance values in reverse order."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q34",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "graph_interpretation",
      "property_identification"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m03",
    "skill_id": "9702_skill_construct_filament_lamp_iv_characteristic",
    "accepted_answer": "A",
    "hints": [
      "Note which quantities are plotted on each axis: potential difference $V$ is on the vertical axis and current $I$ is on the horizontal axis.",
      "As current increases, the filament wire heats up, causing its resistance $R = \\frac{V}{I}$ (the secant gradient on a $V$-$I$ graph) to increase."
    ],
    "walkthrough": [
      "As electric current $I$ through a filament lamp increases, resistive heating increases the filament temperature, causing lattice vibrations and increasing resistance $R$.",
      "Resistance is defined by $R = \\frac{V}{I}$. On a graph of $V$ against $I$ (where $V$ is on the vertical axis and $I$ is on the horizontal axis), resistance corresponds to the ratio $\\frac{V}{I}$.",
      "An increasing resistance as current rises means that $V$ must grow faster than $I$, resulting in an upward-curving graph with an increasing gradient starting at the origin $(0, 0)$.",
      "Graph A correctly displays this upward curve with increasing slope.",
      "Graph B represents an ohmic conductor with constant resistance. Graph C has a non-zero intercept. Graph D curves downwards, which would represent an $I$-$V$ graph with $I$ on the vertical axis (or a thermistor)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q35",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "direct_calculation",
      "multi_step_calculation"
    ],
    "topic_id": "9702_t09",
    "module_id": "9702_t09_m03",
    "skill_id": "9702_skill_apply_resistivity",
    "accepted_answer": "D",
    "hints": [
      "Calculate the resistance of the wire from Ohms law: $R = \\frac{V}{I} = \\frac{6.0\\text{ V}}{3.0\\text{ A}} = 2.0\\ \\Omega$.",
      "Use the resistivity formula $R = \\frac{\\rho L}{A}$ and rearrange to solve for length $L = \\frac{R A}{\\rho}$."
    ],
    "walkthrough": [
      "First find the electrical resistance of the wire using Ohms law: $R = \\frac{V}{I} = \\frac{6.0\\text{ V}}{3.0\\text{ A}} = 2.0\\ \\Omega$.",
      "The resistance of a uniform wire is given by $R = \\frac{\\rho L}{A}$, where $\\rho = 50 \\times 10^{-8}\\ \\Omega\\text{ m}$ and $A = 5.0 \\times 10^{-6}\\text{ m}^2$.",
      "Rearrange the formula to solve for the wire length $L$: $L = \\frac{R A}{\\rho}$.",
      "Substitute the values: $L = \\frac{2.0\\ \\Omega \\times 5.0 \\times 10^{-6}\\text{ m}^2}{50 \\times 10^{-8}\\ \\Omega\\text{ m}} = \\frac{10.0 \\times 10^{-6}}{5.0 \\times 10^{-7}} = 20\\text{ m}$ (option D).",
      "Option A ($L = 0.050\\text{ m}$), Option B ($L = 0.20\\text{ m}$), and Option C ($L = 5.0\\text{ m}$) arise from powers-of-ten errors when handling the micro- and nano-scale coefficients."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q36",
    "component": "P1",
    "difficulty": 2,
    "question_patterns": [
      "circuit_analysis",
      "graph_interpretation"
    ],
    "topic_id": "9702_t10",
    "module_id": "9702_t10_m01",
    "skill_id": "9702_skill_calculate_series_circuit_current_with_internal_resistance",
    "accepted_answer": "B",
    "hints": [
      "Express the circuit current in terms of e.m.f. $E$, fixed external resistance $R$, and variable internal resistance $r$: $I = \\frac{E}{R + r}$.",
      "Determine the value of current at $r = 0$ ($I = \\frac{E}{R}$, a non-zero finite intercept) and describe how $I$ decreases as $r$ increases."
    ],
    "walkthrough": [
      "Applying Kirchhoffs second law to the series circuit gives $E = I(R + r)$, which rearranges to $I = \\frac{E}{R + r}$.",
      "When internal resistance $r = 0$, the current has a finite non-zero value $I_0 = \\frac{E}{R}$, meaning the graph must have a finite positive vertical intercept on the current axis.",
      "As $r$ increases, the denominator $(R + r)$ increases, so the current $I$ decreases asymptotically towards zero as $r \\to \\infty$.",
      "The magnitude of the slope $|\\frac{dI}{dr}| = \\frac{E}{(R + r)^2}$ decreases continuously with increasing $r$, resulting in a curve that is concave upwards, flattening out towards the horizontal axis.",
      "Graph B correctly shows the non-zero vertical intercept and the asymptotic decay toward zero.",
      "Graph A incorrectly shows current tending to infinity at $r = 0$ (which would only occur if $R = 0$). Graph C depicts an incorrect straight line. Graph D shows constant current."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q37",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "comparison",
      "circuit_analysis"
    ],
    "topic_id": "9702_t10",
    "module_id": "9702_t10_m01",
    "skill_id": "9702_skill_calculate_parallel_resistance",
    "accepted_answer": "A",
    "hints": [
      "Let each identical resistor have resistance $R_0$.",
      "Calculate the equivalent resistance for each network: P (two in series), Q (one alone), R (two in parallel), and S (one in series with two in parallel)."
    ],
    "walkthrough": [
      "Let the resistance of each single resistor be $R_0$.",
      "Combination P consists of two resistors in series: $R_P = R_0 + R_0 = 2.0 R_0$.",
      "Combination Q is a single resistor: $R_Q = R_0 = 1.0 R_0$.",
      "Combination R consists of two resistors in parallel: $R_R = \\frac{R_0 \\times R_0}{R_0 + R_0} = 0.5 R_0$.",
      "Combination S consists of one resistor in series with a parallel pair: $R_S = R_0 + 0.5 R_0 = 1.5 R_0$.",
      "Arranging the combined resistances in decreasing order (largest to smallest): $R_P (2.0 R_0) > R_S (1.5 R_0) > R_Q (1.0 R_0) > R_R (0.5 R_0)$.",
      "This gives the sequence $\\text{P} \\to \\text{S} \\to \\text{Q} \\to \\text{R}$, which matches option A."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q38",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "circuit_analysis",
      "direct_calculation"
    ],
    "topic_id": "9702_t10",
    "module_id": "9702_t10_m03",
    "skill_id": "9702_skill_analyse_ldr_potential_divider_response",
    "accepted_answer": "D",
    "hints": [
      "Because component Y draws negligible current, the two resistors of $R_1 = 10\\text{ k}\\Omega$ and $R_2 = 50\\text{ k}\\Omega$ form an unloaded potential divider across the $V = 6.0\\text{ V}$ supply.",
      "Calculate the potential at junction X relative to $V = 0\\text{ V}$ using the potential divider formula $V_X = V_{\\text{supply}} \\times \\frac{R_2}{R_1 + R_2}$."
    ],
    "walkthrough": [
      "The potential divider consists of a top resistor $R_1 = 10\\text{ k}\\Omega$ connected to the $V = +6.0\\text{ V}$ rail and a bottom resistor $R_2 = 50\\text{ k}\\Omega$ connected to the $V = 0\\text{ V}$ rail.",
      "Since component Y draws negligible current, it does not alter the current in the divider chain.",
      "The electric potential at junction X is the potential difference across the bottom resistor: $V_X = V_{\\text{supply}} \\times \\frac{R_2}{R_1 + R_2}$.",
      "Substitute the values: $V_X = 6.0\\text{ V} \\times \\frac{50\\text{ k}\\Omega}{10\\text{ k}\\Omega + 50\\text{ k}\\Omega} = 6.0 \\times \\frac{50}{60} = 5.0\\text{ V}$.",
      "This corresponds to option D.",
      "Option A ($V_X = 1.0\\text{ V}$) is the potential drop across the top resistor with resistance $R_1 = 10\\text{ k}\\Omega$ ($6.0 - 5.0 = 1.0\\text{ V}$). Options B and C result from arithmetic errors."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q39",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "equation_completion",
      "direct_calculation"
    ],
    "topic_id": "9702_t11",
    "module_id": "9702_t11_m01",
    "skill_id": "9702_skill_complete_nuclear_equations",
    "accepted_answer": "D",
    "hints": [
      "Write the nuclear fission equation: ${}^1_0\\text{n} + {}^{235}_{\\ 92}\\text{U} \\to {}^{141}_{\\ 56}\\text{Ba} + {}^{92}_{36}\\text{Kr} + x {}^1_0\\text{n}$.",
      "Apply conservation of nucleon number (mass number) to find the integer $x$ representing the number of released neutrons: $1 + 235 = 141 + 92 + x(1)$."
    ],
    "walkthrough": [
      "The nuclear fission reaction can be written as: ${}^1_0\\text{n} + {}^{235}_{\\ 92}\\text{U} \\to {}^{141}_{\\ 56}\\text{Ba} + {}^{92}_{36}\\text{Kr} + x {}^1_0\\text{n}$, where $x$ is the number of emitted neutrons.",
      "In any nuclear reaction, total nucleon number (mass number $A$) is conserved.",
      "Left-hand side total nucleon number: $A_{\\text{left}} = 1 + 235 = 236$.",
      "Right-hand side total nucleon number: $A_{\\text{right}} = 141 + 92 + x(1) = 233 + x$.",
      "Equating both sides: $A = 236 = 233 + x \\implies x = 236 - 233 = 3$.",
      "We also check conservation of proton number $Z$: $0 + 92 = 56 + 36 + 3(0) = 92$, which is conserved.",
      "Therefore, $N = 3$ neutrons are emitted during the fission event (option D)."
    ]
  },
  {
    "schema_version": "9702_p1_enrichment_v1",
    "question_id": "9702_m19_12_q40",
    "component": "P1",
    "difficulty": 1,
    "question_patterns": [
      "classification",
      "property_identification"
    ],
    "topic_id": "9702_t11",
    "module_id": "9702_t11_m02",
    "skill_id": "9702_skill_identify_beta_decay_products",
    "accepted_answer": "D",
    "hints": [
      "In $\\beta^+$ decay, a proton inside the nucleus transforms into a neutron while emitting a positron (an antielectron).",
      "To conserve lepton number ($L = 0 \\to 0 + (-1) + (+1) = 0$), a positron (lepton number $-1$) must be accompanied by an electron neutrino (lepton number $+1$)."
    ],
    "walkthrough": [
      "In positive beta decay ($\\beta^+$ decay), a proton in an unstable nucleus transforms into a neutron via the weak interaction: $\\text{p} \\to \\text{n} + \\text{e}^+ + \\nu_e$.",
      "The emitted particles are a positron (the antimatter counterpart of an electron, with charge $+e$ and lepton number $L = -1$) and an electron neutrino (a neutral lepton with lepton number $L = +1$).",
      "Charge is conserved ($+1 = 0 + 1 + 0$) and lepton number is conserved ($0 = 0 - 1 + 1$).",
      "The corresponding word equation is: $\\text{proton} \\to \\text{neutron} + \\text{positron} + \\text{electron neutrino}$ (option D).",
      "Options A and B represent processes involving electrons ($\\beta^-$ decay involves $\\text{neutron} \\to \\text{proton} + \\text{electron} + \\text{electron antineutrino}$). Option C incorrectly pairs a positron with an electron antineutrino, violating lepton number conservation."
    ]
  }
]

def main():
    for item in data:
        qid = item["question_id"]
        out_file = OUT_DIR / f"{qid}.enrichment.json"
        out_file.write_text(json.dumps(item, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Generated {len(data)} enrichment files in {OUT_DIR}")

if __name__ == "__main__":
    main()
