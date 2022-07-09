from enum import Enum


class StopPriceLinkType(Enum):
    """Represents the different stop price link type
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.utils.enums import StopPriceLinkType
        >>> StopPriceLinkType.Tick.value
    """

    Value = 'VALUE'
    Percent = 'PERCENT'
    Tick = 'TICK'
