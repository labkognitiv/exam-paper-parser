# The Basic Assumptions of the Kinetic Theory of Gases

## Learning Outcomes

In this lesson, you will learn to:
- State the basic assumptions of the kinetic theory of gases (Cambridge outcome `9702_t15_m03_o01`).
- Explain how molecular movement causes the pressure exerted by a gas, using ideas of momentum and Newton's laws of motion (Cambridge outcome `9702_t15_m03_o02`).
- Derive and use the kinetic theory relationship:
  \[
  pV = \frac{1}{3}Nm\langle c^2\rangle
  \]
  where $\langle c^2\rangle$ is the mean-square speed, using a one-dimensional collision model extended to three dimensions via $\langle c_x^2\rangle = \frac{1}{3}\langle c^2\rangle$ (Cambridge outcome `9702_t15_m03_o02`).
- Express and apply the kinetic theory equation in terms of gas density $\rho$:
  \[
  p = \frac{1}{3}\rho\langle c^2\rangle
  \]

---

## Prior Knowledge

Before beginning this lesson, you should be familiar with:
- **The macroscopic ideal gas equation:** $pV = nRT$ and $pV = NkT$, where $p$ is pressure in pascals ($\text{Pa}$), $V$ is volume in cubic metres ($\text{m}^3$), $n$ is amount of substance in moles ($\text{mol}$), $N$ is the number of molecules, and $T$ is thermodynamic temperature in kelvin ($\text{K}$).
- **Newton's second law of motion:** Resultant force is the rate of change of momentum:
  \[
  F = \frac{\Delta p}{\Delta t}
  \]
- **Newton's third law of motion:** When body A exerts a force on body B, body B exerts an equal and opposite force on body A.
- **Linear momentum:** The product of mass and velocity, $p = mv$, which is a vector quantity.
- **Elastic collisions:** A collision in which total kinetic energy is conserved (no kinetic energy is converted into internal thermal energy or other forms).

---

## Core Concepts

### Macroscopic Observations Versus Microscopic Reality

When you inflate a bicycle tyre or heat air inside a sealed flask, you observe macroscopic properties: pressure $p$, volume $V$, and temperature $T$. A pressure gauge registers a smooth, steady force per unit area on the container wall.

However, matter is not continuous. A gas consists of billions of trillions of individual sub-microscopic particles (atoms or molecules) in rapid, random motion. The smooth pressure registered by a pressure gauge is the cumulative result of countless rapid collisions between these tiny particles and the walls of the container.

To bridge the macroscopic world of thermodynamics and the microscopic world of particles, physicists developed the **kinetic theory of gases**.

---

### The Basic Assumptions of the Kinetic Theory of Gases

To build a workable mathematical model of a gas, we make several idealised assumptions about the molecules and their interactions. In Cambridge International A Level Physics, you are required to recall and explain these fundamental assumptions.

1. **Continuous random motion:**
   The gas consists of a very large number of identical particles (atoms or molecules) moving in continuous, rapid, random motion with a range of speeds and directions.
   - *Exam insight:* "Random" means there is no preferred direction of motion; particles travel in straight lines between collisions, colliding with equal probability in all directions.

2. **Negligible molecular volume:**
   The total volume occupied by the gas molecules themselves is negligible compared with the volume of the containing vessel (or the volume occupied by the gas).
   - *Physical meaning:* Most of a gas is empty space. The molecules can be treated as point masses.

3. **No intermolecular forces except during collisions:**
   There are no forces of attraction or repulsion between the molecules, except during collisions.
   - *Critical deduction:* Because there are no intermolecular forces between collisions, the molecules possess **zero potential energy**. The entire internal energy of an ideal gas consists purely of the kinetic energy of its particles.

4. **Perfectly elastic collisions:**
   All collisions between molecules, and between molecules and the container walls, are perfectly elastic.
   - *Physical meaning:* There is no loss of total kinetic energy during collisions. If collisions were inelastic, the particles would gradually lose kinetic energy, slow down, and the gas would cool down spontaneously.

5. **Negligible duration of collisions:**
   The time spent during a collision is negligible compared with the time between collisions.
   - *Physical meaning:* A particle spends almost all its time moving freely at constant velocity in straight paths, rather than interacting.

