# Kinetic Energy Derivation, Calculation and Application

## Learning Outcomes

By the end of this lesson, you should be able to:
- **Derive**, using the equations of motion, the formula for kinetic energy \(E_K = \frac{1}{2}mv^2\) (`9702_t05_m02_o03`).
- **Recall and use** the formula \(E_K = \frac{1}{2}mv^2\) in qualitative, quantitative, and graphical problem-solving (`9702_t05_m02_o04`).
- **Explain** the scalar nature of kinetic energy and why kinetic energy is always non-negative.
- **Analyze** the speed-squared relationship (\(E_K \propto v^2\)) and its physical consequences for vehicle stopping distances and acceleration work.
- **Apply** the principle of conservation of energy to problems involving the interchange between gravitational potential energy and kinetic energy, including cases with resistive forces.

---

## Prior Knowledge

To master this lesson, you should be familiar with the following concepts from earlier lessons:
- **Newton's second law of motion:** \(F = ma\), where \(F\) is the resultant force in newtons (\(\mathrm{N}\)), \(m\) is mass in kilograms (\(\mathrm{kg}\)), and \(a\) is acceleration in metres per second squared (\(\mathrm{m\,s^{-2}}\)) (Topic 3).
- **Constant-acceleration equation of motion:** \(v^2 = u^2 + 2as\), connecting initial velocity \(u\), final velocity \(v\), constant acceleration \(a\), and displacement \(s\) (Topic 2).
- **Work done by a constant force:** \(W = Fs\), where \(s\) is the displacement in the direction of the force (Module 5.1).
- **Gravitational potential energy change:** \(\Delta E_P = mg\Delta h\) in a uniform gravitational field (Lesson 5).
- **Principle of conservation of energy:** The total energy of an isolated system remains constant; energy transforms between kinetic, potential, and internal (thermal) forms (Module 5.1).

---

## Core Concepts

### What is Kinetic Energy?

Whenever a force accelerates an object from rest, work is done on that object. By the principle of conservation of energy, the mechanical work performed by the resultant force does not vanish; it is stored as the energy of motion of the body. We call this **kinetic energy**.

<a id="definition-9702_def_kinetic_energy"></a>

> **Definition to learn: kinetic energy.** energy that an object has because of its motion

Let us inspect the essential elements of this controlled definition:
- **Energy:** Like all forms of energy, kinetic energy is a **scalar quantity**. It is measured in the SI derived unit of **joules** (\(\mathrm{J}\)), where \(1\,\mathrm{J} = 1\,\mathrm{N\,m} = 1\,\mathrm{kg\,m^2\,s^{-2}}\).
- **Because of its motion:** Any object with non-zero speed possesses kinetic energy. A stationary object has zero kinetic energy.

### Scalar Nature of Kinetic Energy

A critical distinction between **velocity** (a vector) and **kinetic energy** (a scalar) is direction:
- Velocity \(\vec{v}\) has both magnitude (speed) and a specific spatial direction. Reversing the direction reverses the sign of velocity.
- In the kinetic energy formula, speed is squared: \(v^2 = (\vec{v} \cdot \vec{v})\).
- Because the square of any real number (positive or negative) is positive, and mass \(m > 0\), **kinetic energy is always non-negative**:
  \[
  E_K \ge 0
  \]
- For example, a car of mass \(1200\,\mathrm{kg}\) moving North at \(20\,\mathrm{m\,s^{-1}}\) and an identical car moving South at \(20\,\mathrm{m\,s^{-1}}\) have opposite velocities and opposite linear momenta, but their kinetic energies are **identical**:
  \[
  E_K = \frac{1}{2} \times 1200 \times 20^2 = 240\,000\,\mathrm{J}
  \]
  Direction in space does not alter kinetic energy.

### The Speed-Squared Relationship (\(E_K \propto v^2\))

Kinetic energy is directly proportional to mass (\(E_K \propto m\)) and directly proportional to the **square of the speed** (\(E_K \propto v^2\)):
- If the speed of an object is **doubled** (\(\times 2\)), its kinetic energy increases by a factor of \(2^2 = \mathbf{4}\) (it **quadruples**).
- If the speed is **tripled** (\(\times 3\)), its kinetic energy increases by a factor of \(3^2 = \mathbf{9}\) (a ninefold increase).
- Conversely, speed is proportional to the square root of kinetic energy: \(v \propto \sqrt{E_K}\).

