# Work Done by a Force and Work Done by an Expanding Gas

## Learning Outcomes

In this lesson, you will learn to:

- Understand the concept of work as the mechanical transfer of energy.
- Recall and use the definition of work done as the product of force and displacement in the direction of the force.
- Calculate work done by a constant force acting at an angle to the direction of motion using \(W = Fs \cos\theta\).
- Interpret the physical meaning of positive, negative, and zero work.
- Determine work done from the area under a force-displacement graph.
- Derive and use the expression for work done by an expanding gas at constant pressure: \(W = p\Delta V\).
- Distinguish between work done by a gas and work done on a gas.
- Apply the principle of conservation of energy in the context of mechanical energy transfers.

---

## Prior Knowledge

Before beginning this lesson, you should be confident with:

- **Vectors and scalars:** Identifying vectors (force, displacement, velocity) and scalars (energy, distance, speed).
- **Resolving vectors:** Splitting a vector into two mutually perpendicular components using basic trigonometry:
  \[
  F_x = F \cos\theta \quad \text{and} \quad F_y = F \sin\theta
  \]
- **Resultant force and equilibrium:** Newton's first and second laws of motion from Topic 3, where \(\Sigma F = ma\).
- **Pressure:** The definition of pressure as force per unit normal area from Topic 4:
  \[
  p = \frac{F}{A}
  \]

---

## Core Concepts

### 1. What is work in physics?

In everyday conversation, the word "work" is used loosely. You might say you are working when you study for an exam, hold a heavy box in your arms without moving, or sit typing at a computer desk.

In physics, **work** has a precise mathematical and physical meaning:

Work is done only when a **force** causes an object to undergo a **displacement** along, or partially along, the line of action of that force.

If you push against a rigid brick wall with all your strength for an hour, your muscles will feel exhausted, and you will have consumed biochemical energy. However, because the wall does not move (\(s = 0\)), the mechanical work done on the wall is exactly **zero**.

Whenever a force does work on an object, **energy is transferred** mechanically from one system to another. The amount of work done is equal to the quantity of energy transferred:

\[
W = \Delta E
\]

---

### 2. Defining work done

In Cambridge International AS Level Physics, work done by a constant force is defined formally as:

<a id="definition-9702_def_work_done"></a>

> **Definition to learn: work done.** product of force and displacement in the direction of the force

Every word in this definition is critical:
- **Product:** Work involves mathematical multiplication of force and displacement.
- **Force:** The magnitude of the force applied to the body.
- **Displacement in the direction of the force:** It is not sufficient to multiply force by any distance. You must multiply the force by the component of displacement parallel to that force (or equivalently, multiply displacement by the component of force parallel to the displacement).

Work is a **scalar quantity**. Even though it is calculated from two vectors (force and displacement), work has magnitude and sign, but no spatial direction.

The SI unit of work is the **joule**, abbreviated \(\mathrm{J}\).

<a id="formula-9702_formula_work"></a>

> **Formula to learn: Work done by a constant force.**
>
> \[
> W = Fs
> \]

One joule is defined as the work done when a force of one newton moves its point of application through a displacement of one metre in the direction of the force:

\[
1\,\mathrm{J} = 1\,\mathrm{N}\times 1\,\mathrm{m} = 1\,\mathrm{N\,m} = 1\,\mathrm{kg\,m^2\,s^{-2}}
\]

---

### 3. Force acting at an angle to the displacement

In many realistic scenarios, the applied force does not act along the exact line of motion. Consider pulling a suitcase on wheels along a level floor by an inclined handle, or pulling a sled with a rope angled upwards.

Suppose a constant force \(F\) acts at an angle \(\theta\) to the direction of horizontal displacement \(s\).

To find the work done, resolve the force \(F\) into two perpendicular components:
1. **Parallel component:** \(F_{\parallel} = F \cos\theta\), acting parallel to the displacement.
2. **Perpendicular component:** \(F_{\perp} = F \sin\theta\), acting perpendicular to the displacement.

