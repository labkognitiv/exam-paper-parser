# Problem solving with power and the derivation of P = Fv

## Learning Outcomes

In this lesson, you will learn to:
- Solve multi-step problems using \(P = \frac{W}{t}\) and \(P = \frac{\Delta E}{t}\) (Cambridge 9702 outcome `9702_t05_m01_o06`).
- Derive the mechanical power relationship \(P = Fv\) from the definition of power and work done (Cambridge 9702 outcome `9702_t05_m01_o07`).
- State the physical conditions and vector considerations under which \(P = Fv\) is valid.
- Apply \(P = Fv\) to vehicles moving at constant speed along horizontal surfaces against resistive forces.
- Apply \(P = Fv\) to vehicles climbing inclined planes against both friction and the component of weight.
- Solve continuous mass-flow and fluid-pumping problems combined with efficiency.
- Analyze the cubic power law (\(P \propto v^3\)) for motion through a fluid when resistive drag is proportional to speed squared.

---

## Prior Knowledge

Before studying this lesson, ensure you understand:
- **Definition of power:** Power is work done or energy transferred per unit time:
  \[
  P = \frac{W}{t} = \frac{\Delta E}{t}
  \]
  measured in watts (\(\mathrm{W}\)), where \(1\,\mathrm{W} = 1\,\mathrm{J\,s^{-1}} = 1\,\mathrm{kg\,m^2\,s^{-3}}\).
- **Work done by a constant force:**
  \[
  W = Fs
  \]
  where \(s\) is the displacement in the direction of the force.
- **Velocity in uniform motion:** For constant velocity in a straight line, displacement is related to velocity and time by:
  \[
  s = vt
  \]
- **Equilibrium and Newton's first law:** When an object moves with constant velocity, its acceleration is zero (\(a = 0\)). The resultant force is zero:
  \[
  \Sigma F = 0
  \]
  Therefore, any forward driving force must exactly balance the total opposing resistive force.
- **Components of weight on an incline:** For an object of mass \(m\) on a slope inclined at angle \(\theta\) to the horizontal, the component of gravitational force acting parallel to the slope down the incline is:
  \[
  W_{\text{parallel}} = mg\sin\theta
  \]
- **Efficiency:**
  \[
  \eta = \frac{\text{useful power output}}{\text{total power input}}
  \]

---

## Core Concepts

### From work per second to force times velocity

In the previous lesson, we calculated power by taking the total work done over an interval and dividing by the elapsed time:

\[
P = \frac{W}{t}
\]

This formula is ideal when an object is lifted by a fixed height or when a measurable quantity of fuel or electrical energy is consumed over several minutes.

However, consider an aeroplane cruising at \(240\,\mathrm{m\,s^{-1}}\), a car driving along a motorway, or a speedboat cutting through the sea. The engines apply a continuous forward thrust \(F\) against opposing air drag and friction while the vehicle travels at speed \(v\).

In such situations, we do not want to wait for the vehicle to travel many kilometres to measure distance and time. We want to know the power delivered **at this exact speed**. To do that, we derive a direct relationship between power, force, and velocity.

---

### Step-by-step derivation of P = Fv

The derivation of \(P = Fv\) is a syllabus requirement in Cambridge International AS Level Physics and is regularly tested in both structured questions and multiple-choice papers.

Follow each step carefully:

1. **Start with the definition of power:**
   Power is work done per unit time:
   \[
   P = \frac{W}{t}
   \]

2. **Express work done by a constant force:**
   When a constant force \(F\) acts on a body and moves it through a displacement \(s\) in the direction of the force, the work done is:
   \[
   W = Fs
   \]

3. **Substitute work into the power formula:**
   Replace \(W\) with \(Fs\):
   \[
   P = \frac{Fs}{t}
   \]

4. **Group the displacement and time:**
   Rearrange the fraction:
   \[
   P = F \left(\frac{s}{t}\right)
   \]

5. **Substitute velocity for displacement over time:**
   For a body travelling with constant velocity (or to find average speed over time interval \(t\)), the velocity is:
   \[
   v = \frac{s}{t}
   \]
   Substituting \(v\) into the equation yields:
   \[
   P = Fv
   \]

<a id="formula-9702_formula_mechanical_power"></a>

> **Formula to learn: Mechanical power.**
>
> \[
> P = Fv
> \]

