#!/usr/bin/env python3
"""sum a list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum a list of floats
    Args:
        input_list (List[float]): list of floats
    Returns:
        float: sum of floats
    """
    return sum(input_list)
