# Amount of substance is an SI base quantity with the base unit mol

## How do physicists count the uncountably small?

When you measure a volume of water or weigh a cylinder of compressed gas, you are handling vast crowds of microscopic particles. A single breath of air contains tens of billions of trillions of gas molecules. Attempting to track every individual molecule by counting $1, 2, 3, \dots$ is physically impossible.

Yet in physics, the number of particles directly dictates macroscopic properties: the pressure a gas exerts on its container, the thermal energy it stores, and the electrical charge it carries. We need a bridge between the macroscopic world of balances and measuring cylinders, and the microscopic world of atoms and molecules.

To provide this bridge, the International System of Units (SI) defines a dedicated base quantity: the **amount of substance**, measured in **moles**.

---

## Amount of substance as an SI base quantity

In your AS Level studies, you learned that all physical quantities in science are constructed from seven fundamental **SI base quantities**:

1. Length (base unit: metre, $\mathrm{m}$)
2. Mass (base unit: kilogram, $\mathrm{kg}$)
3. Time (base unit: second, $\mathrm{s}$)
4. Electric current (base unit: ampere, $\mathrm{A}$)
5. Thermodynamic temperature (base unit: kelvin, $\mathrm{K}$)
6. Luminous intensity (base unit: candela, $\mathrm{cd}$)
7. **Amount of substance** (base unit: **mole**, symbol: **$\mathrm{mol}$**)

Notice that amount of substance is not a derived quantity. It cannot be expressed as a combination of kilograms, metres, or seconds. It is a distinct, fundamental dimension of measurement.

### Crucial distinction: amount of substance versus mass

A common beginner mistake is to confuse **amount of substance** ($n$) with **mass** ($m$):

- **Mass ($m$, in $\mathrm{kg}$)** measures a body's resistance to acceleration (its inertia) and its gravitational interaction. One kilogram of lead and one kilogram of helium have the exact same mass ($1\,\mathrm{kg}$).
- **Amount of substance ($n$, in $\mathrm{mol}$)** measures the quantity of elementary entities (particles) present in a sample. Because a lead atom is roughly 52 times heavier than a helium atom, one kilogram of helium contains roughly 52 times more atoms than one kilogram of lead!

Amount of substance is therefore proportional to the **number of particles**, regardless of how heavy each particle is.

---

## The Avogadro constant $N_A$

To connect the macroscopic amount of substance $n$ (in moles) to the actual number of individual particles $N$ (a pure count), physics relies on a fundamental physical constant: the **Avogadro constant**, denoted $N_A$.

<a id="definition-9702_def_avogadro_constant"></a>

> **Definition to learn: Avogadro constant.** the number of atoms in 12 g of carbon-12

Let us examine every term in this formal Cambridge definition:
- **12 g of carbon-12:** Carbon-12 ($^{12}\mathrm{C}$) is chosen as the international reference standard. In SI base units, $12\,\mathrm{g}$ is written as $0.012\,\mathrm{kg}$. A carbon-12 nucleus contains exactly 6 protons and 6 neutrons, giving it an atomic mass of exactly 12 unified atomic mass units.
- **Number of atoms:** Experiments show that $12\,\mathrm{g}$ ($0.012\,\mathrm{kg}$) of pure carbon-12 contains approximately $6.02 \times 10^{23}$ carbon atoms.

### Value and units of the Avogadro constant

On the Cambridge International A Level Physics data sheet, the value is given as:

\[
N_A = 6.02 \times 10^{23}\,\mathrm{mol^{-1}}
\]

Notice the unit: **$\mathrm{mol^{-1}}$** (per mole). In modern SI terminology, the Avogadro constant is also accepted as the **number of particles per unit amount of substance**. It is not a dimensionless number; it is a conversion factor that tells us how many particles exist in every one mole of substance.

---

## The mole ($\mathrm{mol}$)

The mole is the SI base unit of amount of substance. Its formal definition links directly to the carbon-12 standard:

