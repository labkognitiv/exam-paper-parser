# Uncertainty in derived quantities

A result often comes from more than one measurement. For example, you may find an area from a length and a width, or a density from a mass and a volume. Each measured value has some uncertainty. The final, **derived quantity** must therefore have an uncertainty too.

In this lesson, you will choose the correct rule from the operation in the calculation. You will not guess from the size of the numbers.

## Start with one measurement

Imagine measuring the length of a book as

\[
x=(15.0\pm0.3)\,\mathrm{cm}.
\]

The central value is **15.0 cm**. The \(\pm0.3\,\mathrm{cm}\) tells us how much the measurement may differ from that central value.

> **Term meaning: absolute uncertainty.** The uncertainty written in the same unit as the measured quantity.

Here, the absolute uncertainty is **0.3 cm**. It must have centimetres because it describes a possible change in a length.

The same uncertainty can also be expressed relative to the size of the measurement.

> **Term meaning: fractional uncertainty.** The absolute uncertainty divided by the measured value.

\[
\text{fractional uncertainty}=\frac{\Delta x}{x}
\]

The symbol \(\Delta x\) means the absolute uncertainty in \(x\). A fraction has no physical unit because the centimetres cancel.

> **Term meaning: percentage uncertainty.** The fractional uncertainty multiplied by \(100\%\).

\[
\text{percentage uncertainty}=\frac{\Delta x}{x}\times100\%
\]

For the book:

\[
\frac{0.3\,\mathrm{cm}}{15.0\,\mathrm{cm}}=0.020
\]

\[
0.020\times100\%=2.0\%
\]

So \((15.0\pm0.3)\,\mathrm{cm}\) has a **2.0% percentage uncertainty**.

Ask yourself: if the measured value were much smaller but the absolute uncertainty stayed at \(0.3\,\mathrm{cm}\), would the percentage uncertainty get larger or smaller? It would get larger. The same possible change is a bigger fraction of a small measurement.

When you need to return to an absolute uncertainty, reverse the process:

\[
\Delta x=\left(\frac{\text{percentage uncertainty}}{100}\right)x
\]

For example, **4.0%** of \(25.0\,\mathrm{N}\) is

\[
\Delta F=\frac{4.0}{100}\times25.0\,\mathrm{N}=1.0\,\mathrm{N}.
\]

So the force would be written as \((25.0\pm1.0)\,\mathrm{N}\).

Which statement is correct for \(x=(8.0\pm0.4)\,\mathrm{m}\)?

- **A:** Its percentage uncertainty is \(5\%\).
- **B:** Its percentage uncertainty is \(20\%\).

**Feedback for A:** Correct. \(0.4\div8.0=0.05\), and \(0.05\times100\%=5\%\).

**Feedback for B:** Not correct. \(8.0\div0.4=20\) reverses the fraction. Percentage uncertainty compares the possible change with the measured value, so use \(0.4\div8.0\).

## Let the operation choose the uncertainty form

Before combining uncertainties, calculate the central value in the normal way. Then look at the operation connecting the measured quantities.

- For a **sum or difference**, add **absolute uncertainties**.
- For a **product or quotient**, add **fractional uncertainties** or **percentage uncertainties**.
- If a measured quantity is raised to a power, multiply its fractional or percentage contribution by the size of that power.

These are simple addition rules for uncertainty sizes. A minus sign in the central calculation does not make an uncertainty contribution negative.

## Addition and subtraction use absolute uncertainties

Suppose a metal strip is found by subtracting two scale readings:

\[
a=(48.6\pm0.2)\,\mathrm{mm}
\]

\[
b=(19.1\pm0.1)\,\mathrm{mm}
\]

The strip length is \(L=a-b\).

First calculate the central value:

\[
L=48.6\,\mathrm{mm}-19.1\,\mathrm{mm}=29.5\,\mathrm{mm}.
\]

Both input uncertainties are absolute uncertainties and both are in millimetres. The operation is a difference, so add them:

\[
\Delta L=0.2\,\mathrm{mm}+0.1\,\mathrm{mm}=0.3\,\mathrm{mm}.
\]

Therefore,

\[
\boxed{L=(29.5\pm0.3)\,\mathrm{mm}}
\]

Why add when the measured values were subtracted? The largest possible difference occurs when \(a\) is high and \(b\) is low:

\[
(48.6+0.2)-(19.1-0.1)=29.8\,\mathrm{mm}.
\]

That is \(0.3\,\mathrm{mm}\) above the central answer. The uncertainties widen the possible result in both directions.

The same rule works for a sum. If \(L=L_1+L_2\), add the absolute uncertainties after making sure they use the same unit.

## Multiplication and division use percentage uncertainties

Now consider the area of a rectangular card. Its measured dimensions are

\[
l=(12.0\pm0.1)\,\mathrm{cm}
\]

\[
w=(4.00\pm0.04)\,\mathrm{cm}.
\]

The area is \(A=lw\). This is a product, so percentage uncertainties are the useful form.

### Worked example: area from two uncertain lengths

**Step 1: calculate the central area.**

\[
A=12.0\,\mathrm{cm}\times4.00\,\mathrm{cm}=48.0\,\mathrm{cm^2}.
\]

**Step 2: find each percentage contribution.**

\[
\text{percentage uncertainty in }l
=\frac{0.1}{12.0}\times100\%=0.833\%.
\]

\[
\text{percentage uncertainty in }w
=\frac{0.04}{4.00}\times100\%=1.0\%.
\]

**Step 3: add the contributions because area is a product.**

\[
\text{percentage uncertainty in }A=0.833\%+1.0\%=1.833\%.
\]

**Step 4: convert the combined percentage to an absolute uncertainty.**

\[
\Delta A=\frac{1.833}{100}\times48.0\,\mathrm{cm^2}=0.880\,\mathrm{cm^2}.
\]

Quote the uncertainty sensibly as \(0.9\,\mathrm{cm^2}\). The central value is then written to the same decimal place:

\[
\boxed{A=(48.0\pm0.9)\,\mathrm{cm^2}}
\]

**Check:** \(0.9\div48.0\approx0.019\), or about \(1.9\%\). This is close to the unrounded combined percentage of \(1.833\%\). The small difference is caused by rounding the final absolute uncertainty.

For a quotient, use the same percentage rule. A denominator can change the final result just as a numerator can.

### Worked example: a quotient with three measured inputs

A thin sheet has mass \(m=(60.0\pm0.3)\,\mathrm{g}\), length \(l=(10.0\pm0.1)\,\mathrm{cm}\), and width \(w=(5.00\pm0.05)\,\mathrm{cm}\). A supplied quantity is

\[
Q=\frac{m}{lw}.
\]

**Step 1: calculate the central value.**

\[
Q=\frac{60.0\,\mathrm{g}}{10.0\,\mathrm{cm}\times5.00\,\mathrm{cm}}
=1.20\,\mathrm{g\,cm^{-2}}.
\]

**Step 2: find the three percentage contributions.**

\[
\frac{0.3}{60.0}\times100\%=0.50\%
\]

\[
\frac{0.1}{10.0}\times100\%=1.0\%
\]

\[
\frac{0.05}{5.00}\times100\%=1.0\%.
\]

**Step 3: add them.** The equation contains a product in the denominator, but every measured input contributes positively to the uncertainty size.

\[
\text{percentage uncertainty in }Q=0.50\%+1.0\%+1.0\%=2.50\%.
\]

**Step 4: find the final absolute uncertainty.**

\[
\Delta Q=\frac{2.50}{100}\times1.20\,\mathrm{g\,cm^{-2}}
=0.030\,\mathrm{g\,cm^{-2}}.
\]

\[
\boxed{Q=(1.20\pm0.03)\,\mathrm{g\,cm^{-2}}}
\]

**Check:** the unit of the uncertainty is the same as the unit of \(Q\). The percentage uncertainty has no unit.

## A power repeats a contribution

In \(A=l^2\), the same length is used twice. Its percentage uncertainty must therefore contribute twice.

If \(r=(2.50\pm0.05)\,\mathrm{cm}\), its percentage uncertainty is

\[
\frac{0.05}{2.50}\times100\%=2.0\%.
\]

For the area of a circle, \(A=\pi r^2\). The uncertain radius has power \(2\), so it contributes

\[
2\times2.0\%=4.0\%.
\]

The number \(\pi\) is exact. It is not a measurement, so it contributes **no uncertainty**.

