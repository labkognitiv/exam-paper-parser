import subprocess
import unittest


class CliTests(unittest.TestCase):
    def test_help_lists_both_commands(self) -> None:
        result = subprocess.run(
            [".venv/bin/paperscript", "--help"],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("paper", result.stdout)
        self.assertIn("markscheme", result.stdout)
        self.assertIn("syllabus", result.stdout)


if __name__ == "__main__":
    unittest.main()
