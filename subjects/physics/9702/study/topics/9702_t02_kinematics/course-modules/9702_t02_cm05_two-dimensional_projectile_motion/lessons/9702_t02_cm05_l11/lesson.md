# Independent components and projectile paths and Time, range and impact velocity

## Motion in two dimensions

When a ball rolls off a horizontal tabletop or a footballer kicks a ball towards the goal, the object moves forwards and vertically at the same time. It does not move forward first and then fall down afterwards. Both motions happen simultaneously during the exact same time interval.

Any object launched into the air and moving under the influence of gravity alone is called a **projectile**. Throughout this lesson, we use the standard Cambridge 9702 model:

- **air resistance is negligible**;
- the acceleration of free fall \(g\) is uniform and directed vertically downwards (\(g = 9.81\,\mathrm{m\,s^{-2}}\)).

Under these conditions, the two-dimensional motion can be completely separated into two independent, perpendicular components:

1. a **horizontal component** with uniform velocity (zero horizontal acceleration);
2. a **vertical component** with uniform downward acceleration \(g\) (due to gravity).

The word **independent** means that the horizontal motion has no effect on the vertical motion, and the vertical motion has no effect on the horizontal motion. What connects the two components is **time**: both motions happen simultaneously and share the exact same duration of flight \(t\).

## Controlled definitions for motion quantities

Before analysing components, remember the precise Cambridge definitions of velocity and acceleration.

<a id="definition-velocity"></a>
> **Definition to learn: velocity.** rate of change of displacement

Velocity is a vector quantity with SI unit \(\mathrm{m\,s^{-1}}\). In two dimensions, velocity has two perpendicular components: a horizontal velocity \(v_x\) and a vertical velocity \(v_y\). The subscripts \(x\) and \(y\) identify the perpendicular directions.

<a id="definition-acceleration"></a>
> **Definition to learn: acceleration.** rate of change of velocity

Acceleration is a vector quantity with SI unit \(\mathrm{m\,s^{-2}}\). Because gravity acts purely vertically downwards:

- vertical acceleration is \(a_y = -9.81\,\mathrm{m\,s^{-2}}\) (taking upwards as positive);
- horizontal acceleration is zero (\(a_x = 0\)) when air resistance is negligible.

A ball is thrown with an initial horizontal velocity of \(12.0\,\mathrm{m\,s^{-1}}\) and air resistance is negligible. While the ball is in flight, which statement correctly describes its horizontal and vertical accelerations?

**A.** Its horizontal acceleration is zero, and its vertical acceleration is \(9.81\,\mathrm{m\,s^{-2}}\) downwards.

**B.** Both its horizontal and vertical accelerations are directed downwards.

**Feedback for A:** Correct. Gravity pulls only vertically downwards. There is no force acting horizontally in the absence of air resistance, so horizontal acceleration is zero while vertical acceleration is \(g\) downwards.

**Feedback for B:** Incorrect. Acceleration is a vector. An acceleration cannot act downwards and be "horizontal" at the same time. The horizontal component of acceleration is zero.

## Resolving initial launch velocity into components

When a projectile is launched with an initial speed \(u\) at an angle \(\theta\) above the horizontal, its initial velocity vector forms the hypotenuse of a right-angled triangle.

Resolving the initial velocity into perpendicular components:

- **Horizontal component:** the side adjacent to angle \(\theta\):

\[
u_x = u \cos\theta
\]

- **Vertical component:** the side opposite to angle \(\theta\):

\[
u_y = u \sin\theta
\]

For a purely **horizontal launch** (such as rolling off a flat desk or dropping a package from an aircraft flying horizontally):

\[
\theta = 0^\circ \implies u_x = u, \quad u_y = 0
\]

Always check that the angle \(\theta\) is measured relative to the horizontal before writing sine or cosine. If the angle is given relative to the vertical, the roles of sine and cosine are reversed.

## Equations for the two independent components

Because the two perpendicular motions are independent, we use separate equations for each component. Never mix horizontal and vertical quantities in the same equation.

### Horizontal motion: uniform velocity

Because no horizontal force acts on the projectile (\(a_x = 0\)), its horizontal velocity remains constant throughout the entire flight:

\[
v_x = u_x = \text{constant}
\]

The horizontal displacement \(s_x\) (often called the **range**, \(R\)) is calculated from the formula for uniform motion:

<a id="formula-uniform-motion-displacement"></a>
> **Formula to learn: Displacement in uniform motion.**
>
> \[
> s = vt
> \]

Applied to the horizontal component:

\[
s_x = u_x t = (u \cos\theta) t
\]

Here \(s_x\) is horizontal displacement in \(\mathrm{m}\), \(u_x\) is constant horizontal velocity in \(\mathrm{m\,s^{-1}}\), and \(t\) is time in \(\mathrm{s}\).

