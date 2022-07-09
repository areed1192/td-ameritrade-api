from enum import Enum

from td.utils.utils import str_range


class LevelOneForex(Enum):
    """Represents the different fields for the Level One
    Forex Feed.

    ### Usage
    ----
        >>> from td.utils.enums import LevelOneForex
        >>> LevelOneForex.All.value
    """

    All = str_range(30)
    Symbol = '0'
    BidPrice = '1'
    AskPrice = '2'
    LastPrice = '3'
    BidSize = '4'
    AskSize = '5'
    TotalVolume = '6'
    LastSize = '7'
    QuoteTime = '8'
    TradeTime = '9'
    HighPrice = '10'
    LowPrice = '11'
    ClosePrice = '12'
    ExchangeId = '13'
    Description = '14'
    OpenPrice = '15'
    NetChange = '16'
    PercentChange = '17'
    ExchangeName = '18'
    Digits = '19'
    SecurityStatus = '20'
    Tick = '21'
    TickAmount = '22'
    Product = '23'
    TradingHours = '24'
    IsTradable = '25'
    MarketMaker = '26'
    FiftyTwoWeekHigh = '27'
    FiftyTwoWeekLow = '28'
    Mark = '29'
