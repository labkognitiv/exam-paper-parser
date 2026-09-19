# Topical mastery and correction

You have met the separate tools of kinematics. This final lesson is about a
different skill: choosing the right tool, showing a complete route, and finding
the first place where a wrong answer went off track.

Imagine that a cyclist's tracker reports a journey, a ball is thrown across a
court, and a light gate records a falling object. The situations look
different. Start by asking the same question each time: **what quantity is the
question actually asking for, and what information connects to it?**

This lesson stays within kinematics. If a question also mentions forces,
energy, electricity or another topic, isolate the motion step first. Do not
replace it with a formula from the other topic unless that later step is
explicitly needed.

## A dependable route through a kinematics question

Before calculating, make a short **motion record**.

1. State the object and the time interval being considered.
2. Choose one positive direction and keep it for that part of the question.
3. List known quantities with units. For constant acceleration, use
   **(s)** for displacement, **(u)** for initial velocity, **(v)** for
   final velocity, **(a)** for acceleration and **(t)** for time.
4. Name the required quantity. This prevents using an equation that happens to
   contain familiar symbols but answers a different question.
5. Decide whether the motion is constant velocity, uniformly accelerated
   straight-line motion, a graph problem, a free-fall approximation or two
   independent perpendicular motions.
6. Calculate with signs and units visible. Then check the direction, unit,
   size and shape of the result.

Ask yourself: **have I written a distance when the question asks for a
displacement?** That one decision changes both the quantity and, sometimes,
the sign.

<a id="definition-displacement"></a>
> **Definition to learn: displacement.** distance in a specified direction from a point

A displacement starts at a stated reference point and ends at a stated
position. It includes direction. For example, an object (4.0\,\mathrm{m})
east of a marker has a displacement of (4.0\,\mathrm{m}) east from that
marker. Its travelled distance can be larger because a route may bend or turn
back.

<a id="definition-velocity"></a>
> **Definition to learn: velocity.** rate of change of displacement

Velocity tells us how quickly displacement changes. Its usual unit is metres
per second, written \(\mathrm{m\,s^{-1}}\), and a direction or sign is part of
its meaning. A negative velocity is not an impossible speed. It means motion
in the direction chosen as negative.

<a id="definition-acceleration"></a>
> **Definition to learn: acceleration.** rate of change of velocity

Acceleration measures how quickly velocity changes. Velocity changes when
speed changes, direction changes, or both change. Its unit is metres per
second per second, written \(\mathrm{m\,s^{-2}}\). A negative acceleration
means acceleration is in the chosen negative direction. It does not always
mean an object is slowing down.

## Choose the representation before the formula

Use a **displacement-time graph** when position changes with time. Its
gradient, meaning rise divided by run, is velocity. A straight line has a
constant gradient, so it shows constant velocity. A horizontal line has zero
gradient, so the object is stationary.

Use a **velocity-time graph** when velocity changes with time. Its gradient is
acceleration. The signed area between the graph and the time axis is
displacement. Area above the axis is positive for the chosen direction. Area
below the axis is negative.

For either graph, first read the axes and scales. Then state whether you need a
coordinate, a gradient, an area or the overall shape. A carefully drawn graph
is evidence: label axes and units, use the given scale, and make a straight
line straight when acceleration is constant.

Here is a common correction. A student sees a velocity-time line below the
time axis and writes that the object is stationary. That is not correct. A
line below the axis has negative velocity. It is moving in the negative
direction. Only a line on the time axis has zero velocity.

An object has a horizontal velocity-time line at
\(-3.0\,\mathrm{m\,s^{-1}}\) for \(5.0\,\mathrm{s}\). Which statement is
correct?

- **A:** Its displacement is \(-15\,\mathrm{m}\).
- **B:** Its displacement is zero because the velocity is negative.

