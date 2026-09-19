#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path

REVIEW_KEYS = {
    "reviewer", "paper_code", "qp_identity", "ms_identity", "qp_complete",
    "answer_key_complete", "source_authority", "verdict", "notes"
}

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--paper-code", required=True)
    p.add_argument("--qp", type=Path, required=True)
    p.add_argument("--ms", type=Path, required=True)
    p.add_argument("--review", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    errors = []

    try:
        prefix, variant = a.paper_code.rsplit("_", 1)
    except ValueError:
        prefix = variant = ""
        errors.append("paper_code must end in a component/variant such as _12")
    expected_qp = f"{prefix}_qp_{variant}.pdf"
    expected_ms = f"{prefix}_ms_{variant}.pdf"

    for label, path, expected in (("QP", a.qp, expected_qp), ("MS", a.ms, expected_ms)):
        lower_parts = [x.lower() for x in path.parts]
        if any(x == "_archive" or "cutout" in x or "crop" in x for x in lower_parts):
            errors.append(f"{label}: archive/cutout/derivative source is forbidden")
        if not path.is_file():
            errors.append(f"{label}: file does not exist")
            continue
        if path.name.lower() != expected.lower():
            errors.append(f"{label}: expected filename {expected}")
        data = path.read_bytes()
        if not data.startswith(b"%PDF"):
            errors.append(f"{label}: file is not a PDF")
        if len(data) < 10_000:
            errors.append(f"{label}: PDF is unexpectedly small")

    try:
        review = json.loads(a.review.read_text(encoding="utf-8"))
    except Exception as exc:
        review = {}
        errors.append(f"source review is unreadable: {exc}")
    missing = REVIEW_KEYS - set(review)
    if missing:
        errors.append(f"source review missing keys: {sorted(missing)}")
    if review.get("paper_code") != a.paper_code:
        errors.append("source review paper_code mismatch")
    for key in ("qp_identity", "ms_identity", "qp_complete", "answer_key_complete", "verdict"):
        if review.get(key) != "passed":
            errors.append(f"source review {key} is not passed")
    if review.get("source_authority") != "original_official_pdfs":
        errors.append("source authority must be original_official_pdfs")
    if not str(review.get("reviewer", "")).strip():
        errors.append("source review requires a reviewer")

    out = {
        "schema_version": "physics_mcq_source_qc_v1",
        "final_status": "passed" if not errors else "failed",
        "paper_code": a.paper_code,
        "qp_path": str(a.qp),
        "ms_path": str(a.ms),
        "qp_sha256": sha256(a.qp) if a.qp.is_file() else None,
        "ms_sha256": sha256(a.ms) if a.ms.is_file() else None,
        "errors": errors,
    }
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())

