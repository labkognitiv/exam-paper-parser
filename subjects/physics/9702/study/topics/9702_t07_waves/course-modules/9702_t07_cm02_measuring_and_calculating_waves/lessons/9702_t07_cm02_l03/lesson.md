# Measuring amplitude and frequency with a CRO and the wave equation

## The mystery of oscillating currents

In 1897, German physicist Karl Ferdinand Braun faced a puzzling technical barrier at the University of Strasbourg.
Alternating currents and early wireless signals reversed direction hundreds or thousands of times every second.
Existing mechanical galvanometers had moving coils and needles with substantial mass and inertia.
These heavy mechanical indicators could not respond fast enough, showing only a stationary blur or zero.

Braun looked for an indicator with virtually zero inertia.
He constructed an evacuated glass tube containing a cold cathode and a phosphorescent screen.
Braun realized that cathode rays consisted of tiny particles that could deflect instantaneously under changing electric forces.
These particles, later identified as electrons, responded to rapid voltage oscillations without mechanical delay.

To display oscillations across time, Braun reflected the moving luminous spot in a rotating mirror.
This continuous sweep converted the vertical back-and-forth motion into a steady, visible wave against time.
Braun received the 1909 Nobel Prize in Physics alongside Guglielmo Marconi for his pioneering work.

How can a beam of electrons sweeping across a calibrated grid reveal rapid oscillations?
How do we turn these glowing traces into quantitative measurements of amplitude, period, frequency, and wave speed?
In this lesson, we master oscilloscope measurements and derive the foundational wave equation.

## Fundamental wave properties

Before studying oscilloscope traces, recall the primary quantities that describe progressive waves.
A progressive wave transfers energy from one position to another without any net transfer of matter.
The particles of the medium vibrate about their equilibrium positions as the wave passes.

Displacement is the distance of a point on a wave from its equilibrium position in a specified direction.
Amplitude is the maximum displacement of a particle or point on a wave from its equilibrium position.
Wavelength is the minimum distance between two adjacent points on a wave that are in phase.

The period $T$ is the time taken for one complete oscillation or wave cycle.
Frequency $f$ is the number of complete oscillations or wave cycles per unit time, measured in hertz ($\text{Hz}$).
Period and frequency share a strict reciprocal relationship.
$$T = \frac{1}{f} \quad \text{and} \quad f = \frac{1}{T}$$
For any uniform motion, speed is defined as the distance travelled divided by the time taken.

## The cathode-ray oscilloscope graticule

A cathode-ray oscilloscope, abbreviated as a CRO, serves as a high-speed graphical voltmeter.
It displays how a potential difference varies with time on a transparent screen.
The screen is marked with a regular square grid known as a graticule.

Most graticules consist of centimetre squares called major divisions.
Each major division is typically divided into five smaller subdivisions of 0.2 centimetres each.
The screen is a calibrated grid where the vertical axis shows potential difference and the horizontal axis shows elapsed time.

Two main controls determine the scale of this coordinate grid.
The y-gain control, also called the voltage sensitivity, sets the vertical scale in volts per division ($\text{V div}^{-1}$) or volts per centimetre ($\text{V cm}^{-1}$).
The time-base control, often called the sweep rate, sets the horizontal scale in seconds per division ($\text{s div}^{-1}$) or seconds per centimetre ($\text{s cm}^{-1}$).

For quantitative measurements, both control dials must click into their calibrated detent positions.
A detent is a mechanical click-stop that locks a rotary switch to a fixed calibration.
If a variable fine-trim knob is left uncalibrated, the markings on the dials will not match the true scale.
Always verify that both dials rest in their calibrated positions before taking measurements.

## Measuring signal amplitude with the y-gain

A microphone detects sound waves and generates an alternating potential difference across the vertical input terminals.
The incoming voltage deflects the electron beam vertically in direct proportion to the potential difference.
A larger sound wave produces a taller vertical deflection on the oscilloscope screen.

To measure signal amplitude, first find the horizontal equilibrium centre line.
Next, count the number of vertical divisions from the centre line to the peak of a crest.
We calculate peak voltage $V_0$ by multiplying the vertical displacement by the y-gain setting.
$$V_0 = \text{vertical divisions} \times \text{y-gain}$$
This peak voltage represents the amplitude of the electrical signal.