Because there is no displacement in the perpendicular direction, the perpendicular component does zero work. Only the parallel component transfers mechanical energy along the direction of motion.

Therefore, the general formula for work done by a constant force is:

\[
W = (F \cos\theta) s = Fs \cos\theta
\]

where:
- \(W\) is the work done, measured in joules (\(\mathrm{J}\)).
- \(F\) is the magnitude of the applied force, measured in newtons (\(\mathrm{N}\)).
- \(s\) is the magnitude of the displacement, measured in metres (\(\mathrm{m}\)).
- \(\theta\) is the angle between the force vector and the displacement vector.

#### Evaluating different angles (\(\theta\))

The factor \(\cos\theta\) determines both the magnitude and the sign of the work done:

1. **Force in the same direction as motion (\(\theta = 0^\circ\)):**
   \[
   \cos 0^\circ = 1 \implies W = +Fs
   \]
   Maximum positive work is done. Energy is transferred to the body (for example, accelerating a car forward).

2. **Acute angle (\(0^\circ < \theta < 90^\circ\)):**
   \[
   \cos\theta > 0 \implies W > 0
   \]
   Positive work is done. A component of the force assists the motion.

3. **Force perpendicular to motion (\(\theta = 90^\circ\)):**
   \[
   \cos 90^\circ = 0 \implies W = 0
   \]
   **Zero work is done.** When a force acts perpendicular to the displacement, it cannot change the kinetic energy or do work on the object. Key examples include:
   - The normal contact force exerted by a horizontal floor on a sliding box.
   - The downward weight of an object when it moves horizontally.
   - The tension in a string providing the centripetal force for an object moving in a circle at constant speed.
   - Carrying a heavy bag horizontally at constant speed: the upward lifting force is at \(90^\circ\) to the horizontal displacement, so the lifting force does zero work on the bag.

4. **Obtuse angle (\(90^\circ < \theta < 180^\circ\)):**
   \[
   \cos\theta < 0 \implies W < 0
   \]
   Negative work is done. A component of the force opposes the motion.

5. **Force directly opposite to motion (\(\theta = 180^\circ\)):**
   \[
   \cos 180^\circ = -1 \implies W = -Fs
   \]
   Work done is negative. Energy is removed from the mechanical kinetic store of the body and transferred to other stores (for example, kinetic friction transferring energy to thermal energy in the surfaces and surroundings).

---

### 4. Work done represented on a force-displacement graph

When a force is constant, plotting force \(F\) on the vertical axis against displacement \(s\) on the horizontal axis produces a horizontal straight line. The work done is given by:

\[
W = F \times s = \text{height} \times \text{base} = \text{area of the rectangle}
\]

What happens if the force varies as the object moves? For example, stretching a spring requires a force that increases linearly with extension (\(F = kx\)), or a rocket engine whose thrust varies with altitude.

In all cases:

\[
\text{Work done} = \text{area under the force against displacement graph}
\]

- For a force that increases linearly from \(0\) to a maximum value \(F_{\mathrm{max}}\) over displacement \(s\), the area is a triangle:
  \[
  W = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} F_{\mathrm{max}} s
  \]
- For a force that changes in steps or along straight segments, divide the region into rectangles and triangles, calculate each area separately, and sum them to obtain the total work done.

---

### 5. Work done by an expanding gas

Gases exert pressure on the walls of any container that encloses them. When a gas expands against an external resistance (such as a movable piston in a car engine cylinder or an expanding balloon), it exerts a force that moves through a distance. Therefore, the gas does mechanical work on its surroundings.

Consider a gas at uniform pressure \(p\) contained in a cylindrical chamber fitted with a frictionless, movable piston of cross-sectional area \(A\).

```
        |<------- delta x ------->|
+-------+-------------------------+
|  Gas  |         Piston          |
|  at   |=======>                 |===>
|  p    |   F = pA                |
+-------+-------------------------+
        |<------- Area A -------->|
```