### Vertical motion: uniform acceleration

Gravity acts vertically downwards with constant acceleration \(g\). The vertical motion is uniformly accelerated straight-line motion, governed by the standard constant-acceleration equations:

<a id="formula-constant-acceleration-displacement"></a>
> **Formula to learn: Constant-acceleration displacement.**
>
> \[
> s = ut + \frac{1}{2}at^2
> \]

Applied to the vertical component (with upwards chosen as positive, so \(a_y = -g\)):

\[
s_y = u_y t - \frac{1}{2}gt^2
\]

To find the vertical velocity \(v_y\) at any time \(t\):

\[
v_y = u_y + a_y t = u_y - gt
\]

To find the vertical velocity from vertical displacement directly:

\[
v_y^2 = u_y^2 + 2a_y s_y = u_y^2 - 2gs_y
\]

Here \(s_y\) is vertical displacement in \(\mathrm{m}\), \(u_y\) is initial vertical velocity in \(\mathrm{m\,s^{-1}}\), and \(v_y\) is vertical velocity at time \(t\) in \(\mathrm{m\,s^{-1}}\).

## Why the projectile path is a parabola

Consider equal intervals of time after launch:

1. In each equal time interval \(\Delta t\), the projectile moves forward by the exact same horizontal distance \(\Delta s_x = u_x \Delta t\).
2. During that same time interval, the vertical velocity changes by \(\Delta v_y = -g \Delta t\). On the way up, the vertical distance gained in each successive interval decreases until the turning point. On the way down, the vertical distance fallen in each successive interval increases.

Combining uniform horizontal motion with uniformly accelerated vertical motion produces a smooth curved trajectory: a **parabola**.

At the highest point (apex) of the trajectory:

- the **vertical velocity is momentarily zero**: \(v_y = 0\,\mathrm{m\,s^{-1}}\);
- the **horizontal velocity is NOT zero**: \(v_x = u_x\);
- the **total velocity at the top** is purely horizontal: \(v_{\text{top}} = u_x\).

At the highest point of a football's flight, which statement correctly describes its velocity?

**A.** Its velocity is zero because it has reached the top of its path.

**B.** Its vertical velocity is zero, but its horizontal velocity is non-zero, so it is still moving.

**Feedback for A:** Incorrect. Only the vertical component of velocity is zero at the top. The football continues to travel forward at its constant horizontal velocity.

**Feedback for B:** Correct. At the turning point of the vertical motion, \(v_y = 0\), but the independent horizontal component \(v_x = u_x\) remains unchanged.

## Standard strategy: connecting vertical time to horizontal range

Every projectile calculation follows a structured sequence:

1. **Resolve initial velocity:** find \(u_x\) and \(u_y\).
2. **Find time of flight \(t\) using the vertical component:** the duration of the flight is determined entirely by vertical constraints (e.g. falling through height \(h\), or returning to the ground \(s_y = 0\)).
3. **Calculate horizontal range using that shared time:** substitute \(t\) into \(s_x = u_x t\).
4. **Determine impact velocity only at the very end:** calculate the final vertical component \(v_y\), keep the constant horizontal component \(v_x\), and combine them using Pythagoras and trigonometry.

## Combining components to find impact velocity

When an exam question asks for the **velocity** of an object just before it strikes the ground, an answer that states only a speed is incomplete. Velocity is a vector and requires both:

- a **magnitude** (speed);
- a **direction** (angle relative to the horizontal or vertical).

At impact, the projectile has two mutually perpendicular velocity components:

- horizontal component: \(v_x = u_x\) (directed horizontally forwards);
- vertical component: \(v_y\) (directed downwards).

Because the two components are perpendicular, use the Pythagorean theorem to calculate the impact speed \(v\):

\[
v = \sqrt{v_x^2 + v_y^2}
\]

To find the angle \(\theta\) of the impact velocity below the horizontal:

\[
\tan\theta = \frac{|v_y|}{v_x} \implies \theta = \tan^{-1}\left(\frac{|v_y|}{v_x}\right)
\]

State the direction clearly in your final answer, for example: "\(18.2\,\mathrm{m\,s^{-1}}\) at an angle of \(54.1^\circ\) below the horizontal".

## Worked example 1: horizontal launch from a cliff

A rescue package is dropped from an aircraft flying horizontally at a constant speed of \(45.0\,\mathrm{m\,s^{-1}}\) at an altitude of \(120\,\mathrm{m}\) above flat level ground. Air resistance is negligible.

Calculate:

1. the time taken for the package to reach the ground;
2. the horizontal distance (range) travelled by the package while falling;
3. the velocity (magnitude and direction) of the package just before it strikes the ground.

Use \(g = 9.81\,\mathrm{m\,s^{-2}}\).

### Step 1: initial conditions

