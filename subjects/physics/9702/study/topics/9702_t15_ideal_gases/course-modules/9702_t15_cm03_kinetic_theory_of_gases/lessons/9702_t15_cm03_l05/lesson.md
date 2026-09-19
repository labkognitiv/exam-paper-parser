# Root-Mean-Square Speed and Translational Kinetic Energy

## Learning Outcomes

In this lesson, you will learn to:
- Understand that the root-mean-square speed $c_{\text{rms}}$ (or $c_{\text{r.m.s.}}$) of gas molecules is given by $\sqrt{\langle c^2\rangle}$ (Cambridge outcome `9702_t15_m03_o03`).
- Compare the kinetic theory equation $pV = \frac{1}{3}Nm\langle c^2\rangle$ with the ideal gas equation of state $pV = NkT$ to deduce that the average translational kinetic energy of a molecule is:
  \[
  E_K = \frac{3}{2}kT
  \]
  (Cambridge outcome `9702_t15_m03_o04`).
- Recall and use the expression $E_K = \frac{1}{2}m\langle c^2\rangle = \frac{3}{2}kT$ to solve quantitative problems involving molecular speeds, thermodynamic temperature, and gas internal energy (Cambridge outcome `9702_t15_m03_o04`).
- Relate root-mean-square speed directly to thermodynamic temperature and molecular mass:
  \[
  c_{\text{rms}} = \sqrt{\frac{3kT}{m}} = \sqrt{\frac{3RT}{M_m}}
  \]

---

## Prior Knowledge

Before beginning this lesson, you should be familiar with:
- **The kinetic theory pressure equation** (from Lesson 4):
  \[
  pV = \frac{1}{3}Nm\langle c^2\rangle
  \]
  where $p$ is pressure, $V$ is volume, $N$ is the number of molecules, $m$ is the mass of one molecule, and $\langle c^2\rangle$ is the mean-square speed.
- **The microscopic equation of state for an ideal gas** (from Lesson 2):
  \[
  pV = NkT
  \]
  where $k$ is the Boltzmann constant ($1.38 \times 10^{-23}\text{ J K}^{-1}$) and $T$ is the thermodynamic temperature in kelvin ($\text{K}$).
- **The molar gas constant and Avogadro constant:**
  \[
  k = \frac{R}{N_A}
  \]
  where $R = 8.31\text{ J K}^{-1}\text{ mol}^{-1}$ and $N_A = 6.02 \times 10^{23}\text{ mol}^{-1}$.
- **Kinetic energy of a moving mass:**
  \[
  E_K = \frac{1}{2}mv^2
  \]

---

## Core Concepts

### Why Can We Not Use Average Velocity?

In a sample of gas containing $N$ molecules, each molecule moves with its own instantaneous velocity vector $\vec{c}_i$. Because molecular motion is completely random with no preferred direction, for every molecule travelling in one direction, another molecule is equally likely to be travelling in the opposite direction.

If you calculate the vector average of the molecular velocities:
\[
\langle\vec{c}\rangle = \frac{1}{N}\sum_{i=1}^N \vec{c}_i = 0
\]
The average velocity of the molecules in any stationary gas is strictly zero.

Average velocity is useless for describing the thermal energy of the gas. The molecules are moving at hundreds of metres per second, carrying substantial kinetic energy, even though the net velocity of the gas as a whole is zero.

---

### Why Root-Mean-Square Speed ($c_{\text{rms}}$)?

To describe how fast molecules are moving regardless of direction, we must look at speed (a scalar). More fundamentally, thermal physics connects directly to energy. The kinetic energy of an individual molecule of mass $m$ travelling at speed $c$ is:
\[
E_{K, i} = \frac{1}{2}m c_i^2
\]

Notice that kinetic energy depends on the **square of the speed** ($c_i^2$). Because the square of any real number is positive, squaring eliminates the directional cancellation.

The total translational kinetic energy of all $N$ molecules is:
\[
E_{K, \text{total}} = \sum_{i=1}^N \frac{1}{2}m c_i^2 = \frac{1}{2}m \sum_{i=1}^N c_i^2
\]

The average translational kinetic energy per molecule, denoted $\langle E_K\rangle$ or $E_K$, is:
\[
E_K = \frac{E_{K, \text{total}}}{N} = \frac{1}{2}m \left(\frac{1}{N}\sum_{i=1}^N c_i^2\right) = \frac{1}{2}m\langle c^2\rangle
\]

where $\langle c^2\rangle$ is the **mean-square speed** (the mean of the squares of the speeds).

To obtain a quantity with the dimensions of speed (metres per second) that directly corresponds to this average kinetic energy, we take the square root of the mean-square speed. This quantity is the **root-mean-square speed**, abbreviated as $c_{\text{rms}}$ or $c_{\text{r.m.s.}}$:

\[
c_{\text{rms}} = \sqrt{\langle c^2\rangle}
\]

---

### Step-by-Step Meaning of the Name: Root-Mean-Square

The name "root-mean-square" explains the exact mathematical operation, read in reverse order:

1. **Square:** First square each individual molecular speed:
   \[
   c_1^2, c_2^2, c_3^2, \dots, c_N^2
   \]
2. **Mean:** Take the arithmetic average (mean) of all these squared values:
   \[
   \langle c^2\rangle = \frac{c_1^2 + c_2^2 + c_3^2 + \dots + c_N^2}{N}
   \]
3. **Root:** Take the square root of that mean:
   \[
   c_{\text{rms}} = \sqrt{\langle c^2\rangle}
   \]

---

### Difference Between Mean Speed and Root-Mean-Square Speed

It is vital not to confuse the root-mean-square speed $c_{\text{rms}}$ with the arithmetic mean speed $\langle c\rangle$.

- The **mean speed** $\langle c\rangle$ is simply the average of the speeds:
  \[
  \langle c\rangle = \frac{c_1 + c_2 + \dots + c_N}{N}
  \]
- The **root-mean-square speed** $c_{\text{rms}}$ is the square root of the average of the squared speeds:
  \[
  c_{\text{rms}} = \sqrt{\frac{c_1^2 + c_2^2 + \dots + c_N^2}{N}}
  \]

For any collection of particles that do not all travel at the exact same speed, the root-mean-square speed is always greater than the mean speed:
\[
c_{\text{rms}} > \langle c\rangle
\]

#### Simple Numerical Illustration:
Consider a tiny group of three particles with speeds $300\text{ m s}^{-1}$, $400\text{ m s}^{-1}$, and $500\text{ m s}^{-1}$.
- **Mean speed:**
  \[
  \langle c\rangle = \frac{300 + 400 + 500}{3} = \frac{1200}{3} = 400\text{ m s}^{-1}
  \]
- **Mean-square speed:**
  \[
  \langle c^2\rangle = \frac{300^2 + 400^2 + 500^2}{3} = \frac{90000 + 160000 + 250000}{3} = \frac{500000}{3} \approx 166667\text{ m}^2\text{ s}^{-2}
  \]
- **Root-mean-square speed:**
  \[
  c_{\text{rms}} = \sqrt{\langle c^2\rangle} = \sqrt{166667} \approx 408.2\text{ m s}^{-1}
  \]
Notice that $c_{\text{rms}} = 408.2\text{ m s}^{-1}$ is distinctly larger than $\langle c\rangle = 400\text{ m s}^{-1}$.

In kinetic theory and thermodynamics, **$c_{\text{rms}}$ is the speed that matters**, because it is directly related to kinetic energy:
\[
E_K = \frac{1}{2}m\langle c^2\rangle = \frac{1}{2}m c_{\text{rms}}^2
\]

---

## Detailed Derivations

### Deducing the Average Translational Kinetic Energy: $E_K = \frac{3}{2}kT$

One of the most celebrated derivations in physics unites macroscopic gas laws with microscopic mechanics.

<a id="formula-9702_formula_ideal_gas_equation_molecules"></a>

> **Formula to learn: Ideal gas equation (molecular form).**
>
> \[
> pV = NkT
> \]

<a id="formula-9702_formula_kinetic_theory_pressure"></a>

> **Formula to learn: Kinetic theory pressure equation.**
>
> \[
> pV = \frac{1}{3}Nm\langle c^2\rangle
> \]

<a id="formula-9702_formula_kinetic_energy_gas_molecule"></a>

> **Formula to learn: Translational kinetic energy of a gas molecule.**
>
> \[
> \frac{1}{2}m\langle c^2\rangle = \frac{3}{2}kT
> \]

#### Step-by-step deduction:

1. **Write down the kinetic theory equation** derived from microscopic collision mechanics (Lesson 4):
   \[
   pV = \frac{1}{3}Nm\langle c^2\rangle
   \]

2. **Write down the experimental equation of state** for an ideal gas written in molecular form (Lesson 2):
   \[
   pV = NkT
   \]
   where $k$ is the Boltzmann constant and $T$ is the thermodynamic temperature in kelvin.

3. **Equate the two expressions** for the product $pV$:
   \[
   \frac{1}{3}Nm\langle c^2\rangle = NkT
   \]

4. **Divide both sides by $N$** (the total number of molecules):
   \[
   \frac{1}{3}m\langle c^2\rangle = kT
   \]

5. **Multiply both sides by $\frac{3}{2}$** to isolate the kinetic energy term $\frac{1}{2}m\langle c^2\rangle$:
   \[
   \frac{3}{2} \times \left(\frac{1}{3}m\langle c^2\rangle\right) = \frac{3}{2} \times (kT)
   \]
   \[
   \frac{1}{2}m\langle c^2\rangle = \frac{3}{2}kT
   \]

6. **Identify the left-hand side** as the average translational kinetic energy of one molecule, $E_K$:
   \[
   E_K = \frac{3}{2}kT
   \]

---

### Physical Significance of $E_K = \frac{3}{2}kT$

This compact formula reveals three profound physics principles:

1. **Direct definition of thermodynamic temperature:**
   Thermodynamic temperature $T$ is directly proportional to the average translational kinetic energy of the molecules:
   \[
   E_K \propto T
   \]
   Temperature is not an arbitrary number on a dial; it is a direct measurement of how vigorously particles vibrate and fly around at the microscopic level.

2. **Independence from molecular mass and gas species:**
   Notice that the mass $m$ of the molecule does not appear on the right-hand side of $E_K = \frac{3}{2}kT$.
   - At a given temperature $T$, **every ideal gas molecule possesses the exact same average translational kinetic energy**, regardless of whether it is a light hydrogen molecule ($\text{H}_2$), a helium atom ($\text{He}$), or a heavy xenon atom ($\text{Xe}$).
   - If a mixture of helium and krypton is in thermal equilibrium at temperature $T$, both types of atoms have identical average translational kinetic energy:
     \[
     E_{K, \text{He}} = E_{K, \text{Kr}} = \frac{3}{2}kT
     \]

3. **Absolute zero ($T = 0\text{ K}$):**
   If $T = 0\text{ K}$, the translational kinetic energy predicted by classical kinetic theory becomes zero ($E_K = 0$). This gives absolute zero its physical meaning as the temperature where classical translational motion ceases.

---

### Derivation of Root-Mean-Square Speed in Terms of Temperature

We can now express the root-mean-square speed $c_{\text{rms}}$ explicitly in terms of temperature $T$ and molecular mass $m$:

Starting from:
\[
\frac{1}{2}m c_{\text{rms}}^2 = \frac{3}{2}kT
\]

Multiply both sides by 2:
\[
m c_{\text{rms}}^2 = 3kT
\]

Divide by $m$:
\[
c_{\text{rms}}^2 = \frac{3kT}{m}
\]

Take the square root of both sides:
\[
c_{\text{rms}} = \sqrt{\frac{3kT}{m}}
\]

#### Expressing $c_{\text{rms}}$ in Terms of Molar Quantities
Recall that $k = \frac{R}{N_A}$ and the molar mass $M_m$ (mass of one mole of molecules in kilograms) is related to molecular mass by:
\[
M_m = m N_A \implies m = \frac{M_m}{N_A}
\]

Substituting $k = \frac{R}{N_A}$ and $m = \frac{M_m}{N_A}$ into the formula gives:
\[
c_{\text{rms}} = \sqrt{\frac{3\left(\frac{R}{N_A}\right)T}{\frac{M_m}{N_A}}} = \sqrt{\frac{3RT}{M_m}}
\]

This alternative form is especially useful when the molar mass $M_m$ is given in kilograms per mole ($\text{kg mol}^{-1}$).

---

### Two Crucial Proportionalities for $c_{\text{rms}}$

From the equation $c_{\text{rms}} = \sqrt{\frac{3kT}{m}}$:

1. **Variation with thermodynamic temperature ($c_{\text{rms}} \propto \sqrt{T}$):**
   - The root-mean-square speed is proportional to the square root of the thermodynamic temperature (in kelvin).
   - If the thermodynamic temperature of a gas is doubled ($T_2 = 2T_1$), its root-mean-square speed increases by a factor of $\sqrt{2} \approx 1.41$, not by a factor of 2.
   - To double the root-mean-square speed, the thermodynamic temperature must be quadrupled ($T_2 = 4T_1$).
   - A graph of $c_{\text{rms}}$ against $T$ starts at the origin $(0,0)$ and curves upward with a positive, decreasing gradient (characteristic of a square-root curve $y \propto \sqrt{x}$).

2. **Variation with molecular mass ($c_{\text{rms}} \propto \frac{1}{\sqrt{m}}$):**
   - At a constant temperature, lighter molecules have a higher root-mean-square speed than heavier molecules.
   - For example, consider helium ($M_m = 0.004\text{ kg mol}^{-1}$) and oxygen ($M_m = 0.032\text{ kg mol}^{-1}$) at the same temperature. Oxygen molecules are 8 times heavier than helium atoms. Therefore, helium atoms travel $\sqrt{8} \approx 2.83$ times faster than oxygen molecules.

---

### Total Internal Energy of an Ideal Gas

Recall the third assumption of the kinetic theory (Lesson 4): there are no intermolecular forces between molecules except during collisions.

Because there are no intermolecular forces, the intermolecular potential energy of an ideal gas is strictly zero:
\[
E_P = 0
\]

Internal energy $U$ is defined as the sum of the random distribution of kinetic and potential energies associated with the molecules of a system:
\[
U = E_{K, \text{total}} + E_{P, \text{total}}
\]

For an ideal gas, because $E_P = 0$, the internal energy is **entirely kinetic**:
\[
U = E_{K, \text{total}} = N \times E_K
\]

Substituting $E_K = \frac{3}{2}kT$:
\[
U = N \left(\frac{3}{2}kT\right) = \frac{3}{2}NkT
\]

Using the ideal gas relationships $NkT = nRT = pV$:
\[
U = \frac{3}{2}NkT = \frac{3}{2}nRT = \frac{3}{2}pV
\]

