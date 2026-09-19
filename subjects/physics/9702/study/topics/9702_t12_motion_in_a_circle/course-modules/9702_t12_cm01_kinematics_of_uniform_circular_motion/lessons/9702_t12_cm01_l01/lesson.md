# The radian and angular displacement in radians

## Start with a curved path

Imagine a point of paint on the rim of a bicycle wheel. As the wheel turns, the point follows a **curved path**. We can describe how far it turns by an **angle** at the centre of the wheel.

You may know angles in degrees. Degrees split one complete turn into 360 equal parts. Physics also uses **radians**, because radians connect an angle directly to two lengths on a circle: the **arc length** and the **radius**.

An **arc** is a curved part of a circle's edge. **Arc length**, written as \(s\), is the distance measured along that curved edge. The **radius**, written as \(r\), is the straight distance from the centre to the circle.

Ask yourself: would the same arc length mean the same amount of turning on every circle? No. An arc of \(0.20\,\mathrm{m}\) is a large part of a small circle but a small part of a large circle. A radian compares the arc length with the radius of that same circle.

<a id="definition-radian"></a>

> **Definition to learn: radian.** the angle subtended at the centre of a circle by an arc equal in length to the radius

**Subtended** means "made at the centre by". Draw two radii from the centre to the ends of an arc. If the arc length is exactly equal to one radius, the angle between those two radii is **1 radian**.

The exact definition is the sentence to use in an examination. The picture to remember is shorter: **one radius-length of arc gives one radian**.

## Linking an arc to its angle

The radian definition gives a useful relationship. It works only when the angle \(\theta\) is measured in **radians**.

<a id="formula-arc-length-angular-displacement"></a>

> **Formula to learn: Arc length and angular displacement.**
>
> \[
> s = r\theta
> \]

Here:

- \(s\) is the **arc length**, in metres (\(\mathrm{m}\)).
- \(r\) is the **radius**, in metres (\(\mathrm{m}\)).
- \(\theta\) is the **angular displacement**, in radians (\(\mathrm{rad}\)).

**Angular displacement** is the angle through which an object has turned from a chosen starting position. In this lesson, use a positive value for the size of a turn. Direction conventions come later.

Why does the formula make sense? For one radian, \(\theta=1\), so

\[
s=r\times1=r.
\]

That is exactly the definition. Two radians give an arc twice the radius. Half a radian gives an arc half the radius.

Check the units:

\[
\mathrm{m}=\mathrm{m}\times\mathrm{rad}.
\]

A radian is treated as dimensionless in this calculation, but write \(\mathrm{rad}\) with an angle so that its meaning is clear.

### Worked example: finding angular displacement from an arc

A point on the edge of a circular turntable travels an arc length of \(0.84\,\mathrm{m}\). The radius of its path is \(0.35\,\mathrm{m}\). Find the angular displacement.

**Decision.** We know an arc length and a radius, and need an angle in radians. Start with \(s=r\theta\) and rearrange it for \(\theta\).

\[
s=r\theta
\]

Divide both sides by \(r\):

\[
\frac{s}{r}=\frac{r\theta}{r}
\]

\[
\theta=\frac{s}{r}
\]

Substitute values with their units:

\[
\theta=\frac{0.84\,\mathrm{m}}{0.35\,\mathrm{m}}
\]

\[
\theta=2.4\,\mathrm{rad}
\]

**Answer: the turntable turns through \(\mathbf{2.4\,rad}\).**

The metres cancel, which is right for an angle. Also, \(2.4\,\mathrm{rad}\) is less than a full turn. A full turn is \(2\pi\,\mathrm{rad}\), about \(6.28\,\mathrm{rad}\).

Suppose the arc length stayed the same but the radius became larger. Would the angle become larger or smaller? It becomes smaller. This is the comparison that radians make visible.

A teacher asks: a point travels an arc exactly three times its radius. Which angular displacement is correct?

- **A:** \(3\,\mathrm{rad}\)
- **B:** \(3\pi\,\mathrm{rad}\)

