"""Demonstrates how to use the Movers service."""

from pprint import pprint
from configparser import ConfigParser

from schwab.client import CharlesSchwabClient
from schwab.credentials import CharlesSchwabCredentials

from schwab.utils.enums import IndexSymbol
from schwab.utils.enums import Sort
from schwab.utils.enums import Frequency

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

# Initialize the `Movers` service.
movers_service = client.movers()

# Grab the 30 minute movers for the Dow Jones.
pprint(
    movers_service.get_movers(
        symbol_id="$DJI", sort=Sort.PERCENT_CHANGE_UP, frequency=Frequency.THIRTY
    )
)

# Grab the 30 minute movers for the Dow Jones.
pprint(
    movers_service.get_movers(
        symbol_id=IndexSymbol.DJI,
        sort=Sort.PERCENT_CHANGE_UP,
        frequency=Frequency.THIRTY,
    )
)
