"""CrossHair symbolic-execution fixture using PEP 316 contracts."""

from typing import List


def clamp(value: int, low: int, high: int) -> int:
    """
    pre: low <= high
    post: low <= __return__ <= high
    """
    if value < low:
        return low
    if value > high:
        return high
    return value


def total(values: List[int]) -> int:
    """
    post: __return__ >= 0 if all(value >= 0 for value in values) else True
    """
    result = 0
    for value in values:
        result += value
    return result
