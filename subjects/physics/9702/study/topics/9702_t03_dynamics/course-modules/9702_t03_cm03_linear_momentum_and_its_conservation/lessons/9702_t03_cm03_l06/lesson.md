# The principle of conservation of momentum

## What happens when moving objects interact?

Imagine two identical curling stones sliding across smooth, level ice towards each other. When they collide head-on with equal speeds, they rebound backwards with those exact same speeds. 

Now imagine a heavy freight locomotive gently bumping into a stationary, uncoupled flat wagon. After the locking mechanism catches, the locomotive does not stop. Instead, both vehicles continue rolling forward together, but at a visibly lower speed than the locomotive had initially.

Finally, think of an ice skater standing motionless in the centre of a frozen pond. The skater throws a heavy medicine ball forward. The ball shoots across the ice in one direction, while the skater immediately recoils and glides backwards across the ice in the opposite direction.

In all three situations, velocities change dramatically during the interaction. Forces push and pull across the contact surfaces. Yet beneath these visible changes, one quantity remains unchanged: the total linear momentum of the interacting objects.

Linear momentum is conserved. In this lesson, you will discover what an isolated system means, derive the principle of conservation of momentum directly from Newton's fundamental laws of motion, and use it to solve problems involving collisions, coalescing bodies, recoil explosions, and vector interactions in two dimensions.

## The concept of an isolated system

Before stating the principle, we must establish the precise condition under which it is true: the system must be **isolated** (also called a **closed system**).

In physics, a **system** is the specific collection of objects or particles chosen for study. Everything else in the universe is the **surroundings**.

Forces acting in a problem fall into two distinct classes:
1. **Internal forces:** Forces that the objects within the chosen system exert directly on one another. During a collision between trolley 1 and trolley 2, the push that trolley 1 exerts on trolley 2 and the push that trolley 2 exerts back on trolley 1 are internal forces.
2. **External forces:** Forces exerted on the objects of the system by agents in the surroundings. Examples include gravitational attraction from the Earth, friction from a rough floor, and air drag from the atmosphere.

An **isolated system** is a system upon which **no resultant external force** acts:

\[
\Sigma F_{\mathrm{external}} = 0
\]

If two billiard balls collide on a smooth, horizontal table:
- Vertically, the downward weight of each ball is balanced by the upward normal contact force from the table. The resultant vertical external force is zero.
- Horizontally, friction and air resistance are negligible during the brief collision contact time. The resultant horizontal external force is zero.

Because the resultant external force on the pair of balls is zero, the two colliding balls form an isolated system. 

If external forces do act, such as friction between a skidding car and a rough asphalt road, momentum transfers from the car to the Earth. The car alone is not an isolated system. However, if the entire Earth and the car are included together in an expanded system, the total momentum of that combined system is still conserved.

## Derivation of conservation of momentum from Newton's laws

The principle of conservation of momentum is not an arbitrary rule. It is a direct mathematical consequence of Newton's second and third laws of motion.

Consider two bodies, body 1 and body 2, that collide along a straight line in an isolated system.

```
Before collision:
  [ Body 1 (m1) ] --> u1        [ Body 2 (m2) ] --> u2

During collision:
  [ Body 1 ] <-- F21              F12 --> [ Body 2 ]
                   (contact time Delta t)

After collision:
  [ Body 1 (m1) ] --> v1        [ Body 2 (m2) ] --> v2
```

### Step 1: Apply Newton's third law

During the impact, body 1 exerts a contact force on body 2, which we call \(F_{12}\). 

By Newton's third law of motion, body 2 simultaneously exerts an equal and opposite contact force on body 1, which we call \(F_{21}\):

\[
F_{21} = -F_{12}
\]

The two forces act in opposite directions, so one carries a positive sign and the other carries a negative sign.

### Step 2: Consider the contact time

Body 1 and body 2 touch each other for the exact same duration of time, \(\Delta t\). One body cannot remain in contact for longer than the other.

Multiplying both sides of Newton's third law by the contact time \(\Delta t\) gives:

\[
F_{21}\Delta t = -F_{12}\Delta t
\]

### Step 3: Apply Newton's second law

Recall Newton's second law: resultant force equals the rate of change of momentum:

\[
F = \frac{\Delta p}{\Delta t} \implies \Delta p = F \Delta t
\]

The quantity \(F \Delta t\) is the impulse, which equals the change in momentum of the body:
- The change in momentum of body 1 is \(\Delta p_1 = F_{21}\Delta t\).
- The change in momentum of body 2 is \(\Delta p_2 = F_{12}\Delta t\).

Substituting these into the impulse equality from Step 2 yields:

\[
\Delta p_1 = -\Delta p_2
\]

Rearranging gives:

\[
\Delta p_1 + \Delta p_2 = 0
\]

This remarkable equation reveals that the total change in momentum of the system during the collision is exactly zero. Whatever momentum body 1 loses, body 2 gains in equal measure!

### Step 4: Express in terms of initial and final velocities

Write each change in momentum explicitly as final momentum minus initial momentum:
- \(\Delta p_1 = m_1 v_1 - m_1 u_1\)
- \(\Delta p_2 = m_2 v_2 - m_2 u_2\)

Substitute these into \(\Delta p_1 + \Delta p_2 = 0\):

\[
(m_1 v_1 - m_1 u_1) + (m_2 v_2 - m_2 u_2) = 0
\]

Grouping initial terms on one side and final terms on the other side yields:

\[
m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2
\]

The sum of the initial momenta equals the sum of the final momenta.

## The formal principle of conservation of momentum

In Cambridge International AS Level Physics, you must learn the approved wording for this principle:

<a id="definition-9702_def_conservation_of_momentum"></a>

> **Definition to learn: principle of conservation of momentum.** the total momentum of an isolated system remains constant

Every word in this definition is essential for exam success:
- **Total momentum:** You must sum the linear momenta of all individual bodies in the system.
- **Isolated system:** The condition under which the principle holds; there must be no resultant external force.
- **Remains constant:** The numerical value and direction of the total vector momentum before the interaction equal the total vector momentum after the interaction.

An accepted equivalent statement often used in Cambridge mark schemes is:
> *The total momentum before an interaction equals the total momentum after an interaction, provided there is no resultant external force acting on the system.*

## One-dimensional collisions and sign conventions

Linear momentum is a vector quantity:

\[
p = mv
\]

Because momentum depends directly on velocity, direction matters. When solving problems in one dimension (motion along a straight line):

1. **Choose a positive direction:** Always establish which direction is positive before writing down any equation. Usually, rightward motion or forward motion is defined as positive (\(+\)).
2. **Assign signs to every velocity:**
   - A body moving to the right with speed \(u\) has velocity \(+u\).
   - A body moving to the left with speed \(u\) has velocity \(-u\).
3. **Write the conservation equation:**
   \[
   \Sigma p_{\mathrm{initial}} = \Sigma p_{\mathrm{final}}
   \]
   \[
   m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2
   \]
4. **Substitute signed values:** Enter negative signs for any velocity directed in the negative direction.
5. **Interpret the result:** A positive calculated velocity means the body moves in the chosen positive direction; a negative calculated velocity means it moves in the opposite direction.

### Coalescing collisions (sticking together)

When two interacting bodies lock or stick together upon impact, they share a single common velocity, \(V\), after the collision. The conservation equation simplifies to:

\[
m_1 u_1 + m_2 u_2 = (m_1 + m_2)V
\]

Rearranging for the final velocity gives:

\[
V = \frac{m_1 u_1 + m_2 u_2}{m_1 + m_2}
\]

Such collisions are called **completely inelastic collisions**. Total momentum is conserved, but as you will see in Lesson 7, a significant portion of the initial kinetic energy is converted into thermal energy, sound, and permanent deformation.

## Explosions and recoil

An **explosion** in physics describes any interaction where stationary or moving bodies push apart from one another due to internal forces (such as a compressed spring or ignited propellant).

Consider a rifle of mass \(M\) containing a bullet of mass \(m\). Before the trigger is pulled, both rifle and bullet are at rest:

\[
p_{\mathrm{initial}} = 0
\]

When the bullet is fired, the expanding gases exert equal and opposite internal forces on the bullet and the rifle barrel. Because the rifle and bullet form an isolated system horizontally:

