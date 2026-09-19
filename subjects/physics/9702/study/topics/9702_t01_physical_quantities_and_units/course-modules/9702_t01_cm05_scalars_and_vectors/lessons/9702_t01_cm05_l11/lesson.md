# Resolving vectors into perpendicular components and Adding and subtracting coplanar vectors

## Vectors in two dimensions

In the previous lesson, you learned that a **vector quantity** needs both a numerical size (magnitude) and a direction before its physical meaning is complete.

<a id="definition-vector-quantity"></a>

> **Definition to learn: vector quantity.** a physical quantity that has magnitude and direction

On diagrams, an arrow represents a vector. The length of the arrow represents the magnitude of the vector to a chosen scale. The arrowhead points in the direction of the vector. The tail is the starting point and the head is the tip.

When vectors lie in the same flat two-dimensional plane, such as on a map, a tabletop or a page, they are called **coplanar vectors**.

Physical problems in two dimensions require two complementary skills:
1. Combining two or more coplanar vectors into a single equivalent vector, called the **resultant vector**. This is **adding and subtracting coplanar vectors**.
2. Replacing a single diagonal vector with two equivalent perpendicular vectors along chosen axes. This is **resolving a vector into perpendicular components**.

Both skills use the geometry of arrows and right-angled triangles rather than simple scalar arithmetic.

## Adding coplanar vectors: the head-to-tail rule

Suppose you walk **6.0 m east** and then **8.0 m north**. You have made two separate displacements. A single displacement from your starting point directly to your final position achieves the exact same change in position. This single equivalent vector is the **resultant**, denoted \(\vec{R}\).

To add vectors \(\vec{A}\) and \(\vec{B}\) graphically, use the **head-to-tail construction**:
1. Draw the first vector \(\vec{A}\) starting from a chosen origin.
2. Place the tail of the second vector \(\vec{B}\) at the head (arrow tip) of \(\vec{A}\), preserving both the length and direction of \(\vec{B}\).
3. Draw the resultant vector \(\vec{R}\) from the tail of the first vector (the starting point) to the head of the second vector (the finish point).

In vector notation:

\[
\vec{R} = \vec{A} + \vec{B}
\]

This vector equation means \(\vec{R}\) produces the combined physical effect of \(\vec{A}\) followed by \(\vec{B}\). It does not mean that the numerical magnitude of \(\vec{R}\) is simply the sum of the magnitudes of \(\vec{A}\) and \(\vec{B}\).

Which diagram correctly represents the addition \(\vec{A} + \vec{B}\)?

- **A:** Place the tail of \(\vec{B}\) at the head of \(\vec{A}\), then draw the resultant arrow pointing from the tail of \(\vec{A}\) to the head of \(\vec{B}\).
- **B:** Place the tail of \(\vec{B}\) at the head of \(\vec{A}\), then draw an arrow pointing from the head of \(\vec{B}\) back to the tail of \(\vec{A}\).

**Feedback for A:** Correct. Head-to-tail addition follows the journey in sequence. The resultant must always point from the initial starting point to the final destination.

**Feedback for B:** Not correct. An arrow pointing from finish back to start is the reverse of the resultant. The resultant must point from start to finish.

## Collinear vectors: addition along one line

When vectors act along the same straight line, they are **collinear**:
- If two collinear vectors point in the **same direction**, add their magnitudes:
  \[
  R = A + B
  \]
  The resultant points in their shared direction.
- If two collinear vectors point in **opposite directions**, they partially cancel. Subtract the smaller magnitude from the larger magnitude:
  \[
  R = A - B
  \]
  The resultant points in the direction of the larger vector.

## Perpendicular vectors make a right-angled triangle

When two vectors are perpendicular (at \(90^\circ\) to each other), their head-to-tail diagram forms a right-angled triangle. The resultant vector \(\vec{R}\) forms the hypotenuse.

1. **Magnitude:** Use Pythagoras' theorem:
   \[
   R = \sqrt{A^2 + B^2}
   \]
2. **Direction:** Use the tangent ratio for the angle \(\theta\) between the resultant and a stated reference axis:
   \[
   \tan\theta = \frac{\text{opposite}}{\text{adjacent}}
   \]
   State the direction clearly with respect to a reference direction, for example "\(53.1^\circ\) north of east".

### Worked example 1: adding perpendicular displacements

A student walks **6.0 m east** and then **8.0 m north**. Determine the magnitude and direction of the resultant displacement.

