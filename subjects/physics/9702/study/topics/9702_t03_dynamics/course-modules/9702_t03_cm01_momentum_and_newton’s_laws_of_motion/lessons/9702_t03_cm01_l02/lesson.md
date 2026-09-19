# Linear momentum and force as the rate of change of momentum

## Why do massive moving objects carry so much impact?

In the previous lesson, you saw that mass is the property of a body that resists changes in motion. A massive object has a large inertia: it is difficult to speed up, difficult to slow down, and difficult to steer around a curve.

However, consider the following real-world comparisons:

- A table tennis ball has a mass of only \(2.7\,\mathrm{g}\). If a friend tosses it to you at \(3.0\,\mathrm{m\,s^{-1}}\), you can catch it effortlessly with your fingertips. Even if a professional player smashes the ball at \(25\,\mathrm{m\,s^{-1}}\), your hand easily stops it without any discomfort.
- Now imagine a heavy cricket ball of mass \(160\,\mathrm{g}\) (nearly 60 times the mass of the table tennis ball). If it is thrown at the same speed of \(25\,\mathrm{m\,s^{-1}}\), attempting to catch it without padded gloves can sting or even fracture a finger.
- Now consider an enormous oil supertanker with a mass of \(300\,000\,\mathrm{tonnes}\) (\(3.0 \times 10^8\,\mathrm{kg}\)). As it approaches a concrete docking pier, its engines are shut down, and it drifts at a barely perceptible speed of just \(0.10\,\mathrm{m\,s^{-1}}\) (about \(10\,\mathrm{cm}\) per second). Despite its tiny speed, if the tanker bumps against the pier, it can crush timber pilings and buckle reinforced steel barriers.

These examples reveal a vital truth about mechanics:

Neither mass alone nor speed alone tells you how much effort is needed to bring a moving body to rest. What matters is the combined effect of both: how much matter is moving, and how fast that matter is traveling.

In physics, this combined "quantity of motion" is called **linear momentum**.

---

## Linear momentum: definition, equation, and units

In Cambridge International AS Level Physics, linear momentum has an exact definition that you must learn word for word:

<a id="definition-9702_def_linear_momentum"></a>

> **Definition to learn: linear momentum.** the product of mass and velocity

Notice the exact wording:
- It is the product of **mass** (a scalar) and **velocity** (a vector).
- You must not write "mass times speed", because speed is a scalar and omits the essential direction of motion.

The mathematical formula follows directly from this definition:

<a id="formula-9702_formula_momentum"></a>

> **Formula to learn: linear momentum.**
>
> \[
> p = mv
> \]

Let us examine each symbol in this formula:
- **\(p\)** is the **linear momentum** of the body. The symbol \(p\) comes from the Latin word *petere*, meaning to go towards or seek out.
- **\(m\)** is the **mass** of the body, measured in kilograms (\(\mathrm{kg}\)).
- **\(v\)** is the **velocity** of the body, measured in metres per second (\(\mathrm{m\,s^{-1}}\)).

### Units of momentum

Because momentum is the product of mass in \(\mathrm{kg}\) and velocity in \(\mathrm{m\,s^{-1}}\), its SI base unit is:

\[
\mathrm{kg\,m\,s^{-1}}
\]

Momentum can also be expressed in an equivalent derived unit: the **newton second**, abbreviated \(\mathrm{N\,s}\).

We can verify that these two unit forms are identical by recalling the definition of the newton from \(F = ma\):

\[
1\,\mathrm{N} = 1\,\mathrm{kg\,m\,s^{-2}}
\]

Multiplying both sides by seconds (\(\mathrm{s}\)) gives:

\[
1\,\mathrm{N\,s} = (1\,\mathrm{kg\,m\,s^{-2}}) \times \mathrm{s} = 1\,\mathrm{kg\,m\,s^{-1}}
\]

Both \(\mathrm{kg\,m\,s^{-1}}\) and \(\mathrm{N\,s}\) are fully accepted in Cambridge examinations. When you are analyzing moving particles, \(\mathrm{kg\,m\,s^{-1}}\) is the natural unit. When you are analyzing forces acting over time intervals (as in collisions), \(\mathrm{N\,s}\) is often more convenient.

---

## Vector nature of momentum and the sign convention

Velocity is a vector quantity having both magnitude and direction. Mass is a positive scalar quantity.

When you multiply a vector (\(\vec{v}\)) by a positive scalar (\(m\)), the resulting quantity (\(\vec{p} = m\vec{v}\)) is also a vector:

> **Linear momentum is a vector quantity that points in the exact same direction as the velocity of the body.**

