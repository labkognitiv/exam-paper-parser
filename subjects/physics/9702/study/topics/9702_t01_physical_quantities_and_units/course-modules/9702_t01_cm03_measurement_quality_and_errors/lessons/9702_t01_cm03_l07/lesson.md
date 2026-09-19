# Precision, accuracy and resolution

Imagine three students measuring the thickness of the same metal sheet. Their
readings may sit tightly together. They may also be close to the sheet's true
thickness. Those are different claims.

One claim is about agreement between repeated readings. The other is about
agreement with the true value. A third idea, **resolution**, is about what the
instrument can tell apart. This lesson separates those ideas so that a question
such as "precise but not accurate" has a clear meaning.

## Three questions to ask about a measurement

When you see repeated readings, pause and ask three different questions.

1. Are the readings close to **each other**?
2. Is a measured value, or a sensible representative value, close to the
   **true value**?
3. What is the smallest change the **instrument** can distinguish?

The answers describe precision, accuracy and resolution in that order.

The previous lesson introduced **systematic errors**, including zero errors,
and **random errors**. Keep that distinction in mind. A systematic error can
move a whole close group away from the true value. Random variation can spread
readings apart.

Teacher question: if five readings are all nearly identical, what have you
learned first: whether they agree with each other, or whether they equal the
true value? The first conclusion is the safe one. Agreement alone does not
reveal the true value.

## Precision means agreement between repeats

<a id="definition-precision"></a>

> **Definition to learn: precision.** the degree of agreement among repeated measurements, indicated by their spread or range

**Repeated measurements** are values found by measuring the same quantity again
under the same intended conditions. Their **spread** describes how far apart
they are. Their **range** is the difference between the largest and smallest
reading.

A small spread or small range means the readings agree closely. That is high
precision. A large spread or large range means they do not agree closely. That
is low precision.

Precision is about the readings themselves. Do not use it to mean "correct".
There may be no known true value in an experiment, but you can still judge
whether the repeated readings are precise.

### Worked example 1: Are these readings precise?

A student measures the width of a card four times. The readings are

\[
42.6\ \mathrm{mm},\quad 42.7\ \mathrm{mm},\quad 42.6\ \mathrm{mm},\quad 42.7\ \mathrm{mm}.
\]

**What is known?** The readings are repeated measurements of one width. No
true width has been supplied.

**Decision.** This question asks about agreement between repeats, so compare
the largest and smallest readings. It is not yet an accuracy question.

The largest reading is **42.7 mm**. The smallest is **42.6 mm**.

\[
42.7\ \mathrm{mm}-42.6\ \mathrm{mm}=0.1\ \mathrm{mm}
\]

The readings have a small range of **0.1 mm**. They are **precise** because
they are tightly grouped.

**Check.** We cannot call the readings accurate because the true width has not
been given. A small range answers the precision question only.

A tempting mistake is to write "precise, so accurate". That joins two separate
tests. Precision compares readings with each other. Accuracy compares a value
with the true value.

Suppose another set is **42.1 mm, 43.0 mm, 42.5 mm and 43.2 mm**. These values
have a much larger spread. They are less precise, even if their average happened
to be near the true width.

You measure a pin's diameter five times and the readings differ only in the
last displayed digit. Which description is supported?

- **A:** The readings are precise.
- **B:** The readings are definitely accurate.

**Feedback for A:** Correct. Very close repeated readings have a small spread,
so they show precision.

**Feedback for B:** Not yet. The readings may be close to each other but all
may be displaced from the true diameter by the same systematic or zero error.

## Accuracy means closeness to the true value

<a id="definition-accuracy"></a>

> **Definition to learn: accuracy.** the closeness of a measured value to the true value of the quantity

The **true value** is the value that would be obtained with an ideal measurement
of the quantity. In real practical work, it may be known from a trusted standard
or reference measurement. It is not automatically the same as the most common
reading in a student's data.

To judge accuracy, compare the measured value with the true value. A small
difference means the measurement is accurate. A large difference means it is
not accurate.

Teacher question: can a collection of readings be very close together and still
miss the true value? Yes. That pattern is the reason accuracy and precision
need different names.

### Worked example 2: Precise but not accurate

A calibrated reference block has a true thickness of **15.00 mm**. A student
uses an instrument and records these repeated readings:

\[
15.36\ \mathrm{mm},\quad 15.35\ \mathrm{mm},\quad 15.36\ \mathrm{mm}.
\]

**Stage 1: decide about precision.** The largest reading is **15.36 mm** and
the smallest is **15.35 mm**. Their range is

\[
15.36\ \mathrm{mm}-15.35\ \mathrm{mm}=0.01\ \mathrm{mm}.
\]

The readings agree very closely, so they are **precise**.

