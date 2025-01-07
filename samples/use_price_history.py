"""Demonstrates for using the Price History service."""

from datetime import datetime
from datetime import timedelta
from configparser import ConfigParser

from schwab.client import CharlesSchwabClient
from schwab.credentials import CharlesSchwabCredentials

from schwab.utils.enums import PeriodType
from schwab.utils.enums import FrequencyType

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read("config/config.ini")

# Get the specified credentials.
client_id = config.get("main", "client_id")
client_secret = config.get("main", "client_secret")
redirect_uri = config.get("main", "redirect_uri")

# Intialize our `CharlesSchwabCredentials` object.
credentials = CharlesSchwabCredentials(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    credential_file="config/credentials.json",
)

# Initalize the `CharlesSchwabClient`
client = CharlesSchwabClient(credentials=credentials)

# Initialize the `PriceHistory` service.
price_history_service = client.price_history()

# Grab the Price History, with enums.
price_history = price_history_service.get_price_history(
    symbol="MSFT",
    frequency_type=FrequencyType.Minute,
    frequency=1,
    period_type=PeriodType.Day,
    period=10,
    extended_hours_needed=False,
)
# pprint(price_history)

# Grab the Price History, without enums.
price_history = price_history_service.get_price_history(
    symbol="MSFT",
    frequency_type="minute",
    frequency=1,
    period_type="day",
    period=10,
    extended_hours_needed=False,
)

# The max look back period for minute data is 31 Days.
end_date = datetime.now()
start_date = datetime.now() - timedelta(seconds=60)

# Grab the Price History, custom time frame.
price_history = price_history_service.get_price_history(
    symbol="MSFT",
    frequency_type=FrequencyType.Minute,
    frequency=1,
    start_date=1628260200000,
    end_date=1628260220000,
    extended_hours_needed=False,
)
print(price_history["candles"])
