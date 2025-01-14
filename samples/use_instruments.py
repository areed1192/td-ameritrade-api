"""Demonstrates how to use the Instruments service."""

from pprint import pprint
from configparser import ConfigParser

from schwab.client import CharlesSchwabClient
from schwab.credentials import CharlesSchwabCredentials

from schwab.utils.enums import Projections

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

# Initialize the `Instruments` service.
instruments_service = client.instruments()

# Search for a symbol.
pprint(
    instruments_service.search_instruments(symbol="MSFT", projection="symbol-search")
)

# Search for fundamental data.
pprint(
    instruments_service.search_instruments(
        symbol="MSFT", projection=Projections.FUNDAMENTAL
    )
)

# Search for a symbol using regular expression.
pprint(
    instruments_service.search_instruments(
        symbol="MS*", projection=Projections.SYMBOL_REGEX
    )
)

# Search for companies using description key words.
pprint(
    instruments_service.search_instruments(
        symbol="Technology", projection=Projections.DESCRIPTION_SEARCH
    )
)

# Search for companies using description regular expression.
pprint(
    instruments_service.search_instruments(
        symbol="[Quantum Computing]", projection=Projections.DESCRIPTION_REGEX
    )
)

# Get an Insturment by using their CUSIP.
pprint(instruments_service.get_instrument(cusip="617446448"))
