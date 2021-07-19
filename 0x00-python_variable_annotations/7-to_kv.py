#!/usr/bin/env python3
"""The function join the tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This function tuple"""
    return (k, (v * v))
