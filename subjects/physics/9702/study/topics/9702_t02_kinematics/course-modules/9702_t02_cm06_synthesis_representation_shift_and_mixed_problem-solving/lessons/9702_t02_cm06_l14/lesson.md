# Kinematics inside mixed-topic questions and Topical mastery and correction

## The kinematics leaf in multi-topic questions

Examination questions in Cambridge 9702 AS Physics rarely test kinematics in complete isolation. You will often encounter questions that begin with an electric field accelerating an electron, a motor lifting a load with a cable, a skydiver falling through the atmosphere, or a vehicle braking due to frictional forces.

When faced with such a scenario, do not be distracted by the unfamiliar context. Always pause and ask: **what is moving, and what changes about its motion?**

If the question involves position, displacement, speed, velocity, acceleration, flight time, or motion graphs, there is a distinct **kinematics step** inside the problem. We call this the **kinematics leaf**.

Think of the question as a sequential chain:

1. One part of the question provides physical quantities (such as an initial speed, stopping distance, or time interval).
2. The kinematics leaf solves for an acceleration, a velocity, or a time using pure motion principles.
3. The next part of the question carries that kinematics result forward into a force, work, energy, or electrical calculation.

Your primary objective is to isolate the kinematics leaf, solve it cleanly using the correct motion model, and hand off the result with its correct algebraic sign, SI unit, and physical interpretation.

## Systematic motion record

Before writing down any formula or substituting numbers, write a short, five-point **motion record** on your working paper:

1. **Object and interval:** identify which object is moving and define the exact start and end points of the interval.
2. **Sign convention:** choose one positive direction (e.g. "take right as positive" or "take upwards as positive") and keep it throughout the calculation.
3. **List the motion quantities:** record the five standard variables with their signs and units:
   - initial velocity \(u\) in \(\mathrm{m\,s^{-1}}\)
   - final velocity \(v\) in \(\mathrm{m\,s^{-1}}\)
   - acceleration \(a\) in \(\mathrm{m\,s^{-2}}\)
   - displacement \(s\) in \(\mathrm{m}\)
   - time interval \(t\) in \(\mathrm{s}\)
4. **Identify the motion model:** determine whether the motion is:
   - uniform motion with constant velocity (\(a = 0\));
   - uniformly accelerated straight-line motion (\(a = \text{constant}\));
   - non-uniform acceleration (requiring graph gradient or area);
   - two-dimensional projectile motion (requiring independent horizontal and vertical components).
5. **Bridge statement:** state clearly what quantity must be passed to the next stage of the question.

A lift is moving upwards towards the top floor of a building and is slowing down uniformly. Taking upwards as positive, what are the signs of its velocity and its acceleration?

**A.** Velocity is positive, and acceleration is negative.

**B.** Both velocity and acceleration are negative because the lift is decelerating.

**Feedback for A:** Correct. The lift is moving upwards, so its displacement is increasing in the positive direction (\(v > 0\)). Because it is slowing down, the rate of change of velocity opposes the direction of motion, meaning the acceleration points downwards (\(a < 0\)).

**Feedback for B:** Incorrect. The sign of velocity indicates the direction of motion. Since the lift is travelling upwards, its velocity is positive. Deceleration in the positive direction corresponds to a negative acceleration.

## Controlled definitions of kinematics quantities

Every kinematics problem rests on three fundamental definitions that must be reproduced accurately.

<a id="definition-displacement"></a>
> **Definition to learn: displacement.** distance in a specified direction from a point

Displacement is a vector quantity with SI unit metres (\(\mathrm{m}\)). It represents the straight-line directed distance from a fixed reference point to the object's current position. Do not confuse displacement with distance: distance is the total scalar path length travelled, whereas displacement depends only on the start and end points.

<a id="definition-velocity"></a>
> **Definition to learn: velocity.** rate of change of displacement

Velocity is a vector quantity with SI unit metres per second (\(\mathrm{m\,s^{-1}}\)). It describes how rapidly displacement changes with time. An object can have a positive velocity while possessing a negative acceleration; this simply means it is moving in the positive direction while slowing down.

<a id="definition-acceleration"></a>
> **Definition to learn: acceleration.** rate of change of velocity

Acceleration is a vector quantity with SI unit metres per second squared (\(\mathrm{m\,s^{-2}}\)). It measures how rapidly the velocity vector changes per unit time. A non-zero acceleration occurs whenever speed changes, direction of motion changes, or both change.