**Stage 2: decide about accuracy.** Each reading is about **0.35 mm** above the
true thickness of **15.00 mm**. The results are not close to the true value, so
they are **not accurate**.

The pattern is **precise but not accurate**. One possible explanation from the
previous lesson is a zero error. If the instrument begins at a non-zero reading,
every measurement can be shifted in the same direction.

**Check.** Repeating the measurement gave a small spread. Repetition did not
remove the shared offset. Averaging close but shifted readings would still give
a shifted answer.

This is different from random variation. Random variation makes readings scatter
unpredictably. It can reduce precision. A fixed zero error can leave precision
high while reducing accuracy.

### The four useful descriptions

Use the comparison below as a reasoning guide, not as a set of labels to guess.

- **Precise and accurate:** readings are close together and close to the true
  value.
- **Precise but not accurate:** readings are close together but displaced from
  the true value. A systematic error is a possible cause.
- **Not precise and not accurate:** readings are spread out and are also far
  from the true value.
- **Accurate but not precise:** a representative result can be close to the
  true value while individual readings have a large spread. More repeated
  measurements would be needed before trusting that agreement.

Do not diagnose the cause from the label alone. "Precise but not accurate" is
evidence consistent with a systematic error, but an investigation is needed to
find the actual cause.

## Resolution belongs to the instrument

<a id="definition-instrument-resolution"></a>

> **Definition to learn: instrument resolution.** the smallest change in a quantity that a measuring instrument can distinguish, usually set by its smallest scale division

Resolution describes the fineness of an instrument's reading. For an analogue
scale, it is usually connected to the smallest marked division. For a digital
display, it is connected to the smallest change shown by the display.

For example, an instrument that distinguishes changes of **0.01 mm** has a
finer resolution than one that distinguishes only **1 mm** changes. The first
instrument can show smaller changes in the measured quantity.

Resolution helps you choose an instrument that suits the size of the change you
need to observe. It does not by itself prove accuracy. An instrument with fine
resolution can still have a zero error. It also does not guarantee precise
repeated readings, because handling, viewing and changing conditions can add
random variation.

### Worked example 3: Choosing an instrument by resolution

A technician needs to check whether the diameter of a wire changes by about
**0.03 mm** after it is heated. Two instruments are available:

- Instrument P distinguishes changes of **1 mm**.
- Instrument Q distinguishes changes of **0.01 mm**.

**Decision.** The important change is **0.03 mm**. The instrument must be able
to distinguish a smaller change than this, otherwise the displayed readings may
not reveal the change.

Instrument P changes only in **1 mm** steps. A change of **0.03 mm** is much
smaller than one step, so P is unsuitable for this purpose.

Instrument Q changes in **0.01 mm** steps. The expected change is three such
steps:

\[
0.03\ \mathrm{mm}=3\times0.01\ \mathrm{mm}
\]

Instrument Q has suitable resolution to distinguish the expected change.

**Check.** This choice is about resolution. Before relying on Q, the technician
should still check for a zero error and repeat measurements. Fine resolution
does not replace those checks.

Two instruments are working correctly. One distinguishes **0.1 °C** changes and
the other distinguishes **0.01 °C** changes. A temperature change of **0.04 °C**
must be observed. Which instrument is the better choice?

- **A:** The instrument with 0.01 °C resolution.
- **B:** The instrument with 0.1 °C resolution.

**Feedback for A:** Correct. A change of 0.04 °C is larger than several 0.01 °C
steps, so the finer-resolution instrument can distinguish it.

**Feedback for B:** Not correct. The 0.04 °C change is smaller than one 0.1 °C
step, so that display may not show the change clearly.

## A reliable answer method

When an exam question gives repeated readings and a true value, take these steps.

1. **Find the comparison being asked for.** Is it reading-to-reading agreement,
   comparison with the true value, or instrument capability?
2. **For precision, inspect the spread or range.** Small spread means high
   precision.
3. **For accuracy, compare with the true value.** Small difference means high
   accuracy.
4. **For resolution, inspect the smallest distinguishable change.** Choose an
   instrument fine enough for the required measurement.
5. **Keep causes separate from descriptions.** A systematic error can explain a
   consistent offset. Random variation can explain scatter. Do not claim a
   cause that the data cannot establish.

## Core recap

- **Precision** is **the degree of agreement among repeated measurements,
  indicated by their spread or range**. It asks whether readings are close to
  each other.
- **Accuracy** is **the closeness of a measured value to the true value of the
  quantity**. It asks whether a measurement is close to the true value.
- **Instrument resolution** is **the smallest change in a quantity that a
  measuring instrument can distinguish, usually set by its smallest scale
  division**. It asks what change the instrument can tell apart.
- High precision, high accuracy and fine resolution are useful, but they are
  not interchangeable claims.

The next lesson uses this language when assessing uncertainty in a quantity
calculated from measurements.