This non-linear dependence explains why high-speed road collisions cause disproportionately severe damage, and why vehicle braking distances increase dramatically with small increases in speed.

---

## Detailed Mathematical Derivations

### Derivation of \(E_K = \frac{1}{2}mv^2\) from Equations of Motion

In Cambridge 9702 examinations, you may be explicitly asked to derive the formula for kinetic energy using the equations of motion and the definition of work done. The derivation proceeds in seven logical steps:

#### Step 1: Define the Physical Model
Consider a body of constant mass \(m\) moving along a straight horizontal line on a frictionless surface.
- The initial velocity of the body is \(u\).
- A constant resultant force \(F\) acts on the body in the direction of its motion over a displacement \(s\).
- Under this constant force, the body undergoes uniform acceleration \(a\).
- The final velocity of the body after displacement \(s\) is \(v\).

#### Step 2: Apply Newton's Second Law
Because the mass \(m\) is constant and the resultant force is \(F\), Newton's second law gives:
\[
F = ma
\]

#### Step 3: Write the Expression for Work Done
The force acts in the exact direction of displacement, so the work done \(W\) on the body by the resultant force is:
\[
W = Fs
\]
Substitute \(F = ma\):
\[
W = (ma)s = m(as)
\]

#### Step 4: Use the Constant-Acceleration Kinematic Equation
From kinematics (Topic 2), the equation connecting initial velocity \(u\), final velocity \(v\), uniform acceleration \(a\), and displacement \(s\) is:
\[
v^2 = u^2 + 2as
\]
Rearrange this equation to make the product \(as\) the subject:
\[
v^2 - u^2 = 2as
\]
\[
as = \frac{v^2 - u^2}{2}
\]

#### Step 5: Substitute \(as\) into the Work Equation
Substitute this expression for \(as\) into the work equation \(W = m(as)\):
\[
W = m\left(\frac{v^2 - u^2}{2}\right)
\]
Expand the brackets:
\[
W = \frac{1}{2}mv^2 - \frac{1}{2}mu^2
\]

#### Step 6: Interpret the Work-Energy Principle
The quantity \(\frac{1}{2}mv^2 - \frac{1}{2}mu^2\) represents the difference between the final kinetic energy and the initial kinetic energy:
\[
W = \Delta E_K = E_{K,\text{final}} - E_{K,\text{initial}}
\]
This fundamental result is known as the **work-energy theorem**: the net work done by all forces acting on a body equals the change in its kinetic energy.

#### Step 7: State the Expression for Kinetic Energy from Rest
If the body starts from rest, its initial velocity is zero (\(u = 0\)). The total work done to accelerate the body from rest to speed \(v\) is:
\[
W = \frac{1}{2}mv^2 - 0 = \frac{1}{2}mv^2
\]
Since the kinetic energy \(E_K\) possessed by a body at speed \(v\) is defined as the work done to accelerate it from rest to that speed:
\[
E_K = \frac{1}{2}mv^2
\]

<a id="formula-9702_formula_kinetic_energy"></a>

> **Formula to learn: Kinetic energy.**
>
> \[
> E_K = \frac{1}{2}mv^2
> \]

Where:
- \(E_K\) is the kinetic energy, measured in joules (\(\mathrm{J}\)).
- \(m\) is the mass of the body, measured in kilograms (\(\mathrm{kg}\)).
- \(v\) is the speed of the body, measured in metres per second (\(\mathrm{m\,s^{-1}}\)).

---

### Conditions and Limitations of Validity

The formula \(E_K = \frac{1}{2}mv^2\) is valid under two physical conditions:
1. **Constant mass:** The mass \(m\) must remain constant during the acceleration (no mass ejection, as occurs in rockets, or mass accretion).
2. **Non-relativistic speeds:** The speed \(v\) must be much less than the speed of light (\(v \ll c\), where \(c \approx 3.0 \times 10^8\,\mathrm{m\,s^{-1}}\)). At speeds approaching the speed of light, classical Newtonian mechanics breaks down and relativistic mechanics must be used. For all terrestrial and ordinary mechanical systems studied at AS Level, this classical formula is extraordinarily accurate.

