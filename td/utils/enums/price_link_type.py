from enum import Enum


class PriceLinkType(Enum):
    """Represents the different price link type
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.utils.enums import PriceLinkType
        >>> PriceLinkType.Value.value
    """

    Value = 'VALUE'
    Percent = 'PERCENT'
    Tick = 'TICK'