- Internal energy $U$ is measured in joules ($\text{J}$).
- For a fixed mass of an ideal gas, internal energy depends **only on its thermodynamic temperature $T$**.
- A change in internal energy is given by:
  \[
  \Delta U = \frac{3}{2}Nk\Delta T = \frac{3}{2}nR\Delta T
  \]

---

## Worked Examples with Cambridge Mark Schemes

### Worked Example 1: Deducing $E_K = \frac{3}{2}kT$ and Energy Calculations

1. The pressure $p$ and volume $V$ of an ideal gas are related by $pV = \frac{1}{3}Nm\langle c^2\rangle$. Use this equation, together with the equation of state for an ideal gas, to show that the mean translational kinetic energy $E_K$ of a molecule is given by $E_K = \frac{3}{2}kT$. [3 marks]
2. A sealed rigid container contains $24.0\text{ g}$ of oxygen gas ($\text{O}_2$) at a temperature of $22.0^{\circ}\text{C}$. The molar mass of oxygen gas is $32.0\text{ g mol}^{-1}$. Calculate:
   - The mean translational kinetic energy of an oxygen molecule. [2 marks]
   - The total internal energy of the oxygen gas in the container. [2 marks]

#### Strategy and Model Check
- Equate $pV = \frac{1}{3}Nm\langle c^2\rangle$ and $pV = NkT$. Cancel $N$, multiply by $3/2$.
- Temperature must be converted to kelvin: $T = 22.0 + 273.15 = 295.15\text{ K}$.
- Find amount of substance $n = \frac{24.0}{32.0} = 0.750\text{ mol}$, then $N = n N_A$.

#### Solutions and Mark Scheme Breakdown

**Part 1: Derivation**
- States $pV = NkT$ (or $pV = nRT$ with $n = N/N_A$ and $R = k N_A$) [B1]
- Equates: $\frac{1}{3}Nm\langle c^2\rangle = NkT \implies \frac{1}{3}m\langle c^2\rangle = kT$ [B1]
- Completes derivation: multiplies by $\frac{3}{2}$ to obtain $E_K = \frac{1}{2}m\langle c^2\rangle = \frac{3}{2}kT$ [B1]

**Part 2(a): Mean kinetic energy of a molecule**
Convert temperature to kelvin:
\[
T = 22.0 + 273.15 = 295.15\text{ K} \approx 295\text{ K}
\]
Apply formula:
\[
E_K = \frac{3}{2}kT = \frac{3}{2} \times (1.38 \times 10^{-23}\text{ J K}^{-1}) \times 295.15\text{ K}
\]
\[
E_K = 1.5 \times 1.38 \times 10^{-23} \times 295.15 = 6.1096 \times 10^{-21}\text{ J} \approx 6.11 \times 10^{-21}\text{ J}
\]
- Correct use of $T = 295\text{ K}$ (use of $T = 22\text{ K}$ scores 0/2) [C1]
- Final answer $6.11 \times 10^{-21}\text{ J}$ (or $6.1 \times 10^{-21}\text{ J}$) [A1]

**Part 2(b): Total internal energy**
Number of moles:
\[
n = \frac{24.0\text{ g}}{32.0\text{ g mol}^{-1}} = 0.750\text{ mol}
\]
Number of molecules:
\[
N = n N_A = 0.750 \times 6.02 \times 10^{23} = 4.515 \times 10^{23}\text{ molecules}
\]
Total internal energy:
\[
U = N \times E_K = (4.515 \times 10^{23}) \times (6.11 \times 10^{-21}\text{ J}) = 2758\text{ J} \approx 2.76 \times 10^3\text{ J}
\]
*(Alternatively: $U = \frac{3}{2}nRT = 1.5 \times 0.750 \times 8.31 \times 295.15 = 2759\text{ J}$.)*
- Method: $U = N \times E_K$ or $U = \frac{3}{2}nRT$ [C1]
- Final answer $2.76 \times 10^3\text{ J}$ (or $2.8 \times 10^3\text{ J}$) [A1]

---

### Worked Example 2: Calculating Root-Mean-Square Speed

Helium-4 ($^4_2\text{He}$) gas may be assumed to behave as an ideal gas. The mass of one helium-4 atom is $6.64 \times 10^{-27}\text{ kg}$.

1. Calculate the root-mean-square speed $c_{\text{rms}}$ of a helium-4 atom at a temperature of $27.0^{\circ}\text{C}$. [3 marks]
2. Krypton gas ($^{84}_{36}\text{Kr}$, atomic mass $1.39 \times 10^{-25}\text{ kg}$) is at the same temperature of $27.0^{\circ}\text{C}$.
   - State, with a reason, how the average translational kinetic energy of a krypton atom compares with that of a helium-4 atom. [1 mark]
   - Without recalculating from scratch, deduce the root-mean-square speed of a krypton atom at $27.0^{\circ}\text{C}$. [2 marks]

