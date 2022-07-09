from enum import Enum


class ActivesVenues(Enum):
    """Represents the different streaming actives
    venues.

    ### Usage
    ----
        >>> from td.utils.enums import ActivesVenues
        >>> ActivesVenues.NasdaqExchange.value
    """

    NasdaqExchange = 'NASDAQ'
    NewYorkStockExchange = 'NYSE'
    OverTheCounterBulletinBoard = 'OTCBB'
    Calls = 'CALLS'
    Puts = 'PUTS'
    Options = 'OPTS'
    CallsDesc = 'CALLS-DESC'
    PutsDesc = 'PUTS-DESC'
    OptionsDec = 'OPTS-DESC'
