#!/usr/bin/env python3
"""sum_mixed_list module file"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum a list of floats and integers
    Args:
        mxd_lst (List[Union[int, float]]): list of floats and integers
    Returns:
        float: sum of floats and integers
    """
    return sum(mxd_lst)