**Feedback for A:** Correct. The signed area is
\((-3.0\,\mathrm{m\,s^{-1}})(5.0\,\mathrm{s})=-15\,\mathrm{m}\). The
negative sign records the direction.

**Feedback for B:** Not correct. Negative velocity means motion in the chosen
negative direction. Zero displacement would require equal positive and
negative areas, or no motion, not one negative rectangular area.

## Formula bank: use the condition as well as the symbols

<a id="formula-uniform-motion"></a>
> **Formula to learn: Displacement in uniform motion.** \(s = vt\)

Here \(s\) is displacement in metres \(\mathrm{m}\), \(v\) is constant
velocity in \(\mathrm{m\,s^{-1}}\), and \(t\) is time in seconds
\(\mathrm{s}\). Use this only for a time interval with constant velocity in a
straight line. The unit check is

\[
\mathrm{m\,s^{-1}} \times \mathrm{s}
\]

\[
= \mathrm{m}.
\]

<a id="formula-average-speed"></a>
> **Formula to learn: Average speed.** \(\bar{v} = \frac{\text{total distance travelled}}{\text{total time taken}}\)

The bar over \(v\) means average. Use total distance, not displacement. The
answer is a scalar, so no direction is required.

<a id="formula-average-velocity"></a>
> **Formula to learn: Average velocity.** \(\vec{v}_{\mathrm{avg}} = \frac{\Delta\vec{s}}{\Delta t}\)

The arrow shows that average velocity is a vector. \(\Delta\vec{s}\) means
change in displacement and \(\Delta t\) means the time interval. Use the
overall displacement from start to finish, not the total route length.

<a id="formula-acceleration"></a>
> **Formula to learn: Acceleration.** \(a = \frac{\Delta v}{\Delta t}\)

\(a\) is acceleration in \(\mathrm{m\,s^{-2}}\), \(\Delta v\) is change in
velocity in \(\mathrm{m\,s^{-1}}\), and \(\Delta t\) is time in
\(\mathrm{s}\). Subtract in the order final minus initial:
\(\Delta v=v-u\). This agrees with the sign convention.

For **uniformly accelerated motion in a straight line**, acceleration is
constant. Starting with \(a=\Delta v/\Delta t\), write

\[
a=\frac{v-u}{t}.
\]

Multiply both sides by \(t\):

\[
at=v-u.
\]

Add \(u\) to both sides:

\[
v=u+at.
\]

The remaining constant-acceleration equations come from the same model. They
are not general motion formulas. Do not use them when acceleration changes
through the interval.

<a id="formula-constant-acceleration-velocity"></a>
> **Formula to learn: Constant-acceleration velocity.** \(v = u + at\)

Use this when you know initial velocity, final velocity, constant acceleration
and time. The signs of \(u\), \(v\) and \(a\) must all use the same chosen
positive direction.

<a id="formula-constant-acceleration-displacement"></a>
> **Formula to learn: Constant-acceleration displacement.** \(s = ut + \frac{1}{2}at^2\)

Use this when constant acceleration applies and the known quantities include
initial velocity, acceleration and time. The \(t^2\) means time multiplied by
itself. It is not \(2t\).

<a id="formula-constant-acceleration-velocity-displacement"></a>
> **Formula to learn: Constant-acceleration velocity and displacement.** \(v^2 = u^2 + 2as\)

Use this when constant acceleration applies and time is not needed. Squaring
\(v\) and \(u\) removes their direction signs in those terms, but the sign of
\(as\) still matters. Choose and state the positive direction first.

These equations also describe **free fall** if air resistance is negligible.
Near Earth's surface, choose down as positive and use \(a=+g\), or choose up
as positive and use \(a=-g\). Both are valid. Mixing the two conventions is
not valid.

## Worked example: correct a graph answer

A delivery robot starts at rest. Its velocity rises uniformly to
\(6.0\,\mathrm{m\,s^{-1}}\) in \(4.0\,\mathrm{s}\). It then travels at that
velocity for \(3.0\,\mathrm{s}\). Find its acceleration during the first stage
and its total displacement.

