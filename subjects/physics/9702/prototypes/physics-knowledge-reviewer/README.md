# Physics knowledge reviewer prototype

Build the embedded dataset after enrichment changes:

```bash
python3 subjects/physics/9702/prototypes/physics-knowledge-reviewer/build_data.py
```

Run from the repository root:

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000/subjects/physics/9702/prototypes/physics-knowledge-reviewer/`.

The prototype is read-only. It combines canonical question images and text, official mark-scheme criteria, enrichment hints and walkthroughs, controlled mappings, skills, definitions, formulas, and checking metadata.
