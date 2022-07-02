from pprint import pprint
from td.client import TdAmeritradeClient

td_client = TdAmeritradeClient()

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
