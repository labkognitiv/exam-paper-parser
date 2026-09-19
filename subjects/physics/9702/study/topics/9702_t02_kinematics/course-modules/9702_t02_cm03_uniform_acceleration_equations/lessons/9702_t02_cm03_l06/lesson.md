# The constant-acceleration model and Choosing and using an equation and Multi-stage and reverse problems

## Check the model before using an equation

Imagine a trolley moving along a straight track. Each second, its velocity increases by the same amount. Its **acceleration is constant**.

The kinematic equations in this lesson model only that specific type of motion: **uniformly accelerated motion in a straight line**. Before applying any equation, you must always ask two essential questions:

1. Is the motion along one straight line?
2. Is the acceleration constant in both magnitude and direction throughout the entire interval?

If either answer is no, you cannot use one constant-acceleration equation for the whole motion. For example, a falling stone experiences nearly constant acceleration in a uniform gravitational field when air resistance is negligible. However, if air resistance increases noticeably as the stone speeds up, the acceleration decreases. The model is then invalid for the entire fall.

## Controlled definitions and symbols

Choose one positive direction along the straight line before writing any values. A negative sign denotes the opposite direction.

<a id="definition-9702_def_displacement"></a>

> **Definition to learn: displacement.** distance in a specified direction from a point

Displacement is represented by the symbol \(s\), with unit metre, \(\mathrm{m}\).

<a id="definition-9702_def_velocity"></a>

> **Definition to learn: velocity.** rate of change of displacement

Velocity has the unit \(\mathrm{m\,s^{-1}}\). In any chosen interval of motion:

- **\(u\)** represents the **initial velocity** at the start of the interval, in \(\mathrm{m\,s^{-1}}\).
- **\(v\)** represents the **final velocity** at the end of the interval, in \(\mathrm{m\,s^{-1}}\).

<a id="definition-9702_def_acceleration"></a>

> **Definition to learn: acceleration.** rate of change of velocity

Acceleration is represented by \(a\), measured in metres per second squared, \(\mathrm{m\,s^{-2}}\). It quantifies the change in velocity, in \(\mathrm{m\,s^{-1}}\), occurring each second.

## Deriving the equations of motion

Cambridge syllabus outcome 9702_t02_m01_o06 requires deriving these equations directly from the definitions of velocity and acceleration.

### Derivation 1: Final velocity from acceleration

Start from the fundamental definition of acceleration:

<a id="formula-9702_formula_acceleration"></a>

> **Formula to learn: Acceleration.**
>
> \[
> a = \frac{\Delta v}{\Delta t}
> \]

Over a time interval \(t\), the change in velocity is \(\Delta v = v - u\). Therefore:

\[
a = \frac{v - u}{t}
\]

Multiply both sides by \(t\):

\[
at = v - u
\]

Add \(u\) to both sides:

\[
v = u + at
\]

<a id="formula-9702_formula_constant_acceleration_velocity"></a>

> **Formula to learn: Constant-acceleration velocity.**
>
> \[
> v = u + at
> \]

This equation states that final velocity equals initial velocity plus the change in velocity (\(at\)). It applies to straight-line motion where \(a\) is constant.

### Derivation 2: Displacement from average velocity

Start from the definition of average velocity:

<a id="formula-9702_formula_average_velocity"></a>

> **Formula to learn: Average velocity.**
>
> \[
> \vec{v}_{\mathrm{avg}} = \frac{\Delta\vec{s}}{\Delta t}
> \]

When acceleration is constant, velocity changes at a uniform rate. The average velocity across the interval is simply the arithmetic mean of the initial and final velocities:

\[
v_{\mathrm{avg}} = \frac{u + v}{2}
\]

Displacement \(s\) over time \(t\) is average velocity multiplied by time:

\[
s = \frac{u + v}{2}t
\]

Now substitute \(v = u + at\) into this expression:

\[
s = \frac{u + (u + at)}{2}t = \frac{2u + at}{2}t
\]

Expand the bracket:

\[
s = ut + \frac{1}{2}at^2
\]

<a id="formula-9702_formula_constant_acceleration_displacement"></a>

