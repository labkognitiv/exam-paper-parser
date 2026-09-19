# Topic 1 Markdown audit

**PASS**

**HTML gate: OPEN.** All 9 active planned lessons and evidence records exist, cover 100% of the 12 syllabus learning outcomes, and have no unresolved topic-level defects.

## Topic-wide findings

- Coverage is complete against `syllabus.json` across all 5 course modules representing the 4 Cambridge syllabus modules:
  - `9702_t01_cm01` (Physical quantities and estimation):
    - `9702_t01_cm01_l01` owns physical quantity fundamentals, numerical magnitude, and unit scales (`9702_t01_m01_o01`).
    - `9702_t01_cm01_l02` owns reasonable estimation of physical quantities, benchmarks, scale bracketing, and rejecting unphysical scales (`9702_t01_m01_o02`).
  - `9702_t01_cm02` (SI units, prefixes, and homogeneity):
    - `9702_t01_cm02_l03` owns the 5 SI base quantity-unit pairs (mass in kg, length in m, time in s, electric current in A, temperature in K), the 10 decimal prefixes from pico to tera (p, n, μ, m, c, d, k, M, G, T), and expressing derived units as products or quotients of SI base units, including unpacking named units (N, J, W, C, Pa) and finding base units of unknown constants (`9702_t01_m02_o01`, `9702_t01_m02_o04`, `9702_t01_m02_o02`) [consolidated with retired `l04`].
    - `9702_t01_cm02_l05` owns using SI base units to test the homogeneity of physical equations, identifying dimensionless numbers/coefficients, determining unknown powers, and clarifying that homogeneity is necessary but not sufficient proof of physical correctness (`9702_t01_m02_o03`).
  - `9702_t01_cm03` (Measurement quality and errors):
    - `9702_t01_cm03_l06` owns systematic errors, zero errors with signs, random errors, their distinct physical origins, and their experimental remedies (`9702_t01_m03_o01`).
    - `9702_t01_cm03_l07` owns the distinction between precision, accuracy, and instrument resolution, selecting measuring apparatus based on resolution, and linking errors to precision and accuracy (`9702_t01_m03_o02`).
  - `9702_t01_cm04` (Combining uncertainties):
    - `9702_t01_cm04_l08` owns assessing uncertainty in derived quantities, converting between absolute, fractional, and percentage uncertainties, combining uncertainties for sums, differences, products, quotients, and powers, and reporting final values with matched decimal places (`9702_t01_m03_o03`).
  - `9702_t01_cm05` (Scalars and vectors):
    - `9702_t01_cm05_l09` owns distinguishing scalar and vector quantities, classifying syllabus quantities, and establishing magnitude, unit, and direction requirements (`9702_t01_m04_o01`).
    - `9702_t01_cm05_l11` owns resolving vectors into perpendicular components and adding and subtracting coplanar vectors graphically and trigonometrically (`9702_t01_m04_o03`, `9702_t01_m04_o02`) [consolidated with retired `l10`].
- Sequence is coherent and strictly prerequisite-led, forming an acyclic DAG with monotonic sequence 1 to 9. Each lesson depends only on established prerequisites, and closing handoffs match subsequent lesson openings.
- Repeated content represents purposeful retrieval:
  - Number-unit pairings from `l01` are retrieved in `l02` for approximate reporting, in `l03` for base-unit tracking, in `l06` for signed zero corrections, in `l08` for uncertainty specifications, and in `l09` and `l11` for vector representations.
  - Derived unit expansions from `l03` provide the necessary foundation for testing equation homogeneity in `l05`.
  - Error diagnosis from `l06` establishes the physical mechanisms underlying precision, accuracy, and resolution distinctions in `l07` and uncertainty propagation in `l08`.
  - The controlled vector definition from `l09` is immediately retrieved and applied to two-dimensional resolution, addition, and subtraction in `l11`.
- Controlled definitions match approved registry records byte-for-byte:
  - Systematic error: "an error that causes measurements to be consistently offset from the true value in the same direction" (`9702_def_systematic_error` in `l06`).
  - Random error: "an unpredictable variation in repeated measurements that causes readings to scatter about the true value" (`9702_def_random_error` in `l06`).
  - Precision: "the degree of agreement among repeated measurements, indicated by their spread or range" (`9702_def_precision` in `l07`).
  - Accuracy: "the closeness of a measured value to the true value of the quantity" (`9702_def_accuracy` in `l07`).
  - Instrument resolution: "the smallest change in a quantity that a measuring instrument can distinguish, usually set by its smallest scale division" (`9702_def_instrument_resolution` in `l07`).
  - Scalar quantity: "a physical quantity that has magnitude only" (`9702_def_scalar_quantity` in `l09`).
  - Vector quantity: "a physical quantity that has magnitude and direction" (`9702_def_vector_quantity` in `l09` and retrieved in `l11`).
