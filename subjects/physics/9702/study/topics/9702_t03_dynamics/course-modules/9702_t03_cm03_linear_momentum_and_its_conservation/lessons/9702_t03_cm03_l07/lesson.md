# That, for an elastic collision, total kinetic energy is conserved and

## Does energy survive a collision?

Drop a soft clay ball onto a hard concrete floor. It lands with a dull thud, deforms into a flat patty, and does not bounce at all. All of its initial kinetic energy has vanished from sight, converted into internal thermal energy and work done in permanently reshaping the clay.

Now drop a fresh glass marble or a solid steel bearing onto the same hard floor. It rebounds almost to the exact height from which it was released. Its kinetic energy was temporarily stored as elastic potential energy during the brief compression of impact, and then almost completely returned to kinetic energy as it bounced back upward.

In Lesson 6, you learned that **linear momentum is always conserved** in any interaction within an isolated system. Whether objects stick together like clay or bounce apart like steel marbles, the total vector momentum before impact equals the total vector momentum after impact.

However, the fate of **kinetic energy** is completely different. In some collisions, kinetic energy is perfectly preserved. In others, a large fraction of the kinetic energy is lost to other forms.

Understanding this difference is one of the most critical skills in Cambridge AS Level Physics. In this lesson, you will master the distinction between elastic and inelastic collisions, learn why total energy is always conserved even when kinetic energy changes, and use the powerful relative speed condition to solve collision problems without cumbersome quadratic equations.

## Elastic versus inelastic collisions

Collisions are classified into two fundamental categories based entirely on what happens to the total kinetic energy of the interacting bodies.

### Elastic collisions

In an **elastic collision** (sometimes called a perfectly elastic collision), no kinetic energy is converted into thermal energy, sound, or permanent deformation.

In Cambridge International AS Level Physics, you must learn the exact approved definition:

<a id="definition-9702_def_elastic_collision"></a>

> **Definition to learn: elastic collision.** a collision in which the total kinetic energy of the system is the same before and after the collision

For an elastic collision between two bodies of mass \(m_1\) and \(m_2\):

\[
\Sigma E_{K, \mathrm{initial}} = \Sigma E_{K, \mathrm{final}}
\]

Recall the formula for kinetic energy:

<a id="formula-9702_formula_kinetic_energy"></a>

> **Formula to learn: Kinetic energy.**
>
> \[
> E_K = \frac{1}{2}mv^2
> \]

Expanding the kinetic energy equation for two bodies yields:

\[
\frac{1}{2}m_1 u_1^2 + \frac{1}{2}m_2 u_2^2 = \frac{1}{2}m_1 v_1^2 + \frac{1}{2}m_2 v_2^2
\]

Truly perfectly elastic collisions between macroscopic objects do not exist in daily life because every real macroscopic collision generates at least a tiny amount of sound or internal friction. However, collisions between subatomic particles (such as electrons, protons, or helium nuclei) and gas molecules in kinetic theory are truly perfectly elastic. Furthermore, collisions between hard steel ball bearings, billiard balls, or specially cushioned air track gliders are so close to being elastic that physicists model them as perfectly elastic.

### Inelastic collisions

In an **inelastic collision**, the total kinetic energy of the system is **not conserved**:

\[
\Sigma E_{K, \mathrm{final}} < \Sigma E_{K, \mathrm{initial}}
\]

Some of the initial kinetic energy is converted into other forms of energy:
- **Thermal energy:** The colliding bodies warm up slightly as atoms vibrate more vigorously.
- **Sound energy:** Acoustic waves radiate into the surrounding air as a bang or click.
- **Permanent deformation (work done):** Crumpling bodywork in a car crash or denting a soft surface.

### Completely inelastic collisions (coalescence)

The extreme case of an inelastic collision occurs when the colliding bodies **stick together** (coalesce) on impact and move forward with a single common velocity \(V\).

A coalescing collision represents the **maximum possible loss of kinetic energy** that is mathematically consistent with the conservation of linear momentum. While the bodies lose as much kinetic energy as possible, their combined momentum remains strictly conserved:

\[
m_1 u_1 + m_2 u_2 = (m_1 + m_2)V
\]

### Kinetic energy change versus the law of conservation of energy

A frequent confusion among students is believing that an inelastic collision violates the law of conservation of energy. It does not!