**Decide the representation.** The first stage asks for acceleration, so use
the gradient of the velocity-time graph or the acceleration formula. Total
displacement is the total area under the velocity-time graph.

For the first stage, \(u=0\), \(v=6.0\,\mathrm{m\,s^{-1}}\), and
\(t=4.0\,\mathrm{s}\):

\[
a=\frac{v-u}{t}
\]

\[
a=\frac{6.0\,\mathrm{m\,s^{-1}}-0\,\mathrm{m\,s^{-1}}}{4.0\,\mathrm{s}}
\]

\[
a=1.5\,\mathrm{m\,s^{-2}}.
\]

The first graph area is a triangle. Its displacement is

\[
s_1=\frac{1}{2}\times4.0\,\mathrm{s}\times6.0\,\mathrm{m\,s^{-1}}
\]

\[
s_1=12\,\mathrm{m}.
\]

The second graph area is a rectangle:

\[
s_2=3.0\,\mathrm{s}\times6.0\,\mathrm{m\,s^{-1}}
\]

\[
s_2=18\,\mathrm{m}.
\]

Add the areas because both are above the time axis:

\[
s_{\mathrm{total}}=12\,\mathrm{m}+18\,\mathrm{m}=30\,\mathrm{m}.
\]

**Answer:** acceleration \(=1.5\,\mathrm{m\,s^{-2}}\); displacement
\(=30\,\mathrm{m}\) in the positive direction.

**Check.** The acceleration unit is \(\mathrm{m\,s^{-2}}\). The area unit is
\(\mathrm{m\,s^{-1}}\times\mathrm{s}=\mathrm{m}\). The result is positive
because the whole graph lies above the axis.

## Worked example: repair a free-fall setup

A stone is released from rest. It falls \(20.0\,\mathrm{m}\). Air resistance
is negligible. Take downwards as positive and use
\(g=9.81\,\mathrm{m\,s^{-2}}\). Find the time of fall.

**Decide the model.** The stone is released, so \(u=0\). The acceleration is
constant and the question gives \(s\), \(u\) and \(a\), but not \(v\). Choose
the equation containing \(s\), \(u\), \(a\) and \(t\):

\[
s=ut+\frac{1}{2}at^2.
\]

Substitute with units and signs:

\[
20.0\,\mathrm{m}=(0\,\mathrm{m\,s^{-1}})(t)+\frac{1}{2}
(9.81\,\mathrm{m\,s^{-2}})t^2.
\]

The first term is zero:

\[
20.0\,\mathrm{m}=4.905\,\mathrm{m\,s^{-2}}t^2.
\]

Divide by \(4.905\,\mathrm{m\,s^{-2}}\):

\[
t^2=4.08\,\mathrm{s^2}.
\]

Take the positive square root because elapsed time is positive:

\[
t=2.02\,\mathrm{s}.
\]

**Answer:** \(t=2.02\,\mathrm{s}\).

**Check.** A fall of \(20\,\mathrm{m}\) in about two seconds gives a final
speed near \(20\,\mathrm{m\,s^{-1}}\), which is a plausible increase under
gravity. A negative square-root answer would be rejected because it cannot be
an elapsed time.

To determine \(g\) experimentally, release a small dense object from rest,
measure a known vertical distance \(s\), and measure the fall time \(t\).
Repeat the timing at several distances. From
\(s=\tfrac{1}{2}gt^2\), plot \(s\) on the vertical axis against \(t^2\) on
the horizontal axis. The gradient is \(\tfrac{1}{2}g\), so
\(g=2\times\text{gradient}\). Release the object without a push, reduce air
resistance, use a longer distance if safe, repeat readings, and use electronic
timing or light gates to reduce reaction-time uncertainty.

## Worked example: split a projectile before solving it

