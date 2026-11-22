"""Test that the README "How it works" section has the heading and step keywords."""

from pathlib import Path

EXPECTED_HEADING = "## How it works"

# One keyword that must appear in each step of the "How it works" section.
STEP_KEYWORDS = [
    "filesystem",
    "network",
    ".dockerignore",
]


def _readme_text() -> str:
    return (Path(__file__).resolve().parent.parent / "README.md").read_text(
        encoding="utf-8"
    )


def test_readme_has_how_it_works_heading() -> None:
    assert EXPECTED_HEADING in _readme_text()


def test_readme_how_it_works_contains_step_keywords() -> None:
    text = _readme_text()
    section = text.split(EXPECTED_HEADING, 1)[1]
    # Only look inside the "How it works" section, up to the next heading.
    section = section.split("\n## ", 1)[0]
    for keyword in STEP_KEYWORDS:
        assert keyword in section, f"missing keyword {keyword!r} in How it works"