# The Principle of Moments

## The Lever of Archimedes

More than two thousand years ago in Syracuse, Archimedes studied the balance of levers. He noticed that a small effort could raise an enormous load. A long wooden beam resting across a single pivot multiplied human strength.

In his treatise *On the Equilibrium of Planes*, Archimedes proved a remarkable mathematical rule. Unequal weights balance when their distances from the pivot are inversely proportional to their weights. Later scholars recorded his famous claim: give me a place to stand, and I will move the Earth.

Yet everyday experience shows that balance is delicate. If the lighter weight shifts even slightly outward, the beam tilts. If the heavier weight shifts inward, the opposite side falls.

A lighter force can balance a much larger force simply by acting farther from the pivot. What exact physical condition prevents an object from beginning to rotate about any chosen point?

## The Turning Effect of a Single Force

Before balancing multiple forces, you must evaluate one force at a time. The turning effect of a force about a chosen reference point is called its moment. A larger force or a greater distance from the pivot produces a greater turning effect.

You calculate a moment using the force and its perpendicular distance from the chosen point. The perpendicular distance is the shortest line from that point to the line of action of the force. It meets the line of action at a right angle of ninety degrees.

You must not measure the distance along an angled or sloping bar. The perpendicular moment arm is always the right-angle distance.

$$M = F d_{\perp}$$

In this formula, $M$ is the moment of the force in newton metres ($\text{N m}$). The symbol $F$ represents the force in newtons ($\text{N}$). The term $d_{\perp}$ is the perpendicular distance in metres ($\text{m}$) from the pivot to the line of action.

The unit of moment is the newton metre ($\text{N m}$). Multiplying newtons by metres gives this compound unit. A moment describes a directional turning effect rather than a scalar energy quantity.

## Sorting Turning Effects by Direction

Every force acting on an object tends to rotate it in a particular sense about the chosen point. Imagine pinning the object at that chosen point so it can only rotate. Then observe which way the force tends to swing the body.

A force produces a clockwise moment if it tends to rotate the object in the direction of clock hands. It produces an anticlockwise moment if it tends to rotate the object in the opposite direction. The direction of the force arrow alone does not determine the turning sense.

A downward force to the right of a pivot turns a horizontal beam clockwise. The same downward force placed to the left of the pivot turns the beam anticlockwise. You must always check both the force direction and its position relative to your chosen point.

## The Principle of Moments and Rotational Balance

When opposing turning effects balance each other, an object does not start to rotate. Physicists call this state rotational equilibrium. In rotational equilibrium, the resultant turning effect about any chosen point is zero.

> **Principle of moments:**
>
> for a body in rotational equilibrium, the sum of clockwise moments about a point equals the sum of anticlockwise moments about the same point

Notice two vital requirements in this official statement. First, the body must be in rotational equilibrium. Second, every clockwise and anticlockwise moment must be evaluated about the very same point.

You cannot equate clockwise moments about one point to anticlockwise moments about a different point. That mistake would compare turning effects about two separate axes. Rotational balance always demands one common reference point.

In mathematical shorthand, we write this balance condition using the summation symbol sigma ($\Sigma$):

$$\Sigma M_{\text{clockwise}} = \Sigma M_{\text{anticlockwise}}$$

## Formulating and Solving Moment Balance Equations

To solve equilibrium problems, begin by identifying every force acting on the body. Select one convenient reference point. Then determine the perpendicular distance from that point to the line of action of each force.

Calculate the moment of each force in newton metres. Group all clockwise moments on one side of the equation. Place all anticlockwise moments on the opposite side.

If the body is a uniform beam, its own weight acts at its geometric center of gravity. You must include this weight at the midpoint unless the pivot sits directly at the center of gravity. If the pivot sits at the midpoint, the perpendicular distance to the beam weight is zero.

### Worked Example 1: Balancing Three Masses on a Central Fulcrum

A uniform horizontal beam of length $6.0\text{ m}$ rests on a pivot at its midpoint. Object A has mass $60\text{ kg}$ and rests at the left-hand end. Object B has mass $45\text{ kg}$ and rests at distance $x$ to the left of the pivot. Object C has mass $80\text{ kg}$ and rests at the right-hand end. The beam is in equilibrium. Calculate the distance $x$. Take $g = 9.81\text{ N kg}^{-1}$.

