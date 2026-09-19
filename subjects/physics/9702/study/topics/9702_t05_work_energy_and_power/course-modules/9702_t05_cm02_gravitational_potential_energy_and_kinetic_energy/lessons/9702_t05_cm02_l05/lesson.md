# Gravitational Potential Energy in a Uniform Field

## Learning Outcomes

By the end of this lesson, you should be able to:
- **Derive**, using \(W = Fs\), the formula \(\Delta E_P = mg\Delta h\) for gravitational potential energy changes in a uniform gravitational field (`9702_t05_m02_o01`).
- **Recall and use** the formula \(\Delta E_P = mg\Delta h\) for gravitational potential energy changes in a uniform gravitational field (`9702_t05_m02_o02`).
- **State the condition** under which \(\Delta E_P = mg\Delta h\) is valid, namely that the gravitational field strength \(g\) is uniform (constant).
- **Explain** why changes in gravitational potential energy depend only on the vertical displacement \(\Delta h\) and are independent of the path taken.

---

## Prior Knowledge

To master this lesson, you should be familiar with the following concepts from earlier lessons:
- **Work done by a constant force:** \(W = Fs\), where \(W\) is work done in joules (\(\mathrm{J}\)), \(F\) is the force in newtons (\(\mathrm{N}\)), and \(s\) is the displacement in metres (\(\mathrm{m}\)) in the direction of the force (Module 5.1).
- **Weight:** \(W_{\text{weight}} = mg\), where \(m\) is mass in kilograms (\(\mathrm{kg}\)) and \(g\) is the acceleration of free fall or gravitational field strength (\(9.81\,\mathrm{m\,s^{-2}}\) or \(9.81\,\mathrm{N\,kg^{-1}}\) near Earth's surface) (Topic 3).
- **Principle of conservation of energy:** Energy cannot be created or destroyed; it can only be transferred from one form to another, with the total energy of a closed system remaining constant (Module 5.1).
- **Vectors and scalars:** Work and energy are scalar quantities with magnitude and units but no direction in space, whereas displacement and force are vector quantities (Topic 1).

---

## Core Concepts

### What is Gravitational Potential Energy?

When you lift an object away from the ground, you must apply an upward force to overcome the downward pull of gravity. As the object rises, you perform work on it. 

Where does this work go? Because energy is conserved, the work done is transferred into stored energy within the gravitational system consisting of the object and the Earth. This stored energy is called **gravitational potential energy**.

<a id="definition-9702_def_gravitational_potential_energy"></a>

> **Definition to learn: gravitational potential energy.** energy stored by a mass because of its position or height in a gravitational field

Let us examine the key components of this controlled definition:
- **Energy stored:** It is potential energy because it represents stored capacity to perform mechanical work. If the object is released, gravity will accelerate it downward, converting this stored energy into kinetic energy.
- **By a mass:** The amount of energy stored depends directly on the quantity of matter in the object.
- **Position or height in a gravitational field:** The higher the mass is raised relative to a reference level, the greater the quantity of energy stored.

### What is a Uniform Gravitational Field?

A **uniform gravitational field** is a region of space in which the gravitational field strength \(g\) has the exact same magnitude and direction at every single point.

- Field lines in a uniform field are **parallel** to one another and **equally spaced**.
- On Earth, the gravitational field strength points vertically downward towards the centre of the Earth.
- Near the surface of the Earth, over height changes of metres, hundreds of metres, or even a few kilometres, the distance from the centre of the Earth (radius \(\approx 6.4 \times 10^6\,\mathrm{m}\)) changes by an insignificant fraction of a percent.
- Therefore, for local situations near Earth's surface, we treat the gravitational field as **strictly uniform**, with:

\[
g = 9.81\,\mathrm{m\,s^{-2}} \quad (\text{or } 9.81\,\mathrm{N\,kg^{-1}})
\]

### Potential Difference versus Absolute Potential

In Cambridge International AS Level Physics, we do not calculate an absolute value of potential energy for an isolated object. Instead, we always measure the **change** in gravitational potential energy, denoted by \(\Delta E_P\).

- We define an arbitrary reference level (such as the ground, the floor of a room, or the top of a laboratory bench) where we define height \(h = 0\).
- When a mass moves upwards by a vertical displacement \(\Delta h\), its gravitational potential energy **increases** (\(\Delta E_P > 0\)).
- When a mass moves downwards by a vertical displacement \(\Delta h\), its gravitational potential energy **decreases** (\(\Delta E_P < 0\)).
- The choice of reference level does not affect the value of \(\Delta E_P\), because the difference in height \(\Delta h = h_{\text{final}} - h_{\text{initial}}\) is identical regardless of where the zero level is placed.

---

## Detailed Mathematical Derivations

### Deriving \(\Delta E_P = mg\Delta h\) from First Principles

You must be able to derive this equation clearly for examination questions by starting from the definition of work done, \(W = Fs\).

#### Step 1: Physical Setup
Consider an object of mass \(m\) initially resting at height \(h_1\) in a uniform gravitational field of field strength \(g\). The object is lifted vertically upwards to a new height \(h_2\).

- The vertical displacement is:
  \[
  s = \Delta h = h_2 - h_1
  \]
- The downward gravitational force acting on the mass is its weight:
  \[
  W_{\text{weight}} = mg
  \]

#### Step 2: Force Required to Lift the Mass
To lift the object vertically at a constant speed (so that there is no acceleration and no change in kinetic energy), the resultant force on the object must be zero (\(\Sigma F = 0\)).

Therefore, the external upward lifting force \(F\) applied to the mass must exactly balance its downward weight:
\[
F = W_{\text{weight}} = mg
\]

#### Step 3: Work Done by the Lifting Force
Recall the definition of work done by a constant force:
\[
W = Fs
\]
Here, the applied force \(F\) acts vertically upward, and the displacement \(s = \Delta h\) is also vertically upward. The force and displacement are in the exact same direction (\(\theta = 0^\circ\), so \(\cos 0^\circ = 1\)).

Substitute \(F = mg\) and \(s = \Delta h\) into the work equation:
\[
W = (mg)(\Delta h) = mg\Delta h
\]

#### Step 4: Connecting Work Done to Potential Energy
By the principle of conservation of energy, the work done by the external force against gravity increases the gravitational potential energy stored in the mass-Earth system:
\[
\Delta E_P = W
\]
Therefore:
\[
\Delta E_P = mg\Delta h
\]

<a id="formula-9702_formula_gravitational_potential_energy"></a>

> **Formula to learn: Change in gravitational potential energy.**
>
> \[
> \Delta E_P = mg\Delta h
> \]

Where:
- \(\Delta E_P\) is the change in gravitational potential energy, measured in joules (\(\mathrm{J}\)).
- \(m\) is the mass of the object, measured in kilograms (\(\mathrm{kg}\)).
- \(g\) is the acceleration of free fall (gravitational field strength), taken as \(9.81\,\mathrm{m\,s^{-2}}\) (or \(\mathrm{N\,kg^{-1}}\)).
- \(\Delta h\) is the change in vertical height, measured in metres (\(\mathrm{m}\)).

---

### Validity Condition: Why Must the Gravitational Field Be Uniform?

The derivation above relies on a crucial physical assumption:
1. The force \(F = mg\) remained **constant** throughout the entire vertical displacement \(\Delta h\).
2. The formula \(W = Fs\) applies only when the force \(F\) is constant along the displacement \(s\).
3. If the gravitational field were non-uniform, \(g\) would vary with height (as happens on astronomical scales, where \(g \propto \frac{1}{r^2}\)). In that case, \(F\) would not be constant, and \(W\) could not be found by a simple product \(Fs\); calculus integration would be required instead.

Therefore:
> **The formula \(\Delta E_P = mg\Delta h\) is valid only in a uniform gravitational field (where \(g\) is constant).**

---

### Path Independence: Why Only Vertical Height Matters

What happens if an object is moved from a lower level to a higher level along an inclined ramp, a spiral path, or steps, rather than straight up?

Let us analyze a mass \(m\) moving up a frictionless ramp inclined at an angle \(\theta\) to the horizontal:
- The length of the ramp is \(L\).
- The vertical height gained is \(\Delta h = L \sin\theta\).
- The component of the object's weight acting parallel to the ramp (down the slope) is:
  \[
  F_{\text{parallel}} = mg \sin\theta
  \]
- To move the object up the ramp at constant speed, the applied force parallel to the ramp must be:
  \[
  F = mg \sin\theta
  \]
- The displacement along the ramp in the direction of this force is \(s = L\).
- The work done by the applied force is:
  \[
  W = Fs = (mg \sin\theta) \times L = mg(L \sin\theta)
  \]
- Since \(L \sin\theta = \Delta h\), this gives:
  \[
  W = mg\Delta h
  \]

Furthermore, any horizontal displacement occurs perpendicular to the downward gravitational force (\(\theta = 90^\circ\)). Since \(\cos 90^\circ = 0\), gravity does zero work during horizontal movement:
\[
W_{\text{horizontal}} = F \times d \times \cos 90^\circ = 0
\]

Therefore:
> **Gravitational potential energy change \(\Delta E_P\) depends exclusively on the vertical height difference \(\Delta h\), completely independent of the horizontal distance or the path taken.**

---

## Worked Examples with Mark Schemes

### Worked Example 1: Lifting an Industrial Load with a Crane

A construction crane lifts a bundle of steel reinforcement bars of mass \(650\,\mathrm{kg}\) vertically from the ground to the top floor of a building at a steady speed. The vertical distance between the ground and the top floor is \(24.0\,\mathrm{m}\).

Calculate:
1. The gain in gravitational potential energy of the steel bars.
2. The minimum useful power output of the crane motor if the lift takes \(40.0\,\mathrm{s}\).

#### Solution and Examination Mark Scheme

**Part 1: Gain in gravitational potential energy**
- State the formula:
  \[
  \Delta E_P = mg\Delta h \quad \text{[M1]}
  \]
- Substitute the known values:
  \[
  \Delta E_P = 650\,\mathrm{kg} \times 9.81\,\mathrm{m\,s^{-2}} \times 24.0\,\mathrm{m}
  \]
  \[
  \Delta E_P = 153\,036\,\mathrm{J}
  \]
- Round to appropriate significant figures (3 s.f.):
  \[
  \Delta E_P = 1.53 \times 10^5\,\mathrm{J} \quad (\text{or } 153\,\mathrm{kJ}) \quad \text{[A1]}
  \]

**Part 2: Minimum useful power output**
- Relate power to rate of work done or energy transferred:
  \[
  P = \frac{W}{t} = \frac{\Delta E_P}{t} \quad \text{[M1]}
  \]
- Substitute values:
  \[
  P = \frac{153\,036\,\mathrm{J}}{40.0\,\mathrm{s}} = 3825.9\,\mathrm{W}
  \]
- Round to 3 significant figures:
  \[
  P = 3.83 \times 10^3\,\mathrm{W} \quad (\text{or } 3.83\,\mathrm{kW}) \quad \text{[A1]}
  \]

#### Reasonableness and Unit Check
- Units: \(\mathrm{kg} \times \mathrm{m\,s^{-2}} \times \mathrm{m} = \mathrm{N} \times \mathrm{m} = \mathrm{J}\).
- Power: \(\mathrm{J\,s^{-1}} = \mathrm{W}\).
- A power of \(3.83\,\mathrm{kW}\) is typical for an industrial electric winch lifting a sub-tonne load at \(\frac{24.0\,\mathrm{m}}{40.0\,\mathrm{s}} = 0.60\,\mathrm{m\,s^{-1}}\). Check: \(P = Fv = (650 \times 9.81) \times 0.60 = 3826\,\mathrm{W}\). Completely consistent.

---

### Worked Example 2: Sledge on an Inclined Slope with Friction

A child and sledge have a combined mass of \(42\,\mathrm{kg}\). They start from rest and slide down a straight snowy hillside inclined at \(18^\circ\) to the horizontal. The distance travelled along the slope is \(65\,\mathrm{m}\). A constant resistive friction force of \(28\,\mathrm{N}\) acts against the sledge along the slope.

Calculate:
1. The vertical height lost by the sledge.
2. The decrease in gravitational potential energy of the sledge and child.
3. The work done against the frictional force along the slope.

#### Solution and Examination Mark Scheme

**Part 1: Vertical height lost**
- Use trigonometry on the right-angled slope triangle:
  \[
  \Delta h = L \sin\theta \quad \text{[M1]}
  \]
  \[
  \Delta h = 65\,\mathrm{m} \times \sin(18^\circ) = 65 \times 0.30902 = 20.086\,\mathrm{m}
  \]
  \[
  \Delta h = 20\,\mathrm{m} \quad (\text{to 2 s.f.}) \quad \text{[A1]}
  \]

**Part 2: Decrease in gravitational potential energy**
- Use \(\Delta E_P = mg\Delta h\):
  \[
  \Delta E_P = mg\Delta h \quad \text{[M1]}
  \]
  \[
  \Delta E_P = 42\,\mathrm{kg} \times 9.81\,\mathrm{m\,s^{-2}} \times 20.086\,\mathrm{m}
  \]
  \[
  \Delta E_P = 8276\,\mathrm{J}
  \]
  \[
  \text{Decrease in } E_P = 8.3 \times 10^3\,\mathrm{J} \quad (\text{or } 8.3\,\mathrm{kJ}) \quad \text{[A1]}
  \]

**Part 3: Work done against friction**
- Friction acts along the slope, opposite to the displacement along the slope:
  \[
  W_f = f \times L \quad \text{[M1]}
  \]
  \[
  W_f = 28\,\mathrm{N} \times 65\,\mathrm{m} = 1820\,\mathrm{J}
  \]
  \[
  W_f = 1.8 \times 10^3\,\mathrm{J} \quad (\text{or } 1.8\,\mathrm{kJ}) \quad \text{[A1]}
  \]

Notice the vital physics: \(\Delta E_P\) is calculated using the **vertical height** (\(20.1\,\mathrm{m}\)), whereas work done against friction is calculated using the **distance along the surface** (\(65\,\mathrm{m}\)) because friction acts along the surface.

---

### Worked Example 3: Multi-Stage Path and Path Independence

A laboratory trolley of mass \(2.50\,\mathrm{kg}\) is moved along a test track in three successive stages:
- **Stage 1 (A to B):** The trolley rolls down a curved ramp, dropping vertically by \(1.20\,\mathrm{m}\) while travelling a horizontal distance of \(2.50\,\mathrm{m}\).
- **Stage 2 (B to C):** The trolley travels along a level horizontal bench for \(3.00\,\mathrm{m}\).
- **Stage 3 (C to D):** The trolley is lifted vertically upwards through a height of \(0.70\,\mathrm{m}\).

Determine the change in gravitational potential energy \(\Delta E_P\) of the trolley for:
1. Stage 1 (from A to B)
2. Stage 2 (from B to C)
3. The overall journey (from A to D)

#### Solution and Examination Mark Scheme

**Part 1: Stage 1 (A to B)**
- The trolley drops vertically, so \(\Delta h = -1.20\,\mathrm{m}\):
  \[
  \Delta E_P = mg\Delta h \quad \text{[M1]}
  \]
  \[
  \Delta E_P = 2.50 \times 9.81 \times (-1.20) = -29.43\,\mathrm{J}
  \]
  \[
  \Delta E_P = -29.4\,\mathrm{J} \quad (\text{or a decrease of } 29.4\,\mathrm{J}) \quad \text{[A1]}
  \]

**Part 2: Stage 2 (B to C)**
- Motion is strictly horizontal, so vertical height change \(\Delta h = 0\):
  \[
  \Delta E_P = 0\,\mathrm{J} \quad \text{[B1]}
  \]
  Reason: Force of gravity is perpendicular to displacement; no work is done by or against gravity.

**Part 3: Overall Journey (A to D)**
- Net vertical displacement from start to finish:
  \[
  \Delta h_{\text{net}} = h_D - h_A = -1.20\,\mathrm{m} + 0.70\,\mathrm{m} = -0.50\,\mathrm{m} \quad \text{[M1]}
  \]
- Overall change in gravitational potential energy:
  \[
  \Delta E_{P,\text{net}} = mg\Delta h_{\text{net}} = 2.50 \times 9.81 \times (-0.50) = -12.26\,\mathrm{J}
  \]
  \[
  \Delta E_{P,\text{net}} = -12.3\,\mathrm{J} \quad (\text{or a net decrease of } 12.3\,\mathrm{J}) \quad \text{[A1]}
  \]
- Check by summing individual stages:
  \[
  \Delta E_{P,\text{total}} = -29.43\,\mathrm{J} + 0\,\mathrm{J} + (2.50 \times 9.81 \times 0.70) = -29.43 + 17.17 = -12.26\,\mathrm{J}
  \]
  Both methods produce the exact same result.

---

## Guided Practice

### Problem 1: Pumped Hydroelectric Energy Storage

A pumped-storage power station pumps water from a lower lake to an upper mountain reservoir during the night when electricity demand is low.
- The volume of water pumped into the upper reservoir is \(4.50 \times 10^5\,\mathrm{m^3}\).
- The density of fresh water is \(1.00 \times 10^3\,\mathrm{kg\,m^{-3}}\).
- The average vertical height through which the water is raised is \(280\,\mathrm{m}\).
- The pumping operation takes \(5.00\,\mathrm{hours}\).

**Task:**
1. Calculate the mass of water transferred to the upper reservoir.
2. Calculate the total increase in gravitational potential energy of the stored water.
3. Determine the minimum average power supplied to the water by the pumps.

#### Step-by-Step Guidance:
- **Step 1:** Use \(\text{mass} = \text{density} \times \text{volume}\) (\(m = \rho V\)).
  \[
  m = (1.00 \times 10^3\,\mathrm{kg\,m^{-3}}) \times (4.50 \times 10^5\,\mathrm{m^3}) = 4.50 \times 10^8\,\mathrm{kg}
  \]
- **Step 2:** Apply \(\Delta E_P = mg\Delta h\).
  \[
  \Delta E_P = (4.50 \times 10^8\,\mathrm{kg}) \times (9.81\,\mathrm{m\,s^{-2}}) \times (280\,\mathrm{m}) = 1.236 \times 10^{12}\,\mathrm{J}
  \]
  Report to 3 significant figures: \(\Delta E_P = 1.24 \times 10^{12}\,\mathrm{J}\) (or \(1.24\,\mathrm{TJ}\)).
- **Step 3:** Convert pumping time to seconds:
  \[
  t = 5.00 \times 3600\,\mathrm{s} = 1.80 \times 10^4\,\mathrm{s}
  \]
  Then calculate power:
  \[
  P = \frac{\Delta E_P}{t} = \frac{1.236 \times 10^{12}\,\mathrm{J}}{1.80 \times 10^4\,\mathrm{s}} = 6.87 \times 10^7\,\mathrm{W} \quad (\text{or } 68.7\,\mathrm{MW})
  \]

---

### Problem 2: Aircraft Climb Rate

A twin-engine transport aircraft has a mass of \(1.80 \times 10^4\,\mathrm{kg}\). The aircraft climbs at a constant airspeed of \(85.0\,\mathrm{m\,s^{-1}}\) along a flight path inclined at an angle of \(8.50^\circ\) above the horizontal.

**Task:**
1. Calculate the vertical component of the aircraft's velocity (the rate of climb).
2. Calculate the gain in gravitational potential energy of the aircraft in a duration of \(60.0\,\mathrm{s}\).
3. Calculate the rate at which gravitational potential energy is gained.

#### Step-by-Step Guidance:
- **Step 1:** Resolve velocity vertically:
  \[
  v_y = v \sin\theta = 85.0\,\mathrm{m\,s^{-1}} \times \sin(8.50^\circ) = 85.0 \times 0.14781 = 12.56\,\mathrm{m\,s^{-1}} \approx 12.6\,\mathrm{m\,s^{-1}}
  \]
- **Step 2:** Find the vertical height gained in \(60.0\,\mathrm{s}\):
  \[
  \Delta h = v_y \times t = 12.564\,\mathrm{m\,s^{-1}} \times 60.0\,\mathrm{s} = 753.8\,\mathrm{m}
  \]
  Calculate \(\Delta E_P\):
  \[
  \Delta E_P = mg\Delta h = (1.80 \times 10^4\,\mathrm{kg}) \times (9.81\,\mathrm{m\,s^{-2}}) \times (753.8\,\mathrm{m}) = 1.33 \times 10^8\,\mathrm{J} \quad (\text{or } 133\,\mathrm{MJ})
  \]
- **Step 3:** Calculate the rate of gain in \(E_P\):
  \[
  \frac{\Delta E_P}{\Delta t} = \frac{1.331 \times 10^8\,\mathrm{J}}{60.0\,\mathrm{s}} = 2.22 \times 10^6\,\mathrm{W} \quad (\text{or } 2.22\,\mathrm{MW})
  \]
  Alternative direct method: \(\text{Rate} = mg v_y = (1.80 \times 10^4 \times 9.81) \times 12.564 = 2.22 \times 10^6\,\mathrm{W}\).

---

## Checks for Understanding with Explanations

### Check 1: Comparing Paths Up a Cliff

A heavy crate of mass \(35\,\mathrm{kg}\) is moved from sea level to the top of a coastal cliff of height \(40\,\mathrm{m}\).
- Crane X hoists the crate vertically upwards to the top of the cliff.
- Crane Y pulls an identical crate up a sloping track of length \(120\,\mathrm{m}\) to the exact same cliff top.

Assuming friction along the track is negligible, which statement correctly compares the gain in gravitational potential energy of the two crates?

- **A.** The crate moved by Crane Y gains three times more gravitational potential energy than the crate moved by Crane X because the distance along the track is three times longer.
- **B.** Both crates gain the exact same amount of gravitational potential energy because \(\Delta E_P\) depends solely on the vertical height difference.

**Feedback for A:** Incorrect. This is a common trap. The distance travelled along the path does not determine gravitational potential energy. Although Crane Y pulls the crate over three times the distance, the pulling force required along the slope is only one-third of the vertical lifting force. Work done against gravity, and therefore the gain in \(E_P\), depends strictly on the vertical height \(\Delta h\).

**Feedback for B:** Correct. Gravitational potential energy change in a uniform field is \(\Delta E_P = mg\Delta h\). Since both crates have the same mass (\(35\,\mathrm{kg}\)) and reach the same vertical height (\(\Delta h = 40\,\mathrm{m}\)), both experience an identical gain: \(\Delta E_P = 35 \times 9.81 \times 40 = 13.7\,\mathrm{kJ}\).

---

### Check 2: Sign of Energy Change for a Falling Object

A skydiver of mass \(75\,\mathrm{kg}\) jumps from an aeroplane and descends vertically from an altitude of \(3000\,\mathrm{m}\) to \(1000\,\mathrm{m}\).

Which statement correctly identifies the change in gravitational potential energy of the skydiver?

- **A.** The change is \(-1.5 \times 10^6\,\mathrm{J}\) (a decrease of \(1.5\,\mathrm{MJ}\)) because the vertical displacement is downward.
- **B.** The change is \(+1.5 \times 10^6\,\mathrm{J}\) (an increase of \(1.5\,\mathrm{MJ}\)) because the skydiver is accelerating and gaining speed.

**Feedback for A:** Correct. The initial height is \(h_1 = 3000\,\mathrm{m}\) and the final height is \(h_2 = 1000\,\mathrm{m}\). The change in height is \(\Delta h = h_2 - h_1 = 1000 - 3000 = -2000\,\mathrm{m}\). Therefore, \(\Delta E_P = mg\Delta h = 75 \times 9.81 \times (-2000) = -1.47 \times 10^6\,\mathrm{J} \approx -1.5\,\mathrm{MJ}\). The negative sign indicates a loss of stored gravitational potential energy (which is transferred into kinetic energy and thermal energy).

**Feedback for B:** Incorrect. Gaining speed means the skydiver gains kinetic energy, not gravitational potential energy. Gravitational potential energy depends only on position in the field; as height decreases, stored gravitational potential energy must decrease.

---

### Check 3: The Uniform Field Condition

A student suggests using the equation \(\Delta E_P = mg\Delta h\) to calculate the energy required to launch a weather satellite from the surface of the Earth to an orbital altitude of \(36\,000\,\mathrm{km}\).

Why is this formula invalid for this calculation?

- **A.** The formula is invalid because the gravitational field strength \(g\) decreases substantially over a distance of \(36\,000\,\mathrm{km}\), so the field is not uniform.
- **B.** The formula is invalid because the satellite has engines that do work, and \(\Delta E_P = mg\Delta h\) only applies to objects falling freely without engines.

**Feedback for A:** Correct. The formula \(\Delta E_P = mg\Delta h\) was derived assuming that the gravitational force \(mg\) remains constant over the displacement. At an altitude of \(36\,000\,\mathrm{km}\) (several Earth radii away), the gravitational field strength has dropped to less than \(5\%\) of its surface value. Because the field is non-uniform, calculus integration with Newton's law of gravitation must be used instead (studied in A2 Topic 13).

**Feedback for B:** Incorrect. The formula applies whenever an external force moves an object in a gravitational field, regardless of whether that force is provided by a crane, a muscle, or a rocket motor. The sole reason the equation fails is that the gravitational field strength \(g\) is not constant over such large distances.

---

### Check 4: Unit Conversion Trap

A table tennis ball of mass \(2.7\,\mathrm{g}\) is dropped from a shelf that is \(85\,\mathrm{cm}\) above the floor.

What is the change in gravitational potential energy of the ball as it falls to the floor?

- **A.** \(-2.3 \times 10^{-2}\,\mathrm{J}\)
- **B.** \(-2300\,\mathrm{J}\)

**Feedback for A:** Correct. You must convert both mass and height into SI base units before calculating: mass \(m = 2.7\,\mathrm{g} = 2.7 \times 10^{-3}\,\mathrm{kg}\), and \(\Delta h = -85\,\mathrm{cm} = -0.85\,\mathrm{m}\). Then \(\Delta E_P = mg\Delta h = (2.7 \times 10^{-3}\,\mathrm{kg}) \times (9.81\,\mathrm{m\,s^{-2}}) \times (-0.85\,\mathrm{m}) = -0.0225\,\mathrm{J} \approx -2.3 \times 10^{-2}\,\mathrm{J}\).

**Feedback for B:** Incorrect. This calculation results from using raw numbers without converting units: \(2.7 \times 9.81 \times 85 \approx 2250\,\mathrm{J}\). Always convert grams to kilograms (\(\div 1000\)) and centimetres to metres (\(\div 100\)).

---

## Common Misconceptions

### Misconception 1: Confusing Distance Along a Path with Vertical Height
Students frequently substitute the distance an object slides along an incline or hill (such as \(100\,\mathrm{m}\) along a slope) into \(\Delta E_P = mg\Delta h\).
- **Correction:** In the formula \(\Delta E_P = mg\Delta h\), \(\Delta h\) must strictly be the **perpendicular vertical distance** between the initial and final levels.
- If an object moves a distance \(L\) along a plane inclined at angle \(\theta\) to the horizontal, the vertical height change is \(\Delta h = L \sin\theta\). Never use \(L\) directly unless the path is purely vertical.

### Misconception 2: Believing \(\Delta E_P = mg\Delta h\) Holds Across Outer Space
Beginners often assume that \(\Delta E_P = mg\Delta h\) is a universal equation for gravitational potential energy anywhere in the universe.
- **Correction:** It is an approximation valid only near the surface of a planet where the gravitational field strength \(g\) can be considered constant (uniform field). For large distances where \(g\) decreases with distance from the centre of mass, the A2 Level formula involving \(\phi = -\frac{GM}{r}\) must be used.

### Misconception 3: Believing Potential Energy Belongs Only to the Object
People often say "the rock has potential energy".
- **Correction:** Potential energy is stored in the **gravitational field** established between the object and the Earth. If the Earth were removed, the rock by itself would have no gravitational potential energy. It is an interaction energy shared by the Earth-mass system.

### Misconception 4: Forgetting the Minus Sign for Falling Objects
When an object falls, students often write \(\Delta E_P = +mg\Delta h\) and get confused when applying conservation of energy (\(\Delta E_K + \Delta E_P = 0\)).
- **Correction:** When height decreases, \(\Delta h < 0\), which makes \(\Delta E_P < 0\). A decrease in gravitational potential energy supplies the energy needed to increase kinetic energy or do work against resistive forces:
  \[
  -\Delta E_P = \Delta E_K + W_{\text{resistive}}
  \]

### Misconception 5: Unit Prefix Errors
Examination reports consistently note that candidates fail to convert grams to kilograms, or centimetres and millimetres to metres.
- **Correction:** Always inspect the units provided in the question:
  - \(1\,\mathrm{g} = 10^{-3}\,\mathrm{kg}\)
  - \(1\,\mathrm{tonne} = 10^3\,\mathrm{kg}\)
  - \(1\,\mathrm{cm} = 10^{-2}\,\mathrm{m}\)
  - \(1\,\mathrm{mm} = 10^{-3}\,\mathrm{m}\)

---

## Core Recap

- **Gravitational potential energy** is the energy stored by a mass because of its position or height in a gravitational field.
- In a uniform gravitational field where \(g\) is constant:
  \[
  \Delta E_P = mg\Delta h
  \]
- **Derivation steps:**
  1. Downward weight: \(W_{\text{weight}} = mg\).
  2. Upward force at constant speed: \(F = mg\).
  3. Work done: \(W = Fs = (mg)(\Delta h)\).
  4. Energy stored equals work done: \(\Delta E_P = mg\Delta h\).
- **Validity condition:** Valid only in a **uniform gravitational field** where gravitational field strength \(g\) does not change with height.
- **Path independence:** Gravitational potential energy change depends solely on the initial and final vertical levels (\(\Delta h\)); it is completely independent of horizontal displacement and the path taken.
- **Signs:** \(\Delta E_P > 0\) when moving upwards (energy gained); \(\Delta E_P < 0\) when moving downwards (energy released).
- **Next lesson:** In Lesson 6 (`9702_t05_cm02_l06`), we will derive the formula for kinetic energy, \(E_K = \frac{1}{2}mv^2\), using the equations of motion and explore the conversion between gravitational potential energy and kinetic energy.