If a car travels due north, its momentum vector points due north. If a basketball travels downwards towards the floor, its momentum vector points downwards.

### Setting up a sign convention in one dimension

In straight-line motion, you must choose one direction along the line of motion as positive:
- Velocities and momenta in this chosen direction carry a **positive sign** (\(+\)).
- Velocities and momenta in the opposite direction carry a **negative sign** (\(-\)).

For instance, if you choose the forward direction as positive:
- A vehicle of mass \(1200\,\mathrm{kg}\) moving forward at \(20\,\mathrm{m\,s^{-1}}\) has momentum:
  \[
  p = 1200\,\mathrm{kg} \times (+20\,\mathrm{m\,s^{-1}}) = +24\,000\,\mathrm{kg\,m\,s^{-1}}
  \]
- If the same vehicle reverses backward at \(5.0\,\mathrm{m\,s^{-1}}\), its momentum is:
  \[
  p = 1200\,\mathrm{kg} \times (-5.0\,\mathrm{m\,s^{-1}}) = -6000\,\mathrm{kg\,m\,s^{-1}}
  \]

### Change in momentum: the critical rebound case

The change in any physical quantity is defined as its final value minus its initial value:

\[
\Delta p = p_{\mathrm{final}} - p_{\mathrm{initial}} = mv - mu = m(v - u)
\]

where:
- \(u\) is the initial velocity.
- \(v\) is the final velocity.
- \(m\) is the mass of the body.

Pay special attention to what happens when an object bounces or rebounds:

Imagine a rubber ball of mass \(m\) moving horizontally towards a wall with speed \(u\). It strikes the wall and rebounds horizontally in the opposite direction with speed \(v\).

Let us define the direction towards the wall as **positive**:
- Initial velocity: \(u_{\mathrm{initial}} = +u\)
- Initial momentum: \(p_{\mathrm{initial}} = +mu\)
- Final velocity (after rebound): \(v_{\mathrm{final}} = -v\)
- Final momentum: \(p_{\mathrm{final}} = -mv\)

Now calculate the change in momentum of the ball:

\[
\Delta p = p_{\mathrm{final}} - p_{\mathrm{initial}} = (-mv) - (+mu) = -m(v + u)
\]

The negative sign indicates that the change in momentum is directed away from the wall. The **magnitude** of the change in momentum is:

\[
|\Delta p| = m(v + u)
\]

Notice that because velocity reverses direction, the speeds **add together** when determining the change in momentum.

Compare this to a ball that does not bounce, but instead hits the wall and sticks to it (so final velocity is zero):
- Initial momentum: \(+mu\)
- Final momentum: \(0\)
- Change in momentum: \(\Delta p = 0 - (+mu) = -mu\)
- Magnitude of change: \(mu\)

When a ball bounces back with roughly the same speed (\(v \approx u\)), the change in momentum is approximately \(2mu\). That is **twice as large** as the momentum change of an object that simply stops. This is why bouncing impacts exert substantially larger forces than stopping impacts.

---

## Force as the rate of change of momentum

In Lesson 1, you met Newton's second law in the familiar form \(F = ma\). We are now ready to establish the deeper, universal definition of force upon which classical dynamics is built.

In Cambridge International AS Level Physics, force is formally defined through momentum:

<a id="definition-9702_def_force"></a>

> **Definition to learn: force.** the rate of change of momentum of a body

This definition gives the governing law of motion:

<a id="formula-9702_formula_newtons_second_law"></a>

> **Formula to learn: Newton's second law of motion.**
>
> \[
> F = \frac{\Delta p}{\Delta t} = ma
> \]

In words:

> **The resultant force acting on a body is equal to the rate of change of momentum of the body, and acts in the direction of the change in momentum.**

Let us examine the terms:
- **\(F\)** is the **resultant force** acting on the body, measured in newtons (\(\mathrm{N}\)).
- **\(\Delta p\)** is the **change in linear momentum**, measured in kilogram metres per second (\(\mathrm{kg\,m\,s^{-1}}\)) or newton seconds (\(\mathrm{N\,s}\)).
- **\(\Delta t\)** is the **time interval** over which the force acts, measured in seconds (\(\mathrm{s}\)).

### Deriving \(F = ma\) from the rate of change of momentum

Why did we use \(F = ma\) in Lesson 1?

Consider a body whose mass \(m\) remains constant while a resultant force acts on it. Its initial velocity is \(u\) and its final velocity after time \(\Delta t\) is \(v\).

The change in momentum of the body is:

\[
\Delta p = mv - mu = m(v - u)
\]

Substitute this into the definition of force:

