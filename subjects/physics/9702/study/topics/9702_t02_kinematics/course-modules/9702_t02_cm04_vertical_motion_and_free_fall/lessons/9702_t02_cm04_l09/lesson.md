# Falling objects and Upward motion and measuring g

## Motion under gravity in a vertical line

Imagine dropping a small dense sphere from rest, or throwing a ball straight up into the air. In both cases, the object moves vertically under the influence of Earth's gravity. When an object moves influenced solely by the gravitational force, it is said to be in **free fall**.

Throughout this lesson, we use the standard Cambridge 9702 model for vertical motion near Earth's surface, based on two essential conditions:

- the object moves in a straight vertical line;
- **air resistance is negligible**.

Near Earth's surface, any freely falling object experiences a constant downward acceleration called the **acceleration of free fall**, denoted by \(g\). The accepted value of \(g\) for Cambridge 9702 calculations is:

\[
g = 9.81\,\mathrm{m\,s^{-2}}
\]

Because this acceleration is constant in magnitude and direction, all straight-line motion under gravity can be analysed using the constant-acceleration equations of motion.

The most critical step in any vertical motion problem comes before writing down any numbers: **you must define a single positive direction** (either upwards or downwards) and use that convention consistently for every displacement, velocity, and acceleration in your calculation.

## Setting a consistent sign convention

Displacement, velocity, and acceleration are all vector quantities. In one-dimensional vertical motion, their directions are represented by algebraic signs: plus (\(+\)) or minus (\(-\)).

### Convention 1: Downwards chosen as positive

If you choose downwards as the positive direction:

- any downward displacement is positive (\(s > 0\));
- any downward velocity is positive (\(v > 0\));
- an upward velocity is negative (\(v < 0\));
- the acceleration of free fall points downwards, so \(a = +g = +9.81\,\mathrm{m\,s^{-2}}\).

This convention is especially convenient for objects dropped from rest and falling directly towards the ground.

### Convention 2: Upwards chosen as positive

If you choose upwards as the positive direction:

- any upward displacement is positive (\(s > 0\));
- a point below the starting position has a negative displacement (\(s < 0\));
- an upward velocity is positive (\(u > 0\));
- a downward velocity is negative (\(v < 0\));
- the acceleration of free fall still points downwards, so \(a = -g = -9.81\,\mathrm{m\,s^{-2}}\).

This convention is especially convenient for objects projected upwards.

Both conventions are physically equivalent and give identical physical conclusions. What will produce an error is changing your convention halfway through a calculation or using two contradictory signs at the same time.

Suppose a stone is thrown upwards and you choose upwards as positive. What is the correct value to substitute for the acceleration \(a\) during both the upward and downward parts of the flight?

**A.** \(a = -9.81\,\mathrm{m\,s^{-2}}\) throughout the entire flight.

**B.** \(a = -9.81\,\mathrm{m\,s^{-2}}\) on the way up, but \(a = +9.81\,\mathrm{m\,s^{-2}}\) on the way down.

**Feedback for A:** Correct. The gravitational force acts downwards throughout the entire flight. Because upwards is chosen as positive, the acceleration remains \(a = -g = -9.81\,\mathrm{m\,s^{-2}}\) at all times, whether the stone is rising, momentarily at rest at the top, or falling.

**Feedback for B:** Incorrect. The acceleration does not reverse direction when the stone starts to fall. Gravity continues to pull downwards towards the centre of the Earth. If upwards is positive, downward acceleration must remain negative throughout.

## The constant-acceleration equations in free fall

Because the acceleration of free fall \(g\) is uniform, the three standard constant-acceleration equations apply directly.

<a id="formula-constant-acceleration-velocity"></a>
> **Formula to learn: Constant-acceleration velocity.**
>
> \[
> v = u + at
> \]

Here \(v\) is final velocity in \(\mathrm{m\,s^{-1}}\), \(u\) is initial velocity in \(\mathrm{m\,s^{-1}}\), \(a\) is constant acceleration in \(\mathrm{m\,s^{-2}}\), and \(t\) is time in \(\mathrm{s}\). In free fall, substitute \(a = +g\) or \(a = -g\) according to your chosen sign convention.

<a id="formula-constant-acceleration-displacement"></a>
> **Formula to learn: Constant-acceleration displacement.**
>
> \[
> s = ut + \frac{1}{2}at^2
> \]

Here \(s\) is vertical displacement in \(\mathrm{m}\) from the release point. When an object is released from rest, \(u = 0\,\mathrm{m\,s^{-1}}\), and this equation simplifies to \(s = \frac{1}{2}at^2\).

