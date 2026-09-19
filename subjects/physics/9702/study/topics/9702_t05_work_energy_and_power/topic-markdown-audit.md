# Topic 5 Markdown audit

**PASS**

**HTML gate: OPEN.** All 6 active planned lessons and build evidence records exist, cover 100% of syllabus learning outcomes (9702_t05_m01_o01 through o07, and 9702_t05_m02_o01 through o04), and have no unresolved topic-level defects.

## Topic-wide findings

- Coverage is complete against `syllabus.json` across both course modules and all 6 active lessons:
  - `9702_t05_cm01` (Energy conservation):
    - `9702_t05_cm01_l01` owns the concept of work as mechanical energy transfer, the quantitative formulation \(W = Fs \cos\theta\), force-displacement graph areas, and constant-pressure gas expansion work (\(W = p\Delta V\)) (`9702_t05_m01_o01`, `9702_t05_m01_o02`).
    - `9702_t05_cm01_l02` owns the principle of conservation of energy in closed systems, energy dissipation into internal thermal energy and sound via friction and drag, efficiency definition (\(\eta = \frac{\text{useful output}}{\text{total input}} \times 100\%\)), quantitative Sankey diagrams, and multi-stage systems (`9702_t05_m01_o03`, `9702_t05_m01_o04`).
    - `9702_t05_cm01_l03` owns the definition of power as work done or energy transferred per unit time (\(P = \frac{W}{t} = \frac{\Delta E}{t}\)), the Watt as \(1\,\mathrm{J\,s^{-1}}\), base unit derivation (\(1\,\mathrm{W} = 1\,\mathrm{kg\,m^2\,s^{-3}}\)), and rating calculations (`9702_t05_m01_o05`).
    - `9702_t05_cm01_l04` owns solving problems using \(P = W/t\), deriving and applying \(P = Fv\) for moving objects, constant velocity under balanced driving and resistive forces, and terminal speed relationships (`9702_t05_m01_o06`, `9702_t05_m01_o07`).
  - `9702_t05_cm02` (Gravitational potential energy and kinetic energy):
    - `9702_t05_cm02_l05` owns deriving the formula \(\Delta E_p = mg\Delta h\) for gravitational potential energy in a uniform gravitational field using \(W = Fs\), path independence on an incline (\(\Delta h = L \sin\theta\)), and uniform field requirement (`9702_t05_m02_o01`, `9702_t05_m02_o02`).
    - `9702_t05_cm02_l06` owns deriving the formula \(E_k = \frac{1}{2}mv^2\) from Newton's second law, work done, and kinematic equations of motion (\(v^2 = u^2 + 2as\)), work-energy theorem (\(W = \Delta E_k\)), and speed calculations (`9702_t05_m02_o03`, `9702_t05_m02_o04`).
- Sequence is coherent, prerequisite-led, and forms a strictly acyclic DAG across Modules 1 and 2: `cm01_l01 -> cm01_l02 -> cm01_l03 -> cm01_l04 -> cm02_l05 -> cm02_l06`. Opening hooks and closing handoffs match consistently across transitions.
- Purposeful retrieval across lessons:
  - The definition and formula for work done \(W = Fs\) from l01 is retrieved in l03/l04 for mechanical power \(P = Fv\), in l05 for the gravitational potential energy derivation \(\Delta E_p = mg\Delta h\), and in l06 for the kinetic energy derivation \(E_k = \frac{1}{2}mv^2\).
  - Energy conservation and dissipation from l02 underpin the combined potential and kinetic energy systems explored in l05 and l06.
- Controlled definitions match the official knowledge base byte-for-byte:
  - Work done (`9702_def_work_done`): "product of force and displacement in the direction of the force" (Lesson 1)
  - Power (`9702_def_power`): "work done or energy transferred per unit time" (Lesson 3)
  - Gravitational potential energy (`9702_def_gravitational_potential_energy`): "energy stored by a mass because of its position or height in a gravitational field" (Lesson 5)
  - Kinetic energy (`9702_def_kinetic_energy`): "energy that an object has because of its motion" (Lesson 6)
- Controlled formulas preserve exact LaTeX, symbols, units, sign conventions, and validity conditions:
  - Work done: \(W = Fs \cos\theta\)
  - Gas expansion work: \(W = p\Delta V\)
  - Efficiency: \(\eta = \frac{\text{useful energy output}}{\text{total energy input}} = \frac{\text{useful power output}}{\text{total power input}}\)
  - Power: \(P = \frac{\Delta E}{t}\)
  - Mechanical power: \(P = Fv\)
  - Gravitational potential energy: \(\Delta E_p = mg\Delta h\)
  - Kinetic energy: \(E_k = \frac{1}{2}mv^2\)
- Scientific accuracy and calculations:
  - Clear distinction between force acting in displacement direction vs perpendicular forces (doing zero work).
  - Gas expansion work requires constant external pressure.
  - \(\Delta E_p = mg\Delta h\) applies strictly to uniform gravitational fields near Earth's surface where \(g\) is constant.
  - Work-energy theorem rigorously links net resultant work to change in kinetic energy.
  - Vector velocity components and scalar energy values are clearly distinguished.
- Misconceptions repaired across the topic:
  - Carrying a heavy load horizontally doing work against gravity.
  - Forgetting to multiply gas pressure by volume change in consistent SI units (\(\mathrm{m^3}\)).
  - Confusing energy conservation (total energy always constant) with efficiency (useful output / input).
  - Assuming efficiency can exceed 100% or equal 100% in real thermal/mechanical processes.
  - Equating power to force without considering speed.
  - Forgetting that doubling speed quadruples kinetic energy due to the \(v^2\) dependence.
- Evidence provenance is complete across all 6 active lessons:
  - Over 140 authentic past-paper question parts from Cambridge 9702 examination series (2016-2025) catalogued across Paper 1 and Paper 2.
- Dash policy: Strictly ZERO em dashes (\u2014) and strictly ZERO en dashes (\u2013) exist across all files in Topic 5.

## Lesson decisions

| Lesson | Decision | Audit result |
| :--- | :--- | :--- |
| `9702_t05_cm01_l01` | keep | Covers outcomes m01_o01 and o02; work done \(W = Fs\cos\theta\), zero work perpendicular forces, force-displacement area, and expanding gas \(W = p\Delta V\). |
| `9702_t05_cm01_l02` | keep | Covers outcomes m01_o03 and o04; principle of conservation of energy, energy dissipation, efficiency calculations, and Sankey diagrams. |
| `9702_t05_cm01_l03` | keep | Covers outcome m01_o05; power definition \(P = W/t\), units (Watt, SI base units), and energy transfer rate. |
| `9702_t05_cm01_l04` | keep | Covers outcomes m01_o06 and o07; solving power problems, derivation and application of \(P = Fv\), and vehicles at constant speed. |
| `9702_t05_cm02_l05` | keep | Covers outcomes m02_o01 and o02; derivation of \(\Delta E_p = mg\Delta h\), uniform field conditions, and path independence on slopes. |
| `9702_t05_cm02_l06` | keep | Covers outcomes m02_o03 and o04; derivation of \(E_k = \frac{1}{2}mv^2\) from kinematic equations and work-energy theorem, calculation, and application. |

## Unresolved mapping or knowledge-base issues

None requiring separate authorization.