6. **Negligible gravitational forces:**
   Gravitational forces between molecules, and on the molecules themselves, are negligible compared with the forces exerted during collisions.

---

### How Molecular Movement Causes Gas Pressure

Pressure is defined as normal force per unit area:
\[
p = \frac{F}{A}
\]

How does a collection of moving particles exert a continuous force on a container wall? The answer lies in momentum changes during collisions:

1. **Collisions with the wall:**
   Molecules move randomly throughout the container. A vast number of molecules strike every unit area of the wall each second.

2. **Change in momentum:**
   When a molecule of mass $m$ strikes a rigid wall perpendicularly with velocity $+u$ and rebounds elastically with velocity $-u$, its velocity changes by:
   \[
   \Delta u = (-u) - (+u) = -2u
   \]
   The change in momentum of the molecule is therefore:
   \[
   \Delta p = m\Delta u = -2mu
   \]
   The magnitude of the momentum change experienced by the molecule is $2mu$.

3. **Force exerted by the wall on the molecule:**
   By Newton's second law of motion, the wall must exert a normal force on the molecule to produce this rate of change of momentum:
   \[
   F_{\text{wall on molecule}} = \frac{\Delta p}{\Delta t}
   \]

4. **Force exerted by the molecule on the wall:**
   By Newton's third law of motion, the molecule exerts an equal and opposite force on the wall:
   \[
   F_{\text{molecule on wall}} = -F_{\text{wall on molecule}}
   \]
   The direction of this force is outward, perpendicular to the wall.

5. **Cumulative steady pressure:**
   Although each individual impact delivers a brief impulsive force, there are billions of collisions occurring every second across every square centimetre of wall area. These individual impacts overlap in time to create a smooth, steady, measurable average force $F_{\text{total}}$ distributed over the wall area $A$, resulting in gas pressure $p = \frac{F_{\text{total}}}{A}$.

---

## Detailed Derivations

### Derivation of the Kinetic Theory Pressure Equation: $pV = \frac{1}{3}Nm\langle c^2\rangle$

We now derive the fundamental equation of kinetic theory by considering a simple one-dimensional model and extending it to three dimensions.

<a id="formula-9702_formula_kinetic_theory_pressure"></a>

> **Formula to learn: Kinetic theory pressure equation.**
>
> \[
> pV = \frac{1}{3}Nm\langle c^2\rangle
> \]

#### Step 1: Geometry and initial conditions
Consider a cubic container with edges of length $L$, so its volume is:
\[
V = L^3
\]
The area of each face is:
\[
A = L^2
\]
Inside the box are $N$ identical gas molecules, each having mass $m$.

#### Step 2: One-dimensional motion of a single molecule
Consider one molecule, labelled molecule 1, moving with a velocity vector $\vec{c}_1$. Let the component of its velocity perpendicular to a chosen face (say, the shaded face perpendicular to the $x$-axis) be $u_1$.

The molecule moves towards the shaded face with velocity $+u_1$. When it collides elastically with the face, it rebounds with velocity $-u_1$.

The change in momentum of molecule 1 is:
\[
\Delta p_1 = \text{final momentum} - \text{initial momentum} = (-m u_1) - (+m u_1) = -2m u_1
\]

The magnitude of the momentum transferred to the shaded face in this single collision is:
\[
|\Delta p| = 2m u_1
\]

#### Step 3: Time between consecutive collisions
After rebounding from the shaded face, the molecule must travel all the way across the box to the opposite face (a distance $L$), rebound there, and travel back to the shaded face (another distance $L$).

The total distance travelled parallel to the $x$-axis between consecutive collisions with the shaded face is:
\[
\Delta x = 2L
\]

Because the speed $u_1$ along the $x$-axis remains constant between collisions, the time interval $\Delta t$ between consecutive impacts with the shaded face is:
\[
\Delta t = \frac{2L}{u_1}
\]

#### Step 4: Average force exerted by one molecule on the face
The number of collisions per unit time on the shaded face is:
\[
\text{collision frequency} = \frac{1}{\Delta t} = \frac{u_1}{2L}
\]

By Newton's second law, the average force $F_1$ exerted on the face by this single molecule is the rate of momentum transfer:
\[
F_1 = \frac{\text{momentum change per collision}}{\text{time between collisions}} = \frac{2m u_1}{\frac{2L}{u_1}} = \frac{2m u_1^2}{2L} = \frac{m u_1^2}{L}
\]