> **Formula to learn: Constant-acceleration displacement.**
>
> \[
> s = ut + \frac{1}{2}at^2
> \]

Check the units of both terms on the right-hand side:

- \([ut] = \mathrm{m\,s^{-1}} \times \mathrm{s} = \mathrm{m}\)
- \([\frac{1}{2}at^2] = \mathrm{m\,s^{-2}} \times \mathrm{s^2} = \mathrm{m}\)

The factor \(\frac{1}{2}\) is dimensionless. Both terms represent displacements in metres and can be added.

### Derivation 3: The equation without time

To relate velocities, acceleration and displacement without involving time \(t\), rearrange \(v = u + at\) to make \(t\) the subject:

\[
t = \frac{v - u}{a}
\]

Substitute this into the displacement expression \(s = \frac{u + v}{2}t\):

\[
s = \frac{u + v}{2}\left(\frac{v - u}{a}\right)
\]

Multiply both sides by \(2a\):

\[
2as = (v + u)(v - u)
\]

The right-hand side is a difference of squares:

\[
(v + u)(v - u) = v^2 - u^2
\]

Therefore:

\[
2as = v^2 - u^2
\]

Add \(u^2\) to both sides:

\[
v^2 = u^2 + 2as
\]

<a id="formula-9702_formula_constant_acceleration_velocity_displacement"></a>

> **Formula to learn: Constant-acceleration velocity and displacement.**
>
> \[
> v^2 = u^2 + 2as
> \]

Unit check:
- \([v^2] = (\mathrm{m\,s^{-1}})^2 = \mathrm{m^2\,s^{-2}}\)
- \([2as] = \mathrm{m\,s^{-2}} \times \mathrm{m} = \mathrm{m^2\,s^{-2}}\)

Both sides have matching units of \(\mathrm{m^2\,s^{-2}}\).

An object starts from rest and moves with constant acceleration \(a\). Which expression correctly gives its displacement after time \(t\)?

- **A:** \(s = \frac{1}{2}at^2\)
- **B:** \(s = at^2\)

**Feedback for A:** Correct. Starting from rest means \(u = 0\), so the term \(ut\) becomes zero, leaving \(s = \frac{1}{2}at^2\).

**Feedback for B:** Not correct. Setting \(u = 0\) eliminates the \(ut\) term, but the factor \(\frac{1}{2}\) in the second term remains. Dropping \(\frac{1}{2}\) would double the actual displacement.

## Choosing and using an equation

In any kinematics problem, there are five core quantities:

- **\(s\)** = displacement (\(\mathrm{m}\))
- **\(u\)** = initial velocity (\(\mathrm{m\,s^{-1}}\))
- **\(v\)** = final velocity (\(\mathrm{m\,s^{-1}}\))
- **\(a\)** = acceleration (\(\mathrm{m\,s^{-2}}\))
- **\(t\)** = time interval (\(\mathrm{s}\))

Every constant-acceleration formula contains four of these five variables and omits exactly one:

| Equation | Missing quantity | When to use |
| --- | --- | --- |
| \(v = u + at\) | \(s\) (displacement) | When displacement is neither given nor required |
| \(s = \frac{u + v}{2}t\) | \(a\) (acceleration) | When acceleration is not involved |
| \(s = ut + \frac{1}{2}at^2\) | \(v\) (final velocity) | When final velocity is neither given nor required |
| \(v^2 = u^2 + 2as\) | \(t\) (time) | When time is neither given nor required |

### Extracting hidden information

Physics questions often state values through standard phrases:

- "starts from rest" or "initially stationary" \(\implies u = 0\)
- "comes to rest", "stops", or "brakes to a halt" \(\implies v = 0\)
- "constant velocity" or "uniform speed" \(\implies a = 0\)

### Structured selection routine

1. **Set convention:** Choose a positive direction along the line of motion.
2. **List variables:** Write down \(s, u, v, a, t\) and record known numerical values with signs and units.
3. **Identify target:** Circle the quantity you need to find.
4. **Select equation:** Find the single equation that contains your target and the three known quantities.
5. **Rearrange first:** Rearrange algebraically before substituting numbers.
6. **Substitute and evaluate:** Calculate the numerical answer and state the correct SI unit and appropriate significant figures.

