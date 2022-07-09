from enum import Enum


class ContractType(Enum):
    """Represents the different option contract types
    when querying the `OptionChain` service.

    ### Usage
    ----
        >>> from td.utils.enums import ContractType
        >>> ContractType.Call.value
    """

    All = 'ALL'
    Call = 'CALL'
    Put = 'PUT'
