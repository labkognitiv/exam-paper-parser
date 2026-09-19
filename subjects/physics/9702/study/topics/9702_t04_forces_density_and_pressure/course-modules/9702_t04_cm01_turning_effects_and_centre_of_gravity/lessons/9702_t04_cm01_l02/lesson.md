# Couples and torque

## The puzzle of the turning wheel

Imagine turning a heavy steering wheel with two hands.
Your left hand pushes upward with a steady force.
At the exact same instant, your right hand pulls downward with the same force.
The two opposing pushes cancel each other out completely as a linear shove.

The wheel does not drift forward, backward, left, or right.
Yet the wheel rotates briskly in your hands.
Why does a pair of balanced pushes create pure turning motion?

In 1803, French mathematician Louis Poinsot examined this everyday action.
Before his work, thinkers tried to simplify every combination of pushes into a single equivalent push.
When two equal pushes acted in opposite directions along different lines, their combined push was zero.
A single push of zero cannot make anything move.

Yet the solid wheel clearly began spinning.
Poinsot saw that this rotational action was unique.
It could never be replaced by any single push.

He also uncovered a remarkable property of this turning pair.
If you slide the two pushes anywhere along the wheel, the turning strength never changes.
Moving a single push changes its turning effect immediately.
Why does shifting two opposing pushes across a body leave its turning effect unchanged, while moving a single push alters how it turns?

## Forces as vectors and resultant forces

A force is a vector quantity having both magnitude and direction.
When multiple forces act on an object, we combine them into a single resultant force.
The resultant force represents the overall linear push on the object.

If two equal forces act in opposite directions along the exact same line, they cancel out completely.
Their vector sum is zero, so the object experiences zero resultant force.
An object with zero resultant force experiences no linear acceleration.

## The moment of a single force

In our previous study, we learned that a single force can also produce a turning effect.
We measure this turning effect using the moment of a force.
The moment of a force is the product of the force and the perpendicular distance from the pivot to the line of action.

Notice that the moment of a single force always depends on a specific chosen pivot.
If you move the pivot, the perpendicular distance changes.
If you move the force farther from the pivot, the moment increases.
A single force has no fixed turning effect on its own without naming a reference point.

## What is a couple?

Some turning effects do not depend on a single force.
When you turn a doorknob, twist a bottle cap, or steer a bicycle, you use two hands together.
Each hand applies a force, and together these forces form a couple.

In physics, a couple is a pair of forces that acts to produce rotation only.
To form a true couple, two forces must satisfy four strict conditions at the same time.

First, the two forces must have equal magnitude.
Second, the two forces must point in opposite directions.
Third, the forces must act along parallel lines of action.
Fourth, the forces must act along separate lines of action.

All four conditions are essential.
If the magnitudes are unequal, an unbalanced push remains, causing linear acceleration.
If the directions are not opposite, the forces push the body sideways together.
If the lines are not parallel, they cross each other at an angle.

Finally, the lines of action must not lie along the same line.
If two equal opposite forces act along the same line, their perpendicular separation is zero.
They pull or squeeze the object along that line, producing zero turning effect.

Be careful not to confuse a couple with a Newton's third law pair.
A Newton's third law pair consists of two equal and opposite forces that act on two different bodies.
A couple always consists of two forces acting on the same single rigid body.

## Zero resultant force does not mean equilibrium

Let us examine the total force exerted by a couple.
One force has magnitude $F$ in one direction.
The other force has the same magnitude $F$ in the exact opposite direction.
Their vector sum is $F + (-F) = 0\text{ N}$.

Because the resultant force is zero, a couple cannot cause translational acceleration.
The centre of mass of the object does not change its linear velocity.
This fact leads to a widespread misconception among physics students.
Many students assume that zero resultant force means an object is in complete mechanical equilibrium.

