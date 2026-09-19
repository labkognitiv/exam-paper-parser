# Frictional forces, fluid resistance, and drag

## Why do moving objects slow down?

In the first three lessons of Dynamics, you studied how forces change motion:
- A resultant force causes an acceleration in the same direction as the force (\(F = ma\)).
- Force is fundamentally the rate of change of momentum of a body (\(F = \frac{\Delta p}{\Delta t}\)).
- In the absence of a resultant force, an object at rest remains at rest, and a moving object continues at constant velocity in a straight line (Newton's first law).

Yet in everyday life, if you slide a book across a wooden table, it quickly slows down and stops. If you stop pedaling a bicycle on a flat road, you gradually coast to a halt. If you switch off the motor of a speedboat on calm water, it glides forward for a short distance before coming to rest.

Does this mean Newton's first law fails in the real world?

Not at all. In every one of these cases, the moving object does experience a resultant force. Whenever two surfaces slide across one another, or whenever an object moves through a fluid such as air or water, invisible resistive forces spring into action. These forces oppose the relative motion of the surfaces or the fluid, pushing backward on the moving body and causing it to decelerate.

In this lesson, we will explore the physical origins, behavior, and key differences between two major types of resistive forces:
1. **Frictional forces** between solid surfaces in contact.
2. **Viscous forces and drag** (including air resistance) acting on objects moving through fluids.

---

## Frictional forces between solid surfaces

### The microscopic origin of friction

At macroscopic scales, polished surfaces like smooth wood, metal, or glass appear completely flat. However, if you inspect any solid surface through an electron microscope, you discover a rugged landscape of microscopic hills and valleys known as **asperities**.

When two solid surfaces are placed against each other:
- The surfaces do not make contact over their entire nominal surface area.
- Instead, contact occurs only at the microscopic peaks (the asperities) where the two surfaces touch.
- The actual area of true microscopic contact is often less than one-thousandth of the apparent macroscopic area.
- At these tiny contact points, the local pressure is immense. The atoms of the two surfaces are pressed so closely together that microscopic adhesive bonds (cold welds) form between them.

When an external force tries to slide one surface over the other, these interlocked asperities and microscopic bonds resist the motion. To make the object slide, you must apply enough force to shear these microscopic welds and ride up over the roughness of the opposing surface.

This resistive contact force, acting parallel to the interface between two solid surfaces, is called **friction**.

---

### Static friction versus kinetic friction

Friction behaves differently depending on whether the two surfaces are stationary relative to each other or actively sliding.

#### 1. Static friction (before sliding begins)

Imagine a heavy wooden crate sitting at rest on a rough concrete floor:
- If you apply no horizontal push, there is no tendency for relative motion. The horizontal frictional force is exactly **zero**.
- If you push gently with a horizontal force of \(20\,\mathrm{N}\) to the right, the crate remains stationary. Why? Because the microscopic bonds between the crate and floor hold firm, generating an opposing static frictional force of exactly \(20\,\mathrm{N}\) to the left. The resultant force is zero, so the crate does not accelerate.
- If you increase your push to \(50\,\mathrm{N}\), and the crate still does not budge, the static friction has automatically self-adjusted to \(50\,\mathrm{N}\) to the left.
- However, static friction cannot increase indefinitely. There is a maximum limit called the **limiting static friction** (or maximum static friction, \(F_{\mathrm{max}}\)).
- If the limiting static friction is \(80\,\mathrm{N}\), and you push with \(85\,\mathrm{N}\), the external push exceeds the maximum holding force. The microscopic bonds rupture, and the crate begins to slide.

> **Key property of static friction:** Static friction is a responsive, self-adjusting force. It matches the applied force to prevent relative motion, up to a maximum limiting value:
> \[
> 0 \le F_{\mathrm{static}} \le F_{\mathrm{max}}
> \]

#### 2. Kinetic (sliding) friction (during sliding)

Once the surfaces are actively sliding across each other:
- The microscopic bonds are continuously broken and reformed.
- The resistive force acting between the sliding surfaces is called **kinetic friction** (or sliding friction, or dynamic friction).
- For most dry solid surfaces over normal operating speeds, kinetic friction has a magnitude that is **approximately constant**, regardless of how fast the object slides.
- Furthermore, the kinetic friction is almost always slightly less than the maximum static friction (\(F_{\mathrm{kinetic}} < F_{\mathrm{max}}\)). This explains why it is noticeably harder to get a heavy piece of furniture moving than it is to keep it sliding once it has started.

---

### Direction of the frictional force

A very common misconception is to state that "friction always opposes motion". In Cambridge 9702, you must be far more precise:

> **Frictional forces always act parallel to the contacting surfaces and oppose the RELATIVE motion (or the tendency of relative motion) between the surfaces.**

Why is the word *relative* so critical? Because friction does not always oppose the overall motion of a body through space. In fact, friction is frequently the very force that makes forward motion possible!

Consider two classic examples:

1. **Walking or running across a floor:**
   - When you step forward, your foot pushes backward against the ground.
   - The tendency of relative motion of the sole of your shoe is backward relative to the floor.
   - Therefore, the static frictional force exerted by the ground on your shoe acts **forward**.
   - This forward frictional force is the resultant horizontal force that accelerates your body forward. If you try to run on a frictionless sheet of ice, your foot slips backward and you cannot accelerate forward.

2. **The driving wheels of a car:**
   - The engine turns the axle, rotating the drive wheels so that the bottom of each tire pushes backward against the road surface.
   - The friction between the tire and the road opposes this backward relative slip, pushing **forward** on the tire.
   - It is this forward frictional force from the road that accelerates the vehicle forward along the highway.

In both cases, friction opposes the relative motion between the contacting surfaces, but propels the overall body forward.

---

### Energy transformations caused by friction

Whenever kinetic friction acts between two sliding surfaces, mechanical work is done against the frictional force.

What happens to this energy?
- The microscopic collisions and shearing of asperities agitate the atoms and molecules in both surfaces.
- The random thermal vibrations of the atoms increase.
- Consequently, macroscopic kinetic energy is converted into **internal energy** (thermal energy), causing the temperature of both contacting surfaces to rise.
- Some energy may also be converted into acoustic energy (the sound of tires screeching or wood scraping).

You experience this every cold morning: when you vigorously rub your hands together, the kinetic energy of your hand motion is converted by friction into thermal energy, making your palms feel warm. In machinery, this thermal heating causes wear, waste of energy, and potential overheating, which is why lubricants like engine oil are used to separate moving metal surfaces.

---

## Viscous and drag forces in fluids

### What is a fluid?

In physics, a **fluid** is any substance that can flow and take the shape of its container. Both **liquids** (such as water, oil, and blood) and **gases** (such as air, helium, and steam) are fluids.

While solid surfaces slide across one another along a distinct contact boundary, an object moving through a fluid must push its way through the fluid, displacing fluid molecules out of its path.

---

### Viscosity: internal friction in fluids

Just as solids experience friction when sliding across each other, fluids experience an internal resistance to flow known as **viscosity**:
- When a fluid flows, adjacent layers of fluid slide past one another.
- Attractive forces between the fluid molecules create shear stresses between adjacent layers.
- A fluid with high viscosity (such as thick honey, cold engine oil, or syrup) resists flow strongly.
- A fluid with low viscosity (such as water or air) flows readily.

When a solid object moves through a fluid, a thin layer of fluid adheres to the surface of the object (called the boundary layer). As the object advances, this boundary layer shears against adjacent layers of fluid. The resulting resistive force is called the **viscous force**.

---

### Drag force and air resistance

The total resistive force exerted by a fluid on an object moving relative to it is known as **drag** (or the **drag force**). When the fluid is atmospheric air, this force is specifically referred to as **air resistance**.

Drag arises through two interconnected mechanisms:
1. **Skin friction (viscous drag):** Frictional shear forces between the fluid and the surface of the moving body as fluid flows along its skin.
2. **Form drag (pressure drag):** As an object pushes forward through a fluid, it collides with fluid particles ahead of it, creating a high-pressure zone in front of the body. Meanwhile, behind the body, the fluid cannot instantly fill the vacated space, creating a low-pressure, turbulent wake. This difference in pressure between front and back pushes backward on the body.

The drag force always acts in a direction that opposes the relative velocity of the body through the fluid:

> **Drag force always acts in the direction opposite to the velocity of the object relative to the fluid.**

If an aeroplane flies horizontally to the east through still air, air resistance acts horizontally to the west. If a stone falls vertically downwards through air, air resistance acts vertically upwards.

---

### The simple model of drag: variation with speed

How does drag force depend on the speed of the moving object?

In Cambridge International AS Level Physics, you do not need complex formulas for fluid mechanics, and no numerical coefficients of friction or viscosity are required. The syllabus explicitly states:

> **A simple model of drag force increasing as speed increases is sufficient.**

Let us trace what this simple model means physically:

1. **At zero speed (\(v = 0\)):**
   - If an object is completely stationary relative to the fluid, no fluid molecules are colliding with it preferentially from one side.
   - Therefore, the drag force is exactly **zero**:
     \[
     D = 0 \quad \text{when} \quad v = 0
     \]
   - Unlike static friction between solids (which can be non-zero when stationary to prevent motion), fluid drag cannot hold an object stationary against an applied force.

2. **At low speeds:**
   - As the object begins to move with speed \(v\), it collides with fluid particles in its path.
   - The fluid particles must be pushed aside, transferring momentum to the fluid.
   - The drag force increases as speed increases.

3. **At higher speeds:**
   - As the speed rises further, the object encounters vastly more fluid particles every second.
   - Moreover, each collision delivers a greater impulse, and turbulent swirling eddies form in the wake behind the object.
   - Consequently, the drag force grows rapidly with speed. (In turbulent flow, drag typically increases roughly with the square of speed, \(D \propto v^2\), though qualitative knowledge that drag increases as speed increases is all that is required for AS Level).

This fundamental relationship can be summarized in one clear rule:

\[
\text{As speed } v \text{ increases, drag force } D \text{ increases.}
\]
\[
\text{As speed } v \text{ decreases, drag force } D \text{ decreases.}
\]

---

### Factors that influence drag force

Besides speed, what other factors determine the magnitude of the drag force on an object?

1. **Cross-sectional area (frontal area):**
   - An object with a large frontal area directly collides with a larger volume of fluid per second than an object with a small frontal area.
   - A skydiver falling belly-to-earth exposes a large surface area (about \(0.8\,\mathrm{m^2}\)) and experiences a large drag force. If the same skydiver straightens their body into a vertical dive, their frontal area drops by more than half, and the drag force at the same speed drops dramatically.
   - Opening a parachute increases the cross-sectional area by a factor of 40 or more, producing a huge upward drag force that slows the descent.

2. **Shape and streamlining:**
   - A blunt, flat plate moving through a fluid causes fluid flow lines to separate violently, leaving a wide, chaotic, low-pressure turbulent wake behind it. This creates enormous pressure drag.
   - A **streamlined** shape (such as a teardrop, an aircraft wing, or the sleek body of a dolphin or racing car) allows fluid to flow smoothly along its contours and close together behind the body with minimal turbulence. Streamlining significantly reduces form drag.

3. **Density and viscosity of the fluid:**
   - Moving through a dense liquid (like water, density \(\approx 1000\,\mathrm{kg\,m^{-3}}\)) involves displacing vastly more mass per second than moving through air (density \(\approx 1.2\,\mathrm{kg\,m^{-3}}\)).
   - At a walking speed of \(1.5\,\mathrm{m\,s^{-1}}\), you barely notice air resistance. But if you try to wade rapidly through waist-deep water at the same speed, the drag force is immediately and overwhelmingly noticeable.

---

## Comparing solid friction and fluid drag

To master this topic for Cambridge examinations, you must clearly contrast how solid friction and fluid drag behave. The following table highlights the vital differences:

| Property | Solid Friction (Kinetic) | Fluid Drag / Air Resistance |
| :--- | :--- | :--- |
| **Media involved** | Two solid surfaces in direct contact | A solid object moving through a fluid (liquid or gas) |
| **Microscopic cause** | Interlocking asperities and microscopic cold welds | Collisions with fluid molecules and viscous shearing |
| **Value when stationary (\(v = 0\))** | Static friction can be non-zero (self-adjusts up to \(F_{\mathrm{max}}\)) | Exactly zero (no drag without relative speed) |
| **Dependence on speed** | Approximately constant over normal sliding speeds | Increases as speed increases |
| **Dependence on contact area** | Largely independent of nominal surface area for rigid solids | Strongly dependent on frontal cross-sectional area and shape |
| **Energy transformation** | Converts kinetic energy to thermal energy and sound | Converts kinetic energy to thermal energy and fluid turbulence |
| **Effect of streamlining** | Not applicable | Dramatically reduces form drag by smoothing fluid flow |

---

## Worked Examples

### Worked Example 1: Horizontal crate on a warehouse floor

A heavy metal packing case of mass \(60\,\mathrm{kg}\) rests on a rough horizontal concrete floor. The maximum limiting static friction between the case and the floor is \(180\,\mathrm{N}\). Once sliding, the constant kinetic frictional force opposing motion is \(150\,\mathrm{N}\). A warehouse worker attaches a horizontal cable to the case and pulls with a steady horizontal tension \(T\).

Assume air resistance is negligible for this low-speed movement.

**(a)** Determine the magnitude and direction of the frictional force acting on the case when the worker pulls with a tension of \(T = 120\,\mathrm{N}\). State whether the case moves.

**(b)** The worker increases the pulling tension to \(T = 210\,\mathrm{N}\). Determine:
1. the resultant horizontal force on the case;
2. the acceleration of the case.

**(c)** While the case is sliding at \(1.5\,\mathrm{m\,s^{-1}}\), the worker suddenly releases the cable so that \(T = 0\). Calculate the deceleration of the case and the distance it slides before coming to rest.

---

#### Solution to Example 1

**(a) Analyzing the stationary case:**

- The maximum limiting static friction is \(F_{\mathrm{max}} = 180\,\mathrm{N}\).
- The applied pulling force is \(T = 120\,\mathrm{N}\) in the forward direction.
- Because \(T \le F_{\mathrm{max}}\) (\(120\,\mathrm{N} \le 180\,\mathrm{N}\)), the applied force is insufficient to overcome the static friction.
- The static frictional force self-adjusts to balance the applied force exactly:
  \[
  F_{\mathrm{static}} = 120\,\mathrm{N} \quad \text{acting in the opposite direction (backward)}
  \]
- Resultant horizontal force:
  \[
  F_{\mathrm{net}} = T - F_{\mathrm{static}} = 120\,\mathrm{N} - 120\,\mathrm{N} = 0\,\mathrm{N}
  \]
- **Conclusion:** The case does not move.

---

**(b) Pulling force exceeds limiting static friction:**

1. The applied tension is \(T = 210\,\mathrm{N}\). Because \(210\,\mathrm{N} > 180\,\mathrm{N}\), the crate begins to slide.
   Once sliding, the opposing force is the **kinetic friction**, which has magnitude \(F_{\mathrm{kinetic}} = 150\,\mathrm{N}\).
   The resultant horizontal force is:
   \[
   F_{\mathrm{net}} = T - F_{\mathrm{kinetic}} = 210\,\mathrm{N} - 150\,\mathrm{N} = +60\,\mathrm{N} \quad \text{(forward)}
   \]

2. Using Newton's second law (\(F_{\mathrm{net}} = ma\)), the acceleration is:
   \[
   a = \frac{F_{\mathrm{net}}}{m} = \frac{60\,\mathrm{N}}{60\,\mathrm{kg}} = 1.0\,\mathrm{m\,s^{-2}} \quad \text{(in the forward direction)}
   \]

---

**(c) Motion after the cable is released:**

1. When the cable is released, \(T = 0\).
   The only horizontal force acting on the sliding case is the kinetic friction, \(F_{\mathrm{kinetic}} = 150\,\mathrm{N}\), acting backward.
   The resultant horizontal force is:
   \[
   F_{\mathrm{net}} = -150\,\mathrm{N}
   \]
   The acceleration is:
   \[
   a = \frac{F_{\mathrm{net}}}{m} = \frac{-150\,\mathrm{N}}{60\,\mathrm{kg}} = -2.5\,\mathrm{m\,s^{-2}}
   \]
   The case undergoes a constant deceleration of magnitude \(2.5\,\mathrm{m\,s^{-2}}\).

2. To find the sliding distance before stopping:
   - Initial velocity: \(u = 1.5\,\mathrm{m\,s^{-1}}\)
   - Final velocity: \(v = 0\,\mathrm{m\,s^{-1}}\)
   - Acceleration: \(a = -2.5\,\mathrm{m\,s^{-2}}\)

   Using the kinematics equation \(v^2 = u^2 + 2as\):
   \[
   0 = (1.5)^2 + 2(-2.5)s
   \]
   \[
   0 = 2.25 - 5.0s
   \]
   \[
   5.0s = 2.25 \implies s = \frac{2.25}{5.0} = 0.45\,\mathrm{m}
   \]

- **Reasonableness check:** A case of mass \(60\,\mathrm{kg}\) moving at walking speed (\(1.5\,\mathrm{m\,s^{-1}}\)) stopped by a substantial frictional force of \(150\,\mathrm{N}\) slides less than half a metre (\(45\,\mathrm{cm}\)), which is entirely realistic.

---

### Worked Example 2: Diver plunging through water

An athlete of mass \(75\,\mathrm{kg}\) dives into a swimming pool. At the instant their entire body is submerged below the water surface, they are moving vertically downwards with an initial entry speed of \(8.0\,\mathrm{m\,s^{-1}}\).

At this instant, the water exerts an upward buoyant force (upthrust) of \(740\,\mathrm{N}\) on the diver, and a viscous drag force of \(620\,\mathrm{N}\) vertically upwards.
The acceleration of free fall is \(g = 9.81\,\mathrm{m\,s^{-2}}\).

**(a)** Calculate the weight of the diver.

**(b)** Determine the magnitude and direction of the resultant vertical force acting on the diver at the instant of full submersion.

**(c)** Calculate the diver's instantaneous acceleration at this moment.

**(d)** As the diver continues to move deeper into the water, explain qualitatively what happens to:
1. the diver's speed;
2. the viscous drag force;
3. the resultant force and the diver's acceleration.

---

#### Solution to Example 2

**(a) Weight of the diver:**

Using the weight formula \(W = mg\):
\[
W = 75\,\mathrm{kg} \times 9.81\,\mathrm{m\,s^{-2}} = 735.75\,\mathrm{N} \approx 740\,\mathrm{N} \quad \text{(to 2 significant figures)}
\]

---

**(b) Resultant vertical force at entry:**

Let us choose **downwards** as the positive direction:
- Downward force: Weight \(W = +735.8\,\mathrm{N}\)
- Upward forces:
  - Upthrust \(U = 740\,\mathrm{N}\) upwards, so \(-740\,\mathrm{N}\)
  - Viscous drag \(D = 620\,\mathrm{N}\) upwards (opposing downward motion), so \(-620\,\mathrm{N}\)

The resultant force is the vector sum:
\[
F_{\mathrm{net}} = W - U - D = +735.8\,\mathrm{N} - 740\,\mathrm{N} - 620\,\mathrm{N} = -624.2\,\mathrm{N} \approx -620\,\mathrm{N}
\]

The negative sign indicates that the resultant force is directed **vertically upwards**.
Magnitude of resultant force = \(620\,\mathrm{N}\) (to 2 significant figures).

---

**(c) Instantaneous acceleration:**

Using Newton's second law:
\[
a = \frac{F_{\mathrm{net}}}{m} = \frac{-624.2\,\mathrm{N}}{75\,\mathrm{kg}} = -8.32\,\mathrm{m\,s^{-2}} \approx -8.3\,\mathrm{m\,s^{-2}}
\]

The acceleration has a magnitude of \(8.3\,\mathrm{m\,s^{-2}}\) and is directed **vertically upwards**.
Because the diver's velocity is downwards while their acceleration is upwards, the diver is rapidly decelerating (slowing down).

---

**(d) Subsequent motion:**

1. **Speed:** Because the resultant force is upward, opposing the downward velocity, the diver's downward speed decreases.
2. **Viscous drag:** Drag force in a fluid decreases as speed decreases. Therefore, as the diver slows down, the upward viscous drag force \(D\) decreases.
3. **Resultant force and acceleration:**
   - The upward resultant force has magnitude \(F_{\mathrm{net}} = (U + D) - W\).
   - Because \(U \approx W\) (the diver's weight is balanced by upthrust), the net upward decelerating force is predominantly due to the drag \(D\).
   - As \(D\) decreases, the resultant upward force decreases, so the magnitude of the deceleration decreases until the diver comes to a momentary halt below the surface.

---

### Worked Example 3: Cyclist on a level road

A cyclist and her bicycle have a combined mass of \(80\,\mathrm{kg}\). When moving along a straight, horizontal asphalt track:
- The mechanical rolling resistance and axle friction exert a constant total resistive force of \(15\,\mathrm{N}\), independent of speed.
- The air resistance \(D\) increases with speed, and is modeled qualitatively such that at a moderate speed of \(4.0\,\mathrm{m\,s^{-1}}\) the air resistance is \(10\,\mathrm{N}\), while at a racing speed of \(12.0\,\mathrm{m\,s^{-1}}\) the air resistance increases to \(90\,\mathrm{N}\).

The cyclist pedals to deliver a constant forward driving force of \(65\,\mathrm{N}\) exerted by the road on the rear tire.

**(a)** State the physical origin of the forward driving force exerted by the road on the tire.

**(b)** Calculate the total resistive force opposing the cyclist at:
1. \(v = 4.0\,\mathrm{m\,s^{-1}}\);
2. \(v = 12.0\,\mathrm{m\,s^{-1}}\).

**(c)** Calculate the cyclist's instantaneous acceleration at:
1. \(v = 4.0\,\mathrm{m\,s^{-1}}\);
2. \(v = 12.0\,\mathrm{m\,s^{-1}}\).

**(d)** State whether the cyclist can maintain the speed of \(12.0\,\mathrm{m\,s^{-1}}\) with this driving force.

---

#### Solution to Example 3

**(a) Origin of the driving force:**

When the cyclist pedals, the chain drives the rear wheel, causing the rubber tire to push backward against the ground. By Newton's third law, the road exerts an equal and opposite forward static frictional force on the tire. This forward static friction between the tire and the road surface is the driving force that propels the bicycle forward.

---

**(b) Total resistive force:**

The total resistive force is the sum of the constant mechanical friction and the speed-dependent air resistance:
\[
R_{\mathrm{total}} = F_{\mathrm{rolling}} + D
\]

1. At \(v = 4.0\,\mathrm{m\,s^{-1}}\):
   \[
   R_{\mathrm{total}} = 15\,\mathrm{N} + 10\,\mathrm{N} = 25\,\mathrm{N}
   \]

2. At \(v = 12.0\,\mathrm{m\,s^{-1}}\):
   \[
   R_{\mathrm{total}} = 15\,\mathrm{N} + 90\,\mathrm{N} = 105\,\mathrm{N}
   \]

---

**(c) Instantaneous acceleration:**

1. At \(v = 4.0\,\mathrm{m\,s^{-1}}\):
   - Driving force: \(F_{\mathrm{drive}} = 65\,\mathrm{N}\)
   - Total resistive force: \(R_{\mathrm{total}} = 25\,\mathrm{N}\)
   - Resultant forward force:
     \[
     F_{\mathrm{net}} = 65\,\mathrm{N} - 25\,\mathrm{N} = +40\,\mathrm{N}
     \]
   - Acceleration:
     \[
     a = \frac{F_{\mathrm{net}}}{m} = \frac{40\,\mathrm{N}}{80\,\mathrm{kg}} = 0.50\,\mathrm{m\,s^{-2}} \quad \text{(forward)}
     \]

2. At \(v = 12.0\,\mathrm{m\,s^{-1}}\):
   - Driving force: \(F_{\mathrm{drive}} = 65\,\mathrm{N}\)
   - Total resistive force: \(R_{\mathrm{total}} = 105\,\mathrm{N}\)
   - Resultant forward force:
     \[
     F_{\mathrm{net}} = 65\,\mathrm{N} - 105\,\mathrm{N} = -40\,\mathrm{N}
     \]
   - Acceleration:
     \[
     a = \frac{F_{\mathrm{net}}}{m} = \frac{-40\,\mathrm{N}}{80\,\mathrm{kg}} = -0.50\,\mathrm{m\,s^{-2}}
     \]
   The cyclist experiences a net backward force, giving an acceleration of \(-0.50\,\mathrm{m\,s^{-2}}\) (a deceleration of \(0.50\,\mathrm{m\,s^{-2}}\)).

---

**(d) Maintaining \(12.0\,\mathrm{m\,s^{-1}}\):**

No. Because the total resistive force at \(12.0\,\mathrm{m\,s^{-1}}\) (\(105\,\mathrm{N}\)) is strictly greater than the driving force (\(65\,\mathrm{N}\)), the net force is backward, causing the bicycle to slow down. To maintain a steady speed of \(12.0\,\mathrm{m\,s^{-1}}\), the cyclist would need to increase her pedal effort so that the forward driving force matches the \(105\,\mathrm{N}\) total resistive force.

---

## Check your understanding

### Check 1: Direction of friction on an accelerating car

A rear-wheel drive sports car accelerates forward along a straight, horizontal dry tarmac track.

Which statement correctly identifies the direction of the horizontal frictional force exerted by the road on the rear (driving) tires and on the front (non-driving) tires?

- **A.** Forward on the rear tires, and backward on the front tires.
- **B.** Backward on the rear tires, and backward on the front tires.

**Feedback for A:** Correct. The engine rotates the rear wheels so that the bottom of each rear tire pushes backward against the road. The friction opposing this relative slip pushes forward on the rear tires, providing the forward driving force that accelerates the car. Meanwhile, the front wheels are not driven by the engine; they are pushed forward by the car chassis, so the road exerts a small backward frictional force that causes them to rotate.

**Feedback for B:** Incorrect. If the friction on the rear driving tires were backward, the total horizontal force on the car would be backward, making it impossible for the car to accelerate forward. The rear tires push backward against the ground, so by Newton's third law, the road pushes forward on the rear tires.

---

### Check 2: Speed dependence of solid friction versus fluid drag

A metal slider is placed on a dry horizontal bench in air. The slider is given an initial push and slides freely, slowing down under the action of both dry kinetic friction from the bench surface and air resistance from the surrounding air.

As the speed of the slider decreases from \(5.0\,\mathrm{m\,s^{-1}}\) to \(1.0\,\mathrm{m\,s^{-1}}\), what happens to the magnitude of the dry kinetic friction and the magnitude of the air resistance?

- **A.** The dry kinetic friction remains approximately constant, while the air resistance decreases.
- **B.** Both the dry kinetic friction and the air resistance decrease.

**Feedback for A:** Correct. Dry kinetic friction between solid surfaces is approximately independent of sliding speed over ordinary ranges. In contrast, air resistance (fluid drag) depends directly on speed and decreases as speed decreases.

**Feedback for B:** Incorrect. While fluid drag decreases with decreasing speed, solid kinetic friction does not. The microscopic mechanism of sliding friction between dry solid surfaces produces a resistive force that remains approximately constant as the body slows down.

---

### Check 3: Energy transformation by resistive forces

When a commercial aircraft glides through the air and applies its carbon wheel brakes after touchdown, work is done against air resistance during flight and against solid friction during ground braking.

Which row correctly identifies the primary final form of energy into which mechanical kinetic energy is transformed by both air resistance and wheel brake friction?

- **A.** Internal (thermal) energy of the aircraft parts and the surrounding atmosphere.
- **B.** Gravitational potential energy stored in the Earth-aircraft system.

**Feedback for A:** Correct. Both fluid drag and solid friction do negative mechanical work on the moving vehicle, transferring macroscopic kinetic energy into the random kinetic and potential energy of atoms and molecules (internal thermal energy). The brake discs become hot, and the air disturbed by the aircraft warms up slightly.

**Feedback for B:** Incorrect. Resistive forces are dissipative: they convert organized mechanical kinetic energy into thermal energy (heat) and sound. They do not store energy as gravitational potential energy.

---

### Check 4: Submarine moving at steady depth

A submarine travels horizontally through the ocean at a constant velocity of \(6.0\,\mathrm{m\,s^{-1}}\). The engines provide a forward thrust of \(250\,\mathrm{kN}\).

Which statement regarding the forces acting on the submarine is correct?

- **A.** The backward viscous drag force exerted by the water on the hull is equal to \(250\,\mathrm{kN}\).
- **B.** The backward viscous drag force must be less than \(250\,\mathrm{kN}\) for the submarine to keep moving forward.

**Feedback for A:** Correct. Because the submarine moves at a constant velocity, its acceleration is zero (\(a = 0\)). By Newton's first law, the resultant horizontal force must be zero. Therefore, the forward thrust of \(250\,\mathrm{kN}\) must be exactly balanced by an equal backward viscous drag force of \(250\,\mathrm{kN}\).

**Feedback for B:** Incorrect. This is a common confusion between motion and acceleration. A resultant forward force (thrust greater than drag) is required to speed up (accelerate), not to maintain constant velocity. Once the submarine reaches a steady speed, the forward thrust exactly balances the backward drag.

---

## Mistakes worth repairing

### Mistake 1: Believing friction always opposes the motion of a body

A widespread misconception among physics students is that friction always acts in the opposite direction to an object's velocity.

In reality:
- Friction opposes the **relative motion between the two surfaces in contact**.
- If you walk forward, your foot pushes backward against the pavement. Pavement friction acts forward on your shoe. Without this forward frictional force, you could not walk forward.
- In wheeled vehicles, the driving wheels push backward against the road, and road friction acts forward on the tires to accelerate the vehicle.
- Always ask: *In which direction does the contacting surface want to slip relative to the other surface?* The friction acts in the exact opposite direction to that relative slip.

---

### Mistake 2: Assuming solid friction increases with speed

Students who have learned that air resistance increases with speed often assume that solid sliding friction behaves the same way.

Remember the essential difference:
- **Fluid drag** starts at zero when stationary and increases as speed increases.
- **Solid kinetic friction** is approximately **constant** over normal ranges of sliding speed. A wooden block sliding across a table at \(4.0\,\mathrm{m\,s^{-1}}\) experiences essentially the same kinetic friction as when sliding at \(1.0\,\mathrm{m\,s^{-1}}\).

---

### Mistake 3: Believing drag forces exist when an object is at rest

Unlike solid static friction, which can exert a substantial holding force on a stationary crate, fluid drag requires **relative motion**:
- If an object is stationary in still water or still air (\(v = 0\)), the drag force is identically **zero**.
- You cannot use fluid resistance to prevent an object from beginning to move when an external force is applied. Drag only comes into existence once velocity is non-zero.

---

### Mistake 4: Confusing friction with the normal contact force

Friction and the normal reaction force are both contact forces between two surfaces, but they act in perpendicular directions:
- The **normal contact force** (\(N\) or \(R\)) acts **perpendicular** (normal) to the contact surface, preventing the surfaces from passing through each other.
- The **frictional force** (\(F\)) acts **parallel** to the contact surface, opposing relative sliding.
- They are mutually perpendicular components of the total contact force exerted by one surface on another.

---

### Mistake 5: Assuming streamlining eliminates drag completely

While streamlining a car, train, or aeroplane reduces the low-pressure wake and greatly lowers **form drag**, it cannot eliminate drag entirely.
- Even the most streamlined teardrop shape still possesses surface area exposed to the fluid.
- Fluid molecules flowing along the body experience viscous shear stresses, producing **skin friction**.
- Therefore, streamlining reduces drag, but can never reduce it to zero.

---

## Core recap

- **Frictional force** between solid surfaces acts parallel to the contact interface and opposes relative motion (or impending relative motion) between the surfaces.
- **Static friction** prevents surfaces from sliding relative to each other. It self-adjusts to balance applied forces from zero up to a maximum limit: \(0 \le F_{\mathrm{static}} \le F_{\mathrm{max}}\).
- **Kinetic friction** opposes ongoing relative sliding between surfaces and has an approximately constant magnitude over normal sliding speeds.
- Frictional forces can propel an object forward (as in walking or the driving wheels of a car) because friction opposes the backward relative slip of the foot or tire against the ground.
- Frictional work converts macroscopic kinetic energy into **internal thermal energy** (heat) and sound.
- **Viscosity** is the internal friction of a fluid that resists flow and relative motion of adjacent fluid layers.
- **Drag force** (including air resistance) is the resistive force exerted by a fluid on an object moving relative to the fluid. It always acts opposite to the velocity of the object relative to the fluid.
- A simple model of drag:
  - Drag is zero when relative speed is zero (\(D = 0\) when \(v = 0\)).
  - Drag force increases as speed increases.
  - Drag force increases with larger frontal cross-sectional area and fluid density.
  - Streamlining reduces pressure/form drag by smoothing fluid flow lines around the body.

---

## Next lesson preview

In the next lesson (**Lesson 5: Qualitatively the motion of objects in a uniform gravitational field with air resistance**), you will apply this simple model of speed-dependent drag to analyze the complete journey of an object falling through the atmosphere. You will see how increasing air resistance reduces the net downward force and acceleration, causing the object to reach a constant **terminal velocity**.
