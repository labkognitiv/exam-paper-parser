import tempfile
import unittest
from pathlib import Path

import pymupdf

from syllabus_converter import convert_pdf


class SyllabusConverterTests(unittest.TestCase):
    def test_page_markers_and_repeated_furniture_removal(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "physics-syllabus.pdf"
            document = pymupdf.open()
            for number in (1, 2):
                page = document.new_page()
                page.insert_text((40, 35), "Cambridge International AS & A Level Physics 9702 syllabus for 2028, 2029 and 2030.")
                page.insert_text((40, 100), f"{number} Subject content")
                page.insert_text((40, 130), "Candidates should be able to:")
                page.insert_text((40, 160), "1. recall and use a physical relationship")
                page.insert_text((40, 810), str(number))
            document.save(source)
            document.close()

            output = convert_pdf(source, root / "output")
            text = output.read_text(encoding="utf-8")

            self.assertIn("--- Page 1 ---", text)
            self.assertIn("--- Page 2 ---", text)
            self.assertIn("Candidates should be able to:", text)
            self.assertNotIn("Cambridge International AS & A Level Physics 9702 syllabus", text)


if __name__ == "__main__":
    unittest.main()
