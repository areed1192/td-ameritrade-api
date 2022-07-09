from enum import Enum


class PeriodType(Enum):
    """Represents the different chart periods
    for the `PriceHistory` service.

    ### Usage
    ----
        >>> from td.utils.enums import PeriodType
        >>> PeriodType.Day.value
    """

    Day = 'day'
    Month = 'month'
    Year = 'year'
    YearToDate = 'ytd'
