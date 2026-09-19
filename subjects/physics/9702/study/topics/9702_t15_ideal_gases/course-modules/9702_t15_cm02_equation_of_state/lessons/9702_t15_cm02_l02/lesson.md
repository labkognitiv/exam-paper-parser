# Ideal gas definition, equation of state pV = nRT and pV = NkT, and thermodynamic temperature

## The macroscopic behavior of gases: pressure, volume, and temperature

When you inflate a bicycle tyre on a cold morning, you notice several interconnected physical changes:
- As you pump more air into the tyre, the internal pressure rises.
- If you leave the bicycle in direct summer sunlight, the temperature of the trapped air increases, and the tyre feels significantly firmer because the pressure inside has climbed.
- If you squeeze a sealed party balloon, reducing its volume, the pressure of the air inside increases immediately.

In the previous lesson, you saw that a gas consists of vast numbers of particles whose amount is quantified in moles ($n$) or direct counts ($N$). To predict how a trapped gas behaves, physics links its macroscopic state variables: **pressure** ($p$), **volume** ($V$), and **temperature** ($T$).

This lesson investigates the mathematical laws that connect these variables, establishes the absolute scale of temperature, defines the model known as an **ideal gas**, and develops the two equivalent forms of the **equation of state**: the molar form $pV = nRT$ and the molecular form $pV = NkT$.

---

## The thermodynamic temperature scale

Before writing any gas equation, we must establish how temperature is measured.

Everyday thermometers use empirical scales, such as the Celsius scale ($^\circ\mathrm{C}$), which rely on the arbitrary properties of a specific thermometric substance (the freezing and boiling points of pure water at standard atmospheric pressure).

Physics requires an absolute scale of temperature that is independent of the properties of any particular substance. This scale is the **thermodynamic temperature scale** (also called the Kelvin scale).

### Absolute zero

Experiments with gases at constant volume reveal that as temperature drops, gas pressure decreases linearly. If you extrapolate this linear graph backward, the pressure reaches zero at exactly:

\[
-273.15\,^\circ\mathrm{C}
\]

This lowest possible theoretical temperature is called **absolute zero**:
- At absolute zero ($0\,\mathrm{K}$), a system has minimum internal energy.
- On the thermodynamic scale, temperature cannot be negative: $0\,\mathrm{K}$ is the absolute floor.

### Conversion between Celsius and thermodynamic temperature

The SI base unit of thermodynamic temperature is the **kelvin**, symbol **$\mathrm{K}$**. A temperature interval of $1\,\mathrm{K}$ is identical in size to an interval of $1\,^\circ\mathrm{C}$.

The conversion between the Celsius temperature $\theta$ (in $^\circ\mathrm{C}$) and thermodynamic temperature $T$ (in $\mathrm{K}$) is:

\[
T\,(\mathrm{K}) = \theta\,(^\circ\mathrm{C}) + 273.15
\]

In many Cambridge examination calculations, rounding to the nearest integer is accepted:

\[
T\,(\mathrm{K}) \approx \theta\,(^\circ\mathrm{C}) + 273
\]

For example:
- Ice point ($0\,^\circ\mathrm{C}$): $T = 0 + 273.15 = 273.15\,\mathrm{K} \approx 273\,\mathrm{K}$.
- Room temperature ($20\,^\circ\mathrm{C}$): $T = 20 + 273 = 293\,\mathrm{K}$.
- Steam point ($100\,^\circ\mathrm{C}$): $T = 100 + 273.15 = 373.15\,\mathrm{K} \approx 373\,\mathrm{K}$.

> **Critical examination rule:** In all ideal gas equations, you must **always** substitute thermodynamic temperature $T$ in kelvin. Substituting temperature in degrees Celsius produces entirely incorrect results and loses method marks!

---

## Definition of an ideal gas

Real gases (such as air, nitrogen, helium, and carbon dioxide) behave in complex ways because their molecules attract one another and occupy physical volume. To understand gas behavior clearly, physicists create a theoretical model: the **ideal gas**.

<a id="definition-9702_def_ideal_gas"></a>

> **Definition to learn: ideal gas.** a gas that obeys the equation of state pV = nRT at all pressures, volumes and thermodynamic temperatures