#### Strategy and Model Check
- For helium: convert $27.0^{\circ}\text{C}$ to $300\text{ K}$. Use $\frac{1}{2}m c_{\text{rms}}^2 = \frac{3}{2}kT$.
- For krypton: same $T$ means identical $E_K$. Speed scales as $c_{\text{rms}} \propto \frac{1}{\sqrt{m}}$.

#### Step 1: Helium-4 root-mean-square speed
Convert temperature:
\[
T = 27.0 + 273.15 = 300.15\text{ K} \approx 300\text{ K}
\]
Using $\frac{1}{2}m c_{\text{rms}}^2 = \frac{3}{2}kT$:
\[
\frac{1}{2} \times (6.64 \times 10^{-27}\text{ kg}) \times c_{\text{rms}}^2 = \frac{3}{2} \times (1.38 \times 10^{-23}\text{ J K}^{-1}) \times 300\text{ K}
\]
\[
3.32 \times 10^{-27} \times c_{\text{rms}}^2 = 6.21 \times 10^{-21}
\]
\[
c_{\text{rms}}^2 = \frac{6.21 \times 10^{-21}}{3.32 \times 10^{-27}} = 1.8705 \times 10^6\text{ m}^2\text{ s}^{-2}
\]
Taking the square root:
\[
c_{\text{rms}} = \sqrt{1.8705 \times 10^6\text{ m}^2\text{ s}^{-2}} = 1368\text{ m s}^{-1} \approx 1.37 \times 10^3\text{ m s}^{-1}
\]
- Formulation: $\frac{1}{2}m c_{\text{rms}}^2 = \frac{3}{2}kT$ with correct temperature $T = 300\text{ K}$ [C1]
- Calculation of $\langle c^2\rangle = 1.87 \times 10^6\text{ m}^2\text{ s}^{-2}$ [C1]
- Final answer $1.37 \times 10^3\text{ m s}^{-1}$ (accept $1.36 \times 10^3$ to $1.37 \times 10^3\text{ m s}^{-1}$) [A1]

#### Step 2(a): Comparison of kinetic energies
- Both gases have the **same** average translational kinetic energy because $E_K = \frac{3}{2}kT$ depends solely on thermodynamic temperature, which is identical ($300\text{ K}$) for both gases. [B1]

#### Step 2(b): Deduction of krypton speed
Because kinetic energies are equal:
\[
\frac{1}{2} m_{\text{Kr}} c_{\text{rms, Kr}}^2 = \frac{1}{2} m_{\text{He}} c_{\text{rms, He}}^2
\]
\[
c_{\text{rms, Kr}} = c_{\text{rms, He}} \times \sqrt{\frac{m_{\text{He}}}{m_{\text{Kr}}}}
\]
Substitute the values:
\[
c_{\text{rms, Kr}} = 1368\text{ m s}^{-1} \times \sqrt{\frac{6.64 \times 10^{-27}\text{ kg}}{1.39 \times 10^{-25}\text{ kg}}} = 1368 \times \sqrt{0.04777} = 1368 \times 0.21856 = 299\text{ m s}^{-1}
\]
- Method: Uses ratio $c_{\text{rms}} \propto 1/\sqrt{m}$ [C1]
- Final answer $299\text{ m s}^{-1}$ (accept $298$ to $300\text{ m s}^{-1}$) [A1]

---

### Worked Example 3: Thermal Energy and Temperature Rise

A rigid cylinder of constant volume $0.035\text{ m}^3$ contains an ideal monatomic gas at an initial pressure of $1.50 \times 10^5\text{ Pa}$ and an initial temperature of $280\text{ K}$.
An electrical heating coil supplies $1800\text{ J}$ of thermal energy to the gas. No gas escapes and volume remains constant.

1. Calculate the number $N$ of gas molecules in the cylinder. [2 marks]
2. Calculate the increase in average translational kinetic energy of a single molecule. [1 mark]
3. Calculate the final temperature of the gas in kelvin. [2 marks]
4. Determine the factor by which the root-mean-square speed of the molecules increased. [2 marks]

#### Strategy and Model Check
- Use $pV = NkT$ to find $N$.
- Because volume is constant, work done $W = 0$. By the first law, $\Delta U = \Delta Q = 1800\text{ J}$.
- Increase per molecule $\Delta E_K = \Delta U / N$.
- Use $\Delta E_K = \frac{3}{2}k\Delta T$ to find $\Delta T$, then $T_{\text{final}} = T_{\text{initial}} + \Delta T$.
- Factor of speed increase is $\frac{c_{\text{rms, 2}}}{c_{\text{rms, 1}}} = \sqrt{\frac{T_{\text{final}}}{T_{\text{initial}}}}$.

#### Step 1: Calculate the number of molecules $N$
\[
pV = NkT \implies N = \frac{pV}{kT}
\]
\[
N = \frac{(1.50 \times 10^5\text{ Pa}) \times (0.035\text{ m}^3)}{(1.38 \times 10^{-23}\text{ J K}^{-1}) \times (280\text{ K})} = \frac{5250}{3.864 \times 10^{-21}} = 1.359 \times 10^{24} \approx 1.36 \times 10^{24}\text{ molecules}
\]
- Formula rearranged and substituted [C1]
- Final answer $1.36 \times 10^{24}$ [A1]

