from pprint import pprint
from td.credentials import TdCredentials
from td.client import TdAmeritradeClient
from td.config.get_config import config

# Initialize our `Credentials` object.
td_credentials = TdCredentials.authentication_default()

# Initialize the `TdAmeritradeClient`
td_client = TdAmeritradeClient(
    credentials=td_credentials
)

account_number = config.get('accounts', 'default')

# Initialize the `Watchlists` service.
watchlists_service = td_client.watchlists()

# Grab all watchlists for all accounts.
pprint(
    watchlists_service.get_all_accounts_watchlists()
)

#
# Doesn't work currently, at least for me
#

# # Grab a specific watchlist for a specific account.
# pprint(
#     watchlists_service.get_watchlist(
#         account_id=account_number,
#         watchlist_id='1003491055'
#     )
# )

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

#
# Doesn't work currently, at least for me
#

# # Create a new watchlist.
# pprint(
#     watchlists_service.create_watchlist(
#         account_id=account_number,
#         name='space companies',
#         watchlist_items=watchlist_items
#     )
# )

#
# Doesn't work currently, at least for me
#

# # Update a watchlist.
# pprint(
#     watchlists_service.update_watchlist(
#         account_id=account_number,
#         watchlist_id='1637006076',
#         name='Space_Companies_Current',
#         watchlist_items=[
#             {
#                 'quantity': 0.0,
#                 'averagePrice': 0.0,
#                 'commission': 0.0,
#                 'instrument': {
#                     'symbol': 'TSLA',
#                     'assetType': 'EQUITY'
#                 },
#                 'sequenceId': 3
#             }
#         ]
#     )
# )


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

#
# Doesn't work currently, at least for me
#

# # Replace a watchlist.
# pprint(
#     watchlists_service.update_watchlist(
#         account_id=account_number,
#         watchlist_id='1637006076',
#         name='Space_Companies_And_Electric_Vehicles',
#         watchlist_items=watchlist_items
#     )
# )

# # Delete an existing watchlist.
# pprint(
#     watchlists_service.delete_watchlist(
#         account_id=account_number,
#         watchlist_id='1637006076'
#     )
# )
