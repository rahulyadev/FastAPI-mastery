"""Classify a synthetic environment incident without changing local state."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class EnvironmentSnapshot:
    expected_executable: Path
    observed_executable: Path
    requested_python: str
    observed_python: str
    required_groups: frozenset[str]
    selected_groups: frozenset[str]
    lock_fresh: bool
    locked_packages: tuple[tuple[str, str], ...]
    installed_packages: tuple[tuple[str, str], ...]


def diagnose(snapshot: EnvironmentSnapshot) -> tuple[str, ...]:
    findings: list[str] = []
    if snapshot.observed_executable != snapshot.expected_executable:
        findings.append(
            "command-provenance: the command used a different interpreter "
            "than the project environment"
        )
    if snapshot.observed_python != snapshot.requested_python:
        findings.append(
            "python-selection: the running patch version does not match the project request"
        )
    if not snapshot.lock_fresh:
        findings.append("resolution: project declarations and the lockfile disagree")

    missing_groups = snapshot.required_groups - snapshot.selected_groups
    if missing_groups:
        findings.append(f"group-selection: missing {', '.join(sorted(missing_groups))}")

    locked = dict(snapshot.locked_packages)
    installed = dict(snapshot.installed_packages)
    drift = [
        f"{name} locked={locked[name]} installed={installed.get(name, 'not-installed')}"
        for name in sorted(locked)
        if installed.get(name) != locked[name]
    ]
    if drift:
        findings.append(f"installed-state: {'; '.join(drift)}")

    return tuple(findings) or ("no mismatch represented by this snapshot",)


def main() -> None:
    incident = EnvironmentSnapshot(
        expected_executable=Path("/workspace/.venv/bin/python"),
        observed_executable=Path("/usr/bin/python"),
        requested_python="3.14.7",
        observed_python="3.14.4",
        required_groups=frozenset({"dev"}),
        selected_groups=frozenset(),
        lock_fresh=False,
        locked_packages=(("fastapi", "0.141.1"), ("pytest", "9.1.1")),
        installed_packages=(("fastapi", "0.140.0"),),
    )
    print("Synthetic incident; no local files or packages are changed.")
    for index, finding in enumerate(diagnose(incident), start=1):
        print(f"{index}. {finding}")


if __name__ == "__main__":
    main()
