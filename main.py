#!/usr/bin/env python3
"""Entry for make.fun news-image-20261117.

Writes the front-page image summing up Tuesday 17 November 2026's
world news to /output/entry.png. The image is bundled in this repo as
entry.png; this program copies it verbatim, so both runs produce
byte-identical output. Standard library only, no network.
"""
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def check_source() -> None:
    """Fail loudly if the bundled image is not a whole PNG."""
    with open(SOURCE, "rb") as handle:
        if handle.read(len(PNG_SIGNATURE)) != PNG_SIGNATURE:
            raise ValueError("entry.png is not a PNG file")


def output_path() -> Path:
    env = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_PATH")
    if env:
        return Path(env) / "entry.png"
    if len(sys.argv) > 1:
        return Path(sys.argv[1])
    return Path("/output/entry.png")


def main() -> None:
    check_source()
    dest = output_path()
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, dest)


if __name__ == "__main__":
    main()
