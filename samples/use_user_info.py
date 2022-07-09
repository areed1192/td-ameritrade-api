from pprint import pprint
from td.client import TdAmeritradeClient
from td.utils.enums import DefaultOrderDuration
from td.utils.enums import DefaultAdvancedToolLaunch
from td.utils.enums import DefaultOrderLegInstruction
from td.utils.enums import DefaultOrderMarketSession
from td.utils.enums import DefaultOrderPriceLinkType
from td.utils.enums import DefaultOrderType
from td.utils.enums import TaxLotMethod
from td.utils.enums import AuthTokenTimeout
from td.utils.user_preferences import UserPreferences

td_client = TdAmeritradeClient()
account_number = td_client.get_account_number()
# Initialize the `UserInfo` service.
user_info_service = td_client.user_info()

# Grab the preferences for a specific account.
pprint(
    user_info_service.get_preferences(
        account_id=account_number
    )
)

# Grab the streamer subscription keys.
pprint(
    user_info_service.get_streamer_subscription_keys(
        account_ids=[account_number]
    )
)

# Grab User Principals.
pprint(
    user_info_service.get_user_principals()
)

# Method 1, Update the User Preferences.
user_info_service.update_user_preferences(
    account_id=account_number,
    preferences={
        'authTokenTimeout': 'EIGHT_HOURS',
        'defaultAdvancedToolLaunch': 'NONE',
        'defaultEquityOrderDuration': 'DAY',
        'defaultEquityOrderLegInstruction': 'NONE',
        'defaultEquityOrderMarketSession': 'NORMAL',
        'defaultEquityOrderPriceLinkType': 'NONE',
        'defaultEquityOrderType': 'LIMIT',
        'defaultEquityQuantity': 0,
        'equityTaxLotMethod': 'FIFO',
        'expressTrading': True,
        'mutualFundTaxLotMethod': 'FIFO',
        'optionTaxLotMethod': 'FIFO'
    }
)

# Method 2, Update the User Preferences.
my_preferences = {
    'default_equity_order_leg_instruction': DefaultOrderLegInstruction.Buy,
    'default_equity_order_type': DefaultOrderType.Market,
    'default_equity_order_price_link_type': DefaultOrderPriceLinkType.Percent,
    'default_equity_order_duration': DefaultOrderDuration.NoneSpecified,
    'default_equity_order_market_session': DefaultOrderMarketSession.Normal,
    'mutual_fund_tax_lot_method': TaxLotMethod.Fifo,
    'option_tax_lot_method': TaxLotMethod.Fifo,
    'equity_tax_lot_method': TaxLotMethod.Fifo,
    'default_advanced_tool_launch': DefaultAdvancedToolLaunch.Ta,
    'auth_token_timeout': AuthTokenTimeout.EightHours
}

# Define a new data class that will store our preferences.
my_user_preferences = UserPreferences(**my_preferences)
user_info_service.update_user_preferences(
    account_id=account_number,
    preferences=my_user_preferences.to_dict()
)
