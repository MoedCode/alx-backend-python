#!/usr/bin/env python3
import pytest
import unittest
import time
import math
from Math_h import *
from shapes import *
@pytest.mark.xfail(reason="we know that fctorial does not handle string")
def test_factorial0():
    result = 5 * 4 * 3 * 2 * 1
    assert factorial_iterative('5') == result
    print("test_factorial --0 Ok" , )
@pytest.mark.skip(reason="This seatcher is currently broken")
def test_factorial1():
    result = 5 * 4 * 3 * 2 * 1
    assert factorial_iterative(5) == factorial_recursive(5) == result
    print("test_factorial --1 Ok" , )


def test_factorial2():
    result = 5 * 4 * 3 * 2 * 1
    assert factorial_iterative(5)  == result
    print("test_factorial --2 Ok" , )

# all in one Test
i = 0
@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (9, 81)])
def test_multiple_square_area(side_length,  expected_area):
    global i
    assert Square(side_length).area() == expected_area
    i += 1
    print(f"test_multiple_square_area {i}.. OK")

j = 0
@pytest.mark.parametrize("side_length, expected_perimeter",[(3, 12),(4, 16),(5, 20)])
def test_multiole_square_perimeter(side_length, expected_perimeter):
    global j
    assert Square(side_length).perimeter() == expected_perimeter
    j += 1
    print(f"test_multiole_square_perimeter{j} ... OK")