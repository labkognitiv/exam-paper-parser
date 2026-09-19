# Topic 2 Markdown audit

**PASS**

**HTML gate: OPEN.** All 9 active planned lessons and build evidence records exist, cover 100% of syllabus learning outcomes (9702_t02_m01_o01 through o09), and have no unresolved topic-level defects.

## Topic-wide findings

- Coverage is complete against `syllabus.json` across all 6 course modules:
  - `9702_t02_cm01` (Motion quantities and modelling):
    - `9702_t02_cm01_l01` owns scalar and vector distinctions, distance, displacement, speed, velocity, average speed, average velocity, and uniform motion displacement ($s = vt$) (`9702_t02_m01_o01`).
    - `9702_t02_cm01_l02` owns acceleration as rate of change of velocity ($a = \frac{\Delta v}{\Delta t}$), unit derivation ($\mathrm{m\ s^{-2}}$), acceleration direction, and distinguishing speeding up from slowing down via sign comparison (`9702_t02_m01_o01`).
  - `9702_t02_cm02` (Motion graphs):
    - `9702_t02_cm02_l03` owns reading displacement-time and velocity-time graphs, determining velocity from the gradient of a displacement-time graph, determining acceleration from the gradient of a velocity-time graph, and tangent construction for instantaneous values on curves (`9702_t02_m01_o02`, `9702_t02_m01_o04`, `9702_t02_m01_o05`) [consolidated with retired `l04`].
    - `9702_t02_cm02_l05` owns determining displacement from the signed area between a velocity-time graph and the time axis (rectangles, triangles, trapezia), and distinguishing net displacement from total distance travelled (`9702_t02_m01_o02`, `9702_t02_m01_o03`).
  - `9702_t02_cm03` (Uniform acceleration equations):
    - `9702_t02_cm03_l06` owns the constant-acceleration model conditions, formal derivations of the equations of motion ($v = u + at$, $s = \frac{u+v}{2}t$, $s = ut + \frac{1}{2}at^2$, $v^2 = u^2 + 2as$, $s = vt - \frac{1}{2}at^2$) from definitions of velocity and acceleration, equation selection strategies, multi-stage journeys, and reverse problem solving (`9702_t02_m01_o06`, `9702_t02_m01_o07`) [consolidated with retired `l07` and `l08`].
  - `9702_t02_cm04` (Vertical motion and free fall):
    - `9702_t02_cm04_l09` owns free fall under gravity without air resistance ($g = 9.81\ \mathrm{m\ s^{-2}}$), mass independence of gravitational acceleration, upward vertical projection, turning point dynamics ($v = 0$, $a = -g \neq 0$), symmetry of flight, laboratory determination of $g$ using falling objects (electromagnet and trapdoor / light gates), graphical determination from $s$ versus $t^2$ where $\text{gradient} = \frac{1}{2}g$, and error reduction strategies (`9702_t02_m01_o07`, `9702_t02_m01_o08`) [consolidated with retired `l10`].
  - `9702_t02_cm05` (Two-dimensional projectile motion):
    - `9702_t02_cm05_l11` owns independence of perpendicular horizontal and vertical components, horizontal uniform velocity ($v_x = u \cos\theta$), vertical uniform acceleration ($a_y = -g$, $v_y = u \sin\theta - gt$), flight time determination, horizontal range calculation, parabolic path derivation, and resultant impact velocity calculation (speed via Pythagoras and angle via trigonometry) (`9702_t02_m01_o09`) [consolidated with retired `l12`].
  - `9702_t02_cm06` (Synthesis, representation shift and mixed problem-solving):
    - `9702_t02_cm06_l13` owns meta-cognitive representation selection between verbal explanations, motion graphs, and kinematic equations, translating between representations, and selecting the most direct solution route (`9702_t02_m01_o01`, `9702_t02_m01_o02`, `9702_t02_m01_o03`, `9702_t02_m01_o04`, `9702_t02_m01_o05`, `9702_t02_m01_o07`).
    - `9702_t02_cm06_l14` owns isolating the kinematics leaf within complex multi-topic questions (dynamics, work-energy, electric fields), systematic 5-point motion records, boundary handoffs between physical domains, and comprehensive topical diagnostic correction (`9702_t02_m01_o01`, `9702_t02_m01_o02`, `9702_t02_m01_o03`, `9702_t02_m01_o04`, `9702_t02_m01_o05`, `9702_t02_m01_o06`, `9702_t02_m01_o07`, `9702_t02_m01_o08`, `9702_t02_m01_o09`) [consolidated with retired `l15`].