\[
p_{\mathrm{final}} = p_{\mathrm{initial}} = 0
\]

\[
M v_{\mathrm{rifle}} + m v_{\mathrm{bullet}} = 0
\]

Rearranging gives:

\[
M v_{\mathrm{rifle}} = -m v_{\mathrm{bullet}}
\]

\[
v_{\mathrm{rifle}} = -\left(\frac{m}{M}\right) v_{\mathrm{bullet}}
\]

This result explains key physical observations:
- **Opposite directions:** The minus sign shows that the rifle moves in the opposite direction to the bullet. This is known as **recoil**.
- **Different speeds:** Because the rifle is much more massive than the bullet (\(M \gg m\)), the ratio \(\frac{m}{M}\) is very small. The recoil speed of the rifle is small, whereas the light bullet emerges with an enormous forward speed.
- **Equal momentum magnitudes:** Although their speeds are very different, the magnitude of the backward momentum of the rifle is identical to the magnitude of the forward momentum of the bullet:
  \[
  |p_{\mathrm{rifle}}| = |p_{\mathrm{bullet}}|
  \]

The same principle governs rocket propulsion: a rocket accelerates forward by ejecting exhaust gases at high speed backwards. The forward momentum gained by the rocket body equals the backward momentum carried away by the ejected propellant.

## Conservation of momentum in two dimensions

In many practical situations, collisions do not occur along a single straight line. For example, two billiard balls may strike each other at a glancing angle and scatter in different directions across a table.

Because momentum is a vector, the principle applies in two dimensions:

\[
\vec{p}_{\mathrm{total, initial}} = \vec{p}_{\mathrm{total, final}}
\]

This single vector equation can be handled using two powerful, equivalent methods:

### Method 1: Component resolution

Choose two mutually perpendicular axes, typically an x-axis and a y-axis. Momentum is conserved independently along each axis:

1. **Along the x-axis:**
   \[
   \Sigma p_{x, \mathrm{initial}} = \Sigma p_{x, \mathrm{final}}
   \]
2. **Along the y-axis:**
   \[
   \Sigma p_{y, \mathrm{initial}} = \Sigma p_{y, \mathrm{final}}
   \]

If an incoming particle of mass \(m\) moves along the x-axis with speed \(u\) and strikes a stationary target of mass \(M\), the initial momenta are:
- \(p_{x, \mathrm{initial}} = mu\)
- \(p_{y, \mathrm{initial}} = 0\)

After the collision, if mass \(m\) scatters at angle \(\alpha\) above the x-axis with speed \(v_1\), and mass \(M\) scatters at angle \(\beta\) below the x-axis with speed \(v_2\):
- Conservation of x-momentum gives:
  \[
  mu = m v_1 \cos\alpha + M v_2 \cos\beta
  \]
- Conservation of y-momentum gives:
  \[
  0 = m v_1 \sin\alpha - M v_2 \sin\beta \implies m v_1 \sin\alpha = M v_2 \sin\beta
  \]

The vertical components of momentum must be equal and opposite so that they cancel out to give zero, matching the initial state!

### Method 2: Closed vector triangle

Alternatively, place the momentum vectors head-to-tail:

- For a two-body collision where a moving particle strikes a stationary particle and both scatter, the vector sum of the two final momenta must equal the initial momentum vector:
  \[
  \vec{p}_1 + \vec{p}_2 = \vec{p}_{\mathrm{initial}}
  \]
  Drawing \(\vec{p}_1\) and \(\vec{p}_2\) head-to-tail produces a resultant vector running from the tail of \(\vec{p}_1\) to the tip of \(\vec{p}_2\). This resultant matches \(\vec{p}_{\mathrm{initial}}\) in length and direction.

- For an explosion from rest where a stationary object breaks into three fragments:
  \[
  \vec{p}_1 + \vec{p}_2 + \vec{p}_3 = 0
  \]
  Because the vector sum is zero, drawing the three momentum vectors head-to-tail forms a **closed triangle**. The tip of the third vector returns exactly to the starting point of the first vector. You can apply the sine rule or cosine rule to this triangle to determine unknown angles or momentum magnitudes.

---

### Worked example 1: Head-on collision with rebound

