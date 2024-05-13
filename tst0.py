#!/usr/bin/python3
import asyncio
import random


async def fun_from_main_thread0():
    print("before asynchronous process  -> function from")


async def wait_random(max_delay: int = 10) -> float:
    '''delay time represent something like asynchronous
    operation like promise maker function in js'''
    delay = random.uniform(0, max_delay)
    ''' wait is the a process wait for the previous process
        like promise receiver in js '''
    await asyncio.sleep(delay)
    return delay


async def fun_from_main_thread1():
    print("After asynchronous process  -> function from")


async def main():
    await fun_from_main_thread0()
    # Run the coroutine in the background
    task = asyncio.create_task(wait_random())
    await fun_from_main_thread1()              # Execute the function asynchronously
    # Wait for and get the result of the coroutine
    result = await task
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
