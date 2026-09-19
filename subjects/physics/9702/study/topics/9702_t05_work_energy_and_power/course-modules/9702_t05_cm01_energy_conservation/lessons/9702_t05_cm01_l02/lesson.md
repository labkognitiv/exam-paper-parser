# Conservation of Energy, Energy Dissipation, and Efficiency

## Learning Outcomes

In this lesson, you will learn to:

- State and apply the principle of conservation of energy to physical systems.
- Explain the physical mechanism of energy dissipation into non-useful thermal stores.
- Recall and understand that the efficiency of a system is the ratio of useful energy output from the system to the total energy input.
- Express efficiency both as a fraction and as a percentage.
- Calculate efficiency using energy ratios and power ratios: \(\eta = \frac{\text{useful energy output}}{\text{total energy input}} = \frac{\text{useful power output}}{\text{total power input}}\).
- Construct and interpret quantitative energy flow diagrams (Sankey diagrams).
- Calculate overall efficiency for multi-stage systems.
- Solve complex numerical problems involving energy conservation, wasted power, and efficiency in mechanical and electrical devices.

---

## Prior Knowledge

Before beginning this lesson, you should be confident with:

- **Work done:** The definition of work as the mechanical transfer of energy (\(W = Fs \cos\theta\)) from Lesson 1.
- **Energy and work equivalence:** The joule (\(\mathrm{J}\)) as the shared SI unit of work and energy, where \(1\,\mathrm{J} = 1\,\mathrm{N\,m} = 1\,\mathrm{kg\,m^2\,s^{-2}}\).
- **Newtonian mechanics:** Weight \(W = mg\) and balanced forces in steady motion from Topic 3.
- **Kinematics:** Constant speed and distance travelled (\(s = vt\)) from Topic 2.

---

## Core Concepts

### 1. The principle of conservation of energy

Energy is one of the most fundamental quantities in the physical universe. While energy exists in many different forms, it obeys an absolute universal rule:

> **The Principle of Conservation of Energy:**
> Energy cannot be created or destroyed; it can only be transformed from one form to another, or transferred from one body to another. The total energy of an isolated (closed) system remains constant.

In any closed system:

\[
E_{\mathrm{total, initial}} = E_{\mathrm{total, final}}
\]

#### Common forms of energy in Cambridge Physics:
1. **Kinetic energy (\(E_K\)):** Energy possessed by an object due to its motion.
2. **Gravitational potential energy (\(E_P\)):** Energy stored in a mass due to its position or height in a gravitational field.
3. **Elastic potential energy (strain energy):** Energy stored in a body due to its reversible mechanical deformation.
4. **Chemical energy:** Energy stored within chemical bonds of molecules (for example, in food, fuel, or battery cells).
5. **Electrical energy:** Energy transferred by electric currents flowing through a potential difference.
6. **Internal (thermal) energy:** The sum of random microscopic kinetic and potential energies of the atoms or molecules in a substance.
7. **Radiant (electromagnetic) energy:** Energy carried by electromagnetic waves, such as visible light, infrared, or radio waves.
8. **Nuclear energy:** Energy stored within the atomic nucleus, released during radioactive decay, fission, or fusion.

When energy changes from one form to another, the total quantity of energy before the transformation is precisely equal to the total quantity after the transformation.

---

### 2. Energy dissipation and degraded energy

If energy is always conserved, why do machines need a continuous fuel or electrical supply to keep running? Why can a car not coast indefinitely once brought up to highway speed?

The answer lies in **energy dissipation**:

In every real physical process, some fraction of the input energy is inevitably transferred into non-useful forms, predominantly **internal thermal energy** of the system components and surrounding atmosphere, as well as sound waves.

```
+--------------------+
| Total Energy Input |
+--------------------+
          |
          +-------------------------> [Useful Energy Output]
          |
          v
  [Dissipated Energy]
  (Thermal energy to surroundings + Sound)
```

#### Physical causes of energy dissipation:
- **Mechanical friction:** When two solid surfaces slide over one another, microscopic surface roughness (asperities) collide and momentarily weld. Breaking these microscopic bonds causes lattice vibrations, heating both surfaces.
- **Viscous drag and air resistance:** Moving through a fluid forces fluid molecules to accelerate and collide, creating turbulence and increasing the random thermal motion of the fluid.
- **Electrical resistance:** When electric charge moves through a conductor, drifting electrons collide with vibrating metal ions in the crystal lattice, transferring energy into lattice heat (Joule heating).
- **Inelastic deformation:** Repeated bending, stretching, or compression of materials (such as vehicle tyres rolling on tarmac) causes internal friction between polymer chains or crystal grains, dissipating energy as heat.

