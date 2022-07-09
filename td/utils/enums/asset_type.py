from enum import Enum


class AssetType(Enum):
    """Represents the different order Asset types
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from td.utils.enums import AssetType
        >>> AssetType.Equity.value
    """

    Equity = 'EQUITY'
    Option = 'OPTION'
    Index = 'INDEX'
    MutualFund = 'MUTUAL_FUND'
    CashEquivalent = 'CASH_EQUIVALENT'
    FixedIncome = 'FIXED_INCOME'
    Currency = 'CURRENCY'
