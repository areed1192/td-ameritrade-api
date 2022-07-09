from enum import Enum


class DefaultOrderType(Enum):
    """Represents the different Default Order Type
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.utils.enums import DefaultOrderType
        >>> DefaultOrderType.Market.value
    """

    Market = 'MARKET'
    Limit = 'LIMIT'
    Stop = 'STOP'
    StopLimit = 'STOP_LIMIT'
    TrailingStop = 'TRAILING_STOP'
    MarketOnClose = 'MARKET_ON_CLOSE'
    NoneSpecified = 'NONE'
