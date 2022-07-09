from enum import Enum


class DefaultOrderDuration(Enum):
    """Represents the different Default Order Duration
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.utils.enums import DefaultOrderDuration
        >>> DefaultOrderDuration.Day.value
    """

    Day = 'DAY'
    GoodTillCancel = 'GOOD_TILL_CANCEL'
    FillOrKill = 'FILL_OR_KILL'
    NoneSpecified = 'NONE'