There is a vital distinction between **kinetic energy** and **total energy**:
- **Total energy is always conserved in every collision.** Energy cannot be created or destroyed.
- In an inelastic collision:
  \[
  E_{K, \mathrm{initial}} = E_{K, \mathrm{final}} + \Delta E_{\mathrm{thermal}} + \Delta E_{\mathrm{sound}} + \Delta E_{\mathrm{deformation}}
  \]
  The missing kinetic energy has simply been transformed into other energy stores. The total energy of the universe remains entirely constant.

| Collision Type | Is Momentum Conserved? | Is Total Energy Conserved? | Is Kinetic Energy Conserved? |
| :--- | :--- | :--- | :--- |
| **Elastic** | Yes (\(\Sigma \vec{p}_i = \Sigma \vec{p}_f\)) | Yes (\(\Sigma E_i = \Sigma E_f\)) | **Yes** (\(\Sigma E_{Ki} = \Sigma E_{Kf}\)) |
| **Inelastic** | Yes (\(\Sigma \vec{p}_i = \Sigma \vec{p}_f\)) | Yes (\(\Sigma E_i = \Sigma E_f\)) | **No** (\(\Sigma E_{Kf} < \Sigma E_{Ki}\)) |
| **Completely Inelastic** | Yes (\(\Sigma \vec{p}_i = \Sigma \vec{p}_f\)) | Yes (\(\Sigma E_i = \Sigma E_f\)) | **No** (maximum loss of \(E_K\)) |

## Relative speed of approach and separation

When two bodies collide in one dimension, testing whether the collision is elastic by calculating \(\frac{1}{2}mv^2\) for each body involves squaring speeds, which can lead to tedious algebra.

Fortunately, there is an elegant relationship that connects the velocities before and after any head-on elastic collision:

<a id="formula-9702_formula_elastic_collision_relative_speed"></a>

> **Formula to learn: Relative speed in elastic collision.**
>
> \[
> u_1 - u_2 = v_2 - v_1
> \]

This equation states a fundamental truth of physics:

> **For an elastic collision, the relative speed of approach is equal to the relative speed of separation.**

### What is the relative speed of approach?

The **relative speed of approach** is the rate at which the distance between the two bodies decreases before they collide:
- If body 1 is behind body 2 and moving in the same direction at a higher speed (e.g. \(u_1 = 8\,\mathrm{m\,s^{-1}}\) chasing \(u_2 = 3\,\mathrm{m\,s^{-1}}\)), the gap closes at:
  \[
  u_1 - u_2 = 8 - 3 = 5\,\mathrm{m\,s^{-1}}
  \]
- If the two bodies move towards each other head-on (e.g. body 1 moves right at \(5\,\mathrm{m\,s^{-1}}\) and body 2 moves left at \(4\,\mathrm{m\,s^{-1}}\)), their closing speed is the sum of their speeds:
  \[
  u_{\mathrm{approach}} = 5 + 4 = 9\,\mathrm{m\,s^{-1}}
  \]
  Using signed velocities with right as positive (\(u_1 = +5\), \(u_2 = -4\)):
  \[
  u_1 - u_2 = (+5) - (-4) = 9\,\mathrm{m\,s^{-1}}
  \]
  The formula handles the signs automatically!

### What is the relative speed of separation?

The **relative speed of separation** is the rate at which the distance between the two bodies increases after they collide:
- After impact, body 2 is ahead of body 1. If body 2 moves forward at \(v_2\) while body 1 moves at \(v_1\), the distance between them widens at rate:
  \[
  v_2 - v_1
  \]
- Notice the subscript order: the left side has \(u_1 - u_2\), while the right side has \(v_2 - v_1\). The indices are reversed!
  \[
  u_1 - u_2 = -(v_1 - v_2) = v_2 - v_1
  \]

### The test for elasticity using relative speeds

Comparing the relative speed of approach with the relative speed of separation provides a direct test for the nature of any head-on collision:
- **Elastic collision:**
  \[
  \text{relative speed of separation} = \text{relative speed of approach}
  \]
- **Inelastic collision:**
  \[
  \text{relative speed of separation} < \text{relative speed of approach}
  \]
- **Completely inelastic collision (coalescing):**
  Because the bodies stick together and travel at the same velocity (\(v_1 = v_2\)):
  \[
  \text{relative speed of separation} = v_2 - v_1 = 0
  \]

### Why does \(u_1 - u_2 = v_2 - v_1\) hold for elastic collisions?

