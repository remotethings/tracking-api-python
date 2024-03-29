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

from lb_tracking_api.configuration import Configuration


class Geofence(object):
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
        'outline': 'list[object]',
        'center': 'GeoPoint',
        'radius': 'float',
        'type': 'str',
        'name': 'str',
        'was_inside': 'bool',
        'last_checked': 'datetime',
        'modified': 'bool',
        'meta': 'object',
        'id': 'float',
        'device_id': 'float',
        'config_id': 'float',
        'user_id': 'float'
    }

    attribute_map = {
        'outline': 'outline',
        'center': 'center',
        'radius': 'radius',
        'type': 'type',
        'name': 'name',
        'was_inside': 'wasInside',
        'last_checked': 'lastChecked',
        'modified': 'modified',
        'meta': 'meta',
        'id': 'id',
        'device_id': 'deviceId',
        'config_id': 'configId',
        'user_id': 'userId'
    }

    def __init__(self, outline=None, center=None, radius=None, type=None, name=None, was_inside=False, last_checked=None, modified=False, meta=None, id=None, device_id=None, config_id=None, user_id=None, _configuration=None):  # noqa: E501
        """Geofence - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._outline = None
        self._center = None
        self._radius = None
        self._type = None
        self._name = None
        self._was_inside = None
        self._last_checked = None
        self._modified = None
        self._meta = None
        self._id = None
        self._device_id = None
        self._config_id = None
        self._user_id = None
        self.discriminator = None

        if outline is not None:
            self.outline = outline
        if center is not None:
            self.center = center
        if radius is not None:
            self.radius = radius
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if was_inside is not None:
            self.was_inside = was_inside
        if last_checked is not None:
            self.last_checked = last_checked
        if modified is not None:
            self.modified = modified
        if meta is not None:
            self.meta = meta
        if id is not None:
            self.id = id
        if device_id is not None:
            self.device_id = device_id
        if config_id is not None:
            self.config_id = config_id
        if user_id is not None:
            self.user_id = user_id

    @property
    def outline(self):
        """Gets the outline of this Geofence.  # noqa: E501

        Array of {lat:x,lng:y} objects representing the vertices of the polygon. Do not use with center and radius.  # noqa: E501

        :return: The outline of this Geofence.  # noqa: E501
        :rtype: list[object]
        """
        return self._outline

    @outline.setter
    def outline(self, outline):
        """Sets the outline of this Geofence.

        Array of {lat:x,lng:y} objects representing the vertices of the polygon. Do not use with center and radius.  # noqa: E501

        :param outline: The outline of this Geofence.  # noqa: E501
        :type: list[object]
        """

        self._outline = outline

    @property
    def center(self):
        """Gets the center of this Geofence.  # noqa: E501

        For circular geofences, the center. Property is ignored if outline != null.  # noqa: E501

        :return: The center of this Geofence.  # noqa: E501
        :rtype: GeoPoint
        """
        return self._center

    @center.setter
    def center(self, center):
        """Sets the center of this Geofence.

        For circular geofences, the center. Property is ignored if outline != null.  # noqa: E501

        :param center: The center of this Geofence.  # noqa: E501
        :type: GeoPoint
        """

        self._center = center

    @property
    def radius(self):
        """Gets the radius of this Geofence.  # noqa: E501

        For circular geofences, the radius of the circle in meters. Property is ignored if outline != null.  # noqa: E501

        :return: The radius of this Geofence.  # noqa: E501
        :rtype: float
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Sets the radius of this Geofence.

        For circular geofences, the radius of the circle in meters. Property is ignored if outline != null.  # noqa: E501

        :param radius: The radius of this Geofence.  # noqa: E501
        :type: float
        """

        self._radius = radius

    @property
    def type(self):
        """Gets the type of this Geofence.  # noqa: E501

        Grouping value  # noqa: E501

        :return: The type of this Geofence.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Geofence.

        Grouping value  # noqa: E501

        :param type: The type of this Geofence.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this Geofence.  # noqa: E501


        :return: The name of this Geofence.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Geofence.


        :param name: The name of this Geofence.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def was_inside(self):
        """Gets the was_inside of this Geofence.  # noqa: E501

        If the last point received was inside the geofence. Only updated for notifications (not the safe-zone as that is evaluated on the device)  # noqa: E501

        :return: The was_inside of this Geofence.  # noqa: E501
        :rtype: bool
        """
        return self._was_inside

    @was_inside.setter
    def was_inside(self, was_inside):
        """Sets the was_inside of this Geofence.

        If the last point received was inside the geofence. Only updated for notifications (not the safe-zone as that is evaluated on the device)  # noqa: E501

        :param was_inside: The was_inside of this Geofence.  # noqa: E501
        :type: bool
        """

        self._was_inside = was_inside

    @property
    def last_checked(self):
        """Gets the last_checked of this Geofence.  # noqa: E501

        When the geofence was last evaluated. Only updated for notifications (not the safe-zone as that is evaluated on the device)  # noqa: E501

        :return: The last_checked of this Geofence.  # noqa: E501
        :rtype: datetime
        """
        return self._last_checked

    @last_checked.setter
    def last_checked(self, last_checked):
        """Sets the last_checked of this Geofence.

        When the geofence was last evaluated. Only updated for notifications (not the safe-zone as that is evaluated on the device)  # noqa: E501

        :param last_checked: The last_checked of this Geofence.  # noqa: E501
        :type: datetime
        """

        self._last_checked = last_checked

    @property
    def modified(self):
        """Gets the modified of this Geofence.  # noqa: E501


        :return: The modified of this Geofence.  # noqa: E501
        :rtype: bool
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Geofence.


        :param modified: The modified of this Geofence.  # noqa: E501
        :type: bool
        """

        self._modified = modified

    @property
    def meta(self):
        """Gets the meta of this Geofence.  # noqa: E501


        :return: The meta of this Geofence.  # noqa: E501
        :rtype: object
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Geofence.


        :param meta: The meta of this Geofence.  # noqa: E501
        :type: object
        """

        self._meta = meta

    @property
    def id(self):
        """Gets the id of this Geofence.  # noqa: E501


        :return: The id of this Geofence.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Geofence.


        :param id: The id of this Geofence.  # noqa: E501
        :type: float
        """

        self._id = id

    @property
    def device_id(self):
        """Gets the device_id of this Geofence.  # noqa: E501


        :return: The device_id of this Geofence.  # noqa: E501
        :rtype: float
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this Geofence.


        :param device_id: The device_id of this Geofence.  # noqa: E501
        :type: float
        """

        self._device_id = device_id

    @property
    def config_id(self):
        """Gets the config_id of this Geofence.  # noqa: E501


        :return: The config_id of this Geofence.  # noqa: E501
        :rtype: float
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """Sets the config_id of this Geofence.


        :param config_id: The config_id of this Geofence.  # noqa: E501
        :type: float
        """

        self._config_id = config_id

    @property
    def user_id(self):
        """Gets the user_id of this Geofence.  # noqa: E501


        :return: The user_id of this Geofence.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Geofence.


        :param user_id: The user_id of this Geofence.  # noqa: E501
        :type: float
        """

        self._user_id = user_id

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
        if issubclass(Geofence, dict):
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
        if not isinstance(other, Geofence):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Geofence):
            return True

        return self.to_dict() != other.to_dict()
