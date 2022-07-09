from enum import Enum


class Projections(Enum):
    """Represents the different search types you can use for
    the `Instruments` service.

    ### Usage
    ----
        >>> from td.utils.enums import Projections
        >>> Projections.SymbolSearch.value
    """

    SymbolSearch = 'symbol-search'
    SymbolRegex = 'symbol-regex'
    DescriptionSearch = 'desc-search'
    DescriptionRegex = 'desc-regex'
    Fundamental = 'fundamental'
