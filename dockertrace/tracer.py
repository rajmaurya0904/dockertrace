"""Tracer core module."""


def _trace_filesystem(path: str) -> list:
    """Return a list of dummy file paths accessed during a build."""
    return [f"{path}/dummy_file_1", f"{path}/dummy_file_2"]


def _suggest_dockerignore(files: list) -> list:
    """Return a list of dockerignore suggestions derived from traced files."""
    return [f"!.{name}" for name in files]


def trace_build(path: str) -> dict:
    """Trace build at path and return a dict with files, hosts, and a dockerignore suggestion."""
    files = _trace_filesystem(path)
    return {
        "files": files,
        "hosts": ["localhost"],
        "dockerignore": _suggest_dockerignore(files),
    }