**Answer**
Take moments about the central pivot.

Clockwise moment from object C:
$$M_C = (80 \times 9.81)\text{ N} \times 3.0\text{ m} = 2354.4\text{ N m}$$

Anticlockwise moments from objects A and B:
$$M_A = (60 \times 9.81)\text{ N} \times 3.0\text{ m} = 1765.8\text{ N m}$$
$$M_B = (45 \times 9.81)\text{ N} \times x = 441.45x\text{ N m}$$

By the principle of moments:
$$\Sigma M_{\text{clockwise}} = \Sigma M_{\text{anticlockwise}}$$
$$2354.4 = 1765.8 + 441.45x$$
$$441.45x = 588.6$$
$$x = 1.3\text{ m}$$

**Explanation**
Step 1: The pivot is at the midpoint of the $6.0\text{ m}$ beam. Each outer end is therefore $3.0\text{ m}$ from the pivot.
Step 2: The weight of the uniform beam acts directly through the central pivot. Its perpendicular distance is zero, so its moment is zero.
Step 3: Object C pulls downwards to the right of the pivot, producing a clockwise turning effect. Objects A and B pull downwards to the left, producing anticlockwise turning effects.
Step 4: Equating moments allows $g$ to cancel from every term. This gives $80 \times 3.0 = (60 \times 3.0) + (45 \times x)$.
Step 5: Solving $240 = 180 + 45x$ gives $45x = 60$. This yields $x = 1.33\text{ m}$, which rounds to $1.3\text{ m}$ to two significant figures.

## Strategic Pivot Selection to Eliminate Unknown Forces

In many engineering systems, a beam is supported by a hinge, pin joint, or unmeasured contact point. That support exerts an unknown reaction force on the beam. If you choose an arbitrary reference point, that unknown force enters your moment equation.

You can remove an unwanted force from your equation by choosing a pivot on its line of action. When the line of action of a force passes through the chosen reference point, its perpendicular distance is zero. The moment produced by that force is therefore zero.

This method is called strategic pivot selection. The unknown reaction force still acts on the body in the physical world. However, because its moment is zero about that specific point, it drops completely out of your moment balance equation.

### Worked Example 2: Hinged Beam Supported by an Upward Force

A uniform horizontal beam AB of length $6.0\text{ m}$ and weight $1700\text{ N}$ is attached to a wall by a hinge at end A. A floating cylinder exerts an upward vertical force of $1300\text{ N}$ on the beam at a distance of $5.0\text{ m}$ from A. A person of weight $660\text{ N}$ stands on the beam at point P, at a distance $x$ from end A. The beam is in equilibrium. By taking moments about hinge A, determine the distance $x$.

**Answer**
Take moments about hinge A.

Anticlockwise moment from the upward cylinder force:
$$M_{\text{cylinder}} = 1300\text{ N} \times 5.0\text{ m} = 6500\text{ N m}$$

Clockwise moments come from the beam weight and the person.
Beam weight acts at the midpoint ($3.0\text{ m}$ from A):
$$M_{\text{beam}} = 1700\text{ N} \times 3.0\text{ m} = 5100\text{ N m}$$
Person weight acts at distance $x$ from A:
$$M_{\text{person}} = 660\text{ N} \times x = 660x\text{ N m}$$

By the principle of moments about hinge A:
$$\Sigma M_{\text{clockwise}} = \Sigma M_{\text{anticlockwise}}$$
$$5100 + 660x = 6500$$
$$660x = 1400$$
$$x = 2.1\text{ m}$$

**Explanation**
Step 1: Choose hinge A as the pivot point. The unknown reaction force at the hinge passes directly through A, so its perpendicular distance is zero and its moment is zero.
Step 2: The cylinder pushes upwards to the right of A. It produces an anticlockwise turning effect with a moment arm of $5.0\text{ m}$.
Step 3: The weight of the uniform beam acts at its center of gravity, which is at the midpoint $3.0\text{ m}$ from A. This downward force turns the beam clockwise.
Step 4: The person also exerts a downward force, adding a clockwise moment of $660x\text{ N m}$.
Step 5: Equating the total clockwise moment to the total anticlockwise moment leaves $x$ as the only unknown. Solving $5100 + 660x = 6500$ gives $x = 2.12\text{ m}$, which rounds to $2.1\text{ m}$ to two significant figures.

