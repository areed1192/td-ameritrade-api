from enum import Enum


class StrategyType(Enum):
    """Represents the different strategy types
    when querying the `OptionChain` service.

    ### Usage
    ----
        >>> from td.utils.enums import StrategyType
        >>> StrategyType.Analytical.value
    """

    Analytical = 'ANALYTICAL'
    Butterfly = 'BUTTERFLY'
    Calendar = 'CALENDAR'
    Collar = 'COLLAR'
    Condor = 'CONDOR'
    Covered = 'COVERED'
    Diagonal = 'DIAGONAL'
    Roll = 'ROLL'
    Single = 'SINGLE'
    Straddle = 'STRADDLE'
    Strangle = 'STRANGLE'
    Vertical = 'VERTICAL'
