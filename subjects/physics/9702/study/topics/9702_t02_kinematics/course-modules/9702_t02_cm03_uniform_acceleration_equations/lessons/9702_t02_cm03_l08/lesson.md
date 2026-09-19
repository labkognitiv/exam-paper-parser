# Multi-stage and reverse problems

## One journey can contain several intervals

Imagine a test car that speeds up, then brakes to a stop. It has not completed
one single motion interval. It has completed two.

Each interval may have a different acceleration. That means one
constant-acceleration equation cannot describe the entire journey at once.
Instead, split the journey into **stages**. Solve one stage at a time. Then
carry the connecting quantity into the next stage.

For a journey in one straight line, choose a positive direction before writing
any values. In this lesson, forward is positive. A velocity, acceleration or
displacement in the opposite direction has a negative sign.

Teacher question: *What connects two stages when an object moves smoothly from
one to the next?* Its velocity at the end of stage 1 is its initial velocity
at the start of stage 2.

## Keep the symbols local to one stage

The letters in a motion equation always describe one chosen interval:

- **(u)** is the velocity at the start of that interval, in
  (mathrm{m,s^{-1}}).
- **(v)** is the velocity at the end of that interval, in
  (mathrm{m,s^{-1}}).
- **(a)** is the constant acceleration during that interval, in
  (mathrm{m,s^{-2}}).
- **(s)** is the displacement during that interval, in (mathrm{m}).
- **(t)** is the time for that interval, in (mathrm{s}).

This is important. If stage 2 begins after 6 seconds of a longer journey, its
own time can still be written as (t=0) at the start of stage 2. Do not mix a
whole-journey time with the acceleration from only one stage.

Here are the three equations already established for straight-line motion with
**constant acceleration** in magnitude and direction.

## Formula 1: change in velocity {#constant-acceleration-velocity}

> **Formula to learn: Constant-acceleration velocity.**
>
> \[
> v = u + at
> \]

Use this when the stage has a known time and you need a velocity, acceleration
or time. The term (at) is the change in velocity. Its unit is

\[
\mathrm{m\,s^{-2}}\times\mathrm{s}=\mathrm{m\,s^{-1}}
\]

so it can be added to (u).

## Formula 2: displacement when time is known {#constant-acceleration-displacement}

> **Formula to learn: Constant-acceleration displacement.**
>
> \[
> s = ut + \frac{1}{2}at^2
> \]

Use this when a stage has a known time and you need its displacement. The
first term, (ut), is the displacement that would occur at the starting
velocity. The second term adds the effect of acceleration during the interval.

Both terms have unit metre. For the second term:

\[
\mathrm{m\,s^{-2}}\times\mathrm{s^2}=\mathrm{m}
\]

## Formula 3: displacement when time is not known {#constant-acceleration-velocity-displacement}

> **Formula to learn: Constant-acceleration velocity and displacement.**
>
> \[
> v^2 = u^2 + 2as
> \]

This equation has no time term. It is especially useful in a stage where the
two velocities, acceleration and displacement are connected, but the time is
not given or not needed. The square applies to the whole velocity, including
its sign before squaring.

All three equations require straight-line motion with constant acceleration
for the individual stage being solved. They do not require every stage of the
whole journey to have the same acceleration.

## A reliable plan for a multi-stage problem

Before calculating, make a short stage table. This prevents values from one
stage being placed into another by accident.

| Stage | (u) | (v) | (a) | (t) | (s) |
| --- | --- | --- | --- | --- | --- |
| 1 | start velocity | end velocity | acceleration in stage 1 | time in stage 1 | displacement in stage 1 |
| 2 | end velocity from stage 1 | end velocity for stage 2 | acceleration in stage 2 | time in stage 2 | displacement in stage 2 |

Then follow this order.

1. Mark where each stage starts and ends.
2. Choose the positive direction once.
3. Write the known values for stage 1 only.
4. Find the quantity that joins stage 1 to stage 2.
5. Start a fresh row for stage 2 and use that joining value as its (u).
6. Add stage displacements only after their signs have been checked.

Teacher question: *If a car finishes stage 1 at
(+12\ \mathrm{m\,s^{-1}}), what is (u) for a directly connected stage 2?*
It is (+12\ \mathrm{m\,s^{-1}}), not zero. The car does not restart from
rest just because a new line of working begins.

