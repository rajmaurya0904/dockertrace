"""Tests for tracer module."""

from dockertrace.tracer import _trace_filesystem, trace_build


def test_trace_filesystem_returns_list() -> None:
    result = _trace_filesystem("/build")
    assert isinstance(result, list)
    assert all(isinstance(item, str) for item in result)


def test_trace_build_includes_files_key() -> None:
    result = trace_build(".")
    assert isinstance(result, dict)
    assert "files" in result
    assert isinstance(result["files"], list)