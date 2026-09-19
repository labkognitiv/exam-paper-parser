---
name: verify-physics-p2-paper-knowledge-base
description: Independently verify every answerable leaf and deterministic contract of one Cambridge Physics 9702 P2 enrichment paper.
---

# Verify Physics 9702 P2

Read repository instructions and [the verification contract](references/verification-contract.md). Process one paper at a time.

1. Enumerate every answerable leaf from canonical questions and immutable official mark schemes.
2. Before scripts, manually compare each leaf's full prompt/context, official criteria, outcome text, skill descriptions, ordered hints, walkthrough, and checking object.
3. Judge physics truth, outcome relevance, hint progression, skill scope, and checking-mode fit for every leaf. Existing reviews never replace this fresh pass.
4. After every leaf is reviewed, run for each question:
   `python3 scripts/audit_p2_question.py --repo . --paper <paper> --question <number>`
5. Run the paper wrapper:
   `python3 subjects/physics/9702/reviews/skills/verify-physics-p2-paper-knowledge-base/scripts/audit_paper.py --repo . --paper <paper>`
6. Preserve manual defects even when scripts pass. Repair only when authorized, then rerun the audit and manually recheck affected leaves.
7. Write `subjects/physics/9702/reviews/p2/<paper>.review.md` and update the existing row in `subjects/physics/9702/reviews/p2/verification-progress.md`.

Manual first. Deterministic second. Never waive script failures. Official mark schemes are immutable. Keep `numerical_values_checked: false`. PASS requires zero semantic and deterministic failures.
