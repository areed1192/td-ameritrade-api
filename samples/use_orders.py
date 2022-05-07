from pprint import pprint
from td.config.get_config import config
from td.credentials import TdCredentials
from td.client import TdAmeritradeClient
from td.utils.enums import OrderStatus

# Initialize our `Credentials` object.
td_credentials = TdCredentials.authentication_default()

# Initialize the `TdAmeritradeClient`
td_client = TdAmeritradeClient(
    credentials=td_credentials
)

account_number = config.get('accounts', 'default')

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
