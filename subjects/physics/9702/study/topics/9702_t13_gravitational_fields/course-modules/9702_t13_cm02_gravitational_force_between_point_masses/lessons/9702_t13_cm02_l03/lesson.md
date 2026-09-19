# Circular orbits and geostationary satellites

## A satellite that keeps falling

Imagine throwing a ball sideways. Gravity pulls it down, so it follows a curved path. If it is moving sideways fast enough and there is no air, the curved path can keep bending around a planet. The object is then in a **circular orbit**.

A satellite in a circular orbit is not held up by a second force. The planet's gravitational force pulls it continuously towards the planet's centre. This inward force changes the **direction** of the satellite's velocity. That change of direction is its **centripetal acceleration**.

Teacher question: if a satellite moves at constant speed, is its velocity constant? No. **Velocity** includes direction, and the direction changes at every point on a circular path.

## One force, two descriptions

The same gravitational force has two useful descriptions in this situation.

<a id="definition-newtons-law"></a>
> **Definition to learn: Newton's law of gravitation.**
> gravitational force is directly proportional to the product of the masses and inversely proportional to the square of their separation

"Directly proportional to the product" means that increasing either mass increases the force. "Inversely proportional to the square" means that doubling the separation makes the force one quarter as large. This exact definition was learned in the preceding lesson and is needed again here.

<a id="formula-gravitation"></a>
> **Formula to learn: Newton's law of gravitation.**
> \[
> F = \frac{G m_1 m_2}{r^2}
> \]

This tells us the gravitational force between two point masses. Here, for a satellite orbiting a planet:

- \(F\) is the gravitational force, in newtons (\(\mathrm{N}\)).
- \(G\) is the gravitational constant, \(6.67 \times 10^{-11}\,\mathrm{N\,m^2\,kg^{-2}}\).
- \(M\) is the mass of the planet, in kilograms (\(\mathrm{kg}\)).
- \(m\) is the mass of the satellite, in kilograms.
- \(r\) is the distance from the **centre of the planet** to the **centre of the satellite**, in metres (\(\mathrm{m}\)). It is the orbital radius, not the height above the surface.

For an orbit, this force points towards the centre of the circle. It is therefore the centripetal force.

<a id="formula-centripetal-force"></a>
> **Formula to learn: Centripetal force.**
> \[
> F = \frac{mv^2}{r} = mr\omega^2
> \]

For this lesson, use \(F = mv^2/r\) when the satellite's linear speed \(v\) is known or required.

- \(v\) is the satellite's linear speed, in \(\mathrm{m\,s^{-1}}\).
- \(r\) is the orbital radius, in \(\mathrm{m}\).
- \(m\) is the satellite mass, in \(\mathrm{kg}\).

The formula applies when an object moves in a circle of radius \(r\). It gives the **resultant inward force**, not an additional outward force. In this orbit, gravity supplies that resultant force.

<a id="formula-newtons-second-law"></a>
> **Formula to learn: Newton's second law of motion.**
> \[
> F = \frac{\Delta p}{\Delta t} = ma
> \]

For a satellite of constant mass, the useful part is \(F=ma\). The resultant force \(F\) causes acceleration \(a\). In a circular orbit, that acceleration points inwards, towards the centre.

<a id="formula-centripetal-acceleration"></a>
> **Formula to learn: Centripetal acceleration.**
> \[
> a = r\omega^2 = \frac{v^2}{r} = \frac{4\pi^2 r}{T^2}
> \]

Here \(a\) is inward centripetal acceleration in \(\mathrm{m\,s^{-2}}\), \(\omega\) is angular speed in \(\mathrm{rad\,s^{-1}}\), and \(T\) is period in seconds. The force equation above is the same relationship after multiplying this acceleration by the satellite mass.

Teacher question: why can we set the two expressions for \(F\) equal? They are both calculating the one gravitational force acting on the same satellite.

So write:

\[
\frac{GMm}{r^2}=\frac{mv^2}{r}
\]

The satellite mass \(m\) appears on both sides. Divide both sides by \(m\):

\[
\frac{GM}{r^2}=\frac{v^2}{r}
\]

Multiply both sides by \(r\):

\[
v^2=\frac{GM}{r}
\]

Taking the positive square root gives the speed:

\[
v=\sqrt{\frac{GM}{r}}
\]

This result explains an important orbit fact. The satellite mass has cancelled. At the same orbital radius around the same planet, a light satellite and a heavy satellite have the same orbital speed.

### Worked example: find an orbital speed

A satellite moves in a circular orbit of radius \(1.90 \times 10^7\,\mathrm{m}\) around a planet of mass \(5.50 \times 10^{24}\,\mathrm{kg}\). Find its speed.

The question gives a planet mass and an orbital radius. The orbit is circular, so gravity supplies the centripetal force. Use:

\[
v=\sqrt{\frac{GM}{r}}
\]

Substitute the values, keeping units visible:

\[
v=\sqrt{\frac{(6.67\times10^{-11}\,\mathrm{N\,m^2\,kg^{-2}})(5.50\times10^{24}\,\mathrm{kg})}{1.90\times10^7\,\mathrm{m}}}
\]

\[
v=\sqrt{1.93\times10^7\,\mathrm{m^2\,s^{-2}}}
\]

\[
v=4.39\times10^3\,\mathrm{m\,s^{-1}}
\]

**Answer: \(v=4.39\times10^3\,\mathrm{m\,s^{-1}}\).**

The unit works because the square root of \(\mathrm{m^2\,s^{-2}}\) is \(\mathrm{m\,s^{-1}}\). A speed of several thousand metres per second is reasonable for a satellite orbiting a planet.

