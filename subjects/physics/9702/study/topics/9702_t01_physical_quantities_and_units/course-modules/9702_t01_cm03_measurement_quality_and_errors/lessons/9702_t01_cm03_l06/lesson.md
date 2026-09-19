# Systematic, zero and random errors

## How can careful readings still be wrong?

Two groups measure the same reference mass, whose known value is **50.00 g**.

Group A records `50.31 g`, `50.30 g`, `50.32 g`, and `50.31 g`. Group B records `50.02 g`, `49.97 g`, `50.04 g`, and `49.99 g`.

Group A's readings are close together, but they are all above the reference value. Group B's readings move above and below it. These patterns need different responses.

Ask two questions whenever you examine repeated measurements:

1. Are the readings all shifted in one direction?
2. Or do they vary unpredictably from reading to reading?

The first pattern suggests a **systematic error**. The second suggests a **random error**.

## <a id="systematic-error"></a>A shared shift is a systematic error

> **Definition to learn: systematic error.** an error that causes measurements to be consistently offset from the true value in the same direction

**Offset** means shifted away from the true value. **Consistently** means the shift happens in the same direction for every measurement. The direction might be too high or too low.

Imagine a balance that adds `0.30 g` to every mass it displays. A true mass of `20.00 g` appears as `20.30 g`. A true mass of `45.00 g` appears as `45.30 g`. The size of the object changes, but the instrument's bias remains in the same direction.

Why would averaging several readings from this balance fail to remove the problem? Every reading includes the same positive offset, so their mean includes it too.

Common causes of a systematic error include an incorrectly calibrated instrument, a damaged scale, a consistent viewing mistake, or a method that leaves out an effect every time.

To deal with a systematic error, find and correct the cause. You might check against a known reference, recalibrate the instrument, or change the method.

Consider these choices.

- A. **Check the balance against a known mass and correct its calibration.**
- B. Take many readings from the same uncorrected balance and use only their mean.

**Feedback for A:** Correct. A known mass can reveal the consistent offset, and calibration can remove or allow correction for its cause.

**Feedback for B:** A mean may look stable, but it retains the shared offset. Repetition alone does not remove a systematic error.

## A zero error is a particular systematic error

A **zero error** is found by checking an instrument when the true input should be zero. For an empty balance, the true mass is `0 g`. For a closed micrometer, the true gap is `0 mm`.

If an empty balance reads `+0.08 g`, it has a positive zero error. That `+0.08 g` is added to every later uncorrected reading, so the error is systematic.

Record the sign. It tells you which direction the correction must go.

## Worked example 1: correct a positive zero error

An empty balance reads **+0.08 g**. With a sample on it, the balance displays **12.64 g**. Find the corrected mass.

### Step 1: identify the error pattern

At true zero, the balance gives a positive reading. The balance is adding `0.08 g` to readings, so this is a **positive zero error**.

### Step 2: remove the extra amount

The indicated reading is too high. Subtract the signed zero reading:

\[
12.64\,\mathrm{g}-(+0.08\,\mathrm{g})=12.56\,\mathrm{g}
\]

### Step 3: check the direction and unit

The corrected value should be lower because the balance initially read too high. `12.56 g` is lower than `12.64 g`, and the unit remains grams.

**Answer: \(12.56\,\mathrm{g}\).**

If an empty instrument showed a negative zero reading, subtracting that negative value would increase the corrected result. Do not decide the operation from memory. Read and keep the sign.

## <a id="random-error"></a>Scatter is random error

> **Definition to learn: random error.** an unpredictable variation in repeated measurements that causes readings to scatter about the true value

**Unpredictable variation** means that one reading can be high and the next low, without a fixed direction. **Scatter** means the readings spread around a central value.

Suppose a student uses a stopwatch five times for the same event and records `2.41 s`, `2.35 s`, `2.39 s`, `2.43 s`, and `2.37 s`. Starting and stopping at slightly different moments can move each reading in a different direction.

Random error does not mean the student was careless. Small uncontrollable changes, limited human reaction time, and slight variation in an instrument's response can all produce scatter.

## Worked example 2: use repeats to reduce random variation

Five times are recorded for an unchanging event:

\[
2.41\,\mathrm{s},\quad2.35\,\mathrm{s},\quad2.39\,\mathrm{s},\quad2.43\,\mathrm{s},\quad2.37\,\mathrm{s}
\]

Find the mean time.

### Step 1: add the five readings with their unit

\[
2.41+2.35+2.39+2.43+2.37=11.95
\]

The total is `11.95 s` because all five terms are times in seconds.

### Step 2: divide by the number of readings

\[
\frac{11.95\,\mathrm{s}}{5}=2.39\,\mathrm{s}
\]

### Step 3: explain why this helps

Some readings are above `2.39 s` and some are below it. Their random deviations partly cancel in the mean. A mean based on several independent readings is less affected by one unusually high or low reading than a single measurement.

**Answer: \(2.39\,\mathrm{s}\).**

The mean reduces the effect of random variation. It does not prove that no systematic error is present.

Which response matches a set of readings that scatter on both sides of a central value, with no fixed direction?

- A. **Take repeated readings and calculate a mean.**
- B. Apply the same fixed correction to every reading without first finding a shared cause.

**Feedback for A:** Correct. Random variation changes direction, so several readings and a mean allow some positive and negative variations to cancel.

**Feedback for B:** A fixed correction is appropriate only after identifying a consistent offset, such as a zero error. It does not address unpredictable scatter.

## Do not use the same remedy for both patterns

| Error pattern | What you notice | Suitable response |
| --- | --- | --- |
| **systematic error** | Readings are consistently shifted in the same direction. | Check zero, calibrate against a reference, or improve the method. |
| **zero error** | An instrument gives a non-zero reading when the true input is zero. | Record the signed zero reading and correct later readings. |
| **random error** | Repeated readings vary unpredictably and scatter. | Take several independent readings and calculate a mean. |

A tempting mistake is to think that a tightly grouped set of readings must be free from error. Group A at the start of this lesson showed why that is unsafe. Readings can be close together and still all be shifted by the same systematic error.

Another tempting mistake is to correct random scatter with one fixed number. Random error has no single fixed direction to remove. The useful response is repeated measurement and averaging.

## A measurement plan for a thin wire

Suppose you need the diameter of a thin wire.

First choose a **micrometer screw gauge**. It is suitable for a small diameter. A metre rule is not suitable because its scale is too coarse for this dimension.

Before measuring the wire, close the micrometer gently with nothing between its faces. If it reads `+0.03 mm`, record that positive zero error.

Now measure at several positions along the wire. Turn the wire between readings so that you sample more than one direction across its cross-section. Correct each reading for the same zero error, then calculate the mean of the corrected readings.

Why use both a zero correction and repeated measurements? The zero correction addresses the systematic offset. Multiple positions, orientations, and readings reduce the effect of random variation and help the measurement represent the whole wire.

## Keep this lesson separate from the next one

This lesson diagnoses patterns and chooses a response. It does not yet introduce the separate meanings of **precision**, **accuracy**, or **resolution**. Those ideas are the next lesson.

## Core recap

- **Systematic error:** `an error that causes measurements to be consistently offset from the true value in the same direction`.
- **Zero error:** a systematic error shown by a non-zero instrument reading when the true input is zero. Keep its sign when correcting readings.
- **Random error:** `an unpredictable variation in repeated measurements that causes readings to scatter about the true value`.
- Correct a shared cause for a systematic error. Take repeated readings and calculate a mean to reduce the effect of random error.
