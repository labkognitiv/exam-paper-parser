# Upward motion and measuring \(g\)

Throw a ball vertically upwards. It moves up more slowly each moment, pauses, then moves down more quickly. Gravity acts throughout. It does not switch off at the highest point.

We model vertical straight-line motion with constant acceleration and negligible air resistance. Choose **upwards as positive**. Gravity is downwards, so \(a=-g\). Use the stated value of \(g\), or \(g=9.81\ \mathrm{m\,s^{-2}}\) when none is given.

## The crucial instant at maximum height

At maximum height, the object has stopped moving upwards but has not stopped being accelerated. Its velocity is zero for an instant:

\[
v=0\ \mathrm{m\,s^{-1}}
\]

Its acceleration remains \(a=-g\). This immediately makes the velocity negative, so the object begins to move downwards.

Teacher question: *At the highest point of an upward throw, which statement is correct?*

- **A:** \(v=0\) and \(a=-g\)
- **B:** \(v=0\) and \(a=0\)

**Feedback for A:** Correct. The velocity is momentarily zero, but gravity still acts downwards. With upwards positive, that acceleration is negative.

**Feedback for B:** Not correct. Zero velocity does not mean zero acceleration. An object can be stationary for an instant while its velocity is changing.

## The three equations in vertical motion

The usual constant-acceleration equations still apply. Here \(u\) and \(v\) are vertical velocities, \(s\) is vertical displacement, and \(a=-g\) when upwards is positive. Their units are \(\mathrm{m\,s^{-1}}\), \(\mathrm{m\,s^{-1}}\), \(\mathrm{m}\), \(\mathrm{m\,s^{-2}}\), and \(\mathrm{s}\), respectively.

### Formula: Constant-acceleration velocity

> **Formula to learn: Constant-acceleration velocity.**
>
> \[
> v = u + at
> \]

Use this to find the time to the top when \(u\) is known. At the top, put \(v=0\) and \(a=-g\).

### Formula: Constant-acceleration displacement

> **Formula to learn: Constant-acceleration displacement.**
>
> \[
> s = ut + \frac{1}{2}at^2
> \]

Use this when time is known and you need a vertical displacement. The unit check is \(\mathrm{m\,s^{-1}}\times\mathrm{s}=\mathrm{m}\) and \(\mathrm{m\,s^{-2}}\times\mathrm{s^2}=\mathrm{m}\).

### Formula: Constant-acceleration velocity and displacement

> **Formula to learn: Constant-acceleration velocity and displacement.**
>
> \[
> v^2 = u^2 + 2as
> \]

Use this to find maximum height directly when time is not needed. At the top, put \(v=0\), \(a=-g\), and let \(s\) be the positive upward height.

## Worked example 1: time and maximum height

A ball is thrown vertically upwards with initial velocity \(14.0\ \mathrm{m\,s^{-1}}\). Air resistance is negligible. Find the time to maximum height and the maximum height. Take upwards as positive and use \(g=9.81\ \mathrm{m\,s^{-2}}\).

At the top, \(v=0\ \mathrm{m\,s^{-1}}\). The known values are \(u=+14.0\ \mathrm{m\,s^{-1}}\) and \(a=-9.81\ \mathrm{m\,s^{-2}}\).

### Stage 1: find the time to the top

The target is time, so use \(v=u+at\):

\[
0=14.0+(-9.81)t
\]

\[
-14.0=-9.81t
\]

\[
t=1.43\ \mathrm{s}
\]

### Stage 2: find the height

Time is no longer needed, so use the direct height route:

\[
v^2=u^2+2as
\]

\[
0=(14.0\ \mathrm{m\,s^{-1}})^2+2(-9.81\ \mathrm{m\,s^{-2}})s
\]

\[
19.62s=196\ \mathrm{m^2\,s^{-2}}
\]

\[
s=10.0\ \mathrm{m}
\]

**Answer:** The ball reaches maximum height after **\(1.43\ \mathrm{s}\)**, at **\(10.0\ \mathrm{m}\)** above its release point.