---

### Useful Relationship: Kinetic Energy and Momentum

In Topic 3, you defined linear momentum as \(p = mv\). We can link kinetic energy and momentum directly:
\[
E_K = \frac{1}{2}mv^2 = \frac{m^2 v^2}{2m} = \frac{(mv)^2}{2m}
\]
\[
E_K = \frac{p^2}{2m} \quad \text{and} \quad p = \sqrt{2mE_K}
\]
This compact relationship is especially powerful in collision and nuclear physics problems where momentum is conserved.

---

## Worked Examples with Mark Schemes

### Worked Example 1: Speed-Squared Dependence and Braking Work

An electric delivery van of mass \(1500\,\mathrm{kg}\) travels on a straight horizontal test track.
1. Calculate the kinetic energy of the van when travelling at \(12.0\,\mathrm{m\,s^{-1}}\).
2. Calculate the kinetic energy of the van when its speed increases to \(24.0\,\mathrm{m\,s^{-1}}\).
3. Determine the additional work that the electric motors must do to accelerate the van from \(12.0\,\mathrm{m\,s^{-1}}\) to \(24.0\,\mathrm{m\,s^{-1}}\), and compare this to the work needed to reach the first \(12.0\,\mathrm{m\,s^{-1}}\) from rest.
4. When travelling at \(24.0\,\mathrm{m\,s^{-1}}\), the driver applies the brakes, providing a constant total retarding force of \(3600\,\mathrm{N}\). Calculate the minimum stopping distance.

#### Solution and Examination Mark Scheme

**Part 1: Kinetic energy at \(12.0\,\mathrm{m\,s^{-1}}\)**
- State the formula:
  \[
  E_K = \frac{1}{2}mv^2 \quad \text{[M1]}
  \]
- Substitute values:
  \[
  E_{K,1} = \frac{1}{2} \times 1500\,\mathrm{kg} \times (12.0\,\mathrm{m\,s^{-1}})^2 = 750 \times 144 = 108\,000\,\mathrm{J}
  \]
  \[
  E_{K,1} = 1.08 \times 10^5\,\mathrm{J} \quad (\text{or } 108\,\mathrm{kJ}) \quad \text{[A1]}
  \]

**Part 2: Kinetic energy at \(24.0\,\mathrm{m\,s^{-1}}\)**
- Substitute \(v = 24.0\,\mathrm{m\,s^{-1}}\):
  \[
  E_{K,2} = \frac{1}{2} \times 1500\,\mathrm{kg} \times (24.0\,\mathrm{m\,s^{-1}})^2 = 750 \times 576 = 432\,000\,\mathrm{J}
  \]
  \[
  E_{K,2} = 4.32 \times 10^5\,\mathrm{J} \quad (\text{or } 432\,\mathrm{kJ}) \quad \text{[A1]}
  \]
  Notice that doubling the speed from \(12\,\mathrm{m\,s^{-1}}\) to \(24\,\mathrm{m\,s^{-1}}\) multiplied the kinetic energy by exactly 4:
  \[
  \frac{432\,\mathrm{kJ}}{108\,\mathrm{kJ}} = 4.0
  \]

**Part 3: Additional work required**
- The additional work required is the change in kinetic energy:
  \[
  W_{\text{additional}} = \Delta E_K = E_{K,2} - E_{K,1} \quad \text{[M1]}
  \]
  \[
  W_{\text{additional}} = 432\,000\,\mathrm{J} - 108\,000\,\mathrm{J} = 324\,000\,\mathrm{J} = 3.24 \times 10^5\,\mathrm{J} \quad (\text{or } 324\,\mathrm{kJ}) \quad \text{[A1]}
  \]
- Comparison:
  \[
  \frac{W_{\text{additional}}}{W_{\text{0 to 12}}} = \frac{324\,\mathrm{kJ}}{108\,\mathrm{kJ}} = 3.0 \quad \text{[B1]}
  \]
  Accelerating from \(12\,\mathrm{m\,s^{-1}}\) to \(24\,\mathrm{m\,s^{-1}}\) requires **three times more work** than accelerating from rest to \(12\,\mathrm{m\,s^{-1}}\), even though the speed increase is the same (\(+12\,\mathrm{m\,s^{-1}}\)).

