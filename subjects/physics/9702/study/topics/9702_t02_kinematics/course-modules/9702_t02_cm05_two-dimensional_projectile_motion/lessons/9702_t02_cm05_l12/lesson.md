# Time, range and impact velocity

## A ball leaving a table

Roll a ball off the edge of a table. It continues moving forward while it also falls. The ball does not first finish moving forward and then start falling. Both motions happen during the same time interval.

This lesson uses the two components introduced in the previous lesson:

- the **horizontal component** moves at uniform velocity when air resistance is negligible
- the **vertical component** accelerates downwards at \(g\)

The two components share one clock. If the ball is in the air for \(1.5\,\mathrm{s}\), its horizontal motion and vertical motion each last \(1.5\,\mathrm{s}\). This shared time connects a vertical fall to the horizontal **range**, which is the horizontal displacement from launch to landing.

We assume that air resistance is negligible. The projectile then has no horizontal acceleration, but it always has vertical acceleration downwards. Do not combine the two components until the question asks for the final speed or direction.

## Name each velocity carefully

<a id="definition-velocity"></a>
> **Definition to learn: velocity.** rate of change of displacement

Velocity includes both speed and direction. A projectile can therefore have a horizontal velocity component, \(v_x\), and a vertical velocity component, \(v_y\). The subscript tells you the direction of the component:

- **\(x\)** means horizontal
- **\(y\)** means vertical

For a projectile launched horizontally, the initial vertical velocity is \(u_y=0\). Its initial horizontal velocity, \(u_x\), is non-zero. With negligible air resistance, \(v_x=u_x\) throughout the flight.

Ask yourself: which component changes because of gravity? Gravity is vertical, so it changes only the vertical component.

## The equations belong to different components

<a id="formula-uniform-motion-displacement"></a>
> **Formula to learn: Displacement in uniform motion.** \(s = vt\)

For the horizontal component, this formula gives the range. Here **\(s\)** is horizontal displacement in \(\mathrm{m}\), **\(v\)** is the constant horizontal velocity in \(\mathrm{m\,s^{-1}}\), and **\(t\)** is flight time in \(\mathrm{s}\). In component notation, write \(s_x=v_xt\). It applies only because the horizontal velocity is constant.

<a id="formula-constant-acceleration-velocity"></a>
> **Formula to learn: Constant-acceleration velocity.** \(v = u + at\)

For the vertical component, this finds vertical velocity after a known time. **\(v\)** and **\(u\)** are vertical velocities in \(\mathrm{m\,s^{-1}}\), **\(a\)** is vertical acceleration in \(\mathrm{m\,s^{-2}}\), and **\(t\)** is time in \(\mathrm{s}\). Choose one positive vertical direction before assigning signs.

<a id="formula-constant-acceleration-displacement"></a>
> **Formula to learn: Constant-acceleration displacement.** \(s = ut + \frac{1}{2}at^2\)

Use this for the vertical motion when you need the flight time. For a horizontal launch, the initial vertical velocity is zero. If downwards is positive, \(u_y=0\), \(a_y=+g\), and the vertical displacement to the ground is positive.

<a id="formula-constant-acceleration-velocity-displacement"></a>
> **Formula to learn: Constant-acceleration velocity and displacement.** \(v^2 = u^2 + 2as\)

This vertical equation is useful when time is not needed. It connects vertical displacement to vertical velocity. As with every constant-acceleration equation, it requires straight-line motion in that component and constant acceleration.

Suppose a ball is launched horizontally and air resistance is negligible. Which statement is correct while the ball is in the air?

**A.** Its horizontal velocity decreases because the ball is falling.

**B.** Its horizontal velocity stays constant while its vertical velocity changes.

**Feedback for A:** Falling does not create a horizontal acceleration. With negligible air resistance, no horizontal force changes the horizontal velocity.

**Feedback for B:** Correct. Gravity gives a downward vertical acceleration. The horizontal component stays constant, while the downward vertical component grows.

## A reliable order for every range problem

Keep your working in two columns mentally, even if you write it in one list.

1. Use the **vertical** motion to find the time in the air.
2. Use that same time in the **horizontal** equation to find the range.
3. Find the final vertical velocity if the question asks about impact.
4. Combine the horizontal and vertical velocity components only at the end.

This order prevents a common mistake: using the total impact speed in \(s_x=v_xt\). The horizontal equation needs the horizontal component only.

## Example 1: horizontal launch from a ledge

A pebble leaves a ledge horizontally at \(8.0\,\mathrm{m\,s^{-1}}\). The ledge is \(12.0\,\mathrm{m}\) above level ground. Air resistance is negligible. Find:

1. the flight time
2. the horizontal range
3. the speed and direction just before impact

Take downwards as positive for the vertical motion. The vertical component begins from rest:

\[
u_y=0\,\mathrm{m\,s^{-1}}
\]

\[
s_y=+12.0\,\mathrm{m}
\]

\[
a_y=+9.81\,\mathrm{m\,s^{-2}}
\]

The horizontal component is constant:

\[
v_x=8.0\,\mathrm{m\,s^{-1}}
\]

### Stage 1: find the flight time from the vertical motion

\[
s_y=u_yt+\frac{1}{2}a_yt^2
\]

\[
12.0=0+\frac{1}{2}(9.81)t^2
\]

\[
t=\sqrt{\frac{2\times12.0}{9.81}}
\]

\[
t=1.56\,\mathrm{s}
\]

### Stage 2: use the same time for the horizontal range

The pebble has no horizontal acceleration, so use \(s_x=v_xt\).

\[
s_x=(8.0\,\mathrm{m\,s^{-1}})(1.56\,\mathrm{s})
\]