- Scientific accuracy is verified across all physical principles:
  - Prefixes are strictly applied with proper case sensitivity (milli $10^{-3}$ vs mega $10^6$), and kilogram is treated as the official base unit without stacked prefixes.
  - Unpacking named units (N, J, W, C, Pa) strictly follows defining physical relationships ($F=ma$, $W=Fd$, $P=W/t$, $Q=It$, $p=F/A$).
  - Homogeneity checks verify identical base units across all additive terms and both sides of an equation, correctly explaining that matching units do not guarantee physical correctness.
  - Zero errors preserve algebraic signs ($+$ or $-$) and are subtracted from raw readings.
  - Random variation is treated by taking repeated independent readings and calculating a mean, distinguishing this from systematic offset correction.
  - Uncertainty propagation rigorously follows syllabus rules: adding absolute uncertainties for sums and differences; adding percentage or fractional uncertainties for products and quotients; multiplying percentage uncertainty by the power index for powers. Final values are quoted to matching decimal precision.
  - Vector resolution explicitly identifies the placement of angle $\theta$ relative to reference axes, assigning $V\cos\theta$ to the adjacent component and $V\sin\theta$ to the opposite component rather than making unverified horizontal/vertical assumptions. Vector subtraction is defined as adding the reversed vector $\vec{A} + (-\vec{B})$.
- Misconceptions addressed across the topic:
  - Treating numerical magnitude alone as a complete physical quantity.
  - Attaching unsupported precision (excess significant figures) to rough estimates.
  - Confusing prefix multipliers or mistaking unit symbols for prefixes (e.g. metre vs milli).
  - Assuming that passing a homogeneity unit check proves an equation is physically correct.
  - Believing that repeated readings or averaging can eliminate systematic errors.
  - Conflating precision with accuracy, or assuming high precision guarantees high accuracy.
  - Adding percentage uncertainties for sums or differences instead of absolute uncertainties.
  - Forgetting to multiply percentage uncertainty by the power for quantities raised to an exponent.
  - Treating vector quantities as scalars and adding perpendicular components directly.
  - Assuming horizontal components always use cosine and vertical components always use sine.
  - Omitting directions or directional signs from resolved vector components.
- Evidence provenance is complete across all 9 active lessons, with 76 authentic question parts inspected and catalogued in detail across Paper 1 and Paper 2 from Cambridge 9702 series (2016-2025).

## Lesson decisions

| Lesson | Decision | Audit result |
| :--- | :--- | :--- |
| `9702_t01_cm01_l01` | keep | Covers outcome m01_o01; physical quantities, numerical magnitude, unit scales, and algebraic unit tracking. |
| `9702_t01_cm01_l02` | keep | Covers outcome m01_o02; physical estimations, everyday benchmarks, scale bracketing, and honest precision. |
| `9702_t01_cm02_l03` | repaired | Covers outcomes m02_o01, m02_o04, and m02_o02; SI base quantities, decimal prefixes, and derived units in base-unit form (repaired LaTeX control character escaping for \times and \frac resulting from consolidation). |
| `9702_t01_cm02_l05` | keep | Covers outcome m02_o03; equation homogeneity, base-unit substitutions, dimensionless coefficients, and unknown powers. |
| `9702_t01_cm03_l06` | keep | Covers outcome m03_o01; systematic errors, signed zero errors, random errors, and measurement plan for wire diameter. |
| `9702_t01_cm03_l07` | keep | Covers outcome m03_o02; precision, accuracy, instrument resolution, and apparatus selection. |
| `9702_t01_cm04_l08` | keep | Covers outcome m03_o03; absolute, fractional, and percentage uncertainty, propagation rules, and significant figure matching. |
| `9702_t01_cm05_l09` | keep | Covers outcome m04_o01; scalar vs vector definitions, syllabus quantity classifications, and magnitude-unit-direction completeness. |
| `9702_t01_cm05_l11` | repaired | Covers outcomes m04_o03 and m04_o02; resolving vectors into perpendicular components and adding/subtracting coplanar vectors (repaired unclosed inline LaTeX delimiter on line 385; consolidated from retired l10). |

## Validator output

```
Loaded 25 topics, 300 total learning outcomes from syllabus.
[PASS] 9702_t01_physical_quantities_and_units: 100% verified
==================================================
VALIDATION COMPLETE: 1 topics checked.
100% PASS: All 25 topics, course modules, lessons, DAGs, and zero em dashes verified.
```

```
Active lessons: 147
Redirects: 47
Errors: 0
PASS
```

## Unresolved mapping or knowledge-base issues

- None requiring separate authorization.
- Tracker schema observation: `study/LESSON-PRODUCTION-TRACKER.md` currently tracks only `Specification` status. As stipulated by repository authoring instructions, no custom columns were introduced and completion tracking awaits tracker schema expansion by its owner.
