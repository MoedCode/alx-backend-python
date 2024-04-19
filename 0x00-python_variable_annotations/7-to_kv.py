#!/usr/bin/env python3
"""to_kv module"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv: takes a string k and an int OR float v as arguments
    Args:
        k (str): string to be returned
        v (Union[int, float]): int OR float to be returned
    Returns:
        Tuple[str, float]: tuple containing k and the square of v
    """
    return (k, v ** 2)
