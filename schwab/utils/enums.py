"""Common Enums for the Schwab API."""

from enum import Enum
from enum import IntEnum


class Sort(Enum):
    """Represents the sort options for the
    `Movers` service.

    ### Usage
    ----
        >>> from schwab.enums import Sort
        >>> Sort.VOLUME.value
        'VOLUME'
    """

    VOLUME = "VOLUME"
    TRADES = "TRADES"
    PERCENT_CHANGE_UP = "PERCENT_CHANGE_UP"
    PERCENT_CHANGE_DOWN = "PERCENT_CHANGE_DOWN"


class Frequency(IntEnum):
    """Represents the Frequency options for the
    `Movers` service.

    ### Usage
    ----
        >>> from schwab.enums import Frequency
        >>> Frequency.ZERO.value
        0
    """

    ZERO = 0
    ONE = 1
    FIVE = 5
    TEN = 10
    THIRTY = 30
    SIXTY = 60


class TransactionTypes(Enum):
    """Represents the types of transaction you
    can query from Charles Schwab using the `Accounts`
    services.

    ### Usage
    ----
        >>> from schwab.enums import TransactionTypes
        >>> TransactionTypes.TRADE.value
    """

    TRADE = "TRADE"
    RECEIVE_AND_DELIVER = "RECEIVE_AND_DELIVER"
    DIVIDEND_OR_INTEREST = "DIVIDEND_OR_INTEREST"
    ACH_RECEIPT = "ACH_RECEIPT"
    ACH_DISBURSEMENT = "ACH_DISBURSEMENT"
    CASH_RECEIPT = "CASH_RECEIPT"
    CASH_DISBURSEMENT = "CASH_DISBURSEMENT"
    ELECTRONIC_FUND = "ELECTRONIC_FUND"
    WIRE_OUT = "WIRE_OUT"
    WIRE_IN = "WIRE_IN"
    JOURNAL = "JOURNAL"
    MEMORANDUM = "MEMORANDUM"
    MARGIN_CALL = "MARGIN_CALL"
    MONEY_MARKET = "MONEY_MARKET"
    SMA_ADJUSTMENT = "SMA_ADJUSTMENT"


class Markets(Enum):
    """Represents the different markets you can request
    hours for the `MarketHours` service.

    ### Usage
    ----
        >>> from schwab.enums import Markets
        >>> Markets.BOND.Value
        'bond
    """

    BOND = "bond"
    EQUITY = "equity"
    OPTION = "option"
    FOREX = "forex"
    FUTURES = "future"

class Projections(Enum):
    """Represents the different search types you can use for
    the `Instruments` service.

    ### Usage
    ----
        >>> from schwab.enums import Projections
        >>> Projections.SYMBOL_SEARCH.value
        'symbol-search'
    """

    SYMBOL_SEARCH = "symbol-search"
    SYMBOL_REGEX = "symbol-regex"
    DESCRIPTION_SEARCH = "desc-search"
    DESCRIPTION_REGEX = "desc-regex"
    FUNDAMENTAL = "fundamental"


class DefaultOrderLegInstruction(Enum):
    """Represents the different Default Order Leg Instructions
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from schwab.enums import DefaultOrderLegInstruction
        >>> DefaultOrderLegInstruction.SELL.value
        'SELL'
    """

    BUY = "BUY"
    SELL = "SELL"
    BUY_TO_COVER = "BUY_TO_COVER"
    SELL_SHORT = "SELL_SHORT"
    NONE_SPECIFIED = "NONE"


class DefaultOrderType(Enum):
    """Represents the different Default Order Type
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from schwab.enums import DefaultOrderType
        >>> DefaultOrderType.MARKET.value
        'MARKET'
    """

    MARKET = "MARKET"
    LIMIT = "LIMIT"
    STOP = "STOP"
    STOP_LIMIT = "STOP_LIMIT"
    TRAILING_STOP = "TRAILING_STOP"
    MARKET_ON_CLOSE = "MARKET_ON_CLOSE"
    NONE_SPECIFIED = "NONE"


class DefaultOrderPriceLinkType(Enum):
    """Represents the different Default Order Price Link Type
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from schwab.enums import DefaultOrderPriceLinkType
        >>> DefaultOrderPriceLinkType.VALUE.value
        'VALUE'
    """

    VALUE = "VALUE"
    PERCENT = "PERCENT"
    NONE_SPECIFIED = "NONE"


class DefaultOrderDuration(Enum):
    """Represents the different Default Order Duration
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from schwab.enums import DefaultOrderDuration
        >>> DefaultOrderDuration.DAY.value
        'DAY'
    """

    DAY = "DAY"
    GOOD_TILL_CANCEL = "GOOD_TILL_CANCEL"
    FILL_OR_KILL = "FILL_OR_KILL"
    IMMEDIATE_OR_CANCEL = "IMMEDIATE_OR_CANCEL"
    END_OF_WEEK = "END_OF_WEEK"
    END_OF_MONTH = "END_OF_MONTH"
    NEXT_END_OF_MONTH = "NEXT_END_OF_MONTH"
    UNKNOWN = "UNKNOWN"