## Derivation of the constant-acceleration equations

Syllabus outcome 9702.02.06 requires you to derive the equations of uniformly accelerated motion from the fundamental definitions of velocity and acceleration.

### Derivation of \(v = u + at\)

From the definition of acceleration as the rate of change of velocity:

\[
a = \frac{\Delta v}{\Delta t} = \frac{v - u}{t}
\]

Multiplying both sides by \(t\):

\[
at = v - u
\]

Adding \(u\) to both sides gives the first equation of motion:

<a id="formula-constant-acceleration-velocity"></a>
> **Formula to learn: Constant-acceleration velocity.**
>
> \[
> v = u + at
> \]

### Derivation of \(s = ut + \frac{1}{2}at^2\)

For an object accelerating uniformly from initial velocity \(u\) to final velocity \(v\) in time \(t\), the average velocity \(v_{\text{avg}}\) is:

\[
v_{\text{avg}} = \frac{u + v}{2}
\]

Displacement \(s\) is average velocity multiplied by time:

\[
s = \left(\frac{u + v}{2}\right)t
\]

Substitute \(v = u + at\) into this expression:

\[
s = \left(\frac{u + (u + at)}{2}\right)t = \left(\frac{2u + at}{2}\right)t = \left(u + \frac{1}{2}at\right)t
\]

Expanding the brackets yields the second equation of motion:

<a id="formula-constant-acceleration-displacement"></a>
> **Formula to learn: Constant-acceleration displacement.**
>
> \[
> s = ut + \frac{1}{2}at^2
> \]

(Alternatively, on a velocity-time graph, this represents the area of a trapezium divided into a rectangle of area \(ut\) and a triangle of area \(\frac{1}{2}(v - u)t = \frac{1}{2}at^2\).)

### Derivation of \(v^2 = u^2 + 2as\)

From the first equation, express time \(t\) in terms of velocities and acceleration:

\[
t = \frac{v - u}{a}
\]

Substitute this expression for \(t\) into the average velocity displacement formula \(s = \left(\frac{u + v}{2}\right)t\):

\[
s = \left(\frac{v + u}{2}\right)\left(\frac{v - u}{a}\right)
\]

Recognising the difference of two squares in the numerator:

\[
s = \frac{v^2 - u^2}{2a}
\]

Multiplying both sides by \(2a\):

\[
2as = v^2 - u^2
\]

Rearranging gives the third equation of motion:

<a id="formula-constant-acceleration-velocity-displacement"></a>
> **Formula to learn: Constant-acceleration velocity and displacement.**
>
> \[
> v^2 = u^2 + 2as
> \]

### Formula for uniform motion

When velocity is constant (\(a = 0\)), acceleration terms vanish and displacement is given simply by:

<a id="formula-uniform-motion-displacement"></a>
> **Formula to learn: Displacement in uniform motion.**
>
> \[
> s = vt
> \]

## Graphical representation and gradient-area relationships

Motion graphs are central to Cambridge kinematics questions. Always check the axes before carrying out any calculation:

| Graph type | Gradient represents | Area under graph represents |
| --- | --- | --- |
| **Displacement-time (\(s\) vs \(t\))** | **Velocity** (\(v = \Delta s / \Delta t\)) | No standard physical meaning |
| **Velocity-time (\(v\) vs \(t\))** | **Acceleration** (\(a = \Delta v / \Delta t\)) | **Displacement** (\(\Delta s\)) |

### Key graph rules

1. **Straight line on a displacement-time graph:** constant gradient, therefore constant velocity. A horizontal line indicates the object is stationary (\(v = 0\)).
2. **Curved line on a displacement-time graph:** changing gradient, therefore changing velocity (accelerated motion). The instantaneous velocity at any time is the gradient of the tangent drawn at that point.
3. **Straight line on a velocity-time graph:** constant gradient, therefore constant acceleration. A horizontal line indicates uniform velocity (\(a = 0\)).
4. **Curved line on a velocity-time graph:** non-uniform acceleration. The instantaneous acceleration is found by drawing a tangent to the curve at that instant and calculating its gradient (\(\Delta v / \Delta t\)). Never use the constant-acceleration equations (\(v = u + at\), etc.) for a curved velocity-time graph.
5. **Signed area on a velocity-time graph:** area above the time axis represents positive displacement; area below the time axis represents negative displacement. To find total distance, add the absolute magnitudes of the areas. To find net displacement, subtract the area below the axis from the area above the axis.

