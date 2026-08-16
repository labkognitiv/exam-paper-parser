from pathlib import Path
import unittest

from markscheme_converter import (
    clean,
    extract_questions,
    extract_table_stream_questions,
    paper_output_name,
    question_json,
    repair_merged_page_number_word,
)


class MarkSchemeTests(unittest.TestCase):
    def test_paper_output_name(self) -> None:
        self.assertEqual(paper_output_name(Path("9702_s25_ms_22.pdf")), "9702_s25_ms_22")

    def test_symbol_cleanup(self) -> None:
        self.assertEqual(clean("F \uf0b4 s  \uf0b1 3"), "F × s ± 3")

    def test_page_number_merged_with_answer_word_is_not_a_question(self) -> None:
        self.assertEqual(
            repair_merged_page_number_word("7(resultant) displacement is sum", 4),
            "(resultant) displacement is sum",
        )
        self.assertEqual(
            repair_merged_page_number_word("5(a) valid next question", 4),
            "5(a) valid next question",
        )

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

    def test_numbered_subpart_is_preserved(self) -> None:
        data = question_json(
            Path("9702_s18_ms_23.pdf"),
            6,
            ["6(b)(ii)1 current in resistor = 0.40 A    C1"],
        )
        self.assertEqual(data["parts"][0]["id"], "9702_s18_23_q06_b_ii_1")

    def test_2018_landscape_table_stream(self) -> None:
        pdf = Path("input/physics/p2/mark-schemes/9702_s18_ms_23.pdf")
        if not pdf.exists():
            self.skipTest("local Cambridge fixture is not installed")
        questions = extract_table_stream_questions(pdf)
        self.assertEqual(sorted(questions), list(range(1, 8)))

    def test_2021_page_number_is_not_a_seventh_question(self) -> None:
        pdf = Path("input/physics/p2/mark-schemes/9702_s21_ms_23.pdf")
        if not pdf.exists():
            self.skipTest("local Cambridge fixture is not installed")
        self.assertEqual(sorted(extract_questions(pdf)), list(range(1, 7)))


if __name__ == "__main__":
    unittest.main()
