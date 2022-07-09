from enum import Enum


class PositionEffect(Enum):
    """Represents the different position effects
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.utils.enums import PositionEffect
        >>> PositionEffect.Opening.value
    """

    Opening = 'OPENING'
    Closing = 'CLOSING'
    Automatic = 'AUTOMATIC'
