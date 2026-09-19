import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from export_website_package import Package, LinkParser, strip_registry_links, normalize_question_parts, SUBJECT, read_json


class WebsiteExportTests(unittest.TestCase):
    def test_markscheme_uses_full_id_not_legacy_short_part_id(self):
        with tempfile.TemporaryDirectory() as temp:
            package = Package(Path(temp))
            qid = "9702_w18_22_q05"
            question = {"question_id": qid, "parts": [{"id": qid + "_a"}]}
            rows = [{"id": qid + "_a", "part_id": "a", "marks": 3}]
            linked = package.linked_parts(rows, question, "markscheme")
            self.assertEqual(linked[0]["question_part_ids"], [qid + "_a"])
            self.assertEqual(linked[0]["marks"], 3)

    def test_combined_marking_row_is_not_duplicated(self):
        with tempfile.TemporaryDirectory() as temp:
            package = Package(Path(temp))
            qid = "9702_s19_22_q05"
            question = {"question_id": qid, "parts": [{"id": qid + "_bi1"}, {"id": qid + "_bi2"}]}
            linked = package.linked_parts([{"id": qid + "_b_i", "marks": 2}], question, "markscheme")
            self.assertEqual(len(linked), 1)
            self.assertEqual(linked[0]["question_part_ids"], [qid + "_bi1", qid + "_bi2"])
            self.assertEqual(linked[0]["marks"], 2)

    def test_repeated_ocr_ids_join_to_distinct_scored_parts(self):
        with tempfile.TemporaryDirectory() as temp:
            package = Package(Path(temp))
            for number in ("02", "06"):
                folder = SUBJECT / "past papers/p2/2019/may-june/variant-3" / ("question_" + number)
                original = read_json(folder / "question_ocr.json")
                question = normalize_question_parts(original)
                ids = [p["id"] for p in question["parts"]]
                self.assertEqual(len(ids), len(set(ids)))
                self.assertEqual(sum(p["marks"] for p in question["parts"]), original["total_marks"])
                linked = package.linked_parts(read_json(folder / "markscheme.json")["parts"], question, "markscheme")
                for row in linked:
                    self.assertEqual(row["marks"], sum(p["marks"] for p in question["parts"] if p["id"] in row["question_part_ids"]))

    def test_skip_libraries_preserves_instructional_formula_text(self):
        source = {"formula_ids": ["9702_formula_force"], "hints": ["Use F = ma."], "definition_ids": ["9702_def_mass"]}
        self.assertEqual(strip_registry_links(source), {"hints": ["Use F = ma."]})

    def test_html_copies_are_independent_and_have_local_dependencies(self):
        with tempfile.TemporaryDirectory() as temp:
            package = Package(Path(temp))
            copies = []
            for lid in ["9702_t01_cm01_l01", "9702_t25_cm03_l06"]:
                directory = Path("study") / lid
                page, assets = package.html_lesson({"id": lid, "title": "Test title"}, directory)
                html_path = Path(temp) / page
                self.assertFalse(html_path.is_symlink())
                self.assertIn(f'data-lesson-id="{lid}"', html_path.read_text())
                self.assertIn("Test content.", html_path.read_text())
                parser = LinkParser()
                parser.feed(html_path.read_text())
                self.assertTrue(all((html_path.parent / url).is_file() for url in parser.assets))
                self.assertTrue(all((Path(temp) / asset).is_file() for asset in assets))
                copies.append((html_path, Path(temp) / assets[0]))
            self.assertNotEqual(copies[0][0].stat().st_ino, copies[1][0].stat().st_ino)
            self.assertNotEqual(copies[0][1].stat().st_ino, copies[1][1].stat().st_ino)


if __name__ == "__main__":
    unittest.main()
