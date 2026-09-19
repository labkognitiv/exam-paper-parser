#!/usr/bin/env python3
import argparse, csv, hashlib, json
from collections import Counter
from pathlib import Path

HEADER = ["question_id", "primary_skill_fit", "supporting_skill_fit", "rubric_fit", "registry_fit", "verdict", "notes"]

def read_csv(path):
    with path.open(newline="", encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    p = argparse.ArgumentParser()
    for name in ("questions", "assignments", "assignment-report", "skill-library", "review"):
        p.add_argument("--" + name, type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    errors = []
    _, questions = read_csv(a.questions)
    _, assignments = read_csv(a.assignments)
    _, library = read_csv(a.skill_library)
    review_header, review = read_csv(a.review)
    upstream = json.loads(a.assignment_report.read_text(encoding="utf-8"))
    if upstream.get("final_status") != "passed":
        errors.append("skills/rubric assignment validator is not passed")
    if review_header != HEADER:
        errors.append("review header does not match contract")
    qids = [r.get("question_id", "") for r in questions]
    aids = [r.get("question_id", "") for r in assignments]
    rids = [r.get("question_id", "") for r in review]
    if len(set(qids)) != len(qids): errors.append("duplicate question IDs")
    if set(aids) != set(qids) or len(aids) != len(qids): errors.append("assignment coverage mismatch")
    if set(rids) != set(qids) or len(rids) != len(qids): errors.append("QC coverage mismatch")
    approved = {r.get("skill_name") for r in library if r.get("status") == "approved"}
    for row in assignments:
        qid = row.get("question_id", "")
        try: tags = json.loads(row.get("skill_tags", ""))
        except Exception: tags = []
        for tag in tags:
            if tag not in approved: errors.append(f"{qid}: unregistered skill {tag!r}")
    for row in review:
        qid = row.get("question_id", "")
        for field in ("primary_skill_fit", "supporting_skill_fit", "rubric_fit", "registry_fit"):
            if row.get(field) not in {"yes", "no"}: errors.append(f"{qid}: invalid {field}")
        if row.get("verdict") not in {"passed", "failed", "needs_review"}: errors.append(f"{qid}: invalid verdict")
        if row.get("verdict") == "passed" and any(row.get(f) != "yes" for f in ("primary_skill_fit", "supporting_skill_fit", "rubric_fit", "registry_fit")):
            errors.append(f"{qid}: passed verdict conflicts with fit fields")
        if row.get("verdict") != "passed" and not row.get("notes", "").strip():
            errors.append(f"{qid}: non-passed row requires notes")
    verdicts = Counter(r.get("verdict") for r in review)
    if verdicts["failed"] or verdicts["needs_review"]:
        errors.append("every skills/rubric QC row must pass")
    out = {
        "schema_version": "physics_mcq_skills_rubric_qc_v1",
        "final_status": "passed" if not errors else "failed",
        "rows": len(review), "passed_rows": verdicts["passed"],
        "failed_rows": verdicts["failed"], "needs_review_rows": verdicts["needs_review"],
        "questions_sha256": sha(a.questions), "assignments_sha256": sha(a.assignments),
        "review_sha256": sha(a.review), "errors": errors,
    }
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())

