# Motion in a uniform gravitational field with air resistance and terminal velocity

## Falling through an ocean of air

In Topic 2 (Kinematics), you analyzed the idealized motion of objects falling freely under gravity. In that simplified model, air resistance was assumed to be negligible:
- Every falling object accelerated downwards at a constant rate equal to the acceleration of free fall:
  \[
  a = g = 9.81\,\mathrm{m\,s^{-2}}
  \]
- Its velocity increased steadily without limit:
  \[
  v = gt
  \]
- Its velocity-time graph was a straight line with a constant gradient of \(9.81\,\mathrm{m\,s^{-2}}\).

If the Earth had no atmosphere (like the Moon), this constant-acceleration model would describe every falling body perfectly. A lead cannonball and a bird feather dropped side by side in a vacuum chamber fall with the exact same acceleration and strike the bottom at the exact same instant.

However, we live at the bottom of an atmosphere of air.

If you drop a feather and a lead ball in an ordinary classroom:
- The lead ball plunges quickly to the floor in a fraction of a second.
- The feather drifts downward slowly, fluttering gently and descending at a low, steady speed.

In the previous lesson, you learned that when an object moves through a fluid such as air, it experiences an opposing **drag force** (air resistance) that increases as its speed increases.

In this lesson, we will combine Newton's laws of motion with this speed-dependent drag to explain the complete journey of an object falling through a uniform gravitational field, from the instant of release to the moment it reaches a constant, unchanging speed known as **terminal velocity**.

---

## Step-by-step physics of vertical fall with air resistance

Consider an object of mass \(m\) released from rest in still air near the surface of the Earth, where the gravitational field strength \(g\) is uniform (\(9.81\,\mathrm{N\,kg^{-1}}\) or \(9.81\,\mathrm{m\,s^{-2}}\)).

Two vertical forces act on the falling object:
1. **Weight (\(W = mg\)):** The downward gravitational force exerted by the Earth. Near the Earth's surface, this force remains completely constant in magnitude and direction throughout the fall.
2. **Air resistance (\(D\)):** The upward drag force exerted by the air, opposing the downward motion. The magnitude of \(D\) depends directly on the object's speed \(v\): \(D = 0\) when stationary, and \(D\) increases as speed increases.

Let us choose **downwards** as the positive direction. The resultant vertical force acting on the object is:

\[
F_{\mathrm{net}} = W - D = mg - D
\]

Applying Newton's second law (\(F_{\mathrm{net}} = ma\)), the object's downward acceleration is:

\[
a = \frac{F_{\mathrm{net}}}{m} = \frac{mg - D}{m} = g - \frac{D}{m}
\]

We can trace the object's motion through three distinct physical stages.

---

### Stage 1: The instant of release (\(t = 0\))

At the very instant the object is released from rest:
- Its speed is zero: \(v = 0\).
- Because drag requires relative motion through the fluid, the air resistance is zero: \(D = 0\).
- Therefore, the only force acting on the object is its downward weight:
  \[
  F_{\mathrm{net}} = mg - 0 = mg
  \]
- The initial acceleration is:
  \[
  a = \frac{mg}{m} = g = 9.81\,\mathrm{m\,s^{-2}}
  \]

> **Crucial observation for graphs:** At \(t = 0\), an object falling in air has the **exact same initial acceleration** (\(g\)) as an object falling in a vacuum. On a velocity-time graph, the tangent to the curve at \(t = 0\) has a gradient of \(9.81\,\mathrm{m\,s^{-2}}\).

---

### Stage 2: As speed increases (\(t > 0\))

Because the initial acceleration is downward, the object accelerates and its downward speed \(v\) begins to increase:
- As speed \(v\) increases, the upward air resistance \(D\) increases.
- Because the downward weight \(mg\) remains constant while upward drag \(D\) grows, the net downward force decreases:
  \[
  F_{\mathrm{net}} = mg - D \quad \text{(decreasing)}
  \]
- Because the net force decreases, the downward acceleration decreases:
  \[
  a = g - \frac{D}{m} \quad \text{(decreasing)}
  \]

Notice carefully what is happening here:
- The acceleration is still positive (directed downwards), and velocity is directed downwards.
- Because acceleration and velocity are in the same direction, the object is **still speeding up**.
- However, because the magnitude of acceleration is decreasing, the object is gaining speed **at an ever-decreasing rate**.
- On a velocity-time graph, the curve continues to rise, but its gradient (\(\frac{\Delta v}{\Delta t}\)) becomes progressively less steep (the curve bends over, concave downwards).

---

### Stage 3: Terminal velocity reached (\(D = mg\))

