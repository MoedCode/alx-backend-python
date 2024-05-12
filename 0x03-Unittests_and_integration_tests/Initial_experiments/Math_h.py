#!/usr/bin/env python3
# fibonacci.py

def fibonacci(n):
    """
    Calculate the Fibonacci sequence up to the nth term using an iterative approach.

    Parameters:
    - n (int): The term up to which Fibonacci sequence is calculated.

    Returns:
    - List[int]: The Fibonacci sequence up to the nth term.
    """
    # Check if input is integer
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    # Check if input is non-negative
    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    # Handle special cases
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Initialize Fibonacci sequence with first two terms
    fib_sequence = [0, 1]

    # Calculate subsequent terms iteratively
    for _ in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
