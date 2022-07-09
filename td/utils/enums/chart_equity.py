from enum import Enum

from td.utils.utils import str_range


class ChartEquity(Enum):
    """Represents the different streaming chart
    equity fields.

    ### Usage
    ----
        >>> from td.utils.enums import ChartEquity
        >>> ChartEquity.All.value
    """

    All = str_range(9)
    Symbol = '0'
    OpenPrice = '1'
    HighPrice = '2'
    LowPrice = '3'
    Close_Price = '4'
    Volume = '5'
    Sequence = '6'
    Chart_Time = '7'
    Chart_Day = '8'