A velocity-time graph consists of a horizontal line at \(v = -4.0\,\mathrm{m\,s^{-1}}\) from \(t = 0\) to \(t = 3.0\,\mathrm{s}\). What is the displacement and the distance travelled during this time?

**A.** Displacement is \(-12\,\mathrm{m}\) and distance travelled is \(12\,\mathrm{m}\).

**B.** Displacement is zero and distance travelled is \(-12\,\mathrm{m}\).

**Feedback for A:** Correct. The area lies below the time axis, giving a signed displacement of \((-4.0\,\mathrm{m\,s^{-1}})(3.0\,\mathrm{s}) = -12\,\mathrm{m}\). Distance is a scalar and cannot be negative, so distance travelled is \(12\,\mathrm{m}\).

**Feedback for B:** Incorrect. Distance cannot be negative, and displacement is non-zero because the object moved continuously in the negative direction.

## Worked example 1: electric field deceleration (mixed topic)

An electron in a vacuum enters a uniform electric field between two parallel plates with an initial horizontal speed of \(5.0 \times 10^6\,\mathrm{m\,s^{-1}}\). The electric field exerts a constant decelerating force on the electron opposing its motion, bringing it to rest in a distance of \(2.5 \times 10^{-2}\,\mathrm{m}\).

1. Identify the kinematics leaf and calculate the acceleration of the electron.
2. Calculate the time taken for the electron to come to rest.
3. Write a bridging statement explaining the significance of the sign of the acceleration for a subsequent electric-force calculation.

### Step 1: define the motion record

Take the initial direction of motion as **positive** (to the right):

- initial velocity: \(u = +5.0 \times 10^6\,\mathrm{m\,s^{-1}}\)
- final velocity: \(v = 0\,\mathrm{m\,s^{-1}}\)
- displacement: \(s = +2.5 \times 10^{-2}\,\mathrm{m}\)
- acceleration \(a\) is constant.

### Step 2: calculate acceleration

Because time is not given, select \(v^2 = u^2 + 2as\):

\[
v^2 = u^2 + 2as
\]

Rearrange for acceleration \(a\):

\[
a = \frac{v^2 - u^2}{2s}
\]

Substitute the signed values:

\[
a = \frac{(0\,\mathrm{m\,s^{-1}})^2 - (5.0 \times 10^6\,\mathrm{m\,s^{-1}})^2}{2(2.5 \times 10^{-2}\,\mathrm{m})} = \frac{-2.5 \times 10^{13}\,\mathrm{m^2\,s^{-2}}}{5.0 \times 10^{-2}\,\mathrm{m}}
\]

\[
a = -5.0 \times 10^{14}\,\mathrm{m\,s^{-2}}
\]

**Answer:** the acceleration is **\(-5.0 \times 10^{14}\,\mathrm{m\,s^{-2}}\)** (or \(5.0 \times 10^{14}\,\mathrm{m\,s^{-2}}\) directed to the left).

### Step 3: calculate time to come to rest

Use \(v = u + at\):

\[
0 = 5.0 \times 10^6 + (-5.0 \times 10^{14})t
\]

\[
t = \frac{5.0 \times 10^6\,\mathrm{m\,s^{-1}}}{5.0 \times 10^{14}\,\mathrm{m\,s^{-2}}} = 1.0 \times 10^{-8}\,\mathrm{s}
\]

**Answer:** the time taken is **\(1.0 \times 10^{-8}\,\mathrm{s}\)** (or \(10\,\mathrm{ns}\)).

### Step 4: bridging statement

"The electron experiences a constant acceleration of \(-5.0 \times 10^{14}\,\mathrm{m\,s^{-2}}\). The negative sign demonstrates that the net electrostatic force acts to the left, directly opposing the electron's velocity."

## Worked example 2: multi-stage crane lift and graph synthesis

A crane lifts a crate vertically from rest on the ground. The lift consists of three distinct stages:

- **Stage 1:** the crate accelerates uniformly upwards from rest at \(0.80\,\mathrm{m\,s^{-2}}\) for \(5.0\,\mathrm{s}\).
- **Stage 2:** the crate continues upwards at constant speed for \(10.0\,\mathrm{s}\).
- **Stage 3:** the motor reduces power and the crate decelerates uniformly to rest in \(4.0\,\mathrm{s}\).