\[
F = \frac{\Delta p}{\Delta t} = \frac{m(v - u)}{\Delta t} = m\left(\frac{v - u}{\Delta t}\right)
\]

From kinematics (Topic 2), the rate of change of velocity is the definition of acceleration:

\[
a = \frac{v - u}{\Delta t}
\]

Therefore:

\[
F = ma
\]

This algebraic step demonstrates that:
- **\(F = \frac{\Delta p}{\Delta t}\)** is the universal, foundational definition of force.
- **\(F = ma\)** is a special case of Newton's second law, strictly valid **only when the mass of the body remains constant**.

### Why the momentum definition of force is superior

There are many real physical situations where mass is not constant:
1. **A rocket accelerating into space:** A rocket consumes and expels vast quantities of burning fuel each second. By the time it leaves the atmosphere, the majority of its initial launch mass has been ejected.
2. **A continuous jet of water or air:** When a stream of fluid strikes a wall or an aircraft turbine blade, mass continuously enters and leaves the interaction zone.
3. **A conveyor belt collecting falling material:** As gravel drops onto a moving conveyor belt, the mass of the moving belt increases continuously.

In these systems, an object can move at constant velocity while a force must be applied to continuously accelerate new incoming mass.

If an object travels at a constant velocity \(v\) while its mass changes by \(\Delta m\) over a time interval \(\Delta t\), the rate of change of momentum is:

\[
F = \frac{\Delta p}{\Delta t} = \frac{\Delta(mv)}{\Delta t} = v\,\frac{\Delta m}{\Delta t}
\]

Here, the acceleration of the mass already on the belt is zero (\(a = 0\)), yet a non-zero force \(F = v \frac{\Delta m}{\Delta t}\) is required to bring the newly added mass up to the belt speed. The equation \(F = ma\) fails to describe this situation, but \(F = \frac{\Delta p}{\Delta t}\) describes it perfectly.

---

## Impulse and force-time graphs

Rearranging the definition of force reveals another powerful relationship:

\[
F = \frac{\Delta p}{\Delta t} \implies \Delta p = F\,\Delta t
\]

When a constant resultant force \(F\) acts on a body for a time duration \(\Delta t\), the product \(F \Delta t\) is called the **impulse** of the force:

\[
\text{Impulse} = F\,\Delta t = \Delta p
\]

- Impulse is measured in **newton seconds** (\(\mathrm{N\,s}\)).
- The impulse delivered to a body is equal to the **change in momentum** of that body.

### Graphical interpretation 1: Momentum-time graphs

On a graph plotting linear momentum \(p\) on the vertical axis against time \(t\) on the horizontal axis:

- The **gradient** (slope) of the line represents the rate of change of momentum:
  \[
  \text{Gradient} = \frac{\Delta p}{\Delta t} = F
  \]
- If the line is straight, the gradient is constant, meaning a **constant resultant force** acts on the body.
- If the line is horizontal, the gradient is zero, meaning the **resultant force is zero** (\(F = 0\)).
- If the line is curved, the resultant force varies with time. The instantaneous resultant force at any time \(t\) is equal to the gradient of the tangent to the curve at that point.

### Graphical interpretation 2: Force-time graphs

In real collisions (such as a bat hitting a baseball or two cars colliding), the contact force is not constant. The force starts at zero when the surfaces first touch, rises rapidly to a high peak value as the objects compress, and then drops back to zero as they separate.

On a graph plotting resultant force \(F\) on the vertical axis against time \(t\) on the horizontal axis:

- The product of force and time represents an area on the graph:
  \[
  \text{Area under a force-time graph} = \Delta p = \text{Impulse}
  \]
- For a constant force, the area is simply a rectangle: \(\text{Area} = F \times \Delta t\).
- For a force that increases linearly from zero to a maximum peak \(F_{\mathrm{max}}\) and then decreases linearly back to zero over time \(\Delta t\), the shape is a triangle:
  \[
  \text{Area} = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2}\,F_{\mathrm{max}}\,\Delta t
  \]
- For any force profile, the total area enclosed between the force curve and the time axis equals the net change in momentum produced on the object.

---

## Original worked examples

### Worked Example 1: Tennis ball rebounding from a wall

A tennis player strikes a ball of mass \(58\,\mathrm{g}\) horizontally towards a smooth vertical practice wall. The ball strikes the wall at a horizontal velocity of \(28\,\mathrm{m\,s^{-1}}\). The ball compresses against the brick surface and rebounds horizontally along its original path with a speed of \(18\,\mathrm{m\,s^{-1}}\).

The time during which the ball is in contact with the wall is \(12\,\mathrm{ms}\).