As the object falls faster and faster, the upward drag force continues to grow:
- Eventually, the speed reaches a critical value where the upward drag force becomes equal in magnitude to the downward weight:
  \[
  D = mg
  \]
- When this happens, the upward and downward forces are perfectly balanced:
  \[
  F_{\mathrm{net}} = mg - D = 0
  \]
- By Newton's second law, when the resultant force is zero, the acceleration must be zero:
  \[
  a = \frac{0}{m} = 0
  \]
- With zero acceleration, the velocity of the object ceases to change:
  \[
  \frac{\Delta v}{\Delta t} = 0
  \]
- The object continues to fall at a constant, maximum speed.

This constant speed is called the **terminal velocity** (symbol \(v_t\)).

> **Definition of terminal velocity:** The constant maximum velocity reached by an object moving through a resistive fluid when the opposing drag force equals the driving force (for a falling body, when upward drag equals downward weight).

---

## Graphical comparison: fall in a vacuum versus fall in air

In Cambridge examinations, you will frequently be asked to sketch, identify, or interpret the motion graphs of an object falling in air compared to one falling in a vacuum.

### 1. The velocity-time (\(v-t\)) graph

- **In a vacuum (no air resistance):**
  - Resultant force is constant (\(F = mg\)).
  - Acceleration is constant (\(a = g\)).
  - The \(v-t\) graph is a straight line through the origin with constant positive gradient \(g\).
- **In air (with air resistance):**
  - At \(t = 0\), the curve starts at the origin with the **same initial gradient** (\(g\)) as the vacuum line.
  - As time proceeds, the gradient decreases steadily, bending away from and below the vacuum line.
  - As \(t\) becomes large, the curve approaches a horizontal line (a plateau) asymptotically at the terminal velocity \(v = v_t\), where the gradient is zero.

```
Velocity (v)
  ^
  |        /  (In a vacuum: straight line, constant gradient g)
  |       /
  |      /       ------------- Terminal velocity (v_t)
  |     /      /
  |    /     /
  |   /    /   (In air: curved, decreasing gradient, levels off)
  |  /   /
  | /  /
  |/ /
  +----------------------------------> Time (t)
  0 (Both start at origin with same initial gradient g)
```

---

### 2. The acceleration-time (\(a-t\)) graph

- **In a vacuum:**
  - Acceleration remains constant at \(a = g = 9.81\,\mathrm{m\,s^{-2}}\) for all times.
  - The \(a-t\) graph is a horizontal straight line at \(a = g\).
- **In air:**
  - At \(t = 0\), acceleration starts at its maximum value: \(a = g\).
  - As speed increases, drag increases, so acceleration decreases continuously.
  - As the object approaches terminal velocity, the acceleration decays smoothly toward zero, approaching the horizontal time axis asymptotically.

```
Acceleration (a)
  ^
g |----------------------------- (In a vacuum: constant a = g)
  |\
  | \
  |  \
  |   \
  |    \___
  |        \____________________ (In air: decays smoothly to a = 0)
  +----------------------------------> Time (t)
  0
```

---

### 3. The displacement-time (\(s-t\)) graph

- **In a vacuum:**
  - Displacement is given by \(s = \frac{1}{2}gt^2\).
  - The \(s-t\) graph is a parabola curving upward with an ever-increasing gradient (ever-increasing velocity).
- **In air:**
  - Initially, the curve begins identically to the vacuum parabola (accelerating).
  - As the velocity levels off to a constant value \(v_t\), the gradient of the displacement-time graph becomes constant.
  - Therefore, the \(s-t\) graph transitions into a straight line with a constant gradient equal to \(v_t\).

---

### 4. Acceleration plotted against drag force

Because the net downward force is \(F_{\mathrm{net}} = mg - D\), we have:

\[
a = \frac{mg - D}{m} = g - \left(\frac{1}{m}\right)D
\]

Notice the mathematical form of this equation:
- It is a linear equation of the form \(y = c + mx\), where \(y = a\) and \(x = D\).
- If you plot **acceleration \(a\)** on the vertical axis against **drag force \(D\)** on the horizontal axis:
  - The graph is a **straight line with a negative gradient** equal to \(-\frac{1}{m}\).
  - The vertical intercept (when \(D = 0\)) is \(a = g\).
  - The horizontal intercept (when \(a = 0\)) occurs at \(D = mg\) (terminal velocity).

---

## Factors determining terminal velocity

Why does a raindrop fall with a terminal velocity of about \(9\,\mathrm{m\,s^{-1}}\), while a skydiver in free fall reaches about \(54\,\mathrm{m\,s^{-1}}\), and a tiny mist droplet falls at less than \(0.01\,\mathrm{m\,s^{-1}}\)?

