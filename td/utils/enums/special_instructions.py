from enum import Enum


class SpecialInstructions(Enum):
    """Represents the different order special instructions
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.utils.enums import SpecialInstructions
        >>> SpecialInstructions.AllOrNone.value
    """

    AllOrNone = 'ALL_OR_NONE'
    DoNotReduce = 'DO_NOT_REDUCE'
    AllOrNoneDoNotReduce = 'ALL_OR_NONE_DO_NOT_REDUCE'
