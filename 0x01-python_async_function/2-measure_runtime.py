#!/usr/bin/env python3
""" Measure the runtime of the coroutine"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime of the coroutine"""
    start_time = time()
    await asyncio.run(wait_n(n, max_delay))
    total_time = time() - start_time
    result = total_time / n
    return result