Terminal velocity occurs when:

\[
D = mg
\]

The value of the terminal velocity depends on three main physical factors:

### 1. Mass and weight

Consider two spheres of identical size, identical spherical shape, and identical smooth surface texture, but one is made of solid lead (dense and heavy) while the other is made of hollow plastic (light):
- Because they have the same size and shape, at any given speed \(v\) they experience the **exact same drag force** \(D\).
- However, the lead sphere has a much larger mass, so its weight \(W_{\mathrm{lead}} = m_{\mathrm{lead}}g\) is much larger than the plastic sphere's weight \(W_{\mathrm{plastic}} = m_{\mathrm{plastic}}g\).
- For the plastic sphere, the small weight is balanced by drag at a relatively low speed. Once \(D = W_{\mathrm{plastic}}\), it reaches terminal velocity and stops accelerating.
- For the lead sphere, the same drag force at that low speed is far smaller than its heavy weight (\(D \ll W_{\mathrm{lead}}\)). The lead sphere keeps accelerating to much higher speeds until the drag finally grows large enough to balance its larger weight.

> **General rule for same size and shape:** A more massive object reaches a **higher terminal velocity** and takes a longer time and distance to reach it.

---

### 2. Surface area and orientation

Drag force increases with the frontal cross-sectional area of the object facing the airflow:
- A larger frontal area collides with more air particles per second, producing a larger drag force at any given speed.
- Because drag is larger at every speed, the drag reaches equality with weight (\(D = mg\)) at a **lower speed**.
- Therefore, increasing surface area **reduces** the terminal velocity.

A skydiver uses this principle dynamically during free fall:
- **Belly-to-earth position:** The skydiver spreads arms and legs wide, presenting a maximum frontal area (about \(0.8\,\mathrm{m^2}\)) to the airflow. The terminal velocity is roughly \(50\,\mathrm{m\,s^{-1}}\) (around \(180\,\mathrm{km\,h^{-1}}\)).
- **Head-first dive:** The skydiver pulls arms and legs tightly against the body, presenting a minimal frontal area (about \(0.2\,\mathrm{m^2}\)). In this streamlined orientation, drag at \(50\,\mathrm{m\,s^{-1}}\) is far smaller than weight, so the skydiver accelerates further, reaching a terminal velocity in excess of \(90\,\mathrm{m\,s^{-1}}\) (\(320\,\mathrm{km\,h^{-1}}\)).

---

### 3. Density of the fluid

The drag force is proportional to the density of the fluid through which the object moves:
- Air has a low density (\(\approx 1.2\,\mathrm{kg\,m^{-3}}\)), so a steel ball bearing falling through air reaches a high terminal velocity (over \(50\,\mathrm{m\,s^{-1}}\)).
- Water is about 800 times denser than air (\(\approx 1000\,\mathrm{kg\,m^{-3}}\)), and engine oil is both dense and highly viscous. If the same steel ball bearing is dropped into a cylinder of thick oil, it encounters immense drag even at tiny speeds, reaching a low terminal velocity of just a few centimetres per second within fractions of a second.

---

## The complete skydiver journey: opening a parachute

The motion of a skydiver deploying a parachute is a classic Cambridge 9702 examination scenario that tests your deep understanding of Newton's laws. Let us break the journey down into four consecutive stages:

```
Speed (v)
  ^
  |        /-----\  (Stage 2: First terminal velocity, v_t1 ≈ 50 m/s)
  |       /       \
  |      /         \  (Stage 3: Parachute opens: rapid deceleration!)
  |     /           \
  |    /             \_____  (Stage 4: Second terminal velocity, v_t2 ≈ 5 m/s)
  |   /                    \
  +--+----------------------+--------> Time (t)
  0 (Stage 1: free fall)    (Landing)
```

### Stage 1: Initial free fall from the aircraft
- The skydiver jumps from the aircraft. Initially \(v = 0\), \(D = 0\), and \(a = g = 9.81\,\mathrm{m\,s^{-2}}\) downwards.
- As the skydiver speeds up, drag increases, net downward force decreases, and downward acceleration decreases.

### Stage 2: First terminal velocity (free fall)
- After about 12 to 15 seconds, upward drag balances downward weight: \(D = mg\).
- Net force is zero, acceleration is zero, and the skydiver falls at a steady terminal velocity of approximately \(v_{t1} \approx 50\,\mathrm{m\,s^{-1}}\).

