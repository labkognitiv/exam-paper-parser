# Power as work done per unit time

## Learning Outcomes

In this lesson, you will learn to:
- Define power as work done or energy transferred per unit time (Cambridge 9702 outcome `9702_t05_m01_o05`).
- Recall and use the relationship \(P = \frac{W}{t} = \frac{\Delta E}{t}\).
- State the SI unit of power, the watt (\(\mathrm{W}\)), and express it in terms of SI base units (\(\mathrm{kg\,m^2\,s^{-3}}\)).
- Distinguish between total work done (energy transferred) and the rate of doing work.
- Interpret work against time graphs, energy against time graphs, and power against time graphs.
- Relate useful power output, total input power, and wasted power through the concept of efficiency.

---

## Prior Knowledge

Before beginning this lesson, ensure you are comfortable with:
- **Work done by a constant force:** Work done is the product of force and displacement in the direction of the force:
  \[
  W = Fs
  \]
  measured in joules (\(\mathrm{J}\)), where \(1\,\mathrm{J} = 1\,\mathrm{N\,m} = 1\,\mathrm{kg\,m^2\,s^{-2}}\).
- **Conservation of energy:** Energy cannot be created or destroyed, only transferred from one form to another.
- **Efficiency:** Efficiency \(\eta\) of an energy transfer is the ratio of useful energy output to total energy input:
  \[
  \eta = \frac{\text{useful energy output}}{\text{total energy input}}
  \]
- **Scalars and vectors:** Work done and energy are scalar quantities, and time is a scalar quantity. Therefore, power is also a **scalar quantity**.

---

## Core Concepts

### Why does time matter in energy transfers?

Consider two electric construction hoists, Hoist A and Hoist B. Both hoists are tasked with lifting an identical pallet of concrete blocks of mass \(400\,\mathrm{kg}\) through a vertical height of \(15\,\mathrm{m}\) at a steady speed.

Because the mass and the lifting distance are identical, both hoists exert the same upward force (equal to the weight \(mg\)) through the exact same vertical displacement. Therefore, both hoists perform the exact same amount of work:

\[
W = Fs = mgh = 400\,\mathrm{kg} \times 9.81\,\mathrm{m\,s^{-2}} \times 15\,\mathrm{m} = 58\,860\,\mathrm{J}
\]

Now observe how long each hoist takes to finish the task:
- Hoist A completes the lift in \(12\,\mathrm{s}\).
- Hoist B takes \(60\,\mathrm{s}\) to complete the same lift.

Both hoists achieve the same physical outcome and transfer the same total quantity of energy (\(58.9\,\mathrm{kJ}\)). Yet Hoist A is clearly performing the work much faster than Hoist B. In everyday language, we say Hoist A is "more powerful".

In physics, we formalize this comparison by measuring how much work is completed every second. That quantity is **power**.

---

### The formal definition of power

In Cambridge International AS Level Physics, power is defined strictly through the rate at which work is done or energy is transferred:

<a id="definition-9702_def_power"></a>

> **Definition to learn: power.** work done or energy transferred per unit time

Let us examine every term in this definition:
- **Work done or energy transferred:** Doing work is the process of transferring energy by the action of a force. Whenever work is done, an equivalent quantity of energy is transferred from one form or store to another.
- **Per unit time:** This means dividing the quantity of work done (or energy transferred) by the time interval taken to do that work. In mathematical physics, "per unit time" is equivalent to "the rate of".
- **Accepted alternative phrasings:** Cambridge mark schemes also accept "rate of doing work" or "rate of energy transfer". However, the primary definition given above is the definitive syllabus standard.

---

### The formula for power

The definition translates directly into a mathematical formula:

<a id="formula-9702_formula_power_energy_time"></a>

> **Formula to learn: Power from energy transfer.**
>
> \[
> P = \frac{\Delta E}{t}
> \]

When expressing power in terms of mechanical work done \(W\), the formula is written as:

\[
P = \frac{W}{t}
\]

Where:
- **\(P\)** is the power, measured in watts (\(\mathrm{W}\)).
- **\(W\)** is the work done, measured in joules (\(\mathrm{J}\)).
- **\(\Delta E\)** is the energy transferred, measured in joules (\(\mathrm{J}\)).
- **\(t\)** is the time taken for the transfer, measured in seconds (\(\mathrm{s}\)).