**Part 4: Minimum stopping distance**
- Work done by braking force equals the kinetic energy dissipated:
  \[
  W = F_{\text{brake}} s = E_{K,2} \quad \text{[M1]}
  \]
  \[
  s = \frac{E_{K,2}}{F_{\text{brake}}} = \frac{432\,000\,\mathrm{J}}{3600\,\mathrm{N}} = 120\,\mathrm{m} \quad \text{[A1]}
  \]
  (By comparison, stopping from \(12.0\,\mathrm{m\,s^{-1}}\) would require only \(\frac{108\,000}{3600} = 30\,\mathrm{m}\). Doubling the speed quadrupled the braking distance from \(30\,\mathrm{m}\) to \(120\,\mathrm{m}\).)

---

### Worked Example 2: Interchange of Potential and Kinetic Energy with Air Resistance

A skydiver of mass \(80.0\,\mathrm{kg}\) falls from rest from a stationary helicopter at an altitude of \(450\,\mathrm{m}\). Upon reaching an altitude of \(150\,\mathrm{m}\), the skydiver's speed is measured to be \(52.0\,\mathrm{m\,s^{-1}}\).

Calculate:
1. The loss in gravitational potential energy of the skydiver over this descent.
2. The kinetic energy of the skydiver at altitude \(150\,\mathrm{m}\).
3. The speed the skydiver would have reached if air resistance had been completely negligible.
4. The average resistive drag force exerted by the air on the skydiver during this fall.

#### Solution and Examination Mark Scheme

**Part 1: Loss in gravitational potential energy**
- Vertical displacement:
  \[
  \Delta h = 450\,\mathrm{m} - 150\,\mathrm{m} = 300\,\mathrm{m} \quad \text{[M1]}
  \]
- Loss in \(E_P\):
  \[
  \Delta E_P = mg\Delta h = 80.0\,\mathrm{kg} \times 9.81\,\mathrm{m\,s^{-2}} \times 300\,\mathrm{m} = 235\,440\,\mathrm{J}
  \]
  \[
  \text{Loss in } E_P = 2.35 \times 10^5\,\mathrm{J} \quad (\text{or } 235\,\mathrm{kJ}) \quad \text{[A1]}
  \]

**Part 2: Actual kinetic energy**
- Use \(E_K = \frac{1}{2}mv^2\):
  \[
  E_K = \frac{1}{2} \times 80.0\,\mathrm{kg} \times (52.0\,\mathrm{m\,s^{-1}})^2 = 40.0 \times 2704 = 108\,160\,\mathrm{J} \quad \text{[M1]}
  \]
  \[
  E_K = 1.08 \times 10^5\,\mathrm{J} \quad (\text{or } 108\,\mathrm{kJ}) \quad \text{[A1]}
  \]

**Part 3: Theoretical speed with no air resistance**
- If air resistance is negligible, all lost potential energy converts to kinetic energy:
  \[
  \frac{1}{2}mv^2 = mg\Delta h \implies v = \sqrt{2g\Delta h} \quad \text{[M1]}
  \]
  \[
  v = \sqrt{2 \times 9.81\,\mathrm{m\,s^{-2}} \times 300\,\mathrm{m}} = \sqrt{5886} = 76.72\,\mathrm{m\,s^{-1}}
  \]
  \[
  v = 76.7\,\mathrm{m\,s^{-1}} \quad \text{[A1]}
  \]

**Part 4: Average resistive force**
- Apply conservation of energy: the difference between potential energy lost and kinetic energy gained is the work done against air drag:
  \[
  W_{\text{drag}} = \Delta E_P - E_K \quad \text{[M1]}
  \]
  \[
  W_{\text{drag}} = 235\,440\,\mathrm{J} - 108\,160\,\mathrm{J} = 127\,280\,\mathrm{J}
  \]
- Relate work to average force over the vertical descent of \(300\,\mathrm{m}\):
  \[
  W_{\text{drag}} = F_{\text{drag}} \times \Delta h \implies F_{\text{drag}} = \frac{W_{\text{drag}}}{\Delta h} \quad \text{[M1]}
  \]
  \[
  F_{\text{drag}} = \frac{127\,280\,\mathrm{J}}{300\,\mathrm{m}} = 424.3\,\mathrm{N}
  \]
  \[
  F_{\text{drag}} = 424\,\mathrm{N} \quad \text{[A1]}
  \]

