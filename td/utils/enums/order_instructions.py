from enum import Enum


class OrderInstructions(Enum):
    """Represents the different order instructions
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.utils.enums import OrderInstructions
        >>> OrderInstructions.SellShort.value
    """

    Buy = 'BUY'
    Sell = 'SELL'
    BuyToCover = 'BUY_TO_COVER'
    SellShort = 'SELL_SHORT'
    BuyToOpen = 'BUY_TO_OPEN'
    BuyToClose = 'BUY_TO_CLOSE'
    SellToOpen = 'SELL_TO_OPEN'
    SellToClose = 'SELL_TO_CLOSE'
    Exchange = 'EXCHANGE'