**Check:** A positive \(s\) fits upward-positive motion. The ball slows from \(14.0\ \mathrm{m\,s^{-1}}\) to zero in about \(1.4\ \mathrm{s}\), which is consistent with a downward acceleration near \(10\ \mathrm{m\,s^{-2}}\).

## Keep ascent and descent separate

The motion is continuous, but the highest point is a useful stage boundary because its vertical velocity is known: \(v=0\). For the ascent, upward displacement is positive and \(a=-g\). For the descent from the top, the initial velocity is \(u=0\), the displacement to a lower point is negative, and \(a=-g\). Do not carry the launch velocity into the descent stage.

Teacher question: *A ball is at maximum height and then falls. What is its initial velocity for the descent stage?*

- **A:** \(u=0\ \mathrm{m\,s^{-1}}\)
- **B:** \(u\) is the launch velocity

**Feedback for A:** Correct. Each stage has its own start. At the top, vertical velocity is zero, so the descent starts from rest.

**Feedback for B:** Not correct. The launch velocity belonged to the start of the ascent. Gravity reduced it to zero before descent began.

## Measuring the acceleration of free fall

Hold a small dense ball with an electromagnet above a light gate or electronic contact. Switching off the electromagnet releases the ball from rest and starts a timer. Stop the timer when the ball reaches a known lower position. Measure the vertical height \(s\) between the same reference points each time.

Choose downwards as positive for this experiment. The ball starts from rest, so \(u=0\) and \(a=+g\). Start with the controlled displacement equation:

\[
s=ut+\frac12at^2
\]

Substitute \(u=0\) and \(a=g\):

\[
s=\frac12gt^2
\]

This is a derived working relationship, not an additional controlled formula. For one run, rearrange it:

\[
2s=gt^2
\]

\[
g=\frac{2s}{t^2}
\]

For several heights, plot **\(s\)** on the vertical axis against **\(t^2\)** on the horizontal axis. The relationship predicts a straight line through the origin. Its gradient is \(g/2\), so double the gradient to obtain \(g\). A range of heights is better than trusting one timing result.

### Worked example 2: calculate \(g\) from one timed fall

A ball is released from rest and falls \(1.80\ \mathrm{m}\). An electronic timer gives \(t=0.606\ \mathrm{s}\). Calculate \(g\).

**Decision:** The ball starts from rest and falls vertically. Use the derived form of the controlled displacement equation, \(g=2s/t^2\).

\[
g=\frac{2(1.80\ \mathrm{m})}{(0.606\ \mathrm{s})^2}
\]

\[
g=\frac{3.60\ \mathrm{m}}{0.367\ \mathrm{s^2}}
\]

\[
g=9.81\ \mathrm{m\,s^{-2}}
\]

**Answer:** \(g=9.81\ \mathrm{m\,s^{-2}}\).

**Check:** Metres divided by seconds squared give \(\mathrm{m\,s^{-2}}\), the unit of acceleration. The result is close to the expected value near Earth's surface.

## Improving the experiment

- Use a **dense, compact ball** and a short enough drop that air resistance is negligible.
- Use electronic timing rather than a hand-held stopwatch. Reaction time is a large uncertainty for a short fall.
- Release the ball with an electromagnet. This avoids an initial push and makes \(u=0\) more reliable.
- Measure the height from the same reference points each time. A changed start or finish position changes \(s\).
- Repeat readings at each height and use a mean time. Then use several heights and a graph to reduce the effect of one unusual reading.

## Core recap

- With upwards positive, **\(a=-g\)** throughout ascent and descent.
- At maximum height, **\(v=0\)** but acceleration is still \(-g\).
- Use **\(v=u+at\)** for time to the top and **\(v^2=u^2+2as\)** for maximum height when time is not needed.
- For a fall released from rest, \(s=\frac12gt^2\), so one-run processing gives \(g=2s/t^2\). A graph of \(s\) against \(t^2\) has gradient \(g/2\).