Calculate:

1. the maximum speed reached during the lift;
2. the total vertical height through which the crate is lifted;
3. describe the features of the distance-time graph representing this motion.

### Part 1: maximum speed reached

Take **upwards as positive**.

For Stage 1:

\[
u_1 = 0\,\mathrm{m\,s^{-1}}, \quad a_1 = +0.80\,\mathrm{m\,s^{-2}}, \quad t_1 = 5.0\,\mathrm{s}
\]

\[
v_1 = u_1 + a_1 t_1 = 0 + (0.80\,\mathrm{m\,s^{-2}})(5.0\,\mathrm{s}) = 4.0\,\mathrm{m\,s^{-1}}
\]

**Answer:** the maximum speed is **\(4.0\,\mathrm{m\,s^{-1}}\)**.

### Part 2: total vertical displacement

Calculate displacement for each stage:

- **Stage 1 displacement:**

\[
s_1 = u_1 t_1 + \frac{1}{2}a_1 t_1^2 = 0 + \frac{1}{2}(0.80\,\mathrm{m\,s^{-2}})(5.0\,\mathrm{s})^2 = 0.40 \times 25 = 10.0\,\mathrm{m}
\]

- **Stage 2 displacement (constant velocity \(v_1 = 4.0\,\mathrm{m\,s^{-1}}\)):**

\[
s_2 = v_1 t_2 = (4.0\,\mathrm{m\,s^{-1}})(10.0\,\mathrm{s}) = 40.0\,\mathrm{m}
\]

- **Stage 3 displacement (uniform deceleration to rest):**

Initial speed for Stage 3 is \(u_3 = 4.0\,\mathrm{m\,s^{-1}}\), final speed is \(v_3 = 0\), and time is \(t_3 = 4.0\,\mathrm{s}\).

Using average velocity:

\[
s_3 = \left(\frac{u_3 + v_3}{2}\right)t_3 = \left(\frac{4.0 + 0}{2}\right)(4.0\,\mathrm{s}) = 2.0 \times 4.0 = 8.0\,\mathrm{m}
\]

- **Total height:**

\[
s_{\text{total}} = s_1 + s_2 + s_3 = 10.0\,\mathrm{m} + 40.0\,\mathrm{m} + 8.0\,\mathrm{m} = 58.0\,\mathrm{m}
\]

(Alternatively, check using the area of a trapezium on a velocity-time graph: \(\text{Area} = \frac{1}{2}(a + b)h = \frac{1}{2}(10.0 + 19.0) \times 4.0 = 29.0 \times 2.0 = 58.0\,\mathrm{m}\).)

**Answer:** the total vertical height lifted is **\(58.0\,\mathrm{m}\)**.

### Part 3: description of distance-time graph

- From \(t = 0\) to \(5.0\,\mathrm{s}\): a curve starting with a horizontal tangent at the origin and curving upwards with an increasing positive gradient (representing constant positive acceleration).
- From \(t = 5.0\) to \(15.0\,\mathrm{s}\): a straight line with a constant steep positive gradient of \(4.0\,\mathrm{m\,s^{-1}}\) (representing uniform velocity).
- From \(t = 15.0\) to \(19.0\,\mathrm{s}\): a curve continuing to rise but bending over with a decreasing positive gradient, ending with a horizontal tangent at \(t = 19.0\,\mathrm{s}\) at height \(58.0\,\mathrm{m}\) (representing uniform deceleration to rest).

## The five classic exam traps and how to correct them

Cambridge examiner reports repeatedly highlight five recurring failure modes in kinematics questions. Use this diagnosis and correction guide.

### Trap 1: Vector sign confusion

- **The error:** writing \(a = -g\) because gravity acts downwards, but then treating downward displacement as positive because "the object is falling downwards".
- **The consequence:** the signs represent two conflicting positive directions simultaneously, producing nonsensical or imaginary solutions.
- **The fix:** write your sign rule at the top of your page before writing any numbers:
  "Upwards is positive: \(u > 0\), \(a = -9.81\,\mathrm{m\,s^{-2}}\), displacement below launch is \(s < 0\)".
  Verify every variable against that single rule.

### Trap 2: Misinterpreting graph features