At release, the package has the same velocity as the aircraft. It moves horizontally:

\[
u_x = 45.0\,\mathrm{m\,s^{-1}}, \quad u_y = 0\,\mathrm{m\,s^{-1}}
\]

Take **downwards as positive** for the vertical motion:

\[
s_y = +120\,\mathrm{m}, \quad a_y = +9.81\,\mathrm{m\,s^{-2}}
\]

### Part 1: time of flight

The time of flight depends exclusively on the vertical motion:

\[
s_y = u_y t + \frac{1}{2}a_y t^2
\]

Because \(u_y = 0\):

\[
120 = 0 + \frac{1}{2}(9.81)t^2
\]

\[
t^2 = \frac{2 \times 120}{9.81} = \frac{240}{9.81} = 24.46\,\mathrm{s^2}
\]

\[
t = \sqrt{24.46} = 4.95\,\mathrm{s}
\]

**Answer:** the time taken to reach the ground is **\(4.95\,\mathrm{s}\)**.

### Part 2: horizontal range

The horizontal component has zero acceleration, so it travels at constant velocity for the entire \(4.95\,\mathrm{s}\):

\[
s_x = u_x t
\]

\[
s_x = (45.0\,\mathrm{m\,s^{-1}})(4.946\,\mathrm{s}) = 222.6\,\mathrm{m}
\]

Round to 3 significant figures:

**Answer:** the horizontal distance travelled is **\(223\,\mathrm{m}\)**.

### Part 3: impact velocity

At impact, find the vertical velocity component:

\[
v_y = u_y + a_y t = 0 + (9.81\,\mathrm{m\,s^{-2}})(4.946\,\mathrm{s}) = 48.52\,\mathrm{m\,s^{-1}} \quad (\text{downwards})
\]

(Alternatively, \(v_y^2 = 0^2 + 2(9.81)(120) = 2354.4 \implies v_y = 48.52\,\mathrm{m\,s^{-1}}\).)

The horizontal velocity component remains unchanged:

\[
v_x = 45.0\,\mathrm{m\,s^{-1}} \quad (\text{forwards})
\]

Now combine the two perpendicular components using Pythagoras:

\[
v = \sqrt{v_x^2 + v_y^2} = \sqrt{(45.0)^2 + (48.52)^2} = \sqrt{2025 + 2354.2} = \sqrt{4379.2} = 66.18\,\mathrm{m\,s^{-1}}
\]

Find the angle \(\theta\) below the horizontal:

\[
\tan\theta = \frac{v_y}{v_x} = \frac{48.52}{45.0} = 1.078
\]

\[
\theta = \tan^{-1}(1.078) = 47.2^\circ
\]

**Answer:** the impact velocity has magnitude **\(66.2\,\mathrm{m\,s^{-1}}\)** at an angle of **\(47.2^\circ\) below the horizontal**.

## Worked example 2: angled projection over level ground

A golf ball is hit off the ground with an initial speed of \(28.0\,\mathrm{m\,s^{-1}}\) at an angle of \(35.0^\circ\) above the horizontal. The ground is level and air resistance is negligible.

Calculate:

1. the maximum height reached by the ball above the ground;
2. the total time of flight;
3. the horizontal range of the ball;
4. the velocity of the ball just before it lands.

Use \(g = 9.81\,\mathrm{m\,s^{-2}}\).

### Step 1: resolve initial velocity into components

\[
u_x = u \cos\theta = 28.0 \cos(35.0^\circ) = 28.0 \times 0.8192 = 22.94\,\mathrm{m\,s^{-1}}
\]

\[
u_y = u \sin\theta = 28.0 \sin(35.0^\circ) = 28.0 \times 0.5736 = 16.06\,\mathrm{m\,s^{-1}}
\]

Take **upwards as positive** for vertical motion:

\[
a_y = -9.81\,\mathrm{m\,s^{-2}}
\]

### Part 1: maximum height

At maximum height, \(v_y = 0\,\mathrm{m\,s^{-1}}\):

\[
v_y^2 = u_y^2 + 2a_y s_y
\]

\[
0 = (16.06\,\mathrm{m\,s^{-1}})^2 + 2(-9.81\,\mathrm{m\,s^{-2}})H
\]

\[
19.62 H = 257.9 \implies H = \frac{257.9}{19.62} = 13.15\,\mathrm{m}
\]

**Answer:** maximum height reached is **\(13.1\,\mathrm{m}\)**.

### Part 2: total time of flight

The ball lands on level ground, so its net vertical displacement between launch and landing is zero: \(s_y = 0\).

\[
s_y = u_y t + \frac{1}{2}a_y t^2
\]

\[
0 = (16.06)t + \frac{1}{2}(-9.81)t^2 = 16.06t - 4.905t^2
\]

Factor out \(t\):

