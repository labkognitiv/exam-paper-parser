from pathlib import Path
import unittest

from markscheme_converter import clean, paper_output_name, question_json


class MarkSchemeTests(unittest.TestCase):
    def test_paper_output_name(self) -> None:
        self.assertEqual(paper_output_name(Path("9702_s25_ms_22.pdf")), "9702_s25_ms_22")

    def test_symbol_cleanup(self) -> None:
        self.assertEqual(clean("F \uf0b4 s  \uf0b1 3"), "F × s ± 3")

    def test_json_groups_continued_rows_and_alternatives(self) -> None:
        data = question_json(
            Path("9702_s25_ms_22.pdf"),
            1,
            [
                "1(a) first point    B1",
                "second point    B1",
                "1(b)(i) method    M1",
                "OR alternative method    (M1)",
                "answer    A1",
            ],
        )
        self.assertEqual(data["question_id"], "9702_s25_22_q01")
        self.assertEqual(data["total_marks"], 4)
        self.assertEqual(data["parts"][0]["id"], "9702_s25_22_q01_a")
        self.assertEqual(len(data["parts"][0]["marking_points"]), 2)
        self.assertTrue(data["parts"][1]["marking_points"][1]["is_alternative"])


if __name__ == "__main__":
    unittest.main()
