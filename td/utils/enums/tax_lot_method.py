from enum import Enum


class TaxLotMethod(Enum):
    """Represents the different Tax Lot Methods
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.utils.enums import TaxLotMethod
        >>> TaxLotMethod.Fifo.value
    """

    Fifo = 'FIFO'
    Lifo = 'LIFO'
    HighCost = 'HIGH_COST'
    LowCost = 'LOW_COST'
    MinimumTax = 'MINIMUM_TAX'
    AverageCost = 'AVERAGE_COST'
    NoneSpecified = 'NONE'
