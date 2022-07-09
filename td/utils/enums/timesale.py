from enum import Enum

from td.utils.utils import str_range


class Timesale(Enum):
    """Represents the different streaming timesale
    fields.

    ### Usage
    ----
        >>> from td.utils.enums import Timesale
        >>> Timesale.All.value
    """

    All = str_range(5)
    Symbol = '0'
    TradeTime = '1'
    LastPrice = '2'
    LastSize = '3'
    LastSequence = '4'
