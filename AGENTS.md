# Repository Agent Instructions

## Working state

- Preserve unrelated changes in this shared, heavily modified worktree. Never reset or broadly clean it.
- Physics 9702 P1 and P2 source processing covers 2016-2025.
- P1 outputs use one complete MCQ PNG, TXT, JSON and official answer value per question. Do not create separate P1 diagram crops.
- P2 canonical question/mark-scheme pairs have completed the current repair sweep. The occurrence-aware `official_reconciliation` contract handles immutable-source identity exceptions.
- Official mark-scheme JSON is immutable. Preserve it byte-for-byte.
- Keep `numerical_values_checked: false` unless a separately authorized numerical-review stage changes it.

## Current phase: taxonomy and knowledge-base design

- Treat the official syllabus as the controlled curriculum spine and past-paper questions as the assessment evidence.
- P1 and P2 share one AS Physics topic/learning-pathway taxonomy, while retaining component-specific assessment metadata.
- Do not duplicate canonical question packages into topic folders. Use stable IDs and additive mappings/indexes.
- Preserve whole structured P2 questions and their dependency graph. Allow topic/skill tags at question and leaf-part grain without breaking contextual relationships.
- Prefer one durable enrichment pass per question/part. Store reusable normalized facts so later modules, lessons, revision, retrieval and question generation do not reread the whole corpus.
- Keep extraction, taxonomy, enrichment, generated learning content and student-state data as separate layers.
- Do not build a vector database until controlled IDs, document grain, metadata and canonical enrichment records are stable; embeddings are a derived index, not the source of truth.
- Brainstorm incrementally with precise, strict bullets. Do not present a large final architecture unless the user asks for it.
