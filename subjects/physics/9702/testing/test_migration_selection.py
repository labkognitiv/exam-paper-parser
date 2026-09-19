import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_migration_selection.py"
SPEC = importlib.util.spec_from_file_location("validate_migration_selection", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PartIdResolutionTests(unittest.TestCase):
    def test_exact(self):
        source = "9702_s17_21_q07_a_i"
        self.assertEqual(MODULE.resolve_part_ids(source, {source}), ("exact", [source]))

    def test_unique_underscore_translation(self):
        source = "9702_m20_42_q03_a_i"
        target = "9702_m20_42_q03_ai"
        self.assertEqual(MODULE.resolve_part_ids(source, {target}), ("translated", [target]))

    def test_explicit_one_to_many(self):
        source = "9702_m20_22_q04_b_i"
        targets = ["9702_m20_22_q04_bi1", "9702_m20_22_q04_bi2"]
        self.assertEqual(
            MODULE.resolve_part_ids(source, set(targets), {source: targets}),
            ("explicit", targets),
        )

    def test_explicit_cross_question_is_rejected(self):
        source = "9702_m20_22_q04_b_i"
        target = "9702_m20_22_q05_bi"
        self.assertEqual(
            MODULE.resolve_part_ids(source, {target}, {source: [target]}),
            ("invalid_explicit", []),
        )

    def test_ambiguous_normalized_translation_is_rejected(self):
        source = "9702_m20_42_q03_a_i"
        targets = {"9702_m20_42_q03_ai", "9702_m20_42_q03_a_i"}
        targets.remove(source)
        targets.add("9702_m20_42_q03_a__i")
        self.assertEqual(MODULE.resolve_part_ids(source, targets), ("ambiguous", []))


if __name__ == "__main__":
    unittest.main()
