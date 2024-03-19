#!/usr/bin/env python3
"""  Run time for four parallel comprehensions"""
from time import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def async_comprehension():
    """  Run time for four parallel comprehensions"""
    start = time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time()
    return end - start
