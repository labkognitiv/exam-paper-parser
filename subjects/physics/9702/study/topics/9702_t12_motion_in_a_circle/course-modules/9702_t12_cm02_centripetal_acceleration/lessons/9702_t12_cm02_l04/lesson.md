# Centripetal acceleration and centripetal force

## A car that is always turning

A car can travel around a circular track at constant speed. It is not speeding up
or slowing down, but its velocity changes because its direction changes.

The previous lesson showed that an inward resultant force causes an inward
acceleration. This is **centripetal acceleration**. The word **centripetal**
means "towards the centre".

This lesson calculates the magnitude of that acceleration and the magnitude of
the required inward resultant force. It does not introduce a new physical force.
Tension, friction, gravity, electric force, or a contact force can provide the
centripetal force when its resultant direction is towards the centre.

First ask: is the object moving in a circle at constant speed? These equations
give magnitudes for **uniform circular motion**.

## Centripetal acceleration

A faster object must turn its velocity direction more rapidly. An object moving
in a tighter circle must also turn more rapidly. This is why centripetal
acceleration depends on speed and radius.

### <a id="formula-centripetal-acceleration"></a>Formula: centripetal acceleration

> **Formula to learn: Centripetal acceleration.**
>
> \[
> a = r\omega^2 = \frac{v^2}{r} = \frac{4\pi^2 r}{T^2}
> \]

For this lesson, use \(a=r\omega^2\) when angular speed is known, and use
\(a=v^2/r\) when linear speed is known.

- \(a\) is centripetal acceleration, in \(\mathrm{m\,s^{-2}}\).
- \(r\) is the radius of the circular path, in \(\mathrm{m}\).
- \(\omega\) is angular speed, in \(\mathrm{rad\,s^{-1}}\).
- \(v\) is linear speed along the tangent, in \(\mathrm{m\,s^{-1}}\).
- \(T\) is the period, in \(\mathrm{s}\).

Notice the squares. If \(v\) doubles while radius is unchanged, \(v^2\)
becomes four times as large. The centripetal acceleration becomes four times
as large, not twice as large.

Suppose two pieces of clay rotate with the same angular speed on a turntable.
Which one has the larger centripetal acceleration?

- **A:** The piece farther from the centre.
- **B:** The piece closer to the centre.

**Feedback for A:** Correct. With \(\omega\) fixed, \(a=r\omega^2\). Larger
\(r\) gives larger \(a\).

**Feedback for B:** Not correct. This would be the wrong comparison condition.
For fixed linear speed, \(a=v^2/r\) gives larger \(a\) for smaller \(r\). State
what is fixed before comparing.

## Worked example: use linear speed

A \(2.4\,\mathrm{kg}\) cart travels at constant speed
\(7.0\,\mathrm{m\,s^{-1}}\) around a circular track of radius
\(14\,\mathrm{m}\). Find its centripetal acceleration.

**Decision.** The known quantities are \(v\) and \(r\), so use
\(a=v^2/r\). The mass is not needed for acceleration.

\[
a=\frac{v^2}{r}
\]

\[
a=\frac{(7.0\,\mathrm{m\,s^{-1}})^2}{14\,\mathrm{m}}
\]

Square the speed before dividing.

\[
(7.0\,\mathrm{m\,s^{-1}})^2=49\,\mathrm{m^2\,s^{-2}}
\]

\[
a=\frac{49\,\mathrm{m^2\,s^{-2}}}{14\,\mathrm{m}}
=3.5\,\mathrm{m\,s^{-2}}
\]

**Answer: \(3.5\,\mathrm{m\,s^{-2}}\), towards the centre.**

Check the unit:

\[
\frac{\mathrm{m^2\,s^{-2}}}{\mathrm{m}}=\mathrm{m\,s^{-2}}
\]

Mass changes the force required, not the acceleration required by a particular
speed and radius.

## Centripetal force

Newton's second law is \(F=ma\). In circular motion, the resultant force and
acceleration point towards the centre. Combining \(F=ma\) with the acceleration
equations gives the centripetal-force equation.

### <a id="formula-centripetal-force"></a>Formula: centripetal force

> **Formula to learn: Centripetal force.**
>
> \[
> F = \frac{mv^2}{r} = mr\omega^2
> \]

- \(F\) is the inward resultant force, in newtons, \(\mathrm{N}\).
- \(m\) is mass, in kilograms, \(\mathrm{kg}\).
- \(v\), \(r\), and \(\omega\) have the meanings and units above.

Use \(F=mv^2/r\) when linear speed is known. Use \(F=mr\omega^2\) when angular
speed is known. The equation applies to the **resultant inward force**.

Do not draw an extra arrow labelled centripetal force. Identify the real force,
or the resultant of real forces, that points inwards. On a level track, static
friction can provide it. For a ball on a string, tension can provide it. For a
satellite, gravity can provide it.

