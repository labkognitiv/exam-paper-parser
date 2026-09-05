# Mathematics prototypes

Follow [subject startup](../AGENTS.md), then read this layer's `SESSION-LOG.md`,
the selected prototype's `README.md` and its `handoff.md` when present.

Product lens: these interfaces help humans inspect whether Kognitiv's content
supports ordered study, meaningful attempts, trustworthy feedback and clear next
steps. They are review tools, not evidence that a learner-facing capability is
deployed, and their generated data must not become source truth.

## Purpose and context

Kognitiv's internal Cambridge pipeline connects official papers, controlled
knowledge and Study lesson packages through stable IDs. These prototypes are
local review interfaces, not canonical content or the public application.
This is the only AGENTS.md for the prototypes subtree. `SESSION-LOG.md` is its
only session log. Each active prototype may have one maintained `handoff.md` in
its own folder; do not create timestamped handoffs, nested logs or codex.md files.

## Two reviewers

- `topical-reviewer/`: P1, P3, M1 and S1 lesson PDFs and original practice
  questions, mark schemes and enrichment from `../study/`.
- `past-paper-reviewer/`: official question packages, mark schemes, assets and
  enrichment from `../past papers/`, browsed by component, year and paper.

The separate P1 scheduling experiment lives in `../planner/`. It shares the
read-only generated topical dataset but is not part of the topical interface.

## Preservation and verification

- Never mutate canonical papers, official mark schemes, enrichment, controlled
  knowledge, Study content or CSV evidence through a reviewer.
- Preserve each reviewer's `review-state.json` and browser storage keys. Review
  decisions and drafts are user work, not disposable generated data.
- `p1-data.js` and `paper-data.js` are derived datasets; rebuild them using their
  owning build_data.py after relevant source or path changes. Keep them available
  for the interfaces to run. The legacy p1-data.js name does not limit coverage
  to P1.
- Keep each interface's HTML, CSS, JavaScript, builder and server together.
  Validate changed paths and behavior without altering review verdicts.
- Generated output never replaces canonical sources or establishes correctness.
  Promote reusable code into maintained modules rather than making production
  depend on a prototype.
- Append material changes to this folder's SESSION-LOG.md; summarize major
  milestones in the Mathematics subject log.

## Context transfer

- When the user asks to transfer context, append one concise `YYYY-MM-DD` entry
  to this folder's `SESSION-LOG.md` and update the selected prototype's
  `handoff.md` in place. Never create a new handoff file for later sessions.
- Keep each handoff at 100 lines or fewer. Include current state, verified facts,
  unresolved work, exact next steps and a brief dated session summary.
- Keep source in its existing prototype folder. Preserve other prototypes,
  their saved state and unrelated handoff/log work.
