#!/usr/bin/env python3
"""The function callable float"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function multiplier callable"""
    return lambda num: multiplier * num
