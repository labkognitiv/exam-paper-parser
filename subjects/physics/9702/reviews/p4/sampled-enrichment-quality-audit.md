# Physics 9702 P4 sampled enrichment quality audit

Last checked: 2026-08-30

## Scope

Q01 was selected consistently from each of the 69 canonical P4 papers. Ten
papers have no Q01 enrichment, so 59 enrichment records containing 281
answerable leaves were available for review.

This is a sampling audit, not a full-paper certification. `SAMPLE PASS` means
that the inspected Q01 passed; it does not certify the remaining questions in
that paper.

The available samples were compared with their canonical questions and official
mark-scheme records. The review checked:

- whether AI-rubric observables and checking configuration represent the exact
  credited work safely;
- whether hints are personalized to the actual objects, quantities, figures,
  dependencies or conceptual decision in the question;
- whether walkthroughs solve or explain that exact question instead of using
  reusable generic prose; and
- both current deterministic gates:
  `validate_p4_enrichment.py` and `audit_structured_question.py`.

Uniqueness was not used as a quality measure. Repeated wording was accepted when
the underlying question and credited physics were genuinely equivalent.

## Results

| Measure | Count |
|---|---:|
| Canonical papers sampled | 69 |
| Q01 enrichments available | 59 |
| Q01 enrichments unavailable | 10 |
| Answerable leaves inspected | 281 |
| Leaves with at least two hints | 281 |
| Generic or unrelated hint failures | 0 |
| Generic or unrelated walkthrough failures | 0 |
| AI-rubric / checking-quality failures | 5 papers |
| Hint formatting failures | 1 paper |
| Walkthrough style failures | 1 paper |
| `validate_p4_enrichment.py` failures | 12 papers |
| `audit_structured_question.py` failures | 10 papers |
| Papers failing either deterministic gate | 22 |
| Sample passes | 37 papers |

No sampled enrichment contained a physics solution that was visibly unrelated
to its question. The hints and walkthroughs are personalized under the requested
definition. The failed samples are primarily blocked by controlled-ID scope,
legacy response/checking contracts, unsafe automatic-marking settings, mapping
order, or formatting. These are still real enrichment-quality failures and must
not be treated as passes.

`numerical_values_checked` remains `false`. This sampled comparison does not
replace a separately authorised corpus-wide numerical review.

## Paper tracker

`V` is `validate_p4_enrichment.py`; `A` is
`audit_structured_question.py`. A hint or walkthrough can be personalized but
still fail quality because of malformed notation or prohibited wording.

