"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import dockertrace


def test_version_is_set() -> None:
    assert dockertrace.__version__
