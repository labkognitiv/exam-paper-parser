# Newton's law of gravitation and the point-mass model

Imagine standing outside a large, round planet. You are not touching the
planet, but it still pulls you towards its centre. How can one equation describe
that pull for a planet, a moon, two laboratory spheres, or two stars?

This lesson answers that question. You will learn when a **uniform sphere** can
be treated as though all its mass were at one point, and how to calculate the
**gravitational force** between two point masses. The next lesson uses this
force to explain circular orbits. We will not do orbital calculations here.

## The useful model outside a uniform sphere

In the previous lesson, you met a **gravitational field**: a region where a
mass experiences a gravitational force. Now we focus on the mass producing
that field.

A **uniform sphere** has its mass spread evenly through its volume. For a point
**outside** such a sphere, Cambridge allows a very useful model:

> **Term meaning: point-mass model.** For calculations outside a uniform
> sphere, treat the sphere's whole mass as if it were concentrated at its
> centre.

This does not say that the planet has literally collapsed into a point. It is a
model that gives the correct external gravitational force.

Suppose a satellite is above a planet's surface. The distance needed in a
gravity calculation is not its height above the ground. It is the distance from
the **centre of the planet** to the **centre of the satellite**. We call this
centre-to-centre distance \(r\).

**Teacher question:** A satellite is \(400\,\mathrm{km}\) above a planet with
radius \(6400\,\mathrm{km}\). Is \(r\) equal to \(400\,\mathrm{km}\), or to
\(6800\,\mathrm{km}\)?

- **A.** \(400\,\mathrm{km}\), because that is the stated height.
- **B.** \(6800\,\mathrm{km}\), because the distance is measured from the
  planet's centre.

**Feedback for A:** This uses a surface-to-satellite distance. Newton's law
uses the separation of the two masses, so it is not the required \(r\).

**Feedback for B:** Correct. Add radius and height:
\(6400\,\mathrm{km}+400\,\mathrm{km}=6800\,\mathrm{km}\). Convert this to
metres before using SI units.

The model has a boundary. It applies to a point **outside** a uniform sphere.
Do not assume that the same simple centre model describes points inside a
non-uniform body, or a situation where other forces are important.

## Newton's law in words

Two masses attract each other. A larger mass produces a larger pull. A larger
second mass also experiences a larger pull. So the force depends on the
**product of the masses**.

Distance matters strongly too. If the centre-to-centre separation doubles,
the force does not merely halve. It becomes one quarter as large. This is an
**inverse-square** relationship.

### Newton's law of gravitation

> **Definition to learn: Newton's law of gravitation.** gravitational force is directly proportional to the product of the masses and inversely proportional to the square of their separation

The exact definition is what you should learn for an exam. In plain language:

- Make either mass twice as large, and the force becomes twice as large.
- Make both masses twice as large, and the force becomes four times as large.
- Make \(r\) twice as large, and \(r^2\) becomes four times as large, so the
  force becomes one quarter as large.

The phrase **directly proportional** means two quantities change by the same
factor. The phrase **inversely proportional to the square** means the quantity
is divided by \(r^2\), not by \(r\).

What should happen to the gravitational force if the separation becomes three
times larger? Pause and square the factor before reading on. The denominator
becomes \(3^2=9\) times larger, so the force becomes **one ninth** as large.

## The calculation form of the law

> **Formula to learn: Newton's law of gravitation.**
>
> \[
> F = \frac{G m_1 m_2}{r^2}
> \]

This equation calculates the **magnitude** of the attractive gravitational
force between two point masses. For a point outside a uniform sphere, use its
mass at the sphere's centre.

Here is what every symbol means:

| Symbol | Meaning | SI unit |
|---|---|---|
| \(F\) | gravitational force | newton, \(\mathrm{N}\) |
| \(G\) | universal gravitational constant | \(\mathrm{N\,m^2\,kg^{-2}}\) |
| \(m_1\), \(m_2\) | the two masses | kilogram, \(\mathrm{kg}\) |
| \(r\) | separation of their centres | metre, \(\mathrm{m}\) |

Use \(G=6.67\times10^{-11}\,\mathrm{N\,m^2\,kg^{-2}}\) unless a question
supplies a different value. The small value helps explain why the gravitational
attraction between ordinary objects is usually too weak to notice.

Notice the units before you calculate:

\[
[F]=\frac{(\mathrm{N\,m^2\,kg^{-2}})(\mathrm{kg})(\mathrm{kg})}{\mathrm{m^2}}
\]