Where:
- **\(P\)** is the power developed by the force, measured in watts (\(\mathrm{W}\)).
- **\(F\)** is the force acting on the body, measured in newtons (\(\mathrm{N}\)).
- **\(v\)** is the velocity of the body in the direction of the force, measured in metres per second (\(\mathrm{m\,s^{-1}}\)).

---

### Conditions and limitations of P = Fv

To use \(P = Fv\) correctly and avoid common exam penalties, keep the following conditions in mind:

1. **Direction of force and motion:**
   The equation \(P = Fv\) assumes that the force \(F\) acts in the **exact same direction** as the velocity vector \(v\).
   If the force is applied at an angle \(\theta\) to the direction of motion, only the component of force parallel to the displacement does work:
   \[
   P = (F\cos\theta) v = Fv\cos\theta
   \]
   A force acting at \(90^\circ\) to the velocity (such as the normal contact force or centripetal force) does zero work and develops zero power because \(\cos 90^\circ = 0\).

2. **Constant velocity versus instantaneous power:**
   - If a body moves at **constant velocity**, \(P = Fv\) gives the steady power delivered by the force over any duration.
   - If a body is **accelerating**, its velocity changes continuously. At any specific moment, \(P = Fv\) gives the **instantaneous power** developed by the force at that precise speed. As speed increases under a constant force, the power developed increases proportionally.

3. **Scalar status:**
   Force is a vector and velocity is a vector, but power is a **scalar quantity**. It represents the scalar product of force and velocity.

---

### Vehicles moving at constant speed on level ground

When a vehicle (car, motorcycle, train, boat, or aircraft) travels along a flat, horizontal path at constant speed \(v\):

1. **Newton's first law applies:**
   Because speed and direction are constant, acceleration is zero (\(a = 0\)).
   The resultant horizontal force on the vehicle must be zero:
   \[
   \Sigma F = F_{\text{drive}} - F_{\text{resist}} = 0
   \]
   \[
   F_{\text{drive}} = F_{\text{resist}}
   \]
   where \(F_{\text{drive}}\) is the forward driving force exerted by the engine (through the wheels or propeller) and \(F_{\text{resist}}\) is the total opposing resistive force (friction and air resistance).

2. **Power delivered by the engine:**
   The useful mechanical power developed by the engine to maintain this constant speed is:
   \[
   P = F_{\text{drive}} v = F_{\text{resist}} v
   \]

3. **What happens to the energy?**
   Students often wonder: if the car is not speeding up and not gaining height, where does the fuel energy go?
   All the mechanical work done by the engine is transferred by resistive forces into **thermal energy** in the air and road surface, as well as sound. The surroundings warm up slightly.

---

### Vehicles moving up an inclined plane at constant speed

When a vehicle travels up a slope inclined at angle \(\theta\) to the horizontal at constant speed \(v\), the engine must work against two distinct opposing influences:

1. **Resistive forces (\(R\)):** Air resistance and road friction acting down the slope opposite to the direction of motion.
2. **Component of weight parallel to the slope:** Gravity pulls vertically downward with force \(W = mg\). Resolving this weight along the slope gives a backward force directed down the incline:
   \[
   F_{\text{gravity}} = mg\sin\theta
   \]

Because the vehicle moves at constant velocity, the resultant force along the slope is zero:

\[
\Sigma F_{\text{parallel}} = 0 \implies F_{\text{drive}} - R - mg\sin\theta = 0
\]

\[
F_{\text{drive}} = R + mg\sin\theta
\]

Multiplying this total required driving force by the speed \(v\) gives the useful power output:

\[
P = F_{\text{drive}} v = (R + mg\sin\theta) v
\]

#### Energy conservation perspective
We can also arrive at this formula by considering energy transfers per second:
- Rate of doing work against friction:
  \[
  P_{\text{friction}} = R v
  \]
- Rate of gaining gravitational potential energy:
  In time \(\Delta t\), the vehicle moves distance \(\Delta s = v \Delta t\) along the slope. The vertical height gained is:
  \[
  \Delta h = \Delta s \sin\theta = (v \Delta t) \sin\theta
  \]
  The rate of gain of gravitational potential energy is:
  \[
  \frac{\Delta E_P}{\Delta t} = \frac{mg\Delta h}{\Delta t} = \frac{mg (v \Delta t \sin\theta)}{\Delta t} = (mg\sin\theta) v
  \]