Because work done is a scalar and time is a scalar, **power is a scalar quantity**. It has magnitude and units, but no spatial direction.

If the rate of work done varies during an interval, \(P = \frac{W}{t}\) gives the **average power** over that time interval \(t\). If the rate of work done is constant, the instantaneous power at every moment equals the average power.

---

### Units of power: the watt and SI base units

The SI derived unit of power is the **watt**, named in honour of the engineer James Watt and abbreviated as \(\mathrm{W}\).

#### Defining the watt
One watt is defined as the rate of energy transfer of one joule per second:

\[
1\,\mathrm{W} = 1\,\mathrm{J\,s^{-1}}
\]

Alternatively, one watt is the power developed when one joule of work is done in a time interval of one second.

#### Expressing the watt in SI base units
In Physics 9702, you must be able to derive and confirm the SI base units of any physical quantity. Let us break down the watt using base definitions:

1. Power is work divided by time:
   \[
   [P] = \frac{[W]}{[t]} = \frac{\mathrm{J}}{\mathrm{s}}
   \]
2. Work is force multiplied by distance (\(W = Fs\)):
   \[
   1\,\mathrm{J} = 1\,\mathrm{N\,m}
   \]
3. Force is mass multiplied by acceleration (\(F = ma\)):
   \[
   1\,\mathrm{N} = 1\,\mathrm{kg\,m\,s^{-2}}
   \]
4. Substitute newtons into joules:
   \[
   1\,\mathrm{J} = (1\,\mathrm{kg\,m\,s^{-2}}) \times (1\,\mathrm{m}) = 1\,\mathrm{kg\,m^2\,s^{-2}}
   \]
5. Finally, divide joules by seconds to find the base units of the watt:
   \[
   1\,\mathrm{W} = \frac{1\,\mathrm{kg\,m^2\,s^{-2}}}{1\,\mathrm{s}} = 1\,\mathrm{kg\,m^2\,s^{-3}}
   \]

> **Key result:** The SI base units of the watt are \(\mathrm{kg\,m^2\,s^{-3}}\).

#### Common metric prefixes for power
Engineering and everyday systems involve powers spanning many orders of magnitude:
- **Milliwatt (\(\mathrm{mW}\)):** \(1\,\mathrm{mW} = 10^{-3}\,\mathrm{W}\) (e.g. laser pointers, small electronic sensors)
- **Watt (\(\mathrm{W}\)):** \(1\,\mathrm{W} = 1\,\mathrm{J\,s^{-1}}\) (e.g. LED light bulbs, mobile phone charging)
- **Kilowatt (\(\mathrm{kW}\)):** \(1\,\mathrm{kW} = 10^3\,\mathrm{W} = 1000\,\mathrm{W}\) (e.g. electric kettles, domestic heaters)
- **Megawatt (\(\mathrm{MW}\)):** \(1\,\mathrm{MW} = 10^6\,\mathrm{W} = 1\,000\,000\,\mathrm{W}\) (e.g. locomotives, commercial wind turbines)
- **Gigawatt (\(\mathrm{GW}\)):** \(1\,\mathrm{GW} = 10^9\,\mathrm{W}\) (e.g. national power grid outputs, large nuclear stations)

Always convert values given in \(\mathrm{kW}\) or \(\mathrm{MW}\) into standard watts (\(\mathrm{W}\)) before performing calculations, and ensure time is in seconds (\(\mathrm{s}\)).

---

### Total work done versus rate of work done

A crucial concept in mechanics is the distinction between:
1. **Total energy transferred (or work done):** This is the total quantity of energy that changes form. It depends only on the magnitude of the force and the displacement. It does not depend on how quickly or slowly the process happens.
2. **Power:** This is the speed of the energy transfer. It depends explicitly on time.

Returning to our two construction hoists:
- Hoist A: \(P_A = \frac{58\,860\,\mathrm{J}}{12\,\mathrm{s}} = 4905\,\mathrm{W} \approx 4.9\,\mathrm{kW}\)
- Hoist B: \(P_B = \frac{58\,860\,\mathrm{J}}{60\,\mathrm{s}} = 981\,\mathrm{W} \approx 0.98\,\mathrm{kW}\)