A car accelerates forward for (4.0\ \mathrm{s}), then brakes while still
moving forward. Which statement is correct?

- **A:** The acceleration in the braking stage is negative if forward is
  positive.
- **B:** The acceleration in the braking stage is positive because the car is
  still moving forward.

**Feedback for A:** Correct. Acceleration describes how velocity changes. The
forward velocity is becoming smaller, so its change is negative. With forward
chosen as positive, braking acceleration is negative.

**Feedback for B:** Not correct. Velocity and acceleration need not have the
same sign. The car can have positive velocity while negative acceleration
slows it down.

## Worked example 1: accelerate, then brake

A scooter travels along a straight road. Take its direction of travel as
positive.

It passes a marker at (4.0\ \mathrm{m\,s^{-1}}). It accelerates uniformly
at (+1.5\ \mathrm{m\,s^{-2}}) for (8.0\ \mathrm{s}). It then brakes
uniformly at (-3.0\ \mathrm{m\,s^{-2}}) until it stops.

Find the total displacement from the marker to the stopping point.

### Stage 1: find the joining velocity

Stage 1 begins at the marker, so

\[
u_1=+4.0\ \mathrm{m\,s^{-1}}
\]

\[
a_1=+1.5\ \mathrm{m\,s^{-2}}
\]

\[
t_1=8.0\ \mathrm{s}
\]

The time is known, so use (v=u+at):

\[
v_1=u_1+a_1t_1
\]

\[
v_1=+4.0\ \mathrm{m\,s^{-1}}+
(+1.5\ \mathrm{m\,s^{-2}})(8.0\ \mathrm{s})
\]

\[
v_1=+16\ \mathrm{m\,s^{-1}}
\]

This is the initial velocity of the braking stage:

\[
u_2=v_1=+16\ \mathrm{m\,s^{-1}}
\]

Now find stage 1 displacement. The same stage has a known time, so use

\[
s_1=u_1t_1+\frac12a_1t_1^2
\]

\[
s_1=(+4.0\ \mathrm{m\,s^{-1}})(8.0\ \mathrm{s})
+\frac12(+1.5\ \mathrm{m\,s^{-2}})(8.0\ \mathrm{s})^2
\]

\[
s_1=32\ \mathrm{m}+48\ \mathrm{m}
\]

\[
s_1=+80\ \mathrm{m}
\]

### Stage 2: find braking displacement

The scooter stops, so the final velocity for stage 2 is

\[
v_2=0\ \mathrm{m\,s^{-1}}
\]

Its braking acceleration is

\[
a_2=-3.0\ \mathrm{m\,s^{-2}}
\]

No time is given for stage 2. Use the equation without time:

\[
v_2^2=u_2^2+2a_2s_2
\]

Rearrange before substituting:

\[
v_2^2-u_2^2=2a_2s_2
\]

\[
s_2=\frac{v_2^2-u_2^2}{2a_2}
\]

\[
s_2=\frac{(0\ \mathrm{m\,s^{-1}})^2-
(16\ \mathrm{m\,s^{-1}})^2}
{2(-3.0\ \mathrm{m\,s^{-2}})}
\]

\[
s_2=\frac{-256}{-6.0}\ \mathrm{m}
\]

\[
s_2=+42.7\ \mathrm{m}
\]

The two negative signs cancel. This makes sense because the scooter continues
forward during the braking stage, so its displacement is positive.

### Combine the stages

\[
s_{\text{total}}=s_1+s_2
\]

\[
s_{\text{total}}=+80\ \mathrm{m}+42.7\ \mathrm{m}
\]

\[
s_{\text{total}}=+123\ \mathrm{m}
\]

**Answer:** The scooter stops (123\ \mathrm{m}) forward of the marker.

**Check:** The scooter has a positive velocity throughout both stages until it
stops. Both stage displacements should therefore be positive. The final unit
is metre, as required for displacement.

## Reverse problems: begin with what you need to find

A **reverse problem** gives an end result and asks you to work back to an
earlier quantity. The equations do not change. Only the order of decisions
changes.

