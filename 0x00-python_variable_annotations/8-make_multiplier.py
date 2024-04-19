#!/usr/bin/env python3
"""make_multiplier Module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier: takes a float multiplier and returns a function that
    multiplies a float by multiplier
    Args:
        multiplier (float): multiplier
    Returns:
        callable: function that multiplies a float by multiplier
    """
    return lambda x: x * multiplier