\[
t(16.06 - 4.905t) = 0
\]

The solution \(t = 0\) is the moment of launch. The landing time is:

\[
t = \frac{16.06}{4.905} = 3.274\,\mathrm{s}
\]

(Alternatively, by symmetry, time to the top is \(t_{\text{top}} = \frac{u_y}{g} = \frac{16.06}{9.81} = 1.637\,\mathrm{s}\), so total time is \(2 \times 1.637 = 3.27\,\mathrm{s}\).)

**Answer:** total time of flight is **\(3.27\,\mathrm{s}\)**.

### Part 3: horizontal range

Use the total time of flight in the horizontal equation:

\[
s_x = u_x t
\]

\[
s_x = (22.94\,\mathrm{m\,s^{-1}})(3.274\,\mathrm{s}) = 75.1\,\mathrm{m}
\]

**Answer:** the horizontal range is **\(75.1\,\mathrm{m}\)**.

### Part 4: landing velocity

Find the vertical velocity component at landing:

\[
v_y = u_y + a_y t = +16.06 + (-9.81)(3.274) = 16.06 - 32.12 = -16.06\,\mathrm{m\,s^{-1}}
\]

Notice that \(v_y = -u_y\), confirming the vertical symmetry over level ground.

The horizontal component is unchanged:

\[
v_x = u_x = 22.94\,\mathrm{m\,s^{-1}}
\]

Combine the components:

\[
v = \sqrt{v_x^2 + v_y^2} = \sqrt{(22.94)^2 + (-16.06)^2} = \sqrt{526.2 + 257.9} = \sqrt{784.1} = 28.0\,\mathrm{m\,s^{-1}}
\]

\[
\tan\theta = \frac{|v_y|}{v_x} = \frac{16.06}{22.94} = 0.7001 \implies \theta = 35.0^\circ
\]

**Answer:** the landing velocity is **\(28.0\,\mathrm{m\,s^{-1}}\)** at an angle of **\(35.0^\circ\) below the horizontal**. Over level ground with no air resistance, the impact speed equals the launch speed, and the impact angle equals the launch angle.

A projectile is launched from a cliff top and lands on the ground below. Which of the following statements about its impact speed is correct?

**A.** The impact speed is greater than the launch speed.

**B.** The impact speed is equal to the launch speed.

**Feedback for A:** Correct. As the projectile falls below its initial launch height, it gains additional downward vertical speed due to gravitational acceleration. Since the horizontal speed remains constant and the vertical speed is larger than at launch, the resultant speed \(\sqrt{v_x^2 + v_y^2}\) is greater than the launch speed.

**Feedback for B:** Incorrect. The impact speed equals the launch speed only when landing at the exact same vertical level as the launch. Landing at a lower level adds kinetic energy and increases vertical speed.

## Common exam traps and misconceptions

1. **Using the horizontal speed to find the fall time:**
   The horizontal speed affects how far the object travels sideways, but does not affect how fast it falls. The fall time is determined solely by the vertical displacement and vertical acceleration.
2. **Substituting the total speed into horizontal equations:**
   Never write \(s_x = v t\) using the resultant launch speed \(u\). You must use the horizontal component \(u_x = u \cos\theta\).
3. **Assuming velocity is zero at the apex:**
   At the highest point of a projectile's path, the vertical velocity is zero (\(v_y = 0\)), but the horizontal velocity is not zero (\(v_x = u_x\)). The object is still moving forward.
4. **Adding components as scalars:**
   Never add \(v_x\) and \(v_y\) algebraically (e.g. \(v \neq v_x + v_y\)). They are perpendicular vectors and must be combined using the Pythagorean theorem: \(v = \sqrt{v_x^2 + v_y^2}\).
5. **Forgetting direction in impact velocity questions:**
   When asked for impact velocity, you must give both the magnitude (speed) and the angle to the horizontal. Stating speed alone loses the final mark.

## Core recap

- Projectile motion with negligible air resistance consists of two independent perpendicular motions sharing a common time \(t\).
- The horizontal motion has zero acceleration (\(a_x = 0\)), so horizontal velocity is constant: \(v_x = u \cos\theta\), and horizontal range is \(s_x = u_x t\).
- The vertical motion has constant downward acceleration \(g = 9.81\,\mathrm{m\,s^{-2}}\), governed by \(v_y = u_y - gt\) and \(s_y = u_y t - \frac{1}{2}gt^2\).
- The time of flight is governed by vertical constraints and links the vertical fall to the horizontal range.
- At maximum height, vertical velocity is zero (\(v_y = 0\)), but horizontal velocity remains non-zero (\(v_x = u_x\)).
- To find impact velocity, combine the final perpendicular components using Pythagoras: \(v = \sqrt{v_x^2 + v_y^2}\), and find the direction using \(\tan\theta = |v_y| / v_x\).
