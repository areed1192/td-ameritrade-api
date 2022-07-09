from enum import Enum

from td.utils.utils import str_range


class LevelTwoQuotes(Enum):
    """Represents the Level Two Quotes Fields.

    ### Usage
    ----
        >>> from td.utils.enums import LevelTwoQuotes
        >>> LevelTwoQuotes.All.value
    """

    All = str_range(3)
    Key = '0'
    Time = '1'
    Data = '2'
