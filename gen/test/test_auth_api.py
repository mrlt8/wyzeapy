"""
    Wyze Auth API

    This spec describes the user authentication API for Wyze as it is used by ha-wyzeapi  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: joshua@mulliken.net
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.auth_api import AuthApi  # noqa: E501


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self):
        self.api = AuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_app_user_refresh_token_post(self):
        """Test case for app_user_refresh_token_post

        Refreshes the access_token using the refresh_token  # noqa: E501
        """
        pass

    def test_user_login_post(self):
        """Test case for user_login_post

        Logs user into the system  # noqa: E501
        """
        pass

    def test_user_login_send_sms_code_post(self):
        """Test case for user_login_send_sms_code_post

        Sends an SMS MFA Code to the user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