Once mechanical or electrical energy is converted into thermal energy in the surroundings, it spreads out (disperses) into billions of randomly moving air molecules. This dispersed energy is described as **degraded energy**. Although the energy still exists, it is disordered and cannot be collected back to do useful mechanical work.

For any real system, the conservation of energy equation is written as:

\[
\text{Total energy input} = \text{Useful energy output} + \text{Wasted (dissipated) energy}
\]

---

### 3. The definition of efficiency

Because no real machine can convert 100% of its input energy into the intended useful form, engineers and physicists use **efficiency** to quantify how effectively a device converts energy.

The Cambridge International AS Level Physics syllabus defines efficiency as:

> **Efficiency:** the ratio of useful energy output from the system to the total energy input

<a id="formula-9702_formula_efficiency"></a>

> **Formula to learn: Efficiency.**
>
> \[
> \eta = \frac{\text{useful energy output}}{\text{total energy input}} = \frac{\text{useful power output}}{\text{total power input}}
> \]

where \(\eta\) (the Greek letter eta) represents efficiency.

#### Key mathematical properties of efficiency:
1. **Efficiency as a fraction:**
   Because both numerator and denominator have units of joules (\(\mathrm{J}\)), efficiency is a **dimensionless ratio** (it has no units). It is expressed as a decimal between \(0\) and \(1\):
   \[
   0 \le \eta < 1
   \]
2. **Efficiency as a percentage:**
   Multiplying the decimal ratio by \(100\%\) gives percentage efficiency:
   \[
   \text{Efficiency } (\%) = \frac{\text{useful energy output}}{\text{total energy input}} \times 100\%
   \]
3. **Upper limit of efficiency:**
   Because useful energy output can never exceed total energy input without violating the conservation of energy, the efficiency of any real passive or active device can **never exceed 100%** (\(\eta \le 1.0\)).
4. **Power formulation:**
   Power is the rate of energy transfer (\(P = E / t\)). Dividing both useful energy output and total energy input by the time interval \(\Delta t\) yields the equivalent power formulation:
   \[
   \eta = \frac{P_{\mathrm{useful}}}{P_{\mathrm{input}}} = \frac{\text{useful power output}}{\text{total power input}}
   \]
   This formulation is particularly useful for continuous machines, such as electric motors, generators, pumps, and power stations.

---

### 4. Identifying useful versus wasted energy

To calculate efficiency correctly, you must clearly distinguish between the **purpose** of the machine (useful output) and the unwanted by-products (wasted output):

| Device | Total Energy Input | Useful Energy Output | Wasted Energy Output |
| :--- | :--- | :--- | :--- |
| **Electric motor** | Electrical energy | Mechanical work / kinetic energy | Thermal energy (Joule heating in windings) and sound |
| **Incandescent lamp** | Electrical energy | Radiant energy (visible light) | Thermal energy (infrared radiation and conduction to air) |
| **LED lamp** | Electrical energy | Radiant energy (visible light) | Thermal energy (in semiconductor junction) |
| **Car engine (petrol)** | Chemical potential energy | Mechanical kinetic energy | Thermal energy in exhaust gases, coolant radiator, sound |
| **Water pump** | Electrical / mechanical energy | Gravitational potential energy of water | Thermal energy in fluid friction, motor windings, pipe drag |
| **Bicycle brakes** | Kinetic energy of bicycle | None (useful function is stopping) | 100% dissipated as thermal energy in brake pads and rims |

Notice that what counts as "useful" depends strictly on the intended purpose:
- In an electric room heater, thermal energy output is the **useful** output, and any visible light emitted is technically wasted.
- In a desk reading lamp, visible light is the **useful** output, and thermal energy is **wasted**.

---

### 5. Quantitative energy flow diagrams (Sankey diagrams)

An effective visual tool for representing energy conservation and efficiency is the **Sankey diagram**.

In a Sankey diagram:
- Energy flows from left to right.
- The **width** of each arrow is directly proportional to the quantity of energy (or power).
- The total width of the input arrow on the left must equal the sum of the widths of all branches exiting on the right, graphically showing that energy is conserved.

```
Input Energy (100 J)
========================================+
                                        |=======> Useful Output Energy (75 J)
                                        |
                                        +=======> Wasted Heat Energy (25 J)
```