Two laboratory trolleys, trolley A of mass \(0.50\,\mathrm{kg}\) and trolley B of mass \(0.80\,\mathrm{kg}\), move towards each other on a smooth, horizontal air track. 

Trolley A moves to the right at \(2.4\,\mathrm{m\,s^{-1}}\). Trolley B moves to the left at \(1.0\,\mathrm{m\,s^{-1}}\).

The trolleys collide. After the collision, trolley A rebounds to the left with a speed of \(0.80\,\mathrm{m\,s^{-1}}\).

Calculate:
1. The total initial momentum of the system.
2. The velocity of trolley B after the collision.
3. The change in momentum of trolley A.

```
Before collision:
  [ Trolley A (0.50 kg) ] --> +2.4 m s^-1       <-- -1.0 m s^-1 [ Trolley B (0.80 kg) ]

After collision:
  [ Trolley A (0.50 kg) ] <-- -0.80 m s^-1                       v_B [ Trolley B (0.80 kg) ]
```

#### Strategy
- Define the direction to the right as positive (\(+\)).
- Carefully assign signs to all velocities before calculating.
- Apply the principle of conservation of momentum: \(\Sigma p_{\mathrm{initial}} = \Sigma p_{\mathrm{final}}\).

#### Step 1: Total initial momentum
Identify initial velocities:
- \(u_A = +2.4\,\mathrm{m\,s^{-1}}\)
- \(u_B = -1.0\,\mathrm{m\,s^{-1}}\) (negative because it travels to the left)

Calculate initial momenta:
- \(p_A = m_A u_A = 0.50\,\mathrm{kg} \times (+2.4\,\mathrm{m\,s^{-1}}) = +1.20\,\mathrm{kg\,m\,s^{-1}}\)
- \(p_B = m_B u_B = 0.80\,\mathrm{kg} \times (-1.0\,\mathrm{m\,s^{-1}}) = -0.80\,\mathrm{kg\,m\,s^{-1}}\)

Total initial momentum:
\[
\Sigma p_{\mathrm{initial}} = (+1.20\,\mathrm{kg\,m\,s^{-1}}) + (-0.80\,\mathrm{kg\,m\,s^{-1}}) = +0.40\,\mathrm{kg\,m\,s^{-1}}
\]

The total initial momentum is \(0.40\,\mathrm{kg\,m\,s^{-1}}\) to the right.

#### Step 2: Velocity of trolley B after collision
After the collision, trolley A rebounds to the left, so:
- \(v_A = -0.80\,\mathrm{m\,s^{-1}}\)

Final momentum of trolley A:
\[
p_{A, \mathrm{final}} = m_A v_A = 0.50\,\mathrm{kg} \times (-0.80\,\mathrm{m\,s^{-1}}) = -0.40\,\mathrm{kg\,m\,s^{-1}}
\]

By conservation of momentum:
\[
\Sigma p_{\mathrm{final}} = \Sigma p_{\mathrm{initial}}
\]
\[
m_A v_A + m_B v_B = +0.40\,\mathrm{kg\,m\,s^{-1}}
\]
\[
-0.40\,\mathrm{kg\,m\,s^{-1}} + 0.80\,\mathrm{kg} \times v_B = +0.40\,\mathrm{kg\,m\,s^{-1}}
\]

Add \(0.40\,\mathrm{kg\,m\,s^{-1}}\) to both sides:
\[
0.80 \times v_B = 0.40 + 0.40 = 0.80\,\mathrm{kg\,m\,s^{-1}}
\]
\[
v_B = \frac{0.80\,\mathrm{kg\,m\,s^{-1}}}{0.80\,\mathrm{kg}} = +1.0\,\mathrm{m\,s^{-1}}
\]

The calculated velocity is positive, meaning trolley B moves at \(1.0\,\mathrm{m\,s^{-1}}\) to the right after the collision.

#### Step 3: Change in momentum of trolley A
Change in momentum is defined as final momentum minus initial momentum:
\[
\Delta p_A = p_{A, \mathrm{final}} - p_{A, \mathrm{initial}}
\]
\[
\Delta p_A = (-0.40\,\mathrm{kg\,m\,s^{-1}}) - (+1.20\,\mathrm{kg\,m\,s^{-1}}) = -1.60\,\mathrm{kg\,m\,s^{-1}}
\]

