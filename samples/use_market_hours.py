"""Demonstrates how to get market hours."""

from pprint import pprint
from datetime import datetime
from configparser import ConfigParser

from schwab.client import CharlesSchwabClient
from schwab.credentials import CharlesSchwabCredentials

from schwab.utils.enums import Markets

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

# Initialize the `MarketHours` service.
market_hours_service = client.market_hours()

# Grab the market hours
pprint(
    market_hours_service.get_multiple_market_hours(
        markets=["EQUITY", Markets.Bond], date=datetime.now()
    )
)

# Grab the hours for a specific market.
pprint(market_hours_service.get_market_hours(market="EQUITY", date=datetime.now()))