Both hoists do identical work (\(58.9\,\mathrm{kJ}\)), but Hoist A operates at \(5.0\) times the power of Hoist B because it finishes the job in one-fifth of the time.

---

### Graphical representations of power

Exam questions frequently assess power through graphs. You must recognize two fundamental graphical relationships:

#### 1. Energy against time (or work against time) graph
Consider a graph plotting energy transferred \(E\) (or work done \(W\)) on the vertical axis against time \(t\) on the horizontal axis:

\[
\text{gradient} = \frac{\Delta E}{\Delta t} = P
\]

- **The gradient of an energy-time graph represents the power.**
- A straight-line graph through the origin indicates a constant gradient, meaning power is constant.
- A steeper straight line represents a higher power.
- If the line curves, the instantaneous power at any given time is found by drawing a tangent to the curve at that time and calculating the tangent's gradient.
- If the curve flattens out to a horizontal line (gradient \(= 0\)), energy transfer has ceased and the power is zero.

#### 2. Power against time graph
Consider a graph plotting power \(P\) on the vertical axis against time \(t\) on the horizontal axis:

\[
\text{area under graph} = P \times \Delta t = \Delta E = W
\]

- **The area under a power-time graph represents the total work done or energy transferred.**
- If power is constant, the area is a simple rectangle (\(\text{height} \times \text{width} = P \times t\)).
- If power varies linearly with time, the area is a triangle or trapezium.
- For non-linear curves, the total work done over a given time interval is the total area enclosed between the curve and the time axis.

---

### Power and efficiency

In real machines, not all input energy is converted into useful work. Friction, electrical resistance, and air turbulence dissipate energy into thermal energy in the surroundings.

Because power is energy transferred per unit time, we can write the law of conservation of energy in terms of power:

\[
P_{\text{input}} = P_{\text{useful}} + P_{\text{wasted}}
\]

Where:
- **\(P_{\text{input}}\)** is the total power supplied to the system.
- **\(P_{\text{useful}}\)** is the useful power output delivered by the system to do intended work.
- **\(P_{\text{wasted}}\)** is the power dissipated as non-useful energy (usually thermal energy) per second.

This gives the formula for **efficiency** in terms of power:

\[
\eta = \frac{\text{useful power output}}{\text{total power input}}
\]

To express efficiency as a percentage:

\[
\text{percentage efficiency} = \frac{\text{useful power output}}{\text{total power input}} \times 100\%
\]

Because the useful power output can never exceed the total power input (which would violate the conservation of energy), the efficiency \(\eta\) must satisfy:

\[
0 \le \eta \le 1 \quad (\text{or } 0\% \le \eta \le 100\%)
\]

---

## Worked Examples

### Worked Example 1: Lifting a load with an industrial crane

An electric overhead crane in a warehouse lifts a steel container of mass \(350\,\mathrm{kg}\) vertically upward through a height of \(18\,\mathrm{m}\) at constant speed. The crane takes \(25\,\mathrm{s}\) to complete the lift.

Calculate:
1. The work done by the crane's lifting cable on the container.
2. The average power output delivered to the container.
3. The power output if an upgraded crane performs the same lift in \(10\,\mathrm{s}\).

#### Strategy and model check
- Motion is vertical at constant speed, so acceleration is zero.
- The upward tension force \(T\) in the cable equals the downward weight \(mg\):
  \[
  T = mg = 350\,\mathrm{kg} \times 9.81\,\mathrm{m\,s^{-2}}
  \]
- Work done is \(W = Fs = T h\).
- Power is \(P = \frac{W}{t}\).
- Take acceleration of free fall \(g = 9.81\,\mathrm{m\,s^{-2}}\).

#### Step 1: Calculate the work done
Find the tension in the lifting cable:

\[
T = mg = 350 \times 9.81 = 3433.5\,\mathrm{N}
\]

Calculate the work done through vertical displacement \(h = 18\,\mathrm{m}\):

\[
W = T h = 3433.5\,\mathrm{N} \times 18\,\mathrm{m} = 61\,803\,\mathrm{J}
\]

Rounding to 2 significant figures gives \(6.2 \times 10^4\,\mathrm{J}\) (or \(62\,\mathrm{kJ}\)).

#### Step 2: Calculate the power output for the 25 s lift
Use the power equation:

\[
P = \frac{W}{t}
\]

Substitute unrounded work:

