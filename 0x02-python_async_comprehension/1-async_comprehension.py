#!/usr/bin/env python3
"""
async_comprehension module file for 0x02-python_async_comprehension project
"""
import asyncio
from typing import Generator, List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension function
    Returns:
        List[float]: [description]
    """
    return [i async for i in async_generator()]
