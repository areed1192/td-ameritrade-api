from enum import Enum


class OrderTaxLotMethod(Enum):
    """Represents the different order tax lot methods
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.utils.enums import OrderTaxLotMethod
        >>> OrderTaxLotMethod.Fifo.value
    """

    Fifo = 'FIFO'
    Lifo = 'LIFO'
    HighCost = 'HIGH_COST'
    LowCost = 'LOW_COST'
    AverageCost = 'AVERAGE_COST'
    SpecificLot = 'SPECIFIC_LOT'
