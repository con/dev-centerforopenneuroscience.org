#!/usr/bin/env python3
"""Build one Netlify preview with explicit unreleased candidates."""

from __future__ import annotations

import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib


SHA = re.compile(r"[0-9a-f]{40}")
ROOT = Path.cwd()
SELECTOR = ROOT / ".orinoco-lite" / "candidate-preview.toml"


def check_out(name: str, value: object, temporary: Path) -> Path:
    if not isinstance(value, dict):
        raise SystemExit(f"candidate {name} must be a TOML table")
    repository, commit = value.get("repository"), value.get("commit")
    if not isinstance(repository, str) or not re.fullmatch(
        r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository
    ):
        raise SystemExit(f"candidate {name}.repository must use OWNER/REPOSITORY form")
    if not isinstance(commit, str) or SHA.fullmatch(commit) is None:
        raise SystemExit(f"candidate {name}.commit must be a full lowercase Git SHA")
    destination = temporary / name
    subprocess.run(
        ("git", "clone", f"https://github.com/{repository}.git", str(destination)),
        check=True,
    )
    subprocess.run(
        ("git", "-C", str(destination), "fetch", "--depth", "1", "origin", commit),
        check=True,
    )
    subprocess.run(
        ("git", "-C", str(destination), "checkout", "--detach", commit),
        check=True,
    )
    return destination


def main() -> int:
    selector = tomllib.loads(SELECTOR.read_text(encoding="utf-8"))
    if selector.get("version") != 1:
        raise SystemExit("candidate-preview.toml version must be 1")
    repository = selector.get("downstream_repository")
    if not isinstance(repository, str) or not re.fullmatch(
        r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository
    ):
        raise SystemExit("candidate-preview.toml downstream_repository is invalid")
    source_commit = os.environ.get("COMMIT_REF", "")
    if SHA.fullmatch(source_commit) is None:
        raise SystemExit("Netlify COMMIT_REF must be a full lowercase Git SHA")
    pull_request = os.environ.get("REVIEW_ID", "")
    if not pull_request.isdigit() or int(pull_request) < 1:
        raise SystemExit("Netlify REVIEW_ID must be a positive pull-request number")
    with tempfile.TemporaryDirectory(prefix="orinoco-netlify-candidate-") as temporary_text:
        temporary = Path(temporary_text)
        package = check_out("package", selector.get("package"), temporary)
        template = check_out("template", selector.get("template"), temporary)
        subprocess.run(
            (
                "git", "-C", str(package), "submodule", "update", "--init",
                "--recursive", "--", "submodules/pool.psychoinformatics.de-ui",
                "submodules/things-schemas",
            ),
            check=True,
        )
        pixi = shutil.which("pixi")
        if pixi is None:
            raise SystemExit("Pixi is unavailable")
        subprocess.run(
            (
                pixi, "run", "--frozen", "--manifest-path", str(package / "pixi.toml"),
                "python", str(package / "tools" / "downstream_development.py"),
                "--downstream", str(ROOT), "--package", str(package),
                "--template", str(template),
                "--repository", repository,
                "--source-commit", source_commit, "--pull-request", pull_request,
                "--task", "build", "--output",
                str(temporary / "output"),
            ),
            check=True,
        )
        source = temporary / "output" / "downstream" / "build" / "site"
        destination = ROOT / "build" / "site"
        shutil.rmtree(destination, ignore_errors=True)
        shutil.copytree(source, destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
