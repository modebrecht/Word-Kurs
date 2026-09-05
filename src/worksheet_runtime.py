from __future__ import annotations

from pathlib import Path
from typing import Callable

from build_runtime import install_deterministic_docx_save
from validate_build import validate_course_package

ROOT = Path(__file__).resolve().parents[1]


def run_single(code: str, builder: Callable[[Path], None]) -> None:
    """Build one worksheet in-place and validate the complete existing package."""
    install_deterministic_docx_save()
    builder(ROOT)
    validate_course_package(ROOT)
    print(f"Generated {code} in {ROOT / 'arbeitsblaetter'}")