#### Step 5: Total force exerted by all $N$ molecules in one dimension
The container contains $N$ molecules, each with its own $x$-component of velocity: $u_1, u_2, u_3, \dots, u_N$.

Because the molecules do not interact except during instantaneous collisions, each molecule contributes independently to the force on the shaded face.

The total normal force $F_x$ on the face is the sum of the individual forces:
\[
F_x = F_1 + F_2 + \dots + F_N = \frac{m}{L} (u_1^2 + u_2^2 + \dots + u_N^2)
\]

We define the **mean-square speed in the $x$-direction**, denoted $\langle u^2\rangle$ or $\langle c_x^2\rangle$, as the average of the squares of the $x$-component velocities:
\[
\langle c_x^2\rangle = \frac{u_1^2 + u_2^2 + \dots + u_N^2}{N}
\]

Rearranging gives:
\[
u_1^2 + u_2^2 + \dots + u_N^2 = N\langle c_x^2\rangle
\]

Substituting this into the expression for total force:
\[
F_x = \frac{m}{L} \times N\langle c_x^2\rangle = \frac{Nm\langle c_x^2\rangle}{L}
\]

#### Step 6: Pressure on the face
The pressure $p$ exerted on the shaded face of area $A = L^2$ is:
\[
p = \frac{F_x}{A} = \frac{\frac{Nm\langle c_x^2\rangle}{L}}{L^2} = \frac{Nm\langle c_x^2\rangle}{L^3}
\]

Because the volume of the cube is $V = L^3$, this becomes:
\[
p = \frac{Nm\langle c_x^2\rangle}{V}
\]

#### Step 7: Extension from one dimension to three dimensions
In reality, molecules move in three dimensions. For any individual molecule, its three-dimensional speed $c$ is related to its rectangular components $(c_x, c_y, c_z)$ by Pythagoras' theorem:
\[
c^2 = c_x^2 + c_y^2 + c_z^2
\]

Averaging over all $N$ molecules in the gas:
\[
\langle c^2\rangle = \langle c_x^2\rangle + \langle c_y^2\rangle + \langle c_z^2\rangle
\]

Because the motion of the molecules is completely random, there is no preferred direction in space. The average squared velocity component is identical along all three Cartesian axes:
\[
\langle c_x^2\rangle = \langle c_y^2\rangle = \langle c_z^2\rangle
\]

Therefore:
\[
\langle c^2\rangle = 3\langle c_x^2\rangle \implies \langle c_x^2\rangle = \frac{1}{3}\langle c^2\rangle
\]

#### Step 8: Final kinetic theory equation
Substitute $\langle c_x^2\rangle = \frac{1}{3}\langle c^2\rangle$ into the pressure equation:
\[
p = \frac{Nm(\frac{1}{3}\langle c^2\rangle)}{V} = \frac{1}{3}\frac{Nm\langle c^2\rangle}{V}
\]

Multiplying both sides by the volume $V$ yields the standard Cambridge relationship:
\[
pV = \frac{1}{3}Nm\langle c^2\rangle
\]

---

### Definition and Meaning of Symbols

In the equation $pV = \frac{1}{3}Nm\langle c^2\rangle$:
- **$p$:** Pressure of the gas in pascals ($\text{Pa}$ or $\text{N m}^{-2}$).
- **$V$:** Volume of the gas in cubic metres ($\text{m}^3$).
- **$N$:** Total number of gas molecules (dimensionless quantity).
- **$m$:** Mass of one individual molecule in kilograms ($\text{kg}$).
- **$Nm$:** Total mass of the gas sample in kilograms ($\text{kg}$).
- **$\langle c^2\rangle$:** Mean-square speed of the gas molecules in metres squared per second squared ($\text{m}^2\text{ s}^{-2}$). This is the mean (average) of the squares of the speeds of all the molecules.

---

### Density Form of the Kinetic Theory Equation

Notice that the total mass of the gas sample is:
\[
M_{\text{total}} = Nm
\]
The density $\rho$ of the gas is total mass divided by volume:
\[
\rho = \frac{Nm}{V}
\]

