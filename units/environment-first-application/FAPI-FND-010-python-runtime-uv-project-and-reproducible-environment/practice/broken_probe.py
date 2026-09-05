"""Seeded provenance defect for the debugging task."""

from pathlib import Path


def current_executable() -> Path:
    """Return the interpreter executable that is running this process."""
    return Path("python")
