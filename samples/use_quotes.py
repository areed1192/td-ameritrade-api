from pprint import pprint
from td.client import TdAmeritradeClient

td_client = TdAmeritradeClient()

# Initialize the `Quotes` service.
quote_service = td_client.quotes()

# Grab a single quote.
pprint(
    quote_service.get_quote(instrument='AAPL')
)

# Grab multiple quotes.
pprint(
    quote_service.get_quotes(instruments=['AAPL', 'SQ'])
)
