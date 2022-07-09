from enum import Enum


class PriceLinkBasis(Enum):
    """Represents the different price link basis
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.utils.enums import PriceLinkBasis
        >>> PriceLinkBasis.Manual.value
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
