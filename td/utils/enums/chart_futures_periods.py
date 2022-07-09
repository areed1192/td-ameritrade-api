from enum import Enum


class ChartFuturesPeriods(Enum):
    """Represents the different periods for the
    Chart History Futures streaming service.

    ### Usage
    ----
        >>> from td.utils.enums import ChartFuturesPeriods
        >>> ChartFuturesPeriods.OneDay.value
    """

    OneDay = 'd1'
    FiveDay = 'd5'
    FourWeeks = 'w4'
    TenMonths = 'n10'
    OneYear = 'y1'
    TenYear = 'y10'
