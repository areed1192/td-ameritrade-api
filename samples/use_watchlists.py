"""This sample demonstrates how to use the `Watchlists` service."""

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

# Initialize the `Watchlists` service.
watchlists_service = client.watchlists()

# Grab all watchlists for all accounts.
pprint(watchlists_service.get_all_accounts_watchlists())

# Grab a specific watchlist for a specific account.
pprint(
    watchlists_service.get_watchlist(
        account_id=account_number, watchlist_id="1003491055"
    )
)

# Grab all the watchlists for a specific account
pprint(watchlists_service.get_accounts_watchlist(account_id=account_number))

# Define some items for our watchlist.
watchlist_items = [
    {
        "quantity": 0.0,
        "averagePrice": 0.0,
        "commission": 0.0,
        "instrument": {"symbol": "SPCE", "assetType": "EQUITY"},
    },
    {
        "quantity": 0.0,
        "averagePrice": 0.0,
        "commission": 0.0,
        "instrument": {"symbol": "UFO", "assetType": "EQUITY"},
    },
]

# Create a new watchlist.
pprint(
    watchlists_service.create_watchlist(
        account_id=account_number,
        name="space companies",
        watchlist_items=watchlist_items,
    )
)


# Update a watchlist.
pprint(
    watchlists_service.update_watchlist(
        account_id=account_number,
        watchlist_id="1637006076",
        name="Space_Companies_Current",
        watchlist_items=[
            {
                "quantity": 0.0,
                "averagePrice": 0.0,
                "commission": 0.0,
                "instrument": {"symbol": "TSLA", "assetType": "EQUITY"},
                "sequenceId": 3,
            }
        ],
    )
)


# Define some items for our watchlist.
watchlist_items = [
    {
        "quantity": 0.0,
        "averagePrice": 0.0,
        "commission": 0.0,
        "instrument": {"symbol": "SPCE", "assetType": "EQUITY"},
    },
    {
        "quantity": 0.0,
        "averagePrice": 0.0,
        "commission": 0.0,
        "instrument": {"symbol": "UFO", "assetType": "EQUITY"},
    },
    {
        "quantity": 0.0,
        "averagePrice": 0.0,
        "commission": 0.0,
        "instrument": {"symbol": "TSLA", "assetType": "EQUITY"},
    },
    {
        "quantity": 0.0,
        "averagePrice": 0.0,
        "commission": 0.0,
        "instrument": {"symbol": "NIO", "assetType": "EQUITY"},
    },
]

# Replace a watchlist.
pprint(
    watchlists_service.update_watchlist(
        account_id=account_number,
        watchlist_id="1637006076",
        name="Space_Companies_And_Electric_Vehicles",
        watchlist_items=watchlist_items,
    )
)

# Delete an existing watchlist.
pprint(
    watchlists_service.delete_watchlist(
        account_id=account_number, watchlist_id="1637006076"
    )
)
