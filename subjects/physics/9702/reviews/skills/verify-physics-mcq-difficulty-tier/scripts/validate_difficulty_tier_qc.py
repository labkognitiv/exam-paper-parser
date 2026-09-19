#!/usr/bin/env python3
import argparse, csv, hashlib, json
from collections import Counter
from pathlib import Path

HEADER = ["question_id", "difficulty_fit", "tier_fit", "reason_fit", "independent_difficulty", "independent_practice_tier", "verdict", "notes"]

def read_csv(path):
    with path.open(newline="", encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    p = argparse.ArgumentParser()
    for name in ("questions", "skills-qc", "assignments", "assignment-report", "review"):
        p.add_argument("--" + name, type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    errors = []
    _, questions = read_csv(a.questions)
    _, assignments = read_csv(a.assignments)
    review_header, review = read_csv(a.review)
    if json.loads(a.skills_qc.read_text()).get("final_status") != "passed": errors.append("skills/rubric QC is not passed")
    if json.loads(a.assignment_report.read_text()).get("final_status") != "passed": errors.append("difficulty/tier assignment validator is not passed")
    if review_header != HEADER: errors.append("review header does not match contract")
    qids = [r.get("question_id", "") for r in questions]
    aids = [r.get("question_id", "") for r in assignments]
    rids = [r.get("question_id", "") for r in review]
    if set(aids) != set(qids) or len(aids) != len(qids): errors.append("assignment coverage mismatch")
    if set(rids) != set(qids) or len(rids) != len(qids): errors.append("QC coverage mismatch")
    assigned = {r.get("question_id"): r for r in assignments}
    for row in review:
        qid = row.get("question_id", "")
        if row.get("difficulty_fit") not in {"yes", "no"}: errors.append(f"{qid}: invalid difficulty_fit")
        if row.get("tier_fit") not in {"yes", "no"}: errors.append(f"{qid}: invalid tier_fit")
        if row.get("reason_fit") not in {"yes", "no"}: errors.append(f"{qid}: invalid reason_fit")
        if row.get("independent_difficulty") not in {"easy", "medium", "hard"}: errors.append(f"{qid}: invalid independent_difficulty")
        if row.get("independent_practice_tier") not in {"mandatory", "revision"}: errors.append(f"{qid}: invalid independent_practice_tier")
        if row.get("verdict") not in {"passed", "failed", "needs_review"}: errors.append(f"{qid}: invalid verdict")
        source = assigned.get(qid, {})
        agrees = row.get("independent_difficulty") == source.get("difficulty") and row.get("independent_practice_tier") == source.get("practice_tier")
        if row.get("verdict") == "passed" and (not agrees or any(row.get(f) != "yes" for f in ("difficulty_fit", "tier_fit", "reason_fit"))):
            errors.append(f"{qid}: passed verdict conflicts with independent review")
        if row.get("verdict") != "passed" and not row.get("notes", "").strip(): errors.append(f"{qid}: non-passed row requires notes")
    verdicts = Counter(r.get("verdict") for r in review)
    tiers = Counter(r.get("independent_practice_tier") for r in review)
    expected = round(len(review) * 0.60)
    if tiers["mandatory"] != expected or tiers["revision"] != len(review) - expected:
        errors.append(f"independent tier split must be {expected} mandatory and {len(review)-expected} revision")
    if verdicts["failed"] or verdicts["needs_review"]: errors.append("every difficulty/tier QC row must pass")
    out = {
        "schema_version": "physics_mcq_difficulty_tier_qc_v1",
        "final_status": "passed" if not errors else "failed", "rows": len(review),
        "passed_rows": verdicts["passed"], "failed_rows": verdicts["failed"],
        "needs_review_rows": verdicts["needs_review"], "practice_tier": dict(tiers),
        "questions_sha256": sha(a.questions), "assignments_sha256": sha(a.assignments),
        "review_sha256": sha(a.review), "errors": errors,
    }
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())