1. The gas exerts a force \(F\) perpendicularly against the inner face of the piston. From the definition of pressure (\(p = F / A\)):
   \[
   F = pA
   \]
2. Suppose the gas expands slowly at constant pressure \(p\), pushing the piston outward through a displacement \(\Delta x\).
3. The mechanical work done by the gas is:
   \[
   W = F \Delta x = (pA) \Delta x
   \]
4. The product of cross-sectional area \(A\) and displacement \(\Delta x\) is the increase in volume of the gas, \(\Delta V\):
   \[
   A \Delta x = \Delta V = V_{\mathrm{final}} - V_{\mathrm{initial}}
   \]
5. Substituting \(\Delta V\) into the work expression yields:

<a id="formula-9702_formula_work_done_gas_expansion"></a>

> **Formula to learn: Work done by expanding gas at constant pressure.**
>
> \[
> W = p\Delta V
> \]

where:
- \(W\) is the work done, in joules (\(\mathrm{J}\)).
- \(p\) is the constant pressure of the gas, in pascals (\(\mathrm{Pa}\) or \(\mathrm{N\,m^{-2}}\)).
- \(\Delta V\) is the change in volume of the gas, in cubic metres (\(\mathrm{m^3}\)).

#### Important conventions for gas work

- **Gas expansion (\(V_{\mathrm{final}} > V_{\mathrm{initial}}\), \(\Delta V > 0\)):**
  The gas pushes outward in the same direction as the displacement of the boundary.
  **Work is done BY the gas on the surroundings.**
  The gas loses energy (or must absorb heat from outside) to perform this work.
- **Gas compression (\(V_{\mathrm{final}} < V_{\mathrm{initial}}\), \(\Delta V < 0\)):**
  An external force pushes the piston inward against the gas pressure.
  **Work is done ON the gas by the surroundings.**
  Mechanical energy is transferred into the gas, increasing its internal energy unless heat escapes.

#### Graphical representation on a \(p-V\) diagram

If pressure \(p\) is plotted on the vertical axis and volume \(V\) on the horizontal axis:
- At constant pressure, the graph is a horizontal line. The area under the line between \(V_1\) and \(V_2\) is a rectangle of height \(p\) and width \(\Delta V\).
- The area under a \(p-V\) graph represents the work done during the change in volume:
  \[
  \text{Work done} = \text{area under the } p-V \text{ graph}
  \]

---

### 6. Mechanical work and the principle of conservation of energy

Energy is a scalar quantity that measures the capacity of a system to do work. The **principle of conservation of energy** is one of the grand unifying laws of physics:

> Energy cannot be created or destroyed; it can only be transformed from one form to another, but the total amount of energy in an isolated system remains constant.

When an external force does work on a body:
- If a resultant force accelerates an object on a frictionless surface, the work done equals the gain in kinetic energy: \(W_{\mathrm{net}} = \Delta E_K\).
- If an object is lifted vertically at constant speed, the work done by the lifting force equals the gain in gravitational potential energy: \(W = \Delta E_P = mg\Delta h\).
- If an object is pulled against friction at constant speed, the work done by the pulling force equals the work done against friction, which is transferred into internal thermal energy of the surfaces and surrounding air. Total energy is conserved: mechanical energy supplied = thermal energy produced.

---

## Worked Examples

### Worked example 1: Pulling a crate at an angle across a rough floor

A worker pulls a heavy wooden crate of mass \(40\,\mathrm{kg}\) along a horizontal concrete floor. The worker applies a constant tension force \(T = 160\,\mathrm{N}\) through a rope inclined at an angle of \(30^\circ\) above the horizontal. The crate moves a distance of \(15\,\mathrm{m}\) in a straight line at constant velocity.

```
       T = 160 N
         ^
          \
           \  30°
            +---------> displacement s = 15 m
         [CRATE]
```

Calculate:
1. The work done on the crate by the tension in the rope.
2. The work done on the crate by its weight and by the normal contact force from the floor.
3. The frictional force opposing the motion and the work done against friction.

