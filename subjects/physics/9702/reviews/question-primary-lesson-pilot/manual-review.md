# Question primary-lesson pilot: manual review

Date: 2026-09-19  
Model: `meta/muse-spark-1.3-contributor`  
Scope: one AS P2 paper (`9702_m22_22`) and one A2 P4 paper (`9702_m22_42`)

## Result

- Structural validity: 19/19 questions have exactly one active primary lesson.
- Manual agreement: P2 7/7; P4 12/12.
- Each derived topic is the parent of the selected lesson.
- Existing part-level mappings were supplied as evidence and were not changed.
- No secondary lessons were produced.

## Decisions

| Question | Primary lesson | Manual verdict |
|---|---|---|
| `9702_m22_22_q01` | `9702_t03_cm02_l05` terminal velocity | Accept: terminal force balance owns the complete setup; upthrust is supporting calculation. |
| `9702_m22_22_q02` | `9702_t02_cm05_l11` projectiles | Accept: independent horizontal and vertical motion unifies the question. |
| `9702_m22_22_q03` | `9702_t03_cm01_l02` momentum | Accept: momentum change and force are the central chain; density and pressure support it. |
| `9702_m22_22_q04` | `9702_t06_cm04_l08` elastic potential energy | Accept: spring energy/compression owns the largest coherent assessed section. |
| `9702_m22_22_q05` | `9702_t07_cm07_l13` polarisation | Accept: largest single assessed section; stationary waves and Doppler are separate supporting sections. |
| `9702_m22_22_q06` | `9702_t09_cm04_l09` resistivity and geometry | Accept: conductor geometry drives the distinctive comparison and explanation. |
| `9702_m22_22_q07` | `9702_t11_cm03_l05` quarks, hadrons and leptons | Accept: quark composition connects the decay subpart to the complete baryon section. |
| `9702_m22_42_q01` | `9702_t13_cm02_l03` gravitational orbits | Accept: orbital derivation and calculation dominate. |
| `9702_m22_42_q02` | `9702_t16_cm02_l02` first law of thermodynamics | Accept: first-law definition and cycle application own 5/10 marks. |
| `9702_m22_42_q03` | `9702_t17_cm01_l01` defining simple harmonic motion | Accept: the restoring-force condition frames the oscillation derivation. |
| `9702_m22_42_q04` | `9702_t18_cm01_l01` electric fields and force | Accept: field-line meaning and force direction frame the potential calculation. |
| `9702_m22_42_q05` | `9702_t19_cm03_l05` capacitor discharge | Accept: time constant and exponential discharge own 6/10 marks. |
| `9702_m22_42_q06` | `9702_t20_cm05_l11` Lenz's law | Accept: statement and opposing-force explanation own 5/7 marks. |
| `9702_m22_42_q07` | `9702_t21_cm01_l01` alternating voltage and power | Accept: waveform equation and mean power own 4/6 marks. |
| `9702_m22_42_q08` | `9702_t22_cm03_l08` de Broglie wavelength | Accept: formula and changed diffraction pattern form the central chain. |
| `9702_m22_42_q09` | `9702_t23_cm02_l07` exponential decay and half-life | Accept: graph, decay constant and changing nuclei form the central chain. |
| `9702_m22_42_q10` | `9702_t24_cm02_l04` X-rays and attenuation | Accept: attenuation and contrast own 4/7 marks and the overall context. |
| `9702_m22_42_q11` | `9702_t24_cm03_l07` annihilation and PET | Accept: annihilation and image formation define the complete question. |
| `9702_m22_42_q12` | `9702_t25_cm01_l01` luminosity and radiant flux | Accept: luminosity establishes the star and supplies the later calculations. |

## Operational note

The provider repeatedly returned empty content for P2 Q4 when both images were attached. A bounded fallback used verified candidate lesson mark totals; the resulting choice was then checked manually against the complete question and official mark scheme. The final manifest records successful-response usage only, so it is not a full billing total for blank retries.

## Conclusion

The proposed hierarchy works for this pilot: assign one primary lesson to each complete structured question, then derive its topic from that lesson. Keep existing part-level lesson mappings for subpart discovery and explanation; do not duplicate them in the question-level classifier.
