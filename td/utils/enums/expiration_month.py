from enum import Enum


class ExpirationMonth(Enum):
    """Represents the different option expiration months
    when querying the `OptionChain` service.

    ### Usage
    ----
        >>> from td.utils.enums import ExpirationMonth
        >>> ExpirationMonth.January.value
    """

    All = 'ALL'
    January = 'JAN'
    February = 'FEB'
    March = 'MAR'
    April = 'APR'
    May = 'MAY'
    June = 'JUN'
    July = 'JUL'
    August = 'AUG'
    September = 'SEP'
    October = 'OCT'
    November = 'NOV'
    December = 'DEC'
