from enum import Enum


class Change(Enum):
    """Represents the change options for the
    `Movers` service.

    ### Usage
    ----
        >>> from td.utils.enums import Change
        >>> Change.Percent.value
    """

    Percent = 'percent'
    Value = 'value'
