#!/usr/bin/env python3
"""safely_get_value module"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None)\
        -> Union[Any, T]:
    """safely_get_value: get value from dict
    Args:
        dct: Mapping
        key: Any
        default: Union[T, None] = None
    Return:
        Union[Any, T]
    """
    if key in dct:
        return dct[key]
    else:
        return default