1. Calculate the initial linear momentum and the final linear momentum of the ball.
2. Determine the change in momentum of the ball during the impact.
3. Calculate the magnitude and state the direction of the average resultant force exerted by the wall on the ball.
4. State the impulse delivered to the ball by the wall.

#### Step 1: Set up units and the sign convention
Convert all quantities into standard SI units:
- Mass: \(m = 58\,\mathrm{g} = 0.058\,\mathrm{kg}\)
- Contact time: \(\Delta t = 12\,\mathrm{ms} = 12 \times 10^{-3}\,\mathrm{s} = 0.012\,\mathrm{s}\)

Choose the direction of the ball's incoming flight (towards the wall) as the **positive direction** (\(+\)):
- Initial velocity: \(u = +28\,\mathrm{m\,s^{-1}}\)
- Final velocity (rebounding away from the wall): \(v = -18\,\mathrm{m\,s^{-1}}\)

#### Step 2: Calculate initial and final momentum
Initial momentum:
\[
p_{\mathrm{initial}} = mu = 0.058\,\mathrm{kg} \times (+28\,\mathrm{m\,s^{-1}}) = +1.624\,\mathrm{kg\,m\,s^{-1}} \approx +1.6\,\mathrm{kg\,m\,s^{-1}}
\]

Final momentum:
\[
p_{\mathrm{final}} = mv = 0.058\,\mathrm{kg} \times (-18\,\mathrm{m\,s^{-1}}) = -1.044\,\mathrm{kg\,m\,s^{-1}} \approx -1.0\,\mathrm{kg\,m\,s^{-1}}
\]

#### Step 3: Determine the change in momentum
Apply \(\Delta p = p_{\mathrm{final}} - p_{\mathrm{initial}}\):
\[
\Delta p = (-1.044\,\mathrm{kg\,m\,s^{-1}}) - (+1.624\,\mathrm{kg\,m\,s^{-1}}) = -2.668\,\mathrm{kg\,m\,s^{-1}}
\]

Rounding to 2 significant figures gives \(\Delta p = -2.7\,\mathrm{kg\,m\,s^{-1}}\).

The magnitude of the change in momentum is \(2.7\,\mathrm{kg\,m\,s^{-1}}\) (or \(2.7\,\mathrm{N\,s}\)). The negative sign shows that the change is directed away from the wall.

#### Step 4: Calculate the average resultant force
Apply Newton's second law:
\[
F = \frac{\Delta p}{\Delta t} = \frac{-2.668\,\mathrm{kg\,m\,s^{-1}}}{0.012\,\mathrm{s}} = -222.33\,\mathrm{N}
\]

Rounding to 2 significant figures gives \(F = -220\,\mathrm{N}\).

- Magnitude: \(220\,\mathrm{N}\)
- Direction: Away from the wall (opposite to the incoming velocity)

#### Step 5: State the impulse
The impulse delivered to the ball is equal to the change in momentum:
\[
\text{Impulse} = \Delta p = -2.7\,\mathrm{N\,s}
\]

**Answers:**
1. Initial momentum = \(+1.6\,\mathrm{kg\,m\,s^{-1}}\); Final momentum = \(-1.0\,\mathrm{kg\,m\,s^{-1}}\)
2. Change in momentum = \(-2.7\,\mathrm{kg\,m\,s^{-1}}\) (magnitude \(2.7\,\mathrm{kg\,m\,s^{-1}}\))
3. Average force = \(220\,\mathrm{N}\) directed away from the wall
4. Impulse = \(-2.7\,\mathrm{N\,s}\) (magnitude \(2.7\,\mathrm{N\,s}\))

---

### Worked Example 2: Continuous momentum transfer from a water jet

An industrial cleaning system directs a steady horizontal jet of water perpendicularly against a flat vertical wall to strip paint.

The water emerges from a nozzle with a speed of \(35\,\mathrm{m\,s^{-1}}\). The cross-sectional area of the water jet is \(4.0 \times 10^{-4}\,\mathrm{m^2}\). The density of water is \(\rho = 1000\,\mathrm{kg\,m^{-3}}\).

Upon hitting the wall, the water loses all its forward horizontal velocity and runs down the wall vertically without splashing backwards.

1. Show that the mass of water striking the wall each second is \(14\,\mathrm{kg}\).
2. Calculate the forward linear momentum carried by the water striking the wall each second.
3. Determine the average horizontal force exerted by the water jet on the wall.
4. If the cleaning system is tested against a rigid rubber sheet causing the water to bounce backwards elastically with a rebound speed of \(25\,\mathrm{m\,s^{-1}}\), calculate the new horizontal force exerted on the sheet.

