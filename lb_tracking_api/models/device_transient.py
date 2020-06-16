# coding: utf-8

"""
    TrackingAPI

    API for retrieving tracking data and changing settings on LightBug & RemoteThings tracking devices  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DeviceTransient(object):
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
        'type': 'float',
        'duration': 'float',
        'triggered_at': 'datetime',
        'end': 'datetime',
        'sent': 'datetime',
        'sms': 'bool',
        'id': 'float',
        'device_id': 'float'
    }

    attribute_map = {
        'type': 'type',
        'duration': 'duration',
        'triggered_at': 'triggeredAt',
        'end': 'end',
        'sent': 'sent',
        'sms': 'sms',
        'id': 'id',
        'device_id': 'deviceId'
    }

    def __init__(self, type=None, duration=None, triggered_at=None, end=None, sent=None, sms=False, id=None, device_id=None):  # noqa: E501
        """DeviceTransient - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._duration = None
        self._triggered_at = None
        self._end = None
        self._sent = None
        self._sms = None
        self._id = None
        self._device_id = None
        self.discriminator = None

        self.type = type
        self.duration = duration
        self.triggered_at = triggered_at
        if end is not None:
            self.end = end
        if sent is not None:
            self.sent = sent
        if sms is not None:
            self.sms = sms
        if id is not None:
            self.id = id
        if device_id is not None:
            self.device_id = device_id

    @property
    def type(self):
        """Gets the type of this DeviceTransient.  # noqa: E501


        :return: The type of this DeviceTransient.  # noqa: E501
        :rtype: float
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeviceTransient.


        :param type: The type of this DeviceTransient.  # noqa: E501
        :type: float
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def duration(self):
        """Gets the duration of this DeviceTransient.  # noqa: E501


        :return: The duration of this DeviceTransient.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this DeviceTransient.


        :param duration: The duration of this DeviceTransient.  # noqa: E501
        :type: float
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def triggered_at(self):
        """Gets the triggered_at of this DeviceTransient.  # noqa: E501


        :return: The triggered_at of this DeviceTransient.  # noqa: E501
        :rtype: datetime
        """
        return self._triggered_at

    @triggered_at.setter
    def triggered_at(self, triggered_at):
        """Sets the triggered_at of this DeviceTransient.


        :param triggered_at: The triggered_at of this DeviceTransient.  # noqa: E501
        :type: datetime
        """
        if triggered_at is None:
            raise ValueError("Invalid value for `triggered_at`, must not be `None`")  # noqa: E501

        self._triggered_at = triggered_at

    @property
    def end(self):
        """Gets the end of this DeviceTransient.  # noqa: E501


        :return: The end of this DeviceTransient.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this DeviceTransient.


        :param end: The end of this DeviceTransient.  # noqa: E501
        :type: datetime
        """

        self._end = end

    @property
    def sent(self):
        """Gets the sent of this DeviceTransient.  # noqa: E501


        :return: The sent of this DeviceTransient.  # noqa: E501
        :rtype: datetime
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """Sets the sent of this DeviceTransient.


        :param sent: The sent of this DeviceTransient.  # noqa: E501
        :type: datetime
        """

        self._sent = sent

    @property
    def sms(self):
        """Gets the sms of this DeviceTransient.  # noqa: E501


        :return: The sms of this DeviceTransient.  # noqa: E501
        :rtype: bool
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this DeviceTransient.


        :param sms: The sms of this DeviceTransient.  # noqa: E501
        :type: bool
        """

        self._sms = sms

    @property
    def id(self):
        """Gets the id of this DeviceTransient.  # noqa: E501


        :return: The id of this DeviceTransient.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceTransient.


        :param id: The id of this DeviceTransient.  # noqa: E501
        :type: float
        """

        self._id = id

    @property
    def device_id(self):
        """Gets the device_id of this DeviceTransient.  # noqa: E501


        :return: The device_id of this DeviceTransient.  # noqa: E501
        :rtype: float
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DeviceTransient.


        :param device_id: The device_id of this DeviceTransient.  # noqa: E501
        :type: float
        """

        self._device_id = device_id

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
        if issubclass(DeviceTransient, dict):
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
        if not isinstance(other, DeviceTransient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other