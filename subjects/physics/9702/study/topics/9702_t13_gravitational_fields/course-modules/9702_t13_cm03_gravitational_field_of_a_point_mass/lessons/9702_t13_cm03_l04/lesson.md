# Deriving the field strength of a point mass

## The question we are answering

Earlier, you met two ideas:

- **Newton's law of gravitation** gives the gravitational force between two point masses.
- **Gravitational field strength** is gravitational force per unit mass.

Now connect them. If a source mass creates a gravitational force, what is the force for each kilogram of a small test mass? That answer gives the gravitational field strength at the test mass.

This lesson derives the relationship. The next lesson will practise recalling and using it in calculations.

## The two starting facts

### Newton's law of gravitation {#definition-newtons-law-of-gravitation}

> **Definition to learn: Newton's law of gravitation.** gravitational force is directly proportional to the product of the masses and inversely proportional to the square of their separation

The phrase **directly proportional to the product of the masses** means that a larger source mass or a larger test mass produces a larger gravitational force. The phrase **inversely proportional to the square of their separation** means that greater separation produces a weaker force.

### Formula for Newton's law {#formula-newtons-law-of-gravitation}

> **Formula to learn: Newton's law of gravitation.**
>
> \[
> F = \frac{G m_1 m_2}{r^2}
> \]

In this formula, \(F\) is gravitational force in \(\mathrm{N}\), \(G\) is the gravitational constant, \(m_1\) and \(m_2\) are the two masses in \(\mathrm{kg}\), and \(r\) is their separation in \(\mathrm{m}\).

For this derivation, call the source mass **\(M\)** and the small test mass **\(m\)**. The distance \(r\) is measured from the centre of the point mass to the test mass. For a point outside a uniform sphere, earlier learning lets us treat the sphere's mass as if it were concentrated at its centre.

So Newton's law becomes:

\[
F = \frac{GMm}{r^2}
\]

Ask yourself: which symbol here belongs to the object creating the field? It is \(M\). Which symbol belongs to the small object testing the field? It is \(m\).

### Gravitational field strength {#definition-gravitational-field-strength}

> **Definition to learn: gravitational field strength.** gravitational force per unit mass acting on a small test mass

### Formula for gravitational field strength {#formula-gravitational-field-strength}

> **Formula to learn: Gravitational field strength.**
>
> \[
> g = \frac{F}{m}
> \]

Here \(g\) is gravitational field strength in \(\mathrm{N\,kg^{-1}}\), \(F\) is the gravitational force on the small test mass in \(\mathrm{N}\), and \(m\) is that test mass in \(\mathrm{kg}\).

The important point is that \(F\) in this definition is the gravitational force. It is not a contact force from a surface and not automatically the resultant force.

## The derivation, one step at a time

We want field strength, so begin with its definition:

\[
g=\frac{F}{m}
\]

Newton's law tells us the gravitational force on the test mass:

\[
F=\frac{GMm}{r^2}
\]

Substitute this expression for \(F\) into the field-strength definition.

\[
g=\frac{\frac{GMm}{r^2}}{m}
\]

The test mass \(m\) appears once in the numerator and once as the divisor. It cancels.

\[
g=\frac{GM}{r^2}
\]

### Derived formula for a point mass {#formula-gravitational-field-strength-point-mass}

> **Formula to learn: Gravitational field strength due to a point mass.**
>
> \[
> g = \frac{GM}{r^2}
> \]

This is the derived relationship for the **magnitude** of gravitational field strength due to a point mass.

Notice what has disappeared: the test mass \(m\). That must happen. Field strength describes the source's field at a position. It must not depend on which suitably small test mass you use to investigate it.

The field direction is towards the source mass because gravity is attractive. The formula above gives the magnitude only.

### Worked example 1: showing the cancellation clearly

A source mass \(M\) acts on a small test mass \(m\), separated by distance \(r\). Derive the field strength at the test mass.

Start with force per unit mass:

\[
g=\frac{F}{m}
\]

Use Newton's law for the force:

\[
F=\frac{GMm}{r^2}
\]

Put this complete expression into the numerator:

\[
g=\frac{\frac{GMm}{r^2}}{m}
\]

Divide by \(m\). The same test-mass factor cancels:

\[
g=\frac{GM}{r^2}
\]

**Result: \(\displaystyle g=\frac{GM}{r^2}\).**

Check the reasoning. The result contains the source mass \(M\) and the separation \(r\). It does not contain the test mass. This agrees with the meaning of field strength.

A test mass is changed from \(m\) to \(4m\), while its position near the same source mass does not change. Which statement is correct?

- **A.** The gravitational force becomes four times larger, but the field strength stays the same.
- **B.** Both the gravitational force and the field strength become four times larger.

**Feedback for A:** Correct. Newton's law makes the force proportional to the test mass. Dividing that larger force by the larger mass still gives the same \(g\).

**Feedback for B:** The force does become four times larger, but field strength is force per unit mass. The factor of four cancels when \(F\) is divided by \(m\).

### Worked example 2: testing the result with two masses

Keep the same source mass \(M\) and separation \(r\). Compare test mass \(m\) with test mass \(3m\).

For the first test mass:

\[
F_1=\frac{GMm}{r^2}
\]

\[
g_1=\frac{F_1}{m}
\]

\[
g_1=\frac{\frac{GMm}{r^2}}{m}=\frac{GM}{r^2}
\]

For the second test mass, Newton's law gives three times the force:

\[
F_2=\frac{GM(3m)}{r^2}
\]

Now divide by the second test mass, \(3m\):

\[
g_2=\frac{F_2}{3m}
\]

\[
g_2=\frac{\frac{GM(3m)}{r^2}}{3m}=\frac{GM}{r^2}
\]

So

\[
g_1=g_2
\]

**Result: both test masses measure the same field strength at the same position.**

This is not a coincidence. A field is a property of the source and the position, not of the chosen small test mass.

## What distance means

The \(r\) in the derivation is the separation between the source mass and the test mass.

For a point mass, measure \(r\) from the point mass to the test mass. For a point outside a uniform spherical body, use the distance from the sphere's centre to the test mass.

Do not use height above the surface when the question needs centre-to-object separation. Height above a surface is only part of the distance. If an object is above a sphere, the full separation is the sphere's radius plus the height.

A source mass is made **twice as large**, while the test mass and separation are unchanged. What happens to the derived field strength?

- **A.** It doubles.
- **B.** It stays unchanged.

**Feedback for A:** Correct. In \(\displaystyle g=\frac{GM}{r^2}\), \(M\) is in the numerator. Doubling \(M\) doubles the derived field strength at the same separation.

**Feedback for B:** The test mass cancels, but the source mass does not. A larger source mass produces a stronger gravitational field at the same position.

## Common mistakes to repair

**Mistake: cancelling the wrong mass.** The test mass \(m\) cancels because we divide force by that same test mass. The source mass \(M\) does not cancel. It tells us how strong the source's gravitational effect is.

**Mistake: using \(r\) as only height above a planet.** Newton's law needs separation between the centres. At the surface, \(r\) is the radius. Above the surface, \(r\) is radius plus height.

**Mistake: saying that field strength is a force.** Field strength is **force per unit mass**. Its unit is \(\mathrm{N\,kg^{-1}}\), not just \(\mathrm{N}\).

## Core recap

- Newton's law gives \(\displaystyle F=\frac{GMm}{r^2}\) for source mass \(M\), test mass \(m\), and separation \(r\).
- Gravitational field strength is \(\displaystyle g=\frac{F}{m}\).
- Substitution gives \(\displaystyle g=\frac{\frac{GMm}{r^2}}{m}\).
- The test mass cancels, giving \(\displaystyle g=\frac{GM}{r^2}\).
- The derived result is independent of the test mass. Its direction is towards the source mass.

The next lesson will use this relationship and explain why field strength is approximately constant for small height changes near Earth's surface.