If an input arrow has a width of \(40\,\mathrm{mm}\) representing \(200\,\mathrm{W}\), and the useful output arrow has a width of \(30\,\mathrm{mm}\), the useful power is:
\[
P_{\mathrm{useful}} = 200\,\mathrm{W}\times \frac{30\,\mathrm{mm}}{40\,\mathrm{mm}} = 150\,\mathrm{W}
\]
The efficiency is:
\[
\eta = \frac{150\,\mathrm{W}}{200\,\mathrm{W}} = 0.75 = 75\%
\]
The remaining \(10\,\mathrm{mm}\) width represents \(50\,\mathrm{W}\) of dissipated power.

---

### 6. Multi-stage systems

Many industrial and everyday systems operate in stages. For example, in a fossil-fuel power delivery system:
1. Chemical energy in coal is converted to thermal steam energy (boiler efficiency \(\eta_1\)).
2. Steam drives a turbine to produce rotational kinetic energy (turbine efficiency \(\eta_2\)).
3. The turbine drives a generator to produce electrical energy (generator efficiency \(\eta_3\)).
4. Transmission cables carry electricity to homes (transmission efficiency \(\eta_4\)).

For any series of energy conversions, the **overall efficiency** of the complete system is the product of the individual stage efficiencies:

\[
\eta_{\mathrm{overall}} = \eta_1 \times \eta_2 \times \eta_3 \times \dots \times \eta_n
\]

#### Why multiply instead of adding or averaging?
Suppose Stage 1 has an efficiency of \(80\%\) (\(0.80\)) and Stage 2 has an efficiency of \(50\%\) (\(0.50\)):
- If \(100\,\mathrm{J}\) of energy enters Stage 1, Stage 1 delivers \(100 \times 0.80 = 80\,\mathrm{J}\) to Stage 2.
- Stage 2 receives \(80\,\mathrm{J}\) and delivers \(80 \times 0.50 = 40\,\mathrm{J}\) of useful output.
- The overall efficiency from start to finish is:
  \[
  \eta_{\mathrm{overall}} = \frac{40\,\mathrm{J}}{100\,\mathrm{J}} = 0.40 = 40\%
  \]
Notice that \(0.80 \times 0.50 = 0.40\).
Because each stage loses energy, the overall efficiency of a multi-stage system is always lower than the efficiency of any single individual stage in the chain.

---

## Worked Examples

### Worked example 1: Electric winch lifting a vertical load

An electric winch is used on a building site to raise a pallet of bricks of mass \(350\,\mathrm{kg}\). The winch lifts the pallet vertically upwards at a steady speed of \(0.60\,\mathrm{m\,s^{-1}}\) through a height of \(18\,\mathrm{m}\). The electric motor is supplied with a steady electrical power input of \(3.2\,\mathrm{kW}\).

```
         [MOTOR] <--- Electrical power input = 3.2 kW
            |
          Cable
            |
            v
       [PALLET] (mass = 350 kg)
            |
            +---> lifts vertically upwards at constant speed v = 0.60 m s^-1
```

Calculate:
1. The time taken to lift the pallet through the \(18\,\mathrm{m}\) vertical height.
2. The gain in gravitational potential energy of the pallet (the useful energy output).
3. The total electrical energy supplied to the motor during the lift.
4. The efficiency of the electric winch system.
5. The average rate at which thermal energy is dissipated to the surroundings.

#### Strategy and model check
- Motion is vertical at constant speed, so acceleration is zero.
- Upward tension equals pallet weight: \(T = mg = 350\,\mathrm{kg}\times 9.81\,\mathrm{m\,s^{-2}}\).
- Useful output is the mechanical work done in lifting the mass against gravity: \(W_{\mathrm{useful}} = mgh\).
- Total input is electrical energy: \(E_{\mathrm{in}} = P_{\mathrm{in}} \times t\).
- Target: time, useful energy, total energy, efficiency, and wasted power.

#### Step 1: Calculate the time taken
Using constant-speed kinematics:
\[
t = \frac{h}{v} = \frac{18\,\mathrm{m}}{0.60\,\mathrm{m\,s^{-1}}} = 30\,\mathrm{s}
\]

#### Step 2: Calculate the useful energy output
The useful work done lifting the load equals the gain in gravitational potential energy:
\[
E_{\mathrm{useful}} = mgh = 350\,\mathrm{kg}\times 9.81\,\mathrm{m\,s^{-2}}\times 18\,\mathrm{m}
\]
\[
E_{\mathrm{useful}} = 61\,803\,\mathrm{J} \approx 6.2 \times 10^4\,\mathrm{J} \quad (61.8\,\mathrm{kJ})
\]