- Adding the two rates gives the total useful power output:
  \[
  P = R v + (mg\sin\theta) v = (R + mg\sin\theta) v
  \]
Both methods yield the identical equation, confirming complete consistency.

---

### Non-linear drag and the cubic power law

In simple problems, resistive force is sometimes modelled as constant. However, for real vehicles moving through fluids (air or water) at moderate to high speeds, aerodynamic drag increases with speed.

In many physical situations, the resistive drag force \(F_{\text{drag}}\) is proportional to the square of the speed:

\[
F_{\text{drag}} = k v^2
\]

where \(k\) is a constant depending on fluid density, frontal cross-sectional area, and aerodynamic shape.

Now substitute this drag into the power formula:

\[
P = F_{\text{drag}} v = (k v^2) v = k v^3
\]

> **Key deduction:** When resistive force is proportional to \(v^2\), the power required to overcome drag is proportional to the **cube of the speed**:
> \[
> P \propto v^3
> \]

#### Consequences of the cubic law
- If the speed of a car or boat is **doubled** (\(\times 2\)), the resistive force increases by \(2^2 = 4\) times.
- But the power required increases by \(2^3 = 8\) times!
- To travel three times as fast (\(\times 3\)), the engine must supply \(3^3 = 27\) times as much power.
This cubic relationship explains why high-speed vehicles require extraordinarily powerful engines to achieve modest gains in top speed, and why fuel economy drops dramatically at high speeds.

---

### Continuous mass flow: fluid pumps and turbines

Another major class of exam problems asks you to apply \(P = \frac{W}{t} = \frac{\Delta E}{t}\) to systems where matter flows continuously, such as water pumps, hydroelectric stations, and jet engines.

When a pump raises a mass of liquid \(\Delta m\) through a vertical height \(h\) in time \(\Delta t\):

1. The work done on that mass of liquid is:
   \[
   \Delta W = (\Delta m) g h
   \]
2. The useful power output is:
   \[
   P_{\text{useful}} = \frac{\Delta W}{\Delta t} = \left(\frac{\Delta m}{\Delta t}\right) g h
   \]
   where \(\frac{\Delta m}{\Delta t}\) is the **mass flow rate** in kilograms per second (\(\mathrm{kg\,s^{-1}}\)).

3. If the volume flow rate \(\frac{\Delta V}{\Delta t}\) (in \(\mathrm{m^3\,s^{-1}}\)) is given alongside the fluid density \(\rho\) (in \(\mathrm{kg\,m^{-3}}\)):
   \[
   \frac{\Delta m}{\Delta t} = \rho \left(\frac{\Delta V}{\Delta t}\right)
   \]
   Substituting this into the power formula gives:
   \[
   P_{\text{useful}} = \rho \left(\frac{\Delta V}{\Delta t}\right) g h
   \]

---

## Worked Examples

### Worked Example 1: Automobile cruising on a level motorway

A passenger car travels along a straight, horizontal motorway at a constant speed of \(90\,\mathrm{km\,h^{-1}}\). The combined resistive forces acting against the car (air resistance and rolling friction) have a magnitude of \(640\,\mathrm{N}\).

The car's internal combustion engine has an overall efficiency of \(28\%\).

Calculate:
1. The forward driving force provided by the car's wheels.
2. The useful mechanical power output delivered by the engine.
3. The total power input required from the fuel.

#### Strategy and model check
- Motion is horizontal and at constant speed, so acceleration \(a = 0\).
- Resultant force is zero: forward driving force equals opposing resistive force.
- Speed is given in kilometres per hour (\(\mathrm{km\,h^{-1}}\)) and must be converted to metres per second (\(\mathrm{m\,s^{-1}}\)).
- Apply \(P_{\text{useful}} = Fv\).
- Apply efficiency \(\eta = \frac{P_{\text{useful}}}{P_{\text{input}}}\) to find fuel power input.

#### Step 1: Forward driving force
Because the car travels at constant velocity, the forces are in equilibrium:

\[
\Sigma F = 0 \implies F_{\text{drive}} = F_{\text{resist}} = 640\,\mathrm{N}
\]

The driving force is **\(640\,\mathrm{N}\) forward**.

#### Step 2: Convert speed and calculate useful power
Convert speed to SI base units:

\[
v = 90\,\mathrm{km\,h^{-1}} = \frac{90 \times 1000\,\mathrm{m}}{3600\,\mathrm{s}} = 25.0\,\mathrm{m\,s^{-1}}
\]

Calculate the useful power output using \(P = Fv\):

\[
P_{\text{useful}} = F_{\text{drive}} v = 640\,\mathrm{N} \times 25.0\,\mathrm{m\,s^{-1}} = 16\,000\,\mathrm{W}
\]

In kilowatts, \(P_{\text{useful}} = 16\,\mathrm{kW}\) (or \(1.6 \times 10^4\,\mathrm{W}\)).

#### Step 3: Total power input from fuel
Use the efficiency formula rearranged for input power:

\[
P_{\text{input}} = \frac{P_{\text{useful}}}{\eta}
\]

Substitute \(P_{\text{useful}} = 16\,000\,\mathrm{W}\) and \(\eta = 0.28\):

\[
P_{\text{input}} = \frac{16\,000\,\mathrm{W}}{0.28} = 57\,143\,\mathrm{W}
\]

To 2 significant figures, \(P_{\text{input}} = 57\,\mathrm{kW}\) (or \(5.7 \times 10^4\,\mathrm{W}\)).

#### Official-style mark scheme breakdown
- **Part 1:**
  - **B1:** Stating that driving force equals resistive force (\(640\,\mathrm{N}\)) due to constant speed (zero resultant force).
- **Part 2:**
  - **M1:** Converting \(90\,\mathrm{km\,h^{-1}}\) to \(25\,\mathrm{m\,s^{-1}}\) and using \(P = Fv\).
  - **A1:** Correct useful power: \(16\,\mathrm{kW}\) or \(16\,000\,\mathrm{W}\).
- **Part 3:**
  - **M1:** Using \(P_{\text{input}} = \frac{P_{\text{useful}}}{\eta}\) with \(\eta = 0.28\).
  - **A1:** Correct input power: \(57\,\mathrm{kW}\) (accept \(57.1\,\mathrm{kW}\) or \(5.7 \times 10^4\,\mathrm{W}\)).

#### Reasonableness check
A useful power output of \(16\,\mathrm{kW}\) (about 21 horsepower) is entirely typical for a modern passenger vehicle cruising at \(90\,\mathrm{km\,h^{-1}}\) on a level highway, where the engine operates at low load. The input power of \(57\,\mathrm{kW}\) properly exceeds the useful power.

---

### Worked Example 2: Heavy freight truck climbing an incline

A fully loaded freight truck of total mass \(8500\,\mathrm{kg}\) climbs a straight road inclined at an angle of \(4.5^\circ\) to the horizontal. The truck maintains a constant speed of \(18\,\mathrm{m\,s^{-1}}\).

The combined opposing frictional and air resistance forces acting on the truck total \(1200\,\mathrm{N}\).

Calculate:
1. The component of the truck's weight directed parallel to the slope down the incline.
2. The forward driving force needed to maintain this constant speed.
3. The useful power output developed by the truck's engine.

#### Strategy and model check
- Motion is along an incline of angle \(\theta = 4.5^\circ\).
- Speed is constant (\(v = 18\,\mathrm{m\,s^{-1}}\)), so acceleration along the slope is zero.
- Opposing forces along the slope: friction (\(R = 1200\,\mathrm{N}\)) plus component of weight down the slope (\(mg\sin\theta\)).
- Apply \(\Sigma F = 0\) along the incline.
- Calculate power using \(P = F_{\text{drive}} v\).
- Use \(g = 9.81\,\mathrm{m\,s^{-2}}\).

#### Step 1: Component of weight along the slope
The weight of the truck is:

\[
W = mg = 8500\,\mathrm{kg} \times 9.81\,\mathrm{m\,s^{-2}} = 83\,385\,\mathrm{N}
\]

The component of weight acting parallel to the incline is:

\[
W_{\text{parallel}} = mg\sin\theta = 83\,385\,\mathrm{N} \times \sin(4.5^\circ)
\]

Evaluating the trigonometric term:
\[
\sin(4.5^\circ) \approx 0.078459
\]

\[
W_{\text{parallel}} = 83\,385 \times 0.078459 = 6542.3\,\mathrm{N}
\]

To 2 significant figures, \(W_{\text{parallel}} = 6500\,\mathrm{N}\) (or \(6.5\,\mathrm{kN}\)).