class DefaultOrderMarketSession(Enum):
    """Represents the different Default Order Market Session
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from schwab.enums import DefaultOrderMarketSession
        >>> DefaultOrderMarketSession.AM.value
        'AM'
    """

    AM = "AM"
    PM = "PM"
    NORMAL = "NORMAL"
    SEAMLESS = "SEAMLESS"


class TaxLotMethod(Enum):
    """Represents the different Tax Lot Methods
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from schwab.enums import TaxLotMethod
        >>> TaxLotMethod.FIFO.value
        'FIFO'
    """

    FIFO = "FIFO"
    LIFO = "LIFO"
    HIGH_COST = "HIGH_COST"
    LOW_COST = "LOW_COST"
    MINIMUM_TAX = "MINIMUM_TAX"
    AVERAGE_COST = "AVERAGE_COST"
    NONE_SPECIFIED = "NONE"


class DefaultAdvancedToolLaunch(Enum):
    """Represents the different Default Advanced Tool Launch
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from schwab.enums import DefaultAdvancedToolLaunch
        >>> DefaultAdvancedToolLaunch.TOS.value
        'TOS'
    """

    TA = "Ta"  # Note: The value remains "Ta" if needed.
    NO = "N"
    YES = "Y"
    TOS = "TOS"
    CC2 = "CC2"
    NONE_SPECIFIED = "NONE"


class AuthTokenTimeout(Enum):
    """Represents the different Auth Token Timeout
    properties for the `UserInfo` service.

    ### Usage
    ----
        >>> from schwab.enums import AuthTokenTimeout
        >>> AuthTokenTimeout.FIFTY_FIVE_MINUTES.value
        'FIFTY_FIVE_MINUTES'
    """

    FIFTY_FIVE_MINUTES = "FIFTY_FIVE_MINUTES"
    TWO_HOURS = "TWO_HOURS"
    FOUR_HOURS = "FOUR_HOURS"
    EIGHT_HOURS = "EIGHT_HOURS"


class FrequencyType(Enum):
    """Represents the different chart frequencies
    for the `PriceHistory` service.

    ### Usage
    ----
        >>> from schwab.enums import FrequencyType
        >>> FrequencyType.DAILY.value
        'daily'
    """

    MINUTE = "minute"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"


class PeriodType(Enum):
    """Represents the different chart periods
    for the `PriceHistory` service.

    ### Usage
    ----
        >>> from schwab.enums import PeriodType
        >>> PeriodType.DAY.value
        'day'
    """

    DAY = "day"
    MONTH = "month"
    YEAR = "year"
    YEAR_TO_DATE = "ytd"


class StrategyType(Enum):
    """Represents the different strategy types
    when querying the `OptionChain` service.

    ### Usage
    ----
        >>> from schwab.enums import StrategyType
        >>> StrategyType.ANALYTICAL.value
        'ANALYTICAL'
    """

    ANALYTICAL = "ANALYTICAL"
    BUTTERFLY = "BUTTERFLY"
    CALENDAR = "CALENDAR"
    COLLAR = "COLLAR"
    CONDOR = "CONDOR"
    COVERED = "COVERED"
    DIAGONAL = "DIAGONAL"
    ROLL = "ROLL"
    SINGLE = "SINGLE"
    STRADDLE = "STRADDLE"
    STRANGLE = "STRANGLE"
    VERTICAL = "VERTICAL"


class OptionRange(Enum):
    """Represents the different option range types
    when querying the `OptionChain` service.

    ### Usage
    ----
        >>> from schwab.enums import OptionRange
        >>> OptionRange.IN_THE_MONEY.value
        'ITM'
    """

    ALL = "ALL"
    IN_THE_MONEY = "ITM"
    NEAR_THE_MONEY = "NTM"
    OUT_THE_MONEY = "OTM"
    STRIKES_ABOVE_MARKET = "SAK"
    STRIKES_BELOW_MARKET = "SBK"
    STRIKES_NEAR_MARKET = "SNK"


class ExpirationMonth(Enum):
    """Represents the different option expiration months
    when querying the `OptionChain` service.

    ### Usage
    ----
        >>> from schwab.enums import ExpirationMonth
        >>> ExpirationMonth.JANUARY.Value
        'JAN'
    """

    ALL = "ALL"
    JANUARY = "JAN"
    FEBRUARY = "FEB"
    MARCH = "MAR"
    APRIL = "APRIL"
    MAY = "MAY"
    JUNE = "JUN"
    JULY = "JUL"
    AUGUST = "AUG"
    SEPTEMBER = "SEP"
    OCTOBER = "OCT"
    NOVEMBER = "NOV"
    DECEMBER = "DEC"


class ContractType(Enum):
    """Represents the different option contract types
    when querying the `ContractType` service.

    ### Usage
    ----
        >>> from schwab.enums import ContractType
        >>> ContractType.CALL.Value
        'CALL'
    """

    ALL = "ALL"
    CALL = "CALL"
    PUT = "PUT"