<a id="definition-9702_def_mole"></a>

> **Definition to learn: mole.** the amount of substance containing the same number of elementary entities as there are atoms in 12 g of carbon-12

In examination questions, Cambridge also accepts the equivalent phrasing:
- *the amount of substance containing the Avogadro constant number of particles ($6.02 \times 10^{23}$ particles)*.

### Specifying the elementary entity

When using the mole, you must always state clearly what **elementary entity** is being counted. An entity can be an atom, a molecule, an ion, an electron, or a specified group of particles.

Consider oxygen gas:
- Oxygen gas at room temperature exists as diatomic molecules, $\mathrm{O_2}$.
- $1\,\mathrm{mol}$ of oxygen molecules ($\mathrm{O_2}$) contains $6.02 \times 10^{23}$ molecules of $\mathrm{O_2}$.
- Because each $\mathrm{O_2}$ molecule consists of two oxygen atoms, $1\,\mathrm{mol}$ of oxygen molecules contains $2 \times 6.02 \times 10^{23} = 1.20 \times 10^{24}$ oxygen atoms ($\mathrm{O}$).
- That means $1\,\mathrm{mol}$ of oxygen molecules contains $2\,\mathrm{mol}$ of oxygen atoms!

Failing to state whether you are discussing moles of molecules or moles of atoms is one of the most common causes of lost marks in thermal physics.

---

## Quantitative relationships: connecting $n$, $N$, mass, and molar mass

### 1. Connecting amount of substance to particle count

The fundamental relationship between the number of particles $N$ and the amount of substance $n$ is:

\[
N = n N_A
\]

or, rearranging for amount of substance $n$:

\[
n = \frac{N}{N_A}
\]

Where:
- $N$ is the total number of particles (dimensionless integer).
- $n$ is the amount of substance in moles ($\mathrm{mol}$).
- $N_A$ is the Avogadro constant, $6.02 \times 10^{23}\,\mathrm{mol^{-1}}$.

### 2. Molar mass $M$

The **molar mass** $M$ of a substance is the mass of one mole of that substance.

- In chemistry, molar mass is almost universally quoted in grams per mole ($\mathrm{g\,mol^{-1}}$), corresponding directly to relative atomic mass $A_r$ or relative molecular mass $M_r$. For example, helium has $M = 4.00\,\mathrm{g\,mol^{-1}}$, and argon has $M = 39.95\,\mathrm{g\,mol^{-1}} \approx 40.0\,\mathrm{g\,mol^{-1}}$.
- In physics, equations require SI base units. You must convert molar mass into kilograms per mole:
  \[
  M\,(\mathrm{kg\,mol^{-1}}) = M\,(\mathrm{g\,mol^{-1}}) \times 10^{-3}
  \]
  For example, for helium: $M = 4.00 \times 10^{-3}\,\mathrm{kg\,mol^{-1}}$.

### 3. Total mass of a sample

If a sample consists of $n$ moles of substance with molar mass $M$:

\[
m = n M
\]

or, rearranging for the amount of substance:

\[
n = \frac{m}{M}
\]

Where:
- $m$ is the total mass of the sample in kilograms ($\mathrm{kg}$).
- $n$ is the amount of substance in moles ($\mathrm{mol}$).
- $M$ is the molar mass in kilograms per mole ($\mathrm{kg\,mol^{-1}}$).

### 4. Mass of an individual particle

Because one mole contains $N_A$ particles and has a mass of $M$, the mass $m_{\mathrm{particle}}$ of a single particle is:

\[
m_{\mathrm{particle}} = \frac{M}{N_A}
\]

Similarly, if you know the total mass $m$ and the total number of particles $N$:

\[
m_{\mathrm{particle}} = \frac{m}{N}
\]

Combining these gives the master identity linking microscopic and macroscopic masses:

\[
m_{\mathrm{total}} = n M = N m_{\mathrm{particle}}
\]

---

## Worked examples