We can rearrange the kinetic theory equation:
\[
p = \frac{1}{3}\left(\frac{Nm}{V}\right)\langle c^2\rangle
\]
Substituting $\rho = \frac{Nm}{V}$:
\[
p = \frac{1}{3}\rho\langle c^2\rangle
\]

This form is especially convenient when the density of the gas is known or when comparing gases under identical pressure conditions.

---

## Worked Examples with Cambridge Mark Schemes

### Worked Example 1: Explaining Gas Pressure and Molecular Collision Mechanics

A cubical vessel of side length $0.20\text{ m}$ contains helium gas. A helium atom of mass $6.6 \times 10^{-27}\text{ kg}$ travels horizontally with a velocity of $850\text{ m s}^{-1}$ perpendicular to one of the vertical walls. It collides elastically with the wall.

1. State two assumptions of the kinetic theory of gases that apply to this collision. [2 marks]
2. Calculate the magnitude of the momentum change of the atom during the collision. [1 mark]
3. Calculate the time between consecutive collisions of this atom with the same wall. [1 mark]
4. Calculate the average force exerted by this single atom on the wall. [1 mark]
5. Explain how the collisions of a large number of such atoms produce a constant pressure on the wall. [3 marks]

#### Model and Strategy Check
- Elastic collision means speed is unchanged upon rebound ($u_{\text{final}} = -850\text{ m s}^{-1}$).
- Motion parallel to the perpendicular axis covers distance $2L = 2 \times 0.20\text{ m} = 0.40\text{ m}$ between consecutive hits on the same wall.
- Average force is $\frac{\Delta p}{\Delta t}$.

#### Solutions and Mark Scheme Breakdown

**Part 1: Basic assumptions**
- Assumption 1: Collisions between the atom and the wall are perfectly elastic (no loss of kinetic energy). [B1]
- Assumption 2: The duration of the collision is negligible compared with the time between collisions (or: forces between particles are zero except during collisions). [B1]

**Part 2: Momentum change**
Initial momentum $p_i = m u = (6.6 \times 10^{-27}\text{ kg}) \times (+850\text{ m s}^{-1}) = +5.61 \times 10^{-24}\text{ kg m s}^{-1}$.
Final momentum after elastic rebound $p_f = -5.61 \times 10^{-24}\text{ kg m s}^{-1}$.
\[
\Delta p = p_f - p_i = -5.61 \times 10^{-24} - (+5.61 \times 10^{-24}) = -1.12 \times 10^{-23}\text{ kg m s}^{-1}
\]
Magnitude of momentum change:
\[
|\Delta p| = 2mu = 2 \times (6.6 \times 10^{-27}) \times 850 = 1.1 \times 10^{-23}\text{ kg m s}^{-1} \text{ [A1]}
\]

**Part 3: Time between consecutive collisions**
Distance travelled between collisions on the same wall:
\[
\Delta x = 2L = 2 \times 0.20\text{ m} = 0.40\text{ m}
\]
\[
\Delta t = \frac{2L}{u} = \frac{0.40\text{ m}}{850\text{ m s}^{-1}} = 4.71 \times 10^{-4}\text{ s} \text{ [A1]}
\]

**Part 4: Average force from this single atom**
\[
F = \frac{|\Delta p|}{\Delta t} = \frac{1.122 \times 10^{-23}\text{ kg m s}^{-1}}{4.706 \times 10^{-4}\text{ s}} = 2.38 \times 10^{-20}\text{ N} \approx 2.4 \times 10^{-20}\text{ N} \text{ [A1]}
\]
*(Check: $\frac{mu^2}{L} = \frac{6.6 \times 10^{-27} \times 850^2}{0.20} = 2.38 \times 10^{-20}\text{ N}$. Consistent!)*

**Part 5: Explanation of constant pressure**
- Many molecules are in continuous random motion and collide with the wall. [B1]
- Each collision involves a change in momentum, producing a force on the wall by Newton's second and third laws. [B1]
- The immense frequency of collisions distributed evenly over the surface area produces a steady, macroscopic average force per unit area, which is pressure ($p = F/A$). [B1]

---

### Worked Example 2: Quantitative Calculations Using Kinetic Theory

A rigid container of volume $0.060\text{ m}^3$ holds $1.50 \times 10^{24}$ molecules of an ideal diatomic gas at a pressure of $2.20 \times 10^5\text{ Pa}$. The mass of one molecule of the gas is $4.65 \times 10^{-26}\text{ kg}$.

