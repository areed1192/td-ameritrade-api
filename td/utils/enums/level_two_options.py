from enum import Enum

from td.utils.utils import str_range


class LevelTwoOptions(Enum):
    """Represents the Level Two Options Fields.

    ### Usage
    ----
        >>> from td.utils.enums import LevelTwoOptions
        >>> LevelTwoOptions.All.value
    """

    All = str_range(3)
    Key = '0'
    Time = '1'
    Data = '2'
