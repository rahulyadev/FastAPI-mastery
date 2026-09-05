"""Trace project declarations into observations made by the running process."""

import platform
import sys
import tomllib
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path


def find_project_root(start: Path) -> Path:
    """Find the nearest ancestor containing both project and lock metadata."""
    resolved = start.resolve()
    search_from = resolved if resolved.is_dir() else resolved.parent
    for candidate in (search_from, *search_from.parents):
        if (candidate / "pyproject.toml").is_file() and (candidate / "uv.lock").is_file():
            return candidate
    raise FileNotFoundError("could not find a project root containing pyproject.toml and uv.lock")


def distribution_version(name: str) -> str:
    try:
        return version(name)
    except PackageNotFoundError:
        return "not-installed"


def trace_lines(project_root: Path) -> tuple[str, ...]:
    project = tomllib.loads((project_root / "pyproject.toml").read_text(encoding="utf-8"))
    lock = tomllib.loads((project_root / "uv.lock").read_text(encoding="utf-8"))
    requested = (project_root / ".python-version").read_text(encoding="utf-8").strip()
    groups = ", ".join(sorted(project.get("dependency-groups", {})))

    return (
        f"1 selection [uv] .python-version={requested}",
        f"2 compatibility [packaging] requires-python={project['project']['requires-python']}",
        (
            "3 resolution [uv] "
            f"lock-schema={lock.get('version', 'unknown')} "
            f"revision={lock.get('revision', 'unknown')} "
            f"packages={len(lock.get('package', []))}"
        ),
        f"4 installation [Python venv] isolated={sys.prefix != sys.base_prefix}",
        f"5 execution [Python] version={platform.python_version()}",
        f"6 execution [Python] executable={Path(sys.executable)}",
        f"7 groups [project policy] declared={groups}",
        f"8 installed metadata [Python] fastapi={distribution_version('fastapi')}",
    )


def main() -> None:
    root = find_project_root(Path(__file__))
    print(f"project-root={root}")
    for line in trace_lines(root):
        print(line)


if __name__ == "__main__":
    main()
