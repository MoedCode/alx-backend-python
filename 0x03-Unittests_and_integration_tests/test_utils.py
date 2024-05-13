#!/usr/bin/env python3
"module for test utils  "
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """class for Tests the `access_nested_map` function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
    ) -> None:
        """for  Tests `access_nested_map`'s output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
        self, nested_map: Dict,
        Path: Tuple[str],
        expected: Exception,
    ) -> None:
        with self.assertRaises(expected):
            access_nested_map(nested_map, Path)


if __name__ == "__main__":
    unittest.main()

'''
print(access_nested_map({"a": {"b": 2}}, ("a",)))
print(access_nested_map(nested_map={"a": {"b": 2}}, path=("a", "b")))
print(access_nested_map(nested_map={"a": {"b":None}}, path=("a", "b", "c")))
'''