1. Calculate the density of the gas in the container. [2 marks]
2. Calculate the mean-square speed $\langle c^2\rangle$ of the molecules. [2 marks]

#### Strategy and Model Check
- Find total mass $M_{\text{total}} = Nm$.
- Find density $\rho = M_{\text{total}} / V$.
- Apply $p = \frac{1}{3}\rho\langle c^2\rangle$ or $pV = \frac{1}{3}Nm\langle c^2\rangle$ to find $\langle c^2\rangle$.
- Units check: $\text{Pa} = \text{N m}^{-2} = \text{kg m}^{-1}\text{ s}^{-2}$, so $\langle c^2\rangle$ must have units $\text{m}^2\text{ s}^{-2}$.

#### Step 1: Calculate the density of the gas
Total mass of gas:
\[
M_{\text{total}} = Nm = (1.50 \times 10^{24}) \times (4.65 \times 10^{-26}\text{ kg}) = 0.06975\text{ kg}
\]
Density:
\[
\rho = \frac{M_{\text{total}}}{V} = \frac{0.06975\text{ kg}}{0.060\text{ m}^3} = 1.1625\text{ kg m}^{-3} \approx 1.16\text{ kg m}^{-3}
\]
- Correct calculation of total mass $M_{\text{total}}$ [C1]
- Final answer $\rho = 1.16\text{ kg m}^{-3}$ (or $1.2\text{ kg m}^{-3}$ to 2 s.f.) [A1]

#### Step 2: Calculate the mean-square speed $\langle c^2\rangle$
Rearrange the kinetic theory equation for $\langle c^2\rangle$:
\[
pV = \frac{1}{3}Nm\langle c^2\rangle \implies \langle c^2\rangle = \frac{3pV}{Nm} = \frac{3p}{\rho}
\]
Substitute values:
\[
\langle c^2\rangle = \frac{3 \times (2.20 \times 10^5\text{ Pa})}{1.1625\text{ kg m}^{-3}} = \frac{6.60 \times 10^5}{1.1625} = 5.677 \times 10^5\text{ m}^2\text{ s}^{-2}
\]
To 3 significant figures:
\[
\langle c^2\rangle = 5.68 \times 10^5\text{ m}^2\text{ s}^{-2}
\]
- Correct substitution into rearranged formula [C1]
- Final answer $\langle c^2\rangle = 5.68 \times 10^5\text{ m}^2\text{ s}^{-2}$ (allow $5.7 \times 10^5\text{ m}^2\text{ s}^{-2}$) with correct units [A1]

#### Reasonableness check
- The square root of $\langle c^2\rangle$ would be $\sqrt{5.68 \times 10^5} \approx 754\text{ m s}^{-1}$, which is entirely realistic for gas molecules at room temperature.

---

### Worked Example 3: Evaluating the Negligible Volume Assumption

A cylinder contains $0.40\text{ mol}$ of argon gas in a volume of $9.8 \times 10^{-3}\text{ m}^3$ at a temperature of $295\text{ K}$.
Each argon atom may be modelled as a hard sphere of radius $r = 1.4 \times 10^{-10}\text{ m}$.

1. Calculate the total number of argon atoms in the cylinder. [1 mark]
2. Estimate the total volume occupied by the argon atoms themselves. [2 marks]
3. State the assumption of the kinetic theory of gases related to particle volume and explain whether your answer to part 2 is consistent with this assumption. [2 marks]

#### Strategy and Model Check
- Number of atoms $N = n N_A$, where $N_A = 6.02 \times 10^{23}\text{ mol}^{-1}$.
- Volume of one spherical atom $V_{\text{atom}} = \frac{4}{3}\pi r^3$.
- Total volume of atoms $V_{\text{atoms}} = N \times V_{\text{atom}}$.
- Compare $V_{\text{atoms}}$ with container volume $V = 9.8 \times 10^{-3}\text{ m}^3$.

#### Step 1: Calculate the number of atoms
\[
N = n N_A = 0.40\text{ mol} \times 6.02 \times 10^{23}\text{ mol}^{-1} = 2.41 \times 10^{23} \text{ atoms [A1]}
\]