The change in momentum of trolley A is \(1.6\,\mathrm{kg\,m\,s^{-1}}\) directed to the left.

As a quick check, calculate the change in momentum of trolley B:
\[
\Delta p_B = m_B v_B - m_B u_B = 0.80 \times (+1.0) - 0.80 \times (-1.0) = +0.80 - (-0.80) = +1.60\,\mathrm{kg\,m\,s^{-1}}
\]
Notice that \(\Delta p_A + \Delta p_B = (-1.60) + (+1.60) = 0\), perfectly confirming Newton's third law!

**Answer:**
1. Total initial momentum is **\(0.40\,\mathrm{kg\,m\,s^{-1}}\) to the right**.
2. Velocity of trolley B is **\(1.0\,\mathrm{m\,s^{-1}}\) to the right**.
3. Change in momentum of trolley A is **\(1.6\,\mathrm{kg\,m\,s^{-1}}\) to the left** (\(-1.6\,\mathrm{kg\,m\,s^{-1}}\)).

---

### Worked example 2: Coalescing carts on a track

A glider cart 1 of mass \(0.45\,\mathrm{kg}\) moves with a velocity of \(1.6\,\mathrm{m\,s^{-1}}\) to the right along a frictionless track. It collides with a stationary glider cart 2 of mass \(0.75\,\mathrm{kg}\). 

The carts are equipped with Velcro strips so that they lock together on impact and move as a single combined unit.

Calculate:
1. The common velocity \(V\) of the two carts after the collision.
2. The change in momentum of cart 1.
3. If the collision lasts for \(0.060\,\mathrm{s}\), the average contact force exerted by cart 2 on cart 1.

#### Step 1: Common velocity after collision
Take the direction to the right as positive.
- \(m_1 = 0.45\,\mathrm{kg}\), \(u_1 = +1.6\,\mathrm{m\,s^{-1}}\)
- \(m_2 = 0.75\,\mathrm{kg}\), \(u_2 = 0\,\mathrm{m\,s^{-1}}\)

Total initial momentum:
\[
\Sigma p_{\mathrm{initial}} = m_1 u_1 + m_2 u_2 = (0.45 \times 1.6) + (0.75 \times 0) = 0.72\,\mathrm{kg\,m\,s^{-1}}
\]

After colliding, the two carts move together with mass \((m_1 + m_2)\) at velocity \(V\):
\[
\Sigma p_{\mathrm{final}} = (m_1 + m_2)V = (0.45 + 0.75)V = 1.20 V
\]

Apply conservation of momentum:
\[
1.20 V = 0.72
\]
\[
V = \frac{0.72}{1.20} = +0.60\,\mathrm{m\,s^{-1}}
\]

The carts move together to the right at \(0.60\,\mathrm{m\,s^{-1}}\).

#### Step 2: Change in momentum of cart 1
\[
\Delta p_1 = m_1 V - m_1 u_1 = 0.45\,\mathrm{kg} \times (0.60 - 1.6)\,\mathrm{m\,s^{-1}} = 0.45 \times (-1.00) = -0.45\,\mathrm{kg\,m\,s^{-1}}
\]

Cart 1 loses \(0.45\,\mathrm{kg\,m\,s^{-1}}\) of momentum (directed to the left).

#### Step 3: Average contact force on cart 1
By Newton's second law:
\[
F = \frac{\Delta p_1}{\Delta t} = \frac{-0.45\,\mathrm{kg\,m\,s^{-1}}}{0.060\,\mathrm{s}} = -7.5\,\mathrm{N}
\]

The negative sign indicates that the contact force acts to the left, opposing the forward motion of cart 1. By Newton's third law, cart 1 exerts an equal force of \(+7.5\,\mathrm{N}\) to the right on cart 2.

**Answer:**
1. Common velocity is **\(0.60\,\mathrm{m\,s^{-1}}\) to the right**.
2. Change in momentum of cart 1 is **\(-0.45\,\mathrm{kg\,m\,s^{-1}}\)** (\(0.45\,\mathrm{kg\,m\,s^{-1}}\) to the left).
3. Average contact force exerted on cart 1 is **\(7.5\,\mathrm{N}\) to the left** (\(-7.5\,\mathrm{N}\)).

