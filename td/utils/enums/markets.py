from enum import Enum


class Markets(Enum):
    """Represents the different markets you can request
    hours for the `MarketHours` service.

    ### Usage
    ----
        >>> from td.utils.enums import Markets
        >>> Markets.Bond.value
    """

    Bond = 'BOND'
    Equity = 'EQUITY'
    Option = 'OPTION'
    Forex = 'FOREX'
    Futures = 'FUTURES'
