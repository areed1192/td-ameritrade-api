from enum import Enum


class FrequencyType(Enum):
    """Represents the different chart frequencies
    for the `PriceHistory` service.

    ### Usage
    ----
        >>> from td.utils.enums import FrequencyType
        >>> FrequencyType.Daily.value
    """

    Minute = 'minute'
    Daily = 'daily'
    Weekly = 'weekly'
    Monthly = 'monthly'
