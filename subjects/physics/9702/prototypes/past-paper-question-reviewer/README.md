# Physics past-paper question reviewer

Local review prototype combining the question-player presentation with the
complete Physics 9702 P1 (MCQ), P2 (AS Theory) and P4 (A2 Theory) past-paper corpus.

- Browse all 4,016 canonical questions from 2016–2025 across P1, P2 and P4.
- Render canonical question text, LaTeX, diagram figures and full P1 MCQ images.
- Interactive P1 MCQ option selection with instant verification against official answer.
- Inspect hints, official marking schemes (marking points & criteria), and step-by-step walkthroughs.
- Integrated Physics Knowledge Base lookup for formal definitions and formulas.
- Record a local note and mark each question Pass or Flag.
- Surface missing, malformed or mismatched package data.

The current snapshot contains 2,760 P1, 476 P2 and 780 P4 questions. Twenty-eight
empty canonical P1 JSON records fall back to their question image, extracted text
and official answer key, and remain visibly flagged for verification.

Review state is saved to `review-state.json`; browser storage is only a fallback.
Run with `npm run dev` and open `http://localhost:3002`. Notes autosave as drafts
when leaving the field or navigating. The reviewer never changes canonical content.
Rebuild derived data with `python3 build_data.py`; verify with `npx tsc --noEmit`.