| Paper | Sample | AI rubric / checking | Hints | Walkthrough | Gates | Result | Note |
|---|---|---|---|---|---|---|---|
| `9702_m16_42` | Q01 | PASS | PASS | PASS | V FAIL; A PASS | **SAMPLE FAIL** | circular-motion supporting skill outside mapped topic |
| `9702_m17_42` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_m18_42` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_m19_42` | Q01 | PASS | PASS | PASS | V FAIL; A PASS | **SAMPLE FAIL** | circular-motion supporting skill outside mapped topic |
| `9702_m20_42` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_m21_42` | Q01 | PASS | PASS | PASS | V FAIL; A PASS | **SAMPLE FAIL** | circular-motion supporting skill outside mapped topic |
| `9702_m22_42` | Q01 | FAIL | PASS | PASS | V FAIL; A PASS | **SAMPLE FAIL** | three skill-topic mismatches; one official criterion ID is not bound in the rubric |
| `9702_m23_42` | Q01 | FAIL | PASS | PASS | V PASS; A FAIL | **SAMPLE FAIL** | legacy response schema; non-canonical fields; unsafe multi-mark auto-checking; mapping faults |
| `9702_m24_42` | Q01 | FAIL | PASS | PASS | V PASS; A FAIL | **SAMPLE FAIL** | legacy response schema; non-canonical fields; unsafe multi-mark auto-checking; mapping faults |
| `9702_m25_42` | Q01 | PASS | PASS | PASS | V PASS; A FAIL | **SAMPLE FAIL** | legacy response schema; figure placement and mapping-order faults |
| `9702_s16_41` | Q01 | PASS | PASS | PASS | V PASS; A FAIL | **SAMPLE FAIL** | legacy response schema and historical official-criterion placement mismatch |
| `9702_s16_42` | Q01 | FAIL | PASS | PASS | V PASS; A FAIL | **SAMPLE FAIL** | legacy response schema; unsafe multi-mark auto-checking; figure and mapping faults |
| `9702_s16_43` | Q01 | N/A | N/A | N/A | N/A | **NOT AVAILABLE** | no P4 enrichment exists for this paper |
| `9702_s17_41` | Q01 | PASS | PASS | PASS | V FAIL; A PASS | **SAMPLE FAIL** | circular-motion supporting skill outside mapped topic |
| `9702_s17_42` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_s17_43` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_s18_41` | Q01 | PASS | PASS | PASS | V FAIL; A PASS | **SAMPLE FAIL** | primary circular-motion skill outside mapped topic |
| `9702_s18_42` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_s18_43` | Q01 | N/A | N/A | N/A | N/A | **NOT AVAILABLE** | no P4 enrichment exists for this paper |
| `9702_s19_41` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_s19_42` | Q01 | PASS | PASS | PASS | V FAIL; A PASS | **SAMPLE FAIL** | moments/couples supporting skill outside mapped topic |
| `9702_s19_43` | Q01 | PASS | PASS | PASS | V FAIL; A PASS | **SAMPLE FAIL** | circular-motion and energy supporting skills outside mapped topic |
| `9702_s21_41` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_s21_42` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_s21_43` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_s22_41` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_s22_42` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_s22_43` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_s23_41` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_s23_42` | Q01 | FAIL | FAIL (format) | PASS | V FAIL; A PASS | **SAMPLE FAIL** | skill-topic mismatch; malformed LaTeX and missing symbol in one hint/rubric observable; content remains question-specific |
| `9702_s23_43` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_s24_41` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_s24_42` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_s24_43` | Q01 | PASS | PASS | PASS | V PASS; A FAIL | **SAMPLE FAIL** | legacy response schema and question-pattern ordering faults |
| `9702_s25_41` | Q01 | PASS | PASS | PASS | V PASS; A FAIL | **SAMPLE FAIL** | legacy response schema and mapping ownership/order faults |
| `9702_s25_42` | Q01 | PASS | PASS | PASS | V PASS; A FAIL | **SAMPLE FAIL** | legacy response schema and outcome-order fault |
| `9702_s25_43` | Q01 | PASS | PASS | PASS | V PASS; A FAIL | **SAMPLE FAIL** | legacy response schema and mapping ownership/order faults |
| `9702_s25_44` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w16_41` | Q01 | N/A | N/A | N/A | N/A | **NOT AVAILABLE** | no P4 enrichment exists for this paper |
| `9702_w16_42` | Q01 | N/A | N/A | N/A | N/A | **NOT AVAILABLE** | no P4 enrichment exists for this paper |
| `9702_w16_43` | Q01 | N/A | N/A | N/A | N/A | **NOT AVAILABLE** | no P4 enrichment exists for this paper |
| `9702_w17_41` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w17_42` | Q01 | PASS | PASS | PASS | V FAIL; A PASS | **SAMPLE FAIL** | circular-motion supporting skill outside mapped topic |
| `9702_w17_43` | Q01 | N/A | N/A | N/A | N/A | **NOT AVAILABLE** | no P4 enrichment exists for this paper |
| `9702_w18_41` | Q01 | PASS | PASS | PASS | V FAIL; A PASS | **SAMPLE FAIL** | conservation-of-energy supporting skill outside mapped topic |
| `9702_w18_42` | Q01 | N/A | N/A | N/A | N/A | **NOT AVAILABLE** | no P4 enrichment exists for this paper |
| `9702_w18_43` | Q01 | N/A | N/A | N/A | N/A | **NOT AVAILABLE** | no P4 enrichment exists for this paper |
| `9702_w19_41` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w19_42` | Q01 | N/A | N/A | N/A | N/A | **NOT AVAILABLE** | no P4 enrichment exists for this paper |
| `9702_w19_43` | Q01 | N/A | N/A | N/A | N/A | **NOT AVAILABLE** | no P4 enrichment exists for this paper |
| `9702_w20_41` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w20_42` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w20_43` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w21_41` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w21_42` | Q01 | PASS | PASS | FAIL (style) | V FAIL; A PASS | **SAMPLE FAIL** | walkthrough is personalized but uses prohibited phrase “the answer is” |
| `9702_w21_43` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w22_41` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w22_42` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w22_43` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w23_41` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w23_42` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w23_43` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w24_41` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w24_42` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w24_43` | Q01 | PASS | PASS | PASS | V PASS; A FAIL | **SAMPLE FAIL** | legacy response schema plus pattern/mapping-order faults |
| `9702_w25_41` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w25_42` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w25_43` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |
| `9702_w25_44` | Q01 | PASS | PASS | PASS | V PASS; A PASS | **SAMPLE PASS** | — |

## Interpretation

The sampled P4 hints and walkthroughs are not generic under the requested
question-personalization definition. Every available answerable leaf has at
least two hints, and the sampled scaffolding refers to the actual quantities,
figures, physical systems, equations or decisions required by its question.

P4 is nevertheless not quality-clean. Twenty-two available Q01 records fail at
least one current deterministic contract, and ten papers cannot be sampled
because their enrichment is absent. The highest-priority content/checking repairs
are `9702_m22_42`, `9702_m23_42`, `9702_m24_42`, `9702_s16_42` and
`9702_s23_42`; the remaining failures are mainly taxonomy/linkage, legacy-schema,
ordering or style faults.
