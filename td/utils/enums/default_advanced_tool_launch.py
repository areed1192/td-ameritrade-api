from enum import Enum


class DefaultAdvancedToolLaunch(Enum):
    """Represents the different Default Advanced Tool
    Lauch for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.utils.enums import DefaultAdvancedToolLaunch
        >>> DefaultAdvancedToolLaunch.Tos.value
    """

    Ta = 'Ta'
    No = 'N'
    Yes = 'Y'
    Tos = 'TOS'
    Cc2 = 'CC2'
    NoneSpecified = 'NONE'