#### Step 3: Calculate the total electrical energy input
The motor operates for \(t = 30\,\mathrm{s}\) at an input power of \(P_{\mathrm{in}} = 3.2\,\mathrm{kW} = 3200\,\mathrm{W}\):
\[
E_{\mathrm{in}} = P_{\mathrm{in}} \times t = 3200\,\mathrm{W}\times 30\,\mathrm{s} = 96\,000\,\mathrm{J} = 9.6 \times 10^4\,\mathrm{J} \quad (96\,\mathrm{kJ})
\]

#### Step 4: Calculate the efficiency
Apply the efficiency definition:
\[
\eta = \frac{E_{\mathrm{useful}}}{E_{\mathrm{in}}} = \frac{61\,803\,\mathrm{J}}{96\,000\,\mathrm{J}} = 0.6438 \implies 64\% \text{ (or } 0.64\text{)}
\]

Alternatively, using the power formulation:
- Useful mechanical power output:
  \[
  P_{\mathrm{useful}} = \frac{E_{\mathrm{useful}}}{t} = \frac{61\,803\,\mathrm{J}}{30\,\mathrm{s}} = 2060\,\mathrm{W} = 2.06\,\mathrm{kW}
  \]
  (or directly \(P_{\mathrm{useful}} = Fv = mgv = 350 \times 9.81 \times 0.60 = 2060\,\mathrm{W}\))
- Efficiency:
  \[
  \eta = \frac{P_{\mathrm{useful}}}{P_{\mathrm{in}}} = \frac{2060\,\mathrm{W}}{3200\,\mathrm{W}} = 0.6438 \implies 64\%
  \]

#### Step 5: Calculate the rate of thermal energy dissipation (wasted power)
By conservation of energy:
\[
P_{\mathrm{in}} = P_{\mathrm{useful}} + P_{\mathrm{wasted}}
\]
\[
P_{\mathrm{wasted}} = P_{\mathrm{in}} - P_{\mathrm{useful}} = 3200\,\mathrm{W} - 2060\,\mathrm{W} = 1140\,\mathrm{W} \approx 1.1 \times 10^3\,\mathrm{W} \quad (1.1\,\mathrm{kW})
\]

The total energy wasted as heat during the lift is:
\[
E_{\mathrm{wasted}} = E_{\mathrm{in}} - E_{\mathrm{useful}} = 96\,000\,\mathrm{J} - 61\,803\,\mathrm{J} = 34\,197\,\mathrm{J} \approx 3.4 \times 10^4\,\mathrm{J}
\]

#### Mark scheme
- **Part 1:**
  - **A1:** \(t = 30\,\mathrm{s}\)
- **Part 2:**
  - **M1:** \(E = mgh = 350 \times 9.81 \times 18\)
  - **A1:** \(E_{\mathrm{useful}} = 6.2 \times 10^4\,\mathrm{J}\) (accept \(61.8\,\mathrm{kJ}\) or \(62\,\mathrm{kJ}\))
- **Part 3:**
  - **M1:** \(E = P \times t = 3200 \times 30\)
  - **A1:** \(E_{\mathrm{in}} = 9.6 \times 10^4\,\mathrm{J}\) (or \(96\,\mathrm{kJ}\))
- **Part 4:**
  - **M1:** Ratio of useful energy (or power) to total input energy (or power) (\(61\,800 / 96\,000\) or \(2060 / 3200\))
  - **A1:** \(\eta = 0.64\) or \(64\%\) (accept \(64.4\%\))
- **Part 5:**
  - **M1:** Subtraction \(P_{\mathrm{in}} - P_{\mathrm{useful}}\) (\(3200 - 2060\))
  - **A1:** Dissipated power = \(1100\,\mathrm{W}\) or \(1.1\,\mathrm{kW}\) (accept \(1140\,\mathrm{W}\))

#### Reasonableness check
- Efficiency is \(64\%\), which is realistic for an industrial electric winch (typically \(60\% - 75\%\)).
- Energy balance: \(61.8\,\mathrm{kJ} + 34.2\,\mathrm{kJ} = 96.0\,\mathrm{kJ}\). Total energy is precisely conserved.

---

### Worked example 2: Pumped-storage hydroelectric system

A pumped-storage hydroelectric facility raises water from a lower reservoir to an upper mountain reservoir during the night. The pump system lifts \(3600\,\mathrm{kg}\) of water per minute through a vertical height of \(60\,\mathrm{m}\). The overall efficiency of the pump and motor system is \(72\%\).