- **The error:** assuming that a velocity-time graph below the horizontal axis means the object is stationary, or calculating displacement as the area under a displacement-time graph.
- **The consequence:** complete loss of marks on graphical interpretation parts.
- **The fix:** check the vertical axis label first:
  - If axis is **displacement**, gradient is velocity; area has no physical meaning.
  - If axis is **velocity**, gradient is acceleration; signed area is displacement. A line below the axis means the object is moving in the negative direction. Only a line on the time axis (\(v = 0\)) represents rest.

### Trap 3: Illegitimate formula application (non-uniform acceleration)

- **The error:** applying \(v^2 = u^2 + 2as\) or \(s = ut + \frac{1}{2}at^2\) to motion where air resistance is significant (such as a falling raindrop or skydiver approaching terminal velocity).
- **The consequence:** formulas for uniform acceleration are invalid when acceleration changes with speed.
- **The fix:** inspect the wording and context:
  - If air resistance is negligible: acceleration is constant, and constant-acceleration equations apply.
  - If air resistance causes a curve on the velocity-time graph: acceleration changes. You must use graph gradients (tangents) and graph areas (counting grid squares or trapeziums), never constant-acceleration equations.

### Trap 4: Mixing perpendicular components in projectile motion

- **The error:** substituting the horizontal velocity or total launch speed into a vertical displacement equation, or using \(9.81\,\mathrm{m\,s^{-2}}\) as a horizontal acceleration.
- **The consequence:** completely invalid physics mixing perpendicular vector directions.
- **The fix:** draw a two-column table:
  - **Horizontal column:** \(a_x = 0\), \(v_x = u \cos\theta = \text{constant}\), \(s_x = v_x t\).
  - **Vertical column:** \(a_y = -9.81\,\mathrm{m\,s^{-2}}\), \(u_y = u \sin\theta\), \(v_y = u_y + a_y t\), \(s_y = u_y t + \frac{1}{2}a_y t^2\).
  - The only quantity allowed to cross between the two columns is **time \(t\)**.

### Trap 5: Prematurely mixing dynamics or energy into kinematics

- **The error:** attempting to calculate forces, tensions, or work before finding the kinematic acceleration.
- **The consequence:** getting stuck trying to solve two unknowns at once.
- **The fix:** cleanly isolate the kinematics leaf first. Determine acceleration, velocity, or time from the motion information alone. Then pass that clean, single value into the dynamics or energy equations.

A student calculates the time taken for a feather to fall \(1.5\,\mathrm{m}\) in air by substituting \(a = 9.81\,\mathrm{m\,s^{-2}}\) into \(s = \frac{1}{2}at^2\). Why is this calculation incorrect?

**A.** Because the feather experiences air resistance comparable to its weight, making its acceleration non-uniform and less than \(9.81\,\mathrm{m\,s^{-2}}\).

**B.** Because the formula \(s = \frac{1}{2}at^2\) applies only when the mass of the object is greater than \(1.0\,\mathrm{kg}\).

**Feedback for A:** Correct. The constant-acceleration model assumes negligible air resistance. For a light object like a feather in air, drag forces cause the acceleration to decrease significantly, so \(a \neq \text{constant}\) and the formula does not apply.

**Feedback for B:** Incorrect. The formula \(s = \frac{1}{2}at^2\) is entirely independent of mass, provided the acceleration is constant.

## Core recap

- In mixed-topic examination questions, isolate the **kinematics leaf** first: establish the interval, choose a sign convention, list known variables, and select the matching motion model.
- Know the exact Cambridge definitions:
  - **displacement:** distance in a specified direction from a point
  - **velocity:** rate of change of displacement
  - **acceleration:** rate of change of velocity
- Be able to derive the constant-acceleration equations from first principles:
  - \(v = u + at\) from \(a = (v - u)/t\)
  - \(s = ut + \frac{1}{2}at^2\) from average velocity \(s = \frac{1}{2}(u + v)t\)
  - \(v^2 = u^2 + 2as\) by eliminating \(t\)
- On motion graphs:
  - displacement-time gradient is velocity
  - velocity-time gradient is acceleration
  - velocity-time signed area is displacement
- For non-uniform acceleration (curved velocity-time graphs), determine instantaneous acceleration by drawing a tangent; never use constant-acceleration equations.
- In two-dimensional projectile motion, treat horizontal motion (uniform velocity) and vertical motion (uniform acceleration \(g\)) as completely independent systems connected only by shared time \(t\).
- To correct mistakes, locate the first broken decision: check sign consistency, verify model validity (constant vs changing acceleration), and ensure vector components are kept separate until the final step.