#### Step 2: Forward driving force
Set up the force balance along the incline:

\[
F_{\text{drive}} = R + W_{\text{parallel}} = 1200\,\mathrm{N} + 6542.3\,\mathrm{N} = 7742.3\,\mathrm{N}
\]

To 2 significant figures, \(F_{\text{drive}} = 7700\,\mathrm{N}\) (or \(7.7\,\mathrm{kN}\)).

#### Step 3: Useful power output
Apply the formula \(P = Fv\):

\[
P = F_{\text{drive}} v = 7742.3\,\mathrm{N} \times 18\,\mathrm{m\,s^{-1}} = 139\,361\,\mathrm{W}
\]

To 2 significant figures, \(P = 140\,\mathrm{kW}\) (or \(1.4 \times 10^5\,\mathrm{W}\)).

#### Alternative check via rate of energy transfer
- Rate of working against friction:
  \[
  P_{\text{resist}} = R v = 1200\,\mathrm{N} \times 18\,\mathrm{m\,s^{-1}} = 21\,600\,\mathrm{W}
  \]
- Rate of gaining potential energy:
  \[
  P_{\text{gain}} = mg (v \sin\theta) = 6542.3\,\mathrm{N} \times 18\,\mathrm{m\,s^{-1}} = 117\,761\,\mathrm{W}
  \]
- Total power:
  \[
  P_{\text{total}} = 21\,600\,\mathrm{W} + 117\,761\,\mathrm{W} = 139\,361\,\mathrm{W} \approx 140\,\mathrm{kW}
  \]
The two approaches match identically.

#### Official-style mark scheme breakdown
- **Part 1:**
  - **C1:** Using \(W_{\text{parallel}} = mg\sin\theta\) with \(8500 \times 9.81 \times \sin(4.5^\circ)\).
  - **A1:** Correct component: \(6540\,\mathrm{N}\) or \(6.5 \times 10^3\,\mathrm{N}\).
- **Part 2:**
  - **C1:** Summing resistive force and parallel weight component: \(1200 + 6542 = 7742\,\mathrm{N}\).
- **Part 3:**
  - **A1:** Multiplying total driving force by speed: \(7742 \times 18 = 140\,\mathrm{kW}\) (accept \(139\,\mathrm{kW}\) or \(1.4 \times 10^5\,\mathrm{W}\)).

---

### Worked Example 3: Non-linear aerodynamic drag and power scaling

An electric high-speed passenger train travels on a horizontal track. At a cruising speed of \(40\,\mathrm{m\,s^{-1}}\), the train requires a useful power output of \(1.6\,\mathrm{MW}\) from its motors to maintain speed.

At these speeds, mechanical friction is negligible compared to aerodynamic drag, and the drag force is known to be proportional to the square of the speed:

\[
F_{\text{drag}} = k v^2
\]

where \(k\) is a constant.

Calculate:
1. Show that the power \(P\) required to overcome this drag is proportional to \(v^3\).
2. The value of the proportionality constant \(k\), stating its SI base units.
3. The useful power output required from the motors if the train accelerates to a new cruising speed of \(60\,\mathrm{m\,s^{-1}}\).

#### Strategy and model check
- Substitute \(F_{\text{drag}} = k v^2\) into \(P = Fv\).
- Use initial conditions (\(v_1 = 40\,\mathrm{m\,s^{-1}}\), \(P_1 = 1.6 \times 10^6\,\mathrm{W}\)) to find \(k\).
- Determine SI base units of \(k\) from \(k = \frac{P}{v^3}\) or \(k = \frac{F}{v^2}\).
- Calculate the new power \(P_2\) using the cubic power relation.

#### Step 1: Derive the cubic power relationship
Start with \(P = Fv\):

\[
P = F_{\text{drag}} v
\]

Substitute \(F_{\text{drag}} = k v^2\):

\[
P = (k v^2) v = k v^3
\]

Because \(k\) is constant, \(P \propto v^3\).

#### Step 2: Determine the constant k and its units
Rearrange for \(k\):

\[
k = \frac{P_1}{v_1^3}
\]

Substitute the known values:

\[
k = \frac{1.6 \times 10^6\,\mathrm{W}}{(40\,\mathrm{m\,s^{-1}})^3} = \frac{1\,600\,000}{64\,000} = 25\,\mathrm{W\,s^3\,m^{-3}}
\]