class SettlementType(Enum):
    """Represents the different option settlement types
    when querying the `SettlementType` service.

    ### Usage
    ----
        >>> from schwab.enums import SettlementType
        >>> SettlementType.CASH.Value
        'CASH'
    """

    REGULAR = "REGULAR"
    NEXT_DAY = "NEXT_DAY"
    UNKNOWN = "UNKNOWN"
    CASH = "CASH"


class ApiRuleAction(Enum):
    """Represents the different API rule actions.

    ### Usage
    ----
        >>> from schwab.enums import ApiRuleAction
        >>> ApiRuleAction.ACCEPT.Value
        'ACCEPT'
    """

    ACCEPT = "ACCEPT"
    ALERT = "ALERT"
    REJECT = "REJECT"
    REVIEW = "REVIEW"
    UNKNOWN = "UNKNOWN"


class OptionType(Enum):
    """Represents the different option types
    when querying the `OptionType` service.

    ### Usage
    ----
        >>> from schwab.enums import OptionType
        >>> OptionType.ALL.Value
        'ALL'
    """

    ALL = "ALL"
    STANDARD_CONTRACTS = "S"
    NON_STANDARD_CONTRACTS = "NS"


class EntitlementType(Enum):
    """Represents the different option types
    when querying the `OptionType` service.

    ### Usage
    ----
        >>> from schwab.enums import OptionType
        >>> OptionType.ALL.Value
        'ALL'
    """

    PP_PAYING_PRO = "PP-PayingPro"
    NP_NON_PRO = "NP-NonPro"
    PN_NON_PAYING_PRO = "PN-NonPayingPro"


class OrderStatus(Enum):
    """Represents the different order status types
    when querying the `Orders` service.

    ### Usage
    ----
        >>> from schwab.enums import OrderStatus
        >>> OrderStatus.WORKING.Value
        'WORKING'
    """

    AWAITING_PARENT_ORDER = "AWAITING_PARENT_ORDER"
    AWAITING_CONDITION = "AWAITING_CONDITION"
    AWAITING_STOP_CONDITION = "AWAITING_STOP_CONDITION"
    AWAITING_MANUAL_REVIEW = "AWAITING_MANUAL_REVIEW"
    ACCEPTED = "ACCEPTED"
    AWAITING_UR_OUT = "AWAITING_UR_OUT"
    PENDING_ACTIVATION = "PENDING_ACTIVATION"
    QUEUED = "QUEUED"
    WORKING = "WORKING"
    REJECTED = "REJECTED"
    PENDING_CANCEL = "PENDING_CANCEL"
    CANCELED = "CANCELED"
    PENDING_REPLACE = "PENDING_REPLACE"
    REPLACED = "REPLACED"
    FILLED = "FILLED"
    EXPIRED = "EXPIRED"
    NEW = "NEW"
    AWAITING_RELASE_TIME = "AWAITING_RELEASE_TIME"
    PENDING_ACKNOWLEDGEMENT = "PENDING_ACKNOWLEDGEMENT"
    PENDING_RECALL = "PENDING_RECALL"
    UNKNOWN = "UNKNOWN"


class QuoteRequest(Enum):
    """Represents the different fields you can request
    when querying the `Quote` service.

    ### Usage
    ----
        >>> from schwab.enums import QuoteRequest
        >>> QuoteRequest.QUOTE.Value
        'quote'
    """

    ALL = ["quote", "fundamental", "extended", "regular"]
    QUOTE = "quote"
    FUNDAMENTAL = "fundamental"
    REFERENCE = "reference"
    EXTENDED = "extended"
    REGULAR = "regular"


class OrderStrategyType(Enum):
    """Represents the different order strategy types
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from schwab.enums import OrderStrategyType
        >>> OrderStrategyType.SINGLE.Value
        'SINGLE'
    """

    SINGLE = "SINGLE"
    CANCEL = "CANCEL"
    RECALL = "RECALL"
    PAIR = "PAIR"
    FLATTEN = "FLATTEN"
    TWO_DAY_SWAP = "TWO_DAY_SWAP"
    BLAST_ALL = "BLAST_ALL"
    OCO = "OCO"
    TRIGGER = "TRIGGER"


class QuantityType(Enum):
    """Represents the different order quantity types
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from schwab.enums import QuantityType
        >>> QuantityType.DOLLARS.Value
        'DOLLARS'
    """

    ALL_SHARES = "ALL_SHARES"
    DOLLARS = "DOLLARS"
    SHARES = "SHARES"
    PERCENTAGE = "PERCENTAGE"
    UNKNOWN = "UNKNOWN"


class AssetType(Enum):
    """Represents the different order Asset types
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from schwab.enums import AssetType
        >>> AssetType.EQUITY.Value
        'EQUITY'
    """

    EQUITY = "EQUITY"
    OPTION = "OPTION"
    INDEX = "INDEX"
    FUTURE = "FUTURE"
    FOREX = "FOREX"
    MUTUAL_FUND = "MUTUAL_FUND"
    CASH_EQUIVALENT = "CASH_EQUIVALENT"
    FIXED_INCOME = "FIXED_INCOME"
    PRODUCT = "PRODUCT"
    CURRENCY = "CURRENCY"
    COLLECTIVE_INVESTMENT = "COLLECTIVE_INVESTMENT"