---

### Worked example 3: Separation of an orbiting satellite module

A satellite module of total mass \(12.0\,\mathrm{kg}\) travels in deep space with a velocity of \(1.5\,\mathrm{m\,s^{-1}}\) in a straight line. 

An internal spring mechanism releases an instrument capsule of mass \(3.0\,\mathrm{kg}\), pushing it directly forward along the original line of motion. The instrument capsule moves forward with a speed of \(3.5\,\mathrm{m\,s^{-1}}\).

Calculate the final velocity of the remaining main body of the satellite.

#### Step 1: Identify given quantities
Define the forward direction of travel as positive (\(+\)).
- Total initial mass: \(M = 12.0\,\mathrm{kg}\)
- Initial velocity of module: \(u = +1.5\,\mathrm{m\,s^{-1}}\)
- Mass of capsule: \(m_c = 3.0\,\mathrm{kg}\)
- Final velocity of capsule: \(v_c = +3.5\,\mathrm{m\,s^{-1}}\)
- Mass of remaining main body: \(m_b = 12.0 - 3.0 = 9.0\,\mathrm{kg}\)
- Final velocity of main body: \(v_b\) (to be found)

#### Step 2: Total initial momentum
\[
p_{\mathrm{initial}} = M u = 12.0\,\mathrm{kg} \times 1.5\,\mathrm{m\,s^{-1}} = +18.0\,\mathrm{kg\,m\,s^{-1}}
\]

#### Step 3: Total final momentum
\[
p_{\mathrm{final}} = m_c v_c + m_b v_b = (3.0\,\mathrm{kg} \times 3.5\,\mathrm{m\,s^{-1}}) + (9.0\,\mathrm{kg} \times v_b)
\]
\[
p_{\mathrm{final}} = 10.5 + 9.0 v_b
\]

#### Step 4: Equate and solve
Because the release involves only internal forces, the satellite is an isolated system:
\[
p_{\mathrm{final}} = p_{\mathrm{initial}}
\]
\[
10.5 + 9.0 v_b = 18.0
\]
\[
9.0 v_b = 18.0 - 10.5 = 7.5
\]
\[
v_b = \frac{7.5}{9.0} \approx +0.833\,\mathrm{m\,s^{-1}}
\]

To two significant figures, the final velocity of the main body is \(0.83\,\mathrm{m\,s^{-1}}\) forward.

#### Physical interpretation
Notice that because the lighter capsule was propelled forward, the heavier main body slowed down from \(1.5\,\mathrm{m\,s^{-1}}\) to \(0.83\,\mathrm{m\,s^{-1}}\). Its forward momentum decreased by \(12.0 \times 1.5 - 9.0 \times 0.833 = 18.0 - 7.5 = 10.5\,\mathrm{kg\,m\,s^{-1}}\), which is exactly the momentum carried by the forward-flying capsule!

**Answer:**
The velocity of the remaining main body is **\(0.83\,\mathrm{m\,s^{-1}}\) forward**.

---

## Active learning checks

### Check 1: Conditions for momentum conservation

A student states: "The total momentum of two colliding cars is always conserved during any crash on a road."

Which evaluation of this statement is correct?

- **A.** The statement is incorrect because the cars and road do not form an isolated system; large external horizontal frictional forces act between the tyres and the road.
- **B.** The statement is correct because momentum is a fundamental conserved quantity and cannot be destroyed in any physical collision.

**Feedback for A:** Correct. The principle of conservation of momentum applies strictly to an **isolated system** with no resultant external force. While internal forces between the colliding cars cancel out, friction with the road surface is an external force acting on the two cars. That external force transfers momentum to the Earth, causing the total momentum of the two cars alone to decrease.

**Feedback for B:** Incorrect. While momentum is universally conserved for the universe as a whole, the two cars alone do not form an isolated system when tyre friction and road forces act. To apply conservation of momentum without qualification, external forces must be zero or negligible.

### Check 2: Sign convention in a head-on collision

