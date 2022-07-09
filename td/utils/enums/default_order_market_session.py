from enum import Enum


class DefaultOrderMarketSession(Enum):
    """Represents the different Default Order Market Session
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.utils.enums import DefaultOrderMarketSession
        >>> DefaultOrderMarketSession.Am.value
    """

    Am = 'AM'
    Pm = 'PM'
    Normal = 'NORMAL'
    Seamless = 'SEAMLESS'
    NoneSpecified = 'NONE'