#### Step 2: Estimate the volume occupied by the atoms
Volume of one spherical atom:
\[
V_{\text{atom}} = \frac{4}{3}\pi r^3 = \frac{4}{3} \times \pi \times (1.4 \times 10^{-10}\text{ m})^3 = \frac{4}{3}\pi \times 2.744 \times 10^{-30} = 1.149 \times 10^{-29}\text{ m}^3
\]
Total volume occupied by all atoms:
\[
V_{\text{atoms}} = N \times V_{\text{atom}} = (2.41 \times 10^{23}) \times (1.149 \times 10^{-29}\text{ m}^3) = 2.77 \times 10^{-6}\text{ m}^3 \approx 2.8 \times 10^{-6}\text{ m}^3
\]
- Formula $\frac{4}{3}\pi r^3$ and multiplication by $N$ [C1]
- Final answer $2.8 \times 10^{-6}\text{ m}^3$ (accept $2.7 \times 10^{-6}$ to $2.8 \times 10^{-6}\text{ m}^3$) [A1]

#### Step 3: Assumption and consistency check
- Assumption: The volume of the gas particles (atoms) is negligible compared with the volume of the containing vessel (or volume of the gas). [B1]
- Consistency explanation:
  \[
  \frac{V_{\text{atoms}}}{V_{\text{container}}} = \frac{2.77 \times 10^{-6}\text{ m}^3}{9.8 \times 10^{-3}\text{ m}^3} \approx 2.8 \times 10^{-4} = 0.028\%
  \]
  Because the atoms occupy less than $0.03\%$ of the container volume ($2.8 \times 10^{-6}\text{ m}^3 \ll 9.8 \times 10^{-3}\text{ m}^3$), the result is completely consistent with the assumption. [B1]

---

## Guided Practice

### Problem 1: Gas Pressure and Momentum Transfer
A stream of neon atoms of mass $m = 3.3 \times 10^{-26}\text{ kg}$, all travelling with speed $u = 600\text{ m s}^{-1}$ perpendicular to a flat plate of area $4.0 \times 10^{-4}\text{ m}^2$, strikes the plate elastically.
If $5.0 \times 10^{21}$ atoms hit the plate each second, calculate:
1. The momentum change of one neon atom upon collision.
2. The total force exerted on the plate.
3. The pressure exerted on the plate.

#### Worked Solution:
1. Since the collision is elastic:
   \[
   |\Delta p| = 2mu = 2 \times (3.3 \times 10^{-26}\text{ kg}) \times 600\text{ m s}^{-1} = 3.96 \times 10^{-23}\text{ kg m s}^{-1}
   \]
2. The rate of arrival of atoms is $\frac{\Delta N}{\Delta t} = 5.0 \times 10^{21}\text{ s}^{-1}$.
   The total rate of change of momentum (force on the plate) is:
   \[
   F = \left(\frac{\Delta N}{\Delta t}\right) \times |\Delta p| = (5.0 \times 10^{21}\text{ s}^{-1}) \times (3.96 \times 10^{-23}\text{ kg m s}^{-1}) = 0.198\text{ N} \approx 0.20\text{ N}
   \]
3. The pressure on the plate:
   \[
   p = \frac{F}{A} = \frac{0.198\text{ N}}{4.0 \times 10^{-4}\text{ m}^2} = 495\text{ Pa} \approx 5.0 \times 10^2\text{ Pa}
   \]

---

### Problem 2: Calculating Gas Density from Pressure and Mean-Square Speed
Air at atmospheric pressure ($1.01 \times 10^5\text{ Pa}$) has a mean-square molecular speed of $2.50 \times 10^5\text{ m}^2\text{ s}^{-2}$.
Calculate the density of air under these conditions.

#### Worked Solution:
From the density form of the kinetic theory equation:
\[
p = \frac{1}{3}\rho\langle c^2\rangle
\]
Rearranging for density $\rho$:
\[
\rho = \frac{3p}{\langle c^2\rangle} = \frac{3 \times 1.01 \times 10^5\text{ Pa}}{2.50 \times 10^5\text{ m}^2\text{ s}^{-2}} = \frac{303000}{250000} = 1.212\text{ kg m}^{-3} \approx 1.21\text{ kg m}^{-3}
\]
*(Check: Standard air density at sea level is approximately $1.2\text{ kg m}^{-3}$, verifying the physical accuracy of the result.)*

