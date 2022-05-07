from pprint import pprint
from td.credentials import TdCredentials
from td.client import TdAmeritradeClient

# Initialize our `Credentials` object.
td_credentials = TdCredentials.authentication_default()

# Initialize the `TdAmeritradeClient`
td_client = TdAmeritradeClient(
    credentials=td_credentials
)

# Initialize the `Movers` service.
movers_service = td_client.movers()

# Grab the top 10 percentage up movers.
pprint(
    movers_service.get_movers(
        index='$DJI',
        direction='up',
        change='percent'
    )
)
