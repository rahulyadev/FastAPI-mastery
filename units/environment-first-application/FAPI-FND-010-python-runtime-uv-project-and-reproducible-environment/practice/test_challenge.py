"""Collectable tests for the intentionally unsolved learner challenge."""

import sys
from pathlib import Path

import pytest

from .broken_probe import current_executable
from .starter import (
    CheckResult,
    EnvironmentContractError,
    EnvironmentReport,
    PackagePin,
    RuntimeEvidence,
    evaluate_environment,
    load_project_contract,
    render_report,
)


def write_project(root: Path) -> None:
    (root / ".python-version").write_text("3.12.8\n", encoding="utf-8")
    (root / "pyproject.toml").write_text(
        """[project]
name = "environment-challenge"
version = "0.1.0"
requires-python = ">=3.11,<3.14"
dependencies = [
  "fastapi==0.141.1",
  "python-multipart>=0.0.29,<1",
]

[dependency-groups]
dev = ["pytest==9.1.1", "pytest-asyncio>=1.3,<2"]
postgres = ["SQLAlchemy==2.0.52"]
""",
        encoding="utf-8",
    )
    (root / "uv.lock").write_text(
        """version = 1
revision = 3
requires-python = ">=3.11,<3.14"
""",
        encoding="utf-8",
    )


@pytest.fixture
def project_root(tmp_path: Path) -> Path:
    write_project(tmp_path)
    return tmp_path


def runtime_evidence(
    *,
    python_version: str = "3.12.8",
    virtual: bool = True,
    packages: tuple[tuple[str, str], ...] = (
        ("fastapi", "0.141.1"),
        ("pytest", "9.1.1"),
    ),
) -> RuntimeEvidence:
    prefix = Path("/workspace/.venv")
    return RuntimeEvidence(
        python_version=python_version,
        executable=prefix / "bin" / "python",
        prefix=prefix,
        base_prefix=Path("/opt/python") if virtual else prefix,
        installed_distributions=packages,
    )


def test_loads_declarations_groups_exact_pins_and_lock_schema(project_root: Path) -> None:
    contract = load_project_contract(project_root)
    assert contract.python_request == "3.12.8"
    assert contract.requires_python == ">=3.11,<3.14"
    assert contract.dependency_groups == ("dev", "postgres")
    assert contract.exact_pins == (
        PackagePin(distribution="fastapi", version="0.141.1", group=None),
        PackagePin(distribution="pytest", version="9.1.1", group="dev"),
        PackagePin(distribution="sqlalchemy", version="2.0.52", group="postgres"),
    )
    assert contract.lock_schema == 1


@pytest.mark.parametrize("missing_name", (".python-version", "pyproject.toml", "uv.lock"))
def test_missing_required_file_names_the_file(project_root: Path, missing_name: str) -> None:
    (project_root / missing_name).unlink()
    with pytest.raises(EnvironmentContractError, match=missing_name.replace(".", r"\.")):
        load_project_contract(project_root)


def test_malformed_lock_schema_names_uv_lock(project_root: Path) -> None:
    (project_root / "uv.lock").write_text('version = "one"\n', encoding="utf-8")
    with pytest.raises(EnvironmentContractError, match=r"uv\.lock"):
        load_project_contract(project_root)


def test_matching_runtime_and_selected_dev_group_pass(project_root: Path) -> None:
    contract = load_project_contract(project_root)
    report = evaluate_environment(contract, runtime_evidence(), frozenset({"dev"}))
    assert report.ok
    assert tuple(check.code for check in report.checks) == (
        "python-selection",
        "virtual-environment",
        "package:fastapi",
        "package:pytest",
    )


def test_unselected_group_pin_is_not_required(project_root: Path) -> None:
    contract = load_project_contract(project_root)
    report = evaluate_environment(contract, runtime_evidence(), frozenset({"dev"}))
    assert all(check.code != "package:sqlalchemy" for check in report.checks)


def test_wrong_python_is_a_failed_selection_check(project_root: Path) -> None:
    contract = load_project_contract(project_root)
    report = evaluate_environment(
        contract,
        runtime_evidence(python_version="3.11.12"),
        frozenset({"dev"}),
    )
    selection = next(check for check in report.checks if check.code == "python-selection")
    assert not selection.passed
    assert "3.12.8" in selection.detail
    assert "3.11.12" in selection.detail


@pytest.mark.parametrize(
    ("virtual", "executable"),
    (
        (False, Path("/workspace/.venv/bin/python")),
        (True, Path("/usr/bin/python")),
    ),
)
def test_virtual_environment_needs_prefix_and_executable_evidence(
    project_root: Path,
    virtual: bool,
    executable: Path,
) -> None:
    contract = load_project_contract(project_root)
    evidence = runtime_evidence(virtual=virtual)
    evidence = RuntimeEvidence(
        python_version=evidence.python_version,
        executable=executable,
        prefix=evidence.prefix,
        base_prefix=evidence.base_prefix,
        installed_distributions=evidence.installed_distributions,
    )
    report = evaluate_environment(contract, evidence, frozenset({"dev"}))
    isolation = next(check for check in report.checks if check.code == "virtual-environment")
    assert not isolation.passed


def test_missing_selected_distribution_fails_with_observed_state(project_root: Path) -> None:
    contract = load_project_contract(project_root)
    evidence = runtime_evidence(packages=(("fastapi", "0.141.1"),))
    report = evaluate_environment(contract, evidence, frozenset({"dev"}))
    package = next(check for check in report.checks if check.code == "package:pytest")
    assert not package.passed
    assert "not-installed" in package.detail


def test_undeclared_selected_group_is_explicit_failure(project_root: Path) -> None:
    contract = load_project_contract(project_root)
    report = evaluate_environment(contract, runtime_evidence(), frozenset({"docs"}))
    group = next(check for check in report.checks if check.code == "group-selection")
    assert not group.passed
    assert "docs" in group.detail


def test_render_report_is_stable_plain_text() -> None:
    report = EnvironmentReport(
        checks=(
            CheckResult("python-selection", True, "requested=3.12.8 observed=3.12.8"),
            CheckResult("package:fastapi", False, "expected=0.141.1 observed=not-installed"),
        )
    )
    assert render_report(report) == (
        "[PASS] python-selection: requested=3.12.8 observed=3.12.8\n"
        "[FAIL] package:fastapi: expected=0.141.1 observed=not-installed\n"
    )
    assert "\x1b" not in render_report(report)
    assert render_report(EnvironmentReport(checks=())) == ""


def test_seeded_probe_reports_the_running_interpreter() -> None:
    assert current_executable() == Path(sys.executable)