Now determine the SI base units of \(k\):
From \(F = k v^2\):
\[
[k] = \frac{[F]}{[v^2]} = \frac{\mathrm{kg\,m\,s^{-2}}}{(\mathrm{m\,s^{-1}})^2} = \frac{\mathrm{kg\,m\,s^{-2}}}{\mathrm{m^2\,s^{-2}}} = \mathrm{kg\,m^{-1}}
\]

Thus, \(k = 25\,\mathrm{kg\,m^{-1}}\).

#### Step 3: Power at 60 m s\(^{-1}\)
Using the ratio method:

\[
\frac{P_2}{P_1} = \left(\frac{v_2}{v_1}\right)^3
\]

\[
\frac{P_2}{1.6\,\mathrm{MW}} = \left(\frac{60}{40}\right)^3 = (1.5)^3 = 3.375
\]

\[
P_2 = 1.6\,\mathrm{MW} \times 3.375 = 5.4\,\mathrm{MW}
\]

#### Official-style mark scheme breakdown
- **Part 1:**
  - **M1:** Clear substitution: \(P = Fv = (k v^2) v = k v^3\).
- **Part 2:**
  - **C1:** Calculation of \(k = \frac{1.6 \times 10^6}{40^3} = 25\).
  - **A1:** Correct base unit for \(k\): \(\mathrm{kg\,m^{-1}}\).
- **Part 3:**
  - **M1:** Using ratio \(\left(\frac{60}{40}\right)^3\) or substituting \(k = 25\) into \(P = 25 \times 60^3\).
  - **A1:** Correct power: \(5.4\,\mathrm{MW}\) (or \(5.4 \times 10^6\,\mathrm{W}\)).

#### Reasonableness check
Increasing the speed by a factor of \(1.5\) (a \(50\%\) increase from \(144\,\mathrm{km\,h^{-1}}\) to \(216\,\mathrm{km\,h^{-1}}\)) increases the power requirement by more than \(3.3\) times (from \(1.6\,\mathrm{MW}\) to \(5.4\,\mathrm{MW}\)). This accurately reflects real high-speed rail dynamics.

---

## Guided Practice

Work through this multi-step problem step by step to consolidate your problem-solving skills.

### Problem
A pump-storage hydroelectric station pumps water from a lower reservoir to an upper reservoir situated at a vertical height of \(42\,\mathrm{m}\) above the pump.

Water is transferred at a steady rate of \(0.25\,\mathrm{m^3}\) each second. The density of water is \(1000\,\mathrm{kg\,m^{-3}}\). The pump-motor system operates with an efficiency of \(78\%\).

Calculate:
1. The mass of water lifted each second.
2. The rate of gain of gravitational potential energy of the water (useful power output).
3. The electrical input power supplied to the pump motor.

---

### Step-by-step guidance

#### Step 1: Mass of water lifted each second
- Recall the density formula:
  \[
  m = \rho V
  \]
- For a time interval of \(t = 1.0\,\mathrm{s}\), volume is \(V = 0.25\,\mathrm{m^3}\):
  \[
  \frac{\Delta m}{\Delta t} = \rho \left(\frac{\Delta V}{\Delta t}\right) = 1000\,\mathrm{kg\,m^{-3}} \times 0.25\,\mathrm{m^3\,s^{-1}} = 250\,\mathrm{kg\,s^{-1}}
  \]
- Answer: **\(250\,\mathrm{kg\,s^{-1}}\)**.

#### Step 2: Useful power output
- The useful work done on the water is the gain in potential energy:
  \[
  \Delta W = (\Delta m) g h
  \]
- Divide by time to get the useful power:
  \[
  P_{\text{useful}} = \left(\frac{\Delta m}{\Delta t}\right) g h
  \]
- Substitute values (\(g = 9.81\,\mathrm{m\,s^{-2}}\), \(h = 42\,\mathrm{m}\)):
  \[
  P_{\text{useful}} = 250\,\mathrm{kg\,s^{-1}} \times 9.81\,\mathrm{m\,s^{-2}} \times 42\,\mathrm{m} = 103\,005\,\mathrm{W}
  \]
- Round to 2 significant figures: **\(100\,\mathrm{kW}\)** (or \(1.0 \times 10^5\,\mathrm{W}\); unrounded \(103\,\mathrm{kW}\)).

