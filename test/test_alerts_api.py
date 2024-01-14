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
from UkraineAlarm.api.alerts_api import AlertsApi  # noqa: E501
from UkraineAlarm.rest import ApiException


class TestAlertsApi(unittest.TestCase):
    """AlertsApi unit test stubs"""

    def setUp(self):
        self.api = AlertsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v3_alerts_get(self):
        """Test case for api_v3_alerts_get

        Області, регіони та громади з тривогами  # noqa: E501
        """
        pass

    def test_api_v3_alerts_region_history_get(self):
        """Test case for api_v3_alerts_region_history_get

        Отримати останніх 25 тривог регіону  # noqa: E501
        """
        pass

    def test_api_v3_alerts_region_id_get(self):
        """Test case for api_v3_alerts_region_id_get

        Статус області/регіону/громади  # noqa: E501
        """
        pass

    def test_api_v3_alerts_status_get(self):
        """Test case for api_v3_alerts_status_get

        Перевірка номеру останньої дії. Використовувати для перевірки необхідності оновлювати дані  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()