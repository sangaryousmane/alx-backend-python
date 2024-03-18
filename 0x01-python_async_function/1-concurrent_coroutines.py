#!/usr/bin/env python3
""" execute multiple coroutines at the same time with async"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ execute multiple coroutines at the same time with async"""

    result: List[float] = []
    i: int = 0
    while i < n:
        result.append(await wait_random(max_delay))
        i += 1
    return result