The same idea applies when a power is in a denominator. In \(y=a/b^2\), add the percentage uncertainty in \(a\) and **twice** the percentage uncertainty in \(b\). Do not subtract the denominator contribution. We are finding the size of possible variation, not the signed direction of a change.

For \(z=x^2/y\), where \(x\) has \(1.5\%\) uncertainty and \(y\) has \(2.0\%\) uncertainty, which combined percentage uncertainty is correct?

- **A:** \(5.0\%\)
- **B:** \(1.0\%\)

**Feedback for A:** Correct. The \(x^2\) contribution is \(2\times1.5\%=3.0\%\). Add the \(y\) contribution: \(3.0\%+2.0\%=5.0\%\).

**Feedback for B:** Not correct. Subtracting \(2.0\%\) from \(3.0\%\) treats the denominator as a negative uncertainty contribution. A less certain denominator still makes the final result less certain, so the sizes are added.

## A complete route from measurements to a final result

Here is a longer example. It combines earlier unit conversion with the uncertainty decisions in this lesson.

A result is given by the supplied relation

\[
R=\frac{kL^3}{t^2},
\]

where \(k\) is exact. Measurements are

\[
L=(3.20\pm0.04)\,\mathrm{cm}
\]

and

\[
t=(4.00\pm0.08)\,\mathrm{ms}.
\]

When SI units are used, \(R\) is in watts. Let \(k=0.100\).

**Step 1: convert units before calculating the central value.**

\[
L=3.20\times10^{-2}\,\mathrm{m}=0.0320\,\mathrm{m}
\]

\[
t=4.00\times10^{-3}\,\mathrm{s}=0.00400\,\mathrm{s}.
\]

**Step 2: calculate the central value.**

\[
R=\frac{0.100(0.0320\,\mathrm{m})^3}{(0.00400\,\mathrm{s})^2}
=0.205\,\mathrm{W}.
\]

**Step 3: find the percentage uncertainty of each measured input.**

\[
\frac{0.04}{3.20}\times100\%=1.25\%
\]

\[
\frac{0.08}{4.00}\times100\%=2.0\%.
\]

**Step 4: apply the powers.**

\[
\text{contribution from }L^3=3\times1.25\%=3.75\%
\]

\[
\text{contribution from }t^2=2\times2.0\%=4.0\%.
\]

**Step 5: add contributions and return to an absolute uncertainty.**

\[
\text{percentage uncertainty in }R=3.75\%+4.0\%=7.75\%.
\]

\[
\Delta R=\frac{7.75}{100}\times0.205\,\mathrm{W}=0.0159\,\mathrm{W}.
\]

Round the uncertainty to \(0.02\,\mathrm{W}\), then write the central value to the same hundredth:

\[
\boxed{R=(0.21\pm0.02)\,\mathrm{W}}
\]

**Check:** \(0.02\,\mathrm{W}\) has the same unit as \(R\). Also, \(0.02\div0.21\) is close to \(0.08\), which is close to the unrounded fractional uncertainty \(0.0775\). The rounding is sensible.

## A common wrong turn

You may be tempted to add every number written after a \(\pm\) sign. That does not work.

For a product such as \(A=lw\), \(0.1\,\mathrm{cm}\) and \(0.04\,\mathrm{cm}\) are absolute uncertainties in different-sized measurements. Add their **percentages**, not the raw numbers.

For a sum such as \(L=L_1+L_2\), keep the uncertainties as absolute values in the same unit, then add them. Do not turn them into percentages unless you need the percentage uncertainty of the completed result afterward.

Also separate measured values from exact numbers. A stated exact constant, the number \(2\), or an exact unit conversion does not add measurement uncertainty.

## Core recap

- **Absolute uncertainty** has the same unit as the quantity.
- **Fractional uncertainty** is \(\Delta x/x\). **Percentage uncertainty** is \((\Delta x/x)\times100\%\).
- For a **sum or difference**, add absolute uncertainties.
- For a **product or quotient**, add fractional or percentage uncertainties.
- Multiply a percentage contribution by the magnitude of its **power**.
- Convert the final percentage uncertainty to an absolute uncertainty before writing a final result in \(\pm\) form.
- Round the uncertainty sensibly, then quote the central value to the same decimal place.

The next lesson uses your ability to report uncertainty in a derived quantity. It then moves to a different idea: whether a quantity needs direction as well as size.
