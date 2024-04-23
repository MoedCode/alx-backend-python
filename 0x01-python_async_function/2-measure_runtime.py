#!/usr/bin/env python3
"""Asynchronous module with measure_time function"""
from asyncio import run
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay)
    Args:
        n (int): number of times to call wait_random
        max_delay (int): max delay passed to wait_random
    Returns:
        float: total time / n
    """
    start: float = time()
    run(wait_n(n, max_delay))
    end: float = time()
    return (end - start) / n