A couple disproves this assumption immediately.
Although the linear pushes cancel, the forces act along separate lines.
As a result, both forces turn the object in the exact same rotational sense.
If one force pushes up on the left edge and the other pushes down on the right edge, both forces turn the object clockwise.

The turning effects of the two forces do not cancel.
Instead, their turning effects reinforce each other.
The object experiences an unbalanced rotational effect and undergoes angular acceleration.
Therefore, zero resultant force alone does not guarantee mechanical equilibrium.

## The torque of a couple

To measure how strongly a couple turns an object, we calculate its torque.
We distinguish the turning effect of a couple from the moment of a single force by using the word torque.

> **Torque of a couple**
> the product of one of the forces and the perpendicular distance between the lines of action of the forces

We express this definition mathematically as a concise equation.
The formula relates the turning strength directly to the force and separation:

$$\text{torque} = F \times d$$

Here, $F$ is the magnitude of one of the forces, measured in newtons ($\text{N}$).
The symbol $d$ is the perpendicular distance between the lines of action of the forces, measured in metres ($\text{m}$).

The SI unit of torque is the newton metre ($\text{N m}$).
Because torque causes rotation, you should always state its rotational sense.
State whether the torque acts clockwise or anticlockwise.

Students often make two common calculation errors when finding torque.
The first error is substituting both forces into the formula as $2F$.
The definition states clearly that you must use one of the forces, not both added together.

The second error is halving the separation distance.
The distance $d$ is already the full perpendicular gap between the two force lines.
You do not divide this distance by two when applying the torque formula.

We can prove why the formula uses one force and the full separation.
Consider a rod of length $d$ pivoted at its central midpoint.
Each force acts at a perpendicular distance of $d/2$ from the central pivot.
The moment of the first force is $F \times (d/2)$ clockwise.

The moment of the second force is also $F \times (d/2)$ clockwise.
Adding the two clockwise moments gives:

$$\text{total moment} = F \times \frac{d}{2} + F \times \frac{d}{2} = F \times d$$

The single expression $F \times d$ already accounts for the turning contribution of both forces.
By using the full separation $d$ rather than the distance to the centre, the formula combines both turning effects into one step.

## Finding the perpendicular separation across different geometries

The most critical step in calculating torque is identifying the correct perpendicular distance $d$.
The perpendicular distance is always the shortest distance between the two parallel lines of action.
It is not always the direct distance between the two points where the forces are applied.

Consider two tangential forces applied to opposite edges of a circular wheel or disc.
Each force line is tangent to the circle, meaning it touches the rim at right angles to the radius.
The perpendicular distance between these two tangent lines is the diameter of the wheel, $2r$.
Do not use the radius $r$; the separation across the two force lines is the full diameter.

Now consider two parallel forces applied at opposite corners of an angled plate.
A straight line connecting the two corners runs diagonally across the plate.
This diagonal line is oblique to the direction of the forces.
You must find the line that meets both lines of action at a right angle.

On a right-angled triangular plate, this perpendicular gap often corresponds to one side length, rather than the hypotenuse.
Always draw or extend the parallel lines of action on your sketch.
Then identify the side or segment that forms a 90-degree angle between them.

Finally, consider forces applied at interior points along a beam.
A problem might state the total length of the beam as extra information.
Ignore the total length of the beam.
Measure only the distance between the two points where the parallel force lines cross the beam.

## Pivot independence and translation invariance

When working with a single force, the moment changes whenever you choose a different pivot point.
A couple behaves very differently.
The torque of a couple has the exact same value about every point in space.

We can prove this remarkable property with algebra.
Let two equal and opposite vertical forces $F$ be separated by a horizontal distance $d$.
Choose any reference point $P$ along the horizontal line.

First, suppose point $P$ lies between the two forces, at distance $x$ from the left-hand force.
The distance from $P$ to the right-hand force is $d - x$.
Both forces produce clockwise moments about $P$.
The total moment is $F \times x + F \times (d - x) = F \times d$.

