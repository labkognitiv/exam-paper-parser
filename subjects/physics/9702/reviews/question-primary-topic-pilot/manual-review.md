# Physics question-primary-topic pilot review

- Papers: `9702_m22_22` (P2) and `9702_m22_42` (P4)
- Questions: 19 total
- Deterministic single-topic assignments: 6
- Muse decisions: 13
- HTTP attempts: 24, including empty-response retries
- Recorded successful-response cost: $0.015377698
- Structural result: 19/19 valid

## Manual semantic result

- P2: 7/7 primary topics accepted.
- P4: 11/12 primary topics accepted.
- Overall: 18/19 primary topics accepted.

Required correction:

- `9702_m22_42_q02`: primary should be `9702_t16` Thermodynamics, not `9702_t15` Ideal gases. The first-law/internal-energy work carries the dominant assessed demand; Muse returned medium confidence.

## Secondary-topic warning

Do not promote the pilot's derived secondary lists as canonical. They faithfully aggregate the existing part-topic mappings, but several of those mappings are semantically incorrect. Examples:

- `9702_m22_42_q01` is a gravitational-fields question, yet existing parts introduce Alternating currents and Capacitance.
- `9702_m22_42_q03` is an oscillations question, yet existing parts introduce Ideal gases, Magnetic fields and Medical physics.
- `9702_m22_22_q06` is an electricity/resistivity question, yet an existing part introduces Deformation of solids.

Conclusion: Muse is suitable for choosing one whole-question primary from the candidate set, with mandatory review of medium/low-confidence outputs. Secondary aggregation is unsafe until the existing part mappings are repaired or independently revalidated.
