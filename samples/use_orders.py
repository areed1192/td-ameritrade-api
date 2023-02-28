from pprint import pprint
from td.credentials import TdCredentials
from td.client import TdAmeritradeClient
from td.utils.enums import OrderStatus
from td.config import TdConfiguration

# A config object
config = TdConfiguration("config-example/config.ini")

# Initialize the `TdAmeritradeClient`
td_client = TdAmeritradeClient()

account_number = config.default_account # pylint: disable=E1101:no-member

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