\[
s_x=12.5\,\mathrm{m}
\]

The \(\mathrm{s}\) cancels, leaving metres. The answer is a horizontal displacement, so metres are the correct unit.

### Stage 3: find the vertical impact velocity

Use the velocity-displacement equation because it gives the vertical impact velocity directly from the height.

\[
v_y^2=u_y^2+2a_ys_y
\]

\[
v_y^2=0+2(9.81)(12.0)
\]

\[
v_y=+15.3\,\mathrm{m\,s^{-1}}
\]

The positive sign means downwards, because downwards was chosen as positive.

### Stage 4: combine the perpendicular components

At impact, the horizontal component is still \(8.0\,\mathrm{m\,s^{-1}}\), and the vertical component is \(15.3\,\mathrm{m\,s^{-1}}\) downwards. These components are perpendicular, so use Pythagoras for the impact speed \(v\).

\[
v^2=v_x^2+v_y^2
\]

\[
v=\sqrt{8.0^2+15.3^2}
\]

\[
v=17.3\,\mathrm{m\,s^{-1}}
\]

For the angle \(\theta\) below the horizontal:

\[
\tan\theta=\frac{v_y}{v_x}=\frac{15.3}{8.0}
\]

\[
\theta=62.4^\circ
\]

**Answer:** the pebble travels \(12.5\,\mathrm{m}\) horizontally and hits the ground at \(17.3\,\mathrm{m\,s^{-1}}\), \(62.4^\circ\) below the horizontal.

The impact speed is larger than the initial horizontal speed because the pebble gains a vertical velocity component while it falls.

## Example 2: a launch with both initial components

A ball is kicked with horizontal component \(u_x=10.0\,\mathrm{m\,s^{-1}}\) and vertical component \(u_y=+6.0\,\mathrm{m\,s^{-1}}\). It lands at the same vertical height from which it was kicked. Air resistance is negligible. Find its flight time, range and impact velocity.

Take upwards as positive. The vertical displacement between launch and landing is zero:

\[
s_y=0\,\mathrm{m}
\]

\[
u_y=+6.0\,\mathrm{m\,s^{-1}}
\]

\[
a_y=-9.81\,\mathrm{m\,s^{-2}}
\]

### Stage 1: find flight time vertically

\[
s_y=u_yt+\frac{1}{2}a_yt^2
\]

\[
0=(6.0)t+\frac{1}{2}(-9.81)t^2
\]

\[
0=6.0t-4.905t^2
\]

One solution is \(t=0\), which is the launch instant. The non-zero solution is the landing time.

\[
t=1.22\,\mathrm{s}
\]

### Stage 2: find range horizontally

\[
s_x=v_xt
\]

\[
s_x=(10.0\,\mathrm{m\,s^{-1}})(1.22\,\mathrm{s})
\]

\[
s_x=12.2\,\mathrm{m}
\]

### Stage 3: find vertical impact velocity

\[
v_y=u_y+a_yt
\]

\[
v_y=+6.0+(-9.81)(1.22)
\]

\[
v_y=-6.0\,\mathrm{m\,s^{-1}}
\]

The negative sign means downwards. The horizontal component is unchanged at \(10.0\,\mathrm{m\,s^{-1}}\).

\[
v=\sqrt{10.0^2+6.0^2}=11.7\,\mathrm{m\,s^{-1}}
\]

\[
\tan\theta=\frac{6.0}{10.0}
\]

\[
\theta=31.0^\circ
\]

**Answer:** the range is \(12.2\,\mathrm{m}\). The ball lands with velocity \(11.7\,\mathrm{m\,s^{-1}}\), \(31.0^\circ\) below the horizontal.

## A useful impact check

Before calculating an impact velocity, predict two things.

- With negligible air resistance, the horizontal component at impact equals the initial horizontal component.
- The vertical component at impact points downwards if the projectile is descending.

If your final vector points upwards at the ground, or if its horizontal component has changed without a horizontal force, revisit the component choices.

A projectile is launched horizontally. Just before it lands, which pair should you combine to find its impact speed?

**A.** The total launch speed and the final vertical speed.

**B.** The constant horizontal component and the final vertical component.

**Feedback for A:** The launch speed is not a horizontal component unless the launch was horizontal, and it is not generally perpendicular to the final vertical component. Combining it this way mixes different stages of the motion.

**Feedback for B:** Correct. At one instant, the horizontal and vertical velocity components are perpendicular. Pythagoras therefore gives the magnitude of the one final velocity vector.

## Common mistakes to repair

**Using the horizontal speed to find fall time.** The fall time comes from vertical motion. A faster horizontal launch changes range, not the time required to fall through a given vertical distance in this model.

**Combining components too early.** Keep \(v_x\) and \(v_y\) separate while finding time and displacement. Recombine only for the final impact speed and direction.

**Forgetting the direction in the answer.** \(11.7\,\mathrm{m\,s^{-1}}\) is a speed. An impact velocity answer also needs a direction, such as \(31.0^\circ\) below the horizontal.

## Core recap

- A projectile has one shared flight time for its horizontal and vertical components.
- With negligible air resistance, horizontal velocity is constant, so use **\(s = vt\)** as \(s_x=v_xt\).
- Find flight time from vertical motion using **\(s = ut + \frac{1}{2}at^2\)**.
- Find vertical impact velocity with **\(v = u + at\)** or **\(v^2 = u^2 + 2as\)**.
- Combine final perpendicular components with Pythagoras only at the end, then use tangent for the angle to the horizontal.

The next lesson practises choosing the shortest valid representation, such as a verbal explanation, graph or equation, in mixed Kinematics questions.