\[
P = \frac{61\,803\,\mathrm{J}}{25\,\mathrm{s}} = 2472.12\,\mathrm{W}
\]

To 2 significant figures, \(P = 2500\,\mathrm{W} = 2.5\,\mathrm{kW}\).

#### Step 3: Calculate the power output for the 10 s lift
The work done depends only on the load and the height, so \(W = 61\,803\,\mathrm{J}\) remains identical:

\[
P_{\text{new}} = \frac{61\,803\,\mathrm{J}}{10\,\mathrm{s}} = 6180.3\,\mathrm{W}
\]

To 2 significant figures, \(P_{\text{new}} = 6200\,\mathrm{W} = 6.2\,\mathrm{kW}\).

#### Official-style mark scheme breakdown
- **Part 1:**
  - **M1:** For using \(W = mgh\) with \(g = 9.81\,\mathrm{m\,s^{-2}}\) (\(350 \times 9.81 \times 18\)).
  - **A1:** Correct work done: \(6.2 \times 10^4\,\mathrm{J}\) (accept \(61.8\,\mathrm{kJ}\) or \(62\,\mathrm{kJ}\)).
- **Part 2:**
  - **M1:** For using \(P = \frac{W}{t}\) with work from part 1 divided by \(25\,\mathrm{s}\).
  - **A1:** Correct power: \(2500\,\mathrm{W}\) or \(2.5\,\mathrm{kW}\).
- **Part 3:**
  - **B1:** Correct power for \(10\,\mathrm{s}\): \(6200\,\mathrm{W}\) or \(6.2\,\mathrm{kW}\).

#### Reasonableness check
Lifting \(350\,\mathrm{kg}\) by \(18\,\mathrm{m}\) (about 6 building storeys) in \(25\,\mathrm{s}\) requires an average speed of \(\frac{18}{25} = 0.72\,\mathrm{m\,s^{-1}}\). A power of \(2.5\,\mathrm{kW}\) is typical for a small commercial hoist motor (about 3.3 horsepower). Units cancel correctly: \(\mathrm{J\,s^{-1}} = \mathrm{W}\).

---

### Worked Example 2: Water pump efficiency and rate of energy waste

An agricultural water pump lifts water from an underground well to an irrigation canal situated \(8.0\,\mathrm{m}\) vertically above the water table. The pump discharges \(45\,\mathrm{kg}\) of water every minute.

The electric motor driving the pump draws an electrical input power of \(95\,\mathrm{W}\).

Calculate:
1. The useful power output of the pumping system.
2. The efficiency of the pumping system.
3. The rate at which energy is wasted to the surroundings as heat and noise.

#### Strategy and model check
- Identify given quantities:
  - Mass of water lifted per minute: \(m = 45\,\mathrm{kg}\).
  - Time interval: \(t = 1.0\,\text{minute} = 60\,\mathrm{s}\).
  - Height lifted: \(h = 8.0\,\mathrm{m}\).
  - Electrical input power: \(P_{\text{input}} = 95\,\mathrm{W}\).
- Useful work done on the water is the gain in gravitational potential energy:
  \[
  W = mgh
  \]
- Useful output power is \(P_{\text{useful}} = \frac{W}{t}\).
- Efficiency is \(\eta = \frac{P_{\text{useful}}}{P_{\text{input}}}\).
- Rate of wasted energy is the wasted power: \(P_{\text{wasted}} = P_{\text{input}} - P_{\text{useful}}\).

#### Step 1: Calculate the useful power output
Convert time into seconds:
\[
t = 60\,\mathrm{s}
\]

Calculate the work done in lifting the water each minute:
\[
W = mgh = 45\,\mathrm{kg} \times 9.81\,\mathrm{m\,s^{-2}} \times 8.0\,\mathrm{m} = 3531.6\,\mathrm{J}
\]

Calculate the useful power output:
\[
P_{\text{useful}} = \frac{W}{t} = \frac{3531.6\,\mathrm{J}}{60\,\mathrm{s}} = 58.86\,\mathrm{W}
\]

To 2 significant figures, \(P_{\text{useful}} = 59\,\mathrm{W}\).

#### Step 2: Calculate the efficiency
Use the power definition of efficiency:

\[
\eta = \frac{P_{\text{useful}}}{P_{\text{input}}} = \frac{58.86\,\mathrm{W}}{95\,\mathrm{W}} = 0.61957 \approx 0.62
\]