**Step 1: draw the head-to-tail route.**
Draw an arrow representing \(6.0\,\mathrm{m}\) pointing east. From its tip, draw an arrow representing \(8.0\,\mathrm{m}\) pointing north. Draw the resultant arrow \(\vec{R}\) from the tail of the east vector to the tip of the north vector.

**Step 2: calculate the magnitude using Pythagoras' theorem.**

\[
R = \sqrt{(6.0\,\mathrm{m})^2 + (8.0\,\mathrm{m})^2}
\]

\[
R = \sqrt{36\,\mathrm{m^2} + 64\,\mathrm{m^2}} = \sqrt{100\,\mathrm{m^2}} = 10\,\mathrm{m}
\]

**Step 3: calculate the direction using trigonometry.**
Let \(\theta\) be the angle measured north of east. The north side (\(8.0\,\mathrm{m}\)) is opposite \(\theta\), and the east side (\(6.0\,\mathrm{m}\)) is adjacent to \(\theta\):

\[
\tan\theta = \frac{8.0\,\mathrm{m}}{6.0\,\mathrm{m}} = 1.333
\]

\[
\theta = \arctan(1.333) = 53.1^\circ
\]

**Step 4: state the complete vector result.**

\[
\boxed{\vec{R} = 10\,\mathrm{m}\text{ at }53.1^\circ\text{ north of east}}
\]

**Check:** The magnitude \(10\,\mathrm{m}\) is greater than either single step (\(6.0\,\mathrm{m}\) or \(8.0\,\mathrm{m}\)), but less than their scalar sum (\(6.0 + 8.0 = 14.0\,\mathrm{m}\)). This is physically reasonable because the two steps are perpendicular.

## Subtracting vectors means reversing the subtracted vector

In physics, changes in vector quantities are calculated by subtraction. For example, a change in velocity is \(\Delta \vec{v} = \vec{v}_2 - \vec{v}_1\).

To subtract vector \(\vec{B}\) from vector \(\vec{A}\), rewrite the subtraction as the addition of a negative vector:

\[
\vec{A} - \vec{B} = \vec{A} + (-\vec{B})
\]

The vector \(-\vec{B}\) has the exact same magnitude as \(\vec{B}\), but points in the directly opposite direction.
- Reverse the direction of the vector that appears after the minus sign (\(\vec{B}\)).
- Do not alter the first vector (\(\vec{A}\)).
- Add \(\vec{A}\) and \((-\vec{B})\) using standard head-to-tail addition.

For the vector subtraction \(\vec{P} - \vec{Q}\), what is the first step before drawing the head-to-tail diagram?

- **A:** Reverse the direction of \(\vec{Q}\) while keeping its magnitude unchanged, then add it to \(\vec{P}\).
- **B:** Reverse the direction of \(\vec{P}\) while keeping its magnitude unchanged, then add it to \(\vec{Q}\).

**Feedback for A:** Correct. \(\vec{P} - \vec{Q} = \vec{P} + (-\vec{Q})\). Only the subtracted vector \(\vec{Q}\) reverses direction.

**Feedback for B:** Not correct. Reversing \(\vec{P}\) computes \(-\vec{P} + \vec{Q}\), which is \(\vec{Q} - \vec{P}\), giving the opposite resultant.

### Worked example 2: subtracting perpendicular vectors

An aircraft flies with initial velocity \(\vec{v}_1 = 40\,\mathrm{m\,s^{-1}}\) east. A short time later, its velocity is \(\vec{v}_2 = 30\,\mathrm{m\,s^{-1}}\) north. Find the change in velocity \(\Delta \vec{v} = \vec{v}_2 - \vec{v}_1\).

**Step 1: identify the operation and reverse the subtracted vector.**
The change is \(\Delta \vec{v} = \vec{v}_2 + (-\vec{v}_1)\).
- \(\vec{v}_2 = 30\,\mathrm{m\,s^{-1}}\) north.
- \(\vec{v}_1 = 40\,\mathrm{m\,s^{-1}}\) east, so \(-\vec{v}_1 = 40\,\mathrm{m\,s^{-1}}\) west.

**Step 2: construct the head-to-tail diagram.**
Draw \(\vec{v}_2\) (\(30\,\mathrm{m\,s^{-1}}\) north). From its head, draw \(-\vec{v}_1\) (\(40\,\mathrm{m\,s^{-1}}\) west). Draw \(\Delta \vec{v}\) from the tail of \(\vec{v}_2\) to the head of \(-\vec{v}_1\).