It is instructive to see how this equation arises from the fundamental conservation laws.

For an isolated, head-on elastic collision:
1. **Conservation of momentum:**
   \[
   m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2
   \]
   Rearrange by grouping mass \(m_1\) on the left and mass \(m_2\) on the right:
   \[
   m_1(u_1 - v_1) = m_2(v_2 - u_2) \quad \text{--- (Equation 1)}
   \]

2. **Conservation of kinetic energy:**
   \[
   \frac{1}{2}m_1 u_1^2 + \frac{1}{2}m_2 u_2^2 = \frac{1}{2}m_1 v_1^2 + \frac{1}{2}m_2 v_2^2
   \]
   Cancel the factor of \(\frac{1}{2}\) and group masses on each side:
   \[
   m_1(u_1^2 - v_1^2) = m_2(v_2^2 - u_2^2)
   \]
   Factor each side using the difference of two squares (\(a^2 - b^2 = (a - b)(a + b)\)):
   \[
   m_1(u_1 - v_1)(u_1 + v_1) = m_2(v_2 - u_2)(v_2 + u_2) \quad \text{--- (Equation 2)}
   \]

3. **Divide Equation 2 by Equation 1:**
   Assuming the bodies actually collide and change their velocities (\(u_1 \neq v_1\)), divide the left side of Equation 2 by the left side of Equation 1, and the right side by the right side:
   \[
   \frac{m_1(u_1 - v_1)(u_1 + v_1)}{m_1(u_1 - v_1)} = \frac{m_2(v_2 - u_2)(v_2 + u_2)}{m_2(v_2 - u_2)}
   \]
   The mass terms and difference terms cancel cleanly:
   \[
   u_1 + v_1 = v_2 + u_2
   \]
   Rearranging gives:
   \[
   u_1 - u_2 = v_2 - v_1
   \]

This derivation proves that whenever both momentum and kinetic energy are conserved, the relative speed of approach must equal the relative speed of separation. Because it is linear rather than quadratic, this formula makes solving collision problems vastly simpler!

## Special cases of elastic collisions

### Case 1: Identical masses (\(m_1 = m_2 = m\))

When two identical masses collide elastically in one dimension:
1. Conservation of momentum simplifies to:
   \[
   u_1 + u_2 = v_1 + v_2
   \]
2. The relative speed equation gives:
   \[
   u_1 - u_2 = v_2 - v_1 \implies u_1 - u_2 = -v_1 + v_2
   \]

Add these two equations together:
\[
(u_1 + u_2) + (u_1 - u_2) = (v_1 + v_2) + (v_2 - v_1)
\]
\[
2u_1 = 2v_2 \implies v_2 = u_1
\]

Subtract the two equations:
\[
(u_1 + u_2) - (u_1 - u_2) = (v_1 + v_2) - (v_2 - v_1)
\]
\[
2u_2 = 2v_1 \implies v_1 = u_2
\]

> **When two bodies of equal mass collide elastically in one dimension, they completely exchange their velocities.**

This famous result explains several physical phenomena:
- **Newton's cradle:** When one ball swings in with velocity \(u\) and strikes the stationary identical balls, the incoming ball stops dead (\(v_1 = 0\)) and the last ball flies out with that exact same velocity \(v_2 = u\).
- **Proton moderator in nuclear reactors:** Fast neutrons from nuclear fission have almost the same mass as hydrogen nuclei (protons). In water or heavy water moderators, elastic head-on collisions with stationary protons bring the fast neutrons to a virtual stop in a few collisions, thermalizing them efficiently.

### Case 2: Elastic collision with a much heavier stationary target (\(m_2 \gg m_1\), \(u_2 = 0\))

Imagine a tennis ball striking a massive concrete wall, or a light cart striking a massive pinned stop block.
Because the target is virtually immovable, \(v_2 \approx 0\).
The relative speed formula gives:
\[
u_1 - 0 = 0 - v_1 \implies v_1 = -u_1
\]
The light projectile rebounds with its original speed in the opposite direction!

---

### Worked example 1: Proving whether a collision is elastic

A glider A of mass \(0.60\,\mathrm{kg}\) moves along a frictionless horizontal air track at a speed of \(2.0\,\mathrm{m\,s^{-1}}\) to the right. It collides with a stationary glider B of mass \(0.40\,\mathrm{kg}\).