Be careful with unit prefixes during this calculation.
Oscilloscope y-gain settings are frequently stated in millivolts per division ($\text{mV div}^{-1}$).
Remember that $1\text{ mV} = 10^{-3}\text{ V}$ and $1\text{ }\mu\text{V} = 10^{-6}\text{ V}$.

### Worked Example 1: Measuring signal amplitude

A microphone detects a pure sound note, producing a sinusoidal trace on a CRO screen.
The y-gain is set to $2.5\text{ mV cm}^{-1}$.
The trace extends 3.2 cm vertically from its central equilibrium axis to a crest.
Calculate the amplitude of the electrical signal in volts.

**Answer**
The peak voltage of the electrical signal is $8.0\text{ mV}$.
Expressed in base units, the signal amplitude is $8.0 \times 10^{-3}\text{ V}$.

**Explanation**
Identify the vertical displacement from the equilibrium line to a peak crest.
The crest lies 3.2 cm above the centre line.
We multiply the vertical divisions by the y-gain setting to find the peak voltage.
Convert millivolts to volts by multiplying by $10^{-3}\text{ V mV}^{-1}$ to obtain $8.0 \times 10^{-3}\text{ V}$.

## Peak voltage versus peak-to-peak voltage

Students often confuse peak voltage with peak-to-peak voltage.
Peak voltage $V_0$ is measured strictly from the equilibrium centre line to a maximum crest.
This peak voltage equals the true wave amplitude.

In contrast, peak-to-peak voltage $V_{\text{p-p}}$ measures the entire vertical height from trough to crest.
The peak-to-peak voltage is exactly twice the signal amplitude.
We express this relationship using $V_{\text{p-p}} = 2 V_0$ or $V_0 = V_{\text{p-p}} / 2$.
Never report peak-to-peak voltage as the wave amplitude without dividing by two.

Measuring peak-to-peak height is helpful when the equilibrium centre line is unlabelled or shifted vertically.
You measure the total vertical span between minimum and maximum extremes.
Dividing that total span by two gives the correct amplitude without guessing the centre position.

## Measuring period and frequency with the time-base

The horizontal axis represents the steady progression of time.
An internal time-base circuit sweeps the electron beam horizontally from left to right at constant speed.
The time-base setting indicates how much time passes per centimetre or division.

The horizontal separation between two successive identical points represents the time period of one complete cycle.
You can measure from crest to crest, from trough to trough, or between matching zero-crossings.
Multiplying this horizontal distance by the time-base setting yields the wave period $T$.

Measuring only a single cycle across a few millimetres can introduce substantial reading uncertainty.
Measuring across several cycles spreads the reading uncertainty across the entire measured span.
To find the period $T$, measure the total horizontal span for $N$ complete cycles.
$$T = \frac{\text{total horizontal distance} \times \text{time-base}}{N}$$
Once period $T$ is determined in seconds, calculate frequency using $f = 1/T$.

Always check the time prefix on the time-base dial before calculating frequency.
Settings are commonly specified in milliseconds per centimetre ($\text{ms cm}^{-1}$) or microseconds per centimetre ($\mu\text{s cm}^{-1}$).
Remember that $1\text{ ms} = 10^{-3}\text{ s}$ and $1\text{ }\mu\text{s} = 10^{-6}\text{ s}$.

### Worked Example 2: Determining period and frequency

A sound wave produces a trace on a CRO with a time-base setting of $0.20\text{ ms cm}^{-1}$.
Two complete cycles span a horizontal distance of 8.0 cm across the screen graticule.
Determine the period and the frequency of the sound wave.

**Answer**
The period of the sound wave is $8.0 \times 10^{-4}\text{ s}$.
The corresponding frequency of the wave is $1300\text{ Hz}$.

**Explanation**
First, determine the horizontal distance corresponding to one complete cycle.
Two full cycles occupy 8.0 cm, so one cycle occupies 4.0 cm.
Multiply this distance by the time-base setting to find a period of $8.0 \times 10^{-4}\text{ s}$.
Taking the reciprocal gives a frequency of 1250 Hz, which rounds to $1300\text{ Hz}$.

## Calculating the time-base setting

