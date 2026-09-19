# Topic 15 Markdown audit

**PASS**

**HTML gate: OPEN.** All 4 active planned lessons and build evidence records exist, cover 100% of syllabus learning outcomes (9702_t15_m01_o01 through o02, 9702_t15_m02_o01 through o03, and 9702_t15_m03_o01 through o04), and have no unresolved topic-level defects.

## Topic-wide findings

- Coverage is complete against `syllabus.json` across all 3 course modules and 4 active lessons (with retired `cm02_l03` correctly redirected to `cm02_l02`):
  - `9702_t15_cm01` (The mole):
    - `9702_t15_cm01_l01` owns amount of substance as an SI base quantity with base unit mol, carbon-12 reference standard (\,\mathrm{g}$ of {12}\mathrm{C}$), the Avogadro constant $, specifying elementary entities, and quantitative molar conversions ( = nN_A, m = nM, m_\text{particle} = M/N_A$) (`9702_t15_m01_o01`, `9702_t15_m01_o02`).
  - `9702_t15_cm02` (Equation of state):
    - `9702_t15_cm02_l02` owns the definition of an ideal gas ( \propto T$), thermodynamic temperature in kelvin ( = \theta + 273.15$), conditions for ideal behaviour (low pressure, high temperature) vs real gas deviations, the molar equation of state ( = nRT$), the molecular equation of state ( = NkT$), and the universal relation  = R/N_A$ (`9702_t15_m02_o01`, `9702_t15_m02_o02`, `9702_t15_m02_o03`).
  - `9702_t15_cm03` (Kinetic theory of gases):
    - `9702_t15_cm03_l04` owns stating and explaining the basic assumptions of kinetic theory (continuous random motion, negligible molecular volume, no intermolecular forces except during collisions, perfectly elastic collisions, negligible collision time, negligible gravity), microscopic origin of pressure from momentum transfer ($\Delta p = 2mu$), and step-by-step 3D derivation of  = \frac{1}{3}Nm\langle c^2\rangle$ and density form  = \frac{1}{3}\rho\langle c^2\rangle$ (`9702_t15_m03_o01`, `9702_t15_m03_o02`).
    - `9702_t15_cm03_l05` owns understanding root-mean-square speed \text{rms} = \sqrt{\langle c^2\rangle}$, equating  = \frac{1}{3}Nm\langle c^2\rangle$ with  = NkT$ to deduce average translational kinetic energy of a gas molecule  = \frac{1}{2}m\langle c^2\rangle = \frac{3}{2}kT$, thermodynamic temperature as a direct measure of molecular translational kinetic energy, speed distributions, and total internal energy  = \frac{3}{2}NkT = \frac{3}{2}nRT$ (`9702_t15_m03_o03`, `9702_t15_m03_o04`).
- Sequence is coherent, prerequisite-led, and forms a strictly acyclic DAG across Modules 1 to 3: `cm01_l01 -> cm02_l02 -> cm03_l04 -> cm03_l05`. Opening hooks and closing handoffs match consistently across transitions.
- Purposeful retrieval across lessons:
  - The concept of amount of substance and Avogadro constant from l01 is directly operationalized in l02 to transition between  = nRT$ and  = NkT$ via  = R/N_A$.
  - The equation of state from l02 is retrieved in l05 and combined with kinetic theory pressure from l04 to deduce the molecular kinetic energy  = \frac{3}{2}kT$.
- Controlled definitions match the official knowledge base byte-for-byte:
  - Mole (`9702_def_mole`): "the amount of substance containing the same number of elementary entities as there are atoms in 12 g of carbon-12" (Lesson 1)
  - Avogadro constant (`9702_def_avogadro_constant`): "the number of atoms in 12 g of carbon-12" (Lesson 1)
  - Ideal gas (`9702_def_ideal_gas`): "a gas that obeys the equation of state pV = nRT at all pressures, volumes and thermodynamic temperatures" (Lesson 2)
- Controlled formulas preserve exact LaTeX, symbols, units, and conditions:
  - Molar equation of state:  = nRT$
  - Molecular equation of state:  = NkT$
  - Kinetic theory pressure:  = \frac{1}{3}Nm\langle c^2\rangle$
  - Translational kinetic energy: $\frac{1}{2}m\langle c^2\rangle = \frac{3}{2}kT$
- Scientific accuracy and calculations:
  - Clear distinction between macroscopic properties (, V, T, n$) and microscopic properties (, N, \langle c^2\rangle, k$).
  - Temperature in gas equations is strictly thermodynamic in kelvin (/\mathrm{K} = \theta/^\circ\mathrm{C} + 273.15$).
  - Root-mean-square speed correctly distinguishes $\sqrt{\langle c^2\rangle}$ from mean speed $\langle c\rangle$.
  - In an ideal gas, zero intermolecular forces means zero internal potential energy ( = 0$), so internal energy is purely translational kinetic energy.
- Misconceptions repaired across the topic:
  - Using Celsius temperatures in gas equations.
  - Confusing molar gas constant $ with Boltzmann constant $.
  - Forgetting to convert volume from $\mathrm{cm^3}$ or $\mathrm{dm^3}$ to $\mathrm{m^3}$.
  - Believing average velocity of gas molecules in a stationary container is non-zero (velocity vector sum is zero, speed root-mean-square is non-zero).
  - Believing gas molecules at the same temperature have the same speed (they have the same average kinetic energy; lighter molecules have higher \text{rms}$).
- Evidence provenance is complete across all 4 active lessons, drawing from over 30 authentic past-paper parts.
- Dash policy: Strictly ZERO em dashes (\u2014) and strictly ZERO en dashes (\u2013) exist across all files in Topic 15.

## Lesson decisions

| Lesson | Decision | Audit result |
| :--- | :--- | :--- |
| `9702_t15_cm01_l01` | keep | Covers outcomes m01_o01 and o02; mole definition, carbon-12 standard, Avogadro constant $, and molar calculations. |
| `9702_t15_cm02_l02` | keep | Covers outcomes m02_o01, o02, and o03; ideal gas definition,  = nRT$,  = NkT$,  = R/N_A$, and real gas conditions (consolidated with redirected cm02_l03). |
| `9702_t15_cm03_l04` | keep | Covers outcomes m03_o01 and o02; kinetic theory assumptions, pressure origin, and 3D derivation of  = \frac{1}{3}Nm\langle c^2\rangle$. |
| `9702_t15_cm03_l05` | keep | Covers outcomes m03_o03 and o04; root-mean-square speed \text{rms}$, deduction of  = \frac{3}{2}kT$, and internal energy of ideal gas. |

## Unresolved mapping or knowledge-base issues

None requiring separate authorization.
