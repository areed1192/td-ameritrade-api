"""Demonstrates how to use the Saved Orders service."""

from pprint import pprint
from configparser import ConfigParser

from schwab.client import CharlesSchwabClient
from schwab.credentials import CharlesSchwabCredentials

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

# Initialize the `SavedOrders` service.
saved_orders_service = client.saved_orders()

# Query all the saved orders for a specific account.
pprint(saved_orders_service.get_saved_orders_by_path(account_id=account_number))

# Query all our orders.
pprint(
    saved_orders_service.get_saved_order(
        account_id=account_number, saved_order_id="12695463"
    )
)

# Define a fake saved order.
fake_saved_order = {
    "complexOrderStrategyType": "NONE",
    "duration": "DAY",
    "orderLegCollection": [
        {
            "instruction": "BUY",
            "instrument": {"assetType": "EQUITY", "symbol": "SQ"},
            "orderLegType": "EQUITY",
            "quantity": 1.0,
        }
    ],
    "orderStrategyType": "SINGLE",
    "orderType": "MARKET",
    "session": "NORMAL",
}

saved_orders_service.place_saved_order(
    account_id=account_number, saved_order_dict=fake_saved_order
)


# Define a new fake saved order.
new_fake_saved_order = {
    "complexOrderStrategyType": "NONE",
    "duration": "DAY",
    "orderLegCollection": [
        {
            "instruction": "BUY",
            "instrument": {"assetType": "EQUITY", "symbol": "SQ"},
            "orderLegType": "EQUITY",
            "quantity": 4.0,  # changed this.
        }
    ],
    "orderStrategyType": "SINGLE",
    "orderType": "MARKET",
    "session": "NORMAL",
}

# Replace a Saved Order.
saved_orders_service.replace_saved_order(
    account_id=account_number,
    saved_order_id="18034925",
    saved_order_dict=new_fake_saved_order,
)

# Delete a saved order.
saved_orders_service.cancel_saved_order(
    account_id=account_number, saved_order_id="18034918"
)