Calculate:
1. The useful power delivered to the water in increasing its gravitational potential energy.
2. The electrical power input required from the grid.
3. The total energy wasted as heat in the pump and pipes during \(2.0\,\mathrm{hours}\) of operation.

#### Strategy and model check
- Water mass per unit time: \(\frac{m}{t} = \frac{3600\,\mathrm{kg}}{60\,\mathrm{s}} = 60\,\mathrm{kg\,s^{-1}}\).
- Useful power output is rate of gain of GPE: \(P_{\mathrm{useful}} = \frac{mgh}{t} = \left(\frac{m}{t}\right) g h\).
- Efficiency is \(\eta = 0.72\). Rearrange \(\eta = \frac{P_{\mathrm{useful}}}{P_{\mathrm{in}}}\) to find \(P_{\mathrm{in}} = \frac{P_{\mathrm{useful}}}{\eta}\).
- Time for energy calculation: \(t = 2.0\,\mathrm{h} = 2.0 \times 3600\,\mathrm{s} = 7200\,\mathrm{s}\).

#### Step 1: Useful power output

\[
\frac{m}{t} = \frac{3600\,\mathrm{kg}}{60\,\mathrm{s}} = 60\,\mathrm{kg\,s^{-1}}
\]
\[
P_{\mathrm{useful}} = \left(\frac{m}{t}\right) g h = 60\,\mathrm{kg\,s^{-1}}\times 9.81\,\mathrm{m\,s^{-2}}\times 60\,\mathrm{m}
\]
\[
P_{\mathrm{useful}} = 35\,316\,\mathrm{W} \approx 3.5 \times 10^4\,\mathrm{W} \quad (35.3\,\mathrm{kW})
\]

#### Step 2: Electrical power input
Using \(\eta = \frac{P_{\mathrm{useful}}}{P_{\mathrm{in}}}\):
\[
P_{\mathrm{in}} = \frac{P_{\mathrm{useful}}}{\eta} = \frac{35\,316\,\mathrm{W}}{0.72} = 49\,050\,\mathrm{W} \approx 4.9 \times 10^4\,\mathrm{W} \quad (49.1\,\mathrm{kW})
\]

#### Step 3: Wasted energy over 2.0 hours
First find the wasted power (rate of heat dissipation):
\[
P_{\mathrm{wasted}} = P_{\mathrm{in}} - P_{\mathrm{useful}} = 49\,050\,\mathrm{W} - 35\,316\,\mathrm{W} = 13\,734\,\mathrm{W}
\]
Now multiply by total time \(t = 7200\,\mathrm{s}\):
\[
E_{\mathrm{wasted}} = P_{\mathrm{wasted}} \times t = 13\,734\,\mathrm{W}\times 7200\,\mathrm{s}
\]
\[
E_{\mathrm{wasted}} = 98\,884\,800\,\mathrm{J} \approx 9.9 \times 10^7\,\mathrm{J} \quad (99\,\mathrm{MJ})
\]

Alternatively, calculate total input energy and subtract total useful energy:
- Total input energy: \(E_{\mathrm{in}} = 49\,050 \times 7200 = 3.53 \times 10^8\,\mathrm{J}\).
- Total useful energy: \(E_{\mathrm{useful}} = 35\,316 \times 7200 = 2.54 \times 10^8\,\mathrm{J}\).
- Wasted energy: \(3.53 \times 10^8 - 2.54 \times 10^8 = 9.9 \times 10^7\,\mathrm{J}\).

#### Mark scheme
- **Part 1:**
  - **M1:** Calculation of mass per second (\(3600 / 60 = 60\)) and use of \(P = (m/t)gh\) (\(60 \times 9.81 \times 60\))
  - **A1:** \(P_{\mathrm{useful}} = 3.5 \times 10^4\,\mathrm{W}\) (or \(35.3\,\mathrm{kW}\))
- **Part 2:**
  - **M1:** Rearrangement \(P_{\mathrm{in}} = P_{\mathrm{useful}} / \eta = 35\,316 / 0.72\)
  - **A1:** \(P_{\mathrm{in}} = 4.9 \times 10^4\,\mathrm{W}\) (or \(49.1\,\mathrm{kW}\))
- **Part 3:**
  - **M1:** Wasted power \((49\,050 - 35\,316 = 13\,734\,\mathrm{W})\) or energy difference method
  - **M1:** Multiplication by time in seconds (\(13\,734 \times 7200\))
  - **A1:** \(E_{\mathrm{wasted}} = 9.9 \times 10^7\,\mathrm{J}\) (accept \(98.9\,\mathrm{MJ}\) or \(99\,\mathrm{MJ}\))