An athlete running forward at \(8.0\ \mathrm{m\,s^{-1}}\) slows down uniformly to a stop over a distance of \(16\ \mathrm{m}\). Time is not recorded. Which equation provides the direct route to calculate the acceleration?

- **A:** \(v^2 = u^2 + 2as\)
- **B:** \(v = u + at\)

**Feedback for A:** Correct. The knowns are \(u = 8.0\ \mathrm{m\,s^{-1}}\), \(v = 0\), and \(s = 16\ \mathrm{m}\). The target is \(a\). Time \(t\) is absent, so \(v^2 = u^2 + 2as\) is the direct equation.

**Feedback for B:** Not correct. This equation contains time \(t\), which is neither known nor requested. Using it introduces an unnecessary unknown.

### Worked example 1: Single-stage motion from rest

A trolley starts from rest on a straight horizontal track and accelerates with a constant acceleration of \(+2.5\ \mathrm{m\,s^{-2}}\) for \(4.0\ \mathrm{s}\).

Calculate:
(a) the final velocity of the trolley;
(b) the displacement of the trolley during this time.

**Step 1: List the variables.**
Take the forward direction as positive.
- \(u = 0\ \mathrm{m\,s^{-1}}\) (starts from rest)
- \(a = +2.5\ \mathrm{m\,s^{-2}}\)
- \(t = 4.0\ \mathrm{s}\)
- Targets: \(v\) and \(s\)

**Step 2: Find final velocity \(v\).**
Use \(v = u + at\):

\[
v = 0 + (2.5\ \mathrm{m\,s^{-2}})(4.0\ \mathrm{s}) = +10\ \mathrm{m\,s^{-1}}
\]

**Step 3: Find displacement \(s\).**
Use \(s = ut + \frac{1}{2}at^2\):

\[
s = (0)(4.0\ \mathrm{s}) + \frac{1}{2}(2.5\ \mathrm{m\,s^{-2}})(4.0\ \mathrm{s})^2
\]

\[
s = 0 + \frac{1}{2}(2.5)(16) = +20\ \mathrm{m}
\]

**Answer:** (a) Final velocity is **\(+10\ \mathrm{m\,s^{-1}}\)** forward. (b) Displacement is **\(+20\ \mathrm{m}\)** forward.

**Check:** The average velocity is \(\frac{0 + 10}{2} = 5.0\ \mathrm{m\,s^{-1}}\). Over \(4.0\ \mathrm{s}\), displacement is \(5.0 \times 4.0 = 20\ \mathrm{m}\), fully consistent with the result.

### Worked example 2: Braking distance without time

A car travels along a straight road at \(+24\ \mathrm{m\,s^{-1}}\). The driver brakes with constant acceleration \(-4.0\ \mathrm{m\,s^{-2}}\) until the car comes to a complete stop.

Calculate the distance travelled by the car while braking.

**Step 1: List the variables.**
Take the forward direction as positive.
- \(u = +24\ \mathrm{m\,s^{-1}}\)
- \(v = 0\ \mathrm{m\,s^{-1}}\) (stops)
- \(a = -4.0\ \mathrm{m\,s^{-2}}\)
- Target: \(s\) (time \(t\) is not given)

**Step 2: Select and rearrange the equation.**
Use \(v^2 = u^2 + 2as\):

\[
v^2 - u^2 = 2as \implies s = \frac{v^2 - u^2}{2a}
\]

**Step 3: Substitute signed values.**

\[
s = \frac{(0\ \mathrm{m\,s^{-1}})^2 - (24\ \mathrm{m\,s^{-1}})^2}{2(-4.0\ \mathrm{m\,s^{-2}})} = \frac{-576\ \mathrm{m^2\,s^{-2}}}{-8.0\ \mathrm{m\,s^{-2}}} = +72\ \mathrm{m}
\]

**Answer:** The braking distance is **\(72\ \mathrm{m}\)** forward.

**Check:** Both numerator and denominator are negative, yielding a positive forward displacement. The unit \(\mathrm{m^2\,s^{-2}} \div \mathrm{m\,s^{-2}} = \mathrm{m}\) is correct.

