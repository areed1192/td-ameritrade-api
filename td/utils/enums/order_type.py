from enum import Enum


class OrderType(Enum):
    """Represents the different order type
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.utils.enums import OrderType
        >>> OrderType.Market.value
    """

    Market = 'MARKET'
    Limit = 'LIMIT'
    Stop = 'STOP'
    StopLimit = 'STOP_LIMIT'
    TrailingStop = 'TRAILING_STOP'
    MarketOnClose = 'MARKET_ON_CLOSE'
    Exercise = 'EXERCISE'
    TrailingStopLimit = 'TRAILING_STOP_LIMIT'
    NetDebit = 'NET_DEBIT'
    NetCredit = 'NET_CREDIT'
    NetZero = 'NET_ZERO'
