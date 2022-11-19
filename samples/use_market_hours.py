from pprint import pprint
from datetime import datetime
from td.credentials import TdCredentials
from td.client import TdAmeritradeClient
from td.config import TdConfiguration
from td.utils.enums import Markets

config = TdConfiguration("config/config.ini")

# Initialize our `Credentials` object.
td_credentials = TdCredentials.authentication_default()

# Initialize the `TdAmeritradeClient`
td_client = TdAmeritradeClient(
    credentials=td_credentials,
    config=config
)

# Initialize the `MarketHours` service.
market_hours_service = td_client.market_hours()

# Grab the market hours
pprint(
    market_hours_service.get_multiple_market_hours(
        markets=['EQUITY', Markets.Bond],
        date_time=datetime.now()
    )
)

# Grab the hours for a specific market.
pprint(
    market_hours_service.get_market_hours(
        market='EQUITY',
        date_time=datetime.now()
    )
)
