# coding: utf-8

"""
    Ukraine Alert API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: support@stfalcon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import UkraineAlarm
from UkraineAlarm.api.regions_api import RegionsApi  # noqa: E501
from UkraineAlarm.rest import ApiException


class TestRegionsApi(unittest.TestCase):
    """RegionsApi unit test stubs"""

    def setUp(self):
        self.api = RegionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v3_regions_get(self):
        """Test case for api_v3_regions_get

        Повертає список усіх областей, регіонів та міст  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()