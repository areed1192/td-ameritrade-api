from enum import Enum

from td.utils.utils import str_range


class LevelOneQuotes(Enum):
    """Represents the different fields for the Level One
    Quotes Feed.

    ### Usage
    ----
        >>> from td.utils.enums import LevelOneQuotes
        >>> LevelOneQuotes.All.value
    """

    All = str_range(53)
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
    TradeTime = '10'
    QuoteTime = '11'
    HighPrice = '12'
    LowPrice = '13'
    BidTick = '14'
    ClosePrice = '15'
    ExchangeId = '16'
    Marginable = '17'
    Shortable = '18'
    IslandBid = '19'
    IslandAsk = '20'
    IslandVolume = '21'
    QuoteDay = '22'
    TradeDay = '23'
    Volatility = '24'
    Description = '25'
    LastId = '26'
    Digits = '27'
    OpenPrice = '28'
    NetChange = '29'
    FiftyTwoWeekHigh = '30'
    FiftyTwoWeekLow = '31'
    PeRatio = '32'
    DividendAmount = '33'
    DividendYield = '34'
    IslandBidSize = '35'
    IslandAskSize = '36'
    Nav = '37'
    FundPrice = '38'
    ExchangeName = '39'
    DividendDate = '40'
    RegularMarketQuote = '41'
    RegularMarketTrade = '42'
    RegularMarketLastPrice = '43'
    RegularMarketLastSize = '44'
    RegularMarketTradeTime = '45'
    RegularMarketTradeDay = '46'
    RegularMarketNetChange = '47'
    SecurityStatus = '48'
    Mark = '49'
    QuoteTimeInLong = '50'
    TradeTimeInLong = '51'
    RegularMarketTradeTimeInLong = '52'