class ComplexOrderStrategyType(Enum):
    """Represents the different complex order strategy types
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from schwab.enums import ComplexOrderStrategyType
        >>> ComplexOrderStrategyType.IRON_CONDOR.Value
        'IRON_CONDOR'
    """

    NONE_PROVIDED = "NONE"
    COVERED = "COVERED"
    VERTICAL = "VERTICAL"
    BACK_RATIO = "BACK_RATIO"
    CALENDAR = "CALENDAR"
    DIAGONAL = "DIAGONAL"
    STRADDLE = "STRADDLE"
    STRANGLE = "STRANGLE"
    COLLAR_SYNTHETIC = "COLLAR_SYNTHETIC"
    BUTTERFLY = "BUTTERFLY"
    CONDOR = "CONDOR"
    IRON_CONDOR = "IRON_CONDOR"
    VERTICAL_ROLL = "VERTICAL_ROLL"
    COLLAR_WITH_STOCK = "COLLAR_WITH_STOCK"
    DOUBLE_DIAGONAL = "DOUBLE_DIAGONAL"
    UNBALANCED_BUTTERFLY = "UNBALANCED_BUTTERFLY"
    UNBALANCED_CONDOR = "UNBALANCED_CONDOR"
    UNBALANCED_IRON_CONDOR = "UNBALANCED_IRON_CONDOR"
    UNBALANCED_VERTICAL_ROLL = "UNBALANCED_VERTICAL_ROLL"
    MUTUAL_FUND_SWAP = "MUTUAL_FUND_SWAP"
    CUSTOM = "CUSTOM"


class OrderInstructions(Enum):
    """Represents the different order instructions
    when constructing and `Order` object.

    ### Usage
    ----
        >>> from schwab.enums import OrderInstructions
        >>> OrderInstructions.SELL_SHORT.Value
        'SELL_SHORT'
    """

    BUY = "BUY"
    SELL = "SELL"
    BUY_TO_COVER = "BUY_TO_COVER"
    SELL_SHORT = "SELL_SHORT"
    BUY_TO_OPEN = "BUY_TO_OPEN"
    BUY_TO_CLOSE = "BUY_TO_CLOSE"
    SELL_TO_OPEN = "SELL_TO_OPEN"
    SELL_TO_CLOSE = "SELL_TO_CLOSE"
    EXCHANGE = "EXCHANGE"
    SELL_SHORT_EXEMPT = "SELL_SHORT_EXEMPT"


class RequestedDestination(Enum):
    """Represents the different order requested
    destinations when constructing an `Order` object.

    ### Usage
    ----
        >>> from schwab.enums import RequestedDestination
        >>> RequestedDestination.CBOE.value
        'CBOE'
    """

    INET = "INET"
    ECN_ARCA = "ECN_ARCA"
    CBOE = "CBOE"
    AMEX = "AMEX"
    PHLX = "PHLX"
    ISE = "ISE"
    BOX = "BOX"
    NYSE = "NYSE"
    NASDAQ = "NASDAQ"
    BATS = "BATS"
    C2 = "C2"
    AUTO = "AUTO"


class StopPriceLinkBasis(Enum):
    """Represents the different stop price link basis
    when constructing an `Order` object.

    ### Usage
    ----
        >>> from schwab.enums import StopPriceLinkBasis
        >>> StopPriceLinkBasis.TRIGGER.value
        'TRIGGER'
    """

    MANUAL = "MANUAL"
    BASE = "BASE"
    TRIGGER = "TRIGGER"
    LAST = "LAST"
    BID = "BID"
    ASK = "ASK"
    ASK_BID = "ASK_BID"
    MARK = "MARK"
    AVERAGE = "AVERAGE"


class StopPriceLinkType(Enum):
    """Represents the different stop price link type
    when constructing an `Order` object.

    ### Usage
    ----
        >>> from schwab.enums import StopPriceLinkType
        >>> StopPriceLinkType.TRIGGER.value
        'TRIGGER'
    """

    VALUE = "VALUE"
    PERCENT = "PERCENT"
    TICK = "TICK"


class StopType(Enum):
    """Represents the different stop type
    when constructing an `Order` object.

    ### Usage
    ----
        >>> from schwab.enums import StopType
        >>> StopType.STANDARD.value
        'STANDARD'
    """

    STANDARD = "STANDARD"
    BID = "BID"
    ASK = "ASK"
    LAST = "LAST"
    MARK = "MARK"


class PriceLinkBasis(Enum):
    """Represents the different price link basis
    when constructing an `Order` object.

    ### Usage
    ----
        >>> from schwab.enums import PriceLinkBasis
        >>> PriceLinkBasis.MANUAL.value
        'MANUAL'
    """

    MANUAL = "MANUAL"
    BASE = "BASE"
    TRIGGER = "TRIGGER"
    LAST = "LAST"
    BID = "BID"
    ASK = "ASK"
    ASK_BID = "ASK_BID"
    MARK = "MARK"
    AVERAGE = "AVERAGE"