#### Strategy and model check
- The crate moves horizontally with constant velocity, so the resultant horizontal force is zero (\(\Sigma F_x = 0\)).
- The displacement is horizontal: \(s = 15\,\mathrm{m}\).
- Tension acts at \(\theta = 30^\circ\) to the displacement. Use \(W = Ts \cos\theta\).
- Weight acts vertically downwards (\(\theta = 90^\circ\)) and normal contact force acts vertically upwards (\(\theta = 90^\circ\)).

#### Step 1: Work done by the tension force

\[
W_T = Ts \cos\theta
\]

Substitute the known values:
\[
W_T = 160\,\mathrm{N}\times 15\,\mathrm{m}\times \cos(30^\circ)
\]
\[
W_T = 2400 \times 0.8660 = 2078\,\mathrm{J} \approx 2100\,\mathrm{J} \text{ (to 2 significant figures)}
\]

#### Step 2: Work done by weight and normal contact force
- The weight acts vertically downward, perpendicular to the horizontal displacement:
  \[
  \theta = 90^\circ \implies \cos(90^\circ) = 0 \implies W_{\mathrm{weight}} = 0\,\mathrm{J}
  \]
- The normal contact force acts vertically upward, perpendicular to the horizontal displacement:
  \[
  \theta = 90^\circ \implies \cos(90^\circ) = 0 \implies W_{\mathrm{normal}} = 0\,\mathrm{J}
  \]

#### Step 3: Frictional force and work done against friction
Because the crate travels at constant velocity, the resultant horizontal force is zero:
\[
\Sigma F_x = T \cos(30^\circ) - f = 0
\]
\[
f = T \cos(30^\circ) = 160\,\mathrm{N}\times 0.8660 = 138.6\,\mathrm{N} \approx 140\,\mathrm{N}
\]

The force of friction acts directly opposite to the displacement (\(\theta = 180^\circ\)):
\[
W_{\mathrm{friction}} = fs \cos(180^\circ) = 138.6\,\mathrm{N}\times 15\,\mathrm{m}\times (-1) = -2078\,\mathrm{J} \approx -2100\,\mathrm{J}
\]
The work done **against friction** is \(+2100\,\mathrm{J}\), which is transferred into thermal energy.

#### Mark scheme
- **Part 1:**
  - **M1:** Use of \(W = Fs \cos\theta\) with correct angle \(30^\circ\) (\(160 \times 15 \times \cos 30^\circ\))
  - **A1:** \(W = 2100\,\mathrm{J}\) (or \(2.1 \times 10^3\,\mathrm{J}\), accept \(2080\,\mathrm{J}\))
- **Part 2:**
  - **B1:** Both forces do \(0\,\mathrm{J}\) because forces are perpendicular to displacement (\(\cos 90^\circ = 0\))
- **Part 3:**
  - **M1:** Horizontal component of tension equated to friction (\(f = 160 \cos 30^\circ\))
  - **A1:** \(f = 140\,\mathrm{N}\) (or \(139\,\mathrm{N}\))
  - **A1:** Work done against friction = \(2100\,\mathrm{J}\) (or work done by friction = \(-2100\,\mathrm{J}\))

#### Reasonableness check
- \(\cos(30^\circ) \approx 0.87\), so work done should be slightly less than \(160 \times 15 = 2400\,\mathrm{J}\). \(2080\,\mathrm{J}\) is consistent.
- Net work done on the crate: \(W_{\mathrm{net}} = W_T + W_f = +2078 - 2078 = 0\,\mathrm{J}\). Zero net work corresponds to constant kinetic energy, perfectly matching constant velocity.

---

### Worked example 2: Work done by an expanding gas in a cylinder

A cylinder contains a fixed mass of gas at a constant pressure of \(2.5 \times 10^5\,\mathrm{Pa}\). The initial volume of the gas is \(0.0040\,\mathrm{m^3}\). When thermal energy is supplied, the gas expands steadily against a movable piston, doing \(750\,\mathrm{J}\) of work on the piston while maintaining constant pressure.