After the collision, glider A continues moving to the right with a speed of \(0.40\,\mathrm{m\,s^{-1}}\), while glider B moves to the right with a speed of \(2.4\,\mathrm{m\,s^{-1}}\).

```
Before collision:
  [ Glider A (0.60 kg) ] --> 2.0 m s^-1         [ Glider B (0.40 kg) ] (at rest)

After collision:
  [ Glider A (0.60 kg) ] --> 0.40 m s^-1        [ Glider B (0.40 kg) ] --> 2.4 m s^-1
```

1. Show that linear momentum is conserved in this collision.
2. By calculation of kinetic energies, determine whether the collision is elastic or inelastic.
3. Confirm your conclusion by calculating the relative speed of approach and the relative speed of separation.

#### Step 1: Conservation of momentum
Define right as positive (\(+\)).
Initial velocities: \(u_A = +2.0\,\mathrm{m\,s^{-1}}\), \(u_B = 0\,\mathrm{m\,s^{-1}}\).
Final velocities: \(v_A = +0.40\,\mathrm{m\,s^{-1}}\), \(v_B = +2.4\,\mathrm{m\,s^{-1}}\).

Total initial momentum:
\[
p_{\mathrm{initial}} = m_A u_A + m_B u_B = (0.60 \times 2.0) + (0.40 \times 0) = 1.20\,\mathrm{kg\,m\,s^{-1}}
\]

Total final momentum:
\[
p_{\mathrm{final}} = m_A v_A + m_B v_B = (0.60 \times 0.40) + (0.40 \times 2.4) = 0.24 + 0.96 = 1.20\,\mathrm{kg\,m\,s^{-1}}
\]

Because \(p_{\mathrm{initial}} = p_{\mathrm{final}} = 1.20\,\mathrm{kg\,m\,s^{-1}}\), linear momentum is conserved.

#### Step 2: Kinetic energy calculation
Calculate initial kinetic energy of the system:
\[
E_{K, \mathrm{initial}} = \frac{1}{2}m_A u_A^2 + \frac{1}{2}m_B u_B^2 = \frac{1}{2}(0.60)(2.0)^2 + 0 = 0.30 \times 4.0 = 1.20\,\mathrm{J}
\]

Calculate final kinetic energy of each glider:
\[
E_{K, A, \mathrm{final}} = \frac{1}{2}m_A v_A^2 = \frac{1}{2}(0.60)(0.40)^2 = 0.30 \times 0.16 = 0.048\,\mathrm{J}
\]
\[
E_{K, B, \mathrm{final}} = \frac{1}{2}m_B v_B^2 = \frac{1}{2}(0.40)(2.4)^2 = 0.20 \times 5.76 = 1.152\,\mathrm{J}
\]

Total final kinetic energy:
\[
E_{K, \mathrm{final}} = 0.048\,\mathrm{J} + 1.152\,\mathrm{J} = 1.20\,\mathrm{J}
\]

Comparing initial and final values:
\[
E_{K, \mathrm{initial}} = E_{K, \mathrm{final}} = 1.20\,\mathrm{J}
\]
Because the total kinetic energy of the system is the same before and after the collision, the collision is **perfectly elastic**.

#### Step 3: Relative speed verification
Relative speed of approach:
\[
u_{\mathrm{approach}} = u_A - u_B = 2.0\,\mathrm{m\,s^{-1}} - 0\,\mathrm{m\,s^{-1}} = 2.0\,\mathrm{m\,s^{-1}}
\]

Relative speed of separation:
\[
v_{\mathrm{separation}} = v_B - v_A = 2.4\,\mathrm{m\,s^{-1}} - 0.40\,\mathrm{m\,s^{-1}} = 2.0\,\mathrm{m\,s^{-1}}
\]

Because the relative speed of approach equals the relative speed of separation (\(2.0\,\mathrm{m\,s^{-1}} = 2.0\,\mathrm{m\,s^{-1}}\)), this independently confirms that the collision is elastic.

**Answer:**
1. Initial momentum equals final momentum (\(1.20\,\mathrm{kg\,m\,s^{-1}}\)), so momentum is conserved.
2. Initial kinetic energy (\(1.2\,\mathrm{J}\)) equals final kinetic energy (\(1.2\,\mathrm{J}\)); the collision is **elastic**.
3. Relative speed of approach equals relative speed of separation (\(2.0\,\mathrm{m\,s^{-1}}\)), confirming the collision is elastic.

---

### Worked example 2: Finding unknown post-collision velocities

