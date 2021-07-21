#!/usr/bin/env python3

"""
Import wait_random from the previous python file that
you’ve written and write an async routine called wait_n
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return list of floats
    args:
        n -> int
        max_delay -> int
        Return: List[float]
    """
    list_random: List[float] = [await wait_random(max_delay) for _ in range(n)]
    return sorted(list_random)
