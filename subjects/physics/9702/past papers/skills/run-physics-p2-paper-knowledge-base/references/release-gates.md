# Release gates

A paper is releasable only when:

1. preflight and final canonical inventories and hashes match;
2. every canonical question and mark-scheme pair validates;
3. every expected question and answerable leaf has enrichment;
4. controlled IDs resolve and question-level unions preserve first-occurrence order;
5. definitions, formulas, skills, hints, walkthroughs, checking rules, and official-criterion bindings pass semantic review;
6. official mark schemes remain byte-identical and canonical changes are separately authorized;
7. deterministic validation, JSON parsing, and diff checks pass;
8. derived data is rebuilt only from passing source records; and
9. the final report has zero unresolved defects or review items.

Schema validity alone never satisfies a release gate.
