from enum import Enum


class OptionType(Enum):
    """Represents the different option types
    when querying the `OptionChain` service.

    ### Usage
    ----
        >>> from td.utils.enums import OptionType
        >>> OptionType.All.value
    """

    All = 'ALL'
    StandardContracts = 'S'
    NonStandardContracts = 'NS'
