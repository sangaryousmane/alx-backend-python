#!/usr/bin/env python3
"""takes an integer and returns a asyncio.Task"""
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ takes an integer and returns a asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
