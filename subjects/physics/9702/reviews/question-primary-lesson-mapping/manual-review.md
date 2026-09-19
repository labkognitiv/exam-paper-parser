# Whole-question primary-lesson mapping: full-corpus review

## Scope and result

- 1,256 complete structured questions: 476 AS P2 and 780 A2 P4 across 138 papers.
- Every record has exactly one active `primary_lesson_id`; it is one of that question's resolved part-level lesson candidates; `derived_topic_id` matches the active lesson's parent topic.
- No secondary lessons were emitted. Existing part-level lesson records, canonical papers, enrichment and official mark schemes were not changed.

## Decision evidence

- 1,177 records were mapped by Muse Spark from the complete compact question image, official mark-scheme image and resolved part-level evidence.
- 19 approved pilot decisions were reused after rechecking current active lesson and candidate membership.
- 60 records are explicitly low-confidence `verified_part_mark_fallback_after_provider_blank` decisions: Muse returned empty or malformed JSON after five bounded attempts, including the compact-image and verified-evidence prompts. Each falls back to the candidate with the greatest sum of unchanged resolved-part marks. All 60 tied at the greatest mark total, so their stable candidate ordering is retained and the IDs, mark totals and provider errors remain in their individual review JSON records.

## Audit

- Structural audit: PASS, 1,256/1,256 active-lesson, candidate-membership and derived-topic checks passed.
- Source/mark-scheme audit: the original 19-question pilot remains accepted (P2 7/7, P4 12/12). The 60 provider fallback edge records were reviewed from their complete retained part evidence and are intentionally flagged `low`, not promoted as high-confidence semantic decisions.
- Representative cross-topic Muse sample and every fallback edge record are traceable at `p2/*.json` and `p4/*.json`; any later human correction can replace only the evidence record without touching canonical mapping data.

## Cost and retry accounting

- Provider-reported successful-response cost: $0.64298.
- Recorded request attempts: 1,817. Empty/malformed provider responses did not return usage/cost fields, so their charge is unavailable rather than treated as zero-cost evidence.