---

### Worked Example 3: Ratio and Proportional Reasoning

A laboratory cart of mass \(M\) is launched down a test ramp.
- On a frictionless trial, the kinetic energy of the cart at the bottom is \(E_1 = 320\,\mathrm{J}\).
- On a rough trial with surface friction, the kinetic energy at the bottom is reduced to \(E_2 = 180\,\mathrm{J}\).

1. Determine the numerical ratio \(\frac{E_2}{E_1}\).
2. Calculate the ratio \(\frac{v_2}{v_1}\) of the speeds of the cart at the bottom of the ramp.
3. If the speed on the frictionless trial was \(v_1 = 8.0\,\mathrm{m\,s^{-1}}\), calculate the speed \(v_2\) on the rough trial.

#### Solution and Examination Mark Scheme

**Part 1: Ratio of kinetic energies**
- Calculate direct ratio:
  \[
  \frac{E_2}{E_1} = \frac{180\,\mathrm{J}}{320\,\mathrm{J}} = \frac{9}{16} = 0.5625 \approx 0.563 \quad \text{[B1]}
  \]

**Part 2: Ratio of speeds**
- Relate speed to kinetic energy:
  \[
  E_K = \frac{1}{2}mv^2 \implies v = \sqrt{\frac{2E_K}{m}} \quad \text{[M1]}
  \]
- Since mass \(m\) is identical in both trials:
  \[
  \frac{v_2}{v_1} = \sqrt{\frac{E_2}{E_1}} \quad \text{[M1]}
  \]
  \[
  \frac{v_2}{v_1} = \sqrt{\frac{9}{16}} = \frac{3}{4} = 0.75 \quad \text{[A1]}
  \]

**Part 3: Calculation of \(v_2\)**
- Multiply by \(v_1\):
  \[
  v_2 = 0.75 \times 8.0\,\mathrm{m\,s^{-1}} = 6.0\,\mathrm{m\,s^{-1}} \quad \text{[A1]}
  \]

---

## Guided Practice

### Problem 1: Rollercoaster Energy Transformation

A rollercoaster train and passengers have a combined mass of \(850\,\mathrm{kg}\). The train is released from rest at point A at the top of a hill of height \(35.0\,\mathrm{m}\) above the ground. It travels along a curved track of total length \(92.0\,\mathrm{m}\) to reach point B at ground level (\(h = 0\)). An average resistive force of \(220\,\mathrm{N}\) opposes the motion along the track.

**Task:**
1. Calculate the loss in gravitational potential energy between point A and point B.
2. Calculate the work done against the resistive force along the track.
3. Calculate the kinetic energy of the train at point B.
4. Calculate the speed of the train at point B.

#### Step-by-Step Guidance:
- **Step 1:** Use \(\Delta E_P = mg\Delta h\):
  \[
  \Delta E_P = 850\,\mathrm{kg} \times 9.81\,\mathrm{m\,s^{-2}} \times 35.0\,\mathrm{m} = 291\,847.5\,\mathrm{J} \approx 2.92 \times 10^5\,\mathrm{J} \quad (\text{or } 292\,\mathrm{kJ})
  \]
- **Step 2:** Use \(W = Fs\) along the track (using track length \(92.0\,\mathrm{m}\)):
  \[
  W_f = 220\,\mathrm{N} \times 92.0\,\mathrm{m} = 20\,240\,\mathrm{J} \approx 2.02 \times 10^4\,\mathrm{J} \quad (\text{or } 20.2\,\mathrm{kJ})
  \]
- **Step 3:** Apply conservation of energy (\(E_{K,B} = \Delta E_P - W_f\)):
  \[
  E_{K,B} = 291\,847.5\,\mathrm{J} - 20\,240\,\mathrm{J} = 271\,607.5\,\mathrm{J} \approx 2.72 \times 10^5\,\mathrm{J} \quad (\text{or } 272\,\mathrm{kJ})
  \]
