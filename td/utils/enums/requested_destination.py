from enum import Enum


class RequestedDestination(Enum):
    """Represents the different order requested
    destinations when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.utils.enums import RequestedDestination
        >>> RequestedDestination.Cboe.value
    """

    Inet = 'INET'
    EcnArca = 'ECN_ARCA'
    Cboe = 'CBOE'
    Amex = 'AMEX'
    Phlx = 'PHLX'
    Ise = 'ISE'
    Box = 'BOX'
    Nyse = 'NYSE'
    Nasdaq = 'NASDAQ'
    Bats = 'BATS'
    C2 = 'C2'
    Auto = 'AUTO'