Examiners often present a trace alongside a known signal frequency and ask for the time-base setting.
To solve this reverse problem, you first find the period using $T = 1/f$.
Next, count how many centimetres or divisions correspond to one complete cycle on the screen.

Dividing the period by the horizontal span of one cycle gives the time-base setting.
We express this calculation with the following formula.
$$\text{time-base setting} = \frac{T}{x_{\text{cycle}}} = \frac{1}{f \times x_{\text{cycle}}}$$
The resulting value carries units of seconds per centimetre ($\text{s cm}^{-1}$) or seconds per division ($\text{s div}^{-1}$).

Alternatively, you can measure the total horizontal span for multiple cycles.
Divide the total time for all observed cycles by the total distance across those cycles.
Both approaches yield the identical time-base setting.

### Worked Example 3: Finding the time-base setting

A sound wave with a frequency of 5000 Hz is detected by a microphone and displayed on a CRO.
On the screen graticule, exactly 1.5 cycles occupy a total horizontal width of 6.0 cm.
Calculate the time-base setting of the oscilloscope in $\text{s cm}^{-1}$.

**Answer**
The period of one complete sound cycle is $2.0 \times 10^{-4}\text{ s}$.
The calculated time-base setting is $5.0 \times 10^{-5}\text{ s cm}^{-1}$.

**Explanation**
Begin by calculating the wave period from the known frequency of 5000 Hz.
Using $T = 1/f$, the period is $1 / 5000\text{ s}^{-1} = 2.0 \times 10^{-4}\text{ s}$.
Because 1.5 cycles span 6.0 cm, one full cycle occupies $6.0\text{ cm} / 1.5 = 4.0\text{ cm}$.
Dividing the period by this distance gives $(2.0 \times 10^{-4}\text{ s}) / 4.0\text{ cm} = 5.0 \times 10^{-5}\text{ s cm}^{-1}$.

## Adjusting oscilloscope controls

Adjusting the oscilloscope controls changes only the scale of the display and never alters the physical signal.
Turning a knob modifies how the incoming electrical signal is drawn on the screen.
The wave entering the instrument keeps its original frequency, period, and amplitude.

Consider the effect of adjusting the time-base control.
Increasing the time-base setting means each division represents a longer duration of time.
As a result, more wave cycles fit across the screen, compressing the trace horizontally.
Decreasing the time-base setting stretches the trace horizontally, showing fewer wave cycles.

Now consider the effect of adjusting the y-gain control.
Increasing the y-gain setting means each division represents a larger potential difference.
The displayed waveform becomes shorter, compressing the trace vertically.
Decreasing the y-gain setting increases the vertical height of the trace on the graticule.

## Deriving the wave equation

Now we derive the fundamental relationship connecting wave speed, frequency, and wavelength.
Consider a continuous progressive wave travelling with uniform speed $v$ through a medium.
The source of the wave undergoes continuous periodic oscillations with period $T$ and frequency $f$.

During one period, the wave pattern advances forward by exactly one wavelength.
Remember that medium particles oscillate back and forth about fixed points rather than travelling with the wave.
The advancing wave profile, however, covers distance $\lambda$ in time $T$.

By definition, uniform speed is distance travelled divided by time taken.
$$v = \frac{\text{distance}}{\text{time}} = \frac{\lambda}{T}$$
Recall that period and frequency are reciprocals, meaning $T = 1/f$.
Substituting this period into the speed equation proves that wave speed equals frequency multiplied by wavelength.
$$v = \frac{\lambda}{\frac{1}{f}} = f\lambda$$
This famous result is known as the wave equation.

## Deriving the wave equation for a wave train

Cambridge examinations also require deriving the wave equation across an extended wave train.
In a continuous wave train, each complete oscillation creates one additional wave cycle.
Suppose a source oscillates $N$ times with frequency $f$ during total elapsed time $t$.

Because each wave cycle occupies one wavelength $\lambda$, the leading wavefront travels total distance $d = N\lambda$.
Since the source oscillates $f$ times each second, the time required for $N$ oscillations is $t = N / f$.
We now apply the kinematics definition of uniform speed to this extended train.

Speed equals total distance travelled divided by total elapsed time.
$$v = \frac{d}{t} = \frac{N\lambda}{\frac{N}{f}}$$
The number of cycles $N$ appears in both numerator and denominator and cancels out completely.
This cancellation yields $v = f\lambda$.
The wave speed is independent of the number of cycles observed in the train.