#### Step 2: Increase in average kinetic energy per molecule
\[
\Delta E_K = \frac{\Delta U}{N} = \frac{1800\text{ J}}{1.359 \times 10^{24}} = 1.325 \times 10^{-21}\text{ J} \approx 1.32 \times 10^{-21}\text{ J} \text{ [A1]}
\]

#### Step 3: Final temperature of the gas
\[
\Delta E_K = \frac{3}{2}k\Delta T \implies \Delta T = \frac{\Delta E_K}{\frac{3}{2}k} = \frac{1.325 \times 10^{-21}\text{ J}}{1.5 \times (1.38 \times 10^{-23}\text{ J K}^{-1})} = \frac{1.325 \times 10^{-21}}{2.07 \times 10^{-23}} = 64.0\text{ K}
\]
Final temperature:
\[
T_{\text{final}} = T_{\text{initial}} + \Delta T = 280\text{ K} + 64.0\text{ K} = 344\text{ K}
\]
- Calculation of $\Delta T = 64\text{ K}$ (accept $64\text{ K}$ to $65\text{ K}$) [C1]
- Final answer $T = 344\text{ K}$ (accept $344\text{ K}$ to $345\text{ K}$) [A1]

#### Step 4: Factor of speed increase
Since $c_{\text{rms}} \propto \sqrt{T}$:
\[
\frac{c_{\text{rms, final}}}{c_{\text{rms, initial}}} = \sqrt{\frac{T_{\text{final}}}{T_{\text{initial}}}} = \sqrt{\frac{344\text{ K}}{280\text{ K}}} = \sqrt{1.2286} \approx 1.11
\]
- Ratio formula $\sqrt{T_2/T_1}$ using kelvin temperatures [C1]
- Final answer $1.11$ (an increase of $11\%$) [A1]

---

## Guided Practice

### Problem 1: Root-Mean-Square Speed of Hydrogen Molecules
The mass of a hydrogen molecule ($\text{H}_2$) is $3.34 \times 10^{-27}\text{ kg}$.
1. Calculate the root-mean-square speed of a hydrogen molecule at $20.0^{\circ}\text{C}$.
2. Calculate the temperature in degrees Celsius at which the root-mean-square speed of hydrogen molecules is doubled.

#### Worked Solution:
1. At $20.0^{\circ}\text{C}$, $T_1 = 20.0 + 273.15 = 293.15\text{ K}$.
   \[
   c_{\text{rms, 1}} = \sqrt{\frac{3kT_1}{m}} = \sqrt{\frac{3 \times (1.38 \times 10^{-23}) \times 293.15}{3.34 \times 10^{-27}}} = \sqrt{\frac{1.2136 \times 10^{-20}}{3.34 \times 10^{-27}}} = \sqrt{3.6337 \times 10^6} \approx 1.91 \times 10^3\text{ m s}^{-1}
   \]
2. Since $c_{\text{rms}} \propto \sqrt{T}$, to double the speed ($c_{\text{rms, 2}} = 2 c_{\text{rms, 1}}$), the thermodynamic temperature must quadruple:
   \[
   T_2 = 4 T_1 = 4 \times 293.15\text{ K} = 1172.6\text{ K}
   \]
   Convert back to degrees Celsius:
   \[
   \theta_2 = 1172.6 - 273.15 = 899.45^{\circ}\text{C} \approx 899^{\circ}\text{C}
   \]
   *(Notice: The Celsius temperature does NOT quadruple from $20^{\circ}\text{C}$ to $80^{\circ}\text{C}$; it rises to approximately $900^{\circ}\text{C}$!)*

---

### Problem 2: Graphical Relationships for $c_{\text{rms}}$
Sketch and describe:
1. The variation of root-mean-square speed $c_{\text{rms}}$ with thermodynamic temperature $T$.
2. The variation of root-mean-square speed $c_{\text{rms}}$ with gas pressure $p$ for a fixed mass of gas held at constant temperature.

#### Worked Solution:
1. **$c_{\text{rms}}$ versus $T$:**
   - Because $c_{\text{rms}} = \sqrt{\frac{3kT}{m}}$, $c_{\text{rms}} \propto \sqrt{T}$.
   - The graph starts at the origin $(0,0)$.
   - It is a smooth curve with positive, decreasing gradient (concave downwards). It never returns to either axis.
2. **$c_{\text{rms}}$ versus $p$ at constant temperature:**
   - Because $T$ is constant, $E_K = \frac{3}{2}kT$ is constant, so $c_{\text{rms}}$ is constant.
   - The graph is a horizontal straight line. Increasing pressure by compressing the gas at constant temperature packs the molecules closer together without changing their average speed.

---