Calculate:
1. The change in volume of the gas, \(\Delta V\).
2. The final volume of the gas in the cylinder.
3. State whether work is done on the gas or by the gas.

#### Strategy and model check
- Constant pressure expansion: formula \(W = p\Delta V\) applies directly.
- Given: \(p = 2.5 \times 10^5\,\mathrm{Pa}\), \(W = 750\,\mathrm{J}\), \(V_{\mathrm{initial}} = 0.0040\,\mathrm{m^3}\).
- Target: \(\Delta V\), then \(V_{\mathrm{final}} = V_{\mathrm{initial}} + \Delta V\).

#### Step 1: Calculate the change in volume

\[
W = p\Delta V \implies \Delta V = \frac{W}{p}
\]

Substitute the values:
\[
\Delta V = \frac{750\,\mathrm{J}}{2.5 \times 10^5\,\mathrm{Pa}}
\]
\[
\Delta V = 3.0 \times 10^{-3}\,\mathrm{m^3} \quad (0.0030\,\mathrm{m^3})
\]

#### Step 2: Calculate the final volume

\[
V_{\mathrm{final}} = V_{\mathrm{initial}} + \Delta V
\]
\[
V_{\mathrm{final}} = 0.0040\,\mathrm{m^3} + 0.0030\,\mathrm{m^3} = 0.0070\,\mathrm{m^3} = 7.0 \times 10^{-3}\,\mathrm{m^3}
\]

#### Step 3: Direction of work
The gas expands (\(\Delta V > 0\)), pushing the piston outward. Therefore, work is done **by the gas on the surroundings** (the piston).

#### Mark scheme
- **Part 1:**
  - **M1:** Rearrangement \(\Delta V = W / p\) and substitution (\(750 / (2.5 \times 10^5)\))
  - **A1:** \(\Delta V = 3.0 \times 10^{-3}\,\mathrm{m^3}\)
- **Part 2:**
  - **M1:** Addition of \(\Delta V\) to initial volume
  - **A1:** \(V_{\mathrm{final}} = 7.0 \times 10^{-3}\,\mathrm{m^3}\) (or \(0.0070\,\mathrm{m^3}\))
- **Part 3:**
  - **B1:** Work is done by the gas (as volume increases / gas expands)

#### Reasonableness check
- Unit check: \(\mathrm{J / Pa} = (\mathrm{N\,m}) / (\mathrm{N\,m^{-2}}) = \mathrm{m^3}\). Units are correct.
- Scaling: \(2.5 \times 10^5 \times 0.0030 = 750\,\mathrm{J}\). Arithmetic is verified.

---

### Worked example 3: Variable force on a force-displacement graph

A trolley is pushed along a straight horizontal track by a variable horizontal force. The force varies with displacement as follows:
- From \(s = 0\,\mathrm{m}\) to \(s = 3.0\,\mathrm{m}\), the force increases linearly from \(0\,\mathrm{N}\) to \(90\,\mathrm{N}\).
- From \(s = 3.0\,\mathrm{m}\) to \(s = 8.0\,\mathrm{m}\), the force remains constant at \(90\,\mathrm{N}\).

Calculate the total work done on the trolley over the entire \(8.0\,\mathrm{m}\) displacement.

#### Strategy and model check
- Work done is the area under the force-displacement graph.
- The region between \(s = 0\) and \(s = 8.0\,\mathrm{m}\) is a trapezium, which can be split into:
  1. A triangular area from \(s = 0\) to \(s = 3.0\,\mathrm{m}\).
  2. A rectangular area from \(s = 3.0\,\mathrm{m}\) to \(s = 8.0\,\mathrm{m}\).

#### Step 1: Area of the triangular section (\(0\) to \(3.0\,\mathrm{m}\))

\[
\text{Area}_1 = \frac{1}{2}\times \text{base}\times \text{height}
\]
\[
\text{Area}_1 = \frac{1}{2}\times 3.0\,\mathrm{m}\times 90\,\mathrm{N} = 135\,\mathrm{J}
\]

