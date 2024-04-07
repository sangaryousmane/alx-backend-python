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

    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=unittest.mock.PropertyMock)
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json, mock_public_repos_url):
        # Define the mocked return value for get_json
        mocked_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = mocked_payload
        url = "https://api.github.com/orgs/testorg/repos"
        mock_public_repos_url.return_value = url
        github_org_client = GithubOrgClient("testorg")
        result = github_org_client.public_repos
        mock_get_json.assert_called_once_with(url)
        self.assertEqual(result, mocked_payload)


if __name__ == '__main__':
    unittest.main()
