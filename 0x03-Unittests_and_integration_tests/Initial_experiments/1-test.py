#!/usr/bin/env python3
from Math_h import fibonacci
import unittest
import pytest
def test_fibonacci_sequence():
    result0 = fibonacci(5)
    assert result0 == [0, 1, 1, 2, 3]
    print(' fibonacci_sequence  --  Ok')
def test_fibonacci_invalid_type():
    with pytest.raises(ValueError):
        fibonacci(-5)
    print("Value Test -- Ok")

test_fibonacci_sequence()
test_fibonacci_invalid_type()