#### Step 2: Area of the rectangular section (\(3.0\) to \(8.0\,\mathrm{m}\))
The base of this section is \(\Delta s = 8.0\,\mathrm{m} - 3.0\,\mathrm{m} = 5.0\,\mathrm{m}\).

\[
\text{Area}_2 = \text{base}\times \text{height} = 5.0\,\mathrm{m}\times 90\,\mathrm{N} = 450\,\mathrm{J}
\]

#### Step 3: Total work done

\[
W_{\mathrm{total}} = \text{Area}_1 + \text{Area}_2 = 135\,\mathrm{J} + 450\,\mathrm{J} = 585\,\mathrm{J} \approx 590\,\mathrm{J} \text{ (to 2 significant figures)}
\]

Alternatively, using the area of a trapezium with parallel sides \(a = 5.0\,\mathrm{m}\) and \(b = 8.0\,\mathrm{m}\), and height \(h = 90\,\mathrm{N}\):
\[
W = \frac{1}{2}(a + b) h = \frac{1}{2}(5.0 + 8.0)\times 90 = \frac{1}{2}\times 13.0\times 90 = 585\,\mathrm{J}
\]

#### Mark scheme
- **M1:** Recognition that work done is area under graph, with triangular area calculated (\(0.5 \times 3.0 \times 90 = 135\,\mathrm{J}\))
- **M1:** Rectangular area calculated (\(5.0 \times 90 = 450\,\mathrm{J}\)) or correct trapezium formula
- **A1:** Total work done = \(585\,\mathrm{J}\) (accept \(590\,\mathrm{J}\))

---

## Guided Practice

### Problem statement
A groundskeeper pushes a lawn roller across a flat grass field. The groundskeeper applies a steady downward push of \(140\,\mathrm{N}\) along the handle, which makes an angle of \(42^\circ\) with the horizontal ground. The roller moves a distance of \(22\,\mathrm{m}\) at a constant speed in a straight line.

```
       Push P = 140 N
         \
          \
           \  42°
            +---------> horizontal motion s = 22 m
          [ROLLER]
```

Work through the following steps to analyze this situation:

#### Guidance step 1: Identify the component of force along the motion
Ask yourself: In which direction is the roller moving? It moves horizontally along the ground.
- The push is directed downward and forward along the handle at \(42^\circ\) to the horizontal.
- The forward horizontal component of the push is:
  \[
  P_x = P \cos(42^\circ) = 140\,\mathrm{N}\times \cos(42^\circ) = 140 \times 0.7431 = 104.0\,\mathrm{N}
  \]

#### Guidance step 2: Calculate the work done by the groundskeeper
Now apply the definition of work done:
\[
W = P s \cos\theta = 140\,\mathrm{N}\times 22\,\mathrm{m}\times \cos(42^\circ) = 3080 \times 0.7431 = 2289\,\mathrm{J} \approx 2300\,\mathrm{J}
\]

#### Guidance step 3: Explain the role of the perpendicular component
The vertical component of the push is \(P_y = P \sin(42^\circ) = 140 \times 0.6691 = 93.7\,\mathrm{N}\), directed vertically downward into the ground.
- The angle between this vertical component and the horizontal displacement is \(90^\circ\).
- Because \(\cos(90^\circ) = 0\), the vertical component does zero work on the roller.
- The vertical component does, however, press the roller harder into the ground, increasing the normal contact force from the ground to \(N = mg + P_y\).

---

## Checks for Understanding

### Check 1: Force perpendicular to motion

A student holds a heavy backpack of mass \(8.0\,\mathrm{kg}\) while walking horizontally across a flat school playground at a constant velocity for a distance of \(25\,\mathrm{m}\).

How much work does the upward lifting force exerted by the student's hands do on the backpack?

- **A.** Zero joules
- **B.** \(1960\,\mathrm{J}\)