<a id="formula-constant-acceleration-velocity-displacement"></a>
> **Formula to learn: Constant-acceleration velocity and displacement.**
>
> \[
> v^2 = u^2 + 2as
> \]

This equation relates velocities and displacement directly without requiring the time of flight \(t\). Use it when the time interval is neither given nor required.

## Falling objects and mass independence

When an object is released from rest and falls through a vertical height \(h\), let downwards be positive. Setting \(u = 0\) and \(a = +g\):

\[
v^2 = 0^2 + 2gh \implies v = \sqrt{2gh}
\]

\[
h = \frac{1}{2}gt^2 \implies t = \sqrt{\frac{2h}{g}}
\]

Notice an important physical fact: neither the final velocity \(v\) nor the fall time \(t\) depends on the mass \(m\) of the falling object.

In the absence of air resistance, all objects in the same uniform gravitational field fall with exactly the same acceleration \(g\). A heavy lead sphere and a light plastic sphere released simultaneously from the same height will strike the ground at the exact same instant with the exact same speed.

In everyday life, a flat sheet of paper falls more slowly than a steel ball because the upward drag force from the air is comparable in size to the paper's small weight. When air resistance is eliminated or made negligible (such as in an evacuated glass tube or by using compact, dense spheres), both objects fall together.

Two solid spheres, X of mass \(0.50\,\mathrm{kg}\) and Y of mass \(2.0\,\mathrm{kg}\), are released simultaneously from rest from the top of a tower in a vacuum. Which sphere reaches the ground first, and with what speed?

**A.** Sphere Y reaches the ground first because it has four times the mass.

**B.** Both spheres reach the ground at the same instant with the same speed.

**Feedback for A:** Incorrect. In a vacuum, air resistance is zero. The acceleration is \(g\) for all objects regardless of their mass.

**Feedback for B:** Correct. Because both spheres start from rest (\(u = 0\)), fall through the same displacement (\(s = h\)), and have the same acceleration (\(a = g\)), the kinematic equations give identical fall times and identical impact speeds.

## Upward motion and the turning point

When an object is thrown vertically upwards with initial velocity \(u\), it moves upwards while being decelerated by gravity.

Choose **upwards as positive**. Then:

- initial velocity is positive: \(u > 0\);
- acceleration is negative: \(a = -g = -9.81\,\mathrm{m\,s^{-2}}\).

### The instant at maximum height

As the object rises, its upward velocity decreases until it reaches its highest point. At maximum height:

\[
v = 0\,\mathrm{m\,s^{-1}}
\]

This is the **turning point** of the motion. The object stops rising and begins to fall.

A critical Cambridge exam concept: **the acceleration at maximum height is NOT zero**. At the very top, the velocity is momentarily zero, but the downward gravitational force still acts. Therefore, the acceleration is still \(a = -9.81\,\mathrm{m\,s^{-2}}\). If the acceleration were zero at the top, the object would have no rate of change of velocity and would remain suspended in mid-air!

To find the maximum height \(H\) reached above the release point, set \(v = 0\) and \(a = -g\) in \(v^2 = u^2 + 2as\):

\[
0 = u^2 + 2(-g)H \implies H = \frac{u^2}{2g}
\]

To find the time \(t_{\text{top}}\) taken to reach maximum height, set \(v = 0\) in \(v = u + at\):

\[
0 = u + (-g)t_{\text{top}} \implies t_{\text{top}} = \frac{u}{g}
\]

### Symmetry of vertical flight

For an object that returns to the same vertical level from which it was launched (with negligible air resistance):

1. **Time symmetry:** the time taken to rise to maximum height equals the time taken to fall back to the launch level:

\[
t_{\text{ascent}} = t_{\text{descent}} = \frac{u}{g} \implies t_{\text{total}} = \frac{2u}{g}
\]

2. **Speed symmetry:** at any given height, the speed on the way down equals the speed on the way up. When it returns to the release height, its velocity is:

\[
v = -u
\]

At the highest point of a vertically projected stone's trajectory, which statement correctly describes its motion?

**A.** Its velocity is zero and its acceleration is \(9.81\,\mathrm{m\,s^{-2}}\) downwards.

**B.** Both its velocity and its acceleration are momentarily zero.

**Feedback for A:** Correct. Velocity passes through zero at the turning point, but the gravitational pull of the Earth is continuous, giving a constant downward acceleration of \(9.81\,\mathrm{m\,s^{-2}}\).