Two pucks on an air hockey table collide head-on. The collision is known to be perfectly elastic.

Puck 1 has a mass of \(0.20\,\mathrm{kg}\) and an initial velocity of \(3.0\,\mathrm{m\,s^{-1}}\) to the right. 
Puck 2 has a mass of \(0.30\,\mathrm{kg}\) and an initial velocity of \(2.0\,\mathrm{m\,s^{-1}}\) to the left.

Determine the velocity of each puck after the collision.

```
Before collision:
  [ Puck 1 (0.20 kg) ] --> +3.0 m s^-1          <-- -2.0 m s^-1 [ Puck 2 (0.30 kg) ]
```

#### Strategy
We have two unknown final velocities, \(v_1\) and \(v_2\).
To find two unknowns, we need two independent equations:
1. Conservation of linear momentum: \(m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2\)
2. Relative speed in elastic collision: \(u_1 - u_2 = v_2 - v_1\)

Solve the two linear equations simultaneously.

#### Step 1: Set up the conservation of momentum equation
Define the direction to the right as positive (\(+\)).
- \(m_1 = 0.20\,\mathrm{kg}\), \(u_1 = +3.0\,\mathrm{m\,s^{-1}}\)
- \(m_2 = 0.30\,\mathrm{kg}\), \(u_2 = -2.0\,\mathrm{m\,s^{-1}}\)

Total initial momentum:
\[
p_{\mathrm{initial}} = (0.20 \times +3.0) + (0.30 \times -2.0) = +0.60 - 0.60 = 0\,\mathrm{kg\,m\,s^{-1}}
\]

Total final momentum:
\[
p_{\mathrm{final}} = m_1 v_1 + m_2 v_2 = 0.20 v_1 + 0.30 v_2
\]

Equating initial and final momentum:
\[
0.20 v_1 + 0.30 v_2 = 0 \implies 2 v_1 + 3 v_2 = 0
\]
\[
v_1 = -1.5 v_2 \quad \text{--- (Equation 1)}
\]

#### Step 2: Set up the relative speed equation
For a perfectly elastic collision:
\[
u_1 - u_2 = v_2 - v_1
\]

Substitute the signed initial velocities:
\[
(+3.0) - (-2.0) = v_2 - v_1
\]
\[
5.0 = v_2 - v_1 \implies v_2 - v_1 = 5.0 \quad \text{--- (Equation 2)}
\]

#### Step 3: Solve the simultaneous equations
Substitute Equation 1 (\(v_1 = -1.5 v_2\)) into Equation 2:
\[
v_2 - (-1.5 v_2) = 5.0
\]
\[
v_2 + 1.5 v_2 = 5.0
\]
\[
2.5 v_2 = 5.0 \implies v_2 = \frac{5.0}{2.5} = +2.0\,\mathrm{m\,s^{-1}}
\]

Now find \(v_1\) using Equation 1:
\[
v_1 = -1.5 \times (+2.0) = -3.0\,\mathrm{m\,s^{-1}}
\]

#### Step 4: Verify the solution
- **Check momentum:** \(p_{\mathrm{final}} = 0.20(-3.0) + 0.30(+2.0) = -0.60 + 0.60 = 0\,\mathrm{kg\,m\,s^{-1}}\). (Matches!)
- **Check relative speed:** \(v_2 - v_1 = (+2.0) - (-3.0) = 5.0\,\mathrm{m\,s^{-1}}\). (Matches approach speed of \(5.0\,\mathrm{m\,s^{-1}}\)!)
- **Check kinetic energy:**
  - \(E_{K, \mathrm{initial}} = \frac{1}{2}(0.20)(3.0)^2 + \frac{1}{2}(0.30)(2.0)^2 = 0.90 + 0.60 = 1.50\,\mathrm{J}\)
  - \(E_{K, \mathrm{final}} = \frac{1}{2}(0.20)(-3.0)^2 + \frac{1}{2}(0.30)(2.0)^2 = 0.90 + 0.60 = 1.50\,\mathrm{J}\)
  The kinetic energy is perfectly conserved.

**Answer:**
- Velocity of puck 1 after the collision is **\(3.0\,\mathrm{m\,s^{-1}}\) to the left** (\(-3.0\,\mathrm{m\,s^{-1}}\)).
- Velocity of puck 2 after the collision is **\(2.0\,\mathrm{m\,s^{-1}}\) to the right** (\(+2.0\,\mathrm{m\,s^{-1}}\)).