#### Step 1: Calculate mass flow rate
In a time interval \(\Delta t = 1.0\,\mathrm{s}\), the length of the cylinder of water emerging from the nozzle is:
\[
L = v\,\Delta t = 35\,\mathrm{m\,s^{-1}} \times 1.0\,\mathrm{s} = 35\,\mathrm{m}
\]

The volume of water striking the wall each second is:
\[
\frac{\Delta V}{\Delta t} = A \times v = (4.0 \times 10^{-4}\,\mathrm{m^2}) \times 35\,\mathrm{m\,s^{-1}} = 0.014\,\mathrm{m^3\,s^{-1}}
\]

The mass flow rate is:
\[
\frac{\Delta m}{\Delta t} = \rho\,\frac{\Delta V}{\Delta t} = 1000\,\mathrm{kg\,m^{-3}} \times 0.014\,\mathrm{m^3\,s^{-1}} = 14\,\mathrm{kg\,s^{-1}}
\]

Thus, \(14\,\mathrm{kg}\) of water strikes the wall each second.

#### Step 2: Calculate initial momentum delivered per second
Each second, mass \(\Delta m = 14\,\mathrm{kg}\) arrives with horizontal velocity \(u = +35\,\mathrm{m\,s^{-1}}\).
\[
p_{\mathrm{initial}} = (\Delta m)u = 14\,\mathrm{kg} \times 35\,\mathrm{m\,s^{-1}} = 490\,\mathrm{kg\,m\,s^{-1}}
\]

The water delivers \(490\,\mathrm{kg\,m\,s^{-1}}\) of forward momentum to the impact zone each second.

#### Step 3: Determine the force exerted on the wall
Because the water loses all forward velocity, its final horizontal velocity is \(v = 0\).

The change in momentum of the water each second is:
\[
\frac{\Delta p}{\Delta t} = \frac{0 - 490\,\mathrm{kg\,m\,s^{-1}}}{1.0\,\mathrm{s}} = -490\,\mathrm{N}
\]

The wall exerts a force of \(-490\,\mathrm{N}\) on the incoming water (pushing backward to halt it).

By Newton's third law, the water exerts an equal and opposite force on the wall:
\[
F_{\mathrm{on\,wall}} = +490\,\mathrm{N} \text{ directed into the wall}
\]

Alternatively, you can compute this directly using the mass flow rate equation:
\[
F = v\,\frac{\Delta m}{\Delta t} = 35\,\mathrm{m\,s^{-1}} \times 14\,\mathrm{kg\,s^{-1}} = 490\,\mathrm{N}
\]

#### Step 4: Rebounding water stream
When the water rebounds backwards at \(v = -25\,\mathrm{m\,s^{-1}}\), the change in velocity for each kilogram of water is:
\[
\Delta v = v - u = -25\,\mathrm{m\,s^{-1}} - (+35\,\mathrm{m\,s^{-1}}) = -60\,\mathrm{m\,s^{-1}}
\]

The rate of change of momentum of the water is:
\[
\frac{\Delta p}{\Delta t} = \left(\frac{\Delta m}{\Delta t}\right)\Delta v = 14\,\mathrm{kg\,s^{-1}} \times (-60\,\mathrm{m\,s^{-1}}) = -840\,\mathrm{N}
\]

Therefore, the force exerted on the rubber sheet is:
\[
F_{\mathrm{on\,sheet}} = +840\,\mathrm{N}
\]

Notice that reversing the stream increases the impact force from \(490\,\mathrm{N}\) to \(840\,\mathrm{N}\), because the wall must both stop the forward motion and accelerate the water in the reverse direction.

**Answers:**
1. Mass flow rate = \(14\,\mathrm{kg\,s^{-1}}\)
2. Momentum delivered per second = \(490\,\mathrm{kg\,m\,s^{-1}}\) (or \(490\,\mathrm{N\,s}\) per second)
3. Average horizontal force on the wall = \(490\,\mathrm{N}\)
4. New force with rebound = \(840\,\mathrm{N}\)

---

### Worked Example 3: Finding exit speed from a force-time graph

A golf club head strikes a stationary golf ball of mass \(45\,\mathrm{g}\). The collision lasts for a total duration of \(0.60\,\mathrm{ms}\).

A high-speed sensor measures the contact force between the club and the ball. The force increases uniformly from \(0\,\mathrm{N}\) at \(t = 0\) to a peak force of \(4500\,\mathrm{N}\) at \(t = 0.20\,\mathrm{ms}\), and then decreases uniformly back to \(0\,\mathrm{N}\) at \(t = 0.60\,\mathrm{ms}\).