**Step 3: calculate the magnitude of the change in velocity.**

\[
|\Delta \vec{v}| = \sqrt{(30\,\mathrm{m\,s^{-1}})^2 + (40\,\mathrm{m\,s^{-1}})^2} = \sqrt{900 + 1600} = \sqrt{2500} = 50\,\mathrm{m\,s^{-1}}
\]

**Step 4: calculate the direction.**
Let \(\theta\) be the angle west of north:

\[
\tan\theta = \frac{\text{opposite}}{\text{adjacent}} = \frac{40\,\mathrm{m\,s^{-1}}}{30\,\mathrm{m\,s^{-1}}} = 1.333
\]

\[
\theta = \arctan(1.333) = 53.1^\circ
\]

**Step 5: write the final result.**

\[
\boxed{\Delta \vec{v} = 50\,\mathrm{m\,s^{-1}}\text{ at }53.1^\circ\text{ west of north}}
\]

**Check:** The subtraction required adding a westward vector to a northward vector. The resultant points northwest (specifically west of north), which confirms the correct reversal of \(\vec{v}_1\).

## What resolving a vector means

Now consider the inverse process. Instead of combining two vectors into one, we break down one diagonal vector into two perpendicular vectors. This is called **resolving a vector into perpendicular components**.

Suppose you walk diagonally across a field. You can achieve the exact same final position by walking along two perpendicular paths: first directly east, then directly north.
- The eastward step is the **horizontal component** (or east component).
- The northward step is the **vertical component** (or north component).

The components are not separate physical things added to the situation. They are two perpendicular vectors that together are completely equivalent to the original single vector.

Each component is a vector in its own right: it has a **magnitude**, a **unit** (identical to the unit of the original vector), and a **direction** along its axis.

## Draw the triangle before choosing sine or cosine

To find the components of a vector of magnitude \(V\):
1. Choose two mutually perpendicular axes (such as horizontal and vertical, or east and north).
2. Construct a right-angled triangle where the original vector is the **hypotenuse**.
3. Locate the given angle \(\theta\) in the triangle:
   - The component along the side **adjacent** to \(\theta\) uses cosine:
     <a id="formula-adjacent-component"></a>
     \[
     \boldsymbol{\text{adjacent component} = V\cos\theta}
     \]
   - The component along the side **opposite** to \(\theta\) uses sine:
     <a id="formula-opposite-component"></a>
     \[
     \boldsymbol{\text{opposite component} = V\sin\theta}
     \]

Never assume that horizontal always uses cosine and vertical always uses sine. Which trigonometric function applies depends entirely on which axis the angle is measured from.

### Case 1: Angle measured from the horizontal axis

When angle \(\theta\) is measured from the horizontal axis:
- The horizontal side is adjacent to \(\theta\):
  \[
  \boldsymbol{V_{\text{horizontal}} = V\cos\theta}
  \]
- The vertical side is opposite to \(\theta\):
  \[
  \boldsymbol{V_{\text{vertical}} = V\sin\theta}
  \]

### Case 2: Angle measured from the vertical axis

When angle \(\theta\) is measured from the vertical axis:
- The vertical side is adjacent to \(\theta\):
  \[
  \boldsymbol{V_{\text{vertical}} = V\cos\theta}
  \]
- The horizontal side is opposite to \(\theta\):
  \[
  \boldsymbol{V_{\text{horizontal}} = V\sin\theta}
  \]

A force of **80 N** acts at an angle of \(30^\circ\) to the vertical. Which expression gives the magnitude of its vertical component?

- **A:** \(80\cos30^\circ\)
- **B:** \(80\sin30^\circ\)

**Feedback for A:** Correct. Because the angle is measured from the vertical, the vertical component is adjacent to the angle. Adjacent sides use cosine.

**Feedback for B:** Not correct. The sine function gives the side opposite to the angle. Here, the side opposite to the \(30^\circ\) angle is the horizontal component, not the vertical component.

### Worked example 3: resolving displacement (angle from horizontal)

A hiker walks a displacement of **52 m at an angle of \(32^\circ\) north of east**. Calculate the east and north components of this displacement.

**Step 1: identify the axes and the reference angle.**
The original displacement has magnitude \(V = 52\,\mathrm{m}\). The angle \(32^\circ\) is measured from the east axis towards north. Therefore:
- The east axis is the reference direction (adjacent).
- The north axis is perpendicular to it (opposite).

**Step 2: calculate the east component.**
The east component is adjacent to the \(32^\circ\) angle:

\[
V_{\text{east}} = 52\cos32^\circ = 52 \times 0.8480 = 44.1\,\mathrm{m}
\]

State with its direction:

\[
\boldsymbol{V_{\text{east}} = 44.1\,\mathrm{m}\text{ east}}
\]

**Step 3: calculate the north component.**
The north component is opposite to the \(32^\circ\) angle:

\[
V_{\text{north}} = 52\sin32^\circ = 52 \times 0.5299 = 27.6\,\mathrm{m}
\]

State with its direction:

\[
\boldsymbol{V_{\text{north}} = 27.6\,\mathrm{m}\text{ north}}
\]

**Step 4: reconstruct the original vector as an independent check.**
Recombine the two perpendicular components using Pythagoras' theorem:

\[
V_{\text{check}} = \sqrt{(44.1\,\mathrm{m})^2 + (27.6\,\mathrm{m})^2} = \sqrt{1944.8 + 761.8} = \sqrt{2706.6} = 52.0\,\mathrm{m}
\]

The reconstructed magnitude matches the original magnitude of \(52\,\mathrm{m}\). Both components are smaller than the hypotenuse, which confirms the calculation.

### Worked example 4: resolving force (angle from vertical)

A cable attached to a crane exerts a tension of **64 N at an angle of \(25^\circ\) east of the vertical**. Calculate the vertical and horizontal components of this tension force.

**Step 1: identify the reference direction.**
The angle of \(25^\circ\) is measured from the vertical.
- The vertical direction is adjacent to the angle.
- The horizontal (east) direction is opposite to the angle.

**Step 2: calculate the vertical component.**
Using cosine for the adjacent side:

\[
F_{\text{vertical}} = 64\cos25^\circ = 64 \times 0.9063 = 58.0\,\mathrm{N}
\]

\[
\boldsymbol{F_{\text{vertical}} = 58.0\,\mathrm{N}\text{ upward}}
\]

**Step 3: calculate the horizontal component.**
Using sine for the opposite side:

\[
F_{\text{horizontal}} = 64\sin25^\circ = 64 \times 0.4226 = 27.0\,\mathrm{N}
\]

\[
\boldsymbol{F_{\text{horizontal}} = 27.0\,\mathrm{N}\text{ east}}
\]

**Step 4: verify by reconstruction.**

\[
F_{\text{check}} = \sqrt{(58.0\,\mathrm{N})^2 + (27.0\,\mathrm{N})^2} = \sqrt{3364 + 729} = \sqrt{4093} = 64.0\,\mathrm{N}
\]

Check the angle:

\[
\tan\theta = \frac{27.0\,\mathrm{N}}{58.0\,\mathrm{N}} = 0.4655 \implies \theta = \arctan(0.4655) = 25.0^\circ\text{ from the vertical}
\]

Both checks confirm the resolved components.

## Directions and signs on coordinate axes

Trigonometry gives the magnitudes of components (positive lengths of triangle sides). You must assign physical directions (e.g. east, west, upward, downward) based on the physical situation.

When working with Cartesian coordinates \((x, y)\):
- Rightward and upward are standard positive directions (\(+x\) and \(+y\)).
- Leftward and downward are standard negative directions (\(-x\) and \(-y\)).

For example, if a velocity vector has a magnitude of \(20\,\mathrm{m\,s^{-1}}\) pointing south-west at \(45^\circ\) below the negative \(x\)-axis:
- The magnitude of the horizontal component is \(20\cos45^\circ = 14.1\,\mathrm{m\,s^{-1}}\) west. In signed Cartesian terms, \(v_x = -14.1\,\mathrm{m\,s^{-1}}\).
- The magnitude of the vertical component is \(20\sin45^\circ = 14.1\,\mathrm{m\,s^{-1}}\) south. In signed Cartesian terms, \(v_y = -14.1\,\mathrm{m\,s^{-1}}\).

The minus sign comes from the direction arrow pointing opposite to the positive coordinate direction, not from a negative key on a calculator.

A velocity vector has a westward component of magnitude \(15\,\mathrm{m\,s^{-1}}\) and a southward component of magnitude \(20\,\mathrm{m\,s^{-1}}\). If east and north are chosen as the positive coordinate axes, how are these components written in signed form?

- **A:** \(v_x = -15\,\mathrm{m\,s^{-1}}\) and \(v_y = -20\,\mathrm{m\,s^{-1}}\)
- **B:** \(v_x = +15\,\mathrm{m\,s^{-1}}\) and \(v_y = +20\,\mathrm{m\,s^{-1}}\)