**Feedback for A:** Correct. The lifting force exerted by the hands acts vertically upwards (to balance the weight of the backpack, \(F = mg = 8.0 \times 9.81 = 78.5\,\mathrm{N}\)). The displacement is horizontal. The angle between the force and the displacement is \(\theta = 90^\circ\). Since \(\cos(90^\circ) = 0\), \(W = Fs \cos(90^\circ) = 0\,\mathrm{J}\). No mechanical work is done on the backpack by the upward force.

**Feedback for B:** Incorrect. You calculated \(W = mgs = 8.0 \times 9.81 \times 25 = 1962\,\mathrm{J}\), which assumes the force acts parallel to the displacement. That would be true only if the backpack were being lifted vertically through \(25\,\mathrm{m}\). For horizontal motion, the lifting force is perpendicular to the displacement, so it does no work.

---

### Check 2: Gas compression at constant pressure

A gas in a sealed cylinder is compressed from an initial volume of \(0.015\,\mathrm{m^3}\) to a final volume of \(0.0090\,\mathrm{m^3}\) by a constant external pressure of \(1.2 \times 10^5\,\mathrm{Pa}\).

Which statement correctly identifies the work done?

- **A.** \(720\,\mathrm{J}\) of work is done by the gas on the surroundings.
- **B.** \(720\,\mathrm{J}\) of work is done on the gas by the surroundings.

**Feedback for A:** Incorrect. When a gas is compressed, its volume decreases (\(\Delta V = 0.0090 - 0.015 = -0.0060\,\mathrm{m^3}\)). The external agent pushes inward, transferring mechanical energy into the gas. Work is done ON the gas, not BY the gas.

**Feedback for B:** Correct. The change in volume has magnitude \(|\Delta V| = 0.015 - 0.0090 = 0.0060\,\mathrm{m^3}\). The work done is \(W = p|\Delta V| = 1.2 \times 10^5\,\mathrm{Pa}\times 0.0060\,\mathrm{m^3} = 720\,\mathrm{J}\). Because the gas decreases in volume, work is done on the gas by the external force compressing it.

---

### Check 3: Acute versus obtuse angles

A car of mass \(1200\,\mathrm{kg}\) travels along a straight, horizontal road. The engine provides a forward driving force of \(1800\,\mathrm{N}\), while air resistance and road friction exert a backward resistive force of \(600\,\mathrm{N}\). The car moves forward by \(50\,\mathrm{m}\).

What is the work done by the resistive force?

- **A.** \(-3.0 \times 10^4\,\mathrm{J}\)
- **B.** \(+3.0 \times 10^4\,\mathrm{J}\)

**Feedback for A:** Correct. The resistive force acts in the direction opposite to the forward displacement. The angle between the backward resistive force and the forward displacement is \(\theta = 180^\circ\). Therefore, \(W = Fs \cos(180^\circ) = 600 \times 50 \times (-1) = -30\,000\,\mathrm{J} = -3.0 \times 10^4\,\mathrm{J}\). The negative sign indicates that energy is removed from the car's kinetic store and dissipated as thermal energy.

**Feedback for B:** Incorrect. You omitted the direction of the force relative to displacement. A force that opposes motion acts at \(180^\circ\) to the displacement vector. Because \(\cos(180^\circ) = -1\), the work done by the resistive force on the car is negative.

---

### Check 4: Work from a force-displacement graph

A graph shows the horizontal force \(F\) acting on a trolley against its displacement \(s\). The force starts at \(0\,\mathrm{N}\) at \(s = 0\) and increases at a constant rate to \(40\,\mathrm{N}\) at \(s = 6.0\,\mathrm{m}\).

What is the work done on the trolley?

- **A.** \(120\,\mathrm{J}\)
- **B.** \(240\,\mathrm{J}\)