1. State the physical quantity represented by the area under this force-time graph.
2. Calculate the impulse delivered to the golf ball.
3. Calculate the launch speed of the golf ball as it leaves the club face.
4. Determine the average force exerted on the ball during the impact.

#### Step 1: Identify graph features and units
- Mass of ball: \(m = 45\,\mathrm{g} = 0.045\,\mathrm{kg}\)
- Total base of triangle: \(\Delta t = 0.60\,\mathrm{ms} = 0.60 \times 10^{-3}\,\mathrm{s} = 6.0 \times 10^{-4}\,\mathrm{s}\)
- Peak height of triangle: \(F_{\mathrm{max}} = 4500\,\mathrm{N}\)
- Initial speed of ball: \(u = 0\,\mathrm{m\,s^{-1}}\)

The area enclosed between the force-time curve and the time axis represents the **impulse**, which is equal to the **change in linear momentum** (\(\Delta p\)).

#### Step 2: Calculate the impulse (area of triangle)
\[
\text{Area} = \frac{1}{2} \times \text{base} \times \text{height}
\]

\[
\text{Impulse} = \frac{1}{2} \times (6.0 \times 10^{-4}\,\mathrm{s}) \times 4500\,\mathrm{N} = 1.35\,\mathrm{N\,s}
\]

#### Step 3: Calculate the launch speed
Because the ball starts from rest (\(p_{\mathrm{initial}} = 0\)), all the impulse goes into creating its final momentum:
\[
\Delta p = p_{\mathrm{final}} - 0 = mv
\]

\[
1.35\,\mathrm{N\,s} = 0.045\,\mathrm{kg} \times v
\]

Rearranging for \(v\):
\[
v = \frac{1.35\,\mathrm{N\,s}}{0.045\,\mathrm{kg}} = 30\,\mathrm{m\,s^{-1}}
\]

#### Step 4: Calculate the average force
The average force \(F_{\mathrm{avg}}\) is the constant force that would deliver the exact same impulse over the same time interval:
\[
F_{\mathrm{avg}} = \frac{\Delta p}{\Delta t} = \frac{1.35\,\mathrm{N\,s}}{6.0 \times 10^{-4}\,\mathrm{s}} = 2250\,\mathrm{N}
\]

Notice that for any triangular force profile, the average force is exactly half of the peak force:
\[
F_{\mathrm{avg}} = \frac{1}{2}\,F_{\mathrm{max}} = \frac{1}{2} \times 4500\,\mathrm{N} = 2250\,\mathrm{N}
\]

**Answers:**
1. The area represents the impulse, or the change in momentum of the ball.
2. Impulse = \(1.35\,\mathrm{N\,s}\)
3. Launch speed = \(30\,\mathrm{m\,s^{-1}}\)
4. Average force = \(2250\,\mathrm{N}\) (or \(2.3 \times 10^3\,\mathrm{N}\) to 2 significant figures)

---

## Active learning checks

### Check 1: Vector nature of momentum on rebound

A squash ball of mass \(0.024\,\mathrm{kg}\) travels horizontally with a speed of \(18\,\mathrm{m\,s^{-1}}\). It strikes the front wall of a squash court and rebounds horizontally along its original line of flight with a speed of \(14\,\mathrm{m\,s^{-1}}\).

What is the magnitude of the change in momentum of the ball?

- **A.** \(0.77\,\mathrm{kg\,m\,s^{-1}}\)
- **B.** \(0.096\,\mathrm{kg\,m\,s^{-1}}\)

**Feedback for A:** Correct. Momentum is a vector quantity. Choose the direction towards the wall as positive. The initial momentum is \(p_i = 0.024 \times (+18) = +0.432\,\mathrm{kg\,m\,s^{-1}}\). The final momentum after rebound is \(p_f = 0.024 \times (-14) = -0.336\,\mathrm{kg\,m\,s^{-1}}\). The change in momentum is \(\Delta p = p_f - p_i = -0.336 - (+0.432) = -0.768\,\mathrm{kg\,m\,s^{-1}}\). The magnitude is \(0.768\,\mathrm{kg\,m\,s^{-1}} \approx 0.77\,\mathrm{kg\,m\,s^{-1}}\). Because the ball reverses direction, the speeds add together in the change: \(\Delta v = 18 + 14 = 32\,\mathrm{m\,s^{-1}}\).