Two identical balls, each of mass \(0.20\,\mathrm{kg}\), travel along the same horizontal line. Ball X travels to the right at \(3.0\,\mathrm{m\,s^{-1}}\). Ball Y travels to the left at \(2.0\,\mathrm{m\,s^{-1}}\).

What is the total momentum of the system?

- **A.** \(+0.20\,\mathrm{kg\,m\,s^{-1}}\) to the right
- **B.** \(+1.0\,\mathrm{kg\,m\,s^{-1}}\) to the right

**Feedback for A:** Correct. Velocity is a vector. Taking right as positive: \(u_X = +3.0\,\mathrm{m\,s^{-1}}\) and \(u_Y = -2.0\,\mathrm{m\,s^{-1}}\). The total momentum is \(p_{\mathrm{total}} = m_X u_X + m_Y u_Y = (0.20 \times 3.0) + (0.20 \times -2.0) = +0.60 - 0.40 = +0.20\,\mathrm{kg\,m\,s^{-1}}\). You must include the negative sign for motion in the opposite direction.

**Feedback for B:** Incorrect. This calculation incorrectly adds the scalar speeds: \(0.60 + 0.40 = 1.0\,\mathrm{kg\,m\,s^{-1}}\). Because the balls are moving towards each other in opposite directions, their momenta have opposite signs and partially cancel.

### Check 3: Speeds in an explosion from rest

A stationary cannon of mass \(1200\,\mathrm{kg}\) fires a cannonball of mass \(12\,\mathrm{kg}\) with a horizontal muzzle velocity of \(200\,\mathrm{m\,s^{-1}}\). Friction with the ground during firing is negligible.

Which statement correctly describes the recoil of the cannon?

- **A.** The cannon has a momentum of \(2400\,\mathrm{kg\,m\,s^{-1}}\) backward and recoils at \(2.0\,\mathrm{m\,s^{-1}}\).
- **B.** The cannon has a momentum of \(2400\,\mathrm{kg\,m\,s^{-1}}\) backward and recoils at \(200\,\mathrm{m\,s^{-1}}\).

**Feedback for A:** Correct. The initial momentum is zero. After firing, the cannonball has forward momentum \(p_{\mathrm{ball}} = 12\,\mathrm{kg} \times 200\,\mathrm{m\,s^{-1}} = +2400\,\mathrm{kg\,m\,s^{-1}}\). By conservation of momentum, the cannon must have backward momentum \(p_{\mathrm{cannon}} = -2400\,\mathrm{kg\,m\,s^{-1}}\). Its recoil speed is \(v = \frac{2400\,\mathrm{kg\,m\,s^{-1}}}{1200\,\mathrm{kg}} = 2.0\,\mathrm{m\,s^{-1}}\). The momenta are equal in magnitude, but the much heavier cannon moves at a fraction of the speed of the ball.

**Feedback for B:** Incorrect. Equal and opposite momentum does not mean equal speeds! Because the cannon has \(100\) times the mass of the cannonball (\(1200\,\mathrm{kg} / 12\,\mathrm{kg} = 100\)), its recoil speed is \(100\) times smaller than the cannonball speed: \(200 / 100 = 2.0\,\mathrm{m\,s^{-1}}\).

### Check 4: Vector representation in two dimensions

A particle moving horizontally along the x-axis with momentum \(\vec{p}_0\) collides with a stationary particle. After the collision, the two particles fly off at angles above and below the x-axis with momenta \(\vec{p}_1\) and \(\vec{p}_2\).

How can these three momentum vectors be drawn to represent conservation of momentum?

- **A.** When vector \(\vec{p}_1\) and vector \(\vec{p}_2\) are placed head-to-tail, their vector sum forms a resultant arrow that exactly equals \(\vec{p}_0\).
- **B.** Vectors \(\vec{p}_0\), \(\vec{p}_1\), and \(\vec{p}_2\) placed head-to-tail must form a closed triangle with zero resultant.

**Feedback for A:** Correct. The conservation law is \(\vec{p}_1 + \vec{p}_2 = \vec{p}_0\). Therefore, placing the final momentum vectors \(\vec{p}_1\) and \(\vec{p}_2\) head-to-tail yields the initial momentum vector \(\vec{p}_0\) as their resultant.

