from enum import Enum


class OrderStrategyType(Enum):
    """Represents the different order strategy types
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.utils.enums import OrderStrategyType
        >>> OrderStrategyType.Single.value
    """

    Single = 'SINGLE'
    Oco = 'OCO'
    Trigger = 'TRIGGER'
