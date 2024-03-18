#!/usr/bin/env python3
"""takes an integer and returns a asyncio.Task"""
import asyncio


async def task_wait_n(n: int, max_delay: int) -> List[float]:
   """ takes an integer and returns a asyncio.Task"""
   result: List[float] = []
   i: int = 0
   
   while i < n:
       result.append(await task_wait_random(max_delay))
       i += 1
       return result;
