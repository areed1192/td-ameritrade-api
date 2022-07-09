from enum import Enum


class TimesaleServices(Enum):
    """Represents the different streaming timesale
    services.

    ### Usage
    ----
        >>> from td.utils.enums import TimesaleServices
        >>> TimesaleServices.TimesaleEquity.value
    """

    TimesaleEquity = 'TIMESALE_EQUITY'
    TimesaleForex = 'TIMESALE_FOREX'
    TimesaleFutures = 'TIMESALE_FUTURES'
    TimesaleOptions = 'TIMESALE_OPTIONS'