### Problem 3: Escape of Gases from Planetary Atmospheres
The escape speed from Earth's atmosphere is approximately $1.12 \times 10^4\text{ m s}^{-1}$. At the top of the atmosphere, the temperature can reach $1000\text{ K}$.
1. Calculate the root-mean-square speed of hydrogen molecules ($\text{H}_2$, $m = 3.34 \times 10^{-27}\text{ kg}$) at $1000\text{ K}$.
2. Calculate the root-mean-square speed of oxygen molecules ($\text{O}_2$, $m = 5.31 \times 10^{-26}\text{ kg}$) at $1000\text{ K}$.
3. Explain why hydrogen has largely escaped from Earth's atmosphere while oxygen has been retained.

#### Worked Solution:
1. For hydrogen at $1000\text{ K}$:
   \[
   c_{\text{rms, H}_2} = \sqrt{\frac{3 \times (1.38 \times 10^{-23}) \times 1000}{3.34 \times 10^{-27}}} = \sqrt{\frac{4.14 \times 10^{-20}}{3.34 \times 10^{-27}}} = \sqrt{1.2395 \times 10^7} \approx 3.52 \times 10^3\text{ m s}^{-1}
   \]
2. For oxygen at $1000\text{ K}$:
   \[
   c_{\text{rms, O}_2} = \sqrt{\frac{3 \times (1.38 \times 10^{-23}) \times 1000}{5.31 \times 10^{-26}}} = \sqrt{\frac{4.14 \times 10^{-20}}{5.31 \times 10^{-26}}} = \sqrt{7.7966 \times 10^5} \approx 8.83 \times 10^2\text{ m s}^{-1}
   \]
3. Explanation:
   - In any gas, particles have a range of speeds described by a distribution; some molecules travel much faster than $c_{\text{rms}}$.
   - For hydrogen, $c_{\text{rms}} \approx 3520\text{ m s}^{-1}$ is roughly one-third of the escape speed ($11200\text{ m s}^{-1}$). A significant fraction of molecules in the high-speed tail of the distribution exceed escape speed and escape into space over geological time.
   - For oxygen, $c_{\text{rms}} \approx 883\text{ m s}^{-1}$ is less than one-twelfth of escape speed. The fraction of oxygen molecules with speeds exceeding escape speed is negligible, so oxygen remains gravitationally bound.

---

## Checks for Understanding

### Check 1: Comparing Molecular Kinetic Energies
A sealed container contains a mixture of $1\text{ mole}$ of helium gas (molar mass $4\text{ g mol}^{-1}$) and $1\text{ mole}$ of nitrogen gas (molar mass $28\text{ g mol}^{-1}$) in thermal equilibrium at temperature $T$. Which statement correctly compares their molecules?

- **A.** The helium atoms have greater average translational kinetic energy because they are lighter and move faster.
- **B.** The helium atoms and nitrogen molecules have identical average translational kinetic energy, but the helium atoms have a higher root-mean-square speed.

**Feedback for A:** Incorrect. Average translational kinetic energy is given by $E_K = \frac{3}{2}kT$, which depends solely on thermodynamic temperature $T$. It does not depend on molecular mass.

**Feedback for B:** Correct. Because both gases are at the same temperature $T$, their average translational kinetic energies are equal: $\frac{1}{2}m_{\text{He}}\langle c_{\text{He}}^2\rangle = \frac{1}{2}m_{\text{N}_2}\langle c_{\text{N}_2}^2\rangle = \frac{3}{2}kT$. Because helium atoms have smaller mass ($m_{\text{He}} < m_{\text{N}_2}$), they must have a higher root-mean-square speed ($c_{\text{rms}} \propto 1/\sqrt{m}$).

---

### Check 2: Effect of Doubling Thermodynamic Temperature
The thermodynamic temperature of an ideal gas is increased from $300\text{ K}$ to $600\text{ K}$. What happens to the root-mean-square speed $c_{\text{rms}}$ of the molecules?

- **A.** It doubles ($c_{\text{rms}}$ becomes $2.0 \times$ larger).
- **B.** It increases by a factor of $\sqrt{2} \approx 1.41$.

**Feedback for A:** Incorrect. Average kinetic energy doubles ($E_K \propto T$). However, speed is proportional to the square root of kinetic energy: $c_{\text{rms}} = \sqrt{\langle c^2\rangle} \propto \sqrt{T}$. Doubling $T$ does not double speed.

**Feedback for B:** Correct. Because $c_{\text{rms}} \propto \sqrt{T}$, when temperature is multiplied by 2, the root-mean-square speed is multiplied by $\sqrt{2} \approx 1.41$.

---

### Check 3: Isothermal Compression and Molecular Speed
A cylinder with a movable piston contains a fixed mass of ideal gas. The piston is pushed in slowly, halving the volume while keeping the temperature strictly constant. What happens to the root-mean-square speed of the gas molecules?

- **A.** It remains constant.
- **B.** It doubles because the pressure has doubled.

**Feedback for A:** Correct. Root-mean-square speed is given by $c_{\text{rms}} = \sqrt{\frac{3kT}{m}}$. It depends strictly on temperature $T$. Because the compression is isothermal ($T = \text{constant}$), the average kinetic energy and root-mean-square speed do not change. The doubled pressure is caused by higher collision frequency per unit area, not by faster molecules.