**Feedback for B:** Incorrect. A closed triangle represents a sum that equals zero: \(\vec{p}_1 + \vec{p}_2 + \vec{p}_3 = 0\), which occurs when an object explodes from rest. In this collision, the initial momentum is non-zero (\(\vec{p}_0 \neq 0\)), so the sum of the two final vectors must equal the non-zero initial vector \(\vec{p}_0\).

---

## Mistakes worth repairing

### Mistake 1: Omitting the isolated system condition
Students frequently write: "Conservation of momentum states that total momentum before equals total momentum after." While close, this omits the essential condition and loses full marks on Cambridge papers. 
- You must state that there is **no resultant external force**, or specify that the system is **isolated** or **closed**.
- Without this condition, the statement is physically false (for instance, a ball falling under gravity gains downward momentum continuously because gravity is an external force).

### Mistake 2: Forgetting velocity is a vector
In one-dimensional calculations, students often add speeds directly:
\[
m_1 u_1 + m_2 u_2
\]
without checking direction. If body 2 is moving to the left, its velocity must be entered as \(-u_2\). Failing to include negative signs for opposing velocities is the single most frequent numerical mistake in Dynamics.

### Mistake 3: Confusing momentum with velocity in recoil problems
Students often think that if momentum is conserved equally between two separating bodies, both bodies must move away at the same speed. 
- The **momenta** are equal in magnitude: \(|p_1| = |p_2|\).
- The **speeds** are inversely proportional to their masses: \(v_1 / v_2 = m_2 / m_1\).
- A lighter fragment always carries away far more speed than a heavy body.

### Mistake 4: Assuming momentum conservation requires kinetic energy conservation
Many learners assume that if total momentum is conserved, total kinetic energy must also be conserved. This is not true!
- Momentum is **always** conserved in any isolated interaction, whether the collision is elastic, inelastic, or an explosion.
- Kinetic energy is conserved **only in elastic collisions**. In inelastic collisions, kinetic energy decreases; in explosions, kinetic energy increases. (This distinction is the central focus of Lesson 7).

### Mistake 5: Constructing velocity triangles instead of momentum triangles
When solving two-dimensional problems, students sometimes draw vector triangles using velocities: \(\vec{u} = \vec{v}_1 + \vec{v}_2\). 
- Velocities do not add to give the initial velocity unless the masses happen to be identical!
- You must multiply each velocity vector by its respective mass to construct a **momentum vector diagram**:
  \[
  \vec{p}_{\mathrm{initial}} = m_1 \vec{v}_1 + m_2 \vec{v}_2
  \]

---

## Core recap

- An **isolated system** (or closed system) is one on which no resultant external force acts (\(\Sigma F_{\mathrm{external}} = 0\)).
- The **principle of conservation of momentum** states that:
  > the total momentum of an isolated system remains constant
- The principle follows directly from Newton's third law (\(F_{21} = -F_{12}\)) and Newton's second law (\(F = \frac{\Delta p}{\Delta t}\)), proving that:
  \[
  \Delta p_1 + \Delta p_2 = 0 \implies \Sigma p_{\mathrm{initial}} = \Sigma p_{\mathrm{final}}
  \]
- For a two-body collision along a straight line:
  \[
  m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2
  \]
  Velocities must be assigned positive or negative signs according to a defined directional convention.
- When two bodies coalesce (stick together) on impact:
  \[
  m_1 u_1 + m_2 u_2 = (m_1 + m_2)V
  \]
- In an explosion or recoil from rest:
  \[
  0 = m_1 v_1 + m_2 v_2 \implies m_1 v_1 = -m_2 v_2
  \]
  The two bodies acquire equal and opposite linear momenta; the lighter body moves with the higher speed.
- In two dimensions, momentum is conserved independently along mutually perpendicular axes:
  \[
  \Sigma p_{x, \mathrm{initial}} = \Sigma p_{x, \mathrm{final}} \quad \text{and} \quad \Sigma p_{y, \mathrm{initial}} = \Sigma p_{y, \mathrm{final}}
  \]
- Graphically, the vector sum of the final momenta equals the initial momentum vector, forming a vector triangle or closed polygon.