### Worked Example 1: Atoms and electrons in a noble gas sample

A sealed glass bulb contains $12.0\,\mathrm{g}$ of pure argon gas ($\mathrm{Ar}$). Argon is a monatomic gas with a molar mass of $40.0\,\mathrm{g\,mol^{-1}}$ and an atomic number of 18.

Calculate:
1. the amount of argon gas in the bulb, in moles;
2. the number of argon atoms in the bulb;
3. the total number of electrons in the argon gas.

#### Solution and Cambridge mark scheme

##### Part 1: Amount of argon in moles

Convert the mass to kilograms or work consistently in grams:
\[
m = 12.0\,\mathrm{g} = 12.0 \times 10^{-3}\,\mathrm{kg}
\]
\[
M = 40.0\,\mathrm{g\,mol^{-1}} = 40.0 \times 10^{-3}\,\mathrm{kg\,mol^{-1}}
\]
\[
n = \frac{m}{M} = \frac{12.0 \times 10^{-3}\,\mathrm{kg}}{40.0 \times 10^{-3}\,\mathrm{kg\,mol^{-1}}} = 0.300\,\mathrm{mol}
\]

- **[C1]** Correct formula $n = \frac{m}{M}$ and substitution: $\frac{12.0}{40.0}$
- **[A1]** Amount of substance $n = 0.300\,\mathrm{mol}$ (or $0.30\,\mathrm{mol}$)

##### Part 2: Number of argon atoms

Use $N = n N_A$:
\[
N = 0.300\,\mathrm{mol} \times 6.02 \times 10^{23}\,\mathrm{mol^{-1}} = 1.806 \times 10^{23} \approx 1.81 \times 10^{23}
\]

- **[C1]** Use of $N = n N_A$ with candidate answer from Part 1
- **[A1]** Number of atoms $N = 1.81 \times 10^{23}$

##### Part 3: Total number of electrons

Each neutral argon atom has an atomic number of 18, meaning it contains 18 electrons:
\[
N_e = 18 \times N = 18 \times 1.806 \times 10^{23} = 3.2508 \times 10^{24} \approx 3.25 \times 10^{24}
\]

- **[B1]** Multiplies total atoms by 18 to give $3.25 \times 10^{24}$ electrons

---

### Worked Example 2: Molecular leak rate and duration of gas escape

A rigid container filled with helium gas ($\mathrm{He}$, molar mass $4.00\,\mathrm{g\,mol^{-1}}$) has a micro-defect in its valve. Helium atoms escape into the surrounding vacuum at a steady rate of $2.50 \times 10^{18}\,\mathrm{s^{-1}}$.

Over an observation period of $8.00\,\mathrm{hours}$, determine:
1. the total number of helium atoms that have escaped;
2. the amount of helium gas lost, in moles;
3. the decrease in the mass of the container, in grams.

#### Solution and Cambridge mark scheme

##### Part 1: Total number of escaped atoms

First, convert the time from hours to seconds:
\[
\Delta t = 8.00\,\mathrm{h} \times 3600\,\mathrm{s\,h^{-1}} = 28\,800\,\mathrm{s}
\]

The total number of atoms escaped $\Delta N$ is:
\[
\Delta N = \text{rate} \times \Delta t = 2.50 \times 10^{18}\,\mathrm{s^{-1}} \times 28\,800\,\mathrm{s} = 7.20 \times 10^{22}
\]

- **[C1]** Conversion of time to seconds ($28\,800\,\mathrm{s}$) and multiplication by escape rate
- **[A1]** $\Delta N = 7.20 \times 10^{22}$ atoms

##### Part 2: Amount of helium gas lost in moles

Use $n = \frac{N}{N_A}$:
\[
\Delta n = \frac{\Delta N}{N_A} = \frac{7.20 \times 10^{22}}{6.02 \times 10^{23}\,\mathrm{mol^{-1}}} = 0.11960\,\mathrm{mol} \approx 0.120\,\mathrm{mol}
\]

