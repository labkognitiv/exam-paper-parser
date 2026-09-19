# Checking equation homogeneity

A card gives the relationship **\(x=vt+at\)**. It says that \(x\) is a distance, \(v\) is a speed, \(a\) is an acceleration, and \(t\) is a time.

You do not need any measurements to test the card. The term \(vt\) has unit \(\mathrm{m}\). The term \(at\) has unit \(\mathrm{m\ s^{-1}}\). These units are different, so the two terms cannot be added to give a distance. The relationship fails a **homogeneity check**.

This lesson is about the units of supplied equations. It does not teach the physical situation that an equation may describe.

## What homogeneous means

An equation is **homogeneous** when both sides have the same SI base-unit form. More carefully, every term joined by addition or subtraction must have that same base-unit form.

Why check each added term? You may add two lengths, such as \(2\ \mathrm{m}+3\ \mathrm{m}\). You may not add a length to a speed, such as \(2\ \mathrm{m}+3\ \mathrm{m\ s^{-1}}\). They describe different kinds of physical quantity.

The previous lesson gave you the base-unit forms needed here:

- force: \(\mathrm{kg\ m\ s^{-2}}\)
- energy: \(\mathrm{kg\ m^2\ s^{-2}}\)
- power: \(\mathrm{kg\ m^2\ s^{-3}}\)

The base units in this lesson are kilograms \(\mathrm{kg}\), metres \(\mathrm{m}\), seconds \(\mathrm{s}\), amperes \(\mathrm{A}\), and kelvin \(\mathrm{K}\). A power tells you repeated multiplication. For example, \(\mathrm{m^2}\) means metre multiplied by metre. A negative power tells you the unit is in a denominator, so \(\mathrm{s^{-2}}\) means divided by seconds squared.

**Teacher question:** If one term has unit \(\mathrm{kg\ m\ s^{-2}}\) and another has unit \(\mathrm{kg\ m^2\ s^{-2}}\), what should you notice first?

The metre powers are different. One term has \(\mathrm{m^1}\) and the other has \(\mathrm{m^2}\), so the terms cannot be added.

## A reliable unit route

For each supplied equation, use the same order.

1. Separate every term joined by \(+\) or \(-\).
2. Replace each quantity with its SI base-unit form.
3. Simplify each complete term. Keep products and quotients together while you collect powers.
4. Compare the power of every base unit in every term and on both sides.
5. State a precise conclusion: **homogeneous** or **not homogeneous**.

A pure number, such as \(2\), \(\tfrac12\), or \(\pi\), has **no unit**. It changes the numerical size of a term but cannot change its base units.

Do not compare only the first term on the right-hand side with the left-hand side. Every added or subtracted term must pass the same check.

### Worked example: a distance-shaped equation

Consider the supplied relationship:

\[
\mathbf{x=vt+at^2}
\]

For this unit check, \(x\) has unit \(\mathrm{m}\), \(v\) has unit \(\mathrm{m\ s^{-1}}\), \(a\) has unit \(\mathrm{m\ s^{-2}}\), and \(t\) has unit \(\mathrm{s}\).

First check the left side:

\[
[x]=\mathrm{m}
\]

Now check the first right-hand term:

\[
\begin{aligned}
[vt]
&=(\mathrm{m\ s^{-1}})(\mathrm{s}) \\
&=\mathrm{m}
\end{aligned}
\]

The \(\mathrm{s^{-1}}\) and \(\mathrm{s}\) cancel. This term has unit \(\mathrm{m}\).

Now check the second right-hand term:

\[
\begin{aligned}
[at^2]
&=(\mathrm{m\ s^{-2}})(\mathrm{s})^2 \\
&=(\mathrm{m\ s^{-2}})(\mathrm{s^2}) \\
&=\mathrm{m}
\end{aligned}
\]

All three parts have unit \(\mathrm{m}\). Therefore the supplied equation is **homogeneous**.

This conclusion is only about units. It does not establish that the equation is a correct model for a real object.

**Teacher question:** Which proposal has matching units for \(x\), \(v\), \(a\), and \(t\) as above?

- **A:** \(x=vt+at\)
- **B:** \(x=vt+at^2\)

**Feedback for A:** Not correct. \(vt\) has unit \(\mathrm{m}\), but \(at\) has unit \(\mathrm{m\ s^{-1}}\). The two right-hand terms have different units.

**Feedback for B:** Correct. Both \(vt\) and \(at^2\) reduce to \(\mathrm{m}\), which matches \([x]\).

## A coefficient is not automatically unitless

A **coefficient** is a quantity that multiplies other quantities in an equation. Some coefficients have no unit. Others need a unit to make an equation homogeneous. You must calculate, not assume.

### Worked example: testing a unitless coefficient

A supplied model is:

\[
\mathbf{F=C\rho Au^2}
\]

Here \(F\) is force, \(\rho\) has unit \(\mathrm{kg\ m^{-3}}\), \(A\) has unit \(\mathrm{m^2}\), \(u\) has unit \(\mathrm{m\ s^{-1}}\), and \(C\) has an unknown unit. We are checking the units of this supplied model only.