### Stage 3: Parachute deployment (rapid deceleration)
- The skydiver pulls the ripcord, and the parachute canopy rapidly inflates.
- The effective surface area increases dramatically (from about \(0.8\,\mathrm{m^2}\) to over \(35\,\mathrm{m^2}\)).
- Because the skydiver is still moving at \(50\,\mathrm{m\,s^{-1}}\), the enormous new surface area produces an instantaneous upward drag force \(D\) that is **vastly larger than the skydiver's weight**:
  \[
  D \gg mg
  \]
- Now look at the net force:
  \[
  F_{\mathrm{net}} = mg - D < 0 \quad \text{(a large net UPWARD force)}
  \]
- By Newton's second law, a net upward force causes an **upward acceleration**:
  \[
  a = \frac{mg - D}{m} \quad \text{(directed upwards)}
  \]
- **What happens to the skydiver's motion?**
  - The skydiver's velocity is **downwards**, but their acceleration is **upwards**.
  - When acceleration opposes velocity, the object **slows down** (decelerates).
  - The skydiver does NOT shoot upwards into the sky! They continue falling downwards, but their downward speed drops rapidly from \(50\,\mathrm{m\,s^{-1}}\) toward \(5\,\mathrm{m\,s^{-1}}\).
  - (The optical illusion seen in skydiving videos where a person appears to shoot upward occurs because the videographer who has not yet deployed a parachute continues falling downward at \(50\,\mathrm{m\,s^{-1}}\), accelerating past the slowing parachutist).

### Stage 4: Second terminal velocity
- As the skydiver's downward speed decreases, the drag force \(D\) decreases.
- The upward drag decreases until it once again exactly balances the downward weight:
  \[
  D = mg
  \]
- When \(D = mg\), the net force returns to zero, acceleration becomes zero, and the parachutist drifts steadily at a new, safe terminal velocity:
  \[
  v_{t2} \approx 4 \text{ to } 6\,\mathrm{m\,s^{-1}}
  \]
- The skydiver lands gently on the ground at this manageable speed.

---

## Worked Examples

### Worked Example 1: Falling metal sphere

A solid steel sphere of mass \(0.50\,\mathrm{kg}\) is dropped from rest from a weather balloon high in the atmosphere. The acceleration of free fall is \(g = 9.81\,\mathrm{m\,s^{-2}}\).

Air resistance \(D\) opposes the downward motion. The magnitude of \(D\) increases with speed such that:
- when \(v = 15\,\mathrm{m\,s^{-1}}\), \(D = 1.9\,\mathrm{N}\);
- when \(v = 30\,\mathrm{m\,s^{-1}}\), \(D = 3.8\,\mathrm{N}\);
- the sphere eventually reaches a constant terminal velocity \(v_t\).

**(a)** Calculate the weight \(W\) of the sphere.

**(b)** State the magnitude and direction of the resultant force and the acceleration of the sphere at the instant of release (\(t = 0\)).

**(c)** Calculate the resultant force and instantaneous acceleration when the sphere reaches a speed of \(v = 30\,\mathrm{m\,s^{-1}}\).

**(d)** Determine the magnitude of the air resistance \(D\) when the sphere falls at its terminal velocity.

**(e)** Sketch the general shape of the velocity-time graph for the sphere, and state the value of the gradient at \(t = 0\) and at terminal velocity.

---

#### Solution to Example 1

**(a) Weight of the sphere:**

Using \(W = mg\):
\[
W = 0.50\,\mathrm{kg} \times 9.81\,\mathrm{m\,s^{-2}} = 4.905\,\mathrm{N} \approx 4.9\,\mathrm{N}
\]

---

**(b) At the instant of release (\(t = 0\)):**

- At release, speed \(v = 0\), so air resistance \(D = 0\).
- The only force acting is downward weight:
  \[
  F_{\mathrm{net}} = W = 4.9\,\mathrm{N} \quad \text{(vertically downwards)}
  \]
- The initial acceleration is:
  \[
  a = \frac{F_{\mathrm{net}}}{m} = \frac{4.905\,\mathrm{N}}{0.50\,\mathrm{kg}} = 9.81\,\mathrm{m\,s^{-2}} \quad \text{(vertically downwards)}
  \]

---

**(c) At speed \(v = 30\,\mathrm{m\,s^{-1}}\):**

- Downward force: Weight \(W = 4.91\,\mathrm{N}\).
- Upward force: Air resistance \(D = 3.8\,\mathrm{N}\).
- Resultant downward force:
  \[
  F_{\mathrm{net}} = W - D = 4.905\,\mathrm{N} - 3.8\,\mathrm{N} = +1.105\,\mathrm{N} \approx 1.1\,\mathrm{N} \quad \text{(downwards)}
  \]