#### Step 3: Electrical input power
- Use the efficiency relationship:
  \[
  \eta = \frac{P_{\text{useful}}}{P_{\text{input}}} \implies P_{\text{input}} = \frac{P_{\text{useful}}}{\eta}
  \]
- Substitute \(P_{\text{useful}} = 103\,005\,\mathrm{W}\) and \(\eta = 0.78\):
  \[
  P_{\text{input}} = \frac{103\,005\,\mathrm{W}}{0.78} = 132\,058\,\mathrm{W}
  \]
- Round to 2 significant figures: **\(130\,\mathrm{kW}\)** (or \(1.3 \times 10^5\,\mathrm{W}\)).

---

## Checks for Understanding

### Check 1: Key relationship in the derivation of P = Fv

In the formal derivation of the equation relating mechanical power, force, and velocity (\(P = Fv\)), which relationship is substituted into the work formula \(W = Fs\)?

- **A.** \(\text{displacement} = \text{velocity} \times \text{time}\)
- **B.** \(\text{force} = \text{mass} \times \text{acceleration}\)

**Feedback for A:** Correct. The derivation begins with \(P = \frac{W}{t} = \frac{Fs}{t}\). Substituting \(s = vt\) (or \(\frac{s}{t} = v\)) gives \(P = Fv\).

**Feedback for B:** Incorrect. While \(F = ma\) is Newton's second law, it is not used in the derivation of \(P = Fv\). The equation \(P = Fv\) applies purely through the kinematic definition of velocity (\(v = \frac{s}{t}\)) and the definition of work done (\(W = Fs\)).

---

### Check 2: Calculating resistive force from power and speed

A motorboat travels across a calm lake at a steady velocity of \(12\,\mathrm{m\,s^{-1}}\). The engine delivers a useful output power of \(36\,\mathrm{kW}\) to the propeller. What is the magnitude of the total resistive force opposing the motion of the boat?

- **A.** \(3.0\,\mathrm{kN}\)
- **B.** \(432\,\mathrm{kN}\)

**Feedback for A:** Correct. At constant velocity, the forward driving thrust \(F\) equals the opposing resistive force. Rearranging \(P = Fv\) gives:
\[
F = \frac{P}{v} = \frac{36\,000\,\mathrm{W}}{12\,\mathrm{m\,s^{-1}}} = 3000\,\mathrm{N} = 3.0\,\mathrm{kN}
\]

**Feedback for B:** Incorrect. This result comes from mistakenly multiplying power by velocity (\(36 \times 12\)). To find force from power and speed, you must divide: \(F = \frac{P}{v}\).

---

### Check 3: Power scaling under quadratic drag

A racing cyclist notes that at high speed, the resistive force opposing motion is dominated by air drag, which is proportional to the square of her speed (\(F_{\text{drag}} \propto v^2\)). If she increases her speed from \(10\,\mathrm{m\,s^{-1}}\) to \(20\,\mathrm{m\,s^{-1}}\), by what factor must her mechanical power output increase?

- **A.** Factor of 8
- **B.** Factor of 4

**Feedback for A:** Correct. The speed is doubled: \(\frac{v_2}{v_1} = \frac{20}{10} = 2\). Because \(F \propto v^2\), the power is proportional to the cube of speed: \(P = Fv \propto v^3\). Therefore, the power required increases by a factor of \(2^3 = 8\).

**Feedback for B:** Incorrect. A factor of 4 (\(2^2 = 4\)) is the increase in the **drag force**. Because power is force multiplied by speed, you must multiply this fourfold increase in force by the doubled speed, giving an eightfold increase in power: \(4 \times 2 = 8\).

---

### Check 4: Car descending an incline at constant speed

A car of weight \(W\) travels down a hill inclined at angle \(\theta\) to the horizontal at a constant speed \(v\). The road friction and air resistance together produce an opposing force \(R\) directed up the slope. If \(W\sin\theta = R\), what is the useful power developed by the car's engine?

- **A.** \(0\,\mathrm{W}\)
- **B.** \(Rv\)

**Feedback for A:** Correct. The downward component of weight along the slope is \(W\sin\theta\). Because this exactly balances the opposing resistive force \(R\), the net force along the slope is zero without any assistance from the engine (\(F_{\text{drive}} = 0\)). The car coasts downhill at constant speed, so the engine delivers zero power.

