from enum import Enum


class ChartFuturesFrequencies(Enum):
    """Represents the different frequencies for the
    Chart History Futures streaming service.

    ### Usage
    ----
        >>> from td.utils.enums import ChartFuturesFrequencies
        >>> ChartFuturesFrequencies.OneMinute.value
    """

    OneMinute = 'm1'
    FiveMinute = 'm5'
    TenMinute = 'm10'
    ThirtyMinute = 'm30'
    OneHour = 'h1'
    OneDay = 'd1'
    OneWeek = 'w1'
    OneMonth = 'n1'
