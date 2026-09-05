from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP

_ONE_DECIMAL = Decimal("0.1")


def swiss_grade(points: int, max_points: int) -> Decimal:
    """Return the linear Swiss grade, rounded half-up to one decimal place."""
    if max_points <= 0:
        raise ValueError("max_points must be greater than zero")
    if not 0 <= points <= max_points:
        raise ValueError("points must be between 0 and max_points")

    raw = Decimal(1) + Decimal(5) * Decimal(points) / Decimal(max_points)
    return raw.quantize(_ONE_DECIMAL, rounding=ROUND_HALF_UP)


def swiss_grade_str(points: int, max_points: int) -> str:
    """Return ``swiss_grade`` formatted with exactly one decimal place."""
    return format(swiss_grade(points, max_points), ".1f")
