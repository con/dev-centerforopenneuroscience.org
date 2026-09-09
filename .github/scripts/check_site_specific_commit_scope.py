#!/usr/bin/env python3
"""Reject commits that mix subtree and parent-repository changes."""

from __future__ import annotations

import subprocess


def staged_paths() -> list[str]:
    output = subprocess.check_output(
        [
            "git",
            "diff",
            "--cached",
            "--name-only",
            "--no-renames",
            "--diff-filter=ACDMRTUXB",
            "-z",
        ]
    )
    return [
        path.decode("utf-8", "surrogateescape")
        for path in output.split(b"\0")
        if path
    ]


def main() -> int:
    paths = staged_paths()
    subtree = [
        path
        for path in paths
        if path == "site-specific" or path.startswith("site-specific/")
    ]
    parent = [path for path in paths if path not in subtree]

    if not subtree or not parent:
        return 0

    print("A commit cannot mix site-specific subtree and parent-repository changes.")
    print("Commit these groups separately:")
    print("\nsite-specific:")
    for path in subtree:
        print(f"  {path}")
    print("\nparent repository:")
    for path in parent:
        print(f"  {path}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