- **Step 4:** Rearrange \(E_K = \frac{1}{2}mv^2\) for speed:
  \[
  v = \sqrt{\frac{2 E_K}{m}} = \sqrt{\frac{2 \times 271\,607.5\,\mathrm{J}}{850\,\mathrm{kg}}} = \sqrt{639.08} = 25.28\,\mathrm{m\,s^{-1}}
  \]
  Report to 3 significant figures: \(v = 25.3\,\mathrm{m\,s^{-1}}\).

---

### Problem 2: Kinetic Energy of a High-Pressure Fluid Jet

A horizontal industrial water jet cutter issues water at a constant speed of \(450\,\mathrm{m\,s^{-1}}\) through a circular nozzle of cross-sectional area \(3.00 \times 10^{-7}\,\mathrm{m^2}\). The density of water is \(1.00 \times 10^3\,\mathrm{kg\,m^{-3}}\).

**Task:**
1. Calculate the mass of water discharged per second (the mass flow rate).
2. Calculate the kinetic energy carried by the water discharged in one second (the kinetic power of the jet).
3. If the cutter runs continuously for \(5.00\,\mathrm{minutes}\), calculate the total kinetic energy delivered.

#### Step-by-Step Guidance:
- **Step 1:** In one second, the jet forms a water cylinder of length \(L = 450\,\mathrm{m}\).
  \[
  \text{Volume per second} = A \times v = (3.00 \times 10^{-7}\,\mathrm{m^2}) \times (450\,\mathrm{m\,s^{-1}}) = 1.35 \times 10^{-4}\,\mathrm{m^3\,s^{-1}}
  \]
  \[
  \frac{\Delta m}{\Delta t} = \rho A v = (1.00 \times 10^3\,\mathrm{kg\,m^{-3}}) \times (1.35 \times 10^{-4}\,\mathrm{m^3\,s^{-1}}) = 0.135\,\mathrm{kg\,s^{-1}}
  \]
- **Step 2:** Calculate kinetic energy per second:
  \[
  P = \frac{\Delta E_K}{\Delta t} = \frac{1}{2} \left(\frac{\Delta m}{\Delta t}\right) v^2
  \]
  \[
  P = \frac{1}{2} \times 0.135\,\mathrm{kg\,s^{-1}} \times (450\,\mathrm{m\,s^{-1}})^2 = 0.0675 \times 202\,500 = 13\,668.75\,\mathrm{W} \approx 1.37 \times 10^4\,\mathrm{W} \quad (\text{or } 13.7\,\mathrm{kW})
  \]
- **Step 3:** Total energy in \(5.00\,\mathrm{minutes}\) (\(300\,\mathrm{s}\)):
  \[
  E_{\text{total}} = P \times t = 13\,668.75\,\mathrm{W} \times 300\,\mathrm{s} = 4.10 \times 10^6\,\mathrm{J} \quad (\text{or } 4.10\,\mathrm{MJ})
  \]

---

## Checks for Understanding with Explanations

### Check 1: Speed Increase and Kinetic Energy Factor

A car travelling along a straight highway increases its speed from \(15\,\mathrm{m\,s^{-1}}\) to \(30\,\mathrm{m\,s^{-1}}\).

By what factor does the kinetic energy of the car increase?

- **A.** The kinetic energy doubles (increases by a factor of 2).
- **B.** The kinetic energy quadruples (increases by a factor of 4).

**Feedback for A:** Incorrect. Kinetic energy is proportional to the **square** of speed, not speed itself. Doubling speed does not double kinetic energy.

**Feedback for B:** Correct. \(E_K = \frac{1}{2}mv^2\). When speed changes from \(v\) to \(2v\), the new kinetic energy is \(E_{K,\text{new}} = \frac{1}{2}m(2v)^2 = \frac{1}{2}m(4v^2) = 4 E_K\). The kinetic energy increases by a factor of 4.

---

### Check 2: Algebraic Evaluation of Kinetic Energy Change

A lorry of mass \(2000\,\mathrm{kg}\) speeds up from \(10\,\mathrm{m\,s^{-1}}\) to \(20\,\mathrm{m\,s^{-1}}\). A student calculates the work done on the lorry using the formula:
\[
W = \frac{1}{2}m(v - u)^2 = \frac{1}{2} \times 2000 \times (20 - 10)^2 = 1000 \times 100 = 1.0 \times 10^5\,\mathrm{J}
\]

