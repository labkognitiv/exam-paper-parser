# Gravitational potential and gravitational potential energy around a point mass

Imagine lifting a satellite away from a planet. At first, the planet pulls it back strongly. Far away, that pull becomes weaker. The energy needed to move the satellite depends on its distance from the **centre** of the planet, not its height above the surface.

In the previous lesson, gravitational potential was defined as work done per unit mass. This lesson turns that idea into two equations for an isolated **point mass** or a uniform sphere viewed from outside it.

By the end, you should be able to find:

- the **gravitational potential** \(\phi\) at a distance \(r\) from a mass \(M\)
- the **gravitational potential energy** \(E_{\mathrm{p}}\) of a mass \(m\) at that point
- the signed change in gravitational potential energy when an object moves between two distances.

## Start with the reference point

For an isolated mass, we choose gravitational potential to be **zero at infinity**. Infinity means so far away that the gravitational effect can be treated as zero.

<a id="definition-gravitational-potential"></a>
> **Definition to learn: gravitational potential.** work done per unit mass in bringing a small test mass from infinity to the point

The phrase **per unit mass** means per kilogram. Potential is a property of the location in the field. It does not depend on which test mass you choose.

Gravity is attractive. If a small mass moves slowly from infinity towards a planet, gravity pulls it in. An external agent would need to do negative work to stop the mass speeding up. Therefore the potential at any finite distance from an isolated mass is **negative**.

Ask yourself: if a location is farther from the planet, should its potential be more negative or closer to zero? It should be **closer to zero**, because less work per kilogram is associated with moving from infinity to that location.

## Potential due to one point mass

For a mass \(M\), the gravitational potential at distance \(r\) from its centre is given by the following controlled formula.

<a id="formula-gravitational-potential-point-mass"></a>
> **Formula to learn: Gravitational potential due to a point mass.**
>
> \[
> \phi = -\frac{GM}{r}
> \]

Here:

- \(\phi\) is **gravitational potential**, measured in \(\mathrm{J\,kg^{-1}}\)
- \(G\) is the gravitational constant, \(6.67\times10^{-11}\,\mathrm{N\,m^2\,kg^{-2}}\)
- \(M\) is the mass producing the field, measured in \(\mathrm{kg}\)
- \(r\) is the distance from the **centre** of \(M\), measured in \(\mathrm{m}\).

This equation applies outside an isolated, spherical mass when its mass can be treated as concentrated at its centre. It also applies directly to a point mass.

The minus sign is not optional. It records the chosen zero at infinity and the attractive nature of gravity. Do not report only the magnitude unless the question explicitly asks for a magnitude.

Notice the inverse relationship. If \(r\) doubles, \(\phi\) becomes half as negative. For example, a potential of \(-12\,\mathrm{J\,kg^{-1}}\) becomes \(-6\,\mathrm{J\,kg^{-1}}\), not \(-24\,\mathrm{J\,kg^{-1}}\). The value has increased because \(-6\) is greater than \(-12\).

### Worked example 1: potential above a planet

A planet has mass \(6.00\times10^{24}\,\mathrm{kg}\) and radius \(6.40\times10^6\,\mathrm{m}\). A spacecraft is \(9.00\times10^5\,\mathrm{m}\) above the surface. Find the gravitational potential at the spacecraft.

**Decision.** The formula needs the centre-to-spacecraft distance. The given height is measured from the surface, so it is not yet \(r\).

\[
r=6.40\times10^6\,\mathrm{m}+9.00\times10^5\,\mathrm{m}
\]

\[
r=7.30\times10^6\,\mathrm{m}
\]

Now use the point-mass potential formula.

\[
\phi=-\frac{GM}{r}
\]

\[
\phi=-\frac{(6.67\times10^{-11}\,\mathrm{N\,m^2\,kg^{-2}})(6.00\times10^{24}\,\mathrm{kg})}{7.30\times10^6\,\mathrm{m}}
\]

\[
\phi=-5.48\times10^7\,\mathrm{J\,kg^{-1}}
\]

**Answer: \(\boldsymbol{\phi=-5.48\times10^7\,\mathrm{J\,kg^{-1}}}\).**

**Check.** The potential is negative, as it must be near an isolated attractive mass. Its unit is energy per unit mass, \(\mathrm{J\,kg^{-1}}\). The potential at the spacecraft is less negative than at the planet surface because the spacecraft is farther from the centre.

Suppose the spacecraft moved to twice this centre distance. Which statement is right?

**A.** Its gravitational potential would be twice as negative.

