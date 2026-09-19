# 9702_t05_work_energy_and_power session log

Append concise dated handoffs for this topic only.

## 2026-09-11 - Topic 5 Lessons 1 and 2 Practice Questions authoring (9702_t05_cm01_l01 and 9702_t05_cm01_l02)

- Generated complete 20-question practice package for `9702_t05_cm01_l01` (Concept of work, W = Fs cos\theta, gas expansion W = p\Delta V, force-displacement graphs, positive, negative, and zero work) covering outcomes `9702_t05_m01_o01` and `9702_t05_m01_o02`.
- Tier distribution: exactly 10 MCQs (1 mark each), 5 drills (1-2 marks each), 3 medium (3-4 marks each), and 2 hard multipart questions (6 marks each) with full response structure and part enrichment; total 41 marks strictly reconciled.
- Generated complete 20-question practice package for `9702_t05_cm01_l02` (Conservation of energy, energy dissipation, efficiency calculations, Sankey diagrams, multi-stage systems) covering outcomes `9702_t05_m01_o03` and `9702_t05_m01_o04`.
- Tier distribution: exactly 10 MCQs (1 mark each), 5 drills (1-2 marks each), 3 medium (3-4 marks each), and 2 hard multipart questions (6 marks each) with full response structure and part enrichment; total 41 marks strictly reconciled.
- Verified SHA256 input hashes for `topic-markdown-audit.md` (61694194c01ad2ecc3c11f7fbd1dbbb1c7562cf98d8cacdc9710529bb4d8df66), `l01/lesson.md` (21a73e0fa586af80aff60279a6935b5582e0e5cf6344c00e3da4cda6b5026c19), and `l02/lesson.md` (09cba9af1b23e068fd337135ac010061a4c94efd26ca892226f6a85a496e6646) in respective `manifest.json` files.
- Verified strictly zero em dashes (\u2014) and zero en dashes (\u2013) across all 42 generated files (40 question JSONs + 2 manifests).
- Validated packages with `python3 subjects/physics/9702/scripts/validate_practice_questions.py`: both `9702_t05_cm01_l01` and `9702_t05_cm01_l02` passed with status PASS (20 questions, 41 marks each).
- Reported tracker schema gap: `study/LESSON-PRODUCTION-TRACKER.md` lacks a `Lesson questions` column; tracker status left unchanged.

## 2026-09-11 - Topic 5 Lessons 3 and 4 Markdown authoring (9702_t05_cm01_l03 and 9702_t05_cm01_l04)

- Authored `lesson.md` and `lesson-build-evidence.json` for `9702_t05_cm01_l03` (Power as work done per unit time) covering learning outcome `9702_t05_m01_o05`.
- Integrated byte-for-byte controlled definition `9702_def_power` ("work done or energy transferred per unit time") and controlled formula `9702_formula_power_energy_time` (\(P = \frac{\Delta E}{t}\)), with SI derived unit watt (\(\mathrm{W}\)) and SI base unit equivalent \(\mathrm{kg\,m^2\,s^{-3}}\).
- Authored three original worked examples with examination mark schemes ([M1], [A1], [B1]) covering industrial crane lifting, water pump efficiency with rate of thermal dissipation, and graphical analysis of energy-time gradient and power-time area. Included guided practice, four active A/B checks with dual-choice feedback, and five evidence-backed misconceptions.
- Authored `lesson.md` and `lesson-build-evidence.json` for `9702_t05_cm01_l04` (Problem solving with power, derivation and application of P = Fv, vehicles moving at constant speed against resistance) covering learning outcomes `9702_t05_m01_o06` and `9702_t05_m01_o07`.
- Developed formal five-step derivation of \(P = Fv\) from \(P = \frac{W}{t}\), \(W = Fs\), and \(s = vt\). Integrated controlled formula `9702_formula_mechanical_power` (\(P = Fv\)) and analyzed vector alignment (\(P = Fv\cos\theta\)).
- Formulated equilibrium conditions for vehicles at constant velocity on horizontal surfaces (\(F_{\text{drive}} = F_{\text{resist}}\)), inclined planes (\(F_{\text{drive}} = R + mg\sin\theta\)), continuous fluid pumping (\(P = \rho \frac{\Delta V}{\Delta t} gh\)), and cubic aerodynamic drag scaling (\(F \propto v^2 \implies P \propto v^3\)).
- Authored three original worked examples with examination mark schemes ([M1], [A1], [B1]) covering motorway cruising with engine fuel input, heavy truck climbing a slope against friction and parallel weight, and high-speed train quadratic drag scaling. Included guided practice, four active A/B checks with dual-choice feedback, and five evidence-backed misconceptions.
- Verified strictly zero em dashes and zero en dashes across all authored Markdown and JSON files.
- Validated all JSON files with `python3 -m json.tool`.
- Ran `python3 scripts/taxonomy/validate_topic_curriculum.py --topics 9702_t05` passing 100% with 0 errors; ran `python3 scripts/validate_lesson_redirects.py` passing 100% with 0 errors.
- Reported tracker schema gap: `study/LESSON-PRODUCTION-TRACKER.md` only exposes `Specification` and lacks a Markdown authoring status column; tracker left unmodified.