class PriceLinkType(Enum):
    """Represents the different price link type
    when constructing an `Order` object.

    ### Usage
    ----
        >>> from schwab.enums import PriceLinkType
        >>> PriceLinkType.TRIGGER.value
        'TRIGGER'
    """

    VALUE = "VALUE"
    PERCENT = "PERCENT"
    TICK = "TICK"


class OrderType(Enum):
    """Represents the different order type
    when constructing an `Order` object.

    ### Usage
    ----
        >>> from schwab.enums import OrderType
        >>> OrderType.MARKET.value
        'MARKET'
    """

    MARKET = "MARKET"
    LIMIT = "LIMIT"
    STOP = "STOP"
    STOP_LIMIT = "STOP_LIMIT"
    TRAILING_STOP = "TRAILING_STOP"
    CABINET = "CABINET"
    NON_MARKETABLE = "NON_MARKETABLE"
    MARKET_ON_CLOSE = "MARKET_ON_CLOSE"
    EXERCISE = "EXERCISE"
    TRAILING_STOP_LIMIT = "TRAILING_STOP_LIMIT"
    NET_DEBIT = "NET_DEBIT"
    NET_CREDIT = "NET_CREDIT"
    NET_ZERO = "NET_ZERO"
    LIMIT_ON_CLOSE = "LIMIT_ON_CLOSE"
    UNKNOWN = "UNKNOWN"


class PositionEffect(Enum):
    """Represents the different position effects
    when constructing an `Order` object.

    ### Usage
    ----
        >>> from schwab.enums import PositionEffect
        >>> PositionEffect.OPENING.value
        'OPENING'
    """

    OPENING = "OPENING"
    CLOSING = "CLOSING"
    AUTOMATIC = "AUTOMATIC"


class OrderTaxLotMethod(Enum):
    """Represents the different order tax lot methods
    when constructing an `Order` object.

    ### Usage
    ----
        >>> from schwab.enums import OrderTaxLotMethod
        >>> OrderTaxLotMethod.FIFO.value
        'FIFO'
    """

    FIFO = "FIFO"
    LIFO = "LIFO"
    HIGH_COST = "HIGH_COST"
    LOW_COST = "LOW_COST"
    AVERAGE_COST = "AVERAGE_COST"
    SPECIFIC_LOT = "SPECIFIC_LOT"
    LOSS_HARVESTER = "LOSS_HARVESTER"


class SpecialInstructions(Enum):
    """Represents the different order special instructions
    when constructing an `Order` object.

    ### Usage
    ----
        >>> from schwab.enums import SpecialInstructions
        >>> SpecialInstructions.ALL_OR_NONE.value
        'ALL_OR_NONE'
    """

    ALL_OR_NONE = "ALL_OR_NONE"
    DO_NOT_REDUCE = "DO_NOT_REDUCE"
    ALL_OR_NONE_DO_NOT_REDUCE = "ALL_OR_NONE_DO_NOT_REDUCE"


class FeeType(Enum):
    """Represents the different fee types
    when constructing an `Order` object.

    ### Usage
    ----
        >>> from schwab.enums import FeeType
        >>> FeeType.COMMISSION.value
        'COMMISSION'
    """

    COMMISSION = "COMMISSION"
    SEC_FEE = "SEC_FEE"
    STR_FEE = "STR_FEE"
    R_FEE = "R_FEE"
    CDSC_FEE = "CDSC_FEE"
    OPT_REG_FEE = "OPT_REG_FEE"
    ADDITIONAL_FEE = "ADDITIONAL_FEE"
    MISCELLANEOUS_FEE = "MISCELLANEOUS_FEE"
    FTT = "FTT"
    FUTURES_CLEARING_FEE = "FUTURES_CLEARING_FEE"
    FUTURES_DESK_OFFICE_FEE = "FUTURES_DESK_OFFICE_FEE"
    FUTURES_EXCHANGE_FEE = "FUTURES_EXCHANGE_FEE"
    FUTURES_GLOBEX_FEE = "FUTURES_GLOBEX_FEE"
    FUTURES_NFA_FEE = "FUTURES_NFA_FEE"
    FUTURES_PIT_BROKERAGE_FEE = "FUTURES_PIT_BROKERAGE_FEE"
    FUTURES_TRANSACTION_FEE = "FUTURES_TRANSACTION_FEE"
    LOW_PROCEEDS_COMMISSION = "LOW_PROCEEDS_COMMISSION"
    BASE_CHARGE = "BASE_CHARGE"
    GENERAL_CHARGE = "GENERAL_CHARGE"
    GST_FEE = "GST_FEE"
    TAF_FEE = "TAF_FEE"
    INDEX_OPTION_FEE = "INDEX_OPTION_FEE"
    TEFRA_TAX = "TEFRA_TAX"
    STATE_TAX = "STATE_TAX"
    UNKNOWN = "UNKNOWN"


