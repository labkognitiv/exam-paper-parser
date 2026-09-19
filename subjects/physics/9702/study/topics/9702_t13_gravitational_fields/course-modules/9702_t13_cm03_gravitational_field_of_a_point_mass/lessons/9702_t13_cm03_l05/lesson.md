# Field strength due to a point mass

Stand on a planet's surface, then move a few metres higher. Does the planet's
gravitational field strength change? Yes. You are farther from the planet's
centre. But near Earth, the change is so small that we normally treat
**\(g\)** as constant.

This lesson lets you calculate the gravitational field strength produced by a
point mass or outside a uniform sphere. It also explains carefully why the
near-surface constant-\(g\) model is usually good enough.

## What gravitational field strength means

Earlier, you learned that a **gravitational field** is a region where a mass
experiences a gravitational force. The **field strength** tells us how much
gravitational force each kilogram would experience at one particular place.

> **Definition to learn: gravitational field strength.** gravitational force per unit mass acting on a small test mass

A **test mass** is a small object used to investigate a field. It should be
small enough that it does not noticeably change the field being measured.

For example, if a \(1.0\,\mathrm{kg}\) test mass experiences a gravitational
force of \(8.0\,\mathrm{N}\), the field strength there is
\(8.0\,\mathrm{N\,kg^{-1}}\). A \(2.0\,\mathrm{kg}\) test mass would feel
twice the force, but the field strength at that place would still be
\(8.0\,\mathrm{N\,kg^{-1}}\).

Why should a field property not depend on the test mass you choose? Pause on
that question. The source mass creates the field. The test mass only samples
it.

## The field of one spherical body

In the last lessons, you learned two connected ideas:

- Outside a **uniform sphere**, treat its mass as a **point mass at its
  centre**.
- Newton's law gives a weaker force when the centre-to-centre separation is
  larger.

When a source mass \(M\) is treated as a point mass, its gravitational field
strength at distance \(r\) from its centre is:

## Gravitational field strength due to a point mass

> **Formula to learn: Gravitational field strength due to a point mass.**
>
> \[
> g = \frac{GM}{r^2}
> \]

This formula gives the **magnitude** of the gravitational field strength. The
field direction is towards the source mass because gravity is attractive.

| Symbol | Meaning | SI unit |
|---|---|---|
| \(g\) | gravitational field strength | \(\mathrm{N\,kg^{-1}}\) |
| \(G\) | universal gravitational constant | \(\mathrm{N\,m^2\,kg^{-2}}\) |
| \(M\) | mass producing the field | \(\mathrm{kg}\) |
| \(r\) | distance from the source mass's centre | \(\mathrm{m}\) |

Use \(G=6.67\times10^{-11}\,\mathrm{N\,m^2\,kg^{-2}}\) unless a question
gives a different value.

The square is important. If the distance from the centre doubles, \(r^2\)
becomes four times larger. The field strength becomes one quarter as large.

**Teacher question:** At a distance \(r\), a point mass produces field
strength \(g\). What is the field strength at \(2r\)?

- **A.** \(g/2\)
- **B.** \(g/4\)

**Feedback for A:** This treats the relationship as inverse distance. The
formula contains \(r^2\), so doubling the distance makes the denominator four
times larger.

**Feedback for B:** Correct. \((2r)^2=4r^2\), so the same numerator is divided
by four times as much. The new field strength is \(g/4\).

## Use the right distance

For a point outside a uniform sphere, \(r\) is measured from the sphere's
**centre**.

- At the surface, \(r\) is the sphere's **radius**.
- At height \(h\) above the surface, \(r=R+h\), where \(R\) is the sphere's
  radius.

Do not use height alone in the formula. Height is measured from the surface,
but the point-mass model places the source mass at the centre.

### Worked example 1: field strength at a moon's surface

A uniform moon has mass \(8.0\times10^{22}\,\mathrm{kg}\) and radius
\(2.0\times10^6\,\mathrm{m}\). Find the gravitational field strength at its
surface.

First make the modelling decision. The point is outside the uniform moon, so
the moon can be treated as a point mass at its centre. At the surface, the
centre distance is the radius:

\[
M=8.0\times10^{22}\,\mathrm{kg}
\]

\[
r=2.0\times10^6\,\mathrm{m}
\]

Use the point-mass field formula:

\[
g=\frac{GM}{r^2}
\]

\[
g=\frac{(6.67\times10^{-11}\,\mathrm{N\,m^2\,kg^{-2}})(8.0\times10^{22}\,\mathrm{kg})}{(2.0\times10^6\,\mathrm{m})^2}
\]

Square the complete radius:

\[
(2.0\times10^6\,\mathrm{m})^2=4.0\times10^{12}\,\mathrm{m^2}
\]

\[
g=1.334\,\mathrm{N\,kg^{-1}}
\]

