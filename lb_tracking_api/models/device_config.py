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


class DeviceConfig(dict):
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
        'current_fw': 'str',
        'ota_fw': 'str',
        'interval': 'float',
        'sleep_interval': 'float',
        'check_in_interval': 'float',
        'packing': 'float',
        'movement_sensitivity': 'float',
        'debounce': 'float',
        'movement_sensitivity2': 'float',
        'behavior': 'float',
        'mode_control': 'float',
        'gps_timeout': 'float',
        'transmit_timeout': 'float',
        'gps_stabilize': 'float',
        'gps_check_interval': 'float',
        'stop_timeout': 'float',
        'tolerance_percentage': 'float',
        'reasons_to_wake': 'list[object]',
        'modified': 'datetime',
        'force_fw': 'bool',
        'received_at': 'datetime',
        'reset': 'float',
        'flash_try_count': 'float',
        'home_wifi_network': 'str',
        'home_wifi_password': 'str',
        'wake_action': 'str',
        'on_demand_time': 'float',
        'alert_action': 'str',
        'id': 'float',
        'device_id': 'float',
        'safe_zone_id': 'float'
    }

    attribute_map = {
        'current_fw': 'currentFW',
        'ota_fw': 'otaFW',
        'interval': 'interval',
        'sleep_interval': 'sleepInterval',
        'check_in_interval': 'checkInInterval',
        'packing': 'packing',
        'movement_sensitivity': 'movementSensitivity',
        'debounce': 'debounce',
        'movement_sensitivity2': 'movementSensitivity2',
        'behavior': 'behavior',
        'mode_control': 'modeControl',
        'gps_timeout': 'gpsTimeout',
        'transmit_timeout': 'transmitTimeout',
        'gps_stabilize': 'gpsStabilize',
        'gps_check_interval': 'gpsCheckInterval',
        'stop_timeout': 'stopTimeout',
        'tolerance_percentage': 'tolerancePercentage',
        'reasons_to_wake': 'reasonsToWake',
        'modified': 'modified',
        'force_fw': 'forceFw',
        'received_at': 'receivedAt',
        'reset': 'reset',
        'flash_try_count': 'flashTryCount',
        'home_wifi_network': 'homeWifiNetwork',
        'home_wifi_password': 'homeWifiPassword',
        'wake_action': 'wakeAction',
        'on_demand_time': 'onDemandTime',
        'alert_action': 'alertAction',
        'id': 'id',
        'device_id': 'deviceId',
        'safe_zone_id': 'safeZoneId'
    }

    def __init__(self, current_fw=None, ota_fw=None, interval=None, sleep_interval=None, check_in_interval=None, packing=None, movement_sensitivity=None, debounce=None, movement_sensitivity2=None, behavior=None, mode_control=None, gps_timeout=None, transmit_timeout=None, gps_stabilize=None, gps_check_interval=None, stop_timeout=None, tolerance_percentage=None, reasons_to_wake=None, modified=None, force_fw=False, received_at=None, reset=None, flash_try_count=None, home_wifi_network=None, home_wifi_password=None, wake_action='normal', on_demand_time=None, alert_action='nothing', id=None, device_id=None, safe_zone_id=None):  # noqa: E501
        """DeviceConfig - a model defined in Swagger"""  # noqa: E501

        self._current_fw = None
        self._ota_fw = None
        self._interval = None
        self._sleep_interval = None
        self._check_in_interval = None
        self._packing = None
        self._movement_sensitivity = None
        self._debounce = None
        self._movement_sensitivity2 = None
        self._behavior = None
        self._mode_control = None
        self._gps_timeout = None
        self._transmit_timeout = None
        self._gps_stabilize = None
        self._gps_check_interval = None
        self._stop_timeout = None
        self._tolerance_percentage = None
        self._reasons_to_wake = None
        self._modified = None
        self._force_fw = None
        self._received_at = None
        self._reset = None
        self._flash_try_count = None
        self._home_wifi_network = None
        self._home_wifi_password = None
        self._wake_action = None
        self._on_demand_time = None
        self._alert_action = None
        self._id = None
        self._device_id = None
        self._safe_zone_id = None
        self.discriminator = None

        if current_fw is not None:
            self.current_fw = current_fw
        if ota_fw is not None:
            self.ota_fw = ota_fw
        self.interval = interval
        self.sleep_interval = sleep_interval
        self.check_in_interval = check_in_interval
        self.packing = packing
        if movement_sensitivity is not None:
            self.movement_sensitivity = movement_sensitivity
        if debounce is not None:
            self.debounce = debounce
        if movement_sensitivity2 is not None:
            self.movement_sensitivity2 = movement_sensitivity2
        if behavior is not None:
            self.behavior = behavior
        if mode_control is not None:
            self.mode_control = mode_control
        if gps_timeout is not None:
            self.gps_timeout = gps_timeout
        if transmit_timeout is not None:
            self.transmit_timeout = transmit_timeout
        if gps_stabilize is not None:
            self.gps_stabilize = gps_stabilize
        if gps_check_interval is not None:
            self.gps_check_interval = gps_check_interval
        if stop_timeout is not None:
            self.stop_timeout = stop_timeout
        if tolerance_percentage is not None:
            self.tolerance_percentage = tolerance_percentage
        if reasons_to_wake is not None:
            self.reasons_to_wake = reasons_to_wake
        if modified is not None:
            self.modified = modified
        if force_fw is not None:
            self.force_fw = force_fw
        if received_at is not None:
            self.received_at = received_at
        if reset is not None:
            self.reset = reset
        if flash_try_count is not None:
            self.flash_try_count = flash_try_count
        if home_wifi_network is not None:
            self.home_wifi_network = home_wifi_network
        if home_wifi_password is not None:
            self.home_wifi_password = home_wifi_password
        self.wake_action = wake_action
        self.on_demand_time = on_demand_time
        self.alert_action = alert_action
        if id is not None:
            self.id = id
        if device_id is not None:
            self.device_id = device_id
        if safe_zone_id is not None:
            self.safe_zone_id = safe_zone_id

    @property
    def current_fw(self):
        """Gets the current_fw of this DeviceConfig.  # noqa: E501

        Current Firmware version  # noqa: E501

        :return: The current_fw of this DeviceConfig.  # noqa: E501
        :rtype: str
        """
        return self._current_fw

    @current_fw.setter
    def current_fw(self, current_fw):
        """Sets the current_fw of this DeviceConfig.

        Current Firmware version  # noqa: E501

        :param current_fw: The current_fw of this DeviceConfig.  # noqa: E501
        :type: str
        """

        self._current_fw = current_fw

    @property
    def ota_fw(self):
        """Gets the ota_fw of this DeviceConfig.  # noqa: E501

        Pending Firmware version. If non null, the unit will be told to upgrade to this version when it next transmits in sleep mode.  # noqa: E501

        :return: The ota_fw of this DeviceConfig.  # noqa: E501
        :rtype: str
        """
        return self._ota_fw

    @ota_fw.setter
    def ota_fw(self, ota_fw):
        """Sets the ota_fw of this DeviceConfig.

        Pending Firmware version. If non null, the unit will be told to upgrade to this version when it next transmits in sleep mode.  # noqa: E501

        :param ota_fw: The ota_fw of this DeviceConfig.  # noqa: E501
        :type: str
        """

        self._ota_fw = ota_fw

    @property
    def interval(self):
        """Gets the interval of this DeviceConfig.  # noqa: E501

        The wake mode interval in seconds. The unit will connect to the server this often when awake.  # noqa: E501

        :return: The interval of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this DeviceConfig.

        The wake mode interval in seconds. The unit will connect to the server this often when awake.  # noqa: E501

        :param interval: The interval of this DeviceConfig.  # noqa: E501
        :type: float
        """
        if interval is None:
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501

        self._interval = interval

    @property
    def sleep_interval(self):
        """Gets the sleep_interval of this DeviceConfig.  # noqa: E501

        Sleep mode interval in seconds. The unit will try to connect this often to the server when asleep  # noqa: E501

        :return: The sleep_interval of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._sleep_interval

    @sleep_interval.setter
    def sleep_interval(self, sleep_interval):
        """Sets the sleep_interval of this DeviceConfig.

        Sleep mode interval in seconds. The unit will try to connect this often to the server when asleep  # noqa: E501

        :param sleep_interval: The sleep_interval of this DeviceConfig.  # noqa: E501
        :type: float
        """
        if sleep_interval is None:
            raise ValueError("Invalid value for `sleep_interval`, must not be `None`")  # noqa: E501

        self._sleep_interval = sleep_interval

    @property
    def check_in_interval(self):
        """Gets the check_in_interval of this DeviceConfig.  # noqa: E501

        Internal Use. A failsafe to ensure the unit connects to the server at least this often.  # noqa: E501

        :return: The check_in_interval of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._check_in_interval

    @check_in_interval.setter
    def check_in_interval(self, check_in_interval):
        """Sets the check_in_interval of this DeviceConfig.

        Internal Use. A failsafe to ensure the unit connects to the server at least this often.  # noqa: E501

        :param check_in_interval: The check_in_interval of this DeviceConfig.  # noqa: E501
        :type: float
        """
        if check_in_interval is None:
            raise ValueError("Invalid value for `check_in_interval`, must not be `None`")  # noqa: E501

        self._check_in_interval = check_in_interval

    @property
    def packing(self):
        """Gets the packing of this DeviceConfig.  # noqa: E501

        The number of GPS points to send with each transmission. A packing setting of 3 with an 'interval' of 60s will result in points recorded approximately every 20s, but they will only be sent together. This increases the time you have to wait for locations to come through to the server but improves battery life  # noqa: E501

        :return: The packing of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._packing

    @packing.setter
    def packing(self, packing):
        """Sets the packing of this DeviceConfig.

        The number of GPS points to send with each transmission. A packing setting of 3 with an 'interval' of 60s will result in points recorded approximately every 20s, but they will only be sent together. This increases the time you have to wait for locations to come through to the server but improves battery life  # noqa: E501

        :param packing: The packing of this DeviceConfig.  # noqa: E501
        :type: float
        """
        if packing is None:
            raise ValueError("Invalid value for `packing`, must not be `None`")  # noqa: E501

        self._packing = packing

    @property
    def movement_sensitivity(self):
        """Gets the movement_sensitivity of this DeviceConfig.  # noqa: E501

        Deprecated. See debounce.  # noqa: E501

        :return: The movement_sensitivity of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._movement_sensitivity

    @movement_sensitivity.setter
    def movement_sensitivity(self, movement_sensitivity):
        """Sets the movement_sensitivity of this DeviceConfig.

        Deprecated. See debounce.  # noqa: E501

        :param movement_sensitivity: The movement_sensitivity of this DeviceConfig.  # noqa: E501
        :type: float
        """

        self._movement_sensitivity = movement_sensitivity

    @property
    def debounce(self):
        """Gets the debounce of this DeviceConfig.  # noqa: E501

        Movement sensitivity on a scale of 1 to 10, with 1 being the most sensitive. It is correlated to the number of consecutive milliseconds the acceleration needs to exceed the movementSensitivity threshold  # noqa: E501

        :return: The debounce of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._debounce

    @debounce.setter
    def debounce(self, debounce):
        """Sets the debounce of this DeviceConfig.

        Movement sensitivity on a scale of 1 to 10, with 1 being the most sensitive. It is correlated to the number of consecutive milliseconds the acceleration needs to exceed the movementSensitivity threshold  # noqa: E501

        :param debounce: The debounce of this DeviceConfig.  # noqa: E501
        :type: float
        """

        self._debounce = debounce

    @property
    def movement_sensitivity2(self):
        """Gets the movement_sensitivity2 of this DeviceConfig.  # noqa: E501

        A secondary debounce value. Typically this value is lower or equal to debounce, representing increased sensitivity to movement once the device is already moving.  # noqa: E501

        :return: The movement_sensitivity2 of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._movement_sensitivity2

    @movement_sensitivity2.setter
    def movement_sensitivity2(self, movement_sensitivity2):
        """Sets the movement_sensitivity2 of this DeviceConfig.

        A secondary debounce value. Typically this value is lower or equal to debounce, representing increased sensitivity to movement once the device is already moving.  # noqa: E501

        :param movement_sensitivity2: The movement_sensitivity2 of this DeviceConfig.  # noqa: E501
        :type: float
        """

        self._movement_sensitivity2 = movement_sensitivity2

    @property
    def behavior(self):
        """Gets the behavior of this DeviceConfig.  # noqa: E501

        Char Bitfield with various flags. Advanced use only.  DisableBluetooth:32 |  Encrypt:128 |  GsmOnWhenAwake:1 |  GsmOnWhenAsleep:2 |  GpsOnWhenAwake:4 |  DisableWifiAccuracyAssist:8 |  RepeatSleep:16 |  DisableWifi:64  # noqa: E501

        :return: The behavior of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._behavior

    @behavior.setter
    def behavior(self, behavior):
        """Sets the behavior of this DeviceConfig.

        Char Bitfield with various flags. Advanced use only.  DisableBluetooth:32 |  Encrypt:128 |  GsmOnWhenAwake:1 |  GsmOnWhenAsleep:2 |  GpsOnWhenAwake:4 |  DisableWifiAccuracyAssist:8 |  RepeatSleep:16 |  DisableWifi:64  # noqa: E501

        :param behavior: The behavior of this DeviceConfig.  # noqa: E501
        :type: float
        """

        self._behavior = behavior

    @property
    def mode_control(self):
        """Gets the mode_control of this DeviceConfig.  # noqa: E501

        Char Bitfield with various flags. Advanced use only.  StartStopOnly:1 |  LockAwakeOnAlert:2 |  SendSleepLocAfterBtDisconnect:4 |   # noqa: E501

        :return: The mode_control of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._mode_control

    @mode_control.setter
    def mode_control(self, mode_control):
        """Sets the mode_control of this DeviceConfig.

        Char Bitfield with various flags. Advanced use only.  StartStopOnly:1 |  LockAwakeOnAlert:2 |  SendSleepLocAfterBtDisconnect:4 |   # noqa: E501

        :param mode_control: The mode_control of this DeviceConfig.  # noqa: E501
        :type: float
        """

        self._mode_control = mode_control

    @property
    def gps_timeout(self):
        """Gets the gps_timeout of this DeviceConfig.  # noqa: E501

        How long to let the GPS searches for a lock in seconds before giving up. Max 255s.  # noqa: E501

        :return: The gps_timeout of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._gps_timeout

    @gps_timeout.setter
    def gps_timeout(self, gps_timeout):
        """Sets the gps_timeout of this DeviceConfig.

        How long to let the GPS searches for a lock in seconds before giving up. Max 255s.  # noqa: E501

        :param gps_timeout: The gps_timeout of this DeviceConfig.  # noqa: E501
        :type: float
        """

        self._gps_timeout = gps_timeout

    @property
    def transmit_timeout(self):
        """Gets the transmit_timeout of this DeviceConfig.  # noqa: E501

        When the unit first wakes up from sleep, how long to wait before trying to transmit in multiples of 30 seconds. 0 = instant, 1 = 30s, 2 = 60s...   Useful to avoid detection or draining battery inside shielded buildings.  # noqa: E501

        :return: The transmit_timeout of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._transmit_timeout

    @transmit_timeout.setter
    def transmit_timeout(self, transmit_timeout):
        """Sets the transmit_timeout of this DeviceConfig.

        When the unit first wakes up from sleep, how long to wait before trying to transmit in multiples of 30 seconds. 0 = instant, 1 = 30s, 2 = 60s...   Useful to avoid detection or draining battery inside shielded buildings.  # noqa: E501

        :param transmit_timeout: The transmit_timeout of this DeviceConfig.  # noqa: E501
        :type: float
        """

        self._transmit_timeout = transmit_timeout

    @property
    def gps_stabilize(self):
        """Gets the gps_stabilize of this DeviceConfig.  # noqa: E501

        How long to let the GPS stabilise in seconds once a lock is achieved before sending the position. Higher values may increase accuracy.  # noqa: E501

        :return: The gps_stabilize of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._gps_stabilize

    @gps_stabilize.setter
    def gps_stabilize(self, gps_stabilize):
        """Sets the gps_stabilize of this DeviceConfig.

        How long to let the GPS stabilise in seconds once a lock is achieved before sending the position. Higher values may increase accuracy.  # noqa: E501

        :param gps_stabilize: The gps_stabilize of this DeviceConfig.  # noqa: E501
        :type: float
        """

        self._gps_stabilize = gps_stabilize

    @property
    def gps_check_interval(self):
        """Gets the gps_check_interval of this DeviceConfig.  # noqa: E501

        If a safe-zone is used, how often to check the wifi & gps to see if its still inside it (only applies when motion is detected)  # noqa: E501

        :return: The gps_check_interval of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._gps_check_interval

    @gps_check_interval.setter
    def gps_check_interval(self, gps_check_interval):
        """Sets the gps_check_interval of this DeviceConfig.

        If a safe-zone is used, how often to check the wifi & gps to see if its still inside it (only applies when motion is detected)  # noqa: E501

        :param gps_check_interval: The gps_check_interval of this DeviceConfig.  # noqa: E501
        :type: float
        """

        self._gps_check_interval = gps_check_interval

    @property
    def stop_timeout(self):
        """Gets the stop_timeout of this DeviceConfig.  # noqa: E501

        The total amount of time in seconds the unit has to be stationary for before deeming the journey over and switching to sleep mode  # noqa: E501

        :return: The stop_timeout of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._stop_timeout

    @stop_timeout.setter
    def stop_timeout(self, stop_timeout):
        """Sets the stop_timeout of this DeviceConfig.

        The total amount of time in seconds the unit has to be stationary for before deeming the journey over and switching to sleep mode  # noqa: E501

        :param stop_timeout: The stop_timeout of this DeviceConfig.  # noqa: E501
        :type: float
        """

        self._stop_timeout = stop_timeout

    @property
    def tolerance_percentage(self):
        """Gets the tolerance_percentage of this DeviceConfig.  # noqa: E501

        Reserved for internal use.  # noqa: E501

        :return: The tolerance_percentage of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._tolerance_percentage

    @tolerance_percentage.setter
    def tolerance_percentage(self, tolerance_percentage):
        """Sets the tolerance_percentage of this DeviceConfig.

        Reserved for internal use.  # noqa: E501

        :param tolerance_percentage: The tolerance_percentage of this DeviceConfig.  # noqa: E501
        :type: float
        """

        self._tolerance_percentage = tolerance_percentage

    @property
    def reasons_to_wake(self):
        """Gets the reasons_to_wake of this DeviceConfig.  # noqa: E501


        :return: The reasons_to_wake of this DeviceConfig.  # noqa: E501
        :rtype: list[object]
        """
        return self._reasons_to_wake

    @reasons_to_wake.setter
    def reasons_to_wake(self, reasons_to_wake):
        """Sets the reasons_to_wake of this DeviceConfig.


        :param reasons_to_wake: The reasons_to_wake of this DeviceConfig.  # noqa: E501
        :type: list[object]
        """

        self._reasons_to_wake = reasons_to_wake

    @property
    def modified(self):
        """Gets the modified of this DeviceConfig.  # noqa: E501

        Set to any non null date to indicate the configuration should be pushed to the device when it next connects  # noqa: E501

        :return: The modified of this DeviceConfig.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this DeviceConfig.

        Set to any non null date to indicate the configuration should be pushed to the device when it next connects  # noqa: E501

        :param modified: The modified of this DeviceConfig.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def force_fw(self):
        """Gets the force_fw of this DeviceConfig.  # noqa: E501

        Internal use.   Used with otaFW. Set to true to force the unit to upgrade on next connection (rather than waiting for a sleep connection  # noqa: E501

        :return: The force_fw of this DeviceConfig.  # noqa: E501
        :rtype: bool
        """
        return self._force_fw

    @force_fw.setter
    def force_fw(self, force_fw):
        """Sets the force_fw of this DeviceConfig.

        Internal use.   Used with otaFW. Set to true to force the unit to upgrade on next connection (rather than waiting for a sleep connection  # noqa: E501

        :param force_fw: The force_fw of this DeviceConfig.  # noqa: E501
        :type: bool
        """

        self._force_fw = force_fw

    @property
    def received_at(self):
        """Gets the received_at of this DeviceConfig.  # noqa: E501

        Indicates the last time the settings were sent to the device  # noqa: E501

        :return: The received_at of this DeviceConfig.  # noqa: E501
        :rtype: datetime
        """
        return self._received_at

    @received_at.setter
    def received_at(self, received_at):
        """Sets the received_at of this DeviceConfig.

        Indicates the last time the settings were sent to the device  # noqa: E501

        :param received_at: The received_at of this DeviceConfig.  # noqa: E501
        :type: datetime
        """

        self._received_at = received_at

    @property
    def reset(self):
        """Gets the reset of this DeviceConfig.  # noqa: E501

        Non NULL values cause unit to restart on next connection   0 = Normal reboot   1 = Clear settings cache and restart   2 = Clear cache and bluetooth connection data, then restart  # noqa: E501

        :return: The reset of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._reset

    @reset.setter
    def reset(self, reset):
        """Sets the reset of this DeviceConfig.

        Non NULL values cause unit to restart on next connection   0 = Normal reboot   1 = Clear settings cache and restart   2 = Clear cache and bluetooth connection data, then restart  # noqa: E501

        :param reset: The reset of this DeviceConfig.  # noqa: E501
        :type: float
        """

        self._reset = reset

    @property
    def flash_try_count(self):
        """Gets the flash_try_count of this DeviceConfig.  # noqa: E501

        Internal use. Set to 0 when changing otaFW  # noqa: E501

        :return: The flash_try_count of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._flash_try_count

    @flash_try_count.setter
    def flash_try_count(self, flash_try_count):
        """Sets the flash_try_count of this DeviceConfig.

        Internal use. Set to 0 when changing otaFW  # noqa: E501

        :param flash_try_count: The flash_try_count of this DeviceConfig.  # noqa: E501
        :type: float
        """

        self._flash_try_count = flash_try_count

    @property
    def home_wifi_network(self):
        """Gets the home_wifi_network of this DeviceConfig.  # noqa: E501

        WiFi network name to use as a Safe-zone. When this network is visible, stay asleep  # noqa: E501

        :return: The home_wifi_network of this DeviceConfig.  # noqa: E501
        :rtype: str
        """
        return self._home_wifi_network

    @home_wifi_network.setter
    def home_wifi_network(self, home_wifi_network):
        """Sets the home_wifi_network of this DeviceConfig.

        WiFi network name to use as a Safe-zone. When this network is visible, stay asleep  # noqa: E501

        :param home_wifi_network: The home_wifi_network of this DeviceConfig.  # noqa: E501
        :type: str
        """
        if home_wifi_network is not None and len(home_wifi_network) > 127:
            raise ValueError("Invalid value for `home_wifi_network`, length must be less than or equal to `127`")  # noqa: E501

        self._home_wifi_network = home_wifi_network

    @property
    def home_wifi_password(self):
        """Gets the home_wifi_password of this DeviceConfig.  # noqa: E501

        WiFi network paswword. If set enables transmission over WiFi.  # noqa: E501

        :return: The home_wifi_password of this DeviceConfig.  # noqa: E501
        :rtype: str
        """
        return self._home_wifi_password

    @home_wifi_password.setter
    def home_wifi_password(self, home_wifi_password):
        """Sets the home_wifi_password of this DeviceConfig.

        WiFi network paswword. If set enables transmission over WiFi.  # noqa: E501

        :param home_wifi_password: The home_wifi_password of this DeviceConfig.  # noqa: E501
        :type: str
        """
        if home_wifi_password is not None and len(home_wifi_password) > 127:
            raise ValueError("Invalid value for `home_wifi_password`, length must be less than or equal to `127`")  # noqa: E501

        self._home_wifi_password = home_wifi_password

    @property
    def wake_action(self):
        """Gets the wake_action of this DeviceConfig.  # noqa: E501

        What to do when the unit wakes up (ie is moved and not in a safe-zone). Options are 'available' (lost and found), and 'normal' (tracking)  # noqa: E501

        :return: The wake_action of this DeviceConfig.  # noqa: E501
        :rtype: str
        """
        return self._wake_action

    @wake_action.setter
    def wake_action(self, wake_action):
        """Sets the wake_action of this DeviceConfig.

        What to do when the unit wakes up (ie is moved and not in a safe-zone). Options are 'available' (lost and found), and 'normal' (tracking)  # noqa: E501

        :param wake_action: The wake_action of this DeviceConfig.  # noqa: E501
        :type: str
        """
        if wake_action is None:
            raise ValueError("Invalid value for `wake_action`, must not be `None`")  # noqa: E501

        self._wake_action = wake_action

    @property
    def on_demand_time(self):
        """Gets the on_demand_time of this DeviceConfig.  # noqa: E501

        Deprecated  # noqa: E501

        :return: The on_demand_time of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._on_demand_time

    @on_demand_time.setter
    def on_demand_time(self, on_demand_time):
        """Sets the on_demand_time of this DeviceConfig.

        Deprecated  # noqa: E501

        :param on_demand_time: The on_demand_time of this DeviceConfig.  # noqa: E501
        :type: float
        """
        if on_demand_time is None:
            raise ValueError("Invalid value for `on_demand_time`, must not be `None`")  # noqa: E501

        self._on_demand_time = on_demand_time

    @property
    def alert_action(self):
        """Gets the alert_action of this DeviceConfig.  # noqa: E501

        What to do when the button is pressed or the unit is dropped. Options are 'available' (stay registered on the mobile network), 'nothing' (one transmission) and  'lockOn' (keep transmitting at 'interval' until instructed otherwise  # noqa: E501

        :return: The alert_action of this DeviceConfig.  # noqa: E501
        :rtype: str
        """
        return self._alert_action

    @alert_action.setter
    def alert_action(self, alert_action):
        """Sets the alert_action of this DeviceConfig.

        What to do when the button is pressed or the unit is dropped. Options are 'available' (stay registered on the mobile network), 'nothing' (one transmission) and  'lockOn' (keep transmitting at 'interval' until instructed otherwise  # noqa: E501

        :param alert_action: The alert_action of this DeviceConfig.  # noqa: E501
        :type: str
        """
        if alert_action is None:
            raise ValueError("Invalid value for `alert_action`, must not be `None`")  # noqa: E501

        self._alert_action = alert_action

    @property
    def id(self):
        """Gets the id of this DeviceConfig.  # noqa: E501


        :return: The id of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceConfig.


        :param id: The id of this DeviceConfig.  # noqa: E501
        :type: float
        """

        self._id = id

    @property
    def device_id(self):
        """Gets the device_id of this DeviceConfig.  # noqa: E501


        :return: The device_id of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DeviceConfig.


        :param device_id: The device_id of this DeviceConfig.  # noqa: E501
        :type: float
        """

        self._device_id = device_id

    @property
    def safe_zone_id(self):
        """Gets the safe_zone_id of this DeviceConfig.  # noqa: E501


        :return: The safe_zone_id of this DeviceConfig.  # noqa: E501
        :rtype: float
        """
        return self._safe_zone_id

    @safe_zone_id.setter
    def safe_zone_id(self, safe_zone_id):
        """Sets the safe_zone_id of this DeviceConfig.


        :param safe_zone_id: The safe_zone_id of this DeviceConfig.  # noqa: E501
        :type: float
        """

        self._safe_zone_id = safe_zone_id

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
        if issubclass(DeviceConfig, dict):
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
        if not isinstance(other, DeviceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other