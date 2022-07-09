from enum import Enum


class Direction(Enum):
    """Represents the direction options for the
    `Movers` service.

    ### Usage
    ----
        >>> from td.utils.enums import Direction
        >>> Direction.Up.value
    """

    Up = 'up'
    Down = 'down'
