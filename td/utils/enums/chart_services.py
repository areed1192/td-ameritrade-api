from enum import Enum


class ChartServices(Enum):
    """Represents the different streaming chart
    services.

    ### Usage
    ----
        >>> from td.utils.enums import ChartServices
        >>> ChartServices.ChartEquity.value
    """

    ChartEquity = "CHART_EQUITY"
    _ChartFutures = "CHART_FUTURES"
    ChartOptions = "CHART_OPTIONS"
