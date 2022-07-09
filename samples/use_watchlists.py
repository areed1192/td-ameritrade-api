from pprint import pprint
from td.client import TdAmeritradeClient

td_client = TdAmeritradeClient()
account_number = td_client.get_account_number()

# Initialize the `Watchlists` service.
watchlists_service = td_client.watchlists()

# Grab all watchlists for all accounts.
pprint(
    watchlists_service.get_all_accounts_watchlists()
)

# Grab a specific watchlist for a specific account.
pprint(
    watchlists_service.get_watchlist(
        account_id=account_number,
        watchlist_id='1003491055'
    )
)

# Grab all the watchlists for a specific account
pprint(
    watchlists_service.get_accounts_watchlist(
        account_id=account_number
    )
)

# Define some items for our watchlist.
watchlist_items = [
    {
        'quantity': 0.0,
        'averagePrice': 0.0,
        'commission': 0.0,
        'instrument': {
            'symbol': 'SPCE',
            'assetType': 'EQUITY'
        }
    },
    {
        'quantity': 0.0,
        'averagePrice': 0.0,
        'commission': 0.0,
        'instrument': {
            'symbol': 'UFO',
            'assetType': 'EQUITY'
        }
    }
]

# Create a new watchlist.
pprint(
    watchlists_service.create_watchlist(
        account_id=account_number,
        name='space companies',
        watchlist_items=watchlist_items
    )
)


# Update a watchlist.
pprint(
    watchlists_service.update_watchlist(
        account_id=account_number,
        watchlist_id='1637006076',
        name='Space_Companies_Current',
        watchlist_items=[
            {
                'quantity': 0.0,
                'averagePrice': 0.0,
                'commission': 0.0,
                'instrument': {
                    'symbol': 'TSLA',
                    'assetType': 'EQUITY'
                },
                'sequenceId': 3
            }
        ]
    )
)


# Define some items for our watchlist.
watchlist_items = [
    {
        'quantity': 0.0,
        'averagePrice': 0.0,
        'commission': 0.0,
        'instrument': {
            'symbol': 'SPCE',
            'assetType': 'EQUITY'
        }
    },
    {
        'quantity': 0.0,
        'averagePrice': 0.0,
        'commission': 0.0,
        'instrument': {
            'symbol': 'UFO',
            'assetType': 'EQUITY'
        }
    },
    {
        'quantity': 0.0,
        'averagePrice': 0.0,
        'commission': 0.0,
        'instrument': {
            'symbol': 'TSLA',
            'assetType': 'EQUITY'
        }
    },
    {
        'quantity': 0.0,
        'averagePrice': 0.0,
        'commission': 0.0,
        'instrument': {
            'symbol': 'NIO',
            'assetType': 'EQUITY'
        }
    }
]

# Replace a watchlist.
pprint(
    watchlists_service.update_watchlist(
        account_id=account_number,
        watchlist_id='1637006076',
        name='Space_Companies_And_Electric_Vehicles',
        watchlist_items=watchlist_items
    )
)

# Delete an existing watchlist.
pprint(
    watchlists_service.delete_watchlist(
        account_id=account_number,
        watchlist_id='1637006076'
    )
)