**Feedback for B:** Incorrect. Pressure increases because the same number of molecules now occupy half the volume, doubling the collision frequency with the walls. The molecules themselves do not move any faster at constant temperature.

---

### Check 4: Comparing $(\langle c\rangle)^2$ with $\langle c^2\rangle$
For a sample of gas molecules with a range of speeds, how does the square of the mean speed $(\langle c\rangle)^2$ compare with the mean-square speed $\langle c^2\rangle$?

- **A.** $(\langle c\rangle)^2 < \langle c^2\rangle$
- **B.** $(\langle c\rangle)^2 = \langle c^2\rangle$

**Feedback for A:** Correct. Because the square function is convex, the average of the squares is always strictly greater than the square of the average whenever there is a distribution of speeds. Therefore, $\langle c^2\rangle > (\langle c\rangle)^2$, which also means $c_{\text{rms}} > \langle c\rangle$.

**Feedback for B:** Incorrect. They would only be equal if every single molecule moved at the exact same speed, which violates the kinetic theory assumption of a random distribution of speeds.

---

## Common Misconceptions

### Misconception 1: Calculating $c_{\text{rms}}$ with temperature in degrees Celsius
- **Incorrect idea:** Substituting $\theta = 25$ into $c_{\text{rms}} = \sqrt{\frac{3kT}{m}}$.
- **Correct physics:** The formula $E_K = \frac{3}{2}kT$ was deduced directly from the ideal gas equation of state $pV = NkT$, where $T$ is the **thermodynamic temperature in kelvin**. You must always convert Celsius to kelvin by adding $273$ (or $273.15$). Using Celsius will give completely incorrect results and score 0 marks in Cambridge examinations.

### Misconception 2: Different gases at the same temperature have the same speed
- **Incorrect idea:** Believing that at room temperature, all gas molecules move at the same speed.
- **Correct physics:** They have the **same average translational kinetic energy** ($E_K = \frac{3}{2}kT$), but **different speeds**. Lighter molecules travel faster ($c_{\text{rms}} \propto 1/\sqrt{m}$).

### Misconception 3: Doubling Celsius temperature doubles molecular speed or energy
- **Incorrect idea:** Thinking that heating a gas from $20^{\circ}\text{C}$ to $40^{\circ}\text{C}$ doubles the kinetic energy of its molecules.
- **Correct physics:** Proportionality holds only for the **thermodynamic scale**. $20^{\circ}\text{C} = 293\text{ K}$, and $40^{\circ}\text{C} = 313\text{ K}$. The temperature increase is only $\frac{313}{293} \approx 1.068$ (a $6.8\%$ increase), so kinetic energy increases by only $6.8\%$ and $c_{\text{rms}}$ increases by only about $3.4\%$.

### Misconception 4: High pressure means molecules are travelling faster
- **Incorrect idea:** Assuming gas in a high-pressure cylinder must have faster molecules than gas in a low-pressure room.
- **Correct physics:** Molecular speed depends on **temperature**, not pressure. A cylinder of compressed nitrogen at $20^{\circ}\text{C}$ has molecules moving at the exact same average speed as nitrogen in the surrounding room at $20^{\circ}\text{C}$. The higher pressure inside the cylinder is due to higher molecular density ($N/V$), which creates a vastly higher collision rate per unit area.

---

## Core Recap

- **Root-mean-square speed:**
  \[
  c_{\text{rms}} = \sqrt{\langle c^2\rangle}
  \]
  where $\langle c^2\rangle$ is the mean of the squared speeds of all molecules. For any speed distribution, $c_{\text{rms}} > \langle c\rangle$.
- **Deduction of average translational kinetic energy:**
  Comparing $pV = \frac{1}{3}Nm\langle c^2\rangle$ with $pV = NkT$ yields:
  \[
  E_K = \frac{1}{2}m\langle c^2\rangle = \frac{3}{2}kT
  \]
- **Temperature and kinetic energy:**
  The average translational kinetic energy of a molecule is directly proportional to thermodynamic temperature $T$ in kelvin, and is independent of molecular mass.
- **Root-mean-square speed formulas:**
  \[
  c_{\text{rms}} = \sqrt{\frac{3kT}{m}} = \sqrt{\frac{3RT}{M_m}}
  \]
  - $c_{\text{rms}} \propto \sqrt{T}$ (quadrupling $T$ doubles $c_{\text{rms}}$).
  - $c_{\text{rms}} \propto \frac{1}{\sqrt{m}}$ (lighter molecules move faster at the same temperature).
  - At constant $T$, changing pressure or volume does not alter $c_{\text{rms}}$.
- **Internal energy of an ideal gas:**
  Because intermolecular forces are zero, potential energy is zero ($E_P = 0$). Internal energy is purely kinetic:
  \[
  U = \frac{3}{2}NkT = \frac{3}{2}nRT = \frac{3}{2}pV
  \]