Next, suppose point $P$ lies outside the two forces, at distance $x$ to the left of the first force.
The distance to the second force is $x + d$.
The first force produces an anticlockwise moment, while the second produces a clockwise moment.
The total moment is $F \times (x + d) - F \times x = F \times d$.

In both cases, the variable distance $x$ cancels out completely.
The net turning effect is always $F \times d$, regardless of where you place the reference point.
Because the torque does not depend on any pivot, torque is an intrinsic property of the couple itself.

This leads to another key principle: translational invariance.
You can slide a couple to any position on a rigid body without altering its turning effect.
As long as the force magnitudes, directions, and perpendicular separation stay the same, the torque remains unchanged.
The body experiences the exact same angular acceleration regardless of where the couple is mounted.

## Scope and boundaries

In this lesson, we focused strictly on defining couples and calculating their torque.
We deliberately do not apply the principle of moments here.
The principle of moments balances clockwise and anticlockwise turning effects in rotational equilibrium and belongs to the next lesson.

We also do not analyze complete equilibrium conditions combining zero force and zero resultant torque.
That complete analysis is explored later in this course module.
Similarly, closed vector triangles for three coplanar forces are reserved for a subsequent lesson.

## Worked examples

### Worked Example 1: A steering wheel with tangential forces

A steering wheel of radius $0.22\text{ m}$ is turned by applying two tangential forces of magnitude $15\text{ N}$ at opposite ends of a vertical diameter. The left force points vertically upwards. The right force points vertically downwards. Calculate the torque produced by this couple.

**Answer**
$\text{torque} = 6.6\text{ N m}$ clockwise

**Explanation**
Identify the two forces and verify that they form a valid couple.
Both forces have equal magnitude ($15\text{ N}$) and point in opposite vertical directions.
The forces act along parallel vertical lines separated across the wheel.

Because the forces act tangentially at opposite ends of a diameter, the perpendicular separation is the diameter of the wheel.
We determine this distance by doubling the radius:

$$d = 2 \times r = 2 \times 0.22\text{ m} = 0.44\text{ m}$$

Next, apply the formula for the torque of a couple.
Multiply the magnitude of one force by this perpendicular separation:

$$\text{torque} = F \times d = 15\text{ N} \times 0.44\text{ m} = 6.6\text{ N m}$$

Both the upward left force and downward right force turn the wheel clockwise.
Therefore, the torque is $6.6\text{ N m}$ clockwise.

### Worked Example 2: Parallel forces on a triangular plate

Two parallel forces of magnitude $24\text{ N}$ act in opposite directions at two corners of a right-angled triangular plate.
The direct diagonal distance between the two corners is $0.50\text{ m}$.
The perpendicular distance between the lines of action of the forces is $0.35\text{ m}$.

Both forces act to rotate the plate anticlockwise.
Calculate the torque exerted on the plate.

**Answer**
$\text{torque} = 8.4\text{ N m}$ anticlockwise

**Explanation**
Identify the perpendicular distance between the lines of action.
The diagonal distance of $0.50\text{ m}$ connects the two points of application, but it is not perpendicular to the force lines.
The formula for torque requires the perpendicular separation $d$ between the lines of action.

The perpendicular distance is given as $0.35\text{ m}$.
Use one force and the perpendicular separation in the torque equation:

$$\text{torque} = F \times d = 24\text{ N} \times 0.35\text{ m} = 8.4\text{ N m}$$

State the rotational sense given in the problem as anticlockwise.
The torque of the couple is $8.4\text{ N m}$ anticlockwise.

### Worked Example 3: Finding force from torque

A technician turns a stiff radiator valve by applying a couple. The valve requires a torque of $7.2\text{ N m}$ to begin turning. The technician grips the valve handle so that the parallel lines of action are separated by a perpendicular distance of $0.18\text{ m}$. Calculate the magnitude of each force applied by the technician.