- **[C1]** Division of $\Delta N$ by $N_A$ ($6.02 \times 10^{23}$)
- **[A1]** $\Delta n = 0.120\,\mathrm{mol}$ (or $0.1196\,\mathrm{mol}$)

##### Part 3: Decrease in container mass

Use $\Delta m = \Delta n \times M$:
\[
\Delta m = 0.11960\,\mathrm{mol} \times 4.00\,\mathrm{g\,mol^{-1}} = 0.4784\,\mathrm{g} \approx 0.478\,\mathrm{g}
\]

Alternatively, using the mass of a single atom:
\[
m_{\mathrm{atom}} = \frac{4.00 \times 10^{-3}\,\mathrm{kg\,mol^{-1}}}{6.02 \times 10^{23}\,\mathrm{mol^{-1}}} = 6.645 \times 10^{-27}\,\mathrm{kg}
\]
\[
\Delta m = 7.20 \times 10^{22} \times 6.645 \times 10^{-27}\,\mathrm{kg} = 4.784 \times 10^{-4}\,\mathrm{kg} = 0.478\,\mathrm{g}
\]

- **[C1]** Multiplication of moles lost by molar mass, or atoms lost by single atom mass
- **[A1]** $\Delta m = 0.478\,\mathrm{g}$ (or $4.78 \times 10^{-4}\,\mathrm{kg}$)

---

### Worked Example 3: Estimating atom mass, number density, and interatomic spacing

Liquid mercury has a density of $\rho = 1.36 \times 10^4\,\mathrm{kg\,m^{-3}}$ and a molar mass of $M = 0.201\,\mathrm{kg\,mol^{-1}}$ ($201\,\mathrm{g\,mol^{-1}}$).

1. Calculate the mass of one mercury atom.
2. Determine the number of mercury atoms present in a volume of $1.00 \times 10^{-6}\,\mathrm{m^3}$ ($1.00\,\mathrm{cm^3}$).
3. Assuming each atom occupies a cube of side $d$, estimate the average interatomic spacing $d$.

#### Solution and Cambridge mark scheme

##### Part 1: Mass of one mercury atom

Use $m_{\mathrm{atom}} = \frac{M}{N_A}$:
\[
m_{\mathrm{atom}} = \frac{0.201\,\mathrm{kg\,mol^{-1}}}{6.02 \times 10^{23}\,\mathrm{mol^{-1}}} = 3.3389 \times 10^{-25}\,\mathrm{kg} \approx 3.34 \times 10^{-25}\,\mathrm{kg}
\]

- **[C1]** Substitution into $m_{\mathrm{atom}} = \frac{M}{N_A}$ with $M$ in $\mathrm{kg\,mol^{-1}}$
- **[A1]** $m_{\mathrm{atom}} = 3.34 \times 10^{-25}\,\mathrm{kg}$

##### Part 2: Number of atoms in $1.00 \times 10^{-6}\,\mathrm{m^3}$

First find the mass of this volume using $m = \rho V$:
\[
m = 1.36 \times 10^4\,\mathrm{kg\,m^{-3}} \times 1.00 \times 10^{-6}\,\mathrm{m^3} = 0.0136\,\mathrm{kg}
\]

The number of atoms is:
\[
N = \frac{m}{m_{\mathrm{atom}}} = \frac{0.0136\,\mathrm{kg}}{3.3389 \times 10^{-25}\,\mathrm{kg}} = 4.073 \times 10^{22} \approx 4.07 \times 10^{22}
\]
(Or find moles first: $n = \frac{0.0136\,\mathrm{kg}}{0.201\,\mathrm{kg\,mol^{-1}}} = 0.06766\,\mathrm{mol}$, then $N = n N_A = 0.06766 \times 6.02 \times 10^{23} = 4.07 \times 10^{22}$.)

- **[C1]** Calculation of sample mass ($0.0136\,\mathrm{kg}$) and division by atom mass, or calculation of moles
- **[A1]** $N = 4.07 \times 10^{22}$ atoms

