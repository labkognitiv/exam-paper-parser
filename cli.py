from __future__ import annotations

import sys
from pathlib import Path

from . import markscheme_converter, mcq_converter, question_compactor


USAGE = """usage: paperscript {paper|markscheme} [options]

commands:
  paper       read PDFs from input/paper and write to output/paper
  markscheme  read PDFs from input/markscheme and write to output/markscheme
  mcq         read PDFs from input/mcq and write to output/mcq
"""


def main(argv: list[str] | None = None) -> int:
    arguments = list(sys.argv[1:] if argv is None else argv)
    if not arguments or arguments[0] in {"-h", "--help"}:
        print(USAGE)
        return 0

    command, *options = arguments
    if command == "paper":
        return question_compactor.main([
            "input/paper",
            "--output-dir",
            "output/paper",
            *options,
        ])
    if command == "markscheme":
        return markscheme_converter.main([
            "input/markscheme",
            "--output",
            "output/markscheme",
            *options,
        ])
    if command == "mcq":
        return mcq_converter.main([
            "input/mcq",
            "--output",
            "output/mcq",
            *options,
        ])

    print(f"error: unknown command: {command}\n\n{USAGE}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
