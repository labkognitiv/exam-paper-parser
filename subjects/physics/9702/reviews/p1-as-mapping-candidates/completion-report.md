# Physics 9702 P1 AS lesson mapping completion

PASS. All 69 papers and 2,760 MCQs have valid non-null lesson tuples: 2,682 direct, 8 contextual-skill and 70 legacy-content. All 13 first-pass low-confidence rows received a five-image review; 13 remain honestly low confidence.

- Primary full run: 2,235.886 s.
- Targeted five-row repair: 21.381 s.
- Primary plus repair: 2,257.267 s.
- Separate preflight proof: 87.411 s.
- Known model elapsed time: 8,611.184 s across retained calls.
- Known cost: $0.995448986.
- Known tokens: 10,586,744 prompt + 762,776 completion = 11,349,520.
- Exact total cost/tokens unavailable: one null-content response escaped before atomic receipt persistence.
- Historical failed calls: 7. Final unresolved failures: 0.

Validator evidence:

- `python3 -m py_compile scripts/p1/bulk_map_p1_as_candidates.py` PASS.
- `python3 scripts/p1/bulk_map_p1_as_candidates.py --validate-only` PASS.
- `python3 scripts/p1/bulk_map_p1_as_candidates.py --finalize-only` PASS.
- `python3 subjects/physics/9702/scripts/taxonomy/validate_topic_curriculum.py` PASS: 25 topics, 300 outcomes, module/lesson structures and prerequisite DAGs.

Outputs: `reference-validation.json`, `manifest.json`, `resolved-all.json`, and per-paper `candidate.json`, `firstpass.json`, `resolved.json`, `meta.json` in this directory.