**Answer**
$\text{force} = 40\text{ N}$

**Explanation**
State the standard equation for the torque of a couple.
Relate the torque directly to force magnitude and separation:

$$\text{torque} = F \times d$$

We need to solve for the magnitude of one force.
Rearrange the equation to make $F$ the subject:

$$F = \frac{\text{torque}}{d}$$

Substitute the given values of torque and perpendicular separation into the rearranged equation.
Perform the division to find the magnitude of the force:

$$F = \frac{7.2\text{ N m}}{0.18\text{ m}} = 40\text{ N}$$

The magnitude of each force is $40\text{ N}$.
Remember that $F$ represents the magnitude of one force, so do not divide this answer by two.

### Worked Example 4: A beam subjected to a single force and a couple

A uniform horizontal bar is pivoted at a fixed support at point O. A downward vertical force of $12\text{ N}$ acts at a distance of $0.30\text{ m}$ to the right of O, tending to turn the bar clockwise. Simultaneously, an independent couple with forces of $8.0\text{ N}$ separated by a perpendicular distance of $0.25\text{ m}$ acts on the bar in an anticlockwise sense. Calculate the resultant turning effect about pivot O.

**Answer**
$\text{resultant moment} = 1.6\text{ N m}$ clockwise

**Explanation**
First, consider the turning effect of the single downward force.
Calculate the moment of this force about pivot O:

$$\text{moment} = F_1 \times d_1 = 12\text{ N} \times 0.30\text{ m} = 3.6\text{ N m}\text{ clockwise}$$

Next, consider the independent couple acting on the bar.
Calculate the torque produced by this couple:

$$\text{torque} = F_2 \times d_2 = 8.0\text{ N} \times 0.25\text{ m} = 2.0\text{ N m}\text{ anticlockwise}$$

Because the torque of a couple is independent of the pivot location, it contributes an anticlockwise turning effect of $2.0\text{ N m}$ about point O.
Combine the two opposing turning effects by subtracting the smaller turning effect from the larger:

$$\text{resultant turning effect} = 3.6\text{ N m} - 2.0\text{ N m} = 1.6\text{ N m}\text{ clockwise}$$

The net turning effect on the bar is $1.6\text{ N m}$ clockwise.
Because the clockwise moment exceeds the anticlockwise torque, the bar tends to rotate clockwise overall.

## Louis Poinsot and the irreducible pair

We can now return to the historical puzzle investigated by Louis Poinsot in 1803.
We asked why shifting two opposing pushes across a body leaves its turning effect unchanged, while moving a single push alters how it turns.

The answer lies in how reference points affect turning effects.
The moment of a single force depends directly on the distance from a specific pivot to that force's line of action.
Moving a single force alters that distance, changing its moment immediately.

In contrast, a couple consists of two equal and opposite forces along separate parallel lines.
When you calculate the combined turning effect about any reference point, the position of the point cancels out algebraically.
The torque depends solely on the magnitude of one force and the fixed perpendicular gap between their lines of action.

Because this perpendicular separation is fixed across a rigid body, the couple exerts the exact same torque everywhere.
Poinsot proved that a couple is an irreducible mechanical entity.
It produces pure rotation with zero translational force, a distinct physical effect that no single force can ever duplicate.

## Summary and next steps

In this lesson, we established the foundations of couples and torque.
A couple consists of two forces with equal magnitude, opposite direction, parallel lines of action, and separate lines of action.
A couple produces zero resultant force but a non-zero turning effect.

The torque of a couple is the product of one of the forces and the perpendicular distance between their lines of action.
Torque is measured in newton metres ($\text{N m}$) and possesses a rotational direction.
The torque of a couple is independent of any pivot point and invariant under translation across a rigid body.

In our next lesson, we will explore bodies that do not rotate.
We will state and apply the principle of moments to analyze balanced systems in rotational equilibrium.