Force has unit:

\[
[F]=\mathrm{kg\ m\ s^{-2}}
\]

First leave out \(C\) and simplify the other factors:

\[
\begin{aligned}
[\rho Au^2]
&=(\mathrm{kg\ m^{-3}})(\mathrm{m^2})(\mathrm{m\ s^{-1}})^2 \\
&=(\mathrm{kg\ m^{-3}})(\mathrm{m^2})(\mathrm{m^2\ s^{-2}}) \\
&=\mathrm{kg\ m\ s^{-2}}
\end{aligned}
\]

This already matches the force unit. Therefore \(C\) must have **no unit**. We call such a coefficient **dimensionless**.

Check the decision. If \(C\) had unit \(\mathrm{m}\), the right side would become \(\mathrm{kg\ m^2\ s^{-2}}\), not the unit of force. So an added metre would spoil the match.

## Use powers to find a missing exponent

Homogeneity can also find an unknown power. Compare the same base-unit power on both sides of the supplied equation.

### Worked example: an unknown length power

Consider this supplied model:

\[
\mathbf{D=\frac{Mh^n}{w}}
\]

The quantity \(D\) has unit \(\mathrm{kg\ m^{-3}}\). The quantity \(M\) has unit \(\mathrm{kg}\). Both \(h\) and \(w\) have unit \(\mathrm{m}\). The exponent \(n\) is unknown.

Replace the right-hand quantities with their units:

\[
\begin{aligned}
[D]
&=\frac{(\mathrm{kg})(\mathrm{m})^n}{\mathrm{m}} \\
&=\mathrm{kg\ m^{n-1}}
\end{aligned}
\]

Now compare with the given left side:

\[
\mathrm{kg\ m^{-3}}=\mathrm{kg\ m^{n-1}}
\]

The kilogram power already matches. Compare the metre powers:

\[
-3=n-1
\]

Add \(1\) to both sides:

\[
n=\mathbf{-2}
\]

Final check:

\[
\frac{\mathrm{kg}(\mathrm{m})^{-2}}{\mathrm{m}}
=\mathrm{kg\ m^{-3}}
\]

The units match. The supplied model is homogeneous only when \(n=-2\).

## A full check can include temperature

Temperature is another base quantity. Its SI base unit is kelvin, \(\mathrm{K}\). A temperature difference can have unit \(\mathrm{K}\), and its kelvin power must be included in the same way as any other base-unit power.

### Worked example: cancel the kelvin units

Use this supplied expression only as a unit-analysis setting:

\[
\mathbf{E=\frac{kV\Delta T}{L}}
\]

The left side \(E\) has unit \(\mathrm{kg\ m^2\ s^{-2}}\). The supplied units are \([k]=\mathrm{kg\ s^{-2}\ K^{-1}}\), \([V]=\mathrm{m^3}\), \([\Delta T]=\mathrm{K}\), and \([L]=\mathrm{m}\).

Work through the complete right-hand unit:

\[
\begin{aligned}
\left[\frac{kV\Delta T}{L}\right]
&=\frac{(\mathrm{kg\ s^{-2}\ K^{-1}})(\mathrm{m^3})(\mathrm{K})}{\mathrm{m}} \\
&=\mathrm{kg\ m^2\ s^{-2}\ K^{-1}K} \\
&=\mathrm{kg\ m^2\ s^{-2}}
\end{aligned}
\]

The \(\mathrm{K^{-1}}\) and \(\mathrm{K}\) cancel. The right side matches the unit of \(E\), so this supplied expression is **homogeneous**.

If an extra time \(t\) in seconds were placed in the denominator, the right side would become \(\mathrm{kg\ m^2\ s^{-3}}\). It would no longer match \(E\), so the altered equation would be **not homogeneous**.

## Passing the check is not proof

A unit mismatch is decisive. It shows that an equation **cannot be correct as written**.

A unit match has a more limited meaning. It shows that an equation passes this unit check. It does not prove that the physical relationship, numerical coefficient, or situation is correct. Different expressions can have the same units.

**Teacher question:** A proposed equation has matching base units on both sides. What can you conclude?

- **A:** It passes the homogeneity check, but the physics still needs separate evidence.
- **B:** It must be the correct physical equation.

**Feedback for A:** Correct. Matching units are necessary for a physical equation, but they do not test whether the proposed relationship describes the real situation.

**Feedback for B:** Not correct. Many expressions can share the same unit. The homogeneity check cannot prove the model or a numerical coefficient.

## Core recap

- An equation is **homogeneous** when every added or subtracted term, and both sides, have the same SI base-unit form.
- Separate terms, substitute base units, simplify powers, then compare every base unit.
- A pure number has **no unit**. A coefficient is dimensionless only when the other factors already match the required unit.
- Match unknown powers by equating the powers of the same base unit.
- A mismatch means an equation **cannot be correct as written**. A match means only that it passes the unit check.