- Instantaneous downward acceleration:
  \[
  a = \frac{F_{\mathrm{net}}}{m} = \frac{1.105\,\mathrm{N}}{0.50\,\mathrm{kg}} = 2.21\,\mathrm{m\,s^{-2}} \approx 2.2\,\mathrm{m\,s^{-2}} \quad \text{(downwards)}
  \]
- **Notice:** The sphere is still accelerating downwards (its speed is still increasing), but its acceleration has fallen from \(9.81\,\mathrm{m\,s^{-2}}\) to \(2.2\,\mathrm{m\,s^{-2}}\).

---

**(d) At terminal velocity:**

At terminal velocity, the velocity is constant, so acceleration is zero (\(a = 0\)).
By Newton's first/second law:
\[
F_{\mathrm{net}} = 0 \implies W - D = 0 \implies D = W
\]
Therefore, the upward air resistance equals the weight:
\[
D = 4.9\,\mathrm{N}
\]

---

**(e) Features of the velocity-time graph:**

- The graph starts at the origin \((0, 0)\).
- Initial gradient at \(t = 0\):
  \[
  \text{gradient} = a = 9.81\,\mathrm{m\,s^{-2}}
  \]
- As \(t\) increases, the curve rises with a steadily decreasing gradient.
- At terminal velocity, the curve levels off to a horizontal line:
  \[
  \text{gradient} = a = 0\,\mathrm{m\,s^{-2}}
  \]

---

### Worked Example 2: Skydiver opening a parachute

A skydiver of total mass \(80\,\mathrm{kg}\) (including gear and parachute) falls vertically through the air. The acceleration of free fall is \(g = 9.81\,\mathrm{m\,s^{-2}}\).

**(a)** Before opening the parachute, the skydiver falls at a steady terminal velocity of \(52\,\mathrm{m\,s^{-1}}\). State:
1. the resultant force acting on the skydiver;
2. the magnitude of the air resistance acting on the skydiver.

**(b)** The skydiver opens the parachute. At the instant the canopy fully opens, the upward drag force suddenly surges to \(2200\,\mathrm{N}\).
1. Calculate the magnitude and direction of the resultant vertical force at this instant.
2. Calculate the magnitude and direction of the skydiver's acceleration at this instant.
3. Describe the effect of this acceleration on the skydiver's velocity.

**(c)** Eventually, the skydiver reaches a second, lower terminal velocity with the open parachute. State the magnitude of the air resistance at this second terminal velocity.

---

#### Solution to Example 2

**(a) During initial terminal velocity (\(v = 52\,\mathrm{m\,s^{-1}}\)):**

1. Because the skydiver is falling at constant velocity, acceleration is zero. By Newton's second law:
   \[
   F_{\mathrm{net}} = 0\,\mathrm{N}
   \]
2. For zero resultant force, upward air resistance must balance downward weight:
   \[
   W = mg = 80\,\mathrm{kg} \times 9.81\,\mathrm{m\,s^{-2}} = 784.8\,\mathrm{N} \approx 780\,\mathrm{N}
   \]
   \[
   D = W = 785\,\mathrm{N} \quad \text{(vertically upwards)}
   \]

---

**(b) Immediately after the parachute opens:**

1. Let us choose **downwards** as positive:
   - Weight: \(W = +785\,\mathrm{N}\) (downwards)
   - Upward drag: \(D = 2200\,\mathrm{N}\) (upwards, so \(-2200\,\mathrm{N}\))
   - Resultant force:
     \[
     F_{\mathrm{net}} = +785\,\mathrm{N} - 2200\,\mathrm{N} = -1415\,\mathrm{N} \approx -1400\,\mathrm{N}
     \]
   The resultant force has a magnitude of \(1400\,\mathrm{N}\) and is directed **vertically upwards**.

2. Acceleration:
   \[
   a = \frac{F_{\mathrm{net}}}{m} = \frac{-1415\,\mathrm{N}}{80\,\mathrm{kg}} = -17.7\,\mathrm{m\,s^{-2}} \approx -18\,\mathrm{m\,s^{-2}}
   \]
   The acceleration has a magnitude of \(18\,\mathrm{m\,s^{-2}}\) and is directed **vertically upwards** (which is approximately \(1.8g\) upward).

3. Effect on velocity:
   The skydiver's velocity is directed **downwards**, but the acceleration is directed **upwards**. Because acceleration opposes velocity, the downward speed decreases rapidly (deceleration). The skydiver continues moving downwards, but slows down rapidly.

---

**(c) At the second terminal velocity:**