**Feedback for A:** Correct. Because west is opposite to the positive east direction, \(v_x\) is negative. Because south is opposite to the positive north direction, \(v_y\) is negative.

**Feedback for B:** Not correct. Positive values would describe an eastward and northward velocity, pointing into the northeast quadrant rather than the southwest quadrant.

## Connecting resolution to general vector addition

Perpendicular resolution provides the general method for adding ANY two or more coplanar vectors, even when they are not at right angles:
1. Resolve each individual vector into its horizontal \((x)\) and vertical \((y)\) components.
2. Sum all the horizontal components, observing positive and negative signs:
   \[
   R_x = \sum V_x
   \]
3. Sum all the vertical components, observing positive and negative signs:
   \[
   R_y = \sum V_y
   \]
4. The resultant components \(R_x\) and \(R_y\) are perpendicular. Find the overall resultant magnitude and direction using Pythagoras and tangent:
   <a id="formula-component-magnitude-check"></a>
   \[
   \boldsymbol{R = \sqrt{R_x^2 + R_y^2}}
   \]
   <a id="formula-component-angle-check"></a>
   \[
   \boldsymbol{\tan\theta = \frac{|R_y|}{|R_x|}}
   \]

This unified framework connects vector resolution directly to vector addition.

## Evidence-backed misconceptions and their repairs

1. **Adding vector magnitudes directly as numbers:**
   Writing \(6.0\,\mathrm{m} + 8.0\,\mathrm{m} = 14.0\,\mathrm{m}\) for perpendicular displacements is incorrect. Vectors must be added geometrically. For right-angled vectors, use \(\sqrt{A^2 + B^2} = 10\,\mathrm{m}\).
2. **Drawing the resultant backwards:**
   The resultant in head-to-tail addition connects the start of the journey to the finish of the journey. Drawing an arrow from the final head back to the origin is wrong; that would represent the vector that cancels the motion, not the resultant.
3. **Subtracting vectors by subtracting lengths:**
   To subtract \(\vec{B}\) from \(\vec{A}\), you cannot simply subtract the magnitude of \(\vec{B}\) from \(\vec{A}\). You must reverse the direction of \(\vec{B}\) to get \(-\vec{B}\), and then add \(\vec{A} + (-\vec{B})\) head-to-tail.
4. **Assuming horizontal is always cosine and vertical is always sine:**
   Trigonometric functions depend on where the angle is placed. Cosine always belongs to the side adjacent to the angle; sine always belongs to the side opposite to the angle. If the angle is measured from the vertical, the vertical component uses cosine.
5. **Adding component magnitudes directly:**
   Components are perpendicular projections. In Worked Example 3, \(44.1\,\mathrm{m} + 27.6\,\mathrm{m} = 71.7\,\mathrm{m}\), which does not equal \(52\,\mathrm{m}\). Do not add component lengths as scalars. Use Pythagoras to recombine them.
6. **Omitting directions or signs:**
   A component is a vector. Writing "\(44.1\,\mathrm{m}\)" is incomplete; it must be written as "\(44.1\,\mathrm{m}\text{ east}\)" or with a coordinate sign as "\(v_x = +44.1\,\mathrm{m}\)".

## Core recap

- A **vector quantity** is **a physical quantity that has magnitude and direction**.
- **Head-to-tail addition:** To add coplanar vectors, place the tail of each subsequent vector at the head of the previous vector. The **resultant** arrow points from the initial start to the final finish.
- **Collinear vectors:** Add magnitudes if in the same direction; subtract magnitudes if in opposite directions, pointing in the direction of the larger vector.
- **Perpendicular vectors:** Form a right-angled triangle. Find magnitude with Pythagoras \(R = \sqrt{A^2 + B^2}\) and direction with \(\tan\theta = \text{opposite} / \text{adjacent}\).
- **Vector subtraction:** \(\vec{A} - \vec{B} = \vec{A} + (-\vec{B})\). Reverse only the subtracted vector \(\vec{B}\), then add head-to-tail.
- **Perpendicular resolution:** Represents one vector as two perpendicular components.
- Identify the stated angle \(\theta\):
  * **Adjacent component:** \(V\cos\theta\)
  * **Opposite component:** \(V\sin\theta\)
- Assign physical directions or coordinate signs based on which way each component points.
- Verify components by reconstructing the original magnitude: \(V = \sqrt{V_x^2 + V_y^2}\).
