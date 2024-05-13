#!/usr/bin/env python3
"module for test utils  "
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """class for Tests the `access_nested_map` function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_value):
        """for  Tests `access_nested_map`'s output."""
        self.assertEqual(access_nested_map(nested_map, path), expected_value)


if __name__ == "__main__":
    unittest.main()

'''
print(access_nested_map({"a": {"b": 2}}, ("a",)))
print(access_nested_map(nested_map={"a": {"b": 2}}, path=("a", "b")))
print(access_nested_map(nested_map={"a": {"b":None}}, path=("a", "b", "c")))
'''
