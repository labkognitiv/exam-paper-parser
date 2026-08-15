from __future__ import annotations

import sys
from pathlib import Path

from . import markscheme_converter, mcq_converter, question_compactor


USAGE = """usage: paperscript {paper|markscheme|mcq} [options]

commands:
  paper       read PDFs from input/physics/paper and write to output/physics/paper
  markscheme  read PDFs from input/physics/markscheme and write to output/physics/markscheme
  mcq         read PDFs from input/physics/mcq and write to output/physics/mcq
"""


def main(argv: list[str] | None = None) -> int:
    arguments = list(sys.argv[1:] if argv is None else argv)
    if not arguments or arguments[0] in {"-h", "--help"}:
        print(USAGE)
        return 0

    command, *options = arguments
    if command == "paper":
        return question_compactor.main([
            "input/physics/paper",
            "--output-dir",
            "output/physics/paper",
            *options,
        ])
    if command == "markscheme":
        return markscheme_converter.main([
            "input/physics/markscheme",
            "--output",
            "output/physics/markscheme",
            *options,
        ])
    if command == "mcq":
        return mcq_converter.main([
            "input/physics/mcq",
            "--output",
            "output/physics/mcq",
            *options,
        ])

    print(f"error: unknown command: {command}\n\n{USAGE}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