## Multi-stage and reverse problems

In many realistic journeys, an object changes its acceleration partway through. For example, a vehicle might accelerate from rest, cruise at constant speed, and then brake to a halt.

Because acceleration changes between parts of the journey, **a single constant-acceleration equation cannot be applied to the entire trip**. Instead, you must divide the motion into discrete **stages**, where acceleration is constant within each individual stage.

### The connecting principle

When motion flows continuously from Stage 1 to Stage 2:

- The **final velocity of Stage 1 equals the initial velocity of Stage 2**:
  \[
  u_2 = v_1
  \]
- Total displacement is the algebraic sum of the stage displacements:
  \[
  s_{\mathrm{total}} = s_1 + s_2 + \dots
  \]
- Total elapsed time is the sum of the stage durations:
  \[
  t_{\mathrm{total}} = t_1 + t_2 + \dots
  \]

Do not reset the initial velocity of Stage 2 to zero unless the problem explicitly states that the object came to rest before Stage 2 began.

### Stage planning table

Organize multi-stage calculations using a clear table:

| Stage | Initial velocity | Final velocity | Acceleration | Time interval | Displacement |
| --- | --- | --- | --- | --- | --- |
| Stage 1 | \(u_1\) | \(v_1\) | \(a_1\) | \(t_1\) | \(s_1\) |
| Stage 2 | \(u_2 = v_1\) | \(v_2\) | \(a_2\) | \(t_2\) | \(s_2\) |

A delivery van finishes Stage 1 at a velocity of \(+14\ \mathrm{m\,s^{-1}}\) and immediately begins braking in Stage 2. What value should be used for \(u_2\) at the start of Stage 2?

- **A:** \(+14\ \mathrm{m\,s^{-1}}\)
- **B:** \(0\ \mathrm{m\,s^{-1}}\)

**Feedback for A:** Correct. The motion is continuous. The velocity at the end of Stage 1 carries forward as the starting velocity for Stage 2.

**Feedback for B:** Not correct. The van does not start from rest again; it is already moving at \(+14\ \mathrm{m\,s^{-1}}\) when the braking stage begins.

A car travels forward (positive direction) and applies its brakes with uniform deceleration. Which statement regarding its acceleration is correct?

- **A:** Its acceleration is negative because its velocity is decreasing.
- **B:** Its acceleration is positive because it is still moving forward.

**Feedback for A:** Correct. Forward velocity is positive. Since the velocity is becoming less positive, the change in velocity is negative, so acceleration is negative.

**Feedback for B:** Not correct. The direction of motion determines the sign of velocity, not acceleration. Deceleration in the positive direction requires a negative acceleration.

### Worked example 3: Multi-stage problem (Accelerating then Braking)

An electric scooter moves along a straight path. Forward is chosen as positive.

- **Stage 1:** It starts from rest and accelerates uniformly at \(+1.5\ \mathrm{m\,s^{-2}}\) for \(6.0\ \mathrm{s}\).
- **Stage 2:** The rider then applies the brakes, causing a uniform acceleration of \(-3.0\ \mathrm{m\,s^{-2}}\) until the scooter stops.

Calculate:
(a) the total displacement of the scooter from start to finish;
(b) the total time taken for the complete journey.

**Stage 1 calculations:**
- \(u_1 = 0\ \mathrm{m\,s^{-1}}\)
- \(a_1 = +1.5\ \mathrm{m\,s^{-2}}\)
- \(t_1 = 6.0\ \mathrm{s}\)

Find final velocity \(v_1\):

\[
v_1 = u_1 + a_1 t_1 = 0 + (1.5\ \mathrm{m\,s^{-2}})(6.0\ \mathrm{s}) = +9.0\ \mathrm{m\,s^{-1}}
\]

Find displacement \(s_1\):

\[
s_1 = u_1 t_1 + \frac{1}{2}a_1 t_1^2 = 0 + \frac{1}{2}(1.5\ \mathrm{m\,s^{-2}})(6.0\ \mathrm{s})^2 = \frac{1}{2}(1.5)(36) = +27\ \mathrm{m}
\]

