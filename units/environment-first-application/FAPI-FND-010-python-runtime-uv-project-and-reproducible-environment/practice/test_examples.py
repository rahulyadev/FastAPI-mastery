"""Passing scaffold tests for worked examples and the micro-lab."""

import json
import subprocess
import sys
from pathlib import Path

import pytest

UNIT_DIR = Path(__file__).resolve().parents[1]
EXAMPLES = UNIT_DIR / "examples"


def run_python(path: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(path), *arguments],
        cwd=UNIT_DIR,
        check=False,
        capture_output=True,
        text=True,
        timeout=30,
    )


@pytest.mark.parametrize(
    "filename",
    ("01_minimal.py", "02_traced.py", "03_realistic.py", "04_failure_case.py"),
)
def test_each_worked_example_runs(filename: str) -> None:
    completed = run_python(EXAMPLES / filename)
    assert completed.returncode == 0, completed.stderr or completed.stdout


def test_minimal_example_reports_live_provenance() -> None:
    completed = run_python(EXAMPLES / "01_minimal.py")
    assert "python=" in completed.stdout
    assert f"executable={Path(sys.executable)}" in completed.stdout
    assert "virtual_environment=True" in completed.stdout
    assert "fastapi=0.141.1" in completed.stdout


def test_trace_names_declaration_resolution_and_execution() -> None:
    completed = run_python(EXAMPLES / "02_traced.py")
    assert "selection [uv]" in completed.stdout
    assert "compatibility [packaging]" in completed.stdout
    assert "resolution [uv]" in completed.stdout
    assert "execution [Python]" in completed.stdout


def test_realistic_preflight_reports_only_passes() -> None:
    completed = run_python(EXAMPLES / "03_realistic.py")
    assert "[PASS] python-selection:" in completed.stdout
    assert "[PASS] virtual-environment:" in completed.stdout
    assert "[FAIL]" not in completed.stdout


def test_failure_example_classifies_independent_layers() -> None:
    completed = run_python(EXAMPLES / "04_failure_case.py")
    assert "command-provenance:" in completed.stdout
    assert "python-selection:" in completed.stdout
    assert "resolution:" in completed.stdout
    assert "group-selection:" in completed.stdout
    assert "installed-state:" in completed.stdout


def test_micro_lab_json_is_runtime_evidence() -> None:
    completed = run_python(UNIT_DIR / "practice" / "micro_lab.py", "--json")
    assert completed.returncode == 0, completed.stderr
    evidence = json.loads(completed.stdout)
    assert evidence["python_request"] == "3.14.7"
    assert evidence["python_observed"] == "3.14.7"
    assert evidence["in_virtual_environment"] is True
    assert evidence["installed_distributions"]["fastapi"] == "0.141.1"
    assert "dev" in evidence["declared_groups"]
    assert evidence["lock_schema"] == 1