---

### Worked example 3: System with percentage wasted power

An industrial refrigeration compressor has an efficiency of \(68\%\). During continuous operation, it dissipates wasted thermal energy into the surrounding coolant at a steady rate of \(560\,\mathrm{W}\).

Calculate:
1. The percentage of the input power that is wasted.
2. The total electrical power supplied to the compressor.
3. The useful mechanical power output delivered to compress the refrigerant gas.

#### Strategy and model check
- Conservation of power requires: \(\text{Percentage useful} + \text{Percentage wasted} = 100\%\).
- Given: \(\eta = 68\%\), so useful fraction is \(0.68\).
- Wasted power is \(P_{\mathrm{wasted}} = 560\,\mathrm{W}\).
- Target: percentage wasted, total input power \(P_{\mathrm{in}}\), and useful power \(P_{\mathrm{useful}}\).

#### Step 1: Percentage of input power wasted

\[
\text{Percentage wasted} = 100\% - \text{Efficiency} = 100\% - 68\% = 32\%
\]

#### Step 2: Total electrical power supplied
Because \(32\%\) of the total input power equals \(560\,\mathrm{W}\):
\[
0.32 \times P_{\mathrm{in}} = 560\,\mathrm{W}
\]
\[
P_{\mathrm{in}} = \frac{560\,\mathrm{W}}{0.32} = 1750\,\mathrm{W} \approx 1800\,\mathrm{W} \quad (1.8\,\mathrm{kW})
\]

#### Step 3: Useful mechanical power output
Now find \(68\%\) of the input power:
\[
P_{\mathrm{useful}} = \eta \times P_{\mathrm{in}} = 0.68 \times 1750\,\mathrm{W} = 1190\,\mathrm{W} \approx 1200\,\mathrm{W} \quad (1.2\,\mathrm{kW})
\]
Alternatively, using power conservation:
\[
P_{\mathrm{useful}} = P_{\mathrm{in}} - P_{\mathrm{wasted}} = 1750\,\mathrm{W} - 560\,\mathrm{W} = 1190\,\mathrm{W}
\]

#### Mark scheme
- **Part 1:**
  - **A1:** \(32\%\)
- **Part 2:**
  - **M1:** \(P_{\mathrm{in}} = 560 / 0.32\)
  - **A1:** \(P_{\mathrm{in}} = 1800\,\mathrm{W}\) or \(1.75\,\mathrm{kW}\) (accept \(1750\,\mathrm{W}\))
- **Part 3:**
  - **M1:** \(P_{\mathrm{useful}} = 1750 - 560\) or \(0.68 \times 1750\)
  - **A1:** \(P_{\mathrm{useful}} = 1200\,\mathrm{W}\) or \(1.19\,\mathrm{kW}\) (accept \(1190\,\mathrm{W}\))

---

## Guided Practice

### Problem statement
An electric delivery van of mass \(1800\,\mathrm{kg}\) travels at a steady speed of \(15\,\mathrm{m\,s^{-1}}\) along a horizontal road. To maintain this speed against air drag and rolling resistance, the electric motors must exert a total forward driving force of \(1200\,\mathrm{N}\). The vehicle battery pack supplies electrical energy at a constant rate of \(25\,\mathrm{kW}\).

Follow the steps below to evaluate the system performance:

#### Guidance step 1: Calculate the useful mechanical power output
Ask yourself: What is the useful purpose of the motor? It is to provide a forward driving force that moves the van along the road.
- The useful power output of a force moving at speed \(v\) is given by \(P = Fv\):
  \[
  P_{\mathrm{useful}} = Fv = 1200\,\mathrm{N}\times 15\,\mathrm{m\,s^{-1}} = 18\,000\,\mathrm{W} = 18\,\mathrm{kW}
  \]

#### Guidance step 2: Calculate the efficiency of the electric drive system
Now compare the useful mechanical power output to the total electrical power input:
\[
\eta = \frac{P_{\mathrm{useful}}}{P_{\mathrm{in}}} = \frac{18\,\mathrm{kW}}{25\,\mathrm{kW}} = 0.72
\]
Expressed as a percentage:
\[
\text{Efficiency} = 0.72 \times 100\% = 72\%
\]