class LevelOneQuotes(Enum):
    """Represents the different fields for the Level One
    Quotes Feed.

    ### Usage
    ----
        >>> from schwab.enums import LevelOneQuotes
        >>> LevelOneQuotes.ALL.value  # Returns a list of strings 0-52
        ['0', '1', ..., '52']
    """

    ALL = [str(item) for item in range(0, 53)]
    SYMBOL = 0
    BID_PRICE = 1
    ASK_PRICE = 2
    LAST_PRICE = 3
    BID_SIZE = 4
    ASK_SIZE = 5
    ASK_ID = 6
    BID_ID = 7
    TOTAL_VOLUME = 8
    LAST_SIZE = 9
    TRADE_TIME = 10
    QUOTE_TIME = 11
    HIGH_PRICE = 12
    LOW_PRICE = 13
    BID_TICK = 14
    CLOSE_PRICE = 15
    EXCHANGE_ID = 16
    MARGINABLE = 17
    SHORTABLE = 18
    ISLAND_BID = 19
    ISLAND_ASK = 20
    ISLAND_VOLUME = 21
    QUOTE_DAY = 22
    TRADE_DAY = 23
    VOLATILITY = 24
    DESCRIPTION = 25
    LAST_ID = 26
    DIGITS = 27
    OPEN_PRICE = 28
    NET_CHANGE = 29
    FIFTY_TWO_WEEK_HIGH = 30
    FIFTY_TWO_WEEK_LOW = 31
    PE_RATIO = 32
    DIVIDEND_AMOUNT = 33
    DIVIDEND_YIELD = 34
    ISLAND_BID_SIZE = 35
    ISLAND_ASK_SIZE = 36
    NAV = 37
    FUND_PRICE = 38
    EXCHANGE_NAME = 39
    DIVIDEND_DATE = 40
    REGULAR_MARKET_QUOTE = 41
    REGULAR_MARKET_TRADE = 42
    REGULAR_MARKET_LAST_PRICE = 43
    REGULAR_MARKET_LAST_SIZE = 44
    REGULAR_MARKET_TRADE_TIME = 45
    REGULAR_MARKET_TRADE_DAY = 46
    REGULAR_MARKET_NET_CHANGE = 47
    SECURITY_STATUS = 48
    MARK = 49
    QUOTE_TIME_IN_LONG = 50
    TRADE_TIME_IN_LONG = 51
    REGULAR_MARKET_TRADE_TIME_IN_LONG = 52


class LevelOneOptions(Enum):
    """Represents the different fields for the Level One
    Options Feed.

    ### Usage
    ----
        >>> from schwab.enums import LevelOneOptions
        >>> LevelOneOptions.ALL.value  # Returns a list of strings 0-41
        ['0', '1', ..., '41']
    """

    ALL = [str(item) for item in range(0, 42)]
    SYMBOL = 0
    DESCRIPTION = 1
    BID_PRICE = 2
    ASK_PRICE = 3
    LAST_PRICE = 4
    HIGH_PRICE = 5
    LOW_PRICE = 6
    CLOSE_PRICE = 7
    TOTAL_VOLUME = 8
    OPEN_INTEREST = 9
    VOLATILITY = 10
    QUOTE_TIME = 11
    TRADE_TIME = 12
    MONEY_INTRINSIC_VALUE = 13
    QUOTE_DAY = 14
    TRADE_DAY = 15
    EXPIRATION_YEAR = 16
    MULTIPLIER = 17
    DIGITS = 18
    OPEN_PRICE = 19
    BID_SIZE = 20
    ASK_SIZE = 21
    LAST_SIZE = 22
    NET_CHANGE = 23
    STRIKE_PRICE = 24
    CONTRACT_TYPE = 25
    UNDERLYING = 26
    EXPIRATION_MONTH = 27
    DELIVERABLES = 28
    TIME_VALUE = 29
    EXPIRATION_DAY = 30
    DAYS_TO_EXPIRATION = 31
    DELTA = 32
    GAMMA = 33
    THETA = 34
    VEGA = 35
    RHO = 36
    SECURITY_STATUS = 37
    THEORETICAL_OPTION_VALUE = 38
    UNDERLYING_PRICE = 39
    UV_EXPIRATION_TYPE = 40
    MARK = 41


class LevelOneFutures(Enum):
    """Represents the different fields for the Level One
    Futures Feed.

    ### Usage
    ----
        >>> from schwab.enums import LevelOneFutures
        >>> LevelOneFutures.ALL.value  # Returns a list of strings 0-35
        ['0', '1', ..., '35']
    """

    ALL = [str(item) for item in range(0, 36)]
    SYMBOL = 0
    BID_PRICE = 1
    ASK_PRICE = 2
    LAST_PRICE = 3
    BID_SIZE = 4
    ASK_SIZE = 5
    ASK_ID = 6
    BID_ID = 7
    TOTAL_VOLUME = 8
    LAST_SIZE = 9
    QUOTE_TIME = 10
    TRADE_TIME = 11
    HIGH_PRICE = 12
    LOW_PRICE = 13
    CLOSE_PRICE = 14
    EXCHANGE_ID = 15
    DESCRIPTION = 16
    LAST_ID = 17
    OPEN_PRICE = 18
    NET_CHANGE = 19
    FUTURE_PERCENT_CHANGE = 20
    EXHANGE_NAME = 21  # Might be a typo, but left as-is
    SECURITY_STATUS = 22
    OPEN_INTEREST = 23
    MARK = 24
    TICK = 25
    TICK_AMOUNT = 26
    PRODUCT = 27
    FUTURE_PRICE_FORMAT = 28
    FUTURE_TRADING_HOURS = 29
    FUTURE_IS_TRADABLE = 30
    FUTURE_MULTIPLIER = 31
    FUTURE_IS_ACTIVE = 32
    FUTURE_SETTLEMENT_PRICE = 33
    FUTURE_ACTIVE_SYMBOL = 34
    FUTURE_EXPIRATION_DATE = 35


