from enum import Enum

from td.utils.utils import str_range


class NewsHeadlines(Enum):
    """Represents the different fields for the News
    Headline Feed.

    ### Usage
    ----
        >>> from td.utils.enums import NewsHeadlines
        >>> NewsHeadlines.All.value
    """

    All = str_range(11)
    Symbol = '0'
    ErrorCode = '1'
    StoryDatetime = '2'
    HeadlineId = '3'
    Status = '4'
    Headline = '5'
    StoryId = '6'
    CountForKeyword = '7'
    KeywordArray = '8'
    IsHot = '9'
    StorySource = '10'