Is this calculation correct?

- **A.** Yes, because the change in speed is \(\Delta v = 10\,\mathrm{m\,s^{-1}}\), and substituting \(\Delta v\) into \(\frac{1}{2}m(\Delta v)^2\) gives the energy change.
- **B.** No, because the change in kinetic energy is \(\frac{1}{2}mv^2 - \frac{1}{2}mu^2\), which gives \(3.0 \times 10^5\,\mathrm{J}\).

**Feedback for A:** Incorrect. This is one of the most common algebraic mistakes in mechanics. In algebra, \((v - u)^2 \neq v^2 - u^2\). Expanding \((v - u)^2\) gives \(v^2 - 2vu + u^2\), which is completely different from \(v^2 - u^2\). You must always calculate final \(E_K\) and initial \(E_K\) separately and subtract them.

**Feedback for B:** Correct. \(\Delta E_K = \frac{1}{2}mv^2 - \frac{1}{2}mu^2 = \frac{1}{2} \times 2000 \times (20^2 - 10^2) = 1000 \times (400 - 100) = 1000 \times 300 = 3.0 \times 10^5\,\mathrm{J}\). The incorrect formula underestimated the work by a factor of 3.

---

### Check 3: Kinetic Energy of Opposing Bodies

Two identical ice-hockey pucks, each of mass \(0.16\,\mathrm{kg}\), slide towards each other along a straight line on a frictionless ice rink. Puck 1 moves East at \(15\,\mathrm{m\,s^{-1}}\) and Puck 2 moves West at \(15\,\mathrm{m\,s^{-1}}\).

What is the total kinetic energy of the two pucks?

- **A.** \(0\,\mathrm{J}\), because the velocities are equal and opposite, so the two energies cancel out.
- **B.** \(36\,\mathrm{J}\), because kinetic energy is a scalar quantity and cannot be negative.

**Feedback for A:** Incorrect. You are thinking of **linear momentum**, which is a vector: \(\Sigma p = (+0.16 \times 15) + (-0.16 \times 15) = 0\,\mathrm{kg\,m\,s^{-1}}\). But kinetic energy is a **scalar**, not a vector. Energy has no direction and cannot cancel out due to opposing velocities.

**Feedback for B:** Correct. For each puck: \(E_K = \frac{1}{2}mv^2 = \frac{1}{2} \times 0.16 \times 15^2 = 0.08 \times 225 = 18\,\mathrm{J}\). Total kinetic energy is \(E_{K,\text{total}} = 18\,\mathrm{J} + 18\,\mathrm{J} = 36\,\mathrm{J}\).

---

### Check 4: Estimation of Kinetic Energy

A high school athlete of mass \(60\,\mathrm{kg}\) runs in a \(100\,\mathrm{m}\) sprint race at a steady speed of \(9.0\,\mathrm{m\,s^{-1}}\).

Which value gives the correct order of magnitude for the athlete's kinetic energy?

- **A.** Approximately \(2.4 \times 10^3\,\mathrm{J}\) (order of magnitude \(10^3\,\mathrm{J}\)).
- **B.** Approximately \(2.4 \times 10^2\,\mathrm{J}\) (order of magnitude \(10^2\,\mathrm{J}\)).

**Feedback for A:** Correct. \(E_K = \frac{1}{2}mv^2 = \frac{1}{2} \times 60\,\mathrm{kg} \times (9.0\,\mathrm{m\,s^{-1}})^2 = 30 \times 81 = 2430\,\mathrm{J} \approx 2.4 \times 10^3\,\mathrm{J}\). The order of magnitude is \(10^3\,\mathrm{J}\) (a few kilojoules), which matches authentic Cambridge estimation questions for human movement.

**Feedback for B:** Incorrect. This would correspond to forgetting to square the speed: \(\frac{1}{2} \times 60 \times 9.0 = 270\,\mathrm{J}\). Always remember to square the speed.

---

## Common Misconceptions

