#!/usr/bin/env python3
import unittest
import time
import math
from shapes import Circle, Square
class TstCircle(unittest.TestCase):
    def setUp(self):
        print("Setting up")
        self.circle0 = Circle(10)

    def tearDown(self):
        print("Tearing down")
        del self.circle0
    for i in range(1000):

        def test_area(self):
            assert self.circle0.area() == math.pi * self.circle0.radius ** 2
            print('Ok')
        def test_perimeter(self):
            assert self.circle0.perimeter() == 2 * math.pi * self.circle0.radius


def test_square_cls(Square, ):
    print("-----test_square_cls--------")
    square = Square()


if __name__ == "__main__":
    unittest.main()
    # x = TstCircle()
    # x.setup_metod(x.test_0)