- Sequence is coherent, prerequisite-led, and forms a strictly acyclic DAG with monotonic sequence 1 to 9. Each lesson builds only on established prerequisites, and closing handoffs match subsequent lesson openings.
- Repeated content represents purposeful retrieval:
  - Controlled definitions of displacement and velocity established in `l01` are retrieved in `l02` to define acceleration, in `l03` to explain gradient physical meanings, in `l05` for graph areas, in `l06` to derive suvat equations, and in `l11` for 2D components.
  - Sign conventions introduced in `l01` and `l02` are systematically applied to vector motion graphs in `l03`/`l05`, vertical free fall in `l09`, and 2D vector resolutions in `l11`.
  - Equation derivation from `l06` is retrieved to justify component equations in `l11` and representation shifts in `l13`/`l14`.
- Controlled definitions match the official knowledge base byte-for-byte:
  - Displacement (`9702_def_displacement`): "distance in a specified direction from a point"
  - Velocity (`9702_def_velocity`): "rate of change of displacement"
  - Acceleration (`9702_def_acceleration`): "rate of change of velocity"
- Controlled formulas preserve exact LaTeX, symbols, units, sign conventions, and validity conditions:
  - Average speed: $\bar{v} = \frac{\text{total distance travelled}}{\text{total time taken}}$
  - Average velocity: $\vec{v}_{\mathrm{avg}} = \frac{\Delta\vec{s}}{\Delta t}$
  - Uniform motion displacement: $s = vt$
  - Acceleration: $a = \frac{\Delta v}{\Delta t}$
  - Constant-acceleration velocity: $v = u + at$
  - Constant-acceleration displacement: $s = ut + \frac{1}{2}at^2$
  - Constant-acceleration velocity and displacement: $v^2 = u^2 + 2as$
- Scientific accuracy is verified across all kinematic principles:
  - Vector versus scalar distinctions are maintained consistently throughout.
  - Tangent gradients on curves are clearly distinguished from chord gradients (instantaneous vs average rates).
  - Graph area signed geometry is strictly observed (positive area above time axis, negative area below time axis).
  - Constant-acceleration validity condition is explicitly enforced before using suvat equations.
  - At maximum height of vertical projection, vertical velocity is zero ($v = 0$) while downward acceleration remains $g = 9.81\ \mathrm{m\ s^{-2}}$.
  - Experimental determination of $g$ correctly derives $g = 2 \times \text{gradient}$ from $s = \frac{1}{2}gt^2$ when plotting $s$ against $t^2$.
  - In 2D projectile motion, perpendicular components are treated independently: horizontal acceleration is zero ($a_x = 0$), vertical acceleration is $-g$, and impact velocity includes both magnitude (Pythagoras) and angle to the horizontal (trigonometry).
  - Calculations adhere to 2-3 significant figures matching input data precision.
- Misconceptions repaired:
  - Conflating distance (scalar path length) with displacement (directed vector from reference point).
  - Averaging stage speeds directly without weighting by time intervals.
  - Assuming negative acceleration automatically denotes slowing down.
  - Assuming an object is stationary at a horizontal line on a velocity-time graph away from the time axis.
  - Believing acceleration is zero at the turning point of vertical upward motion.
  - Believing heavier objects fall faster in free fall (in vacuum).
  - Plotting $s$ against $t^2$ and taking gradient as $g$ instead of $g/2$.
  - Assuming horizontal velocity affects vertical time of flight in projectile motion.
  - Stating only speed when an examination question asks for impact velocity.
- Evidence provenance is complete across all 9 active lessons:
  - 66 authentic past-paper question parts from Cambridge 9702 examination series (2016-2025) catalogued across Paper 1 and Paper 2.
  - Every inspected question records evaluated demand, reasoning routes, misconceptions, and specific sections informed.
- Dash policy: Strictly ZERO em dashes (\u2014 / chr(8212)) and strictly ZERO en dashes (\u2013 / chr(8211)) exist across all files in Topic 2.

