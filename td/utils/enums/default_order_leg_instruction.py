from enum import Enum


class DefaultOrderLegInstruction(Enum):
    """Represents the different Default Order Leg Instructions
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.utils.enums import DefaultOrderLegInstruction
        >>> DefaultOrderLegInstruction.Sell.value
    """

    Buy = 'BUY'
    Sell = 'SELL'
    BuyToCover = 'BUY_TO_COVER'
    SellShort = 'SELL_SHORT'
    NoneSpecified = 'NONE'
