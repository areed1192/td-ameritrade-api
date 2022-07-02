from pprint import pprint
from td.client import TdAmeritradeClient
from td.utils.enums import OrderStatus

td_client = TdAmeritradeClient()
account_number = td_client.get_account_number()

# Initialize the `Orders` service.
orders_service = td_client.orders()

# Query all our orders for a specific account.
pprint(
    orders_service.get_orders_by_path(
        account_id=account_number,
        order_status=OrderStatus.Filled
    )
)

# Query all our orders.
pprint(
    orders_service.get_orders_by_query()
)