class LevelOneForex(Enum):
    """Represents the different fields for the Level One
    Forex Feed.

    ### Usage
    ----
        >>> from schwab.enums import LevelOneForex
        >>> LevelOneForex.ALL.value  # Returns a list of strings 0-29
        ['0', '1', ..., '29']
    """

    ALL = [str(item) for item in range(0, 30)]
    SYMBOL = 0
    BID_PRICE = 1
    ASK_PRICE = 2
    LAST_PRICE = 3
    BID_SIZE = 4
    ASK_SIZE = 5
    TOTAL_VOLUME = 6
    LAST_SIZE = 7
    QUOTE_TIME = 8
    TRADE_TIME = 9
    HIGH_PRICE = 10
    LOW_PRICE = 11
    CLOSE_PRICE = 12
    EXCHANGE_ID = 13
    DESCRIPTION = 14
    OPEN_PRICE = 15
    NET_CHANGE = 16
    PERCENT_CHANGE = 17
    EXCHANGE_NAME = 18
    DIGITS = 19
    SECURITY_STATUS = 20
    TICK = 21
    TICK_AMOUNT = 22
    PRODUCT = 23
    TRADING_HOURS = 24
    IS_TRADABLE = 25
    MARKET_MAKER = 26
    FIFTY_TWO_WEEK_HIGH = 27
    FIFTY_TWO_WEEK_LOW = 28
    MARK = 29


class LevelOneFuturesOptions(Enum):
    """Represents the different fields for the Level
    One Futures Options feed.

    ### Usage
    ----
        >>> from schwab.enums import LevelOneFuturesOptions
        >>> LevelOneFuturesOptions.ALL.value  # Returns a list of strings 0-35
        ['0', '1', ..., '35']
    """

    ALL = [str(item) for item in range(0, 36)]
    SYMBOL = 0
    BID_PRICE = 1
    ASK_PRICE = 2
    LAST_PRICE = 3
    BID_SIZE = 4
    ASK_SIZE = 5
    ASK_ID = 6
    BID_ID = 7
    TOTAL_VOLUME = 8
    LAST_SIZE = 9
    QUOTE_TIME = 10
    TRADE_TIME = 11
    HIGH_PRICE = 12
    LOW_PRICE = 13
    CLOSE_PRICE = 14
    EXCHANGE_ID = 15
    DESCRIPTION = 16
    LAST_ID = 17
    OPEN_PRICE = 18
    NET_CHANGE = 19
    FUTURE_PERCENT_CHANGE = 20
    EXHANGE_NAME = 21
    SECURITY_STATUS = 22
    OPEN_INTEREST = 23
    MARK = 24
    TICK = 25
    TICK_AMOUNT = 26
    PRODUCT = 27
    FUTURE_PRICE_FORMAT = 28
    FUTURE_TRADING_HOURS = 29
    FUTURE_IS_TRADABLE = 30
    FUTURE_MULTIPLIER = 31
    FUTURE_IS_ACTIVE = 32
    FUTURE_SETTLEMENT_PRICE = 33
    FUTURE_ACTIVE_SYMBOL = 34
    FUTURE_EXPIRATION_DATE = 35


class ChartServices(Enum):
    """Represents the different streaming chart
    services.

    ### Usage
    ----
        >>> from schwab.enums import ChartServices
        >>> ChartServices.CHART_EQUITY.value
        'CHART_EQUITY'
    """

    CHART_EQUITY = "CHART_EQUITY"
    CHART_FUTURES = "CHART_FUTURES"  # Was _ChartFutures
    CHART_OPTIONS = "CHART_OPTIONS"


class ChartEquity(Enum):
    """Represents the different streaming chart
    equity fields.

    ### Usage
    ----
        >>> from schwab.enums import ChartEquity
        >>> ChartEquity.ALL.value  # Returns a list of strings 0-8
        ['0', '1', ..., '8']
    """

    ALL = [str(item) for item in range(0, 9)]
    SYMBOL = 0
    OPEN_PRICE = 1
    HIGH_PRICE = 2
    LOW_PRICE = 3
    CLOSE_PRICE = 4  # Renamed from Close_Price
    VOLUME = 5
    SEQUENCE = 6
    CHART_TIME = 7
    CHART_DAY = 8


class ChartFutures(Enum):
    """Represents the different streaming chart
    futures fields.

    ### Usage
    ----
        >>> from schwab.enums import ChartFutures
        >>> ChartFutures.ALL.value  # Returns a list of strings 0-6
        ['0', '1', ..., '6']
    """

    ALL = [str(item) for item in range(0, 7)]
    SYMBOL = 0
    CHART_TIME = 1
    OPEN_PRICE = 2
    HIGH_PRICE = 3
    LOW_PRICE = 4
    CLOSE_PRICE = 5
    VOLUME = 6


