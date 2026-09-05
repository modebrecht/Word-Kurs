from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP
from typing import Iterable

_ONE_DECIMAL = Decimal("0.1")
_MIN_GRADE = Decimal("1.0")
_MAX_GRADE = Decimal("6.0")


def _to_decimal(value: Decimal | int | float | str) -> Decimal:
    """Convert numeric input without inheriting binary-float artefacts."""
    if isinstance(value, Decimal):
        return value
    return Decimal(str(value))


def _round_one_decimal(value: Decimal) -> Decimal:
    return value.quantize(_ONE_DECIMAL, rounding=ROUND_HALF_UP)


def swiss_grade(points: int, max_points: int) -> Decimal:
    """Return the linear Swiss grade, rounded half-up to one decimal place."""
    if max_points <= 0:
        raise ValueError("max_points must be greater than zero")
    if not 0 <= points <= max_points:
        raise ValueError("points must be between 0 and max_points")

    raw = Decimal(1) + Decimal(5) * Decimal(points) / Decimal(max_points)
    return _round_one_decimal(raw)


def swiss_grade_str(points: int, max_points: int) -> str:
    """Return ``swiss_grade`` formatted with exactly one decimal place."""
    return format(swiss_grade(points, max_points), ".1f")


def effort_grade(points: int, possible_points: int) -> Decimal:
    """Return the A1-A13 Fleissnote using the same linear Swiss scale.

    ``possible_points`` is normally 26 (13 sheets x 2 points), but may be
    lower when a sheet is formally removed from the denominator because of
    a longer excused absence.
    """
    return swiss_grade(points, possible_points)


def final_grade_with_drop(
    effort: Decimal | int | float | str,
    steckbrief: Decimal | int | float | str,
    word_test: Decimal | int | float | str,
) -> Decimal:
    """Drop the lowest of three valid component grades and average the best two.

    Component grades are expected to be the already published one-decimal
    grades. The final average is rounded half-up to one decimal place.
    """
    grades = [_to_decimal(value) for value in (effort, steckbrief, word_test)]
    for grade in grades:
        if not _MIN_GRADE <= grade <= _MAX_GRADE:
            raise ValueError("component grades must be between 1.0 and 6.0")

    best_two = sorted(grades, reverse=True)[:2]
    return _round_one_decimal(sum(best_two, Decimal("0")) / Decimal(2))


def final_grade_with_drop_str(
    effort: Decimal | int | float | str,
    steckbrief: Decimal | int | float | str,
    word_test: Decimal | int | float | str,
) -> str:
    """Return ``final_grade_with_drop`` formatted with one decimal place."""
    return format(final_grade_with_drop(effort, steckbrief, word_test), ".1f")