A ball leaves a table horizontally at \(5.0\,\mathrm{m\,s^{-1}}\). It is in
the air for \(0.60\,\mathrm{s}\). Air resistance is negligible. Find its
horizontal displacement and vertical displacement. Take upwards as positive.

**Decide what is independent.** Horizontally, acceleration is zero, so velocity
is constant. Vertically, initial velocity is zero and acceleration is
\(-9.81\,\mathrm{m\,s^{-2}}\). The same time, \(0.60\,\mathrm{s}\), belongs
to both motions.

For the horizontal motion:

\[
s_x=v_xt
\]

\[
s_x=(5.0\,\mathrm{m\,s^{-1}})(0.60\,\mathrm{s})
\]

\[
s_x=3.0\,\mathrm{m}.
\]

For the vertical motion, \(u_y=0\):

\[
s_y=u_yt+\frac{1}{2}at^2
\]

\[
s_y=(0)(0.60\,\mathrm{s})+\frac{1}{2}(-9.81\,\mathrm{m\,s^{-2}})
(0.60\,\mathrm{s})^2
\]

\[
s_y=-1.77\,\mathrm{m}.
\]

**Answer:** the ball travels \(3.0\,\mathrm{m}\) horizontally and has a
vertical displacement of \(-1.77\,\mathrm{m}\), meaning \(1.77\,\mathrm{m}\)
downwards.

**Check.** The horizontal result uses constant velocity. The vertical result is
negative because up was chosen as positive. Do not add the two displacements as
ordinary numbers: they are perpendicular components.

A projectile has no air resistance. Which statement is correct while it is in
flight?

- **A:** Its horizontal velocity stays constant while gravity changes its
  vertical velocity.
- **B:** Gravity gradually reduces both its horizontal and vertical velocity.

**Feedback for A:** Correct. Gravity acts vertically downward. With no air
resistance there is no horizontal force, so horizontal acceleration is zero.
The vertical velocity changes by \(g\) each second downward.

**Feedback for B:** Not correct. This would require a horizontal force. Air
resistance could change horizontal velocity, but the stated no-air-resistance
model excludes it.

## Correct mistakes by locating the first broken decision

Do not only replace an answer. Use this correction sequence.

1. **Compare the required quantity with your final unit.** A requested
   acceleration needs \(\mathrm{m\,s^{-2}}\), not metres or seconds.
2. **Check the model condition.** Constant-acceleration equations need constant
   acceleration. \(s=vt\) needs constant velocity.
3. **Check the sign convention.** Write it before substituting values. In a
   vertical calculation, use either up positive or down positive throughout.
4. **Check the representation.** A gradient uses two points on the line. An
   area uses the correct geometric shape and signed position relative to the
   axis.
5. **Check the physical story.** At maximum height, vertical velocity is zero,
   not horizontal velocity. At rest, velocity is zero, but acceleration need
   not be zero.
6. **Retry after a delay.** Cover the old working. Rebuild the motion record
   and solve from the first decision. This tests the method rather than memory
   of a corrected number.

When a question mixes topics, write a boundary line in your working. For
example: "Kinematics result: time to reach the point is ..." Then carry that
value, including its unit, into the next part. That keeps the kinematics method
auditable.

## Core recap

- **Displacement** is distance in a specified direction from a point.
- **Velocity** is rate of change of displacement.
- **Acceleration** is rate of change of velocity.
- Use graph gradient for a rate of change and signed velocity-time area for
  displacement.
- Use \(s=vt\) only for constant velocity.
- Use \(v=u+at\), \(s=ut+\tfrac{1}{2}at^2\), or
  \(v^2=u^2+2as\) only for constant acceleration in a straight line.
- For a projectile, write separate horizontal and vertical motion records. The
  time is shared, but the accelerations are different.
- A good final answer has a value, unit and direction when direction matters.
  A good correction finds the first decision that failed.
