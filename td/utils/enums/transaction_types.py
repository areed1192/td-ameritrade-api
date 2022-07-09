from enum import Enum


class TransactionTypes(Enum):
    """Represents the types of transaction you
    can query from TD Ameritrade using the `Accounts`
    services.

    ### Usage
    ----
        >>> from td.utils.enums import TransactionTypes
        >>> TransactionTypes.Trade.value
    """

    All = 'ALL'
    Trade = 'TRADE'
    BuyOnly = 'BUY_ONLY'
    SellOnly = 'SELL_ONLY'
    CashInOrCashOut = 'CASH_IN_OR_CASH_OUT'
    Checking = 'CHECKING'
    Dividend = 'DIVIDEND'
    Interest = 'INTEREST'
    Other = 'OTHER'
    AdvisorFees = 'ADVISOR_FEES'