## Multi-Moment Structures and Direct Couple Integration

Engineering structures such as signboards, crane jibs, and brackets often involve multiple loads and external couples. The same systematic procedure applies to every coplanar system. You choose a pivot, determine perpendicular distances, and equate the total clockwise turning effect to the total anticlockwise turning effect.

If an external couple acts on the system, recall that its torque is independent of the reference point. The torque of a couple is already measured in newton metres ($\text{N m}$). You never multiply the torque of a couple by a distance to the pivot.

Instead, you add the couple torque directly to the appropriate directional sum. If a motor applies an anticlockwise torque, you simply add that value to the anticlockwise moment sum.

### Worked Example 3: Cable Tension on a Hinged Signboard

A uniform signboard of length $3.6\text{ m}$ and weight $420\text{ N}$ is attached to a vertical wall by a hinge at H. A floodlight of weight $180\text{ N}$ is mounted on the board at a distance of $3.0\text{ m}$ from the hinge. A vertical support cable attached to the outer tip, $3.6\text{ m}$ from H, exerts an upward tension $T$. Calculate the tension $T$ required to keep the board horizontal.

**Answer**
Take moments about hinge H.

Clockwise moments come from the signboard weight and floodlight.
Signboard weight acts at the midpoint ($1.8\text{ m}$ from H):
$$M_{\text{board}} = 420\text{ N} \times 1.8\text{ m} = 756\text{ N m}$$
Floodlight weight acts at $3.0\text{ m}$ from H:
$$M_{\text{light}} = 180\text{ N} \times 3.0\text{ m} = 540\text{ N m}$$
Total clockwise moment:
$$\Sigma M_{\text{clockwise}} = 756 + 540 = 1296\text{ N m}$$

Anticlockwise moment from the cable tension:
$$\Sigma M_{\text{anticlockwise}} = T \times 3.6\text{ m}$$

By the principle of moments about hinge H:
$$T \times 3.6 = 1296$$
$$T = \frac{1296}{3.6} = 360\text{ N}$$

**Explanation**
Step 1: Selecting hinge H as the pivot removes the unknown wall reaction force because its line of action passes through H.
Step 2: Both the signboard weight and the floodlight weight act vertically downwards to the right of H, producing clockwise moments.
Step 3: The vertical cable pulls upwards at the right-hand end, producing an anticlockwise moment about H with a moment arm of $3.6\text{ m}$.
Step 4: The sum of the clockwise moments is $756\text{ N m} + 540\text{ N m} = 1296\text{ N m}$.
Step 5: Dividing the total clockwise moment by $3.6\text{ m}$ gives $T = 360\text{ N}$. Notice that $360\text{ N}$ is less than the total downward weight of $600\text{ N}$. This happens because the cable acts farther from the pivot than either load.

## Reaction Forces and the Tipping Threshold

When an object rests across two separate supports, both supports exert upward reaction forces. If you take moments about one support, the reaction force at that support exerts zero moment. That choice allows you to determine the reaction force exerted by the second support.

As a load shifts across the beam, the distribution of force changes. The support closer to the moving load carries an increasing share of the total weight. Meanwhile, the upward force exerted by the farther support decreases.

At the critical threshold of tipping, the beam is on the verge of lifting off the far support. The contact reaction force at that far support drops to exactly zero. The beam then pivots entirely about the remaining contact point.

### Worked Example 4: Support Forces and Tipping on a Two-Pivot Beam

A uniform horizontal beam AD has length $9.0\text{ m}$ and weight $380\text{ N}$. Upward vertical forces $F_B$ and $F_C$ support the beam at pivots B and C. Pivot B is $2.0\text{ m}$ from end A, and pivot C is $2.0\text{ m}$ from end D. A person of weight $750\text{ N}$ stands $3.6\text{ m}$ from end D.
(a) By taking moments about pivot C, calculate the upward force $F_B$.
(b) The person walks towards end D. Determine the minimum distance $x$ from end D that the person can reach without tipping the beam.

