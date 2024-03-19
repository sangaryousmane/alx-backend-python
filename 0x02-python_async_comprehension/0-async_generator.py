#!/usr/bin/env python3
""" Async Generator: will loop 10 times, each time asynchronously
wait 1 second, then yield a random number between 0 and 10.
"""
import asyncio


async def async_generator():
    """ Async Generator: will loop 10 times, each time asynchronously
    wait 1 second, then yield a random number between 0 and 10.
    """
    for i in range(0, 11):
        yield i
        asyncio.sleep(1)