##### Part 3: Average interatomic spacing $d$

The volume occupied by each atom is:
\[
V_{\mathrm{atom}} = \frac{V}{N} = \frac{1.00 \times 10^{-6}\,\mathrm{m^3}}{4.073 \times 10^{22}} = 2.455 \times 10^{-29}\,\mathrm{m^3}
\]

If each atom occupies a cube of side $d$, then $V_{\mathrm{atom}} = d^3$:
\[
d = (V_{\mathrm{atom}})^{1/3} = (2.455 \times 10^{-29}\,\mathrm{m^3})^{1/3} = 2.906 \times 10^{-10}\,\mathrm{m} \approx 2.91 \times 10^{-10}\,\mathrm{m}
\]

- **[C1]** Determination of volume per atom: $\frac{V}{N}$ (or $\frac{m_{\mathrm{atom}}}{\rho}$)
- **[A1]** $d = 2.91 \times 10^{-10}\,\mathrm{m}$ (or $0.291\,\mathrm{nm}$)

---

## Guided practice

Now test your understanding with this scaffolded problem. Work through each step on paper before revealing the solution.

### Problem

A cylinder stores $4.80\,\mathrm{kg}$ of pure methane gas ($\mathrm{CH_4}$). The molar mass of methane is $16.0\,\mathrm{g\,mol^{-1}}$ ($0.0160\,\mathrm{kg\,mol^{-1}}$).

1. Calculate the amount of methane gas in the cylinder, in moles.
2. Calculate the total number of methane molecules in the cylinder.
3. Calculate the total number of hydrogen atoms in the cylinder.
4. Calculate the mass of a single methane molecule in kilograms.

### Step-by-step guidance

- **Step 1:** Use $n = \frac{m}{M}$. Ensure both masses share the same unit prefix (either both in grams or both in kilograms).
  \[
  n = \frac{4800\,\mathrm{g}}{16.0\,\mathrm{g\,mol^{-1}}} = 300\,\mathrm{mol}
  \]
- **Step 2:** Multiply the amount in moles by the Avogadro constant $N_A$:
  \[
  N_{\mathrm{molecules}} = 300\,\mathrm{mol} \times 6.02 \times 10^{23}\,\mathrm{mol^{-1}} = 1.806 \times 10^{26} \approx 1.81 \times 10^{26}
  \]
- **Step 3:** Inspect the chemical formula $\mathrm{CH_4}$. Each molecule contains 4 hydrogen atoms. Therefore, multiply the molecular count by 4:
  \[
  N_{\mathrm{H}} = 4 \times 1.806 \times 10^{26} = 7.224 \times 10^{26} \approx 7.22 \times 10^{26}
  \]
- **Step 4:** Divide the molar mass in kilograms by the Avogadro constant:
  \[
  m_{\mathrm{molecule}} = \frac{0.0160\,\mathrm{kg\,mol^{-1}}}{6.02 \times 10^{23}\,\mathrm{mol^{-1}}} = 2.658 \times 10^{-26}\,\mathrm{kg} \approx 2.66 \times 10^{-26}\,\mathrm{kg}
  \]

---

## Active learning checks

### Check 1: Comparing amounts of substance for equal masses

Sample X contains $10.0\,\mathrm{g}$ of helium gas ($\mathrm{He}$, molar mass $4.00\,\mathrm{g\,mol^{-1}}$). Sample Y contains $10.0\,\mathrm{g}$ of neon gas ($\mathrm{Ne}$, molar mass $20.2\,\mathrm{g\,mol^{-1}}$). Both are monatomic gases.

Which sample contains more atoms?

- **A.** Sample X (helium), because helium atoms have less mass each, so more atoms are required to make up $10.0\,\mathrm{g}$.
- **B.** Both samples contain the same number of atoms, because both samples have an identical mass of $10.0\,\mathrm{g}$.

