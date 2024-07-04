#!/usr/bin/env python3
"""
Duck typing with TypeVar
"""
from typing import Mapping, TypeVar, Any, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """
    Safely get value from a dictionary with a default.

    Args:
        dct: A dictionary-like mapping.
        key: The key to lookup.
        default: The default value to return if the key is not found.

    Returns:
        The value associated with the key if it exists, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

