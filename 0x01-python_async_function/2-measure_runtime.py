#!/usr/bin/env python3

"""Create a measure_time function with integers n and max_delay arguments"""

import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return measure"""
    total_time = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (perf_counter() - total_time) / n
