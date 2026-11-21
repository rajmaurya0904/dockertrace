"""Tests for tracer module."""

from dockertrace.tracer import trace_build


def test_trace_build() -> None:
    result = trace_build(".")
    assert isinstance(result, dict)
    assert result == {}
