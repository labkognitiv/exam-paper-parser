import unittest
from unittest.mock import Mock

from question_compactor import normalized


class NormalizationTests(unittest.TestCase):
    def test_collapses_whitespace_and_nuls(self):
        self.assertEqual(normalized("  1\x00  (a)\nQuestion  "), "1 (a) Question")


if __name__ == "__main__":
    unittest.main()
