"""Tracer core module."""


def _trace_filesystem(path: str) -> list:
    """Return a list of dummy file paths accessed during a build."""
    return [f"{path}/dummy_file_1", f"{path}/dummy_file_2"]


def trace_build(path: str) -> dict:
    """Trace build at path and return a dict with traced files."""
    return {"files": _trace_filesystem(path)}
