# Choosing between words, graphs and equations

Earlier lessons gave you several ways to describe the same motion. You can use **words**, a **graph**, or an **equation**. This lesson is about making the first decision in an unfamiliar question: which representation will reveal the answer most directly?

Imagine a ball thrown upwards. A sentence can tell you that it slows down, stops for an instant, then falls. A velocity-time graph can show the same change. An equation can calculate a height or a time. These are not competing stories. They are different ways to express one physical situation.

## Start by asking what the question needs

Before choosing a formula, pause and ask: **What type of answer has the question asked for?**

- Use **words** when the question asks for a definition, a comparison, an explanation, or a physical reason.
- Use a **graph** when the question asks for a changing quantity, a gradient, an area, a shape, or a sketch.
- Use an **equation** when the motion has constant acceleration and the known and unknown quantities fit one relationship.

A useful first line on rough paper is:

\[
\text{question asks for} \longrightarrow \text{shortest valid representation}
\]

Ask yourself: *Does this question need a reason, a changing-picture, or a numerical relationship?*

## Keep the key meanings available

The representation may change, but the meanings of the quantities do not.

### Displacement {#def-displacement}

> **Definition to learn: displacement.** distance in a specified direction from a point

Displacement tells you where the object is relative to a chosen point. It includes a direction. In one dimension, choose one direction as positive before using a sign. For example, if east is positive, a displacement of \(-3\,\mathrm{m}\) means \(3\,\mathrm{m}\) west.

Do not replace displacement with distance without checking the path. Distance is the total length travelled. Displacement is the straight directed change of position.

### Velocity {#def-velocity}

> **Definition to learn: velocity.** rate of change of displacement

Velocity tells you how quickly displacement changes. Its SI unit is metres per second, \(\mathrm{m\,s^{-1}}\). A negative velocity does not mean that the object has a negative speed. It means the object moves in the chosen negative direction.

### Acceleration {#def-acceleration}

> **Definition to learn: acceleration.** rate of change of velocity

Acceleration tells you how quickly velocity changes. Its SI unit is metres per second squared, \(\mathrm{m\,s^{-2}}\). The squared time unit appears because velocity changes by a certain number of \(\mathrm{m\,s^{-1}}\) every second.

For a falling object, you might choose upward as positive. Gravity then gives a negative acceleration because it acts downward. The sign comes from the direction choice, not from the size of gravity changing.

## When a graph is the shortest route

A graph is useful when the question is about a quantity changing with time. Read the axes before doing any calculation. The vertical axis is the changing quantity. The horizontal axis is usually time.

### Displacement from a velocity-time graph

The **area under a velocity-time graph** gives displacement. Areas above the time axis are positive. Areas below it are negative.

If the graph has several regions, calculate each signed area separately, then add them. This is often safer than trying to remember the whole journey at once.

### Velocity from a displacement-time graph

The **gradient** of a displacement-time graph gives velocity. Gradient means vertical change divided by horizontal change:

\[
\text{gradient}=\frac{\Delta \text{displacement}}{\Delta t}
\]

A horizontal line has zero gradient, so the object is stationary. A downward slope has negative velocity when upward or forward has been chosen as positive.

### Acceleration from a velocity-time graph

The **gradient** of a velocity-time graph gives acceleration.

### Acceleration {#formula-acceleration}

> **Formula to learn: Acceleration.** \(a = \frac{\Delta v}{\Delta t}\)

Here \(a\) is acceleration in \(\mathrm{m\,s^{-2}}\), \(\Delta v\) is the change in velocity in \(\mathrm{m\,s^{-1}}\), and \(\Delta t\) is the time interval in seconds, \(\mathrm{s}\). The symbol \(\Delta\) means "change in".

Use this formula, or the graph gradient, when you compare two velocities over a stated time interval. A straight line on a velocity-time graph has constant gradient. It therefore shows constant acceleration.

### Worked example 1: decide what a velocity-time graph is for

A skateboarder has velocity \(+6.0\,\mathrm{m\,s^{-1}}\) at \(t=0\). Their velocity decreases uniformly to \(0\,\mathrm{m\,s^{-1}}\) in \(3.0\,\mathrm{s}\).

Find:

1. the acceleration
2. the displacement during the \(3.0\,\mathrm{s}\)

**Decision.** The first answer is a rate of velocity change, so use the gradient or the acceleration equation. The second answer is displacement over the whole interval, so use the area below a velocity-time graph. The graph would be a straight line from \(+6.0\,\mathrm{m\,s^{-1}}\) to zero.

For acceleration:

\[
a=\frac{\Delta v}{\Delta t}
\]