As a percentage:

\[
\text{percentage efficiency} = 0.61957 \times 100\% = 62\%
\]

#### Step 3: Calculate the rate of wasted energy
By conservation of energy:

\[
P_{\text{wasted}} = P_{\text{input}} - P_{\text{useful}}
\]

\[
P_{\text{wasted}} = 95\,\mathrm{W} - 58.86\,\mathrm{W} = 36.14\,\mathrm{W}
\]

To 2 significant figures, \(P_{\text{wasted}} = 36\,\mathrm{W}\).

#### Official-style mark scheme breakdown
- **Part 1:**
  - **M1:** For calculating gravitational potential energy gain per second: \(\frac{45 \times 9.81 \times 8.0}{60}\).
  - **A1:** For correct useful power output: \(59\,\mathrm{W}\) (accept \(58.9\,\mathrm{W}\)).
- **Part 2:**
  - **M1:** For \(\frac{P_{\text{useful}}}{95}\) or \(\frac{3531.6}{95 \times 60}\).
  - **A1:** For correct efficiency: \(0.62\) or \(62\%\).
- **Part 3:**
  - **B1:** For correct wasted power: \(36\,\mathrm{W}\) (or \(95 - 59 = 36\,\mathrm{W}\)).

#### Reasonableness check
The useful power (\(59\,\mathrm{W}\)) is less than the input power (\(95\,\mathrm{W}\)), which satisfies the second law of thermodynamics (efficiency \(< 100\%\)). Wasted power (\(36\,\mathrm{W}\)) plus useful power (\(59\,\mathrm{W}\)) exactly sums to the total electrical power input of \(95\,\mathrm{W}\).

---

### Worked Example 3: Graphical analysis of energy transfer

An experimental electrical heating coil is energized at time \(t = 0\). The variation with time \(t\) of the total thermal energy \(E\) transferred by the coil is monitored and recorded:
- From \(t = 0\) to \(t = 30\,\mathrm{s}\), energy increases steadily in a straight line from \(0\) to \(7200\,\mathrm{J}\).
- From \(t = 30\,\mathrm{s}\) to \(t = 90\,\mathrm{s}\), the heater is switched to a lower setting; energy increases steadily in a straight line from \(7200\,\mathrm{J}\) to \(12\,600\,\mathrm{J}\).

Calculate:
1. The power rating of the heater during the first 30 seconds.
2. The power rating of the heater between \(t = 30\,\mathrm{s}\) and \(t = 90\,\mathrm{s}\).
3. The total area under the corresponding power against time graph from \(t = 0\) to \(t = 90\,\mathrm{s}\), explaining its physical meaning.

#### Strategy and model check
- On an energy-time graph, power is the gradient:
  \[
  P = \text{gradient} = \frac{\Delta E}{\Delta t}
  \]
- On a power-time graph, area under the graph represents total energy transferred:
  \[
  \text{Area} = \Delta E
  \]

#### Step 1: Power during Stage 1 (\(0\) to \(30\,\mathrm{s}\))
\[
P_1 = \frac{\Delta E_1}{\Delta t_1} = \frac{7200\,\mathrm{J} - 0\,\mathrm{J}}{30\,\mathrm{s} - 0\,\mathrm{s}} = \frac{7200\,\mathrm{J}}{30\,\mathrm{s}} = 240\,\mathrm{W}
\]

#### Step 2: Power during Stage 2 (\(30\) to \(90\,\mathrm{s}\))
The time duration of the second stage is \(\Delta t_2 = 90\,\mathrm{s} - 30\,\mathrm{s} = 60\,\mathrm{s}\).
The energy transferred during this interval is:
\[
\Delta E_2 = 12\,600\,\mathrm{J} - 7200\,\mathrm{J} = 5400\,\mathrm{J}
\]

Calculate the gradient:
\[
P_2 = \frac{\Delta E_2}{\Delta t_2} = \frac{5400\,\mathrm{J}}{60\,\mathrm{s}} = 90\,\mathrm{W}
\]

#### Step 3: Area under the power-time graph
The power-time graph consists of two horizontal segments:
- Segment 1: Height \(= 240\,\mathrm{W}\), width \(= 30\,\mathrm{s}\).
  \[
  \text{Area}_1 = 240\,\mathrm{W} \times 30\,\mathrm{s} = 7200\,\mathrm{J}
  \]
