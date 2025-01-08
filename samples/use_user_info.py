"""Demonstrates how to use the User Info Service."""

from pprint import pprint
from configparser import ConfigParser

from schwab.client import CharlesSchwabClient
from schwab.credentials import CharlesSchwabCredentials

from schwab.utils.enums import DefaultOrderDuration
from schwab.utils.enums import DefaultAdvancedToolLaunch
from schwab.utils.enums import DefaultOrderLegInstruction
from schwab.utils.enums import DefaultOrderMarketSession
from schwab.utils.enums import DefaultOrderPriceLinkType
from schwab.utils.enums import DefaultOrderType
from schwab.utils.enums import TaxLotMethod
from schwab.utils.enums import AuthTokenTimeout

from schwab.utils.user_preferences import UserPreferences

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read("config/config.ini")

# Get the specified credentials.
client_id = config.get("main", "client_id")
client_secret = config.get("main", "client_secret")
redirect_uri = config.get("main", "redirect_uri")
account_number = config.get("main", "account_number")

# Intialize our `CharlesSchwabCredentials` object.
credentials = CharlesSchwabCredentials(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    credential_file="config/credentials.json",
)

# Initalize the `CharlesSchwabClient`
client = CharlesSchwabClient(credentials=credentials)

# Initialize the `UserInfo` service.
user_info_service = client.user_info()

# Grab the preferences for a specific account.
pprint(user_info_service.get_preferences(account_id=account_number))

# Grab the streamer subscription keys.
pprint(user_info_service.get_streamer_subscription_keys(account_ids=[account_number]))

# Grab User Principals.
pprint(user_info_service.get_user_principals())

# Method 1, Update the User Preferences.
user_info_service.update_user_preferences(
    account_id=account_number,
    preferences={
        "authTokenTimeout": "EIGHT_HOURS",
        "defaultAdvancedToolLaunch": "NONE",
        "defaultEquityOrderDuration": "DAY",
        "defaultEquityOrderLegInstruction": "NONE",
        "defaultEquityOrderMarketSession": "NORMAL",
        "defaultEquityOrderPriceLinkType": "NONE",
        "defaultEquityOrderType": "LIMIT",
        "defaultEquityQuantity": 0,
        "equityTaxLotMethod": "FIFO",
        "expressTrading": True,
        "mutualFundTaxLotMethod": "FIFO",
        "optionTaxLotMethod": "FIFO",
    },
)

# Method 2, Update the User Preferences.
my_preferences = {
    "default_equity_order_leg_instruction": DefaultOrderLegInstruction.BUY,
    "default_equity_order_type": DefaultOrderType.MARKET,
    "default_equity_order_price_link_type": DefaultOrderPriceLinkType.PERCENT,
    "default_equity_order_duration": DefaultOrderDuration.NONE_SPECIFIED,
    "default_equity_order_market_session": DefaultOrderMarketSession.NORMAL,
    "mutual_fund_tax_lot_method": TaxLotMethod.FIFO,
    "option_tax_lot_method": TaxLotMethod.FIFO,
    "equity_tax_lot_method": TaxLotMethod.FIFO,
    "default_advanced_tool_launch": DefaultAdvancedToolLaunch.TA,
    "auth_token_timeout": AuthTokenTimeout.EIGHT_HOURS,
}

# Define a new data class that will store our preferences.
my_user_perferences = UserPreferences(**my_preferences)
user_info_service.update_user_preferences(
    account_id=account_number, preferences=my_user_perferences.to_dict()
)
