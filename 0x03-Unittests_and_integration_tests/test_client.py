#!/usr/bin/env python3
""" Implement a GitHub client
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Test Gihub organization client module"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ Test this method """
        mock_get_json.return_value = {"login": org_name, "id": 12345}
        github_org_client = GithubOrgClient(org_name)

        result = github_org_client.org
        url = 'https://api.github.com/orgs/{}'.format(org_name)
        mock_get_json.assert_called_once_with(url)
        self.assertEqual(result, mock_get_json.return_value)


if __name__ == '__main__':
    unittest.main()