- Segment 2: Height \(= 90\,\mathrm{W}\), width \(= 60\,\mathrm{s}\).
  \[
  \text{Area}_2 = 90\,\mathrm{W} \times 60\,\mathrm{s} = 5400\,\mathrm{J}
  \]
- Total Area:
  \[
  \text{Total Area} = \text{Area}_1 + \text{Area}_2 = 7200\,\mathrm{J} + 5400\,\mathrm{J} = 12\,600\,\mathrm{J}
  \]

Physical meaning: The area under the power-time graph equals the total energy transferred by the heater over the entire 90-second duration (\(12.6\,\mathrm{kJ}\)).

#### Official-style mark scheme breakdown
- **Part 1:**
  - **C1:** Stating or using \(P = \text{gradient} = \frac{\Delta E}{\Delta t}\).
  - **A1:** \(P_1 = 240\,\mathrm{W}\).
- **Part 2:**
  - **C1:** Calculating \(\Delta E = 5400\,\mathrm{J}\) and \(\Delta t = 60\,\mathrm{s}\).
  - **A1:** \(P_2 = 90\,\mathrm{W}\).
- **Part 3:**
  - **B1:** Explaining that area under the power-time graph represents total energy transferred.
  - **B1:** Numerical value of area: \(12\,600\,\mathrm{J}\) (or \(1.26 \times 10^4\,\mathrm{J}\)).

---

## Guided Practice

Try this structured problem step by step before attempting the checks for understanding.

### Problem
A builder uses a motorized hoist to raise a bucket of wet cement of total mass \(65\,\mathrm{kg}\) from the ground to the scaffolding on a roof at a constant vertical speed. The vertical height of the roof is \(14\,\mathrm{m}\). The electric motor of the hoist has an efficiency of \(65\%\). The lift takes \(16\,\mathrm{s}\).

Calculate:
1. The gain in gravitational potential energy of the bucket (work done by the hoist).
2. The useful power output of the hoist.
3. The electrical input power required by the motor.

---

### Step-by-step guidance

#### Step 1: Gain in potential energy (work done)
- Use the formula \(W = mgh\).
- State the values: \(m = 65\,\mathrm{kg}\), \(g = 9.81\,\mathrm{m\,s^{-2}}\), \(h = 14\,\mathrm{m}\).
- Working:
  \[
  W = 65\,\mathrm{kg} \times 9.81\,\mathrm{m\,s^{-2}} \times 14\,\mathrm{m} = 8927.1\,\mathrm{J}
  \]
- Answer: **\(8.9 \times 10^3\,\mathrm{J}\)** (or \(8.93\,\mathrm{kJ}\)).

#### Step 2: Useful power output
- Use the formula \(P_{\text{useful}} = \frac{W}{t}\).
- State the time: \(t = 16\,\mathrm{s}\).
- Working:
  \[
  P_{\text{useful}} = \frac{8927.1\,\mathrm{J}}{16\,\mathrm{s}} = 557.94\,\mathrm{W}
  \]
- Answer: **\(560\,\mathrm{W}\)** (to 2 significant figures).

#### Step 3: Electrical input power
- Recall the efficiency formula:
  \[
  \eta = \frac{P_{\text{useful}}}{P_{\text{input}}} \implies P_{\text{input}} = \frac{P_{\text{useful}}}{\eta}
  \]
- Substitute \(\eta = 0.65\) and \(P_{\text{useful}} = 557.94\,\mathrm{W}\):
  \[
  P_{\text{input}} = \frac{557.94\,\mathrm{W}}{0.65} = 858.37\,\mathrm{W}
  \]
- Answer: **\(860\,\mathrm{W}\)** (to 2 significant figures).

---

## Checks for Understanding

Test your understanding of the concepts covered in this lesson.

### Check 1: Comparing work and power in athletes

Two weightlifters, Weightlifter X and Weightlifter Y, are performing training lifts:
- Weightlifter X lifts a barbell of mass \(70\,\mathrm{kg}\) vertically through a distance of \(0.60\,\mathrm{m}\) in a time of \(0.80\,\mathrm{s}\).
- Weightlifter Y lifts a barbell of mass \(90\,\mathrm{kg}\) vertically through a distance of \(0.60\,\mathrm{m}\) in a time of \(1.5\,\mathrm{s}\).

