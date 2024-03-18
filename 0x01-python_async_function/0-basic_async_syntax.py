#!/usr/bin/env python3
""" Write an asynchronous coroutine that takes
in an integer argument"""
from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """  Write an asynchronous coroutine that takes
    in an integer argument"""
    wait_time = uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
