from enum import Enum


class ComplexOrderStrategyType(Enum):
    """Represents the different order Asset types
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.utils.enums import ComplexOrderStrategyType
        >>> ComplexOrderStrategyType.IronCondor.value
    """

    NoneProvided = 'NONE'
    Covered = 'COVERED'
    Vertical = 'VERTICAL'
    BackRatio = 'BACK_RATIO'
    Calendar = 'CALENDAR'
    Diagonal = 'DIAGONAL'
    Straddle = 'STRADDLE'
    Strangle = 'STRANGLE'
    CollarSynthetic = 'COLLAR_SYNTHETIC'
    Butterfly = 'BUTTERFLY'
    Condor = 'CONDOR'
    IronCondor = 'IRON_CONDOR'
    VerticalRoll = 'VERTICAL_ROLL'
    CollarWithStock = 'COLLAR_WITH_STOCK'
    DoubleDiagonal = 'DOUBLE_DIAGONAL'
    UnbalancedButterfly = 'UNBALANCED_BUTTERFLY'
    UnbalancedCondor = 'UNBALANCED_CONDOR'
    UnbalancedIronCondor = 'UNBALANCED_IRON_CONDOR'
    UnbalancedVerticalRoll = 'UNBALANCED_VERTICAL_ROLL'
    Custom = 'CUSTOM'
