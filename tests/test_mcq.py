import unittest
from pathlib import Path

from mcq_converter import ANSWER_ROW_RE, extract_question_text, extract_split_answer_rows, metadata


class McqTests(unittest.TestCase):
    def test_metadata(self) -> None:
        data = metadata(Path("9702_s25_qp_11.pdf"))
        self.assertEqual(data["paper_code"], "9702_s25_11")
        self.assertEqual(data["variant"], 11)

    def test_answer_row(self) -> None:
        match = ANSWER_ROW_RE.match("40 B 1")
        self.assertIsNotNone(match)
        self.assertEqual(match.group("answer"), "B")

    def test_legacy_split_answer_rows_in_two_columns(self) -> None:
        lines = ["Question", "Number", "Key"]
        for number in range(1, 21):
            lines.extend((str(number), "ABCD"[(number - 1) % 4]))
            lines.extend((str(number + 20), "DCBA"[(number - 1) % 4]))
        answers = extract_split_answer_rows(lines)
        self.assertEqual(len(answers), 40)
        self.assertEqual(answers[1], {"answer": "A", "marks": 1})
        self.assertEqual(answers[40], {"answer": "A", "marks": 1})

    def test_legacy_two_column_rows_on_same_line(self) -> None:
        lines = [f"{number} A {number + 20} D" for number in range(1, 21)]
        answers = extract_split_answer_rows(lines)
        self.assertEqual(len(answers), 40)
        self.assertEqual(answers[1]["answer"], "A")
        self.assertEqual(answers[40]["answer"], "D")

    def test_markscheme_metadata_matches_question_code(self) -> None:
        data = metadata(Path("9702_s25_ms_11.pdf"))
        self.assertEqual(data["paper_code"], "9702_s25_11")

    def test_extract_question_text_preserves_lines(self) -> None:
        class FakePage:
            def get_text(self, kind, clip, sort):
                self.call = (kind, clip, sort)
                return {
                    "blocks": [
                        {
                            "lines": [
                                {"spans": [{"text": "1  What is "}, {"text": "X?"}]},
                                {"spans": [{"text": "A  first option"}]},
                                {"spans": [{"text": "   "}]},
                            ]
                        }
                    ]
                }

        page = FakePage()
        result = extract_question_text(page, "clip")
        self.assertEqual(result, "1  What is X?\nA  first option")
        self.assertEqual(page.call, ("dict", "clip", True))


if __name__ == "__main__":
    unittest.main()
