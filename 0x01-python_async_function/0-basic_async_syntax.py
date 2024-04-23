#!/usr/bin/env python3
"""Asynchronous module with wait_random function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that takes in an integer argument
    Args:
        max_delay (int, optional): Defaults to 10.
    Returns:
        float: random delay between 0 and max_delay
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
