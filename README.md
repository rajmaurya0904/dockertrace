# dockertrace

**A diagnostic tool that traces container filesystem and network activity during Docker builds to generate minimal `.dockerignore` files and multi-stage configurations.**

Bloated build contexts cause slow Docker builds, pushing gigabytes of unnecessary source files, node_modules, and virtual environments to daemon sockets. Writing `.dockerignore` files manually is tedious, error-prone, and often leaves out hidden cache directories or build artifacts.

## Worked Example

Running `dockertrace` on a sample repository:

```bash
$ python -c "import dockertrace.tracer; print(dockertrace.tracer.trace_build('.'))"
{}
```

## Install

```bash
pip install -e ".[dev]"
```

## Usage

- `python -c "import dockertrace.tracer; print(dockertrace.tracer.trace_build('.'))"`: Run core build trace stub on target directory.

## How it works

During a Docker build the tool attaches to the build container and records every filesystem operation performed – reads, writes, and directory listings – building a precise map of which source files are actually used.

It also hooks into the container’s network stack, capturing outbound connections and DNS lookups to understand which external services the build depends on.

Finally, the collected traces are processed to generate a minimal `.dockerignore` file and optional multi‑stage Dockerfile suggestions that exclude unused files and isolate network‑dependent steps.

## Limitations

- Currently only provides a stub function (`trace_build`) returning an empty dictionary.
- Does not yet execute or intercept container build systems or kernel calls.

## Development

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```

## License

MIT -- see [LICENSE](LICENSE).
