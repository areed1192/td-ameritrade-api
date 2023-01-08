from pprint import pprint
import string
from td.credentials import TdCredentials
from td.client import TdAmeritradeClient
from td.config import TdConfiguration
from td.utils.enums import Projections

# Initialize our `Credentials` object.
td_credentials = TdCredentials.authentication_default()

# A config object
config = TdConfiguration()

# Initialize the `TdAmeritradeClient`
td_client = TdAmeritradeClient(
    credentials=td_credentials,
    config=config
)

# Initialize the `Instruments` service.
instruments_service = td_client.instruments()

az_Upper = string.ascii_uppercase

count = 0
result_list = []
for char in az_Upper:
    symbol = "\$" + char + ".*"
    # Search for a symbol using regular expression.
    result = instruments_service.search_instruments(
        symbol=symbol,
        projection=Projections.SymbolRegex
    )
    if (result):
        count += 1
        result_list.append(result)
print(count)