At the second terminal velocity, the velocity is once again constant, so acceleration is zero (\(a = 0\)).
Therefore, the resultant force must again be zero:
\[
D = W = 785\,\mathrm{N} \approx 780\,\mathrm{N}
\]
Notice that the air resistance is exactly the same (\(785\,\mathrm{N}\)) at the second terminal velocity as it was at the first terminal velocity! What has changed is the **speed**: because the parachute has an enormous surface area, a drag of \(785\,\mathrm{N}\) is achieved at a very low speed (\(\approx 5\,\mathrm{m\,s^{-1}}\)) instead of \(52\,\mathrm{m\,s^{-1}}\).

---

### Worked Example 3: Comparing two falling spheres of different mass

Two spheres, \(X\) and \(Y\), have identical external volumes, identical spherical shapes, and identical smooth surface finishes. Sphere \(X\) is made of solid lead and has a mass of \(2.0\,\mathrm{kg}\). Sphere \(Y\) is made of solid wood and has a mass of \(0.40\,\mathrm{kg}\).

Both spheres are released simultaneously from rest from the top of a very tall tower in still air.

**(a)** Compare the initial acceleration of Sphere \(X\) and Sphere \(Y\) at the moment of release (\(t = 0\)).

**(b)** Explain why Sphere \(X\) reaches a higher terminal velocity than Sphere \(Y\).

**(c)** State which sphere hits the ground first if the tower is tall enough for both spheres to reach their terminal velocities during the fall.

---

#### Solution to Example 3

**(a) Initial acceleration at \(t = 0\):**

At \(t = 0\), both spheres have \(v = 0\), so for both spheres, the air resistance is zero (\(D = 0\)).
For Sphere \(X\):
\[
a_X = \frac{m_X g}{m_X} = g = 9.81\,\mathrm{m\,s^{-2}}
\]
For Sphere \(Y\):
\[
a_Y = \frac{m_Y g}{m_Y} = g = 9.81\,\mathrm{m\,s^{-2}}
\]
Both spheres have the **exact same initial acceleration** of \(9.81\,\mathrm{m\,s^{-2}}\) downwards.

---

**(b) Why Sphere \(X\) has a higher terminal velocity:**

1. Because the two spheres have identical dimensions, surface area, and shape, at any given speed \(v\) they experience the **exact same drag force** \(D\).
2. Terminal velocity requires the upward drag to equal the downward weight: \(D = mg\).
3. The weight of Sphere \(X\) is:
   \[
   W_X = 2.0\,\mathrm{kg} \times 9.81\,\mathrm{m\,s^{-2}} = 19.6\,\mathrm{N}
   \]
   The weight of Sphere \(Y\) is:
   \[
   W_Y = 0.40\,\mathrm{kg} \times 9.81\,\mathrm{m\,s^{-2}} = 3.92\,\mathrm{N}
   \]
4. For Sphere \(Y\), a drag force of only \(3.92\,\mathrm{N}\) is required to balance its weight. It reaches this drag force at a relatively low speed. Once \(D = 3.92\,\mathrm{N}\), its net force is zero and it stops accelerating.
5. For Sphere \(X\), when it reaches the terminal speed of Sphere \(Y\), the drag is only \(3.92\,\mathrm{N}\). But Sphere \(X\) weighs \(19.6\,\mathrm{N}\), so it still has a large net downward force:
   \[
   F_{\mathrm{net}} = 19.6\,\mathrm{N} - 3.92\,\mathrm{N} = 15.7\,\mathrm{N}
   \]
   Sphere \(X\) continues to accelerate to much higher speeds until drag finally reaches \(19.6\,\mathrm{N}\).
6. Therefore, Sphere \(X\) reaches a substantially higher terminal velocity.

---

**(c) Which sphere strikes the ground first:**

Sphere \(X\) (the lead sphere) strikes the ground first. Throughout the descent, Sphere \(X\) maintains a larger net downward force and larger average downward acceleration than Sphere \(Y\), reaches a higher speed, and covers the distance in a shorter time.

---

## Check your understanding

### Check 1: Forces at terminal velocity

A stone of mass \(m\) is dropped from the top of a tall cliff and falls through air until it reaches terminal velocity. The acceleration of free fall is \(g\).

Which statement correctly gives the magnitude of the force of gravity, the magnitude of the air resistance, and the acceleration of the stone when falling at terminal velocity?

- **A.** Force of gravity = \(mg\), Air resistance = \(mg\), Acceleration = \(0\).
- **B.** Force of gravity = \(0\), Air resistance = \(mg\), Acceleration = \(0\).

**Feedback for A:** Correct. The force of gravity is the stone's weight (\(W = mg\)), which acts continuously throughout the fall. At terminal velocity, velocity is constant, so acceleration is zero (\(a = 0\)). By Newton's second law, the resultant force must be zero, meaning upward air resistance must balance downward gravity: Air resistance = \(mg\).

