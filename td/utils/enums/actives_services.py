from enum import Enum


class ActivesServices(Enum):
    """Represents the different streaming actives
    services.

    ### Usage
    ----
        >>> from td.utils.enums import ActivesServices
        >>> ActivesServices.ActivesNasdaq.value
    """

    ActivesNasdaq = 'ACTIVES_NASDAQ'
    ActivesNyse = 'ACTIVES_NYSE'
    ActivesOptions = 'ACTIVES_OPTIONS'
    ActivesOtcbb = 'ACTIVES_OTCBB'