## 2026-09-11 - Topic 5 Lessons 5 and 6 Markdown authoring (9702_t05_cm02_l05 and 9702_t05_cm02_l06)

- Authored `lesson.md` and `lesson-build-evidence.json` for `9702_t05_cm02_l05` (Gravitational Potential Energy in a Uniform Field) covering learning outcomes `9702_t05_m02_o01` and `9702_t05_m02_o02`.
- Integrated byte-for-byte controlled definition `9702_def_gravitational_potential_energy` ("energy stored by a mass because of its position or height in a gravitational field") and controlled formula `9702_formula_gravitational_potential_energy` (\(\Delta E_P = mg\Delta h\)).
- Developed rigorous derivation from \(W = Fs\) and weight \(W_{\text{weight}} = mg\), proved path independence on inclined planes, explained the physical necessity of the uniform field condition (constant \(g\)), and detailed reference level conventions.
- Authored three original worked examples with examination mark schemes ([M1], [A1], [B1]) covering crane lifting power, inclined snowy slope with friction, and multi-stage path independence. Included two guided practice problems, four active A/B checks with dual-choice feedback, and five evidence-backed misconceptions.
- Authored `lesson.md` and `lesson-build-evidence.json` for `9702_t05_cm02_l06` (Kinetic Energy Derivation, Calculation and Application) covering learning outcomes `9702_t05_m02_o03` and `9702_t05_m02_o04`.
- Integrated byte-for-byte controlled definition `9702_def_kinetic_energy` ("energy that an object has because of its motion") and controlled formula `9702_formula_kinetic_energy` (\(E_K = \frac{1}{2}mv^2\)).
- Developed full seven-step derivation from Newton's second law \(F = ma\), work done \(W = Fs\), and the kinematic equation \(v^2 = u^2 + 2as\), yielding the work-energy theorem \(W = \Delta E_K\) and kinetic energy from rest \(E_K = \frac{1}{2}mv^2\).
- Detailed scalar nature, non-negative property, speed-squared relationship (\(E_K \propto v^2\)), non-relativistic condition (\(v \ll c\)), stopping distance scaling, and momentum connection (\(E_K = \frac{p^2}{2m}\)).
- Authored three original worked examples with examination mark schemes ([M1], [A1], [B1]) covering speed-squared work and braking distance, vertical dive potential-to-kinetic conversion with drag force, and kinetic energy/speed ratio scaling. Included two guided practice problems, four active A/B checks with dual-choice feedback, and five evidence-backed misconceptions.
- Verified strictly zero em dashes and zero en dashes across all authored Markdown and JSON files.
- Validated all JSON files using `python3 -m json.tool`.
- Ran `python3 scripts/taxonomy/validate_topic_curriculum.py --topics 9702_t05` passing 100% with 0 errors; ran `python3 scripts/validate_lesson_redirects.py` passing 100% with 0 errors.
- Reported tracker schema gap: `study/LESSON-PRODUCTION-TRACKER.md` only exposes `Specification` and lacks a Markdown authoring status column; tracker left unmodified.


## 2026-09-11 - Lessons 1 and 2 Markdown authoring (9702_t05_cm01_l01 and 9702_t05_cm01_l02)