\[
a=\frac{0-6.0\,\mathrm{m\,s^{-1}}}{3.0\,\mathrm{s}}
\]

\[
a=-2.0\,\mathrm{m\,s^{-2}}
\]

The negative sign means the acceleration is opposite to the chosen positive direction. The skateboarder is slowing while still moving in the positive direction.

For displacement, the area is a triangle:

\[
s=\frac{1}{2}\times \text{base}\times \text{height}
\]

\[
s=\frac{1}{2}\times 3.0\,\mathrm{s}\times 6.0\,\mathrm{m\,s^{-1}}
\]

\[
s=9.0\,\mathrm{m}
\]

The unit check is useful:

\[
\mathrm{s}\times\mathrm{m\,s^{-1}}=\mathrm{m}
\]

So the area has the unit of displacement. The positive answer matches the fact that the skateboarder never reverses direction.

Suppose the question instead asked for the shape of the graph. An equation would calculate a number, but it would not communicate the required shape. A straight downward-sloping line is then the better representation.

**A velocity-time graph is a straight line that slopes down to the time axis. Which statement correctly identifies the displacement in this interval?**

- **A:** It is the triangular area between the line and the time axis.
- **B:** It is the gradient of the line.

**Feedback for A:** Correct. On a velocity-time graph, signed area gives displacement. The triangle in this example gives \(+9.0\,\mathrm{m}\).

**Feedback for B:** Not correct. The gradient of a velocity-time graph gives acceleration. Here the gradient is \(-2.0\,\mathrm{m\,s^{-2}}\), not displacement.

## When an equation is the shortest route

Use a constant-acceleration equation only when acceleration is constant and all quantities refer to one straight-line direction. Choose a positive direction first. Then keep every velocity, acceleration and displacement sign consistent with that choice.

Do not choose an equation because it is familiar. First list the known quantities, identify the unknown, and select a formula that contains those quantities but no unneeded unknown.

### Final velocity after constant acceleration {#formula-constant-acceleration-velocity}

> **Formula to learn: Constant-acceleration velocity.** \(v = u + at\)

Here \(v\) is final velocity in \(\mathrm{m\,s^{-1}}\), \(u\) is initial velocity in \(\mathrm{m\,s^{-1}}\), \(a\) is constant acceleration in \(\mathrm{m\,s^{-2}}\), and \(t\) is time in seconds. Use it when you need a velocity after a known time, or when the time can be found from known velocities and acceleration.

### Displacement after constant acceleration {#formula-constant-acceleration-displacement}

> **Formula to learn: Constant-acceleration displacement.** \(s = ut + \frac{1}{2}at^2\)

Here \(s\) is displacement in metres, \(\mathrm{m}\). The other symbols have the meanings above. Use this formula when time is known and you need displacement. The \(t^2\) means \(t\times t\), so its unit is \(\mathrm{s^2}\).

### Velocity and displacement without time {#formula-constant-acceleration-velocity-displacement}

> **Formula to learn: Constant-acceleration velocity and displacement.** \(v^2 = u^2 + 2as\)

Use this formula when time is not given and is not needed. The symbols \(v\), \(u\), \(a\), and \(s\) have the same meanings and units as above. The squared velocities mean that two possible directions can require careful sign decisions before the square is used.

### Worked example 2: select an equation by removing an unnecessary unknown

A stone is thrown vertically upward at \(+14\,\mathrm{m\,s^{-1}}\). Take upward as positive. Air resistance is negligible. Find its maximum height above the release point. Use \(g=9.81\,\mathrm{m\,s^{-2}}\).

**Decision.** At maximum height, the stone has vertical velocity \(v=0\). The question gives no time, and does not need time. Choose the equation that links \(v\), \(u\), \(a\), and \(s\) without \(t\):

\[
v^2=u^2+2as
\]

The known values are:

\[
v=0\,\mathrm{m\,s^{-1}}
\]

\[
u=+14\,\mathrm{m\,s^{-1}}
\]

\[
a=-9.81\,\mathrm{m\,s^{-2}}
\]

Substitute the signs as well as the numbers:

\[
0^2=(+14)^2+2(-9.81)s
\]

\[
0=196-19.62s
\]

Add \(19.62s\) to both sides:

\[
19.62s=196
\]

\[
s=\frac{196}{19.62}\,\mathrm{m}
\]

\[
s=10.0\,\mathrm{m}
\]

**Answer: the maximum height is \(+10.0\,\mathrm{m}\) above the release point.**

The positive displacement fits the situation because the stone finishes above where it started. The acceleration is negative because gravity is downward while upward was chosen as positive.

If the question asked for the time to reach the top instead, this equation would not be the shortest route. The equation \(v=u+at\) includes the required time.