## Applying the wave equation

The wave equation $v = f\lambda$ applies to all periodic waves, including sound, water, and electromagnetic waves.
We can rearrange the equation algebraically to solve for any unknown parameter.
$$\lambda = \frac{v}{f} \quad \text{and} \quad f = \frac{v}{\lambda}$$
Always ensure that units are coherent before performing substitutions.

Speed must be in metres per second ($\text{m s}^{-1}$), frequency in hertz ($\text{Hz}$), and wavelength in metres ($\text{m}$).
Exam questions frequently present values with metric prefixes such as kilohertz, megahertz, or nanometres.
All electromagnetic waves travel through free space at speed $c = 3.00 \times 10^8\text{ m s}^{-1}$.

### Worked Example 4: Calculating wavelength across wave types

A musical tuning fork produces sound in air at 440 Hz with speed $330\text{ m s}^{-1}$; calculate the wavelength.
An FM radio transmitter broadcasts at $98.5\text{ MHz}$; calculate its wavelength in air.

**Answer**
The wavelength of the musical sound wave is $0.75\text{ m}$.
The wavelength of the radio transmitter broadcast is $3.05\text{ m}$.

**Explanation**
Always convert all metric prefixes into base SI units before performing calculations.
For the tuning fork, the speed of sound is $330\text{ m s}^{-1}$ and the frequency is $440\text{ Hz}$.
Rearranging the wave equation gives $\lambda = v / f = 330\text{ m s}^{-1} / 440\text{ Hz} = 0.75\text{ m}$.

For the radio transmitter, convert $98.5\text{ MHz}$ into $98.5 \times 10^6\text{ Hz}$.
Radio waves travel at the speed of light, $c = 3.00 \times 10^8\text{ m s}^{-1}$.
Applying $\lambda = c / f$ yields $(3.00 \times 10^8\text{ m s}^{-1}) / (98.5 \times 10^6\text{ Hz}) = 3.05\text{ m}$.

## Synthesizing CRO traces with wave calculations

In real physics experiments, an oscilloscope is paired with a sensor such as a microphone or optical detector.
The oscilloscope records the variation of voltage with time.
It allows us to measure the time period $T$ and deduce the wave frequency $f$.

Crucially, an oscilloscope alone cannot measure the physical wavelength in metres.
The horizontal axis displays time in seconds, not distance in space.
To find wavelength or wave speed, you must combine the CRO measurement with an external piece of data.

If the propagation speed in the medium is known, calculate wavelength using $\lambda = v / f = v T$.
If the wavelength is measured along a metre rule, calculate the wave speed using $v = f\lambda$.
This synthesis connects laboratory voltage measurements directly to wave motion.

### Worked Example 5: Combining a CRO trace with wave speed

An optical sensor detects an electromagnetic wave in space and displays the trace on an oscilloscope.
The time-base setting is $5.0 \times 10^{-15}\text{ s cm}^{-1}$.
One complete wave cycle spans a horizontal distance of 6.0 cm on the graticule.
Calculate the wavelength of the detected radiation.

**Answer**
The period of the detected wave is $3.0 \times 10^{-14}\text{ s}$.
The calculated wavelength of the radiation is $9.0 \times 10^{-6}\text{ m}$.

**Explanation**
First, determine the time period from the oscilloscope trace dimensions.
Multiplying the horizontal distance by the time-base yields $T = 6.0\text{ cm} \times 5.0 \times 10^{-15}\text{ s cm}^{-1} = 3.0 \times 10^{-14}\text{ s}$.
Electromagnetic waves travel through space at speed $c = 3.00 \times 10^8\text{ m s}^{-1}$.
Multiplying the wave speed by the measured period gives the physical wavelength.

We compute the wavelength using $\lambda = c T = (3.00 \times 10^8\text{ m s}^{-1}) \times (3.0 \times 10^{-14}\text{ s}) = 9.0 \times 10^{-6}\text{ m}$.
Alternatively, calculate frequency $f = 1 / T = 3.33 \times 10^{13}\text{ Hz}$ and apply $\lambda = c / f$.
Both methods yield the identical wavelength of $9.0 \times 10^{-6}\text{ m}$.
