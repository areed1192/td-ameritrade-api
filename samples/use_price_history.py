from pprint import pprint
from td.credentials import TdCredentials
from td.client import TdAmeritradeClient
from td.utils.enums import PeriodType
from td.utils.enums import FrequencyType
from datetime import datetime
from datetime import timedelta

# Initialize our `Credentials` object.
td_credentials = TdCredentials.authentication_default()

# Initialize the `TdAmeritradeClient`
td_client = TdAmeritradeClient(
    credentials=td_credentials
)

# Initialize the `PriceHistory` service.
price_history_service = td_client.price_history()

# Grab the Price History, with enums.
price_history = price_history_service.get_price_history(
    symbol='MSFT',
    frequency_type=FrequencyType.Minute,
    frequency=1,
    period_type=PeriodType.Day,
    period=10,
    extended_hours_needed=False
)
pprint(price_history)

# Grab the Price History, without enums.
price_history = price_history_service.get_price_history(
    symbol='MSFT',
    frequency_type='minute',
    frequency=1,
    period_type='day',
    period=10,
    extended_hours_needed=False
)
pprint(price_history)

# The max look back period for minute data is 31 Days.
end_date = datetime.now()
start_date = datetime.now() - timedelta(days=31)

# Grab the Price History, custom time frame.
price_history = price_history_service.get_price_history(
    symbol='MSFT',
    frequency_type=FrequencyType.Minute,
    frequency=1,
    start_date=start_date,
    end_date=end_date,
    extended_hours_needed=False
)
print(len(price_history['candles']))
