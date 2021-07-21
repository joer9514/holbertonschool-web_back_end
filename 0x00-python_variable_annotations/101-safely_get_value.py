#!/usr/bin/env python3

from typing import Union, Any, Mapping, T


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """Return key"""
    if key in dct:
        return dct[key]
    else:
        return default
