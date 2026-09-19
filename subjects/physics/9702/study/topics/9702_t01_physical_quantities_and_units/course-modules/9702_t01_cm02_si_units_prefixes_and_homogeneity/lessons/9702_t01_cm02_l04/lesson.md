# Derived units in base-unit form

## Start with two labels

One energy meter is labelled **J**. Another is labelled **kg m² s⁻²**. Do the meters have to measure different things because their labels look different?

No. A named unit can be a shorter name for a product or quotient of **SI base units**. This lesson unpacks those shorter names. You already know the five base units used in this course:

\[
\mathrm{kg,\ m,\ s,\ A,\ K}
\]

They measure mass, length, time, electric current and temperature. We will now combine them to express units for other quantities.

## Build a derived unit from a relationship

### Derived unit {#plain-meaning-derived-unit}

> **Plain meaning:** A **derived unit** is made by multiplying or dividing SI base units.

Start with familiar examples. An area uses a length in two directions:

\[
\mathrm{m}\times\mathrm{m}=\mathrm{m^2}
\]

A volume uses a length in three directions:

\[
\mathrm{m}\times\mathrm{m}\times\mathrm{m}=\mathrm{m^3}
\]

A speed compares distance with time:

\[
\frac{\mathrm{m}}{\mathrm{s}}=\mathrm{m\,s^{-1}}
\]

The notation \(\mathrm{s^{-1}}\) means "per second" or "divided by seconds". A negative power does not mean a negative time. It tells you that the unit is in the denominator.

Ask yourself: why does a volume use \(\mathrm{m^3}\) rather than \(\mathrm{m^2}\)? A volume needs three length dimensions, whereas an area needs only two.

## Read named units as short forms

Physics often gives a derived unit a name. You need to be able to replace that name with base units when asked.

Use these unit identities in this lesson:

\[
1\,\mathrm{N}=1\,\mathrm{kg\,m\,s^{-2}}
\]

\[
1\,\mathrm{J}=1\,\mathrm{N\,m}
\]

\[
1\,\mathrm{W}=1\,\mathrm{J\,s^{-1}}
\]

The **newton**, \(\mathrm{N}\), is the unit of force. The **joule**, \(\mathrm{J}\), is the unit of energy. The **watt**, \(\mathrm{W}\), is the unit of power. The named unit is useful shorthand, but its base-unit form reveals how it is built.

### Worked example 1: express a joule in base units

Express \(\mathrm{J}\) in SI base units.

Start with the unit identity:

\[
1\,\mathrm{J}=1\,\mathrm{N\,m}
\]

Replace \(\mathrm{N}\) with its base-unit form:

\[
1\,\mathrm{J}=(1\,\mathrm{kg\,m\,s^{-2}})(1\,\mathrm{m})
\]

Now collect the metre factors:

\[
1\,\mathrm{J}=1\,\mathrm{kg\,m^2\,s^{-2}}
\]

**Answer: \(\mathrm{J}=\mathrm{kg\,m^2\,s^{-2}}\).**

The two \(\mathrm{m}\) factors multiply, so their powers add:

\[
\mathrm{m^1}\times\mathrm{m^1}=\mathrm{m^{1+1}}=\mathrm{m^2}
\]

Notice the decision before the simplification: first expand every named unit that is not a base unit. Then collect powers.

Which step is needed before you simplify \(\mathrm{J}=\mathrm{N\,m}\)?

- **A.** Replace \(\mathrm{N}\) with \(\mathrm{kg\,m\,s^{-2}}\).
- **B.** Replace \(\mathrm{m}\) with \(\mathrm{N}\).

**Feedback for A:** Correct. \(\mathrm{N}\) is a named derived unit, so expand it into base units before collecting the metre factors.

**Feedback for B:** Not this time. Metre is already an SI base unit. It should remain \(\mathrm{m}\).

## Division creates negative powers

When a unit is in the denominator, you can either keep a fraction or write a negative power. Both forms mean the same thing:

\[
\frac{1}{\mathrm{m^3}}=\mathrm{m^{-3}}
\]

For example, a quantity reported in kilograms per cubic metre has the unit:

\[
\frac{\mathrm{kg}}{\mathrm{m^3}}=\mathrm{kg\,m^{-3}}
\]

The \(-3\) records that cubic metres are in the denominator. The correct unit is not \(\mathrm{kg\,m^3}\), because that would mean kilograms multiplied by cubic metres.

### Worked example 2: express a watt in base units

Express \(\mathrm{W}\) in SI base units.

Start with the watt identity:

\[
1\,\mathrm{W}=1\,\mathrm{J\,s^{-1}}
\]

Replace \(\mathrm{J}\) using the result from the previous worked example:

\[
1\,\mathrm{W}=(1\,\mathrm{kg\,m^2\,s^{-2}})\mathrm{s^{-1}}
\]

Collect the time powers:

\[
\mathrm{s^{-2}}\times\mathrm{s^{-1}}=\mathrm{s^{-3}}
\]