**A falling object has constant acceleration. You know its initial velocity, final velocity, acceleration and displacement, but not its time. Which equation avoids introducing time?**

- **A:** \(v^2=u^2+2as\)
- **B:** \(s=ut+\frac{1}{2}at^2\)

**Feedback for A:** Correct. This equation contains exactly the known quantities and the required displacement. It works only for constant acceleration in one straight-line direction.

**Feedback for B:** Not correct for this information set. It contains the unknown time \(t\), so it would add another unknown rather than giving a direct route.

## When words are the shortest route

Some kinematics questions ask for no calculation at all. They test whether you can state the physical meaning accurately.

For example, if a question asks why a projectile has constant horizontal velocity when air resistance is negligible, begin with the force direction. Weight acts vertically. There is no horizontal force, so there is no horizontal acceleration. Therefore the horizontal component of velocity remains constant.

If a question asks whether displacement is less than, equal to, or greater than the distance along a curved path, use the definitions. The straight directed displacement between the start and finish is shorter than the curved distance travelled.

Words are also essential after a calculation. A number without a direction or a physical conclusion may be incomplete. Ask yourself: *What does this sign, area, gradient, or graph shape mean for the object?*

## A representation must agree with the motion

You can use more than one representation to check an answer. They must tell the same physical story.

Consider an object thrown upward, with upward chosen as positive:

- The words say that its velocity decreases to zero, then becomes negative as it falls.
- A velocity-time graph slopes downward with constant gradient \(-g\).
- The equation \(v=u+at\) uses \(a=-g\).

If one representation gives a positive acceleration while the other two describe gravity acting downward, revisit the chosen signs. The problem is usually a direction mismatch, not a mysterious new effect.

### Worked example 3: choose words before calculating

A water droplet leaves a horizontal pipe. Air resistance is negligible. Explain why its horizontal velocity stays constant. Then find the time to travel a horizontal distance of \(4.8\,\mathrm{m}\) if its horizontal velocity is \(8.0\,\mathrm{m\,s^{-1}}\).

**Decision for the explanation.** This is a words question. The only force is weight, and weight acts vertically. Therefore there is no horizontal force and no horizontal acceleration. The horizontal velocity stays constant.

**Decision for the time.** Horizontally, the velocity is constant. The related controlled formula is recorded in the formula registry as displacement in uniform motion:

### Displacement in uniform motion {#formula-uniform-motion-displacement}

> **Formula to learn: Displacement in uniform motion.** \(s = vt\)

Here \(s\) is displacement in metres, \(\mathrm{m}\), \(v\) is constant velocity in \(\mathrm{m\,s^{-1}}\), and \(t\) is time in seconds. For this horizontal motion, rearrange it to \(t=s/v\).

\[
t=\frac{s}{v}
\]

\[
t=\frac{4.8\,\mathrm{m}}{8.0\,\mathrm{m\,s^{-1}}}
\]

\[
t=0.60\,\mathrm{s}
\]

The unit check is:

\[
\frac{\mathrm{m}}{\mathrm{m\,s^{-1}}}=\mathrm{s}
\]

**Answer: the travel time is \(0.60\,\mathrm{s}\).** The equation gives the number, while the words explain why the horizontal velocity can be treated as constant.

## Common wrong starts

### Starting with every equation

It is tempting to write all three constant-acceleration equations immediately. This can hide the useful information instead of organising it. First list what is known and what is required. Then choose the equation that leaves no extra unknown when possible.

### Treating every graph area as distance

Area under a velocity-time graph gives **displacement**, not always distance. Areas below the time axis are negative displacement. If the object reverses direction and you need total distance, find the size of each section separately and add the positive distances.

### Forgetting what gradient belongs to

The graph axes decide the meaning of a gradient.

- displacement-time gradient gives velocity
- velocity-time gradient gives acceleration

Do not use a gradient rule before naming both axes.

## Core recap

Choose the representation that answers the question directly:

- **Words** for a definition, explanation, comparison, direction, or physical conclusion.
- **Graphs** for changing motion, gradient, signed area, sketching, or extracting a pattern.
- **Equations** for constant-acceleration quantities in one straight-line direction.

Remember the exact definitions:

- **displacement:** distance in a specified direction from a point
- **velocity:** rate of change of displacement
- **acceleration:** rate of change of velocity

Remember these graph links:

- velocity-time area gives displacement
- displacement-time gradient gives velocity
- velocity-time gradient gives acceleration

For equations, list known quantities, choose a positive direction, keep signs and units, then select a constant-acceleration equation that does not introduce an unnecessary unknown. The next lesson will use this choice process when kinematics appears alongside another topic.
