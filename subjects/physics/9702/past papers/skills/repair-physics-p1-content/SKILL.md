---
name: repair-physics-p1-content
description: Audit, normalize, and repair Cambridge AS Physics 9702 Paper 1 (MCQ) enrichment packages and canonical metadata. Fixes cross-topic skill misassignments, taxonomy hierarchy conflicts, distractor walkthrough gaps, hint giveaways, and LaTeX math formatting without modifying immutable official answers.
---

# Repair Physics P1 (MCQ) Content

Repair and normalize one or more Cambridge International AS Level Physics 9702 Paper 1 (40 MCQs per paper) enrichment packages.

## Operating Mode & Strict Constraints

1. **Source Immutability**:
   - Official `correct_answer` in `question_XX.json` and `answer_key.json` is immutable official truth. Never change an official answer key.
   - Question image crops (`question_XX.png`) are canonical visual evidence and must not be altered or recropped.
2. **Flat P1 Schema Contract (`9702_p1_enrichment_v1`)**:
   - Every MCQ must have: `question_id`, `component: "P1"`, `difficulty` (1–3), `question_patterns`, `topic_id`, `module_id`, `skill_id`, `accepted_answer`, `hints` (>= 2), and `walkthrough` (>= 2).
3. **Controlled Scope & Boundary Rules**:
   - `skill_id` MUST be compatible with the question's `topic_id` as registered in `subjects/physics/9702/knowledge/skills.json`.
   - `module_id` MUST belong to `topic_id` in `subjects/physics/9702/knowledge/2025-2027/as/9702-2025-2027-as-taxonomy.json`.

---

## Common Error Patterns & Deterministic Repair Table

During corpus sweeps, the most frequent failure modes and their standard repairs are:

| Failure Mode | Defect Signature | Standard Repair Action |
| :--- | :--- | :--- |
| **Superposition vs. Waves Skill** | Topic `9702_t08` (Superposition) assigned wave skills (`9702_skill_progressive_wave_properties` or `9702_skill_wave_intensity_amplitude`). | Assign in-topic skill: `9702_skill_stationary_waves`, `9702_skill_two_source_interference`, `9702_skill_diffraction_grating`, or `9702_skill_single_slit_diffraction`. |
| **Electrical Power vs. Mechanics Power** | Topic `9702_t09` (Electricity) assigned `9702_skill_power_efficiency` (restricted to Topic 5 mechanics). | Assign in-topic skill: `9702_skill_potential_difference_power` or `9702_skill_electrical_circuits`. |
| **Deformation Work vs. Estimation** | Topic `9702_t06` (Deformation of solids) assigned `9702_skill_physical_estimations` (Topic 1). | Assign in-topic skill: `9702_skill_hookes_law_elastic_energy` or `9702_skill_stress_strain_young_modulus`. |
| **Static Equilibrium vs. Dynamics** | Topic `9702_t04` (Forces & Equilibrium) assigned `9702_skill_newtons_laws` (Topic 3). | Assign in-topic skill: `9702_skill_equilibrium_coplanar_forces` or `9702_skill_moments_couples`. |
| **Terminal Velocity vs. Motion Graphs** | Topic `9702_t03` (Non-uniform motion) assigned `9702_skill_motion_graphs` (Topic 2). | Assign in-topic skill: `9702_skill_drag_terminal_velocity`. |
| **DC Circuits vs. Current/PD** | Topic `9702_t09` assigned `9702_skill_kirchhoffs_laws` or `9702_skill_potential_dividers` (Topic 10). | Re-assign to `9702_skill_potential_difference_power` if single-component, or reclassify topic to `9702_t10` if circuit network. |
| **Hint Answer Giveaway** | Hints explicitly stating option letters ("The correct answer is C", "Select option B"). | Rewrite hint to provide progressive mathematical or physical scaffolding without mentioning option indices. |
| **Missing Distractor Diagnosis** | Walkthrough only proves why the correct option holds, ignoring distractors A, B, C, D. | Add clear diagnostic explanations of why common distractor choices / miscalculations are invalid. |
| **LaTeX Delimiter Asymmetry** | Unbalanced single dollar signs ($) or shell PID expansion artifacts ($$12345). | Normalize math spans with clean matching $ ... $ delimiters. |

---

## Step-by-Step Repair Workflow

1. **Run Paper Audit**:
   ```bash
   .venv/bin/python scripts/validate_p1_enrichment.py --paper [PAPER_CODE]
   ```
2. **Review Identified Defects**:
   - Inspect reported skill-topic mismatches, taxonomy violations, or schema failures.
3. **Execute Targeted Repairs**:
   - For skill-topic mismatches: consult `references/common-skill-mappings.md` and update `skill_id`.
   - For walkthroughs: ensure physical justification + full option distractor analysis.
   - For hints: ensure >= 2 progressive conceptual hints with zero answer giveaways.
4. **Re-Validate Paper**:
   - Re-run `scripts/validate_p1_enrichment.py --paper [PAPER_CODE]` and confirm **`PASS: [PAPER_CODE] (40/40 MCQs valid)`**.
5. **Verify Full Test Suite**:
   ```bash
   .venv/bin/python -m unittest discover tests
   ```

---

## Completion Gate

A paper repair is complete when:
- Exactly 40/40 MCQs pass `scripts/validate_p1_enrichment.py`.
- 0 skill-topic scope errors remain.
- All 40 accepted answers match canonical question answer keys byte-for-byte.
- No unit tests or regression checks fail.