### Misconception 1: Calculating \(\Delta E_K\) as \(\frac{1}{2}m(\Delta v)^2\)
Students often calculate \(\Delta E_K\) by first finding the change in speed \(\Delta v = v - u\) and then writing \(\frac{1}{2}m(\Delta v)^2\).
- **Correction:** The correct formula is \(\Delta E_K = \frac{1}{2}mv^2 - \frac{1}{2}mu^2 = \frac{1}{2}m(v^2 - u^2)\).
- Mathematically, \((v - u)^2 = v^2 - 2uv + u^2 \neq v^2 - u^2\). The term \(-2uv\) creates a major error unless \(u = 0\).

### Misconception 2: Treating Kinetic Energy as a Vector
Students sometimes assign a negative sign to kinetic energy when an object moves to the left or downward.
- **Correction:** Kinetic energy is strictly a **scalar**. Speed is squared, so \(E_K\) is always positive (or zero when stationary). It has magnitude and units, but zero direction.

### Misconception 3: Believing Doubling Speed Doubles Braking Distance
A very common real-world misconception is that travelling twice as fast requires twice the braking distance.
- **Correction:** By the work-energy theorem, braking work equals initial kinetic energy: \(F_{\text{brake}} \times s = \frac{1}{2}mv^2\). For a constant braking force \(F_{\text{brake}}\), the stopping distance is:
  \[
  s = \frac{mv^2}{2 F_{\text{brake}}} \propto v^2
  \]
- Doubling speed **quadruples** the stopping distance (\(2^2 = 4\)). Tripling speed increases stopping distance by a factor of 9.

### Misconception 4: Confusing Kinetic Energy with Momentum
Students often confuse \(E_K = \frac{1}{2}mv^2\) with \(p = mv\).
- **Correction:**
  - Momentum is a vector; kinetic energy is a scalar.
  - In an explosion from rest, total momentum remains zero (\(\Sigma p = 0\)), but total kinetic energy increases dramatically (\(\Sigma E_K > 0\)).
  - Momentum is proportional to speed (\(p \propto v\)); kinetic energy is proportional to speed squared (\(E_K \propto v^2\)).

### Misconception 5: Forgetting Units and Prefixes
Students often report kinetic energy without converting mass from grams to kilograms or speed from \(\mathrm{km\,h^{-1}}\) to \(\mathrm{m\,s^{-1}}\).
- **Correction:**
  - Convert mass: \(1\,\mathrm{g} = 10^{-3}\,\mathrm{kg}\).
  - Convert speed: to convert from \(\mathrm{km\,h^{-1}}\) to \(\mathrm{m\,s^{-1}}\), divide by \(3.6\) (since \(1\,\mathrm{km\,h^{-1}} = \frac{1000\,\mathrm{m}}{3600\,\mathrm{s}} = \frac{1}{3.6}\,\mathrm{m\,s^{-1}}\)).

---

## Core Recap

- **Kinetic energy** is the energy that an object has because of its motion. It is a scalar quantity measured in joules (\(\mathrm{J}\)).
- **Derivation steps:**
  1. Resultant force: \(F = ma\).
  2. Work done: \(W = Fs = m(as)\).
  3. Equation of motion: \(v^2 = u^2 + 2as \implies as = \frac{v^2 - u^2}{2}\).
  4. Substitution: \(W = \frac{1}{2}mv^2 - \frac{1}{2}mu^2 = \Delta E_K\).
  5. From rest (\(u = 0\)): \(E_K = \frac{1}{2}mv^2\).
- **Conditions:** Valid for constant mass and non-relativistic speeds (\(v \ll c\)).
- **Speed-squared relationship:** \(E_K \propto v^2\). Doubling speed quadruples kinetic energy and quadruples braking distance for constant braking force.
- **Change in kinetic energy:** Always calculate as \(\Delta E_K = \frac{1}{2}m(v^2 - u^2)\), never as \(\frac{1}{2}m(v - u)^2\).
- **Energy conservation:** In a gravitational descent without friction, \(\Delta E_K = -\Delta E_P \implies \frac{1}{2}mv^2 = mg\Delta h \implies v = \sqrt{2g\Delta h}\). When friction acts, \(\Delta E_P = \Delta E_K + W_{\text{resistive}}\).
- **Topic 5 Complete:** You have now mastered Work, Energy, and Power across both modules: work, energy conservation, power, efficiency, gravitational potential energy, and kinetic energy.