#### Guidance step 3: Determine the rate of thermal energy dissipation
Apply conservation of energy to determine how much power is wasted as heat in the battery, motor windings, and transmission:
\[
P_{\mathrm{wasted}} = P_{\mathrm{in}} - P_{\mathrm{useful}} = 25\,\mathrm{kW} - 18\,\mathrm{kW} = 7.0\,\mathrm{kW} \quad (7000\,\mathrm{W})
\]
This \(7.0\,\mathrm{kW}\) is dissipated as thermal energy into the motor casings, inverter cooling system, and surrounding air.

---

## Checks for Understanding

### Check 1: Comparing traditional and modern lamps

An old-fashioned \(60\,\mathrm{W}\) filament lamp has an efficiency of \(5.0\%\), converting the remaining \(95\%\) of its electrical energy into heat. A modern LED lamp produces the exact same useful light output as the filament lamp, but requires an electrical power input of only \(5.0\,\mathrm{W}\).

What is the efficiency of the modern LED lamp?

- **A.** \(60\%\)
- **B.** \(12\%\)

**Feedback for A:** Correct. First find the useful light output of the filament lamp: \(P_{\mathrm{light}} = 0.050 \times 60\,\mathrm{W} = 3.0\,\mathrm{W}\). The modern LED lamp produces this same \(3.0\,\mathrm{W}\) of light from an electrical input of only \(5.0\,\mathrm{W}\). Therefore, the efficiency of the LED lamp is \(\eta = \frac{3.0\,\mathrm{W}}{5.0\,\mathrm{W}} = 0.60 = 60\%\). The LED lamp is 12 times more efficient than the traditional filament bulb.

**Feedback for B:** Incorrect. You divided \(60\,\mathrm{W}\) by \(5.0\,\mathrm{W}\) to get 12, and then wrote \(12\%\). The ratio of the two input powers tells you that the filament bulb consumes 12 times more power for the same light output. To find the efficiency of the LED lamp, divide its useful light power (\(3.0\,\mathrm{W}\)) by its electrical input power (\(5.0\,\mathrm{W}\)), which gives \(60\%\).

---

### Check 2: Efficiency calculation from wasted energy

A conveyor belt motor is supplied with \(4000\,\mathrm{J}\) of electrical energy to transport heavy luggage up a ramp. During the operation, \(1400\,\mathrm{J}\) of energy is dissipated as thermal energy due to friction and motor resistance.

What is the efficiency of the conveyor system?

- **A.** \(35\%\)
- **B.** \(65\%\)

**Feedback for A:** Incorrect. You calculated \(\frac{1400}{4000} \times 100\% = 35\%\). This is the percentage of energy **wasted**, not the efficiency. Efficiency is the ratio of **useful** energy output to total input.

**Feedback for B:** Correct. By conservation of energy, useful energy output equals total energy input minus wasted energy: \(E_{\mathrm{useful}} = 4000\,\mathrm{J} - 1400\,\mathrm{J} = 2600\,\mathrm{J}\). The efficiency is therefore \(\eta = \frac{2600\,\mathrm{J}}{4000\,\mathrm{J}} \times 100\% = 65\%\).

---

### Check 3: Power versus efficiency

Machine X has a power rating of \(500\,\mathrm{W}\) and an efficiency of \(80\%\). Machine Y has a power rating of \(2000\,\mathrm{W}\) and an efficiency of \(40\%\).

Which machine converts a higher fraction of its input energy into useful work?

- **A.** Machine X
- **B.** Machine Y

**Feedback for A:** Correct. Efficiency measures the **fraction** or percentage of input energy that becomes useful work. Machine X converts \(80\%\) of its input energy into useful work, whereas Machine Y converts only \(40\%\). Even though Machine Y has higher total power and produces more total useful power (\(800\,\mathrm{W}\) compared to \(400\,\mathrm{W}\)), Machine X is the more efficient machine because it wastes a smaller fraction of its energy.

**Feedback for B:** Incorrect. You confused total power output with efficiency. Machine Y does produce more useful power (\(0.40 \times 2000 = 800\,\mathrm{W}\)) than Machine X (\(0.80 \times 500 = 400\,\mathrm{W}\)). However, the question asked which machine converts a higher *fraction* of its input energy into useful work. That fraction is efficiency, and Machine X has an efficiency of \(80\%\) compared to \(40\%\) for Machine Y.

---

### Check 4: Multi-stage system efficiency

A coal-fired power station converts chemical energy to electricity with an efficiency of \(35\%\) (\(0.35\)). The national grid transmits this electricity to a factory with a transmission efficiency of \(90\%\) (\(0.90\)). Inside the factory, an electric motor operates with an efficiency of \(80\%\) (\(0.80\)).