class ActivesVenues(Enum):
    """Represents the different streaming actives
    venues.

    ### Usage
    ----
        >>> from schwab.enums import ActivesVenues
        >>> ActivesVenues.NASDAQ_EXCHANGE.value
        'NASDAQ'
    """

    NASDAQ_EXCHANGE = "NASDAQ"
    NEW_YORK_STOCK_EXCHANGE = "NYSE"
    OVER_THE_COUNTER_BULLETIN_BOARD = "OTCBB"
    CALLS = "CALLS"
    PUTS = "PUTS"
    OPTIONS = "OPTS"
    CALLS_DESC = "CALLS-DESC"
    PUTS_DESC = "PUTS-DESC"
    OPTIONS_DESC = "OPTS-DESC"

class ChartFuturesFrequencies(Enum):
    """Represents the different frequencies for the
    Chart History Futures streaming service.

    ### Usage
    ----
        >>> from schwab.enums import ChartFuturesFrequencies
        >>> ChartFuturesFrequencies.ONE_MINUTE.value
        'm1'
    """

    ONE_MINUTE = "m1"
    FIVE_MINUTE = "m5"
    TEN_MINUTE = "m10"
    THIRTY_MINUTE = "m30"
    ONE_HOUR = "h1"
    ONE_DAY = "d1"
    ONE_WEEK = "w1"
    ONE_MONTH = "n1"


class ChartFuturesPeriods(Enum):
    """Represents the different periods for the
    Chart History Futures streaming service.

    ### Usage
    ----
        >>> from schwab.enums import ChartFuturesPeriods
        >>> ChartFuturesPeriods.ONE_DAY.value
        'd1'
    """

    ONE_DAY = "d1"
    FIVE_DAY = "d5"
    FOUR_WEEKS = "w4"
    TEN_MONTHS = "n10"
    ONE_YEAR = "y1"
    TEN_YEAR = "y10"


class LevelTwoQuotes(Enum):
    """Represents the Level Two Quotes Fields.

    ### Usage
    ----
        >>> from schwab.enums import LevelTwoQuotes
        >>> LevelTwoQuotes.ALL.value
        ['0', '1', '2']
    """

    ALL = [str(item) for item in range(0, 3)]
    KEY = 0
    TIME = 1
    DATA = 2


class LevelTwoOptions(Enum):
    """Represents the Level Two Options Fields.

    ### Usage
    ----
        >>> from schwab.enums import LevelTwoOptions
        >>> LevelTwoOptions.ALL.value
        ['0', '1', '2']
    """

    ALL = [str(item) for item in range(0, 3)]
    KEY = 0
    TIME = 1
    DATA = 2


class StreamingServices(Enum):
    """Represents the different streaming services.

    ### Usage
    ----
        >>> from schwab.enums import StreamingServices
        >>> StreamingServices.OPTION.value
        'OPTION'
    """

    ADMIN = "ADMIN"
    LEVELONE_EQUITIES = "LEVELONE_EQUITIES"
    LEVELONE_OPTIONS = "LEVELONE_OPTIONS"
    LEVELONE_FUTURES = "LEVELONE_FUTURES"
    LEVELONE_FUTURES_OPTIONS = "LEVELONE_FUTURES_OPTIONS"
    LEVELONE_FOREX = "LEVELONE_FOREX"
    NYSE_BOOK = "NYSE_BOOK"
    NASDAQ_BOOK = "NASDAQ_BOOK"
    OPTIONS_BOOK = "OPTIONS_BOOK"
    CHART_EQUITY = "CHART_EQUITY"
    CHART_FUTURES = "CHART_FUTURES"
    SCREENER_EQUITY = "SCREENER_EQUITY"
    SCREENER_OPTION = "SCREENER_OPTION"
    ACCT_ACTIVITY = "ACCT_ACTIVITY"


class StreamingServiceCommands(Enum):
    """Represents the different commands for the streaming
    services.

    ### Usage
    ----
        >>> from schwab.enums import StreamingServiceCommands
        >>> StreamingServiceCommands.LOGIN.value
        'LOGIN'
    """

    LOGIN = "LOGIN"
    SUBS = "SUBS"
    ADD = "ADD"
    UNSUBS = "UNSUBS"
    VIEW = "VIEW"
    LOGOUT = "LOGOUT"


class IndexSymbol(Enum):
    """Represents the different index symbols. For the
    `Movers` service.

    ### Usage
    ----
        >>> from schwab.enums import IndexSymbol
        >>> IndexSymbol.DJI.value
        '$DJI'
    """

    DJI = "$DJI"
    COMPX = "$COMPX"
    SPX = "$SPX"
    NYSE = "NYSE"
    NASDAQ = "NASDAQ"
    OTCBB = "OTCBB"
    INDEX_ALL = "INDEX_ALL"
    EQUITY_ALL = "EQUITY_ALL"
    OPTION_ALL = "OPTION_ALL"
    OPTION_PUT = "OPTION_PUT"
    OPTION_CALL = "OPTION_CALL"