**Feedback for A:** Correct. Amount of substance is $n = \frac{m}{M}$. For helium, $n = \frac{10.0\,\mathrm{g}}{4.00\,\mathrm{g\,mol^{-1}}} = 2.50\,\mathrm{mol}$, giving $N = 2.50 \times 6.02 \times 10^{23} = 1.51 \times 10^{24}$ atoms. For neon, $n = \frac{10.0\,\mathrm{g}}{20.2\,\mathrm{g\,mol^{-1}}} = 0.495\,\mathrm{mol}$, giving $N = 2.98 \times 10^{23}$ atoms. Equal mass does not mean equal number of particles when the constituent particles have different masses.

**Feedback for B:** Incorrect. Equal mass means the two samples resist acceleration equally, but because neon atoms are roughly 5 times heavier than helium atoms, the neon sample consists of roughly one-fifth as many atoms.

---

### Check 2: Elementary entities in diatomic gases

A sealed glass flask contains exactly $1.00\,\mathrm{mol}$ of chlorine gas, $\mathrm{Cl_2}$.

What is the total number of chlorine atoms present in the flask?

- **A.** $1.20 \times 10^{24}$ atoms
- **B.** $6.02 \times 10^{23}$ atoms

**Feedback for A:** Correct. One mole of chlorine gas consists of $1.00 \times N_A = 6.02 \times 10^{23}$ chlorine molecules ($\mathrm{Cl_2}$). Because each molecule is diatomic (contains two atoms), the total number of chlorine atoms is $2 \times 6.02 \times 10^{23} = 1.20 \times 10^{24}$ atoms.

**Feedback for B:** Incorrect. $6.02 \times 10^{23}$ is the number of chlorine molecules ($\mathrm{Cl_2}$), not atoms. Always check whether the question asks for molecules or individual constituent atoms.

---

### Check 3: Calculation of single particle mass

Krypton gas has a molar mass of $83.8\,\mathrm{g\,mol^{-1}}$. What is the mass of one single krypton atom in kilograms?

- **A.** $1.39 \times 10^{-25}\,\mathrm{kg}$
- **B.** $1.39 \times 10^{-22}\,\mathrm{kg}$

**Feedback for A:** Correct. First convert the molar mass to kilograms per mole: $M = 83.8 \times 10^{-3}\,\mathrm{kg\,mol^{-1}} = 0.0838\,\mathrm{kg\,mol^{-1}}$. Then divide by the Avogadro constant: $m_{\mathrm{atom}} = \frac{0.0838\,\mathrm{kg\,mol^{-1}}}{6.02 \times 10^{23}\,\mathrm{mol^{-1}}} = 1.392 \times 10^{-25}\,\mathrm{kg}$.

**Feedback for B:** Incorrect. This result comes from dividing $83.8$ directly by $6.02 \times 10^{23}$, which leaves the mass in grams ($1.39 \times 10^{-22}\,\mathrm{g}$). In SI units, mass must be expressed in kilograms ($\mathrm{kg}$), which requires dividing by an additional factor of $1000$.

---

### Check 4: Rate of molecular leak

A microscopic container of xenon gas is leaking at a constant rate of $3.01 \times 10^{17}\,\text{atoms per second}$.

How long does it take for $0.0500\,\mathrm{mol}$ of xenon gas to escape?

- **A.** $1.00 \times 10^5\,\mathrm{s}$
- **B.** $1.66 \times 10^{-19}\,\mathrm{s}$

**Feedback for A:** Correct. First find the total number of atoms in $0.0500\,\mathrm{mol}$: $N = n N_A = 0.0500\,\mathrm{mol} \times 6.02 \times 10^{23}\,\mathrm{mol^{-1}} = 3.01 \times 10^{22}$ atoms. Then divide by the escape rate: $t = \frac{3.01 \times 10^{22}}{3.01 \times 10^{17}\,\mathrm{s^{-1}}} = 1.00 \times 10^5\,\mathrm{s}$ (approximately 27.8 hours).