---

### Worked example 3: Inelastic shunter impact and kinetic energy loss

A railway goods wagon of mass \(15\,000\,\mathrm{kg}\) travels along a level track at \(2.0\,\mathrm{m\,s^{-1}}\) to the right. It collides with a stationary loaded wagon of mass \(25\,000\,\mathrm{kg}\). 

The coupling locks the wagons together automatically so that they roll forward as a single combined train.

Calculate:
1. The common velocity of the coupled wagons after impact.
2. The total kinetic energy before the collision.
3. The total kinetic energy after the collision.
4. The loss of kinetic energy, and state what has happened to this energy.

#### Step 1: Common velocity after collision
Take right as positive.
- \(m_1 = 15\,000\,\mathrm{kg}\), \(u_1 = +2.0\,\mathrm{m\,s^{-1}}\)
- \(m_2 = 25\,000\,\mathrm{kg}\), \(u_2 = 0\,\mathrm{m\,s^{-1}}\)

By conservation of linear momentum:
\[
m_1 u_1 + m_2 u_2 = (m_1 + m_2)V
\]
\[
(15\,000 \times 2.0) + 0 = (15\,000 + 25\,000)V
\]
\[
30\,000 = 40\,000 V
\]
\[
V = \frac{30\,000}{40\,000} = +0.75\,\mathrm{m\,s^{-1}}
\]

The coupled wagons move to the right at \(0.75\,\mathrm{m\,s^{-1}}\).

#### Step 2: Initial kinetic energy
Only wagon 1 is moving initially:
\[
E_{K, \mathrm{initial}} = \frac{1}{2}m_1 u_1^2 = \frac{1}{2} \times 15\,000\,\mathrm{kg} \times (2.0\,\mathrm{m\,s^{-1}})^2 = 7500 \times 4.0 = 30\,000\,\mathrm{J} = 30\,\mathrm{kJ}
\]

#### Step 3: Final kinetic energy
Both wagons move together at \(0.75\,\mathrm{m\,s^{-1}}\):
\[
E_{K, \mathrm{final}} = \frac{1}{2}(m_1 + m_2)V^2 = \frac{1}{2} \times 40\,000\,\mathrm{kg} \times (0.75\,\mathrm{m\,s^{-1}})^2 = 20\,000 \times 0.5625 = 11\,250\,\mathrm{J} = 11.25\,\mathrm{kJ}
\]

To two significant figures, this is \(11\,\mathrm{kJ}\).

#### Step 4: Kinetic energy loss and energy destination
\[
\Delta E_K = E_{K, \mathrm{initial}} - E_{K, \mathrm{final}} = 30\,000\,\mathrm{J} - 11\,250\,\mathrm{J} = 18\,750\,\mathrm{J} \approx 19\,\mathrm{kJ}
\]

Percentage of initial kinetic energy lost:
\[
\frac{18\,750}{30\,000} \times 100\% = 62.5\%
\]

Over \(60\%\) of the original kinetic energy has been lost!

**Where did the energy go?**
The missing \(18.8\,\mathrm{kJ}\) of kinetic energy was converted into:
- Internal energy (thermal energy), heating the metal buffers, wheels, and coupling springs.
- Acoustic wave energy (sound), heard as the loud mechanical clang of impact.
- Microscopic permanent deformation of the contacting metal surfaces.

Total energy in the universe remains strictly conserved.

**Answer:**
1. Common velocity is **\(0.75\,\mathrm{m\,s^{-1}}\) to the right**.
2. Initial kinetic energy is **\(30\,\mathrm{kJ}\)** (\(30\,000\,\mathrm{J}\)).
3. Final kinetic energy is **\(11\,\mathrm{kJ}\)** (\(11\,250\,\mathrm{J}\)).
4. Loss in kinetic energy is **\(19\,\mathrm{kJ}\)** (\(18\,750\,\mathrm{J}\)), transformed into thermal energy, sound, and deformation.

---

## Active learning checks

### Check 1: Comparing momentum and kinetic energy conservation

In an isolated system, two rubber balls collide and bounce off each other. The collision is known to be inelastic.

Which row correctly describes what happens to the total momentum and the total kinetic energy of the balls?

- **A.** Total momentum is conserved, but total kinetic energy decreases.
- **B.** Both total momentum and total kinetic energy decrease.

