from enum import Enum

from td.utils.utils import str_range


class ChartFutures(Enum):
    """Represents the different streaming chart
    futures fields.

    ### Usage
    ----
        >>> from td.utils.enums import ChartFutures
        >>> ChartFutures.All.value
    """

    All = str_range(7)
    Symbol = '0'
    ChartTime = '1'
    OpenPrice = '2'
    HighPrice = '3'
    LowPrice = '4'
    ClosePrice = '5'
    Volume = '6'
