import unittest
import tempfile
from pathlib import Path

import pymupdf

from mcq_converter import ANSWER_ROW_RE, display_mode, extract_question_text, metadata, render_figure


class McqTests(unittest.TestCase):
    def test_metadata(self) -> None:
        data = metadata(Path("9702_s25_qp_11.pdf"))
        self.assertEqual(data["paper_code"], "9702_s25_11")
        self.assertEqual(data["variant"], 11)

    def test_answer_row(self) -> None:
        match = ANSWER_ROW_RE.match("40 B 1")
        self.assertIsNotNone(match)
        self.assertEqual(match.group("answer"), "B")

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

    def test_display_mode_without_visual_is_text_options(self) -> None:
        self.assertEqual(display_mode(None, None, None), "text_options")

    def test_figure_render_has_white_border_and_visible_content(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "figure.png"
            document = pymupdf.open()
            page = document.new_page(width=200, height=200)
            page.draw_rect(pymupdf.Rect(50, 50, 150, 150), color=(0, 0, 0), width=4)
            render_figure(page, pymupdf.Rect(40, 40, 160, 160), output, dpi=72)
            rendered = pymupdf.Pixmap(output)
            self.assertEqual((rendered.width, rendered.height), (248, 248))
            self.assertEqual(rendered.pixel(0, 0), (255, 255, 255))
            self.assertNotEqual(rendered.pixel(74, 74), (255, 255, 255))
            document.close()


if __name__ == "__main__":
    unittest.main()
