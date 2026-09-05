"""Run a read-only environment preflight suitable for a backend repository."""

import platform
import re
import sys
import tomllib
from dataclasses import dataclass
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path


@dataclass(frozen=True)
class Check:
    name: str
    passed: bool
    detail: str


def find_project_root(start: Path) -> Path:
    resolved = start.resolve()
    search_from = resolved if resolved.is_dir() else resolved.parent
    for candidate in (search_from, *search_from.parents):
        if (candidate / "pyproject.toml").is_file() and (candidate / "uv.lock").is_file():
            return candidate
    raise FileNotFoundError("project root not found")


def normalize_distribution(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def exact_pins(requirements: list[str]) -> tuple[tuple[str, str], ...]:
    """Extract only simple exact pins; ranges remain compatibility declarations."""
    pins: list[tuple[str, str]] = []
    for requirement in requirements:
        before_marker = requirement.split(";", maxsplit=1)[0].strip()
        if "==" not in before_marker:
            continue
        name, expected = before_marker.split("==", maxsplit=1)
        if "[" in name:
            name = name.split("[", maxsplit=1)[0]
        pins.append((normalize_distribution(name.strip()), expected.strip()))
    return tuple(sorted(pins))


def installed_version(distribution: str) -> str | None:
    try:
        return version(distribution)
    except PackageNotFoundError:
        return None


def run_preflight(project_root: Path) -> tuple[Check, ...]:
    project = tomllib.loads((project_root / "pyproject.toml").read_text(encoding="utf-8"))
    requested = (project_root / ".python-version").read_text(encoding="utf-8").strip()
    declared = project["project"]
    dev_requirements = project.get("dependency-groups", {}).get("dev", [])
    pins = exact_pins([*declared["dependencies"], *dev_requirements])

    checks = [
        Check(
            "python-selection",
            platform.python_version() == requested,
            f"requested={requested} observed={platform.python_version()}",
        ),
        Check(
            "virtual-environment",
            sys.prefix != sys.base_prefix and Path(sys.executable).is_relative_to(Path(sys.prefix)),
            (
                f"executable={Path(sys.executable)} "
                f"prefix={Path(sys.prefix)} base={Path(sys.base_prefix)}"
            ),
        ),
        Check(
            "lock-present",
            (project_root / "uv.lock").is_file(),
            str(project_root / "uv.lock"),
        ),
    ]

    for distribution, expected in pins:
        observed = installed_version(distribution)
        checks.append(
            Check(
                f"package:{distribution}",
                observed == expected,
                f"expected={expected} observed={observed or 'not-installed'}",
            )
        )
    return tuple(checks)


def main() -> int:
    root = find_project_root(Path(__file__))
    checks = run_preflight(root)
    for check in checks:
        status = "PASS" if check.passed else "FAIL"
        print(f"[{status}] {check.name}: {check.detail}")
    return 0 if all(check.passed for check in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