In Cambridge marking schemes, the following equivalent definitions are also fully accepted:
- *a gas that obeys $pV \propto T$, where $T$ is the thermodynamic temperature, for all values of $p, V,$ and $T$*;
- *a gas that obeys the relationship $\frac{pV}{T} = \text{constant}$ at all pressures, volumes, and thermodynamic temperatures*.

### When do real gases behave like an ideal gas?

No real gas is perfectly ideal under all conditions. However, real gases approximate ideal gas behavior very closely under two specific conditions:

1. **Low pressure:** When the pressure is low, the gas molecules are spaced very far apart. The volume occupied by the molecules themselves is negligible compared to the total volume of the container.
2. **High temperature:** When the temperature is high (well above the gas's condensation point), the molecules move with large kinetic energies. During collisions and near encounters, the intermolecular attractive forces are negligible compared to the kinetic energies of the particles.

### When do real gases deviate from ideal behavior?

A real gas deviates noticeably from an ideal gas when:
- **Pressure is very high:** The molecules are compressed close together. The physical volume occupied by the molecules can no longer be ignored compared to the volume of the container.
- **Temperature is very low:** The molecules move slowly. Intermolecular forces of attraction pull molecules toward one another, reducing the force of impacts on the container walls (lowering the observed pressure), and eventually causing the gas to liquefy. An ideal gas never liquefies because it has zero intermolecular forces.

---

## Empirical gas laws leading to the equation of state

Historically, the ideal gas equation was synthesized from three separate empirical gas laws established for a fixed mass of gas:

### 1. Boyle's law (constant temperature, constant $n$)

For a fixed mass of gas at constant temperature, pressure is inversely proportional to volume:

\[
p \propto \frac{1}{V} \quad \Longleftrightarrow \quad pV = \text{constant}
\]

If a gas changes from state 1 to state 2 at constant temperature:
\[
p_1 V_1 = p_2 V_2
\]

### 2. Charles's law (constant pressure, constant $n$)

For a fixed mass of gas at constant pressure, volume is directly proportional to thermodynamic temperature:

\[
V \propto T \quad \Longleftrightarrow \quad \frac{V}{T} = \text{constant}
\]

If a gas is heated or cooled at constant pressure:
\[
\frac{V_1}{T_1} = \frac{V_2}{T_2}
\]

### 3. Gay-Lussac's law / Pressure law (constant volume, constant $n$)

For a fixed mass of gas at constant volume, pressure is directly proportional to thermodynamic temperature:

\[
p \propto T \quad \Longleftrightarrow \quad \frac{p}{T} = \text{constant}
\]

If a rigid container of gas is heated or cooled:
\[
\frac{p_1}{T_1} = \frac{p_2}{T_2}
\]

### 4. The combined gas equation

Combining these three proportionalities shows that for a fixed mass of gas:

\[
\frac{pV}{T} = \text{constant}
\]

which leads to the working formula for changes of state:

\[
\frac{p_1 V_1}{T_1} = \frac{p_2 V_2}{T_2}
\]

---

## The ideal gas equation: molar form ($pV = nRT$)

When the amount of substance $n$ is included, the constant in $\frac{pV}{T} = \text{constant}$ is directly proportional to $n$:

<a id="formula-9702_formula_ideal_gas_equation_moles"></a>

> **Formula to learn: ideal gas equation (molar form).**
>
> \[
> pV = nRT
> \]

### Meaning and units of each term

Let us inspect each quantity and its required SI units:
- **$p$** is the **pressure** of the gas in pascals ($\mathrm{Pa}$, where $1\,\mathrm{Pa} = 1\,\mathrm{N\,m^{-2}}$). If pressure is quoted in kilopascals ($\mathrm{kPa}$) or megapascals ($\mathrm{MPa}$), convert:
  \[
  1\,\mathrm{kPa} = 1 \times 10^3\,\mathrm{Pa}, \quad 1\,\mathrm{MPa} = 1 \times 10^6\,\mathrm{Pa}
  \]
- **$V$** is the **volume** of the container in cubic metres ($\mathrm{m^3}$). Volume unit conversions are a frequent source of errors:
  \[
  1\,\mathrm{cm^3} = (10^{-2}\,\mathrm{m})^3 = 10^{-6}\,\mathrm{m^3}
  \]
  \[
  1\,\mathrm{dm^3} = 1\,\text{litre} = (10^{-1}\,\mathrm{m})^3 = 10^{-3}\,\mathrm{m^3}
  \]
- **$n$** is the **amount of substance** in moles ($\mathrm{mol}$).
- **$R$** is the **molar gas constant**. Its value is given on the Cambridge data sheet as:
  \[
  R = 8.31\,\mathrm{J\,K^{-1}\,mol^{-1}}
  \]
  $R$ is a universal constant: it has the same value for every ideal gas, regardless of chemical composition.
- **$T$** is the **thermodynamic temperature** in kelvin ($\mathrm{K}$).

---

## The ideal gas equation: molecular form ($pV = NkT$)

In many physics problems, we want to relate pressure and volume directly to the microscopic number of molecules $N$, rather than the macroscopic number of moles $n$.

From the previous lesson, the number of moles $n$ and the number of molecules $N$ are linked by:

\[
n = \frac{N}{N_A}
\]

Substitute this into $pV = nRT$:

\[
pV = \left(\frac{N}{N_A}\right)RT = N\left(\frac{R}{N_A}\right)T
\]

Notice the group of constants in parentheses: $\frac{R}{N_A}$.

Both $R$ (the gas constant per mole) and $N_A$ (the number of particles per mole) are universal physical constants. Their quotient is therefore also a universal physical constant: the **Boltzmann constant**, denoted $k$.

### The Boltzmann constant $k$

\[
k = \frac{R}{N_A}
\]

Using the values from the Cambridge data sheet:
\[
k = \frac{8.31\,\mathrm{J\,K^{-1}\,mol^{-1}}}{6.02 \times 10^{23}\,\mathrm{mol^{-1}}} = 1.3804 \times 10^{-23}\,\mathrm{J\,K^{-1}} \approx 1.38 \times 10^{-23}\,\mathrm{J\,K^{-1}}
\]

Physical interpretation:
- **$R$** is the molar gas constant: the gas constant **per mole**.
- **$k$** is the Boltzmann constant: the gas constant **per molecule**.

### The molecular equation of state

Substituting $k = \frac{R}{N_A}$ into the equation gives:

<a id="formula-9702_formula_ideal_gas_equation_molecules"></a>

> **Formula to learn: ideal gas equation (molecular form).**
>
> \[
> pV = NkT
> \]

Where:
- **$p$** is pressure in pascals ($\mathrm{Pa}$);
- **$V$** is volume in cubic metres ($\mathrm{m^3}$);
- **$N$** is the total number of gas molecules (dimensionless integer);
- **$k$** is the Boltzmann constant ($1.38 \times 10^{-23}\,\mathrm{J\,K^{-1}}$);
- **$T$** is thermodynamic temperature in kelvin ($\mathrm{K}$).

Both equations, $pV = nRT$ and $pV = NkT$, represent the identical physical law. Use $pV = nRT$ when working with moles or molar masses; use $pV = NkT$ when working directly with particle populations.

---

## Graphical representations of ideal gas relationships

Cambridge examinations regularly test your ability to sketch and interpret graphs representing the gas laws:

### 1. Pressure against volume ($p-V$ isotherms)
- At constant temperature, $pV = \text{constant}$, giving an inverse curve (a rectangular hyperbola).
- For higher temperatures, the curve shifts outward and upward, further from the axes.

### 2. Product $pV$ against pressure $p$
- For an ideal gas at constant temperature, the product $pV$ is constant regardless of pressure.
- A plot of $pV$ on the vertical axis against $p$ on the horizontal axis is a **horizontal straight line**.
- The height of the line above the horizontal axis is proportional to the thermodynamic temperature $T$ ($pV = nRT$).

### 3. Volume against thermodynamic temperature ($V-T$)
- At constant pressure, $V \propto T$.
- A plot of $V$ against $T$ (in $\mathrm{K}$) is a **straight line passing directly through the origin** $(0, 0)$.
- If volume is plotted against temperature in degrees Celsius $\theta$, the line is straight but intercepts the horizontal axis at $\theta = -273.15\,^\circ\mathrm{C}$.

### 4. Pressure against thermodynamic temperature ($p-T$)
- At constant volume, $p \propto T$.
- A plot of $p$ against $T$ (in $\mathrm{K}$) is a **straight line passing directly through the origin** $(0, 0)$.
- If extrapolated backward, the pressure reaches zero at absolute zero ($0\,\mathrm{K}$).

---

## Worked examples

### Worked Example 1: State parameters, moles, and isochoric heating

A rigid, sealed steel canister has an internal volume of $4.50 \times 10^3\,\mathrm{cm^3}$. It contains an ideal gas at a pressure of $3.20 \times 10^5\,\mathrm{Pa}$ and a temperature of $27.0\,^\circ\mathrm{C}$.

Calculate:
1. the thermodynamic temperature of the gas, in kelvin;
2. the amount of gas inside the canister, in moles;
3. the new temperature of the gas, in degrees Celsius, when it is heated until the pressure reaches $4.80 \times 10^5\,\mathrm{Pa}$.

#### Solution and Cambridge mark scheme

##### Part 1: Thermodynamic temperature

Convert the Celsius temperature to kelvin:
\[
T_1 = 27.0 + 273.15 = 300.15\,\mathrm{K} \approx 300\,\mathrm{K}
\]

- **[B1]** Correct conversion to kelvin: $T = 300\,\mathrm{K}$ (or $300.15\,\mathrm{K}$)

##### Part 2: Amount of gas in moles

First convert the volume from $\mathrm{cm^3}$ to $\mathrm{m^3}$:
\[
V = 4.50 \times 10^3 \times 10^{-6}\,\mathrm{m^3} = 4.50 \times 10^{-3}\,\mathrm{m^3}
\]

Rearrange $pV = nRT$ for $n$:
\[
n = \frac{pV}{RT} = \frac{3.20 \times 10^5\,\mathrm{Pa} \times 4.50 \times 10^{-3}\,\mathrm{m^3}}{8.31\,\mathrm{J\,K^{-1}\,mol^{-1}} \times 300\,\mathrm{K}}
\]
\[
n = \frac{1440}{2493} = 0.5776\,\mathrm{mol} \approx 0.578\,\mathrm{mol}
\]

- **[C1]** Correct volume conversion ($4.50 \times 10^{-3}\,\mathrm{m^3}$) and substitution into $pV = nRT$
- **[A1]** Amount of gas $n = 0.578\,\mathrm{mol}$ (or $0.58\,\mathrm{mol}$)

##### Part 3: Final temperature in degrees Celsius

Because the canister is rigid and sealed, volume $V$ and amount $n$ are constant. Apply Gay-Lussac's law:
\[
\frac{p_1}{T_1} = \frac{p_2}{T_2} \quad \implies \quad T_2 = T_1 \left(\frac{p_2}{p_1}\right)
\]
\[
T_2 = 300\,\mathrm{K} \times \left(\frac{4.80 \times 10^5\,\mathrm{Pa}}{3.20 \times 10^5\,\mathrm{Pa}}\right) = 300 \times 1.50 = 450\,\mathrm{K}
\]

Now convert the final thermodynamic temperature back to degrees Celsius:
\[
\theta_2 = T_2 - 273.15 = 450 - 273.15 = 176.85\,^\circ\mathrm{C} \approx 177\,^\circ\mathrm{C}
\]

- **[C1]** Use of $\frac{p_1}{T_1} = \frac{p_2}{T_2}$ to find $T_2 = 450\,\mathrm{K}$
- **[A1]** $\theta_2 = 177\,^\circ\mathrm{C}$ (or $176.9\,^\circ\mathrm{C}$)

---

### Worked Example 2: Molecular calculations and molecular mass from $pV = NkT$

A sealed research chamber of volume $0.850\,\mathrm{m^3}$ contains a gas sample of total mass $0.0580\,\mathrm{kg}$ at a pressure of $1.15 \times 10^5\,\mathrm{Pa}$ and a temperature of $147\,^\circ\mathrm{C}$.

Assuming the gas behaves as an ideal gas, calculate:
1. the number $N$ of molecules in the chamber;
2. the mass of a single molecule of the gas;
3. the molar mass $M$ of the gas in $\mathrm{g\,mol^{-1}}$.

#### Solution and Cambridge mark scheme

##### Part 1: Number of molecules $N$

Convert the temperature to kelvin:
\[
T = 147 + 273 = 420\,\mathrm{K}
\]

Use the molecular form of the equation of state, $pV = NkT$:
\[
N = \frac{pV}{kT} = \frac{1.15 \times 10^5\,\mathrm{Pa} \times 0.850\,\mathrm{m^3}}{1.38 \times 10^{-23}\,\mathrm{J\,K^{-1}} \times 420\,\mathrm{K}}
\]
\[
N = \frac{9.775 \times 10^4}{5.796 \times 10^{-21}} = 1.6865 \times 10^{25} \approx 1.69 \times 10^{25}
\]

- **[C1]** Temperature in kelvin ($420\,\mathrm{K}$) and formula $pV = NkT$ (or $pV = nRT$ with $N = nN_A$)
- **[A1]** Number of molecules $N = 1.69 \times 10^{25}$

##### Part 2: Mass of a single molecule

The total mass of the gas is $m_{\mathrm{total}} = 0.0580\,\mathrm{kg}$. The mass of one molecule $m$ is:
\[
m = \frac{m_{\mathrm{total}}}{N} = \frac{0.0580\,\mathrm{kg}}{1.6865 \times 10^{25}} = 3.439 \times 10^{-26}\,\mathrm{kg} \approx 3.44 \times 10^{-26}\,\mathrm{kg}
\]

- **[C1]** Division of total mass by calculated number of molecules
- **[A1]** Mass of one molecule $m = 3.44 \times 10^{-26}\,\mathrm{kg}$

##### Part 3: Molar mass of the gas in $\mathrm{g\,mol^{-1}}$

Multiply the single molecule mass by the Avogadro constant:
\[
M = m \times N_A = 3.439 \times 10^{-26}\,\mathrm{kg} \times 6.02 \times 10^{23}\,\mathrm{mol^{-1}} = 0.02070\,\mathrm{kg\,mol^{-1}}
\]
Convert to grams per mole:
\[
M = 0.02070 \times 10^3\,\mathrm{g\,mol^{-1}} = 20.7\,\mathrm{g\,mol^{-1}}
\]
(Note: this identifies the gas as neon, which has an atomic mass of $20.2\,\mathrm{g\,mol^{-1}}$.)

- **[B1]** Molar mass $M = 20.7\,\mathrm{g\,mol^{-1}}$ (or $0.0207\,\mathrm{kg\,mol^{-1}}$)

---

### Worked Example 3: Changing states with molecular gas escape

A high-pressure gas cylinder of volume $0.0250\,\mathrm{m^3}$ initially contains an ideal gas at a pressure of $6.00 \times 10^6\,\mathrm{Pa}$ at room temperature ($295\,\mathrm{K}$).

1. Show that the initial amount of gas in the cylinder is approximately $61.2\,\mathrm{mol}$.
2. A valve is opened and gas escapes into a container at a steady rate of $4.20 \times 10^{20}\,\text{molecules per second}$ for a time period of $5.00\,\mathrm{hours}$. The cylinder is kept at a constant temperature of $295\,\mathrm{K}$.
   Calculate:
   (i) the amount of gas lost from the cylinder, in moles;
   (ii) the final pressure of the gas remaining in the cylinder.

#### Solution and Cambridge mark scheme

##### Part 1: Initial amount of gas

Use $pV = nRT$:
\[
n_1 = \frac{p_1 V}{R T} = \frac{6.00 \times 10^6\,\mathrm{Pa} \times 0.0250\,\mathrm{m^3}}{8.31\,\mathrm{J\,K^{-1}\,mol^{-1}} \times 295\,\mathrm{K}} = \frac{150\,000}{2451.45} = 61.188\,\mathrm{mol} \approx 61.2\,\mathrm{mol}
\]

- **[M1]** Rearrangement $n = \frac{pV}{RT}$ and substitution of all initial values
- **[A1]** Correct evaluation showing $n_1 = 61.2\,\mathrm{mol}$

##### Part 2(i): Amount of gas lost in moles

Convert the time to seconds:
\[
\Delta t = 5.00\,\mathrm{h} \times 3600\,\mathrm{s\,h^{-1}} = 18\,000\,\mathrm{s}
\]
Calculate the total number of escaped molecules $\Delta N$:
\[
\Delta N = 4.20 \times 10^{20}\,\mathrm{s^{-1}} \times 18\,000\,\mathrm{s} = 7.56 \times 10^{24}\,\text{molecules}
\]
Convert the escaped count into moles:
\[
\Delta n = \frac{\Delta N}{N_A} = \frac{7.56 \times 10^{24}}{6.02 \times 10^{23}\,\mathrm{mol^{-1}}} = 12.558\,\mathrm{mol} \approx 12.6\,\mathrm{mol}
\]

- **[C1]** Calculation of escaped molecules: $4.20 \times 10^{20} \times 18\,000 = 7.56 \times 10^{24}$
- **[A1]** $\Delta n = \frac{7.56 \times 10^{24}}{6.02 \times 10^{23}} = 12.6\,\mathrm{mol}$

##### Part 2(ii): Final pressure of remaining gas

The amount of gas remaining in the cylinder is:
\[
n_2 = n_1 - \Delta n = 61.188\,\mathrm{mol} - 12.558\,\mathrm{mol} = 48.630\,\mathrm{mol}
\]
Calculate the new pressure $p_2$ using $p_2 = \frac{n_2 R T}{V}$:
\[
p_2 = \frac{48.630\,\mathrm{mol} \times 8.31\,\mathrm{J\,K^{-1}\,mol^{-1}} \times 295\,\mathrm{K}}{0.0250\,\mathrm{m^3}} = \frac{1.192 \times 10^5}{0.0250} = 4.7686 \times 10^6\,\mathrm{Pa} \approx 4.77 \times 10^6\,\mathrm{Pa}
\]

Alternatively, because $V$ and $T$ are constant, pressure is directly proportional to amount of substance ($p \propto n$):
\[
p_2 = p_1 \left(\frac{n_2}{n_1}\right) = 6.00 \times 10^6\,\mathrm{Pa} \times \left(\frac{48.630}{61.188}\right) = 4.769 \times 10^6\,\mathrm{Pa} \approx 4.77 \times 10^6\,\mathrm{Pa}
\]

- **[C1]** Determination of remaining amount of substance: $n_2 = 61.2 - 12.6 = 48.6\,\mathrm{mol}$
- **[A1]** Final pressure $p_2 = 4.77 \times 10^6\,\mathrm{Pa}$ (or $4.77\,\mathrm{MPa}$)

---

## Guided practice

Work through this multi-step problem to consolidate your problem-solving process.

### Problem

An industrial cylinder of fixed volume $1.60 \times 10^{-2}\,\mathrm{m^3}$ stores nitrogen gas. At a temperature of $17.0\,^\circ\mathrm{C}$, the pressure inside the cylinder is $2.50 \times 10^6\,\mathrm{Pa}$.

1. Calculate the initial thermodynamic temperature $T_1$ in kelvin.
2. Use $pV = NkT$ to calculate the number of nitrogen molecules $N$ in the cylinder.
3. The cylinder is transported to a hot factory floor where its temperature rises to $47.0\,^\circ\mathrm{C}$. Assuming no gas leaks, calculate the new pressure $p_2$ inside the cylinder.

### Step-by-step guidance

- **Step 1:** Convert Celsius to kelvin:
  \[
  T_1 = 17.0 + 273.15 \approx 290\,\mathrm{K}
  \]
- **Step 2:** Rearrange $pV = NkT$ for $N$:
  \[
  N = \frac{p_1 V}{k T_1} = \frac{2.50 \times 10^6\,\mathrm{Pa} \times 1.60 \times 10^{-2}\,\mathrm{m^3}}{1.38 \times 10^{-23}\,\mathrm{J\,K^{-1}} \times 290\,\mathrm{K}} = \frac{40\,000}{4.002 \times 10^{-21}} = 9.995 \times 10^{24} \approx 1.00 \times 10^{25}
  \]
- **Step 3:** Calculate the new thermodynamic temperature:
  \[
  T_2 = 47.0 + 273 = 320\,\mathrm{K}
  \]
  Because the cylinder has a fixed volume, use the pressure law:
  \[
  p_2 = p_1 \left(\frac{T_2}{T_1}\right) = 2.50 \times 10^6\,\mathrm{Pa} \times \left(\frac{320\,\mathrm{K}}{290\,\mathrm{K}}\right) = 2.759 \times 10^6\,\mathrm{Pa} \approx 2.76 \times 10^6\,\mathrm{Pa}
  \]

---

## Active learning checks

### Check 1: Definition of ideal gas and temperature scale

Which statement correctly defines an ideal gas in Cambridge International A Level Physics?

- **A.** A gas that obeys $pV \propto T$, where $T$ is the thermodynamic temperature, for all values of pressure, volume, and temperature.
- **B.** A gas that obeys $pV \propto \theta$, where $\theta$ is the temperature in degrees Celsius, for all values of pressure, volume, and temperature.

**Feedback for A:** Correct. By definition, an ideal gas strictly obeys the equation of state $pV = nRT$ (or $pV \propto T$) at all pressures, volumes, and thermodynamic temperatures. The proportionality holds only when temperature is measured from absolute zero on the Kelvin scale.

**Feedback for B:** Incorrect. The product $pV$ is not proportional to Celsius temperature. If you double the Celsius temperature from $20\,^\circ\mathrm{C}$ to $40\,^\circ\mathrm{C}$, the thermodynamic temperature only increases from $293\,\mathrm{K}$ to $313\,\mathrm{K}$, so $pV$ only increases by approximately 7%, not 100%!

---

### Check 2: Relation between gas constants

A physics student knows that the molar gas constant is $R = 8.31\,\mathrm{J\,K^{-1}\,mol^{-1}}$. To perform calculations on individual molecules using $pV = NkT$, what is the correct formula and value for the Boltzmann constant $k$?

- **A.** $k = \frac{R}{N_A} \approx 1.38 \times 10^{-23}\,\mathrm{J\,K^{-1}}$
- **B.** $k = R \times N_A \approx 5.00 \times 10^{24}\,\mathrm{J\,K^{-1}}$

**Feedback for A:** Correct. $R$ is the gas constant per mole, and $N_A$ is the number of molecules per mole. Dividing $R$ by $N_A$ gives the gas constant per single molecule: $k = \frac{R}{N_A} = \frac{8.31}{6.02 \times 10^{23}} = 1.38 \times 10^{-23}\,\mathrm{J\,K^{-1}}$.

**Feedback for B:** Incorrect. Multiplying $R$ by $N_A$ yields an enormous number with incorrect units. The Boltzmann constant must be tiny because it represents the energy scale associated with an individual microscopic molecule.

---

### Check 3: Heating a sealed rigid container

A sealed rigid glass container of ideal gas is heated from $25\,^\circ\mathrm{C}$ to $50\,^\circ\mathrm{C}$.

What happens to the pressure of the gas?

- **A.** The pressure increases by a factor of $\frac{323}{298} \approx 1.08$ (an 8% increase).
- **B.** The pressure doubles (increases by a factor of 2.0).

**Feedback for A:** Correct. For a fixed volume of gas, pressure is proportional to thermodynamic temperature: $p \propto T$. Converting both temperatures to kelvin gives $T_1 = 25 + 273 = 298\,\mathrm{K}$ and $T_2 = 50 + 273 = 323\,\mathrm{K}$. Therefore, $\frac{p_2}{p_1} = \frac{323}{298} \approx 1.084$.

**Feedback for B:** Incorrect. This mistake comes from doubling the Celsius temperature ($50 / 25 = 2$). Pressure is proportional to absolute temperature in kelvin, not Celsius. Doubling Celsius temperature does not double thermal energy.

---

### Check 4: Real gas deviation conditions

Under which set of conditions does a real gas show the greatest deviation from ideal gas behavior?

- **A.** High pressure and low temperature
- **B.** Low pressure and high temperature

**Feedback for A:** Correct. At high pressure, molecules are packed closely together, so the volume of the molecules themselves becomes significant compared to the container volume. At low temperature, molecules move slowly, so intermolecular attractive forces can no longer be neglected. These two factors cause substantial deviation from $pV = nRT$.

**Feedback for B:** Incorrect. Low pressure and high temperature are the conditions where real gases behave most like an ideal gas, because the particles are far apart and moving too rapidly for intermolecular attractions to have an effect.

---

## Mistakes worth repairing

### Mistake 1: Substituting temperature in degrees Celsius into $pV = nRT$
This is the single most common error in A Level thermal physics. If a question states that $T = 25\,^\circ\mathrm{C}$, substituting $25$ directly into $pV = nRT$ yields an answer that is wrong by a factor of more than 10! You must convert to kelvin immediately: $T = 25 + 273 = 298\,\mathrm{K}$.

### Mistake 2: Incorrect volume unit conversions ($\mathrm{cm^3}$ and $\mathrm{dm^3}$ to $\mathrm{m^3}$)
Linear conversion factors cannot be applied to volumes:
- $1\,\mathrm{m} = 100\,\mathrm{cm}$, but $1\,\mathrm{m^3} = (100\,\mathrm{cm})^3 = 10^6\,\mathrm{cm^3}$. Therefore, $1\,\mathrm{cm^3} = 10^{-6}\,\mathrm{m^3}$.
- $1\,\mathrm{dm^3} = 1\,\text{litre} = 10^{-3}\,\mathrm{m^3}$.
Inserting a volume of $500\,\mathrm{cm^3}$ as $500 \times 10^{-2}$ or $500 \times 10^{-3}$ corrupts the entire calculation.

### Mistake 3: Confusing the molar gas constant $R$ with the Boltzmann constant $k$
Remember the distinction:
- When the equation uses the number of **moles** $n$, use the molar gas constant $R = 8.31\,\mathrm{J\,K^{-1}\,mol^{-1}}$ ($pV = nRT$).
- When the equation uses the number of **molecules** $N$, use the Boltzmann constant $k = 1.38 \times 10^{-23}\,\mathrm{J\,K^{-1}}$ ($pV = NkT$).
Using $R$ with $N$, or $k$ with $n$, leads to an answer that is wrong by a factor of $N_A \approx 6.02 \times 10^{23}$!

### Mistake 4: Believing real gases always behave ideally
Real gases deviate from ideal behavior at high pressure and low temperature because real molecules have finite volume and experience attractive intermolecular forces. An ideal gas is a theoretical model that assumes point-like molecules with zero intermolecular forces.

### Mistake 5: Assuming $pV = \text{constant}$ applies during leaks or temperature changes
Boyle's law ($pV = \text{constant}$) is valid only if **both** temperature $T$ and the mass of gas $n$ remain strictly constant. If gas leaks from the container or if the container is heated, you must apply the full equation of state $pV = nRT$ rather than assuming $p_1 V_1 = p_2 V_2$.

---

## Core recap

- An **ideal gas** is defined as a gas that obeys the equation of state $pV = nRT$ (or $pV \propto T$) at all pressures, volumes, and thermodynamic temperatures.
- **Thermodynamic temperature** $T$ (in kelvin, $\mathrm{K}$) is measured from absolute zero:
  \[
  T\,(\mathrm{K}) = \theta\,(^\circ\mathrm{C}) + 273.15
  \]
- Absolute zero ($0\,\mathrm{K} = -273.15\,^\circ\mathrm{C}$) is the theoretical temperature at which a system has minimum internal energy.
- Real gases approximate ideal gases at **low pressure** and **high temperature**. They deviate at **high pressure** and **low temperature**.
- The **molar equation of state** is:
  \[
  pV = nRT
  \]
  where $n$ is amount of substance in moles, and $R = 8.31\,\mathrm{J\,K^{-1}\,mol^{-1}}$ is the molar gas constant.
- The **molecular equation of state** is:
  \[
  pV = NkT
  \]
  where $N$ is the number of molecules, and $k = 1.38 \times 10^{-23}\,\mathrm{J\,K^{-1}}$ is the Boltzmann constant.
- The Boltzmann constant links macroscopic and microscopic constants:
  \[
  k = \frac{R}{N_A}
  \]
- For a fixed mass of gas undergoing a change of state:
  \[
  \frac{p_1 V_1}{T_1} = \frac{p_2 V_2}{T_2}
  \]
