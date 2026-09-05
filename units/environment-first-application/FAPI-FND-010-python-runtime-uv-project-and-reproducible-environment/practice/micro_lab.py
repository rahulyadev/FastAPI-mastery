"""Observe the live environment without importing the learner challenge."""

import json
import platform
import sys
import tomllib
from argparse import ArgumentParser
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any

OBSERVED_DISTRIBUTIONS = ("fastapi", "pydantic", "uvicorn", "pytest")


def find_project_root(start: Path) -> Path:
    resolved = start.resolve()
    search_from = resolved if resolved.is_dir() else resolved.parent
    for candidate in (search_from, *search_from.parents):
        if (candidate / "pyproject.toml").is_file() and (candidate / "uv.lock").is_file():
            return candidate
    raise FileNotFoundError("project root with pyproject.toml and uv.lock not found")


def installed_version(name: str) -> str:
    try:
        return version(name)
    except PackageNotFoundError:
        return "not-installed"


def collect_evidence(project_root: Path) -> dict[str, Any]:
    project = tomllib.loads((project_root / "pyproject.toml").read_text(encoding="utf-8"))
    lock = tomllib.loads((project_root / "uv.lock").read_text(encoding="utf-8"))
    return {
        "project_root": str(project_root.resolve()),
        "python_request": (project_root / ".python-version").read_text(encoding="utf-8").strip(),
        "requires_python": project["project"]["requires-python"],
        "python_observed": platform.python_version(),
        "executable": str(Path(sys.executable)),
        "prefix": str(Path(sys.prefix)),
        "base_prefix": str(Path(sys.base_prefix)),
        "in_virtual_environment": sys.prefix != sys.base_prefix,
        "lock_schema": lock.get("version"),
        "lock_revision": lock.get("revision"),
        "locked_package_records": len(lock.get("package", [])),
        "declared_groups": sorted(project.get("dependency-groups", {})),
        "installed_distributions": {
            name: installed_version(name) for name in OBSERVED_DISTRIBUTIONS
        },
    }


def human_lines(evidence: dict[str, Any]) -> tuple[str, ...]:
    packages = evidence["installed_distributions"]
    return (
        "DECLARATION",
        f"  python request: {evidence['python_request']}",
        f"  compatibility: {evidence['requires_python']}",
        f"  dependency groups: {', '.join(evidence['declared_groups'])}",
        (
            f"  lock: schema={evidence['lock_schema']} "
            f"revision={evidence['lock_revision']} "
            f"records={evidence['locked_package_records']}"
        ),
        "RUNTIME EVIDENCE",
        f"  python observed: {evidence['python_observed']}",
        f"  executable: {evidence['executable']}",
        f"  prefix differs from base: {evidence['in_virtual_environment']}",
        "INSTALLED DISTRIBUTIONS",
        *(f"  {name}: {packages[name]}" for name in sorted(packages)),
    )


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--json", action="store_true", help="emit machine-readable evidence")
    args = parser.parse_args()

    evidence = collect_evidence(find_project_root(Path(__file__)))
    if args.json:
        print(json.dumps(evidence, indent=2, sort_keys=True))
        return
    print("\n".join(human_lines(evidence)))


if __name__ == "__main__":
    main()
