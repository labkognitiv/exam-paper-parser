# Internal lesson-question reviewer

Local, non-canonical prototype for reviewing original Physics lesson questions.

- Browse module, lesson and question.
- Review MCQs and structured theory questions.
- Inspect mark scheme, hints, solution, walkthrough and past-paper inspiration.
- Save Pass or Flag decisions and notes in this prototype only.

Run:

```bash
python3 build_data.py
python3 server.py
```

Open `http://127.0.0.1:8771`.

The source question JSON files are read-only. Review state is stored in
`review-state.json`.