To two significant figures:

\[
g=1.3\,\mathrm{N\,kg^{-1}}
\]

**Answer: \(1.3\,\mathrm{N\,kg^{-1}}\), directed towards the moon's
centre.**

The unit check is useful:

\[
\frac{\mathrm{N\,m^2\,kg^{-2}}\times\mathrm{kg}}{\mathrm{m^2}}
=\mathrm{N\,kg^{-1}}
\]

That is the unit of field strength, so the calculation is consistent.

## Why \(g\) is approximately constant near Earth's surface

The formula says that \(g\) changes with \(r\). So why do many earlier
questions use one value of \(g\), such as \(9.81\,\mathrm{N\,kg^{-1}}\), for
a falling object near Earth?

Earth's radius is about \(6.4\times10^6\,\mathrm{m}\). A height change of a
few metres, or even a few kilometres, is tiny compared with this radius.

If an object rises by height \(h\), its centre distance changes from \(R\) to
\(R+h\). The exact relationship is:

\[
g_{\text{surface}}=\frac{GM}{R^2}
\]

\[
g_{\text{height}}=\frac{GM}{(R+h)^2}
\]

When \(h\) is much smaller than \(R\), the two denominators are almost equal.
Therefore the two values of \(g\) are almost equal.

The same idea can be seen with field lines. Far from Earth, the lines spread
out radially, so their spacing changes noticeably with distance. Near the
surface, over a small height range, the lines look almost parallel and equally
spaced. That local pattern represents an approximately uniform field.

### Worked example 2: a small height change

Consider a uniform planet with mass \(5.4\times10^{24}\,\mathrm{kg}\) and
radius \(6.0\times10^6\,\mathrm{m}\). Compare \(g\) at the surface with \(g\)
at height \(12\,\mathrm{km}\).

The height must be in metres:

\[
h=12\,\mathrm{km}=1.2\times10^4\,\mathrm{m}
\]

At the surface:

\[
g_{\text{surface}}=\frac{(6.67\times10^{-11})(5.4\times10^{24})}{(6.0\times10^6)^2}
\]

\[
g_{\text{surface}}=10.0\,\mathrm{N\,kg^{-1}}
\]

At height \(h\), use centre distance \(R+h\):

\[
r=6.0\times10^6\,\mathrm{m}+1.2\times10^4\,\mathrm{m}
\]

\[
r=6.012\times10^6\,\mathrm{m}
\]

\[
g_{\text{height}}=\frac{(6.67\times10^{-11})(5.4\times10^{24})}{(6.012\times10^6)^2}
\]

\[
g_{\text{height}}=9.97\,\mathrm{N\,kg^{-1}}
\]

The decrease is:

\[
10.005\,\mathrm{N\,kg^{-1}}-9.965\,\mathrm{N\,kg^{-1}}=0.040\,\mathrm{N\,kg^{-1}}
\]

This is about a \(0.4\%\) change. For many near-surface problems, treating
\(g\) as constant is accurate enough.

**Teacher question:** A balloon rises \(20\,\mathrm{m}\) above ground. Should
you normally use \(r=20\,\mathrm{m}\) in \(g=GM/r^2\) for Earth?

- **A.** Yes, because \(20\,\mathrm{m}\) is the balloon's height.
- **B.** No, because \(r\) is nearly Earth's radius plus \(20\,\mathrm{m}\).

**Feedback for A:** Height is measured from the surface. The equation needs
distance from Earth's centre, so using \(20\,\mathrm{m}\) would predict an
impossibly huge field strength.

**Feedback for B:** Correct. Use \(r=R+h\). Since \(20\,\mathrm{m}\) is tiny
beside Earth's radius, the change in \(g\) is negligible for most problems.

## When the constant-\(g\) approximation fails

Do not use one constant value of \(g\) for a journey far from Earth. A
satellite thousands of kilometres above Earth, a spacecraft travelling between
planets, or a question explicitly giving \(M\) and \(r\), needs the
inverse-square formula.

The approximation is not a different law. It is a convenient short-range use
of the same law. The exact field gets weaker as distance from the centre grows.

## Core recap

- Learn the definition: gravitational field strength is gravitational force
  per unit mass acting on a small test mass.
- For a point mass, or outside a uniform sphere,
  \(\displaystyle g=\frac{GM}{r^2}\).
- \(r\) is measured from the source mass's **centre**. At a sphere's surface,
  \(r\) equals its radius.
- The field strength has unit **\(\mathrm{N\,kg^{-1}}\)** and points towards
  the source mass.
- Because of the square, doubling \(r\) makes \(g\) one quarter as large.
- Near Earth's surface, small height changes are tiny compared with Earth's
  radius, so \(g\) is approximately constant.

The next lesson moves from field strength to **gravitational potential**. It
will introduce the work done per unit mass in moving a test mass from infinity.