- Authored `lesson.md` and `lesson-build-evidence.json` for `9702_t05_cm01_l01` (Understand the concept of work, W = Fs cos\theta, work done by expanding gas W = p\Delta V) covering outcomes `9702_t05_m01_o01` and `9702_t05_m01_o02`.
- Integrated byte-for-byte controlled definition `9702_def_work_done` ("product of force and displacement in the direction of the force") and controlled formulas `9702_formula_work` (W = Fs) and `9702_formula_work_done_gas_expansion` (W = p\Delta V).
- Developed mechanical energy transfer concepts, directional cosine resolution (positive, negative, and zero work), force-displacement graph areas, constant-pressure gas expansion and compression, and connection to energy conservation.
- Authored three original worked examples with authentic Cambridge mark schemes (M1, A1, B1), a scaffolded guided practice problem, four active learning checks with comprehensive feedback for both choices, five evidence-backed misconceptions, and a core recap.
- Authored `lesson.md` and `lesson-build-evidence.json` for `9702_t05_cm01_l02` (Conservation of energy, energy dissipation, efficiency = useful output / total input * 100%) covering outcomes `9702_t05_m01_o03` and `9702_t05_m01_o04`.
- Integrated controlled formula `9702_formula_efficiency` (\eta = useful energy output / total energy input = useful power output / total power input).
- Developed physical mechanisms of energy dissipation (friction, drag, electrical resistance, deformation), degraded thermal energy, decimal and percentage efficiency, power formulation, quantitative Sankey diagrams, and multi-stage system efficiency (\eta_overall = \eta_1 * \eta_2 * ...).
- Authored three original worked examples with authentic Cambridge mark schemes (M1, A1, B1), a guided practice problem, four active learning checks with complete feedback for both options, five evidence-backed misconceptions, and a core recap.
- Verified strictly zero em dashes and zero en dashes across all 4 authored Markdown and JSON files.
- Ran `python3 scripts/taxonomy/validate_topic_curriculum.py --topics 9702_t05` passing 100% with 0 errors; ran `python3 scripts/validate_lesson_redirects.py` passing 100% with 0 errors.
- Reported tracker schema gap: `study/LESSON-PRODUCTION-TRACKER.md` only exposes `Specification` and lacks a Markdown authoring status column; tracker left unmodified.

## 2026-09-01  -  External asset-folder consolidation

- Consolidated all Topic 5 prompt packages under `work-energy-power-prompt-work/prompts/` and merged both historical image roots into `images/`, retaining attempts, revisions, reports and compatibility symlinks.
- Verified 40 prompt-package files and 227 PNGs after the move; canonical Topic 5 records and prompt contents were unchanged.

## 2026-09-01  -  Lessons 8 to 10 verified page-image release

- Released 8, 8 and 9 external standalone 1024 x 1536 PNGs for Lessons 8, 9 and 10 in strict lesson order.
- Exactly three disjoint makers produced the initial passes; one fresh read-only verifier applied both original-detail release gates and passed all targeted primary-agent repairs.
- Preserved 42 attempts/revisions and three checksum-backed manifests; prompt packages and canonical Topic 5 records were unchanged.

## 2026-09-01  -  Lessons 5 to 7 notes-first prompt packages

- Created exactly four external Markdown deliverables each for `9702_t05_cm03_l05`, `9702_t05_cm03_l06`, and `9702_t05_cm04_l07`, totalling 23 density-controlled page prompts and 184 binary page checks.
- Verified complete notes-native coverage, controlled wording/formulas, arithmetic, signed changes, significant figures, units, reverse algebra, efficiency conditions, and adjacent-lesson boundaries through one fresh read-only verifier and author repair loops to clean pass.
- Recorded the missing Topic 5 structural map files as source gaps, resolved controlled records from subject registries, excluded all placeholder figures and assessment/evidence sources, and generated no images.

## 2026-09-01  -  Work, conservation and gravitational-energy prompt packages

- Created and independently verified four external notes-first prompt packages for `9702_t05_cm01_l01` through `9702_t05_cm02_l04`.
- Released 10, 8, 9 and 11 construction-grade page contracts after complete source, calculation, notation, density, exact-string and boundary checks.
- Ignored all placeholder figure planning, kept assessment/enrichment/evidence layers unopened, generated no images and changed no canonical curriculum records.

## 2026-09-01  -  Lessons 8 to 10 notes-first prompt packages

- Created 25 verified external construction-grade page prompts across the final three Topic 5 lessons, with exactly eight binary acceptance checks per page.
- Recorded the absent Topic 5 lesson/module structural records, resolved controlled content from canonical subject registries, and passed the mandated fresh-verifier repair and recheck cycle.
- Used no question-bank, mark-scheme, enrichment, evidence or placeholder-figure content and generated no images.