---

### Problem 3: Explaining When the Assumptions Break Down
State and explain two conditions under which real gases deviate significantly from ideal gas behavior.

#### Worked Solution:
1. **Very high pressure:**
   At high pressures, gas molecules are forced close together. The total volume occupied by the molecules themselves is no longer negligible compared with the volume of the container. Furthermore, because particles are packed tightly, intermolecular repulsive forces become significant.
2. **Very low temperature:**
   At low temperatures, molecular speeds are small. When molecules move slowly past one another, intermolecular attractive forces (van der Waals forces) have sufficient time to pull them together, so intermolecular forces are no longer negligible. This leads to condensation into a liquid.

---

## Checks for Understanding

### Check 1: Zero Potential Energy of an Ideal Gas
Which basic assumption of the kinetic theory of gases directly explains why the molecules of an ideal gas have zero potential energy?

- **A.** The collisions between molecules and the container walls are perfectly elastic.
- **B.** There are no intermolecular forces of attraction or repulsion between molecules except during collisions.

**Feedback for A:** Incorrect. Perfectly elastic collisions mean that kinetic energy is conserved during impacts. However, potential energy arises from forces acting across distances between particles.

**Feedback for B:** Correct. Potential energy is defined by the work done against intermolecular forces. If there are no intermolecular forces between molecules, no work is required to change the separation between them, which means the potential energy is zero. All internal energy in an ideal gas is therefore purely kinetic energy.

---

### Check 2: Momentum Transfer to Container Walls
A gas molecule of mass $m$ travels horizontally at speed $u$ towards a vertical wall and rebounds elastically. What is the magnitude of the momentum change of the molecule, and what force does it exert on the wall?

- **A.** The momentum change has magnitude $2mu$, and the molecule exerts a normal force outward against the wall.
- **B.** The momentum change has magnitude $mu$, and the molecule exerts a tangential force along the surface of the wall.

**Feedback for A:** Correct. Because velocity reverses from $+u$ to $-u$, the change in velocity is $(-u) - (+u) = -2u$. The momentum change of the molecule is $-2mu$, so the magnitude is $2mu$. By Newton's third law, the wall experiences an outward normal force in the direction of the initial motion.

**Feedback for B:** Incorrect. The momentum change is a vector difference, not a scalar difference. Reversing direction doubles the momentum change ($2mu$). Furthermore, the force acts normal (perpendicular) to the wall, not tangentially.

---

### Check 3: One-Dimensional Versus Three-Dimensional Mean-Square Speed
In the derivation of $pV = \frac{1}{3}Nm\langle c^2\rangle$, why is the factor of $\frac{1}{3}$ introduced?

- **A.** One-third of the molecules are stationary at any instant while two-thirds are moving.
- **B.** Motion is random in three dimensions with no preferred direction, so the mean-square speed along one axis is one-third of the total three-dimensional mean-square speed ($\langle c_x^2\rangle = \frac{1}{3}\langle c^2\rangle$).

**Feedback for A:** Incorrect. All molecules in an ideal gas are in continuous motion.

**Feedback for B:** Correct. In three dimensions, $c^2 = c_x^2 + c_y^2 + c_z^2$. Because molecular motion is random and isotropic (the same in all directions), $\langle c_x^2\rangle = \langle c_y^2\rangle = \langle c_z^2\rangle$. Therefore, $\langle c^2\rangle = 3\langle c_x^2\rangle$, which gives $\langle c_x^2\rangle = \frac{1}{3}\langle c^2\rangle$.

---

### Check 4: Behavior at Extreme Pressures
A gas in a sealed cylinder is compressed until its pressure reaches $500\text{ atmospheres}$. Why is the behavior of the gas unlikely to be described accurately by the formula $pV = \frac{1}{3}Nm\langle c^2\rangle$?

- **A.** The molecules travel too fast, causing their mass to change due to relativity.
- **B.** The volume of the molecules is no longer negligible compared with the reduced volume of the container, and intermolecular forces become significant.

**Feedback for A:** Incorrect. At ordinary temperatures, molecular speeds are a few hundred metres per second, which is vastly smaller than the speed of light ($3 \times 10^8\text{ m s}^{-1}$). Relativistic mass change is completely negligible.

