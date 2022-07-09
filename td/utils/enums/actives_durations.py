from enum import Enum


class ActivesDurations(Enum):
    """Represents the different durations for the
    Actives Service.

    ### Usage
    ----
        >>> from td.utils.enums import ActivesDurations
        >>> ActivesDurations.All.value
    """

    All = 'ALL'
    SixtySeconds = '60'
    ThreeHundredSeconds = '300'
    SixHundredSeconds = '600'
    EighteenHundredSeconds = '1800'
    ThirtySixHundredSeconds = '3600'