**Feedback for B:** Incorrect. Gravity does not turn off or disappear when an object reaches terminal velocity! The Earth continues to pull downward on the stone with force \(mg\). The reason acceleration is zero is that the upward air resistance has grown to equal the downward gravity, producing a resultant force of zero.

---

### Check 2: Immediately after parachute opening

A parachutist falls vertically downwards at a steady terminal velocity of \(50\,\mathrm{m\,s^{-1}}\). She deploys her parachute.

Which row correctly describes the direction of the parachutist's velocity and the direction of her acceleration immediately after the parachute opens?

- **A.** Velocity is downwards; acceleration is upwards.
- **B.** Velocity is upwards; acceleration is upwards.

**Feedback for A:** Correct. When the parachute opens, the massive increase in surface area creates an upward drag force that is much larger than the downward weight (\(D > mg\)). The resultant force is therefore directed upwards, which produces an upward acceleration. However, the parachutist was already traveling downwards at \(50\,\mathrm{m\,s^{-1}}\). Her downward velocity cannot reverse instantaneously; instead, the upward acceleration decelerates her downward motion, causing her downward speed to decrease.

**Feedback for B:** Incorrect. The parachutist never travels upwards. Her downward speed is reduced from \(50\,\mathrm{m\,s^{-1}}\) to about \(5\,\mathrm{m\,s^{-1}}\), but she continues moving downwards throughout. An upward acceleration applied to a downward velocity reduces the speed of downward motion.

---

### Check 3: Initial gradient on a velocity-time graph

Two identical balls are dropped from rest from the same height. Ball 1 is dropped in an evacuated vacuum chamber, while Ball 2 is dropped in air.

Which statement correctly compares the initial gradient of their velocity-time graphs at the exact moment of release (\(t = 0\))?

- **A.** Both graphs have the exact same initial gradient equal to \(g\).
- **B.** Ball 1 in the vacuum has an initial gradient of \(g\), while Ball 2 in air has a smaller initial gradient because air resistance opposes its motion.

**Feedback for A:** Correct. At the instant of release (\(t = 0\)), the speed of both balls is zero (\(v = 0\)). Because drag requires relative motion, the air resistance on Ball 2 is exactly zero at \(t = 0\). Therefore, for both balls, the only force acting at \(t = 0\) is weight (\(mg\)), and both balls start falling with the exact same initial acceleration \(a = g = 9.81\,\mathrm{m\,s^{-2}}\).

**Feedback for B:** Incorrect. Drag force depends on speed: at \(t = 0\), speed is zero, so drag is zero. Air resistance only comes into existence once the ball starts moving (\(v > 0\)). Therefore, the initial gradient of the velocity-time graph in air is identical to that in a vacuum (\(g\)).

---

### Check 4: Acceleration-time graph for fall with air resistance

Which description correctly characterizes the acceleration-time graph of an object dropped from rest in air until it reaches terminal velocity?

- **A.** Acceleration starts at \(g\) at \(t = 0\) and decreases smoothly toward zero as time increases.
- **B.** Acceleration starts at zero at \(t = 0\) and increases smoothly toward \(g\) as time increases.

**Feedback for A:** Correct. At release (\(t = 0\)), drag is zero and the acceleration is at its maximum value: \(a = g = 9.81\,\mathrm{m\,s^{-2}}\). As the object gains speed, upward drag increases, reducing the resultant force \(F_{\mathrm{net}} = mg - D\). Thus, acceleration decreases smoothly from \(g\) toward zero at terminal velocity.

**Feedback for B:** Incorrect. You have confused acceleration with velocity or drag. Velocity starts at zero and rises to a constant value. Acceleration starts at \(g\) and falls to zero.

---

## Mistakes worth repairing

### Mistake 1: Believing gravity stops acting at terminal velocity

When students learn that acceleration is zero at terminal velocity, they sometimes jump to the conclusion that gravity has ceased to pull on the object or that weight is zero.

In reality:
- Gravitational pull near Earth is constant: \(W = mg\).
- Gravity pulls downward on the object just as strongly at terminal velocity as it did at the instant of release.
- Acceleration is zero because the upward air resistance has grown to exactly match the downward weight:
  \[
  F_{\mathrm{net}} = mg - D = mg - mg = 0
  \]
