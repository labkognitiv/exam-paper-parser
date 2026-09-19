# Topic 3 Markdown audit

**PASS**

**HTML gate: OPEN.** All 7 active planned lessons and build evidence records exist, cover 100% of syllabus learning outcomes (9702_t03_m01_o01 through o06, 9702_t03_m02_o01 through o03, and 9702_t03_m03_o01 through o04), and have no unresolved topic-level defects.

## Topic-wide findings

- Coverage is complete against `syllabus.json` across all 3 course modules and 7 active lessons:
  - `9702_t03_cm01` (Momentum and Newton's laws of motion):
    - `9702_t03_cm01_l01` owns mass as the property resisting change in motion (inertia), the quantitative relation \(F = ma\), unit derivation (\(1\,\mathrm{N} = 1\,\mathrm{kg\,m\,s^{-2}}\)), understanding that acceleration and resultant force are always in the exact same direction, and multi-body contacting/connected systems (`9702_t03_m01_o01`, `9702_t03_m01_o02`).
    - `9702_t03_cm01_l02` owns defining and using linear momentum as the product of mass and velocity (\(p = mv\)), defining and using force as the rate of change of momentum (\(F = \frac{\Delta p}{\Delta t}\)), impulse (\(\Delta p = F \Delta t\)), force-time graph area interpretation, and continuous mass-flow rate problems (`9702_t03_m01_o03`, `9702_t03_m01_o04`).
    - `9702_t03_cm01_l03` owns stating and applying each of Newton's three laws of motion, distinguishing Newton's third law interaction pairs from balanced forces on a single object, the concept of weight as the gravitational force exerted on a mass by a gravitational field (\(W = mg\)), normal contact force, and apparent weight in accelerating reference frames (`9702_t03_m01_o05`, `9702_t03_m01_o06`).
  - `9702_t03_cm02` (Non-uniform motion):
    - `9702_t03_cm02_l04` owns qualitative understanding of static and kinetic friction, viscous drag forces in liquids and gases, air resistance, dependence of drag on velocity, frontal surface area, and fluid density, absence of coefficient requirements per syllabus boundaries, and non-uniform acceleration under variable net force (`9702_t03_m02_o01`).
    - `9702_t03_cm02_l05` owns describing and explaining qualitatively the motion of objects in a uniform gravitational field with air resistance, downward acceleration decreasing from \(g\) towards zero as drag increases with speed, reaching terminal velocity when drag balances weight (\(D = mg\), \(a = 0\)), velocity-time curves (gradient decreasing from \(g\) to \(0\)), acceleration-time curves, and parachute deployment phases (`9702_t03_m02_o02`, `9702_t03_m02_o03`).
  - `9702_t03_cm03` (Linear momentum and its conservation):
    - `9702_t03_cm03_l06` owns stating the principle of conservation of momentum, enforcing the isolated system condition (no resultant external force), formal derivation of momentum conservation from Newton's second and third laws, solving one-dimensional collision problems, coalescing bodies, explosions and recoil dynamics, and solving two-dimensional interactions using perpendicular component resolution and closed vector triangles (`9702_t03_m03_o01`, `9702_t03_m03_o02`).
    - `9702_t03_cm03_l07` owns distinguishing elastic from inelastic collisions, conservation of kinetic energy in elastic collisions (\(\Sigma E_{K,\mathrm{initial}} = \Sigma E_{K,\mathrm{final}}\)), the relative speed condition (\(u_1 - u_2 = v_2 - v_1\)), velocity exchange between identical colliding masses, simultaneous linear equation solution strategies, and kinetic energy dissipation into thermal, sound, and deformation energies during inelastic impacts while total universe energy is conserved (`9702_t03_m03_o03`, `9702_t03_m03_o04`).
- Sequence is coherent, prerequisite-led, and forms a strictly acyclic DAG with monotonic sequence 1 to 7. Each lesson builds directly upon established concepts from Kinematics (Topic 2) and previous Dynamics lessons, with opening hooks and closing handoffs aligning consistently across transitions.
- Purposeful retrieval across lessons:
  - Controlled definition of mass as inertia established in `l01` is retrieved in `l02` to construct momentum (\(p = mv\)), in `l03` to formulate Newton's first and second laws and weight (\(W = mg\)), in `l04` and `l05` to analyze opposing forces during acceleration changes, and in `l06` and `l07` for system inertia in collisions.
  - Newton's second law (\(F = \frac{\Delta p}{\Delta t}\)) from `l02` and Newton's third law from `l03` are retrieved in `l06` to derive the conservation of linear momentum.
  - Directional sign conventions introduced in Topic 2 and consolidated in `l01` and `l02` are systematically maintained across 1D and 2D collision analysis in `l06` and `l07`.
- Controlled definitions match the official knowledge base byte-for-byte:
  - Mass (`9702_def_mass`): "the property of a body that resists changes in motion" (Lesson 1)
  - Force (`9702_def_force`): "the rate of change of momentum of a body" (Lessons 2 and 3)
  - Linear momentum (`9702_def_linear_momentum`): "the product of mass and velocity" (Lesson 2)
  - Newton's first law of motion (`9702_def_newtons_first_law`): "a body remains at rest or continues at constant velocity unless acted on by a resultant force" (Lesson 3)
  - Newton's third law of motion (`9702_def_newtons_third_law`): "when two bodies interact, the forces they exert on each other are equal in magnitude and opposite in direction" (Lesson 3)
  - Principle of conservation of momentum (`9702_def_conservation_of_momentum`): "the total momentum of an isolated system remains constant" (Lesson 6)
  - Elastic collision (`9702_def_elastic_collision`): "a collision in which the total kinetic energy of the system is the same before and after the collision" (Lesson 7)
- Controlled formulas preserve exact LaTeX, symbols, units, sign conventions, and validity conditions:
  - Newton's second law: \(F = \frac{\Delta p}{\Delta t} = ma\)
  - Weight: \(W = mg\)
  - Linear momentum: \(p = mv\)
  - Relative speed in elastic collision: \(u_1 - u_2 = v_2 - v_1\)
  - Kinetic energy: \(E_K = \frac{1}{2}mv^2\)
  - One-dimensional conservation of momentum: \(m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2\)
- Scientific accuracy is verified across all dynamic principles:
  - Clear, consistent distinction between scalar mass (inertia) and vector weight (gravitational force).
  - Acceleration direction is strictly governed by net resultant force, not velocity direction.
  - Impulse is rigorously related to change in momentum via the integral/geometric area of force-time graphs.
  - Newton's third law criteria are rigorously audited: forces must be of the exact same physical type, have equal magnitude, act in opposite directions, and act on two distinct interacting bodies.
  - Frictional forces oppose relative motion between surfaces; fluid drag increases monotonically with relative speed; terminal velocity occurs strictly when drag matches driving/gravitational force (\(a = 0\)).
  - Free fall with air resistance produces a decreasing acceleration gradient on velocity-time graphs asymptotically approaching zero at terminal velocity.
  - The isolated system condition (zero resultant external force) is consistently enforced before applying momentum conservation.
  - Inelastic collisions conserve linear momentum while kinetic energy transforms into internal thermal, acoustic, and microscopic deformation energy; total energy remains strictly conserved.
  - In 2D collisions, linear momentum is conserved independently along orthogonal axes.
  - Numerical calculations strictly adhere to 2-3 significant figures matching input data precision.
- Misconceptions repaired across the topic:
  - Confusing mass and weight.
  - Believing a forward force is required to sustain steady velocity (Aristotelian misconception).
  - Equating applied force directly to resultant force without subtracting resistance or friction.
  - Assuming acceleration must point in the direction of travel.
  - Confusing Newton's third law interaction pairs with balanced forces acting on a single body.
  - Assuming the normal contact force on a floor is always equal to \(mg\).
  - Believing friction always opposes movement rather than relative motion.
  - Believing drag remains constant as an object speeds up.
  - Believing terminal velocity means an object comes to a stop.
  - Assuming an object falling in air has zero acceleration prior to reaching terminal velocity.
  - Omitting the isolated system requirement when stating momentum conservation.
  - Neglecting directional signs for opposing velocities in collision calculations.
  - Confusing equal and opposite momentum with equal speeds during recoil or explosion.
  - Believing momentum is only conserved in elastic collisions.
  - Confusing conservation of kinetic energy with conservation of total energy.
  - Subtracting scalar speeds directly in head-on collisions rather than calculating relative closing speed.
  - Assuming the physics term elastic refers to flexible or rubbery materials.
- Evidence provenance is complete across all 7 active lessons:
  - 71 authentic past-paper question parts from Cambridge 9702 examination series (2016-2025) catalogued across Paper 1 and Paper 2.
  - Every inspected question records assessed demand, reasoning pathways, distractor analysis, and specific lesson sections informed.
- Dash policy: Strictly ZERO em dashes (\u2014) and strictly ZERO en dashes (\u2013) exist across all files in Topic 3.

## Lesson decisions

| Lesson | Decision | Audit result |
| :--- | :--- | :--- |
| `9702_t03_cm01_l01` | keep | Covers outcomes 9702_t03_m01_o01 and o02; mass as property resisting change in motion (inertia), \(F = ma\), unit derivation (\(1\,\mathrm{N} = 1\,\mathrm{kg\,m\,s^{-2}}\)), acceleration and resultant force directional identity, and multi-body contacting/connected systems. |
| `9702_t03_cm01_l02` | keep | Covers outcomes 9702_t03_m01_o03 and o04; linear momentum (\(p = mv\)), force as rate of change of momentum (\(F = \frac{\Delta p}{\Delta t}\)), impulse (\(\Delta p = F\Delta t\)), force-time graph area interpretation, and continuous mass-flow rate problems. |
| `9702_t03_cm01_l03` | keep | Covers outcomes 9702_t03_m01_o05 and o06; Newton's first, second, and third laws of motion, distinguishing third-law pairs from balanced forces, weight as gravitational force on mass (\(W = mg\)), normal contact force, and apparent weight in accelerating lifts. |
| `9702_t03_cm02_l04` | keep | Covers outcome 9702_t03_m02_o01; qualitative treatment of friction, viscous drag forces in liquids and gases, air resistance, speed/area/density dependence, qualitative model without coefficient requirements, and non-uniform acceleration. |
| `9702_t03_cm02_l05` | keep | Covers outcomes 9702_t03_m02_o02 and o03; motion in uniform gravitational field with air resistance, acceleration decrease from \(g\) to zero, terminal velocity condition (\(D = W\)), velocity-time and acceleration-time curves, and parachute opening dynamics. |
| `9702_t03_cm03_l06` | keep | Covers outcomes 9702_t03_m03_o01 and o02; principle of conservation of momentum, isolated system condition (no resultant external force), derivation from Newton's 2nd and 3rd laws, 1D collisions, coalescing bodies, recoil/explosions, and 2D momentum vector components/triangles. |
| `9702_t03_cm03_l07` | keep | Covers outcomes 9702_t03_m03_o03 and o04; elastic vs inelastic collisions, conservation of kinetic energy, relative speed condition (\(u_1 - u_2 = v_2 - v_1\)), velocity exchange for equal masses, simultaneous equations, and kinetic energy loss to heat, sound, and deformation. |

## Validator output

```
Loaded 25 topics, 300 total learning outcomes from syllabus.
[PASS] 9702_t03_dynamics: 100% verified
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
1. Syllabus outcome `9702_t03_m01_o01` phrases the concept as "mass is the property of an object that resists change in motion", whereas the controlled definition record in `definitions.json` (`9702_def_mass`) is "the property of a body that resists changes in motion". Lesson `l01` preserves the approved registry definition byte-for-byte in its formal definition block while addressing the syllabus phrasing naturally in surrounding text.
2. In `formulas.json`, Newton's second law is recorded as `F = \frac{\Delta p}{\Delta t} = ma` (`9702_formula_newtons_second_law`). Lessons `l01` and `l02` appropriately unpack this composite formula into its constituent learning outcomes: Lesson 1 focuses on \(F = ma\) for constant mass, while Lesson 2 formalizes \(F = \frac{\Delta p}{\Delta t}\) as the fundamental definition of force, both linking to the same controlled formula anchor.
3. One-dimensional conservation of momentum (\(m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2\)) is derived and applied in Lesson 6 as the quantitative realization of outcome `9702_t03_m03_o02`. Because no dedicated formula entry exists in `formulas.json` (momentum conservation is governed by `9702_def_conservation_of_momentum`), Lesson 6 treats it as an algebraic consequence of the controlled principle without mutating the formulas registry.
4. Qualitative outcomes in Course Module 2 (`cm02_l04` and `cm02_l05`) require no quantitative formulas for drag or friction per syllabus instruction ("no treatment of the coefficients of friction and viscosity is required, and a simple model of drag force increasing as speed increases is sufficient"). Lessons adhere strictly to this scope without inventing unapproved formulas.
5. All 7 active lessons in Topic 3 were newly authored without requiring redirects; `study/lesson-id-redirects.json` has 0 redirect entries for Topic 3.
