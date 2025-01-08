"""Demonstrates how to get quotes for a single or multiple instruments."""

from pprint import pprint
from configparser import ConfigParser

from schwab.client import CharlesSchwabClient
from schwab.credentials import CharlesSchwabCredentials

from schwab.utils.enums import QuoteRequest

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

# Initialize the `Quotes` service.
quote_service = client.quotes()

# Grab a single quote.
pprint(quote_service.get_quote(symbol_id="AAPL"))

# Grab multiple quotes.
pprint(
    quote_service.get_quotes(symbol_ids=["AAPL", "SQ"], fields=QuoteRequest.EXTENDED)
)
