#!/usr/bin/env python3
""" A module for accesing nested map
"""
from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """ A class for testing access map
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "KeyError not raised for empty map"),
        ({"a": 1}, ("a", "b"), "KeyError not raised for invalid path")
    ])
    def test_access_nested_map_exception(self, np, path, expected_msg):
        with self.assertRaises(KeyError) as msg:
            access_nested_map(np, path)
        self.assertEqual(str(msg.exception), expected_msg)


class TestGetJson(unittest.TestCase):
    """ A class to implement the get_json method for mocking """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Mock the json method of the response object """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