**Feedback for B:** Correct. When compressed into a very small volume, the actual volume of the molecules forms a noticeable fraction of the container volume. In addition, the close proximity makes intermolecular forces non-negligible, violating two fundamental assumptions of ideal gas behavior.

---

## Common Misconceptions

### Misconception 1: Gas pressure is caused by molecules repelling each other
- **Incorrect idea:** Beginners often imagine that molecules in a gas push against each other like compressed springs, pushing outward against the container walls.
- **Correct physics:** In an ideal gas, there are **no repulsive or attractive forces** between molecules between collisions. Gas pressure is entirely **dynamic**, caused by the continuous bombardment and momentum transfer of moving particles striking the walls.

### Misconception 2: Gas molecules lose kinetic energy when colliding with container walls
- **Incorrect idea:** In everyday life, a bouncing tennis ball loses energy with each bounce and eventually stops. Students assume gas molecules do the same.
- **Correct physics:** Molecular collisions are **perfectly elastic**. There is no microscopic mechanism for an isolated gas molecule to lose kinetic energy during an elastic impact with a container wall at thermal equilibrium. The total kinetic energy of the gas remains strictly constant.

### Misconception 3: Mean-square speed $\langle c^2\rangle$ is the square of the mean speed $(\langle c\rangle)^2$
- **Incorrect idea:** Students often assume that $\langle c^2\rangle = (\langle c\rangle)^2$.
- **Correct physics:** The mean-square speed $\langle c^2\rangle$ is the **average of the squared speeds**. The square of the mean speed $(\langle c\rangle)^2$ is the **square of the average speed**. For any distribution containing different speeds, $\langle c^2\rangle > (\langle c\rangle)^2$. For example, if two particles have speeds $2\text{ m s}^{-1}$ and $4\text{ m s}^{-1}$, the mean speed is $\langle c\rangle = 3\text{ m s}^{-1}$ and $(\langle c\rangle)^2 = 9\text{ m}^2\text{ s}^{-2}$. However, the mean-square speed is $\langle c^2\rangle = \frac{2^2 + 4^2}{2} = \frac{4 + 16}{2} = 10\text{ m}^2\text{ s}^{-2}$.

### Misconception 4: The volume $V$ in $pV = \frac{1}{3}Nm\langle c^2\rangle$ is the volume of the molecules
- **Incorrect idea:** Students sometimes insert the volume of the individual atoms into the kinetic theory equation.
- **Correct physics:** $V$ is the **volume of the container** (the macroscopic volume throughout which the molecules are free to move). The volume of the molecules themselves is assumed to be negligible.

---

## Core Recap

- **Assumptions of kinetic theory:**
  1. Large number of identical molecules in continuous, rapid, random motion.
  2. Total volume of molecules is negligible compared with the volume of the gas.
  3. No intermolecular forces except during collisions (which implies intermolecular potential energy is zero).
  4. Collisions between molecules and with the walls are perfectly elastic.
  5. Collision duration is negligible compared with the time between collisions.
  6. Gravitational forces are negligible.
- **Microscopic cause of pressure:**
  - Molecules collide with walls, undergoing momentum change $\Delta p = 2mu$ per perpendicular collision.
  - By Newton's second and third laws, molecules exert outward forces on the walls.
  - The sum of immense numbers of impacts per second produces a steady average force per unit area: pressure $p = F/A$.
- **Kinetic theory pressure equation:**
  \[
  pV = \frac{1}{3}Nm\langle c^2\rangle
  \]
  where $p$ is pressure ($\text{Pa}$), $V$ is volume ($\text{m}^3$), $N$ is number of molecules, $m$ is mass of one molecule ($\text{kg}$), and $\langle c^2\rangle$ is mean-square speed ($\text{m}^2\text{ s}^{-2}$).
- **The factor of $\frac{1}{3}$:**
  Arises from extending one-dimensional motion to three-dimensional random motion:
  \[
  \langle c_x^2\rangle = \frac{1}{3}\langle c^2\rangle
  \]
- **Density relationship:**
  \[
  p = \frac{1}{3}\rho\langle c^2\rangle
  \]
  where $\rho = \frac{Nm}{V}$ is the gas density in $\text{kg m}^{-3}$.
