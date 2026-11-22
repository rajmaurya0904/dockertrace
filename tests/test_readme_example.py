"""Test that the README includes the Worked Example heading and sample command."""

from pathlib import Path

EXPECTED_HEADING = "## Worked Example"
EXPECTED_COMMAND = (
    "python -c \"import dockertrace.tracer; "
    "print(dockertrace.tracer.trace_build('.'))\""
)


def test_readme_has_worked_example_heading() -> None:
    readme = (Path(__file__).resolve().parent.parent / "README.md").read_text(
        encoding="utf-8"
    )
    assert EXPECTED_HEADING in readme


def test_readme_has_sample_command() -> None:
    readme = (Path(__file__).resolve().parent.parent / "README.md").read_text(
        encoding="utf-8"
    )
    assert EXPECTED_COMMAND in readme