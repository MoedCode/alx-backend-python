#!/usr/bin/env python3
"module for test utils  "
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import (
    access_nested_map,
    get_json
)


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


class TestGetJson(unittest.TestCase):
    "Test get_json class"
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url_val: str, exp_payload: Dict) -> None:
        "Test get_json method"
        attr = {"json.return_value": exp_payload}
        with patch("requests.get", return_value=Mock(**attr)) as get_req:
            self.assertEqual(get_json(url_val), exp_payload)
            get_req.assert_called_once_with(url_val)


if __name__ == "__main__":
    unittest.main()

'''
print(access_nested_map({"a": {"b": 2}}, ("a",)))
print(access_nested_map(nested_map={"a": {"b": 2}}, path=("a", "b")))
print(access_nested_map(nested_map={"a": {"b":None}}, path=("a", "b", "c")))
'''