### A common mistake: using altitude as \(r\)

It is tempting to put the satellite's height above the ground into \(r\). That is not correct. Both gravitational-force and circular-motion equations use the distance to the centre of the planet.

If Earth has radius \(R_{\mathrm{E}}\) and a satellite is at height \(h\), then:

\[
r=R_{\mathrm{E}}+h
\]

Teacher question: a satellite is \(600\,\mathrm{km}\) above Earth. Is \(r\) equal to \(600\,\mathrm{km}\)? No. The Earth radius must be added first, and the final value should be in metres.

The force is also perpendicular to the satellite's instantaneous direction of motion. A perpendicular force changes direction but does no work on the satellite at that instant. This is why a circular-orbit satellite can have constant speed while its velocity keeps changing.

The satellite has two possible orbit radii around the same planet. Which one has the greater speed?

- **A:** The smaller orbit radius.
- **B:** The larger orbit radius.

**Feedback for A:** Correct. In \(v=\sqrt{GM/r}\), \(G\) and \(M\) are fixed for one planet. A smaller \(r\) makes \(GM/r\) larger, so \(v\) is larger.

**Feedback for B:** Not correct. A larger orbit needs a smaller speed, not a larger one. The satellite is farther from the planet, so gravity is weaker and provides less centripetal force.

## From speed to orbital period

The **orbital period**, \(T\), is the time for one complete orbit. In one orbit, the satellite travels the circumference \(2\pi r\). Therefore:

\[
v=\frac{2\pi r}{T}
\]

Substitute this expression for \(v\) into \(v^2=GM/r\):

\[
\left(\frac{2\pi r}{T}\right)^2=\frac{GM}{r}
\]

\[
\frac{4\pi^2r^2}{T^2}=\frac{GM}{r}
\]

Multiply both sides by \(rT^2\):

\[
4\pi^2r^3=GMT^2
\]

Rearrange:

\[
T^2=\frac{4\pi^2r^3}{GM}
\]

For a given planet, \(G\) and \(M\) are constant. Therefore, a larger orbit radius gives a longer orbital period.

## What makes an orbit geostationary?

A **geostationary satellite** remains above the same point on Earth's surface. Its orbit must meet all four conditions below:

1. It has an **orbital period of 24 hours**.
2. It orbits **from west to east**, the same direction as Earth rotates.
3. Its orbit is **directly above the Equator**.
4. It is circular and has the same angular speed as Earth.

The first condition alone is not enough. A satellite with a 24-hour period but an orbit tilted relative to the Equator would appear to move north and south in the sky. A satellite travelling east to west would pass over a point rather than remain above it.

Teacher question: why must the satellite travel west to east? It must turn around Earth's axis in the same direction as Earth's surface so that their relative angular positions do not change.

### Worked example: estimate a geostationary orbit radius

Use \(M=5.97\times10^{24}\,\mathrm{kg}\) for Earth. Find the radius of a circular orbit with period \(24.0\,\mathrm{h}\).

First convert the period to seconds. The formulas use SI units:

\[
T=24.0\,\mathrm{h}\times3600\,\mathrm{s\,h^{-1}}
\]

\[
T=8.64\times10^4\,\mathrm{s}
\]

Rearrange the period equation to make \(r^3\) the subject:

\[
r^3=\frac{GMT^2}{4\pi^2}
\]

Substitute:

\[
r^3=\frac{(6.67\times10^{-11})(5.97\times10^{24})(8.64\times10^4)^2}{4\pi^2}\,\mathrm{m^3}
\]

\[
r^3=7.53\times10^{22}\,\mathrm{m^3}
\]

Now take the cube root, not the square root:

\[
r=\sqrt[3]{7.53\times10^{22}\,\mathrm{m^3}}
\]

\[
r=4.22\times10^7\,\mathrm{m}
\]

**Answer: \(r=4.22\times10^7\,\mathrm{m}\) from Earth's centre.**

This is much larger than Earth's radius, about \(6.37\times10^6\,\mathrm{m}\). That is sensible: a 24-hour orbit is a relatively slow, wide orbit. The corresponding height above Earth's surface is about \(3.59\times10^7\,\mathrm{m}\), but the orbital equations used the centre-to-centre radius.

A satellite has a circular orbit directly above the Equator and travels west to east. Its period is \(12\) hours. Does it remain above one point on Earth?

- **A:** Yes, because its orbit is above the Equator and travels in the correct direction.
- **B:** No, because its period does not match Earth's 24-hour rotation.

**Feedback for A:** Not correct. Equatorial position and direction are necessary, but the satellite must also have a 24-hour period. In 12 hours it completes one orbit while Earth has turned through only half a rotation.

**Feedback for B:** Correct. The satellite needs the same angular speed as Earth. A 12-hour period means it moves around Earth too quickly to remain over one surface point.

## Core recap

- In a circular orbit, **gravity is the centripetal force**. It points towards the centre and changes the direction of velocity.
- Equate \(GMm/r^2\) with \(mv^2/r\) to analyse a circular gravitational orbit.
- The orbital speed is \(v=\sqrt{GM/r}\). Satellite mass cancels.
- Use \(r\) from the planet's centre, not the height above the surface.
- A geostationary satellite has a **24-hour period**, travels **west to east**, and orbits **directly above the Equator**, so it remains above one Earth-surface point.
- Do not introduce the point-mass gravitational-field-strength equation yet. The next lesson derives it from Newton's law of gravitation and the definition of gravitational field strength.
