from enum import Enum

from td.utils.utils import str_range


class LevelOneFuturesOptions(Enum):
    """
    Represents the different fields for the Level One Futures Options feed.

    ### Usage
    ----
        >>> from td.utils.enums import LevelOneFuturesOptions
        >>> LevelOneFuturesOptions.All.value
    """

    All = str_range(36)
    Symbol = '0'
    BidPrice = '1'
    AskPrice = '2'
    LastPrice = '3'
    BidSize = '4'
    AskSize = '5'
    AskId = '6'
    BidId = '7'
    TotalVolume = '8'
    LastSize = '9'
    QuoteTime = '10'
    TradeTime = '11'
    HighPrice = '12'
    LowPrice = '13'
    ClosePrice = '14'
    ExchangeId = '15'
    Description = '16'
    LastId = '17'
    OpenPrice = '18'
    NetChange = '19'
    FuturePercentChange = '20'
    ExchangeName = '21'
    SecurityStatus = '22'
    OpenInterest = '23'
    Mark = '24'
    Tick = '25'
    TickAmount = '26'
    Product = '27'
    FuturePriceFormat = '28'
    FutureTradingHours = '29'
    FutureIsTradeable = '30'
    FutureMultiplier = '31'
    FutureIsActive = '32'
    FutureSettlementPrice = '33'
    FutureActiveSymbol = '34'
    FutureExpirationDate = '35'