If the same object moves at twice its original linear speed around the same
circle, what happens to the required centripetal force?

- **A:** It becomes four times as large.
- **B:** It becomes twice as large.

**Feedback for A:** Correct. In \(F=mv^2/r\), mass and radius are fixed. If
\(v\) doubles, \(v^2\) is \(2^2=4\) times as large.

**Feedback for B:** Not correct. Force is not directly proportional to \(v\).
The speed is squared before the other operations are done.

## Worked example: use angular speed and find force

A \(0.15\,\mathrm{kg}\) sensor is fixed \(0.30\,\mathrm{m}\) from the axis of
a rotating platform. Its angular speed is \(8.0\,\mathrm{rad\,s^{-1}}\).
Find its centripetal acceleration and the inward resultant force.

**Step 1: calculate acceleration.** The question gives \(r\) and \(\omega\).

\[
a=r\omega^2
\]

\[
a=(0.30\,\mathrm{m})(8.0\,\mathrm{rad\,s^{-1}})^2
\]

\[
a=(0.30\,\mathrm{m})(64\,\mathrm{s^{-2}})
=19.2\,\mathrm{m\,s^{-2}}
\]

The radian is dimensionless in this calculation. The acceleration unit is
therefore \(\mathrm{m\,s^{-2}}\).

**Step 2: calculate force.**

\[
F=ma
\]

\[
F=(0.15\,\mathrm{kg})(19.2\,\mathrm{m\,s^{-2}})
=2.88\,\mathrm{kg\,m\,s^{-2}}
\]

\[
1\,\mathrm{N}=1\,\mathrm{kg\,m\,s^{-2}}
\]

\[
F=2.88\,\mathrm{N}
\]

**Answer: \(a=19.2\,\mathrm{m\,s^{-2}}\) and
\(F=2.88\,\mathrm{N}\), both towards the axis.**

**Check using the formula block directly.**

\[
F=mr\omega^2=(0.15)(0.30)(8.0)^2=2.88\,\mathrm{N}
\]

Both routes agree.

## The radius comparison trap

The formulas below do not disagree:

\[
a=r\omega^2
\]

\[
a=\frac{v^2}{r}
\]

They describe different fixed conditions.

If **angular speed is fixed**, larger \(r\) gives larger \(a\). A point farther
from the centre also has larger linear speed.

If **linear speed is fixed**, smaller \(r\) gives larger \(a\). The object must
turn more sharply in the tighter circle.

Write down the fixed quantity before choosing a formula.

## Worked example: rearrange for radius

A ride car of mass \(420\,\mathrm{kg}\) has angular speed
\(1.6\,\mathrm{rad\,s^{-1}}\). The inward resultant force must not exceed
\(4.3\times10^3\,\mathrm{N}\). Find the largest radius possible.

**Decision.** We know \(F\), \(m\), and \(\omega\), and need \(r\). Use
\(F=mr\omega^2\).

\[
F=mr\omega^2
\]

Divide both sides by \(m\omega^2\).

\[
r=\frac{F}{m\omega^2}
\]

\[
r=\frac{4.3\times10^3\,\mathrm{N}}
{(420\,\mathrm{kg})(1.6\,\mathrm{rad\,s^{-1}})^2}
\]

\[
r=\frac{4300}{420\times2.56}\,\mathrm{m}
=4.00\,\mathrm{m}
\]

**Answer: \(4.0\,\mathrm{m}\) to two significant figures.**

At fixed mass and angular speed, \(F=mr\omega^2\) means force is proportional
to radius. A larger radius would require more than the allowed force.

## Mistakes to repair

### Treating centripetal force as an extra force

This double-counts. **Centripetal force is the inward resultant of real forces
already acting.** Find the inward resultant of tension, friction, gravity, or
contact forces.

### Forgetting the square

The equations contain \(v^2\) and \(\omega^2\). Using \(v/r\) or \(r\omega\)
gives the wrong number and wrong unit.

### Mixing centimetres and metres

If speed is in \(\mathrm{m\,s^{-1}}\), use radius in metres. For example,
\(35\,\mathrm{cm}=0.35\,\mathrm{m}\). Leaving it as 35 changes the result by a
factor of 100.

### Omitting direction

The equations give a magnitude. In a written answer, state that both the
acceleration and resultant force are **towards the centre**.

## Core recap

- **\(a=r\omega^2\)** and **\(a=v^2/r\)** give centripetal acceleration.
- **\(F=mr\omega^2\)** and **\(F=mv^2/r\)** give the required inward resultant
  force.
- Speed and angular speed are squared. Doubling either makes the relevant
  acceleration and force four times as large when other quantities are fixed.
- State what is fixed before comparing circular motions.
- Both \(a\) and \(F\) point **towards the centre**.

