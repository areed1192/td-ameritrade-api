from enum import Enum


class QuantityType(Enum):
    """Represents the different order quantity types
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.utils.enums import QuantityType
        >>> QuantityType.Dollars.value
    """

    AllShares = 'ALL_SHARES'
    Dollars = 'DOLLARS'
    Shares = 'SHARES'
