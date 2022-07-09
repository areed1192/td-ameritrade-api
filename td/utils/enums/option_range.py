from enum import Enum


class OptionRange(Enum):
    """Represents the different option range types
    when querying the `OptionChain` service.

    ### Usage
    ----
        >>> from td.utils.enums import OptionRange
        >>> OptionRange.InTheMoney.value
    """

    All = 'ALL'
    InTheMoney = 'ITM'
    NearTheMoney = 'NTM'
    OutTheMoney = 'OTM'
    StrikesAboveMarket = 'SAK'
    StrikesBelowMarket = 'SBK'
    StrikesNearMarket = 'SNK'
