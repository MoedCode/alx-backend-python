#!/usr/bin/python3
import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_value):
        self.assertEqual(access_nested_map(nested_map, path), expected_value)

if __name__ == "__main__":
    unittest.main()

'''
print(access_nested_map({"a": {"b": 2}}, ("a",)))
print(access_nested_map(nested_map={"a": {"b": 2}}, path=("a", "b")))
print(access_nested_map(nested_map={"a": {"b":None}}, path=("a", "b", "c")))
'''