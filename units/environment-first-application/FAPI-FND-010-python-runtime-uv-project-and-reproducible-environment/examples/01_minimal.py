"""Print the smallest useful proof of Python environment provenance."""

import platform
import sys
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

PACKAGES = ("fastapi", "pydantic", "uvicorn", "pytest")


def installed_version(distribution: str) -> str:
    """Return an installed distribution version without importing that package."""
    try:
        return version(distribution)
    except PackageNotFoundError:
        return "not-installed"


def main() -> None:
    print(f"python={platform.python_version()}")
    print(f"executable={Path(sys.executable)}")
    print(f"virtual_environment={sys.prefix != sys.base_prefix}")
    for package in PACKAGES:
        print(f"{package}={installed_version(package)}")


if __name__ == "__main__":
    main()