**B.** Its gravitational potential would be half as negative.

**Feedback.** **B is correct.** In \(\phi=-GM/r\), doubling \(r\) halves the magnitude of \(\phi\), so the negative value moves closer to zero. **A is tempting** if you remember that distance matters but forget that \(r\) is in the denominator.

## From potential to potential energy

Potential is energy per kilogram. If you place an object of mass \(m\) at a point where the potential is \(\phi\), multiply by its mass to obtain that object's gravitational potential energy.

<a id="formula-gravitational-potential-energy"></a>
> **Formula to learn: Gravitational potential energy in a radial field.**
>
> \[
> E_{\mathrm{p}} = m\phi = -\frac{GMm}{r}
> \]

Here:

- \(E_{\mathrm{p}}\) is **gravitational potential energy**, measured in \(\mathrm{J}\)
- \(m\) is the mass placed in the field, measured in \(\mathrm{kg}\)
- \(\phi\), \(G\), \(M\), and \(r\) have the meanings already given.

The first equality, \(E_{\mathrm{p}}=m\phi\), is the key connection. Potential is energy per kilogram. Multiplying by kilograms gives energy in joules.

\[
(\mathrm{J\,kg^{-1}})(\mathrm{kg})=\mathrm{J}
\]

The second equality gives the same energy directly for two point masses, or for an object outside a spherical mass treated as a point mass at its centre.

At any finite distance, \(E_{\mathrm{p}}\) is negative with the infinity-zero convention. A negative energy does not mean that the object has no energy or that the calculation has failed. It means energy must be supplied to separate the two masses all the way to infinity.

## Worked example 2: energy of a satellite in orbit

Use the spacecraft in Worked example 1. Its mass is \(340\,\mathrm{kg}\). Find its gravitational potential energy.

**Decision.** We already know the potential at the spacecraft. The shortest route is \(E_{\mathrm{p}}=m\phi\). This also checks that potential and potential energy are not the same quantity.

\[
E_{\mathrm{p}}=m\phi
\]

\[
E_{\mathrm{p}}=(340\,\mathrm{kg})(-5.48\times10^7\,\mathrm{J\,kg^{-1}})
\]

\[
E_{\mathrm{p}}=-1.86\times10^{10}\,\mathrm{J}
\]

**Answer: \(\boldsymbol{E_{\mathrm{p}}=-1.86\times10^{10}\,\mathrm{J}}\).**

**Check.** The \(\mathrm{kg}\) cancels, leaving joules. The result is negative because the spacecraft is gravitationally bound to the planet. Its magnitude is large because both the planet mass and spacecraft mass are substantial.

You can verify the same result with the direct form.

\[
E_{\mathrm{p}}=-\frac{GMm}{r}
\]

\[
E_{\mathrm{p}}=-\frac{(6.67\times10^{-11})(6.00\times10^{24})(340)}{7.30\times10^6}\,\mathrm{J}
\]

\[
E_{\mathrm{p}}=-1.86\times10^{10}\,\mathrm{J}
\]

The two routes agree because the potential formula was used to find \(\phi\) in the first place.

### A common mix-up: negative versus decreasing

Near a planet, gravitational potential energy is negative. When an object moves **outward**, \(r\) increases and \(-GMm/r\) becomes less negative. Its gravitational potential energy therefore **increases**.

For example, changing from \(-20\,\mathrm{J}\) to \(-8\,\mathrm{J}\) is an increase of \(+12\,\mathrm{J}\). The final value is still negative, but it is higher than before.

When an object moves **inward**, \(r\) decreases and its gravitational potential energy becomes more negative. Its gravitational potential energy decreases. The gravitational field does positive work as it pulls the object inward.

An object is raised from a lower orbit to a higher orbit. What happens to its gravitational potential energy?

**A.** It increases because the final value is less negative.

**B.** It decreases because gravity is weaker at the higher orbit.

**Feedback.** **A is correct.** Moving outward requires energy against the inward gravitational force, and \(-GMm/r\) moves closer to zero as \(r\) increases. **B identifies a true fact**, that gravity is weaker farther out, but reaches the wrong conclusion about energy. A weaker pull does not make the higher position lower in gravitational potential energy.

## Finding a change in gravitational potential energy

Questions often give two distances. First calculate the potential energy at each position. Then use the ordinary change rule:

\[
\Delta E_{\mathrm{p}}=E_{\mathrm{p,final}}-E_{\mathrm{p,initial}}
\]