**Feedback for B:** Incorrect. If acceleration were zero when velocity is zero, the velocity would never change from zero, so the stone would never fall back down. Acceleration is the rate of change of velocity, not the value of velocity.

## Worked example 1: upward projection from an elevated platform

A small metal ball is projected vertically upwards with an initial speed of \(14.0\,\mathrm{m\,s^{-1}}\) from the edge of a platform \(18.0\,\mathrm{m}\) above the ground. Air resistance is negligible.

Calculate:

1. the maximum height reached above the platform;
2. the time taken from projection until the ball strikes the ground;
3. the velocity with which the ball strikes the ground.

Take **upwards as positive** and use \(g = 9.81\,\mathrm{m\,s^{-2}}\).

### Part 1: maximum height above the platform

At maximum height, vertical velocity \(v = 0\,\mathrm{m\,s^{-1}}\).

Known values:

\[
u = +14.0\,\mathrm{m\,s^{-1}}, \quad v = 0\,\mathrm{m\,s^{-1}}, \quad a = -9.81\,\mathrm{m\,s^{-2}}
\]

Use the equation linking \(u\), \(v\), \(a\), and \(s\):

\[
v^2 = u^2 + 2as
\]

\[
0 = (14.0\,\mathrm{m\,s^{-1}})^2 + 2(-9.81\,\mathrm{m\,s^{-2}})s
\]

\[
0 = 196 - 19.62s
\]

\[
19.62s = 196 \implies s = \frac{196}{19.62} = 9.99\,\mathrm{m}
\]

**Answer:** the ball rises to a maximum height of **\(10.0\,\mathrm{m}\)** (to 3 significant figures) above the platform.

### Part 2: total time of flight to the ground

When the ball hits the ground, it is \(18.0\,\mathrm{m}\) below the platform. Because upwards is positive:

\[
s = -18.0\,\mathrm{m}
\]

Known values:

\[
u = +14.0\,\mathrm{m\,s^{-1}}, \quad a = -9.81\,\mathrm{m\,s^{-2}}, \quad s = -18.0\,\mathrm{m}
\]

Substitute into the displacement-time equation:

\[
s = ut + \frac{1}{2}at^2
\]

\[
-18.0 = 14.0t + \frac{1}{2}(-9.81)t^2
\]

\[
-18.0 = 14.0t - 4.905t^2
\]

Rearrange into standard quadratic form \(At^2 + Bt + C = 0\):

\[
4.905t^2 - 14.0t - 18.0 = 0
\]

Solve using the quadratic formula \(t = \frac{-B \pm \sqrt{B^2 - 4AC}}{2A}\):

\[
t = \frac{-(-14.0) \pm \sqrt{(-14.0)^2 - 4(4.905)(-18.0)}}{2(4.905)}
\]

\[
t = \frac{14.0 \pm \sqrt{196.0 + 353.16}}{9.81} = \frac{14.0 \pm \sqrt{549.16}}{9.81} = \frac{14.0 \pm 23.43}{9.81}
\]

We select the positive root because time after projection must be positive:

\[
t = \frac{14.0 + 23.43}{9.81} = \frac{37.43}{9.81} = 3.82\,\mathrm{s}
\]

**Answer:** the ball reaches the ground after **\(3.82\,\mathrm{s}\)**.

### Part 3: impact velocity at the ground

Use the velocity equation with the calculated time \(t = 3.82\,\mathrm{s}\):

\[
v = u + at
\]

\[
v = +14.0\,\mathrm{m\,s^{-1}} + (-9.81\,\mathrm{m\,s^{-2}})(3.816\,\mathrm{s})
\]

\[
v = 14.0 - 37.43 = -23.4\,\mathrm{m\,s^{-1}}
\]

Alternatively, verify this using \(v^2 = u^2 + 2as\) directly:

\[
v^2 = (14.0)^2 + 2(-9.81)(-18.0) = 196 + 353.16 = 549.16
\]

\[
v = -\sqrt{549.16} = -23.4\,\mathrm{m\,s^{-1}}
\]

The negative sign confirms that the ball is moving downwards at impact.

**Answer:** the impact velocity is **\(23.4\,\mathrm{m\,s^{-1}}\) downwards** (or \(-23.4\,\mathrm{m\,s^{-1}}\)).

## Measuring the acceleration of free fall g

Syllabus learning outcome 9702.02.08 requires you to describe an experiment to determine the acceleration of free fall using a falling object.

### Apparatus and arrangement

The standard laboratory method uses an electrically released steel sphere and electronic timing:

- **Electromagnet:** holds a small, dense steel ball bearing at a known vertical position.
- **Switch:** a two-way switch that simultaneously turns off the electromagnet and starts an electronic millisecond timer.
- **Trapdoor (or light gate):** located vertically below the electromagnet. When the falling ball strikes the trapdoor, it breaks an electrical circuit and instantly stops the timer.
- **Metre rule and set square:** used to measure the vertical height of fall \(s\).
- **Plumb line:** ensures the trapdoor is positioned directly vertically beneath the ball.

### Experimental procedure

1. Align the metre rule vertically using a set square against the bench. Use a plumb line to check that the steel ball will fall cleanly onto the centre of the trapdoor.
2. Measure the vertical fall distance \(s\) using the metre rule. Measure from the bottom of the suspended steel ball to the top surface of the trapdoor. Use a set square against the metre rule to avoid parallax error when reading the scale.
3. Switch off the electromagnet. The sphere is released from rest (\(u = 0\)) and the electronic timer starts automatically at the same instant.
4. When the sphere hits the trapdoor, the timer stops automatically. Record the time of fall \(t\).
5. Repeat the timing at the same height two more times and calculate the mean value of \(t\).
6. Adjust the height of the electromagnet so that \(s\) is varied over a wide range (for example, from \(0.300\,\mathrm{m}\) to \(1.500\,\mathrm{m}\) in regular intervals of \(0.200\,\mathrm{m}\)). At each height, obtain a repeatable mean time \(t\).

### Graphical analysis to determine g

For an object falling from rest with uniform acceleration \(g\), the displacement \(s\) after time \(t\) is given by:

\[
s = ut + \frac{1}{2}gt^2
\]

Because the ball is released from rest, \(u = 0\), which gives:

\[
s = \frac{1}{2}gt^2
\]

Compare this equation with the standard equation of a straight line through the origin, \(y = mx\):

- plot vertical fall height \(s\) on the vertical (\(y\)) axis;
- plot the square of the fall time \(t^2\) on the horizontal (\(x\)) axis.

The resulting graph is a straight line passing through the origin \((0,0)\).

The gradient \(m\) of the line of best fit is:

\[
m = \frac{1}{2}g
\]

Therefore, the acceleration of free fall is calculated by doubling the gradient:

\[
g = 2 \times \text{gradient}
\]

A straight-line graph using multiple data points is far superior to calculating \(g\) from a single drop because:

- random timing and distance measurement errors are averaged across all data points;
- any anomalous result is immediately obvious as an outlier from the line;
- a systematic zero error (such as a constant electronic delay) would appear as a non-zero intercept rather than distorting the gradient.

### Sources of uncertainty and experimental improvements

Cambridge questions frequently ask how to reduce uncertainties in this practical procedure:

1. **Eliminating reaction time:** using an electronic timer triggered by an electromagnet and stopped by a trapdoor or light gate eliminates human reaction time. Human reaction time (~0.2 s) would cause an unacceptably large percentage uncertainty in a fall time of around 0.4 s to 0.5 s.
2. **Residual magnetism delay:** when the current in an electromagnet is switched off, the soft iron core may take a small fraction of a second to demagnetise, delaying release after the timer has started.
   - *Improvements:* use a small energising current; place a thin sheet of paper between the ball and the core; or use **two light gates** placed vertically along the path, dropping the ball from slightly above the first gate so that timing begins only when the ball cuts the first beam, completely eliminating release-mechanism delays.
3. **Parallax error in measuring height:** when reading the metre rule, keep your line of sight strictly perpendicular to the scale, using a set square against the rule.
4. **Minimising air resistance:** use a small, dense, smooth sphere (such as a steel ball bearing) so that air resistance is negligible compared to the sphere's weight over the drop distance. Avoid low-density objects such as table tennis balls.
5. **Reference points:** always measure height from the bottom of the ball to the top of the trapdoor plate, ensuring the measured distance corresponds exactly to the distance through which the ball falls before stopping the timer.

In an experiment to determine \(g\), a student plots a graph of height \(s\) on the vertical axis against \(t^2\) on the horizontal axis. The line of best fit has a gradient of \(4.90\,\mathrm{m\,s^{-2}}\). What is the experimental value of \(g\)?

**A.** \(4.90\,\mathrm{m\,s^{-2}}\)

**B.** \(9.80\,\mathrm{m\,s^{-2}}\)

**Feedback for A:** Incorrect. From \(s = \frac{1}{2}gt^2\), the gradient equals \(\frac{1}{2}g\), not \(g\). You must multiply the gradient by 2.