**Feedback for B:** Incorrect. You divided the amount of substance in moles ($0.0500$) directly by the escape rate in atoms per second ($3.01 \times 10^{17}$), without converting moles into number of atoms using $N_A$. The units of that division are $\mathrm{mol\,s}$, not seconds.

---

## Mistakes worth repairing

### Mistake 1: Confusing amount of substance ($n$) with mass ($m$) or volume ($V$)
In colloquial language, people often say "an amount of water" to mean its mass or volume. In physics, **amount of substance** is a technical term with a strict definition: it refers solely to the number of elementary entities measured in moles ($n = \frac{N}{N_A}$). Two samples with the same volume or mass do not generally contain the same amount of substance.

### Mistake 2: Failing to identify the elementary entity being counted
Stating that a container holds "$1\,\mathrm{mol}$ of chlorine" is ambiguous. You must specify whether you mean $1\,\mathrm{mol}$ of chlorine molecules ($\mathrm{Cl_2}$) or $1\,\mathrm{mol}$ of chlorine atoms ($\mathrm{Cl}$). For a diatomic gas, the number of atoms is twice the number of molecules. Always check the entity named in the examination question.

### Mistake 3: Forgetting the $10^{-3}$ conversion for molar mass in physics
Chemistry periodic tables quote molar masses in grams per mole ($\mathrm{g\,mol^{-1}}$). In physics calculations involving force, momentum, speed, and energy, all quantities must be in SI base units. Always convert $\mathrm{g\,mol^{-1}}$ to $\mathrm{kg\,mol^{-1}}$ by multiplying by $10^{-3}$. A molar mass of $32.0\,\mathrm{g\,mol^{-1}}$ must be entered as $32.0 \times 10^{-3}\,\mathrm{kg\,mol^{-1}}$ or $0.0320\,\mathrm{kg\,mol^{-1}}$.

### Mistake 4: Treating the Avogadro constant as a pure number without units
While $N_A$ represents a count, it is defined physically as the number of entities per unit amount of substance. Its SI unit is **$\mathrm{mol^{-1}}$**. Writing $N_A$ without units or treating it as a dimensionless scalar obscures dimensional analysis when deriving relations such as $k = \frac{R}{N_A}$.

### Mistake 5: Assuming one mole of any substance occupies the same volume
Under standard temperature and pressure, one mole of an ideal gas occupies approximately $22.4\,\mathrm{dm^3}$ (or $24.0\,\mathrm{dm^3}$ at room temperature). However, one mole of liquid water occupies only $18\,\mathrm{cm^3}$, and one mole of solid gold occupies only $10.2\,\mathrm{cm^3}$. The mole measures number of particles, not volume.

---

## Core recap

- **Amount of substance** is an SI base quantity with the base unit **mole** (symbol: **$\mathrm{mol}$**).
- The **Avogadro constant** $N_A$ is defined as the number of atoms in $12\,\mathrm{g}$ of carbon-12. Its value is $N_A = 6.02 \times 10^{23}\,\mathrm{mol^{-1}}$.
- One **mole** is the amount of substance containing the same number of elementary entities as there are atoms in $12\,\mathrm{g}$ of carbon-12 (that is, $N_A$ particles).
- The elementary entity (atom, molecule, ion, electron) must always be explicitly stated.
- Number of particles $N$ and amount of substance $n$ are linked by:
  \[
  N = n N_A \quad \Longleftrightarrow \quad n = \frac{N}{N_A}
  \]
- Total mass $m$, amount of substance $n$, and molar mass $M$ are related by:
  \[
  m = n M \quad \Longleftrightarrow \quad n = \frac{m}{M}
  \]
  where $M$ is in $\mathrm{kg\,mol^{-1}}$ for SI consistency.
- The mass of an individual particle is:
  \[
  m_{\mathrm{particle}} = \frac{M}{N_A} = \frac{m}{N}
  \]