What is the overall efficiency of converting the coal chemical energy into useful mechanical work in the factory?

- **A.** \(25\%\)
- **B.** \(68\%\)

**Feedback for A:** Correct. For multi-stage energy conversion systems, overall efficiency is the product of the individual stage efficiencies: \(\eta_{\mathrm{overall}} = \eta_1 \times \eta_2 \times \eta_3 = 0.35 \times 0.90 \times 0.80 = 0.252 = 25.2\% \approx 25\%\). Out of every \(100\,\mathrm{J}\) of chemical energy stored in the coal, only \(25\,\mathrm{J}\) is delivered as mechanical work by the factory motor.

**Feedback for B:** Incorrect. You calculated the average of the three efficiencies: \(\frac{35 + 90 + 80}{3} = 68.3\%\). Stage efficiencies cannot be averaged or added because each stage acts on the reduced energy output of the previous stage. You must multiply the fractional efficiencies.

---

## Common Misconceptions

### Misconception 1: "Wasted energy is destroyed or disappears"
A frequent student error is stating that energy is "lost" or "destroyed" by friction. In physics, energy is never destroyed. It is simply transformed into internal thermal energy, causing the temperature of the machine, contact surfaces, and surrounding air molecules to rise slightly. The total energy remains completely accounted for. It is better to use the term **dissipated** rather than "lost".

### Misconception 2: "A well-designed machine can be 100% efficient"
Some students believe that with superior lubricants, superconductors, or magnetic bearings, a mechanical or electrical machine could reach 100% efficiency. In practice, macroscopic processes always involve some degree of irreversibility: resistance, microscopic contact, thermal gradients, or acoustic radiation. Efficiency is always strictly less than 100% for any real-world device.

### Misconception 3: Confusing high power with high efficiency
Power and efficiency are distinct physical concepts:
- **Power** is the rate of energy transfer (measured in watts, \(\mathrm{W} = \mathrm{J\,s^{-1}}\)). It tells you how fast energy is being transferred.
- **Efficiency** is a dimensionless ratio (or percentage) comparing useful output to total input.
A massive \(500\,\mathrm{MW}\) power station can have a modest efficiency of \(36\%\), while a tiny \(5\,\mathrm{W}\) electronic circuit can achieve an efficiency exceeding \(90\%\). Never infer high efficiency from high power.

### Misconception 4: Inverting numerator and denominator
In exam calculations under time pressure, students occasionally calculate \(\frac{\text{total input}}{\text{useful output}}\). This yields a number greater than 1 (e.g. \(1.45\)), which would imply an impossible efficiency of \(145\%\). Always check: **efficiency must always be less than or equal to 1.0 (or \(100\%\))**. If your calculated value exceeds 1, you have inverted the fraction.

### Misconception 5: Treating wasted power as an extra input
When setting up conservation of power equations, some students mistakenly write \(\text{Input} + \text{Wasted} = \text{Useful}\). Remember that input energy is the total reservoir supplied to the machine:
\[
\text{Input} = \text{Useful} + \text{Wasted}
\]
Useful output and wasted output are the two branching pathways of the single input stream.

---

## Core Recap

- **Principle of conservation of energy:** Energy cannot be created or destroyed, only transformed from one form to another. Total energy in an isolated system is constant.
- **Energy dissipation:** In every real process, energy is partly converted into non-useful thermal energy that spreads out into the surroundings as degraded energy.
- **Efficiency:** The ratio of useful energy output from the system to the total energy input:
  \[
  \eta = \frac{\text{useful energy output}}{\text{total energy input}}
  \]
- **Power formulation of efficiency:**
  \[
  \eta = \frac{\text{useful power output}}{\text{total power input}}
  \]
- **Percentage efficiency:**
  \[
  \text{Efficiency } (\%) = \eta \times 100\%
  \]
- **Conservation of energy in any device:**
  \[
  \text{Total input} = \text{Useful output} + \text{Wasted output}
  \]
- Efficiency is a dimensionless scalar between \(0\) and \(1\) (\(0\%\) to \(100\%\)). For real systems, \(\eta < 1.0\).
- In a **Sankey diagram**, arrow widths are proportional to energy or power, visually illustrating energy conservation.
- For a **multi-stage system**, overall efficiency is the product of the individual stage efficiencies:
  \[
  \eta_{\mathrm{overall}} = \eta_1 \times \eta_2 \times \dots \times \eta_n
  \]