**Feedback for B:** Correct. Because \(\text{gradient} = \frac{1}{2}g\), \(g = 2 \times \text{gradient} = 2 \times 4.90\,\mathrm{m\,s^{-2}} = 9.80\,\mathrm{m\,s^{-2}}\).

## Worked example 2: experimental calculation of g

In an electromagnet-and-trapdoor experiment, the vertical distance from the bottom of the ball to the trapdoor is measured with a metre rule as \(s = 1.250\,\mathrm{m}\).

Three successive drops at this height produce the following timer readings:

\[
t_1 = 0.503\,\mathrm{s}, \quad t_2 = 0.507\,\mathrm{s}, \quad t_3 = 0.505\,\mathrm{s}
\]

1. Calculate the mean fall time \(t_{\text{mean}}\).
2. Calculate the experimental value of the acceleration of free fall \(g\) from this set of readings.
3. Explain one reason why repeating the measurement improves the reliability of the result.

### Step 1: calculate the mean fall time

\[
t_{\text{mean}} = \frac{0.503 + 0.507 + 0.505}{3} = \frac{1.515}{3} = 0.505\,\mathrm{s}
\]

### Step 2: calculate g

The sphere was released from rest, so \(u = 0\). Using \(s = \frac{1}{2}gt^2\):

\[
g = \frac{2s}{t^2}
\]

Substitute the measured distance and mean time:

\[
g = \frac{2(1.250\,\mathrm{m})}{(0.505\,\mathrm{s})^2} = \frac{2.500\,\mathrm{m}}{0.2550\,\mathrm{s^2}} = 9.803\,\mathrm{m\,s^{-2}}
\]

Round to 3 significant figures, matching the precision of the timing data:

**Answer:** \(g = 9.80\,\mathrm{m\,s^{-2}}\).

### Step 3: reason for repeating

Repeating measurements allows anomalous values to be identified and discarded, and taking the mean reduces the effect of random errors in the timing and release mechanisms.

## Common exam traps and misconceptions

1. **Assuming acceleration is zero at maximum height:**
   Velocity is momentarily zero at the top (\(v = 0\)), but the gravitational force still pulls downwards. The acceleration is \(9.81\,\mathrm{m\,s^{-2}}\) downwards at the top, exactly as it is throughout the entire flight.
2. **Mixing signs within one calculation:**
   If you select upwards as positive, write \(a = -9.81\,\mathrm{m\,s^{-2}}\) and ensure any displacement below the launch point is negative. If you choose downwards as positive, write \(a = +9.81\,\mathrm{m\,s^{-2}}\) and an initial upward velocity must be negative. Never change the sign convention mid-calculation.
3. **Forgetting that the gradient of s against t^2 is g/2:**
   When processing experimental data from \(s = \frac{1}{2}gt^2\), remember that the gradient of \(s\) against \(t^2\) is \(\frac{1}{2}g\). To find \(g\), you must multiply the gradient by 2.
4. **Carrying launch velocity into a separate descent stage:**
   If you split an upward throw into two separate stages (ascent and descent), the initial velocity for the descent stage starts from rest at the top (\(u = 0\)), not the launch velocity from the ground.
5. **Thinking heavier objects fall faster in free fall:**
   In the absence of air resistance, all masses experience the exact same gravitational acceleration \(g\). Mass cancels out of the equations of motion.

## Core recap

- Free fall is motion under gravity alone with negligible air resistance, giving a constant downward acceleration \(g = 9.81\,\mathrm{m\,s^{-2}}\).
- Always define a single positive direction before calculating and apply it consistently to displacement, velocity, and acceleration.
- In free fall from rest (\(u = 0\)) with downwards positive: \(v = gt\), \(s = \frac{1}{2}gt^2\), and \(v^2 = 2gs\).
- At maximum height of an upward projection: velocity is momentarily zero (\(v = 0\)), but acceleration remains \(9.81\,\mathrm{m\,s^{-2}}\) downwards.
- For symmetric upward and downward flight, \(t_{\text{ascent}} = t_{\text{descent}} = u/g\) and the return velocity is \(-u\).
- To measure \(g\) experimentally, drop a steel ball from rest using an electromagnet and record the fall time \(t\) through height \(s\) with an electronic timer.
- Plotting \(s\) against \(t^2\) produces a straight line through the origin with gradient \(m = \frac{1}{2}g\), giving \(g = 2m\).
- Electronic timing eliminates human reaction time; using small dense spheres makes air resistance negligible.
