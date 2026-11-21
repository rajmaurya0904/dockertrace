"""Test that the README opening paragraph matches the expected text."""

from pathlib import Path

EXPECTED_OPENING = (
    "**A diagnostic tool that traces container filesystem and network "
    "activity during Docker builds to generate minimal `.dockerignore` "
    "files and multi-stage configurations.**"
)


def test_readme_opening_paragraph() -> None:
    readme = (Path(__file__).resolve().parent.parent / "README.md").read_text(
        encoding="utf-8"
    )
    assert EXPECTED_OPENING in readme