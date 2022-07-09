from enum import Enum

from td.utils.utils import str_range


class LevelOneOptions(Enum):
    """Represents the different fields for the Level One
    Options Feed.

    ### Usage
    ----
        >>> from td.utils.enums import LevelOneOptions
        >>> LevelOneOptions.All.value
    """

    All = str_range(42)
    Symbol = '0'
    Description = '1'
    BidPrice = '2'
    AskPrice = '3'
    LastPrice = '4'
    HighPrice = '5'
    LowPrice = '6'
    ClosePrice = '7'
    TotalVolume = '8'
    OpenInterest = '9'
    Volatility = '10'
    QuoteTime = '11'
    TradeTime = '12'
    MoneyIntrinsicValue = '13'
    QuoteDay = '14'
    TradeDay = '15'
    ExpirationYear = '16'
    Multiplier = '17'
    Digits = '18'
    OpenPrice = '19'
    BidSize = '20'
    AskSize = '21'
    LastSize = '22'
    NetChange = '23'
    StrikePrice = '24'
    ContractType = '25'
    Underlying = '26'
    ExpirationMonth = '27'
    Deliverables = '28'
    TimeValue = '29'
    ExpirationDay = '30'
    DaysToExpiration = '31'
    Delta = '32'
    Gamma = '33'
    Theta = '34'
    Vega = '35'
    Rho = '36'
    SecurityStatus = '37'
    TheoreticalOptionValue = '38'
    UnderlyingPrice = '39'
    UvExpirationType = '40'
    Mark = '41'