**Answer**
Part (a):
Take moments about pivot C.
The distance between pivots B and C is $9.0 - 2.0 - 2.0 = 5.0\text{ m}$.

The upward force $F_B$ acts to the left of C and produces a clockwise moment:
$$M_{FB} = F_B \times 5.0\text{ m}$$

The center of gravity is $4.5\text{ m}$ from each end. This position is $4.5 - 2.0 = 2.5\text{ m}$ to the left of pivot C.
The downward beam weight produces an anticlockwise moment:
$$M_{\text{beam}} = 380\text{ N} \times 2.5\text{ m} = 950\text{ N m}$$

The person stands $3.6\text{ m}$ from end D, which is $3.6 - 2.0 = 1.6\text{ m}$ to the left of pivot C.
The downward person weight produces an anticlockwise moment:
$$M_{\text{person}} = 750\text{ N} \times 1.6\text{ m} = 1200\text{ N m}$$

By the principle of moments about pivot C:
$$\Sigma M_{\text{clockwise}} = \Sigma M_{\text{anticlockwise}}$$
$$F_B \times 5.0 = 950 + 1200 = 2150\text{ N m}$$
$$F_B = \frac{2150}{5.0} = 430\text{ N}$$

Part (b):
When the beam is about to tip about pivot C, contact at pivot B is lost, so $F_B = 0\text{ N}$.
The person is at distance $x$ from end D, which is $(2.0 - x)\text{ m}$ to the right of pivot C.

Take moments about pivot C.
Clockwise moment from the person about C:
$$M_{\text{person}} = 750\text{ N} \times (2.0 - x)$$
Anticlockwise moment from the beam weight about C:
$$M_{\text{beam}} = 380\text{ N} \times 2.5\text{ m} = 950\text{ N m}$$

Equating moments about pivot C:
$$750(2.0 - x) = 950$$
$$2.0 - x = \frac{950}{750} \approx 1.27\text{ m}$$
$$x = 2.0 - 1.27 = 0.73\text{ m}$$
The minimum distance from end D without tipping is $0.73\text{ m}$ (or $0.7\text{ m}$ to one decimal place).

**Explanation**
Step 1: In part (a), choosing pivot C eliminates the unknown upward reaction force $F_C$ because its line of action passes through C.
Step 2: Force $F_B$ acts $5.0\text{ m}$ to the left of C and pushes upwards, creating a clockwise turning effect about C.
Step 3: Both the beam weight and the person act to the left of C and pull downwards, creating anticlockwise turning effects about C.
Step 4: Solving $5.0 F_B = 950 + 1200$ gives $F_B = 430\text{ N}$. The support force $F_C$ does not need to be known to solve this step.
Step 5: In part (b), the person walks past pivot C towards end D. Their downward weight produces a clockwise turning effect about pivot C.
Step 6: That turning effect tilts the beam and lifts end A off pivot B. At the threshold of tipping, contact with pivot B is just lost, so $F_B$ drops to zero.
Step 7: Taking moments about pivot C with $F_B = 0$ leaves only the beam weight balancing the person. Solving $750(2.0 - x) = 950$ gives $x = 0.73\text{ m}$.

## Archimedes and the Balanced Lever

We can now answer the question posed by Archimedes. A lighter force can balance a much heavier force because rotational equilibrium does not depend on force magnitude alone. The essential condition is that the total clockwise turning effect equals the total anticlockwise turning effect about the same point.

When $F_1 d_1 = F_2 d_2$, the opposing moments cancel each other completely. The net turning effect about the fulcrum is zero, preventing any rotational acceleration. Archimedes succeeded because increasing the distance compensates exactly for a smaller force.

In this lesson, you have learned to calculate individual moments and classify their rotational directions. You have applied the principle of moments to find unknown loads and positions. You also saw how choosing a pivot strategically eliminates unwanted reaction forces.

Moment balance guarantees rotational equilibrium, but it does not tell the whole story. An object with balanced moments can still accelerate linearly if the resultant force is non-zero. In the next lesson, we will combine moment balance with force balance to establish the complete conditions for equilibrium.
