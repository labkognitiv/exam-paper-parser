# SI base quantities and prefixes and Derived units in base-unit form

## Start with a timing puzzle

One timer reads **0.004 s**. Another reads **4 ms**. The second number looks larger, but does that mean the recorded time is longer?

It does not. The number and the unit must be read together. A measurement is a **physical quantity** written with a numerical magnitude and a unit. In this lesson, you will build the shared unit language that lets scientists compare measurements reliably and express complex quantities in terms of fundamental building blocks.

Before continuing, what does the unit `s` tell you? It tells you that the quantity is a time, not a length or a mass.

## Five SI base quantity-unit pairs

Scientists use the **SI system** (Système International d'Unités) so that the same measurement has the same meaning in every laboratory. A **base quantity** is one of the agreed starting quantities that cannot be defined in terms of other physical quantities. Its **SI base unit** is the agreed unit used to measure it.

For this course, learn these five pairs exactly.

| SI base quantity | SI base-unit name | SI base-unit symbol |
| --- | --- | --- |
| **mass** | **kilogram** | **kg** |
| **length** | **metre** | **m** |
| **time** | **second** | **s** |
| **electric current** | **ampere** | **A** |
| **temperature** | **kelvin** | **K** |

Keep the three columns separate in your thinking. **Electric current** is a quantity. **Ampere** is the name of its unit. **A** is the symbol for that unit.

The symbols are part of the answer. **A** and **K** are capital letters. **kg**, **m**, and **s** use lower-case letters.

Why is `m` not the SI base quantity for length? `m` is only the symbol for the unit metre. The quantity is **length**.

Consider this question.

Which row is correct?

- **A.** **electric current, ampere, A**
- **B.** temperature, degree Celsius, °C

**Feedback for A:** Correct. Electric current is an SI base quantity and its SI base unit is the ampere, with symbol `A`.

**Feedback for B:** Degree Celsius is useful in everyday life, but it is not the SI base unit required here. The SI base unit for temperature is kelvin, `K`.

## A prefix changes the size of a unit

Some measurements are much smaller or much larger than one base unit. Writing every zero is slow and easy to misread. An **SI prefix** is a short label that represents a fixed power-of-ten multiplier.

For example, **milli** means one thousandth. Therefore:

\[
1\,\mathrm{ms}=1\times10^{-3}\,\mathrm{s}
\]

The physical quantity remains time. Only the unit scale has changed.

### Prefixes smaller than the unprefixed unit

| Prefix | Symbol | Multiplier |
| --- | --- | --- |
| **pico** | **p** | \(10^{-12}\) |
| **nano** | **n** | \(10^{-9}\) |
| **micro** | **μ** | \(10^{-6}\) |
| **milli** | **m** | \(10^{-3}\) |
| **centi** | **c** | \(10^{-2}\) |
| **deci** | **d** | \(10^{-1}\) |

### Prefixes larger than the unprefixed unit

| Prefix | Symbol | Multiplier |
| --- | --- | --- |
| **kilo** | **k** | \(10^{3}\) |
| **mega** | **M** | \(10^{6}\) |
| **giga** | **G** | \(10^{9}\) |
| **tera** | **T** | \(10^{12}\) |

An unprefixed unit has multiplier \(10^0=1\). So `m` for metre means one metre, while `mm` means millimetre, or \(10^{-3}\) metre.

Notice the potential confusion: the symbol `m` can mean the metre unit when it stands alone, or the **milli** prefix when it appears before another unit symbol, such as `ms`. Context and position matter.

## Read symbols exactly

Upper-case and lower-case letters do not mean the same thing in SI notation.

| Symbol | Prefix | Multiplier |
| --- | --- | --- |
| **m** | milli | \(10^{-3}\) |
| **μ** | micro | \(10^{-6}\) |
| **M** | mega | \(10^{6}\) |

So `3 mA` means three milliamperes, while `3 MA` means three megaamperes. The multipliers differ by \(10^9\). Treating capital letters as optional would produce a very large error.

What should you check before any prefix conversion? Read the prefix symbol and its letter case before changing the number.

### Worked example 1: convert to an unprefixed unit

A sensor records a pulse duration of **6.5 μs**. Write the duration in seconds.

#### Step 1: identify the quantity and the target unit

The quantity is time. The target unit is seconds, symbol `s`.

#### Step 2: replace the prefix with its multiplier

**Micro**, `μ`, means \(10^{-6}\). Therefore:

\[
6.5\,\mathrm{\mu s}=6.5\times10^{-6}\,\mathrm{s}
\]

#### Step 3: check the scale

A microsecond is one millionth of a second. The result must be much less than one second. \(6.5\times10^{-6}\,\mathrm{s}\) has that size and still has the unit `s`.

**Answer: \(6.5\,\mathrm{\mu s}=6.5\times10^{-6}\,\mathrm{s}\).**

The decision comes before the arithmetic: identify `μ` first, then use its multiplier. Do not move a decimal point by guesswork.

### Worked example 2: choose a useful prefix

A small length is \(0.0000042\,\mathrm{m}\). Write it using a suitable prefix.

#### Step 1: write the number in scientific notation

\[
0.0000042\,\mathrm{m}=4.2\times10^{-6}\,\mathrm{m}
\]

#### Step 2: match the power of ten to a prefix

The multiplier \(10^{-6}\) is **micro**, symbol `μ`.

\[
4.2\times10^{-6}\mathrm{m}=4.2\,\mathrm{\mu m}
\]

#### Step 3: convert back as a check

\[
4.2\,\mathrm{\mu m}=4.2\times10^{-6}\,\mathrm{m}=0.0000042\,\mathrm{m}
\]

The starting value returns, so the conversion is consistent.

**Answer: \(4.2\,\mathrm{\mu m}\).**

### Compare measurements on one scale

Return to the two timers from the opening.

\[
4\,\mathrm{ms}=4\times10^{-3}\,\mathrm{s}=0.004\,\mathrm{s}
\]

Both timers recorded the same duration. A larger displayed number does not automatically mean a larger quantity. Convert to a shared unit scale before comparing.

Which statement is correct?

- **A.** **4 ms and 0.004 s are equal times.**
- **B.** 4 ms is longer because 4 is greater than 0.004.

**Feedback for A:** Correct. Milli means \(10^{-3}\), so `4 ms` becomes \(4\times10^{-3}\,\mathrm{s}\), which is `0.004 s`.

**Feedback for B:** The numerical magnitudes cannot be compared alone because the units are different. The `m` in `ms` changes the size of the second.

### The mass-unit detail

The SI base unit for mass is the **kilogram**, `kg`. It already includes the prefix kilo (`k`), but `kg` is the official base unit.

Do not attach another prefix directly to `kg`. For smaller masses, use gram-based notation and relate it to kilograms:

\[
1\,\mathrm{g}=10^{-3}\,\mathrm{kg}
\]

\[
1\,\mathrm{mg}=10^{-6}\,\mathrm{kg}
\]

Here `mg` means milligram. It is not "milli-kilogram". This notation convention prevents stacked prefixes.

## Build a derived unit from a relationship

### Derived unit {#plain-meaning-derived-unit}

> **Plain meaning:** A **derived unit** is made by multiplying or dividing SI base units.

Most physical quantities are not base quantities. Their units are built from combinations of the five SI base units.

Start with familiar geometric and kinematic examples.

An area multiplies two lengths:

\[
\mathrm{m}\times\mathrm{m}=\mathrm{m^2}
\]

A volume multiplies three lengths:

\[
\mathrm{m}\times\mathrm{m}\times\mathrm{m}=\mathrm{m^3}
\]

A speed divides distance by time:

\[
\frac{\mathrm{m}}{\mathrm{s}}=\mathrm{m\,s^{-1}}
\]

Density divides mass by volume:

\[
\frac{\mathrm{kg}}{\mathrm{m^3}}=\mathrm{kg\,m^{-3}}
\]

The notation \(\mathrm{s^{-1}}\) means "per second" or "divided by seconds". A negative index does not mean a negative number. It tells you that the unit is in the denominator.

Ask yourself: why does volume have unit \(\mathrm{m^3}\) while area has unit \(\mathrm{m^2}\)? Volume involves three length dimensions, whereas area involves two.

## Read named units as short forms

Physics often gives a derived unit a special name to honour a scientist and make everyday communication quicker. In Cambridge Physics examinations, you are frequently asked to express these named units in terms of SI base units.

To unpack a named unit into base units, use a defining physical relationship:

1. **Force:** unit is the **newton** (\(\mathrm{N}\)). From \(F=ma\):
\[
1\,\mathrm{N}=1\,\mathrm{kg}\times1\,\mathrm{m\,s^{-2}}=1\,\mathrm{kg\,m\,s^{-2}}
\]

2. **Energy and work:** unit is the **joule** (\(\mathrm{J}\)). From \(W=Fd\):
\[
1\,\mathrm{J}=1\,\mathrm{N}\times1\,\mathrm{m}=(1\,\mathrm{kg\,m\,s^{-2}})(1\,\mathrm{m})=1\,\mathrm{kg\,m^2\,s^{-2}}
\]

3. **Power:** unit is the **watt** (\(\mathrm{W}\)). From \(P=\frac{W}{t}\):
\[
1\,\mathrm{W}=\frac{1\,\mathrm{J}}{1\,\mathrm{s}}=\frac{1\,\mathrm{kg\,m^2\,s^{-2}}}{1\,\mathrm{s}}=1\,\mathrm{kg\,m^2\,s^{-3}}
\]

4. **Electric charge:** unit is the **coulomb** (\(\mathrm{C}\)). From \(Q=It\):
\[
1\,\mathrm{C}=1\,\mathrm{A}\times1\,\mathrm{s}=1\,\mathrm{A\,s}
\]

5. **Pressure:** unit is the **pascal** (\(\mathrm{Pa}\)). From \(p=\frac{F}{A}\):
\[
1\,\mathrm{Pa}=\frac{1\,\mathrm{N}}{1\,\mathrm{m^2}}=\frac{1\,\mathrm{kg\,m\,s^{-2}}}{1\,\mathrm{m^2}}=1\,\mathrm{kg\,m^{-1}\,s^{-2}}
\]

The named unit is convenient shorthand, but its base-unit form reveals how the quantity is physically composed.

### Worked example 3: express a joule in SI base units

Express the **joule** (\(\mathrm{J}\)) in SI base units.

#### Step 1: state a defining relationship

Work is defined as force multiplied by distance in the direction of the force:

\[
W=Fd
\]

Therefore, the unit identity is:

\[
1\,\mathrm{J}=1\,\mathrm{N\,m}
\]

#### Step 2: replace the named unit with base units

Newton is not an SI base unit. From \(F=ma\), \(1\,\mathrm{N}=1\,\mathrm{kg\,m\,s^{-2}}\). Substitute this into the unit equation:

\[
1\,\mathrm{J}=(1\,\mathrm{kg\,m\,s^{-2}})(1\,\mathrm{m})
\]

#### Step 3: collect powers of each base unit

Multiply the metre factors:

\[
\mathrm{m^1}\times\mathrm{m^1}=\mathrm{m^{1+1}}=\mathrm{m^2}
\]

Therefore:

\[
1\,\mathrm{J}=1\,\mathrm{kg\,m^2\,s^{-2}}
\]

**Answer: \(\mathrm{J}=\mathrm{kg\,m^2\,s^{-2}}\).**

Always expand any named unit that is not an SI base unit before collecting powers.

Which step is needed first when simplifying \(\mathrm{J}=\mathrm{N\,m}\) into SI base units?

- **A.** Replace \(\mathrm{N}\) with \(\mathrm{kg\,m\,s^{-2}}\).
- **B.** Replace \(\mathrm{m}\) with \(\mathrm{N}\).

**Feedback for A:** Correct. The newton is a named derived unit. Expanding it into base units allows you to collect the metre powers.

**Feedback for B:** Metre is already an SI base unit. It must remain \(\mathrm{m}\).

## Find the base units of an unknown constant

Examinations frequently supply an unfamiliar equation and ask for the SI base units of a constant or quantity within it. You do not need to study the full physics of the topic yet. Treat the equation as an algebraic route for units.

### Worked example 4: find the unit of an unfamiliar constant

A resistive force \(F\) acting on an object moving through a fluid with speed \(v\) is modelled by:

\[
F=kAv
\]

where \(A\) is the cross-sectional area and \(k\) is a constant.

Find the SI base units of \(k\).

#### Step 1: rearrange the equation to isolate the constant

\[
k=\frac{F}{Av}
\]

#### Step 2: write the SI base units for each quantity

- \([F]=\mathrm{kg\,m\,s^{-2}}\) (force)
- \([A]=\mathrm{m^2}\) (area)
- \([v]=\mathrm{m\,s^{-1}}\) (speed)

Here the square brackets \([k]\) denote "the SI base units of \(k\)".

#### Step 3: substitute base units into the expression

\[
[k]=\frac{\mathrm{kg\,m\,s^{-2}}}{(\mathrm{m^2})(\mathrm{m\,s^{-1}})}
\]

#### Step 4: simplify denominator and divide powers

Combine the metre terms in the denominator:

\[
\mathrm{m^2}\times\mathrm{m^1}=\mathrm{m^3}
\]

So the denominator is \(\mathrm{m^3\,s^{-1}}\). Now divide numerator by denominator:

\[
[k]=\frac{\mathrm{kg\,m\,s^{-2}}}{\mathrm{m^3\,s^{-1}}}=\mathrm{kg}\times\mathrm{m^{1-3}}\times\mathrm{s^{-2-(-1)}}
\]

Calculate each index carefully:

- For length: \(1 - 3 = -2\), giving \(\mathrm{m^{-2}}\).
- For time: \(-2 - (-1) = -2 + 1 = -1\), giving \(\mathrm{s^{-1}}\).

Therefore:

\[
[k]=\mathrm{kg\,m^{-2}\,s^{-1}}
\]

**Answer: \(\mathrm{kg\,m^{-2}\,s^{-1}}\).**

#### Step 5: check with fractions

\[
\frac{\frac{\mathrm{kg\,m}}{\mathrm{s^2}}}{\mathrm{m^2}\times\frac{\mathrm{m}}{\mathrm{s}}}
=\frac{\mathrm{kg\,m}}{\mathrm{s^2}}\times\frac{\mathrm{s}}{\mathrm{m^3}}
=\frac{\mathrm{kg}}{\mathrm{m^2\,s}}
=\mathrm{kg\,m^{-2}\,s^{-1}}
\]

Both routes match, confirming the result.

What is the correct index subtraction when dividing \(\mathrm{s^{-2}}\) by \(\mathrm{s^{-1}}\)?

- **A.** \(-2 - (-1) = -1\), so \(\mathrm{s^{-1}}\)
- **B.** \(-2 - 1 = -3\), so \(\mathrm{s^{-3}}\)

**Feedback for A:** Correct. Dividing by \(\mathrm{s^{-1}}\) subtracts \(-1\) from the power: \(-2 - (-1) = -2 + 1 = -1\).

**Feedback for B:** Not correct. The denominator power is \(-1\), not \(+1\). Subtracting a negative power adds the index: \(-2 - (-1) = -1\).

## Common misconceptions and errors

1. **Confusing quantities with units:**
   Current is a quantity; ampere is its unit. Length is a quantity; metre is its unit. Do not write "the base quantity is second".
2. **Treating case sensitivity as optional:**
   The symbol `m` means milli (\(10^{-3}\)) or metre, whereas `M` means mega (\(10^{6}\)). Writing `3 MA` when `3 mA` is intended changes the value by a factor of one billion (\(10^9\)).
3. **Double prefixing:**
   Do not attach a prefix to kilogram, such as "micro-kilogram". Mass submultiples use grams: \(1\,\mathrm{mg}=10^{-6}\,\mathrm{kg}\).
4. **Treating named units as base units:**
   The newton, joule, watt, and pascal are convenient names for derived units. Never list them as SI base units.
5. **Index mistakes in denominators:**
   When bringing a unit from denominator to numerator, reverse the sign of its power: \(\frac{1}{\mathrm{m^3}}=\mathrm{m^{-3}}\). When dividing powers of the same base unit, subtract the denominator power from the numerator power.

## Core recap

- The five required SI base quantity-unit pairs are:
  - **mass:** kilogram (\(\mathrm{kg}\))
  - **length:** metre (\(\mathrm{m}\))
  - **time:** second (\(\mathrm{s}\))
  - **electric current:** ampere (\(\mathrm{A}\))
  - **temperature:** kelvin (\(\mathrm{K}\))
- A **prefix** represents a fixed power-of-ten multiplier from pico (\(10^{-12}\)) to tera (\(10^{12}\)). Read symbols with exact letter case.
- A **derived unit** is formed as a product or quotient of SI base units.
- Important named derived units in base-unit form:
  - Force: \(1\,\mathrm{N}=1\,\mathrm{kg\,m\,s^{-2}}\)
  - Energy / Work: \(1\,\mathrm{J}=1\,\mathrm{kg\,m^2\,s^{-2}}\)
  - Power: \(1\,\mathrm{W}=1\,\mathrm{kg\,m^2\,s^{-3}}\)
  - Electric charge: \(1\,\mathrm{C}=1\,\mathrm{A\,s}\)
  - Pressure: \(1\,\mathrm{Pa}=1\,\mathrm{kg\,m^{-1}\,s^{-2}}\)
- To find the base units of an unfamiliar constant, isolate the constant algebraically, substitute base units for each quantity, and simplify powers.
- In the next lesson, you will use these base-unit representations to test whether physical equations are homogeneous.
