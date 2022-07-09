from pprint import pprint
from td.client import TdAmeritradeClient
from td.utils.enums import TransactionTypes

td_client = TdAmeritradeClient()

account_number = td_client.get_account_number()

# Initialize the `Accounts` service.
accounts_service = td_client.accounts()

# Grab all the Positions and Orders for a specific account.
pprint(
    accounts_service.get_accounts(
        account_id=account_number,
        include_orders=True,
        include_positions=True
    )
)

# Grab all the Positions and Orders for all my accounts.
pprint(
    accounts_service.get_accounts(
        include_orders=True,
        include_positions=True
    )
)

# Grab all the transactions for a specific account.
pprint(
    accounts_service.get_transactions(
        account_id=account_number,
        transaction_type=TransactionTypes.All
    )
)

# Grab a specific transaction for a specific account.
pprint(
    accounts_service.get_transaction(
        account_id=account_number,
        transaction_id='27444883992'
    )
)
