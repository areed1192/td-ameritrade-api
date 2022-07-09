from enum import Enum


class AuthTokenTimeout(Enum):
    """Represents the different Auth Token Timeout
    properties for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.utils.enums import AuthTokenTimeout
        >>> AuthTokenTimeout.FiftyFiveMinutes.value
    """

    FiftyFiveMinutes = 'FIFTY_FIVE_MINUTES'
    TwoHours = 'TWO_HOURS'
    FourHours = 'FOUR_HOURS'
    EightHours = 'EIGHT_HOURS'
