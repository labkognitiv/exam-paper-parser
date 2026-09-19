# Choosing and using an equation

Imagine timing a trolley on a straight track. You may know its initial velocity, acceleration and time. In another problem, you may know two velocities and a displacement but not the time. The arithmetic is useful only after you choose the equation that matches the information.

Before choosing, ask two questions.

1. Is the motion along one straight line?
2. Is the acceleration constant in magnitude and direction for the whole interval?

If either answer is no, these equations do not model the whole interval. If both answers are yes, choose a positive direction. A negative value then means the opposite direction.

## Write a symbol list first

For one selected interval of motion:

- **\(u\)** is initial velocity, in \(\mathrm{m\,s^{-1}}\).
- **\(v\)** is final velocity, in \(\mathrm{m\,s^{-1}}\).
- **\(a\)** is constant acceleration, in \(\mathrm{m\,s^{-2}}\).
- **\(s\)** is displacement, in \(\mathrm{m}\).
- **\(t\)** is the time interval, in \(\mathrm{s}\).

Teacher question: *Which symbol does “starts from rest” fix?* It gives \(u=0\). “Stops” gives \(v=0\). Mark this information before selecting an equation.

Write the target quantity. Then look for an equation containing that target and only known quantities. Do not choose an equation merely because you used it in the previous question.

## When time is known

### Formula: Constant-acceleration velocity

> **Formula to learn: Constant-acceleration velocity.**
>
> \[
> v = u + at
> \]

Use this when you need a velocity, acceleration or time and displacement is not required. The term \(at\) is the change in velocity. Its unit is

\[
\mathrm{m\,s^{-2}}\times\mathrm{s}=\mathrm{m\,s^{-1}}
\]

so it can be added to \(u\). The formula requires straight-line motion with constant acceleration.

Teacher question: *A car has \(u=18\ \mathrm{m\,s^{-1}}\), \(a=-3.0\ \mathrm{m\,s^{-2}}\), and \(t=2.0\ \mathrm{s}\). What is \(at\)?*

- **A:** \(-6.0\ \mathrm{m\,s^{-1}}\)
- **B:** \(+6.0\ \mathrm{m\,s^{-1}}\)

**Feedback for A:** Correct. \(at=(-3.0)(2.0)=-6.0\ \mathrm{m\,s^{-1}}\). The velocity decreases by \(6.0\ \mathrm{m\,s^{-1}}\).

**Feedback for B:** Not correct. Positive time multiplied by negative acceleration gives a negative change in velocity.

### Formula: Constant-acceleration displacement

> **Formula to learn: Constant-acceleration displacement.**
>
> \[
> s = ut + \frac{1}{2}at^2
> \]

Use this when \(u\), \(a\) and \(t\) are known and the target is displacement. The first term is the displacement at the initial velocity. The second term adjusts it because the velocity changes.

Both terms have unit metre:

\[
\mathrm{m\,s^{-1}}\times\mathrm{s}=\mathrm{m}
\]

\[
\mathrm{m\,s^{-2}}\times\mathrm{s^2}=\mathrm{m}
\]

### Worked example 1: displacement with time given

A train moves in a straight line. Its initial velocity is \(4.0\ \mathrm{m\,s^{-1}}\). It accelerates constantly at \(1.5\ \mathrm{m\,s^{-2}}\) for \(6.0\ \mathrm{s}\). Find its displacement.

**Decision:** The target is \(s\), and \(u\), \(a\) and \(t\) are known. Use \(s=ut+\frac12at^2\). Take the direction of travel as positive.

\[
s=(4.0\ \mathrm{m\,s^{-1}})(6.0\ \mathrm{s})+\frac12(1.5\ \mathrm{m\,s^{-2}})(6.0\ \mathrm{s})^2
\]

\[
s=24\ \mathrm{m}+27\ \mathrm{m}
\]

\[
s=51\ \mathrm{m}
\]

**Answer:** The displacement is **\(51\ \mathrm{m}\)** forward.

**Check:** \(51\ \mathrm{m}\) in \(6.0\ \mathrm{s}\) gives an average velocity of \(8.5\ \mathrm{m\,s^{-1}}\). This is sensible because the train speeds up from \(4.0\ \mathrm{m\,s^{-1}}\).

## When time is absent

### Formula: Constant-acceleration velocity and displacement

> **Formula to learn: Constant-acceleration velocity and displacement.**
>
> \[
> v^2 = u^2 + 2as
> \]

Use this equation when time is not known and is not needed. It links the two velocities, acceleration and displacement. Its conditions are still straight-line motion and constant acceleration.

The unit of \(v^2\) is \(\mathrm{m^2\,s^{-2}}\). The term \(as\) has the same unit:

\[
\mathrm{m\,s^{-2}}\times\mathrm{m}=\mathrm{m^2\,s^{-2}}
\]

Matching units checks the algebra. It does not prove that the motion has constant acceleration.

Teacher question: *A cyclist's initial velocity, final velocity, constant acceleration and displacement are known, but time is not. Which equation fits directly?*

- **A:** \(v^2=u^2+2as\)
- **B:** \(s=ut+\frac12at^2\)

**Feedback for A:** Correct. It contains \(u\), \(v\), \(a\) and \(s\), but no time.

**Feedback for B:** Not correct. It contains \(t\), an extra unknown. It is not the direct route in this situation.

### Worked example 2: braking distance without time

A car travels at \(22\ \mathrm{m\,s^{-1}}\). It brakes with constant acceleration \(-5.5\ \mathrm{m\,s^{-2}}\) until it stops. Find its displacement while braking.

**Decision:** Time is absent. “Stops” means \(v=0\ \mathrm{m\,s^{-1}}\). Choose \(v^2=u^2+2as\). Take the original direction of travel as positive.

Rearrange before substituting:

\[
v^2-u^2=2as
\]

\[
s=\frac{v^2-u^2}{2a}
\]

Substitute signed values:

\[
s=\frac{(0\ \mathrm{m\,s^{-1}})^2-(22\ \mathrm{m\,s^{-1}})^2}{2(-5.5\ \mathrm{m\,s^{-2}})}
\]

\[
s=\frac{-484\ \mathrm{m^2\,s^{-2}}}{-11\ \mathrm{m\,s^{-2}}}
\]

\[
s=44\ \mathrm{m}
\]

**Answer:** The car travels **\(44\ \mathrm{m}\)** forward while braking.

**Check:** Both numerator and denominator are negative, so a positive displacement is expected. The units cancel to metres.

## A reliable choice routine

1. Check the model conditions and choose a positive direction.
2. Write the target quantity and the five symbols you know.
3. Include hidden information: at rest means \(u=0\), and stops means \(v=0\).
4. Reject an equation containing an unnecessary unknown.
5. Rearrange first, then substitute values with units.
6. Check the final sign, unit and physical meaning.

A common mistake is using \(v=u+at\) when time is absent. That introduces an extra unknown. The 2023 car pattern instead uses the no-time equation, with \(u=0\), then rearranges to find acceleration.

## Core recap

- Use these equations only for **straight-line motion** with **constant acceleration**.
- **\(v=u+at\)** links velocity, acceleration and time.
- **\(s=ut+\frac12at^2\)** finds displacement when \(u\), \(a\) and \(t\) are known.
- **\(v^2=u^2+2as\)** is the direct route when time is absent.
- Keep signs and units until the final answer. Negative acceleration can mean an object is slowing down while still moving in the positive direction.