**Feedback for B:** Incorrect. You subtracted the speeds: \(18 - 14 = 4.0\,\mathrm{m\,s^{-1}}\), giving \(0.024 \times 4.0 = 0.096\,\mathrm{kg\,m\,s^{-1}}\). This treats momentum as a scalar without direction. Because the ball reversed direction, its velocity changed from \(+18\,\mathrm{m\,s^{-1}}\) to \(-14\,\mathrm{m\,s^{-1}}\), producing a total velocity change of \(-32\,\mathrm{m\,s^{-1}}\).

---

### Check 2: Scientific definition of force

Which statement defines force according to Cambridge International AS Level Physics?

- **A.** Force is the rate of change of momentum of a body.
- **B.** Force is the product of the mass of a body and its acceleration.

**Feedback for A:** Correct. Newton's second law fundamentally defines resultant force as the rate of change of momentum (\(F = \frac{\Delta p}{\Delta t}\)). This definition holds universally, including when mass changes.

**Feedback for B:** Incorrect. While \(F = ma\) is widely used to calculate forces for objects of constant mass, it is a derived consequence of Newton's second law, not its scientific definition. When Cambridge exam papers ask for the definition of force, "rate of change of momentum" is required; "mass times acceleration" is specifically marked as incomplete or incorrect.

---

### Check 3: Stopping time for a vehicle

An electric delivery van of mass \(1500\,\mathrm{kg}\) travels along a straight level road at an initial speed of \(12\,\mathrm{m\,s^{-1}}\). The driver applies the regenerative braking system, which exerts a constant total retarding force of \(3600\,\mathrm{N}\) until the van stops.

How long does it take for the van to come to rest?

- **A.** \(5.0\,\mathrm{s}\)
- **B.** \(0.20\,\mathrm{s}\)

**Feedback for A:** Correct. The initial momentum of the van is \(p_i = 1500\,\mathrm{kg} \times 12\,\mathrm{m\,s^{-1}} = 18\,000\,\mathrm{kg\,m\,s^{-1}}\). The final momentum is \(0\,\mathrm{kg\,m\,s^{-1}}\), so the magnitude of the change in momentum is \(\Delta p = 18\,000\,\mathrm{N\,s}\). Using \(F = \frac{\Delta p}{\Delta t}\), rearrange for time: \(\Delta t = \frac{\Delta p}{F} = \frac{18\,000\,\mathrm{N\,s}}{3600\,\mathrm{N}} = 5.0\,\mathrm{s}\).

**Feedback for B:** Incorrect. You divided force by momentum change: \(\frac{3600}{18\,000} = 0.20\,\mathrm{s}\). The correct algebraic rearrangement of \(F = \frac{\Delta p}{\Delta t}\) is \(\Delta t = \frac{\Delta p}{F}\), which yields \(\frac{18\,000}{3600} = 5.0\,\mathrm{s}\).

---

### Check 4: Continuous momentum transfer from a falling stream

A conveyor chute drops gravel vertically onto a stationary horizontal deflector plate at a steady rate of \(25\,\mathrm{kg\,s^{-1}}\). The gravel hits the plate vertically with a speed of \(6.0\,\mathrm{m\,s^{-1}}\) and immediately slides off horizontally with zero vertical velocity.

What vertical force does the gravel exert on the deflector plate?

- **A.** \(150\,\mathrm{N}\)
- **B.** \(4.2\,\mathrm{N}\)

**Feedback for A:** Correct. Each second, \(25\,\mathrm{kg}\) of gravel loses its vertical velocity of \(6.0\,\mathrm{m\,s^{-1}}\). The rate of change of vertical momentum is \(F = v\,\frac{\Delta m}{\Delta t} = 6.0\,\mathrm{m\,s^{-1}} \times 25\,\mathrm{kg\,s^{-1}} = 150\,\mathrm{N}\). By Newton's third law, the gravel exerts an equal downward force of \(150\,\mathrm{N}\) on the plate.

**Feedback for B:** Incorrect. You divided the mass flow rate by the speed: \(\frac{25}{6.0} \approx 4.2\). Force has units of newtons (\(\mathrm{kg\,m\,s^{-2}}\)), which requires multiplying mass flow rate (\(\mathrm{kg\,s^{-1}}\)) by velocity (\(\mathrm{m\,s^{-1}}\)): \(25 \times 6.0 = 150\,\mathrm{N}\).

---

## Mistakes worth repairing

### Mistake 1: Treating momentum as a scalar and subtracting speeds during rebounds

The single most common mistake in momentum calculations is forgetting that momentum is a vector. When a ball rebounds off a wall from speed \(u\) to speed \(v\), students frequently write:

\[
\Delta p = m(u - v) \quad \text{(INCORRECT)}
\]