For example, if a vehicle starts from rest, reaches a stated final velocity,
and covers a stated displacement, the time is missing. Begin with the equation
that does not contain time. Find acceleration first. Then use the velocity
equation to find time.

Teacher question: *Why not begin with (v=u+at) in that situation?* Both
(a) and (t) would be unknown, so one equation would contain two unknown
quantities. Find one of them first using an equation that avoids the other.

## Worked example 2: work backwards through a single stage

A test car starts from rest and accelerates uniformly along a straight track.
After travelling (162\ \mathrm{m}), its velocity is
(18\ \mathrm{m\,s^{-1}}).

Find its acceleration and the time taken.

Choose the direction of motion as positive. The car starts from rest, so

\[
u=0\ \mathrm{m\,s^{-1}}
\]

The final velocity and displacement are

\[
v=+18\ \mathrm{m\,s^{-1}}
\]

\[
s=+162\ \mathrm{m}
\]

### Step 1: find acceleration without time

Time is not known. Use

\[
v^2=u^2+2as
\]

Rearrange carefully:

\[
v^2-u^2=2as
\]

\[
a=\frac{v^2-u^2}{2s}
\]

Now substitute the complete values:

\[
a=\frac{(+18\ \mathrm{m\,s^{-1}})^2-
(0\ \mathrm{m\,s^{-1}})^2}
{2(+162\ \mathrm{m})}
\]

\[
a=\frac{324}{324}\ \mathrm{m\,s^{-2}}
\]

\[
a=+1.0\ \mathrm{m\,s^{-2}}
\]

The positive sign agrees with a car gaining forward velocity.

### Step 2: use the acceleration to find time

Now (u), (v) and (a) are known. Use

\[
v=u+at
\]

Subtract (u):

\[
v-u=at
\]

Divide by (a):

\[
t=\frac{v-u}{a}
\]

\[
t=\frac{+18\ \mathrm{m\,s^{-1}}-
0\ \mathrm{m\,s^{-1}}}{+1.0\ \mathrm{m\,s^{-2}}}
\]

\[
t=18\ \mathrm{s}
\]

**Answer:** The acceleration is (+1.0\ \mathrm{m\,s^{-2}}) and the time
is (18\ \mathrm{s}).

**Check:** With constant acceleration from (0) to
(18\ \mathrm{m\,s^{-1}}), the average velocity is
(9.0\ \mathrm{m\,s^{-1}}). In (18\ \mathrm{s}), this gives

\[
(9.0\ \mathrm{m\,s^{-1}})(18\ \mathrm{s})=162\ \mathrm{m}
\]

which matches the stated displacement.

## A mistake worth catching early

It is tempting to put the total journey time into every stage equation. That
only works if that equation describes the complete journey with one constant
acceleration. In a multi-stage problem, it usually does not.

Suppose stage 1 lasts (5.0\ \mathrm{s}) and stage 2 lasts
(3.0\ \mathrm{s}). The time in a stage 2 equation is
(3.0\ \mathrm{s}), not (8.0\ \mathrm{s}). Stage 2 begins only after the
first stage has finished.

A car has two stages. It accelerates for (5.0\ \mathrm{s}) and then brakes
for (3.0\ \mathrm{s}). In a displacement equation for the braking stage,
which time belongs in (t)?

- **A:** (3.0\ \mathrm{s})
- **B:** (8.0\ \mathrm{s})

**Feedback for A:** Correct. The braking equation models stage 2 only. Its
time is the duration of braking, (3.0\ \mathrm{s}).

**Feedback for B:** Not correct. (8.0\ \mathrm{s}) is the total journey
time. It would combine stage 1 acceleration with stage 2 motion and give an
incorrect displacement.

## Core recap

- Split a changing journey into **stages**. Each stage must separately have
  straight-line motion with constant acceleration before using these equations.
- Carry the end velocity of one directly connected stage into the next stage
  as its initial velocity.
- Use (v=u+at) when time is useful, (s=ut+\frac12at^2) for displacement
  with known time, and (v^2=u^2+2as) when time is not involved.
- Keep one sign convention and retain signs in every line of calculation.
- For a **reverse problem**, choose an equation with only one unknown first.
  Use its result in the next equation.

The next lesson applies these methods to falling objects, including the
acceleration due to gravity and its sign.
