---
name: run-physics-p2-paper-knowledge-base
description: Orchestrate authoring, repair, independent verification, and release of one complete Cambridge Physics 9702 Paper 2 enrichment paper.
---

# Run the Physics P2 knowledge pipeline

Manage separate authoring and verification passes. An author cannot certify its own work.

## Sequence

1. Read repository `AGENTS.md`, the nearest scoped instructions, and [release gates](references/release-gates.md).
2. Inventory and hash canonical questions and immutable official mark schemes under `subjects/physics/9702/papers/p2/`.
3. Invoke `$enrich-physics-p2-paper-knowledge-base` for the complete paper.
4. Invoke `$verify-physics-p2-paper-knowledge-base` from primary artifacts, without giving it the author's conclusions.
5. Return any exact defect list to the author. Permit only scoped enrichment or registry repairs. Use a canonical-repair workflow separately for proven extraction defects.
6. Run fresh independent verification after every repair. Never waive a failed gate.
7. Rebuild derived reviewer or search data only after PASS.
8. Compare final canonical and official-source hashes with preflight hashes.
9. Report counts, registry additions, justified exceptions, repairs, and final PASS or FAIL.

Use distinct agents for authoring and verification when delegation is available and authorized. Never modify official mark-scheme JSON. Keep `numerical_values_checked: false` unless a separately authorized numerical-review workflow changes it.