The subscript **final** means the destination. The subscript **initial** means the starting position. Keep the negative signs until after the subtraction.

For movement outward from \(r_1\) to \(r_2\), where \(r_2>r_1\):

\[
\Delta E_{\mathrm{p}}=-\frac{GMm}{r_2}-\left(-\frac{GMm}{r_1}\right)
\]

\[
\Delta E_{\mathrm{p}}=GMm\left(\frac{1}{r_1}-\frac{1}{r_2}\right)
\]

The final result is positive because \(1/r_1\) is larger than \(1/r_2\). A positive change means the object has gained gravitational potential energy.

Do not memorise the last line without thinking. The reliable method is always final energy minus initial energy. It works whether the object moves outward or inward.

## Worked example 3: change from the surface to a high orbit

A \(360\,\mathrm{kg}\) satellite is moved from the surface of Earth to a circular orbit. Take Earth to have mass \(6.00\times10^{24}\,\mathrm{kg}\), radius \(6.40\times10^6\,\mathrm{m}\), and orbital radius \(2.40\times10^8\,\mathrm{m}\). Find the change in gravitational potential energy.

**Decision.** The start is at Earth's surface, so \(r_1\) is Earth's radius. The final orbit radius is already measured from Earth's centre, so \(r_2\) is \(2.40\times10^8\,\mathrm{m}\).

\[
r_1=6.40\times10^6\,\mathrm{m}
\]

\[
r_2=2.40\times10^8\,\mathrm{m}
\]

Write final minus initial before substituting numbers.

\[
\Delta E_{\mathrm{p}}=-\frac{GMm}{r_2}-\left(-\frac{GMm}{r_1}\right)
\]

\[
\Delta E_{\mathrm{p}}=GMm\left(\frac{1}{r_1}-\frac{1}{r_2}\right)
\]

\[
\Delta E_{\mathrm{p}}=(6.67\times10^{-11})(6.00\times10^{24})(360)
\left(\frac{1}{6.40\times10^6}-\frac{1}{2.40\times10^8}\right)\,\mathrm{J}
\]

\[
\Delta E_{\mathrm{p}}=2.19\times10^{10}\,\mathrm{J}
\]

**Answer: \(\boldsymbol{\Delta E_{\mathrm{p}}=+2.19\times10^{10}\,\mathrm{J}}\).**

**Check.** The satellite moved outward, so the positive sign is sensible. The gravitational potential energy has increased from a more negative value near Earth's surface to a less negative value in orbit. The result is in joules, as required for energy.

If the question asks for the **magnitude** of the change, give \(2.19\times10^{10}\,\mathrm{J}\) without a sign. If it asks for the **change**, include the sign or clearly state that it is an increase.

## Reading a potential-distance graph

The formula \(\phi=-GM/r\) tells you how a graph of potential against distance from the centre behaves outside a planet.

- At the surface, the potential has a negative value.
- As \(r\) increases, the graph rises towards zero.
- It stays below zero at every finite distance.
- The graph flattens as \(r\) becomes very large because the potential approaches zero more slowly.

The graph is not a straight line against \(r\), because potential is proportional to \(-1/r\), not to \(-r\). If potential is plotted against \(1/r\), the relationship is a straight line through the origin with a negative gradient of \(-GM\).

This graph tells the same story as the calculation: far away means less negative potential, not positive potential.

## When to use each equation

Use the potential equation when the question asks for the field property at a location.

\[
\phi=-\frac{GM}{r}
\]

Use the potential-energy equation when the question includes the mass of an object and asks for energy.

\[
E_{\mathrm{p}}=m\phi=-\frac{GMm}{r}
\]

Before either calculation, ask two short questions:

1. Is \(r\) measured from the **centre** of the mass creating the field?
2. Have I kept the **negative sign**?

Those two checks prevent many errors in satellite and planet questions.

## Core recap

- **Gravitational potential** is work done per unit mass in bringing a small test mass from infinity to the point.
- For a point mass or outside a spherical mass, **\(\phi=-GM/r\)**. Potential is measured in **\(\mathrm{J\,kg^{-1}}\)**.
- The zero is at infinity. At a finite distance from an isolated mass, potential is **negative**.
- **Gravitational potential energy** is **\(E_{\mathrm{p}}=m\phi=-GMm/r\)** and is measured in **\(\mathrm{J}\)**.
- Moving outward makes gravitational potential energy **increase** because it becomes less negative. Moving inward makes it **decrease** because it becomes more negative.
- For a change, calculate **final minus initial** and keep all signs until the subtraction is complete.
