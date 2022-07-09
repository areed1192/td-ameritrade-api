from enum import Enum


class StopPriceLinkBasis(Enum):
    """Represents the different stop price link basis
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.utils.enums import StopPriceLinkBasis
        >>> StopPriceLinkBasis.Trigger.value
    """

    Manual = 'MANUAL'
    Base = 'BASE'
    Trigger = 'TRIGGER'
    Last = 'LAST'
    Bid = 'BID'
    Ask = 'ASK'
    AskBid = 'ASK_BID'
    Mark = 'MARK'
    Average = 'AVERAGE'