- Zero resultant force means constant velocity (Newton's first law), not absence of forces.

---

### Mistake 2: Thinking a skydiver shoots upwards when the parachute opens

In video footage of skydiving, when a jumper opens their canopy, they appear to shoot rapidly upward out of the camera frame.

This is an illusion caused by the relative motion of the cameraman:
- The cameraman is still in free fall, descending at \(50\,\mathrm{m\,s^{-1}}\).
- The skydiver's parachute opens, rapidly slowing them down from \(50\,\mathrm{m\,s^{-1}}\) to \(5\,\mathrm{m\,s^{-1}}\).
- The skydiver is still falling downwards towards the Earth at all times.
- Because the cameraman is falling past them at a much higher speed, the skydiver appears to move upward relative to the camera.
- In Cambridge physics, the velocity of the skydiver remains **downward**; only their acceleration is upward.

---

### Mistake 3: Confusing decreasing acceleration with slowing down

Students often see the statement "acceleration is decreasing" and assume that the object is slowing down (decelerating).

Remember the vector rule:
- If velocity is downwards and acceleration is downwards, the object is **speeding up**.
- During Stage 2 of a fall, acceleration decreases from \(9.8\,\mathrm{m\,s^{-2}}\) to \(6.0\,\mathrm{m\,s^{-2}}\) to \(2.0\,\mathrm{m\,s^{-2}}\).
- Because acceleration is still positive (downward), the object is still gaining downward speed. It is simply gaining speed at a lower rate per second.
- An object only slows down when acceleration is directed in the **opposite direction** to velocity (such as when the parachute opens).

---

### Mistake 4: Believing heavy and light objects fall together in air

Students often remember Galileo's famous principle that "all objects fall with the same acceleration regardless of mass" and misapply it to motion in air.

- In a **vacuum**, all objects fall with the exact same acceleration \(g\), because weight is proportional to mass (\(W = mg\)) and inertia is proportional to mass (\(a = \frac{F}{m} = \frac{mg}{m} = g\)).
- In **air**, this mass cancellation breaks down:
  \[
  a = \frac{mg - D}{m} = g - \frac{D}{m}
  \]
- For two objects of the same size and shape, \(D\) is the same at any speed, but the term \(\frac{D}{m}\) is much smaller for the more massive object.
- Therefore, the heavier object accelerates faster, reaches a higher terminal velocity, and strikes the ground earlier.

---

### Mistake 5: Drawing a zero initial gradient on velocity-time graphs in air

When asked to sketch the velocity-time graph for an object dropped from rest in air, candidates frequently start the graph with a horizontal tangent at the origin (gradient = 0), believing that air resistance makes it start slowly.

This is a serious physical error:
- At \(t = 0\), speed is zero, so air resistance is zero.
- With zero air resistance, the net force is \(mg\), and the initial acceleration is exactly \(g\).
- The initial tangent of the velocity-time curve at \(t = 0\) must have a gradient of \(9.81\,\mathrm{m\,s^{-2}}\), matching the straight-line graph in a vacuum.

---

## Core recap

- An object falling from rest in a uniform gravitational field experiences downward weight \(W = mg\) and upward drag \(D\).
- Net downward force is \(F_{\mathrm{net}} = mg - D\), giving downward acceleration \(a = g - \frac{D}{m}\).
- **At release (\(t = 0\)):** speed \(v = 0\), drag \(D = 0\), net force \(F_{\mathrm{net}} = mg\), and initial acceleration \(a = g = 9.81\,\mathrm{m\,s^{-2}}\).
- **During acceleration (\(t > 0\)):** speed increases, drag increases, net force decreases, and acceleration decreases. The \(v-t\) graph is curved with decreasing gradient.
- **At terminal velocity:** drag balances weight (\(D = mg\)), net force is zero (\(F_{\mathrm{net}} = 0\)), acceleration is zero (\(a = 0\)), and velocity remains constant at \(v_t\).
- On motion graphs for fall in air:
  - \(v-t\) starts at \((0,0)\) with initial slope \(g\), bends over, and plateaus horizontally at \(v_t\).
  - \(a-t\) starts at \(g\) and decays smoothly to zero.
  - \(s-t\) curves upward initially, then becomes a straight line of constant gradient \(v_t\).
- **Factors affecting terminal velocity:**
  - Greater mass (for same shape/area) results in higher terminal velocity.
  - Greater frontal cross-sectional area results in lower terminal velocity.
  - Streamlining reduces drag, resulting in higher terminal velocity.
  - Denser fluids result in lower terminal velocity.
- When a parachute opens, drag suddenly exceeds weight (\(D \gg mg\)), producing a large upward resultant force and upward acceleration that rapidly decelerates the downward velocity to a much lower second terminal velocity.

---

## Next lesson preview

In the next lesson (**Topic 3 Module 3 Lesson 6: The principle of conservation of momentum**), you will turn to multi-body interactions. You will define closed, isolated systems, formally state the principle of conservation of linear momentum, and use it to solve collision and explosion problems in one and two dimensions.
