"""Demonstrates how to use the Accounts service."""

from pprint import pprint
from datetime import datetime
from configparser import ConfigParser

from schwab.client import CharlesSchwabClient
from schwab.credentials import CharlesSchwabCredentials

from schwab.utils.enums import TransactionTypes

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

# Initialize the `Accounts` service.
accounts_service = client.accounts()

all_accounts = accounts_service.get_account_numbers()
pprint(all_accounts)

# Find the account number and grab the hashvalue
for account in all_accounts:
    if account["accountNumber"] == account_number:
        account_number_hash = account["hashValue"]
        break


# Grab all the Positions and Orders for a specific account.
pprint(
    accounts_service.get_accounts(
        account_id=account_number_hash, include_positions=True
    )
)

# Grab all the Positions and Orders for all my accounts.
pprint(accounts_service.get_accounts(include_positions=True))

# Grab all the transactions for a specific account.
# This will automatically convert into UTC if you pass a datetime object.
pprint(
    accounts_service.get_transactions(
        account_id=account_number_hash,
        end_date=datetime(year=2025, month=1, day=1),
        start_date=datetime(year=2024, month=12, day=1),
        transaction_type=TransactionTypes.TRADE,
    )
)

# Grab a specific transaction for a specific account.
pprint(
    accounts_service.get_transaction(
        account_id=account_number_hash, transaction_id="27444883992"
    )
)
