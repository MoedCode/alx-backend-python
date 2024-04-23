#!/usr/bin/env python3
"""Asynchronous module with wait_n function"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """waits for random delay and returns list of delays in ascending order
    Args:
        n (int): number of times to call wait_random
        max_delay (int): max delay passed to wait_random
    Returns:
        list: list of delays in ascending order
    """
    tasklist: List[float] = []
    tasklist = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasklist)]