This calculation treats velocity as a scalar speed. If a ball hits at \(15\,\mathrm{m\,s^{-1}}\) and rebounds at \(10\,\mathrm{m\,s^{-1}}\), this error gives a speed change of \(5\,\mathrm{m\,s^{-1}}\).

In reality, the ball was halted from \(+15\,\mathrm{m\,s^{-1}}\) to \(0\), and then accelerated in the opposite direction from \(0\) to \(-10\,\mathrm{m\,s^{-1}}\). The total change in velocity is \((-10) - (+15) = -25\,\mathrm{m\,s^{-1}}\). Always assign a clear sign convention before calculating \(\Delta p\).

### Mistake 2: Confusing linear momentum with kinetic energy

Students often mix up the properties of linear momentum (\(p = mv\)) and kinetic energy (\(E_k = \frac{1}{2}mv^2\)):

| Property | Linear Momentum (\(p\)) | Kinetic Energy (\(E_k\)) |
| :--- | :--- | :--- |
| **Formula** | \(p = mv\) | \(E_k = \frac{1}{2}mv^2\) |
| **Quantity type** | Vector (has direction and sign) | Scalar (always positive or zero) |
| **SI unit** | \(\mathrm{kg\,m\,s^{-1}}\) or \(\mathrm{N\,s}\) | \(\mathrm{J}\) (joules) or \(\mathrm{kg\,m^2\,s^{-2}}\) |
| **Speed dependency** | Proportional to \(v\) | Proportional to \(v^2\) |

They are linked by the useful identity:

\[
E_k = \frac{p^2}{2m}
\]

If you double the velocity of an object, its momentum doubles, but its kinetic energy quadruples. Furthermore, two objects moving in opposite directions can have equal and opposite momenta that sum to zero (\(+p + (-p) = 0\)), whereas their kinetic energies are positive scalars that always add together.

### Mistake 3: Believing force is needed to maintain momentum

A persistent misconception is that a body with large momentum must currently have a large resultant force acting on it.

In reality:
- Momentum is the measure of an object's current quantity of motion.
- Resultant force measures the **rate at which momentum is changing**.
- A spacecraft drifting through deep space at \(15\,000\,\mathrm{m\,s^{-1}}\) has an enormous momentum (\(p = mv\)), but the resultant force acting on it is exactly **zero**.
- Force is required only to **change** momentum: to speed the spacecraft up, slow it down, or redirect its path.

### Mistake 4: Stating that force is defined as mass times acceleration

When asked "Define force" or "State Newton's second law", many candidates write "\(F = ma\)" or "mass times acceleration".

In Cambridge 9702 mark schemes:
- The accepted definition is **rate of change of momentum** (\(\frac{\Delta p}{\Delta t}\)).
- Stating "\(F = ma\)" earns zero marks unless qualified by stating that mass must be constant.
- Whenever you are asked to define force, always state: **the rate of change of momentum of a body**.

### Mistake 5: Confusing the gradient and area of motion graphs

Students frequently mix up the mathematical operations on graphs:
- On a **momentum-time** graph: the **gradient** is force (\(F = \frac{\Delta p}{\Delta t}\)).
- On a **force-time** graph: the **area under the line** is change in momentum or impulse (\(\Delta p = F\,\Delta t\)).

Always check the vertical axis label before analyzing a graph.

---

## Core recap

- **Linear momentum** is defined as the product of mass and velocity:
  \[
  p = mv
  \]
- Linear momentum is a **vector quantity** having the same direction as velocity.
- The SI unit of momentum is \(\mathrm{kg\,m\,s^{-1}}\), which is identical to the newton second (\(\mathrm{N\,s}\)).
- In one dimension, always establish a positive direction. When an object reverses direction, its change in momentum is:
  \[
  \Delta p = m(v_{\mathrm{final}} - u_{\mathrm{initial}}) = m(-v - u) = -m(v + u)
  \]
- **Force** is defined as the rate of change of momentum of a body:
  \[
  F = \frac{\Delta p}{\Delta t}
  \]
- When mass \(m\) is constant, this definition leads directly to \(F = ma\).
- When mass varies at constant velocity, the force is \(F = v\,\frac{\Delta m}{\Delta t}\).
- **Impulse** is defined as \(F\,\Delta t\) and equals the change in momentum \(\Delta p\).
- On a **momentum-time graph**, the **gradient** equals the resultant force.
- On a **force-time graph**, the **area under the graph** equals the change in momentum (impulse).

---

## Next lesson preview

In the next lesson (**Lesson 3: Each of Newton's laws of motion**), you will bring together inertia, acceleration, and momentum to formally state and apply all three of Newton's laws of motion. You will also examine the concept of weight as the gravitational force acting on a mass in a gravitational field.
