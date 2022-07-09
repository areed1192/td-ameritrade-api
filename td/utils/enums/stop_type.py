from enum import Enum


class StopType(Enum):
    """Represents the different stop type
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.utils.enums import StopType
        >>> StopType.Standard.value
    """

    Standard = 'STANDARD'
    Bid = 'BID'
    Ask = 'ASK'
    Last = 'LAST'
    Mark = 'MARK'
