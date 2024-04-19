#!/usr/bin/env python3
"""element_length module"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element_length: takes a list and returns a list of tuples
    Args:
        lst (Iterable[Sequence]): list of sequences
    Returns:
        List[Tuple[Sequence, int]]: list of tuples
    """
    return [(i, len(i)) for i in lst]