**Feedback for A:** Correct. In any isolated system with no resultant external force, the total linear momentum is **always conserved**, regardless of whether the collision is elastic or inelastic. In an inelastic collision, some kinetic energy is converted into thermal and sound energy, so total kinetic energy decreases.

**Feedback for B:** Incorrect. Momentum is not lost in an inelastic collision. Provided there is no resultant external force, momentum is strictly conserved. Only kinetic energy changes.

### Check 2: Relative speed in a head-on collision

Ball P travels to the right at \(6.0\,\mathrm{m\,s^{-1}}\) towards ball Q, which travels to the left at \(4.0\,\mathrm{m\,s^{-1}}\). The balls undergo a perfectly elastic head-on collision. After the collision, ball P rebounds to the left at \(2.0\,\mathrm{m\,s^{-1}}\).

What is the velocity of ball Q after the collision?

- **A.** \(8.0\,\mathrm{m\,s^{-1}}\) to the right
- **B.** \(4.0\,\mathrm{m\,s^{-1}}\) to the right

**Feedback for A:** Correct. First find the relative speed of approach: because the balls travel towards each other, their closing speed is \(6.0 - (-4.0) = 10.0\,\mathrm{m\,s^{-1}}\). For a perfectly elastic collision, the relative speed of separation must also equal \(10.0\,\mathrm{m\,s^{-1}}\). After impact, ball P moves left with velocity \(v_P = -2.0\,\mathrm{m\,s^{-1}}\). Using the formula \(u_P - u_Q = v_Q - v_P\): \(10.0 = v_Q - (-2.0) \implies v_Q + 2.0 = 10.0 \implies v_Q = +8.0\,\mathrm{m\,s^{-1}}\) (to the right).

**Feedback for B:** Incorrect. If ball Q moved at \(4.0\,\mathrm{m\,s^{-1}}\) to the right while ball P moved at \(2.0\,\mathrm{m\,s^{-1}}\) to the left, their speed of separation would be \(4.0 - (-2.0) = 6.0\,\mathrm{m\,s^{-1}}\), which is less than the approach speed of \(10.0\,\mathrm{m\,s^{-1}}\). That would correspond to an inelastic collision, not a perfectly elastic one.

### Check 3: Collision of equal masses

Two identical steel pucks, A and B, of mass \(m = 0.50\,\mathrm{kg}\) slide on a horizontal frictionless ice rink. Puck A has a velocity of \(+4.0\,\mathrm{m\,s^{-1}}\) along a straight line, while puck B is at rest (\(u_B = 0\)). The pucks make a perfectly elastic head-on collision.

What are the velocities of puck A and puck B after the collision?

- **A.** Puck A comes to rest (\(v_A = 0\)) and puck B moves forward at \(+4.0\,\mathrm{m\,s^{-1}}\).
- **B.** Both pucks move forward together at \(+2.0\,\mathrm{m\,s^{-1}}\).

**Feedback for A:** Correct. When two equal masses collide elastically in one dimension, they completely exchange their velocities: \(v_A = u_B = 0\) and \(v_B = u_A = +4.0\,\mathrm{m\,s^{-1}}\). Momentum is conserved (\(0.50 \times 4.0 = 0.50 \times 4.0 = 2.0\,\mathrm{kg\,m\,s^{-1}}\)), and kinetic energy is conserved (\(\frac{1}{2} \times 0.50 \times 4.0^2 = 4.0\,\mathrm{J}\) before and after).

**Feedback for B:** Incorrect. Moving forward together at \(+2.0\,\mathrm{m\,s^{-1}}\) conserves momentum (\((0.50 + 0.50) \times 2.0 = 2.0\,\mathrm{kg\,m\,s^{-1}}\)), but represents a completely inelastic collision where they stick together! In that case, final kinetic energy would be \(\frac{1}{2}(1.00)(2.0)^2 = 2.0\,\mathrm{J}\), losing half of the original \(4.0\,\mathrm{J}\). For an elastic collision, they must separate with equal relative speed.

### Check 4: The law of conservation of energy in a car crash

A student is asked why a car crash is described as inelastic even though physics teachers say energy can never be created or destroyed.

Which explanation is scientifically accurate?

- **A.** The collision is inelastic because kinetic energy alone is not conserved, having been converted into thermal energy, sound, and deformation of the car bodies; total energy is fully conserved.
- **B.** The collision is inelastic because energy is destroyed when the metal crumbles and breaks under high impact force.