## Lesson decisions

| Lesson | Decision | Audit result |
| :--- | :--- | :--- |
| `9702_t02_cm01_l01` | keep | Covers outcome m01_o01; distance, displacement, speed, velocity, average speed, average velocity, scalar/vector distinctions, sign conventions, and uniform motion ($s=vt$). |
| `9702_t02_cm01_l02` | keep | Covers outcome m01_o01; acceleration definition, $a = \Delta v / \Delta t$, unit derivation ($\mathrm{m\ s^{-2}}$), acceleration direction, and speed change analysis. |
| `9702_t02_cm02_l03` | keep | Covers outcomes m01_o02, m01_o04, and m01_o05; displacement-time and velocity-time graphs, gradient physical meanings (velocity and acceleration), tangent construction, and reversal points (consolidated with retired l04). |
| `9702_t02_cm02_l05` | keep | Covers outcomes m01_o02 and m01_o03; displacement from signed area under velocity-time graphs (rectangles, triangles, trapezia), and net displacement vs total distance. |
| `9702_t02_cm03_l06` | keep | Covers outcomes m01_o06 and m01_o07; constant-acceleration model conditions, formal derivations of all suvat equations from definitions, equation selection, multi-stage and reverse problems (consolidated with retired l07 and l08). |
| `9702_t02_cm04_l09` | keep | Covers outcomes m01_o07 and m01_o08; free fall under gravity ($g = 9.81\ \mathrm{m\ s^{-2}}$), mass independence, upward motion and turning point, flight symmetry, experimental determination of $g$ (electromagnet and trapdoor / light gates), $s$ vs $t^2$ graph analysis ($g = 2m$), and uncertainty reduction (consolidated with retired l10). |
| `9702_t02_cm05_l11` | keep | Covers outcome m01_o09; independence of perpendicular components, horizontal uniform velocity ($v_x = u \cos\theta$), vertical uniform acceleration ($a_y = -g$), flight time, range, parabolic trajectories, and resultant impact velocity (magnitude and angle) (consolidated with retired l12). |
| `9702_t02_cm06_l13` | keep | Covers outcomes m01_o01, m01_o02, m01_o03, m01_o04, m01_o05, and m01_o07; meta-cognitive representation selection between words, graphs, and equations, and cross-representation translation. |
| `9702_t02_cm06_l14` | keep | Covers all outcomes m01_o01 through m01_o09; isolating kinematics leaf in multi-topic contexts (dynamics, energy, fields), 5-point motion records, domain handoffs, and topical mastery correction (consolidated with retired l15). |

## Validator output

```
Loaded 25 topics, 300 total learning outcomes from syllabus.
[PASS] 9702_t02_kinematics: 100% verified
==================================================
VALIDATION COMPLETE: 1 topics checked.
100% PASS: All 25 topics, course modules, lessons, DAGs, and zero em dashes verified.
```

```
Active lessons: 147
Redirects: 47
Errors: 0
PASS
```

## Unresolved mapping or knowledge-base issues

None requiring separate authorization. Specific metadata observations recorded for traceability:
1. Mapped formula ID `9702_formula_displacement_velocity_time_graph` has no standalone record in `formulas.json` (merged into `9702_formula_uniform_motion_displacement`). Active lessons (`l05`, `l13`, `l14`) faithfully teach the signed geometric area under a velocity-time graph as required by syllabus outcome `9702_t02_m01_o03` without altering the controlled formula registry.
2. The controlled definition of displacement in the knowledge base is "distance in a specified direction from a point", whereas some mark schemes expect "straight line distance from a point". Active lessons preserve the approved registry definition byte-for-byte in the formal definition callout while clarifying straight-line displacement in explanatory prose.
3. No separate formal definition for "acceleration of free fall" is registered in `definitions.json`; lessons appropriately treat it as a defined physical quantity and experimental constant ($g = 9.81\ \mathrm{m\ s^{-2}}$) rather than fabricating an unapproved formal definition.
4. Several multi-topic past paper questions in `evidence-index.json` carry primary topic classifications in dynamics, work-energy, or electric fields. These questions were inspected and used specifically for their kinematics leaves without mutating canonical taxonomy mappings.
