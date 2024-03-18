#!/usr/bin/env python3
"""takes an integer and returns a asyncio.Task"""
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
   """ takes an integer and returns a asyncio.Task"""
   result = [task_wait_random(max_delay) for _ in range(n)]
   return [await t for t in asyncio.as_completed(result)]
