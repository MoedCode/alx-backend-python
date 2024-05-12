#!/usr/bin/python3
import asyncio
from typing import List

# Assuming wait_random is defined in a separate file and imported here
from tst0 import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawns wait_random n times with the specified max_delay.

    Args:
        n: Number of times to spawn wait_random coroutine.
        max_delay: Maximum delay for each wait_random coroutine.

    Returns:
        List of all the delays in ascending order.
    """
    delays = []
    tasks = []

    async def run_wait_random():
        delay = await wait_random(max_delay)
        delays.append(delay)

    # Schedule wait_random coroutines
    for _ in range(n):
        tasks.append(asyncio.create_task(run_wait_random()))
        # print("tasks from inside loo", tasks)

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

    # Sort the delays in ascending order
    delays.sort()
    print("Task before return ", tasks)
    return delays

# Test the wait_n coroutine
if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    # print(asyncio.run(wait_n(10, 7)))
    # print(asyncio.run(wait_n(10, 0)))