Which statement correctly compares their performances?

- **A.** Weightlifter Y does more work, but Weightlifter X develops greater power.
- **B.** Weightlifter Y does more work and develops greater power.

**Feedback for A:** Correct. Let us calculate both values:
- Work done:
  - \(W_X = m_X g h = 70 \times 9.81 \times 0.60 = 412\,\mathrm{J}\).
  - \(W_Y = m_Y g h = 90 \times 9.81 \times 0.60 = 530\,\mathrm{J}\).
  Weightlifter Y performs more work because the mass lifted is greater.
- Power developed:
  - \(P_X = \frac{412\,\mathrm{J}}{0.80\,\mathrm{s}} = 515\,\mathrm{W}\).
  - \(P_Y = \frac{530\,\mathrm{J}}{1.5\,\mathrm{s}} = 353\,\mathrm{W}\).
  Weightlifter X finishes the lift in a much shorter time, resulting in higher power.

**Feedback for B:** Incorrect. While Weightlifter Y does indeed do more work (\(530\,\mathrm{J}\) compared to \(412\,\mathrm{J}\)), Weightlifter Y takes almost twice as long (\(1.5\,\mathrm{s}\) versus \(0.80\,\mathrm{s}\)). Dividing work by time shows that Weightlifter X develops \(515\,\mathrm{W}\), which is significantly greater than Weightlifter Y's \(353\,\mathrm{W}\).

---

### Check 2: SI base units of the watt

Which combination of SI base units is equivalent to the watt (\(\mathrm{W}\))?

- **A.** \(\mathrm{kg\,m^2\,s^{-3}}\)
- **B.** \(\mathrm{kg\,m^2\,s^{-2}}\)

**Feedback for A:** Correct. Power is energy per unit time (\(\mathrm{J\,s^{-1}}\)). The joule in base units is \(\mathrm{N\,m} = (\mathrm{kg\,m\,s^{-2}})(\mathrm{m}) = \mathrm{kg\,m^2\,s^{-2}}\). Dividing by seconds (\(\mathrm{s}\)) gives \(\mathrm{kg\,m^2\,s^{-3}}\).

**Feedback for B:** Incorrect. \(\mathrm{kg\,m^2\,s^{-2}}\) is the SI base unit equivalent of the **joule** (the unit of work and energy). Power is work divided by time, so you must divide by an additional second, which changes \(\mathrm{s^{-2}}\) into \(\mathrm{s^{-3}}\).

---

### Check 3: Interpreting graph features

A scientist monitors an electric motor and plots a graph of the electrical power supplied to the motor against time. What does the area bounded between the plotted line and the time axis represent?

- **A.** The total electrical energy supplied to the motor.
- **B.** The rate of acceleration of the motor.

**Feedback for A:** Correct. On a power-time graph, the vertical axis represents \(\frac{\text{energy}}{\text{time}}\) and the horizontal axis represents \(\text{time}\). The product of the two axes is \((\text{power}) \times (\text{time}) = \left(\frac{\mathrm{J}}{\mathrm{s}}\right) \times \mathrm{s} = \mathrm{J}\). The area under the graph therefore represents total energy transferred (or work done).

**Feedback for B:** Incorrect. Power multiplied by time yields energy (\(\mathrm{J}\)), not acceleration (\(\mathrm{m\,s^{-2}}\)). To find acceleration, one would need a velocity-time graph.

---

### Check 4: Useful power and energy dissipation in a machine

An electric motor has a total electrical power input of \(400\,\mathrm{W}\) and operates with an efficiency of \(75\%\). At what rate is energy dissipated as heat to the surroundings?

- **A.** \(100\,\mathrm{W}\)
- **B.** \(300\,\mathrm{W}\)

**Feedback for A:** Correct. An efficiency of \(75\%\) means \(75\%\) of the input power is converted to useful output:
\[
P_{\text{useful}} = 0.75 \times 400\,\mathrm{W} = 300\,\mathrm{W}
\]
The remaining \(25\%\) is wasted as thermal energy. The rate of energy dissipation is:
\[
P_{\text{wasted}} = P_{\text{input}} - P_{\text{useful}} = 400\,\mathrm{W} - 300\,\mathrm{W} = 100\,\mathrm{W}
\]