**Feedback for A:** Correct. Energy is never destroyed. Inelastic means only that **kinetic energy** decreases. The missing mechanical energy is accounted for by the thermal energy of the crumpled metal, sound waves radiated into the surroundings, and microscopic work done in permanently deforming the molecular lattice of the vehicle structure.

**Feedback for B:** Incorrect. Energy cannot be destroyed under any circumstances. Chemical, mechanical, and thermal energies change forms, but the total energy of an isolated system always remains constant.

---

## Mistakes worth repairing

### Mistake 1: Believing momentum is only conserved in elastic collisions
This is the single most persistent misconception in Dynamics. Many students mistakenly write: "Momentum was not conserved because the collision was inelastic."
- **Momentum is ALWAYS conserved** in any collision (elastic or inelastic), provided the system has no resultant external force.
- It is **kinetic energy** that is conserved only in elastic collisions.

### Mistake 2: Confusing conservation of kinetic energy with conservation of total energy
Students frequently confuse \(E_K\) with total energy \(E\):
- **Total energy** is universally conserved in all physical processes without exception.
- **Kinetic energy** is a specific mechanical form of energy that can be converted into heat, sound, or chemical energy. An inelastic collision conserves total energy while losing kinetic energy.

### Mistake 3: Subtracting speeds when finding relative speed of approach for head-on collisions
When two objects move towards each other, students sometimes subtract their speed numbers (e.g. \(5 - 3 = 2\,\mathrm{m\,s^{-1}}\)).
- If object 1 moves right at \(5\,\mathrm{m\,s^{-1}}\) and object 2 moves left at \(3\,\mathrm{m\,s^{-1}}\), the distance between them shrinks by \(5\) metres each second from object 1 and \(3\) metres each second from object 2. The closing speed is \(5 + 3 = 8\,\mathrm{m\,s^{-1}}\).
- Using algebraic velocities with signs: \(u_1 - u_2 = (+5) - (-3) = 8\,\mathrm{m\,s^{-1}}\). Always check that your answer makes physical sense!

### Mistake 4: Assuming "elastic" means stretchy or made of rubber
In everyday conversation, "elastic" refers to materials like rubber bands or bungee cords that stretch easily.
- In physics, an **elastic collision** is defined strictly by the conservation of kinetic energy.
- Real rubber balls are actually somewhat inelastic: when dropped, a rubber squash ball warms up noticeably after repeated impacts because internal friction dissipates kinetic energy into heat.

### Mistake 5: Neglecting the relative speed shortcut
When tasked with finding unknown velocities after an elastic collision, students often set up the kinetic energy equation \(\frac{1}{2}m_1 u_1^2 + \frac{1}{2}m_2 u_2^2 = \frac{1}{2}m_1 v_1^2 + \frac{1}{2}m_2 v_2^2\), leading to quadratic equations with multiple roots and high risk of sign errors.
- Always combine linear momentum with the linear relative speed condition:
  \[
  u_1 - u_2 = v_2 - v_1
  \]
- This creates a system of two simple linear equations that can be solved in a few steps.

---

## Core recap

- An **elastic collision** is:
  > a collision in which the total kinetic energy of the system is the same before and after the collision
  \[
  \Sigma E_{K, \mathrm{initial}} = \Sigma E_{K, \mathrm{final}}
  \]
- In an **inelastic collision**, total kinetic energy is not conserved (\(\Sigma E_{K, \mathrm{final}} < \Sigma E_{K, \mathrm{initial}}\)). Some kinetic energy transforms into internal thermal energy, sound, and work done in deformation.
- A **completely inelastic collision** occurs when colliding bodies coalesce (stick together); this produces the maximum possible loss of kinetic energy consistent with momentum conservation.
- The **law of conservation of energy** holds in all collisions: total energy remains constant even when kinetic energy decreases.
- For any one-dimensional elastic collision:
  \[
  u_1 - u_2 = v_2 - v_1
  \]
  The **relative speed of approach** equals the **relative speed of separation**.
- For an inelastic collision, the relative speed of separation is less than the relative speed of approach; if the bodies stick together, the relative speed of separation is zero.
- When two bodies of **equal mass** collide elastically in one dimension, they **exchange velocities**:
  \[
  v_1 = u_2 \quad \text{and} \quad v_2 = u_1
  \]
- To find two unknown post-collision velocities in an elastic collision, solve the linear momentum equation simultaneously with the relative speed equation.