\[
[F]=\mathrm{N}
\]

The kilograms and square metres cancel, leaving newtons. That is the correct
unit for force.

### Worked example 1: force between a planet and a spacecraft

A spacecraft of mass \(1200\,\mathrm{kg}\) is \(1.6\times10^6\,\mathrm{m}\)
above the surface of a uniform planet. The planet has radius
\(6.4\times10^6\,\mathrm{m}\) and mass \(6.0\times10^{24}\,\mathrm{kg}\).
Find the gravitational force on the spacecraft.

First decide what the two masses are. The planet is a uniform sphere and the
spacecraft is outside it, so use the point-mass model for the planet.

The separation is centre to centre, not the height:

\[
r=6.4\times10^6\,\mathrm{m}+1.6\times10^6\,\mathrm{m}
\]

\[
r=8.0\times10^6\,\mathrm{m}
\]

Newton's law fits because we need the force between the planet and the
spacecraft:

\[
F=\frac{Gm_1m_2}{r^2}
\]

\[
F=\frac{(6.67\times10^{-11})(6.0\times10^{24})(1200)}{(8.0\times10^6)^2}
\]

Square the whole separation:

\[
(8.0\times10^6)^2=6.4\times10^{13}\,\mathrm{m^2}
\]

\[
F=7.5\times10^3\,\mathrm{N}
\]

**Answer: \(7.5\times10^3\,\mathrm{N}\), directed towards the planet's
centre.**

The unit is newtons, so the calculation has produced a force. The direction is
attractive. The spacecraft pulls the planet with the same magnitude in the
opposite direction, although the planet's acceleration is much smaller because
its mass is far larger.

## A fast route when only a factor changes

Sometimes you do not need to substitute numbers. Compare the two situations
instead.

From the formula,

\[
F\propto\frac{m_1m_2}{r^2}
\]

This is not a new formula to memorise. It is the proportional relationship
already contained in Newton's law.

### Worked example 2: comparing two separations

The masses of two objects stay unchanged. Their centre-to-centre separation
changes from \(r\) to \(3r\). The original force is \(F\). Find the new force.

The masses have not changed. Only the separation changes, so focus on the
\(r^2\) in the denominator.

\[
F_{\text{new}}\propto\frac{1}{(3r)^2}
\]

\[
F_{\text{new}}\propto\frac{1}{9r^2}
\]

So the new force is one ninth of the old force:

\[
F_{\text{new}}=\frac{F}{9}
\]

**Answer: the force becomes \(F/9\).**

The important check is the square. A result of \(F/3\) would treat the law as
an inverse-distance law, which it is not.

**Teacher question:** Two point masses keep the same separation. One mass
doubles and the other mass triples. What happens to the force?

- **A.** It becomes \(6F\).
- **B.** It becomes \(5F\).

**Feedback for A:** Correct. The formula contains the product \(m_1m_2\).
The factor is \(2\times3=6\), so the force becomes \(6F\).

**Feedback for B:** Adding the factors would be appropriate only for a sum.
Newton's law uses a product of the two masses, so multiply the factors instead.

## A common mistake: using the gap between surfaces

Suppose two spherical bodies are close together. It is tempting to use the
empty gap between their surfaces as \(r\). That gives a force that is far too
large because the denominator is too small.

Always ask: **Where is the mass represented in this model?** For a uniform
sphere, it is represented at its centre. Therefore, measure from centre to
centre.

There is a second important limitation. The calculation assumes the objects
can be treated as **point masses**, or as uniform spheres observed from
outside. In a real experiment, nearby equipment, non-uniform density, or other
electrical and magnetic forces may make a measured force differ from the simple
prediction. That does not make Newton's law useless. It tells you to check
whether the model's conditions match the situation.

## Core recap

- Outside a **uniform sphere**, treat its mass as a **point mass at its
  centre**.
- Use the centre-to-centre separation \(r\), in **metres**.
- Learn the exact law: gravitational force is directly proportional to the
  product of the masses and inversely proportional to the square of their
  separation.
- Use \(\displaystyle F=\frac{Gm_1m_2}{r^2}\), with masses in
  **kilograms**, to find a force in **newtons**.
- Double \(r\), and the force becomes one quarter. Triple \(r\), and it
  becomes one ninth.
- The force is **attractive** and acts along the line joining the two centres.

The next lesson will take this gravitational force and ask what happens when it
provides the inward force needed for a circular orbit.