**Feedback for A:** Correct. \(\theta=s/r\). If \(s=3r\), then \(\theta=3r/r=3\,\mathrm{rad}\).

**Feedback for B:** Not this time. \(\pi\) appears when an arc is related to a full circumference, because a full circumference is \(2\pi r\). Here the arc is stated directly as three radii, so \(\theta=3\,\mathrm{rad}\).

## A whole turn in radians

For a complete turn, the arc is the whole circumference:

\[
s=2\pi r.
\]

Use \(\theta=s/r\):

\[
\theta=\frac{2\pi r}{r}
\]

\[
\theta=2\pi\,\mathrm{rad}.
\]

So these angles describe the same turns:

| Turn | Degrees | Radians |
| --- | ---: | ---: |
| complete turn | \(360^\circ\) | \(2\pi\,\mathrm{rad}\) |
| half turn | \(180^\circ\) | \(\pi\,\mathrm{rad}\) |
| quarter turn | \(90^\circ\) | \(\pi/2\,\mathrm{rad}\) |
| three-quarter turn | \(270^\circ\) | \(3\pi/2\,\mathrm{rad}\) |

Keep \(\pi\) in an answer when possible. For example, \(3\pi/2\,\mathrm{rad}\) is exact. Its decimal value is about \(4.71\,\mathrm{rad}\).

To convert degrees to radians, use \(180^\circ=\pi\,\mathrm{rad}\):

\[
\text{angle in radians}=\text{angle in degrees}\times\frac{\pi}{180}.
\]

This conversion follows from the full-turn relationship. It is not an extra physical law.

### Worked example: expressing a turn in radians

A camera platform turns through \(225^\circ\). Express this angular displacement in radians.

**Decision.** The angle is in degrees, but the requested unit is radians. Multiply by \(\pi/180\).

\[
\theta=225^\circ\times\frac{\pi\,\mathrm{rad}}{180^\circ}
\]

Cancel degrees:

\[
\theta=\frac{225\pi}{180}\,\mathrm{rad}.
\]

Divide numerator and denominator by \(45\):

\[
\theta=\frac{5\pi}{4}\,\mathrm{rad}.
\]

**Answer: \(\mathbf{225^\circ=5\pi/4\,rad}\).**

Check the size. \(225^\circ\) is greater than half a turn, \(180^\circ\). The answer should therefore be greater than \(\pi\,\mathrm{rad}\). Since \(5\pi/4>\pi\), it is sensible.

## A common mix-up

It is tempting to use \(s=r\theta\) when \(\theta\) is in degrees. That does not work. The relationship is for \(\theta\) in radians.

For example, an arc equal to the radius gives \(s/r=1\). The angle is \(1\,\mathrm{rad}\), not \(1^\circ\). In degrees, it is about \(57.3^\circ\).

A teacher asks: an object turns through \(180^\circ\). Which expression gives the same angle in radians?

- **A:** \(\pi\,\mathrm{rad}\)
- **B:** \(2\pi\,\mathrm{rad}\)

**Feedback for A:** Correct. \(180^\circ\) is half of \(360^\circ\), so it is half of \(2\pi\,\mathrm{rad}\). Half of \(2\pi\) is \(\pi\).

**Feedback for B:** \(2\pi\,\mathrm{rad}\) is a complete turn, equal to \(360^\circ\). A turn of \(180^\circ\) is only half of that.

## Core recap

- A **radian** is **the angle subtended at the centre of a circle by an arc equal in length to the radius**.
- Use \(\mathbf{s=r\theta}\) only when \(\theta\) is in **radians**.
- \(s\) is arc length in metres, \(r\) is radius in metres and \(\theta\) is angular displacement in radians.
- A complete turn is \(\mathbf{2\pi\,rad}\), a half turn is \(\mathbf{\pi\,rad}\) and a quarter turn is \(\mathbf{\pi/2\,rad}\).
- Convert degrees to radians by multiplying by \(\pi/180\).

The next lesson uses radians to describe **how quickly** an object turns. This lesson is only about the size of an angular displacement.

