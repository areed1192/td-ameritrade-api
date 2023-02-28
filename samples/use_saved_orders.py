from pprint import pprint
from td.credentials import TdCredentials
from td.client import TdAmeritradeClient
from td.config import TdConfiguration

# A config object
config = TdConfiguration("config-example/config.ini")

# Initialize the `TdAmeritradeClient`
td_client = TdAmeritradeClient()

account_number = config.default_account # pylint: disable=E1101:no-member

# Initialize the `SavedOrders` service.
saved_orders_service = td_client.saved_orders()

#
# Doesn't work currently, at least for me
#

# # Query all the saved orders for a specific account.
# pprint(
#     saved_orders_service.get_saved_orders_by_path(
#         account_id=account_number
#     )
# )

# # Query all our orders.
# pprint(
#     saved_orders_service.get_saved_order(
#         account_id=account_number,
#         saved_order_id='12695463'
#     )
# )

# # Define a fake saved order.
# fake_saved_order = {
#     'complexOrderStrategyType': 'NONE',
#     'duration': 'DAY',
#     'orderLegCollection': [
#         {
#             'instruction': 'BUY',
#             'instrument': {
#                 'assetType': 'EQUITY',
#                 'symbol': 'SQ'
#             },
#             'orderLegType': 'EQUITY',
#             'quantity': 1.0
#         }
#     ],
#     'orderStrategyType': 'SINGLE',
#     'orderType': 'MARKET',
#     'session': 'NORMAL'
# }

# # doesn't exist
# # saved_orders_service.place_saved_order(
# #     account_id=account_number,
# #     saved_order_dict=fake_saved_order
# # )


# # Define a new fake saved order.
# new_fake_saved_order = {
#     'complexOrderStrategyType': 'NONE',
#     'duration': 'DAY',
#     'orderLegCollection': [
#         {
#             'instruction': 'BUY',
#             'instrument': {
#                 'assetType': 'EQUITY',
#                 'symbol': 'SQ'
#             },
#             'orderLegType': 'EQUITY',
#             'quantity': 4.0  # changed this.
#         }
#     ],
#     'orderStrategyType': 'SINGLE',
#     'orderType': 'MARKET',
#     'session': 'NORMAL'
# }

# # Replace a Saved Order.
# saved_orders_service.replace_saved_order(
#     account_id=account_number,
#     saved_order_id='18034925',
#     saved_order_dict=new_fake_saved_order
# )

# # Delete a saved order.
# saved_orders_service.delete_saved_order(
#     account_id=account_number,
#     saved_order_id='18034918'
# )
