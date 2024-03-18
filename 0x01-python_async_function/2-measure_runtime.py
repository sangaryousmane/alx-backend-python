#!/usr/bin/env python3
""" Measure the runtime of the coroutine"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime of the coroutine"""
    start_time: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time: float = time.perf_counter() - start_time
    result: float = total_time / n
    return result