**Stage 2 calculations:**
Connect Stage 1 to Stage 2:
- \(u_2 = v_1 = +9.0\ \mathrm{m\,s^{-1}}\)
- \(v_2 = 0\ \mathrm{m\,s^{-1}}\) (scooter stops)
- \(a_2 = -3.0\ \mathrm{m\,s^{-2}}\)

Find displacement \(s_2\) using \(v_2^2 = u_2^2 + 2a_2 s_2\):

\[
s_2 = \frac{v_2^2 - u_2^2}{2a_2} = \frac{(0)^2 - (9.0\ \mathrm{m\,s^{-1}})^2}{2(-3.0\ \mathrm{m\,s^{-2}})} = \frac{-81}{-6.0} = +13.5\ \mathrm{m}
\]

Find time \(t_2\) using \(v_2 = u_2 + a_2 t_2\):

\[
0 = 9.0 + (-3.0)t_2 \implies 3.0t_2 = 9.0 \implies t_2 = 3.0\ \mathrm{s}
\]

**Combine the stages:**

\[
s_{\mathrm{total}} = s_1 + s_2 = 27\ \mathrm{m} + 13.5\ \mathrm{m} = 40.5\ \mathrm{m} \approx 41\ \mathrm{m}
\]

\[
t_{\mathrm{total}} = t_1 + t_2 = 6.0\ \mathrm{s} + 3.0\ \mathrm{s} = 9.0\ \mathrm{s}
\]

**Answer:** (a) Total displacement is **\(41\ \mathrm{m}\)** forward (or \(40.5\ \mathrm{m}\)). (b) Total time taken is **\(9.0\ \mathrm{s}\)**.

**Check:** During Stage 1 the scooter reaches \(9.0\ \mathrm{m\,s^{-1}}\). The braking acceleration has twice the magnitude of the initial acceleration (\(3.0\) vs \(1.5\ \mathrm{m\,s^{-2}}\)), so braking should take half the time (\(3.0\ \mathrm{s}\) vs \(6.0\ \mathrm{s}\)) and cover half the displacement (\(13.5\ \mathrm{m}\) vs \(27\ \mathrm{m}\)). This matches exactly.

## Common mistakes to repair

**Mistake: Applying suvat equations to non-uniform acceleration.**  
These formulas require constant acceleration in magnitude and direction. If air resistance changes during a long fall, acceleration changes and suvat equations cannot be applied to the whole fall.

**Mistake: Combining values from different stages into a single formula.**  
In a multi-stage journey, each stage has its own acceleration, time, and displacement. Never substitute Stage 1 time into an equation alongside Stage 2 acceleration.

**Mistake: Assuming \(u = 0\) at the start of every stage.**  
When a stage follows directly from earlier motion, its initial velocity \(u\) equals the final velocity of the previous stage. It is zero only if the object started from rest at that moment.

**Mistake: Dropping minus signs on deceleration and vectors.**  
If forward is positive, braking acceleration is negative (\(a < 0\)). Dropping the minus sign produces unphysical negative stopping distances or imaginary square roots.

**Mistake: Selecting an equation with an unwanted unknown.**  
When time is not given and not requested, do not use \(v = u + at\). Select \(v^2 = u^2 + 2as\) directly to avoid introducing extra unknowns.

## Core recap

- Constant-acceleration equations apply exclusively to **straight-line motion** with **constant acceleration** in magnitude and direction.
- Key definitions:
  - **Displacement:** distance in a specified direction from a point.
  - **Velocity:** rate of change of displacement.
  - **Acceleration:** rate of change of velocity: \(a = \frac{\Delta v}{\Delta t}\).
- Fundamental suvat equations:
  - \(v = u + at\) (omits \(s\))
  - \(s = \frac{u + v}{2}t\) (omits \(a\))
  - \(s = ut + \frac{1}{2}at^2\) (omits \(v\))
  - \(v^2 = u^2 + 2as\) (omits \(t\))
- "Starts from rest" means \(u = 0\); "stops" or "comes to rest" means \(v = 0\).
- In multi-stage problems, divide the journey into stages of constant acceleration and connect them via \(u_{n+1} = v_n\). Add stage displacements and stage times to find totals.
