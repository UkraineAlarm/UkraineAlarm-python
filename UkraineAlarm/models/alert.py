# coding: utf-8

"""
    Ukraine Alert API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: support@stfalcon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Alert(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'region_id': 'str',
        'region_type': 'V2RegionType',
        'type': 'AlertType',
        'last_update': 'datetime'
    }

    attribute_map = {
        'region_id': 'regionId',
        'region_type': 'regionType',
        'type': 'type',
        'last_update': 'lastUpdate'
    }

    def __init__(self, region_id=None, region_type=None, type=None, last_update=None):  # noqa: E501
        """Alert - a model defined in Swagger"""  # noqa: E501
        self._region_id = None
        self._region_type = None
        self._type = None
        self._last_update = None
        self.discriminator = None
        if region_id is not None:
            self.region_id = region_id
        if region_type is not None:
            self.region_type = region_type
        if type is not None:
            self.type = type
        if last_update is not None:
            self.last_update = last_update

    @property
    def region_id(self):
        """Gets the region_id of this Alert.  # noqa: E501


        :return: The region_id of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this Alert.


        :param region_id: The region_id of this Alert.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def region_type(self):
        """Gets the region_type of this Alert.  # noqa: E501


        :return: The region_type of this Alert.  # noqa: E501
        :rtype: V2RegionType
        """
        return self._region_type

    @region_type.setter
    def region_type(self, region_type):
        """Sets the region_type of this Alert.


        :param region_type: The region_type of this Alert.  # noqa: E501
        :type: V2RegionType
        """

        self._region_type = region_type

    @property
    def type(self):
        """Gets the type of this Alert.  # noqa: E501


        :return: The type of this Alert.  # noqa: E501
        :rtype: AlertType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Alert.


        :param type: The type of this Alert.  # noqa: E501
        :type: AlertType
        """

        self._type = type

    @property
    def last_update(self):
        """Gets the last_update of this Alert.  # noqa: E501


        :return: The last_update of this Alert.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this Alert.


        :param last_update: The last_update of this Alert.  # noqa: E501
        :type: datetime
        """

        self._last_update = last_update

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Alert, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Alert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
