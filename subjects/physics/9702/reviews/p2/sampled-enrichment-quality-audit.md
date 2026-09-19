# Physics 9702 P2 sampled enrichment quality audit

Last checked: 2026-08-30

## Scope

One complete question was checked from each of the 69 P2 papers. Q01 was used
consistently to avoid cherry-picking. This is a sampling audit, not a full-paper
verification: `SAMPLE PASS` means the inspected question passed, not that every
question in that paper is certified.

The audit compared each sampled enrichment directly with its canonical question
and official mark scheme. It checked:

- whether every AI-rubric observable represents the exact credited criterion;
- whether hints are personalized to the question's objects, values, figures,
  dependencies or exact conceptual task;
- whether walkthroughs solve or explain the actual question rather than giving
  reusable generic prose; and
- deterministic schema, hierarchy, controlled-ID and official-binding checks.

Uniqueness was not used as a quality measure. Repeated wording was acceptable
where the underlying question and credited physics were genuinely equivalent.

## Results

- Sampled papers: 69
- Sampled questions: 69
- Sampled answerable leaves: 290
- AI-rubric failures: 0
- Hint-personalization failures: 0
- Walkthrough-personalization failures: 0
- Deterministic failures: 0
- Sample reviews: 0 papers
- Sample passes: 69 papers

### Repair notes

- The five 2017 samples previously limited to one hint per leaf now have two
  ordered, question-personalized hints per sampled leaf. The first hint frames
  the question-specific decision; the second gives the more explicit method.
- The four former skill-scope warnings were resolved by splitting broad skills
  into controlled scalar/vector property, vector-resultant, measurement-error,
  and uncertainty-propagation competencies and remapping only the affected
  leaves.
- All nine repaired Q01 records pass `audit_p2_question.py` with zero failures
  and zero AI checks.
- Numerical values were compared with the official mark-scheme records during
  this sample audit. The canonical `numerical_values_checked` field remains
  `false`; this report does not change that separate corpus-wide review state.

## Paper tracker

| Paper | Sample | AI rubric | Hints personalized | Walkthrough personalized | Result | Note |
|---|---|---|---|---|---|---|
| `9702_m16_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_m17_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | progressive hints repaired |
| `9702_m18_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_m19_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_m20_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_m21_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_m22_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_m23_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_m24_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_m25_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s16_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s16_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s16_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s17_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s17_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s17_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | progressive hints repaired |
| `9702_s18_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | skill scope repaired |
| `9702_s18_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s18_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | skill scope repaired |
| `9702_s19_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s19_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s19_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s21_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s21_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s21_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | skill scope repaired |
| `9702_s22_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s22_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s22_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s23_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s23_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s23_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s24_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s24_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s24_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s25_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s25_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s25_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_s25_24` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w16_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w16_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w16_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w17_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | progressive hints repaired |
| `9702_w17_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | progressive hints repaired |
| `9702_w17_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | progressive hints repaired |
| `9702_w18_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w18_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w18_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w19_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w19_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w19_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w20_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w20_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w20_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w21_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w21_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w21_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w22_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | skill scope repaired |
| `9702_w22_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w22_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w23_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w23_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w23_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w24_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w24_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w24_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w25_21` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w25_22` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w25_23` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |
| `9702_w25_24` | Q01 | PASS | PASS | PASS | **SAMPLE PASS** | — |

## Interpretation

The sampled P2 enrichment is not generic under the question-personalization
definition. Rubrics, hints and walkthroughs are tied to the actual assessed
content. The sampled progressive-hint and skill-scope issues have been repaired.
A full-paper accuracy
claim still requires every question in each paper to be manually reviewed under
the repository verification contract.
