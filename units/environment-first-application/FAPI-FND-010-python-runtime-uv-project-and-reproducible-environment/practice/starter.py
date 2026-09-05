"""Unsolved environment inspector for FAPI-FND-010."""

from dataclasses import dataclass
from pathlib import Path


class EnvironmentContractError(ValueError):
    """Raised when required project environment metadata is absent or invalid."""


@dataclass(frozen=True)
class PackagePin:
    distribution: str
    version: str
    group: str | None


@dataclass(frozen=True)
class ProjectContract:
    python_request: str
    requires_python: str
    dependency_groups: tuple[str, ...]
    exact_pins: tuple[PackagePin, ...]
    lock_schema: int


@dataclass(frozen=True)
class RuntimeEvidence:
    python_version: str
    executable: Path
    prefix: Path
    base_prefix: Path
    installed_distributions: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class CheckResult:
    code: str
    passed: bool
    detail: str


@dataclass(frozen=True)
class EnvironmentReport:
    checks: tuple[CheckResult, ...]

    @property
    def ok(self) -> bool:
        return all(check.passed for check in self.checks)


def load_project_contract(project_root: Path) -> ProjectContract:
    """Load the project declarations needed for an environment check."""
    raise NotImplementedError("learner task: load and validate the project contract")


def evaluate_environment(
    contract: ProjectContract,
    evidence: RuntimeEvidence,
    selected_groups: frozenset[str],
) -> EnvironmentReport:
    """Compare runtime evidence with the applicable part of the project contract."""
    raise NotImplementedError("learner task: evaluate environment evidence")


def render_report(report: EnvironmentReport) -> str:
    """Render stable, plain-text check lines for a terminal or CI log."""
    raise NotImplementedError("learner task: render the environment report")
