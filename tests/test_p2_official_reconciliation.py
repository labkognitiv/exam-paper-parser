import copy
import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "skills/repair-physics-p2-content/scripts/validate_pair.py"
QUESTION = ROOT / "output/physics/p2/questions/9702_w16_qp_22/question_02.json"
MARKSCHEME = ROOT / "output/physics/p2/mark-schemes/9702_w16_ms_22/markscheme_02.json"


class OfficialReconciliationValidationTests(unittest.TestCase):
    def validate(self, question):
        with tempfile.TemporaryDirectory(dir=QUESTION.parent) as directory:
            question_path = Path(directory) / "question.json"
            for figure in QUESTION.parent.glob("figure_*.png"):
                (Path(directory) / figure.name).symlink_to(figure)
            question_path.write_text(json.dumps(question))
            return subprocess.run(
                ["python3", str(VALIDATOR), str(question_path), str(MARKSCHEME)],
                text=True,
                capture_output=True,
                check=False,
            )

    def test_valid_occurrence_aware_contract_passes(self):
        result = self.validate(json.loads(QUESTION.read_text()))
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_missing_binding_cannot_hide_marks(self):
        question = json.loads(QUESTION.read_text())
        question["official_reconciliation"]["part_bindings"].pop()
        result = self.validate(question)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unconsumed official part occurrence", result.stdout)

    def test_official_occurrence_cannot_be_used_twice(self):
        question = json.loads(QUESTION.read_text())
        duplicate = copy.deepcopy(question["official_reconciliation"]["part_bindings"][0])
        duplicate["question_part_ids"] = ["9702_w16_22_q02_a"]
        question["official_reconciliation"]["part_bindings"].append(duplicate)
        result = self.validate(question)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("official part occurrence used more than once", result.stdout)


if __name__ == "__main__":
    unittest.main()
