import unittest
from unittest.mock import Mock

import pymupdf

from question_compactor import (
    detect_spatial_math,
    latexify_line,
    normalized,
    plain_from_latex,
    question_text,
)


class NormalizationTests(unittest.TestCase):
    def test_collapses_whitespace_and_nuls(self):
        self.assertEqual(normalized("  1\x00  (a)\nQuestion  "), "1 (a) Question")

    def test_scientific_value_stays_inline_with_units(self):
        self.assertEqual(
            latexify_line("speed is 4.9 × 10^{7} m s^{-1}."),
            "speed is $4.9 \\times 10^{7}\\,\\mathrm{m}\\,\\mathrm{s}^{-1}$.",
        )

    def test_scripted_variable_stays_inline(self):
        self.assertEqual(
            latexify_line(r"variation of V_{\mathrm{IN}} with t"),
            r"variation of $V_{\mathrm{IN}}$ with t",
        )

    def test_angle_expression_is_one_math_region(self):
        self.assertEqual(
            latexify_line("symbols m and 〈c^{2}〉."),
            r"symbols m and $\langle c^{2}\rangle$.",
        )

    def test_fraction_conversion_is_not_value_specific(self):
        self.assertEqual(
            latexify_line(r"x = ^{a+b}_{c-d}"),
            r"$x = \frac{a+b}{c-d}$",
        )

    def test_square_root_preserves_nested_expression(self):
        self.assertEqual(
            latexify_line(r"v = √(x_0^{2}-(x-y)^{2})"),
            r"$v = \sqrt{x_0^{2}-(x-y)^{2}}$",
        )

    def test_inline_equality_does_not_turn_prose_into_display_math(self):
        line = "(ii) The car is at rest at time t = 0 and moves at t = 5.8 s."
        self.assertEqual(latexify_line(line), line)

    def test_plain_text_does_not_flatten_letter_subscript(self):
        document = pymupdf.open()
        page = document.new_page()
        page.insert_text((50, 50), "E", fontsize=12)
        page.insert_text((58, 53), "K", fontsize=8)
        extracted = question_text(page)
        document.close()
        self.assertIn("E_{K}", extracted)

    def test_fraction_is_inferred_from_pdf_geometry(self):
        document = pymupdf.open()
        page = document.new_page()
        page.insert_text((45, 105), "E", fontsize=12)
        page.insert_text((53, 109), "K", fontsize=8)
        page.insert_text((60, 105), " =", fontsize=12)
        page.insert_text((90, 84), "a+b", fontsize=12)
        page.insert_text((92, 108), "c-d", fontsize=12)
        page.insert_text((121, 105), " mv", fontsize=12)
        page.insert_text((141, 99), "2", fontsize=8)
        page.draw_line((87, 91), (118, 91), width=0.5)
        detected = detect_spatial_math(page)
        document.close()
        self.assertTrue(any(r"\frac{a+b}{c-d}" in latex for _rect, latex in detected))
        self.assertTrue(any(r"E_{\mathrm{K}}" in latex for _rect, latex in detected))
        self.assertTrue(any(r"mv^{2}" in latex for _rect, latex in detected))

    def test_root_is_inferred_from_pdf_geometry(self):
        document = pymupdf.open()
        page = document.new_page()
        page.insert_text((50, 100), "v =", fontsize=12)
        page.insert_text((98, 100), "x+1", fontsize=12)
        shape = page.new_shape()
        shape.draw_polyline([(82, 96), (86, 102), (92, 80), (125, 80)])
        shape.finish(color=(0, 0, 0), width=0.7)
        shape.commit()
        detected = detect_spatial_math(page)
        document.close()
        self.assertTrue(any(r"\sqrt{x+1}" in latex for _rect, latex in detected))

    def test_plain_text_retains_structural_fraction_and_root(self):
        self.assertEqual(
            plain_from_latex(r"$E_{K}=\frac{a+b}{\sqrt{c^{2}}}$"),
            "E_{K}=(a+b)/(sqrt(c^{2}))",
        )


if __name__ == "__main__":
    unittest.main()