**Feedback for B:** Incorrect. \(300\,\mathrm{W}\) is the **useful power output** (\(0.75 \times 400\,\mathrm{W}\)). The question asks for the rate at which energy is dissipated as heat (the wasted power), which is the remaining \(100\,\mathrm{W}\).

---

## Common Misconceptions

### Misconception 1: Confusing power with work done or energy
Students often use "powerful" as a synonym for "having a lot of energy" or "doing a lot of work".
- **The reality:** A small battery-powered toy motor and a huge industrial engine can perform the exact same amount of work (for example, lifting \(1000\,\mathrm{kg}\) through \(10\,\mathrm{m}\)). The toy motor might take three days, while the industrial engine takes two seconds.
- Total work done depends only on the force and displacement. Power measures **how quickly** that work is accomplished.

---

### Misconception 2: Confusing power with force
A frequent everyday mistake is assuming that a "more powerful machine" must always exert a larger force.
- **The reality:** Power is the rate of energy transfer, not force. A high-power engine can exert a relatively small force if that force moves at very high speed. Conversely, a hydraulic press can exert an immense force of hundreds of kilonewtons while moving at a crawl (\(1\,\mathrm{mm\,s^{-1}}\)), developing very modest power.
- Force is measured in newtons (\(\mathrm{N}\)); power is measured in watts (\(\mathrm{W}\)).

---

### Misconception 3: Forgetting to convert time into seconds
When calculating power, exam questions often state time intervals in minutes, hours, or days (for example, "a pump discharges water for 2.0 minutes" or "fuel used per hour").
- **The error:** Substituting minutes or hours directly into \(P = \frac{W}{t}\).
- **The correction:** The watt is defined strictly as joules per **second** (\(1\,\mathrm{W} = 1\,\mathrm{J\,s^{-1}}\)). You must always convert time into seconds:
  \[
  t = 2.0\,\text{minutes} = 2.0 \times 60\,\mathrm{s} = 120\,\mathrm{s}
  \]
  \[
  t = 1.0\,\text{hour} = 3600\,\mathrm{s}
  \]

---

### Misconception 4: Misidentifying graph properties (gradient versus area)
Students frequently invert the meanings of graphs involving power, work, and time:
- On an **energy against time graph**:
  - The **gradient** is power (\(P = \frac{\Delta E}{\Delta t}\)).
  - The area under the graph has no standard physical meaning (\(\mathrm{J\,s}\)).
- On a **power against time graph**:
  - The **area under the graph** is energy transferred or work done (\(W = P \times \Delta t\)).
  - The gradient represents the rate of change of power.

---

### Misconception 5: Multiplying by efficiency instead of dividing when finding input power
When given the useful power output and asked to calculate the required input power:
- **The error:** Calculating \(P_{\text{input}} = P_{\text{useful}} \times \eta\). This yields an input power that is smaller than the output power, which violates energy conservation.
- **The correction:** Because real machines are never more than \(100\%\) efficient (\(\eta < 1\)), the input power must always be **greater** than the useful output power:
  \[
  P_{\text{input}} = \frac{P_{\text{useful}}}{\eta}
  \]

---

## Core Recap

- **Power** is defined as **work done or energy transferred per unit time**:
  \[
  P = \frac{W}{t} = \frac{\Delta E}{t}
  \]
- Power is a **scalar quantity**.
- The SI unit of power is the **watt** (\(\mathrm{W}\)), defined as one joule per second:
  \[
  1\,\mathrm{W} = 1\,\mathrm{J\,s^{-1}}
  \]
- In **SI base units**, the watt is:
  \[
  1\,\mathrm{W} = 1\,\mathrm{kg\,m^2\,s^{-3}}
  \]
- **Energy** is the total quantity of work done (measured in \(\mathrm{J}\)); **power** is the rate at which work is done (measured in \(\mathrm{W}\)).
- On an **energy-time graph** (or work-time graph), the **gradient** equals power.
- On a **power-time graph**, the **area under the graph** equals total work done (energy transferred).
- For any real system:
  \[
  P_{\text{input}} = P_{\text{useful}} + P_{\text{wasted}}
  \]
- **Efficiency** in terms of power is:
  \[
  \eta = \frac{\text{useful power output}}{\text{total power input}}
  \]
