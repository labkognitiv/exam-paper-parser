# Physics 9702: Kinematics lesson previews

Three complete HTML lessons with shared styling, local fonts, KaTeX, diagrams, two A/B check-ins per lesson and a shared revision-gem collection. Teacher-voice edition, 7 September 2026.

## Run

From this directory, run:

```sh
python3 -m http.server 8788
```

Open http://localhost:8788/ and choose a lesson. Keep the server running. Use HTTP rather than double-clicking HTML because the gem catalogs load with fetch.

No Node install, build step or API key is required. Keep all folders together. Collection state is saved only in the current browser and origin; no student data is included. Lesson 1 introduces five gems, Lesson 2 introduces two, Lesson 3 introduces none. Remove controls let you retry collecting.

## Edit

- `kinematics-lesson-{1,2,3}/index.html`: lesson copy and structure.
- `lesson-assets/lesson.css`: shared lesson design.
- `lesson-assets/revision.css` and `revision.js`: cards, check-ins and collection.
- Each lesson's `assets/gems.json`: only its first-introduction definitions/formulas.
- Each lesson's `tools/`: optional diagram generators; see requirements.txt. Figures are already generated.

All runtime assets are local. Font license files are in lesson-assets/fonts. KaTeX licensing is recorded in THIRD-PARTY-NOTICES.md. These are teaching previews, not a complete course or canonical question bank. Lesson 4 is outside this bundle. Historical screenshots/backups and Gemini's comparison version are excluded.

Validation: local HTML/CSS asset references resolve; original exact definition/formula records preserved; earlier desktop/mobile review and cross-lesson collection checks passed. Print pagination and learner outcomes have not been validated.