**Feedback for A:** Correct. The work done is equal to the area under the force-displacement graph. For a force that increases linearly from zero, the shape is a right-angled triangle with base \(6.0\,\mathrm{m}\) and height \(40\,\mathrm{N}\). Area = \(\frac{1}{2}\times \text{base}\times \text{height} = \frac{1}{2}\times 6.0\,\mathrm{m}\times 40\,\mathrm{N} = 120\,\mathrm{J}\).

**Feedback for B:** Incorrect. You multiplied maximum force by total displacement (\(40 \times 6.0 = 240\,\mathrm{J}\)). That calculation gives the area of a rectangle, which would be correct only if the force were constantly \(40\,\mathrm{N}\) throughout the whole motion. Because the force increased linearly from zero, the average force is only \(20\,\mathrm{N}\), giving \(120\,\mathrm{J}\).

---

## Common Misconceptions

### Misconception 1: "Tiring out your muscles means you are doing work"
In everyday life, holding a heavy barbell above your head or carrying luggage stationary feels exhausting. Biologically, your muscle fibres are continuously contracting and relaxing, expending chemical energy. In physics, however, **work requires a displacement in the direction of the force**. If the barbell does not move, displacement \(s = 0\), so the work done on the barbell is precisely zero. Always check for a physical displacement.

### Misconception 2: Forgetting to resolve the force along the displacement
Students often calculate work done simply as \(W = F \times s\), ignoring the angle between the two vectors. If a child pulls a sledge with a rope angled at \(45^\circ\), multiplying the rope tension directly by the distance travelled overestimates the work done by a factor of \(\frac{1}{\cos 45^\circ} \approx 1.41\). Always identify the angle \(\theta\) between the force vector and the displacement vector, and use \(W = Fs \cos\theta\).

### Misconception 3: Assuming perpendicular forces do work
A common exam error is including the weight or normal contact force when calculating the work done on an object moving horizontally. Because gravity and normal contact forces act at \(90^\circ\) to horizontal displacement, \(\cos(90^\circ) = 0\), meaning they transfer zero energy along the horizontal. Only forces (or components of forces) parallel or antiparallel to the displacement do work.

### Misconception 4: Confusing work done BY a gas with work done ON a gas
When a gas expands, it pushes its boundary outward, doing work on the external surroundings (\(W_{\mathrm{by}} = p\Delta V > 0\)). When a gas is compressed, an external agent pushes the boundary inward, doing work on the gas (\(W_{\mathrm{on}} = p|\Delta V|\)). Confusing these leads to sign errors in thermodynamic calculations. Remember: expansion = work done by the gas; compression = work done on the gas.

### Misconception 5: Treating work as a vector because force and displacement are vectors
Force is a vector and displacement is a vector, so students often assume their product must also be a vector with a directional arrow. In reality, work is a **scalar**. It has magnitude and can be positive or negative (indicating whether energy is added to or removed from a system), but it has no direction in space such as "north" or "at \(30^\circ\)".

---

## Core Recap

- **Work done** is defined as the product of force and displacement in the direction of the force.
- The SI unit of work is the **joule** (\(\mathrm{J}\)), where \(1\,\mathrm{J} = 1\,\mathrm{N\,m} = 1\,\mathrm{kg\,m^2\,s^{-2}}\).
- Work is a **scalar quantity**.
- For a constant force \(F\) acting at an angle \(\theta\) to displacement \(s\):
  \[
  W = Fs \cos\theta
  \]
- When \(\theta = 0^\circ\), \(W = +Fs\) (force assists motion; maximum positive work).
- When \(\theta = 90^\circ\), \(W = 0\) (force perpendicular to motion does zero work).
- When \(\theta = 180^\circ\), \(W = -Fs\) (force opposes motion; negative work).
- **Work done = area under a force-displacement graph.**
- For an expanding gas at constant pressure \(p\):
  \[
  W = p\Delta V
  \]
- During expansion (\(\Delta V > 0\)), work is done **by** the gas. During compression (\(\Delta V < 0\)), work is done **on** the gas.
- **Work done represents the mechanical transfer of energy:** \(W = \Delta E\), consistent with the principle of conservation of energy.
