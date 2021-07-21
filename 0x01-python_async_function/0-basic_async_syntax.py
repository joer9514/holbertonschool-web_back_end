#!/usr/bin/env python3

""" Asynchronous coroutine that takes in an integer argument """

import asyncio
from random import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Return random number
    args:
        max_delay = default value is 10
    """
    random_number: float = random() * max_delay
    await asyncio.sleep(random_number)
    return random_number
