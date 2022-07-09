from enum import Enum


class DefaultOrderPriceLinkType(Enum):
    """Represents the different Default Order Price Link Type
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.utils.enums import DefaultOrderPriceLinkType
        >>> DefaultOrderPriceLinkType.Value.value
    """

    Value = 'VALUE'
    Percent = 'PERCENT'
    NoneSpecified = 'NONE'