Therefore:

\[
1\,\mathrm{W}=1\,\mathrm{kg\,m^2\,s^{-3}}
\]

**Answer: \(\mathrm{W}=\mathrm{kg\,m^2\,s^{-3}}\).**

Check with a fraction:

\[
\frac{\mathrm{kg\,m^2\,s^{-2}}}{\mathrm{s}}=\mathrm{kg\,m^2\,s^{-3}}
\]

Both routes give the same result. The fraction makes it clear why dividing by another second makes the time power more negative.

## Find the unit of an unfamiliar quantity

Sometimes a question supplies a relationship containing a quantity or constant whose unit you have not met. You do not need to know the later physics behind it. Use the relationship only as a **unit route**.

Suppose a supplied model is:

\[
F=kAv
\]

Here \(F\) has unit \(\mathrm{kg\,m\,s^{-2}}\), \(A\) has unit \(\mathrm{m^2}\), \(v\) has unit \(\mathrm{m\,s^{-1}}\), and \(k\) is an unfamiliar constant.

We want the base-unit form of \(k\). First rearrange:

\[
k=\frac{F}{Av}
\]

Then replace each quantity with its unit:

\[
[k]=\frac{\mathrm{kg\,m\,s^{-2}}}{(\mathrm{m^2})(\mathrm{m\,s^{-1}})}
\]

Simplify the denominator one factor at a time:

\[
\mathrm{m^2}\times\mathrm{m\,s^{-1}}=\mathrm{m^3\,s^{-1}}
\]

Now divide:

\[
[k]=\frac{\mathrm{kg\,m\,s^{-2}}}{\mathrm{m^3\,s^{-1}}}
\]

\[
[k]=\mathrm{kg\,m^{1-3}\,s^{-2-(-1)}}
\]

\[
[k]=\mathrm{kg\,m^{-2}\,s^{-1}}
\]

**Answer: \(k\) has unit \(\mathrm{kg\,m^{-2}\,s^{-1}}\).**

The brackets in \([k]\) mean "the unit of \(k\)". They do not mean multiplication.

What is the safest choice when you divide by \(\mathrm{m^3\,s^{-1}}\)?

- **A.** Subtract the denominator powers: \(m^{1-3}\) and \(s^{-2-(-1)}\).
- **B.** Copy both denominator powers unchanged into the answer.

**Feedback for A:** Correct. Division subtracts the powers of the denominator. The second subtraction includes a negative power, so \(-2-(-1)=-1\).

**Feedback for B:** This would treat division as multiplication. Keeping denominator powers unchanged gives the wrong unit.

## Use the charge bridge carefully

Electric charge has a named unit, the coulomb, \(\mathrm{C}\). Its base-unit form is:

\[
1\,\mathrm{C}=1\,\mathrm{A\,s}
\]

This says that charge combines electric current and time. If a question asks for a base-unit form involving charge, replace \(\mathrm{C}\) with \(\mathrm{A\,s}\) before simplifying.

For example, suppose a supplied quantity \(x\) has unit \(\mathrm{C\,N^{-1}}\). Expand one named unit at a time:

\[
\mathrm{C\,N^{-1}}=(\mathrm{A\,s})(\mathrm{kg\,m\,s^{-2}})^{-1}
\]

Taking the reciprocal reverses every power:

\[
(\mathrm{kg\,m\,s^{-2}})^{-1}=\mathrm{kg^{-1}\,m^{-1}\,s^2}
\]

Now multiply:

\[
\mathrm{C\,N^{-1}}=(\mathrm{A\,s})(\mathrm{kg^{-1}\,m^{-1}\,s^2})
\]

\[
\mathrm{C\,N^{-1}}=\mathrm{A\,kg^{-1}\,m^{-1}\,s^3}
\]

This is unit algebra. It does not require you to learn what \(x\) represents.

## A reliable unit routine

For every base-unit question:

1. Identify the requested quantity or named unit.
2. Write a supplied relationship if a quantity must be isolated.
3. Replace each named derived unit with its base-unit form.
4. Keep fractions visible until every factor is present.
5. Multiply factors and collect powers of the same base unit.
6. Use a fraction or reciprocal route as a check.

Do not yet use these units to decide whether an entire equation is valid. Comparing units on two sides of an equation is **homogeneity**, which is the next lesson.

## Core recap

- A **derived unit** is a product or quotient of SI base units.
- \(\mathrm{N}=\mathrm{kg\,m\,s^{-2}}\).
- \(\mathrm{J}=\mathrm{kg\,m^2\,s^{-2}}\).
- \(\mathrm{W}=\mathrm{kg\,m^2\,s^{-3}}\).
- A denominator can be written with negative powers, such as \(\mathrm{kg\,m^{-3}}\).
- Expand named units, collect powers carefully, and use a fraction or reciprocal check.

You are ready to use SI base units to check whether the units on both sides of a supplied equation agree.
