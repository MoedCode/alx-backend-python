#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import requests


def make_http_request(url):
    print(url)
    response = requests.get(url)
    return response.status_code


@patch('requests.get')
def test_successful_request(self, mock_get):
    # Configure mock to return a successful response
    mock_get.return_value.status_code = 200

    # Call the function that makes the HTTP request
    status_code = make_http_request('http://example.com')

    # Verify that the function behaves as expected
    self.assertEqual(status_code, 200)


if __name__ == "__main__":
    unittest.main()