**Feedback for B:** Incorrect. The resistive force is entirely overcome by the component of gravity acting down the incline (\(W\sin\theta\)). If the engine also provided a forward force equal to \(R\), the car would accelerate down the hill rather than moving at constant speed.

---

## Common Misconceptions

### Misconception 1: Believing zero resultant force means zero engine power
A very common student misunderstanding is:
"If a car travels at constant speed, the resultant force is zero (\(\Sigma F = 0\)). Therefore, the work done is zero and the power developed by the engine must be zero."
- **The reality:** The **net** force on the car is zero, so the **net** work done on the car is zero (the car does not gain kinetic energy).
- However, the engine exerts a real forward contact force \(F_{\text{drive}}\) that does positive work at a rate of \(P = F_{\text{drive}} v\).
- Simultaneously, resistive forces do negative work at an equal rate, dissipating energy as heat. The engine must supply power constantly to maintain motion against resistance.

---

### Misconception 2: Erroneously inserting a factor of 1/2 into P = Fv
Students often write \(P = \frac{1}{2}Fv\), confusing power with kinetic energy (\(E_K = \frac{1}{2}mv^2\)) or average velocity under uniform acceleration (\(\frac{u+v}{2}\)).
- **The reality:** Power is defined as \(P = \frac{W}{t} = \frac{Fs}{t} = Fv\). There is no factor of \(\frac{1}{2}\) in the formula.

---

### Misconception 3: Forgetting the component of weight on a slope
When calculating power on an incline, students frequently make two errors:
1. Forgetting gravity entirely and using only friction: \(P = R v\).
2. Using \(\cos\theta\) instead of \(\sin\theta\) for the slope component: writing \(mg\cos\theta\) instead of \(mg\sin\theta\).
- **The reality:** The component of weight acting along the incline parallel to the direction of motion is **always** \(mg\sin\theta\). The term \(mg\cos\theta\) is the component perpendicular to the slope.

---

### Misconception 4: Using non-SI units for speed without conversion
Exam questions often specify speed in \(\mathrm{km\,h^{-1}}\) or \(\mathrm{cm\,s^{-1}}\).
- **The error:** Substituting \(100\,\mathrm{km\,h^{-1}}\) directly into \(P = Fv\), resulting in an answer that is \(3.6\) times too large.
- **The correction:** Always convert to metres per second (\(\mathrm{m\,s^{-1}}\)):
  \[
  v = \frac{\text{speed in }\mathrm{km\,h^{-1}}}{3.6}
  \]

---

### Misconception 5: Assuming P is always proportional to v
Students often assume that doubling speed always doubles the power requirement.
- **The reality:** That is true **only** if the resistive force is constant (independent of speed).
- For objects moving through air or water at normal speeds, drag increases with speed (\(F \propto v^2\)), making power proportional to the cube of speed (\(P \propto v^3\)).

---

## Core Recap

- The mechanical power developed by a constant force \(F\) moving at velocity \(v\) in the direction of the force is:
  \[
  P = Fv
  \]
- **Derivation steps:**
  1. \(P = \frac{W}{t}\)
  2. \(W = Fs\)
  3. \(P = \frac{Fs}{t} = F\left(\frac{s}{t}\right)\)
  4. With \(v = \frac{s}{t}\), \(P = Fv\).
- If the force is applied at an angle \(\theta\) to the direction of velocity:
  \[
  P = Fv\cos\theta
  \]
- For a vehicle travelling on level ground at constant speed \(v\):
  \[
  F_{\text{drive}} = F_{\text{resist}} \implies P = F_{\text{resist}} v
  \]
- For a vehicle climbing an incline of angle \(\theta\) at constant speed \(v\):
  \[
  F_{\text{drive}} = R + mg\sin\theta \implies P = (R + mg\sin\theta) v
  \]
- When aerodynamic drag satisfies \(F_{\text{drag}} = k v^2\), power required to overcome drag obeys the cubic law:
  \[
  P = k v^3 \implies P \propto v^3
  \]
- For fluid pumps raising mass at rate \(\frac{\Delta m}{\Delta t}\) through height \(h\):
  \[
  P_{\text{useful}} = \left(\frac{\Delta m}{\Delta t}\right) g h = \rho \left(\frac{\Delta V}{\Delta t}\right) g h
  \]
- To find input power when efficiency \(\eta\) is known:
  \[
  P_{\text{input}} = \frac{P_{\text{useful}}}{\eta}
  \]
