from td.credentials import TdCredentials
from td.client import TdAmeritradeClient
from td.config import TdConfiguration

config = TdConfiguration()

# Initialize our `Credentials` object.
td_credentials = TdCredentials.authentication_default()

# Initialize the `TdAmeritradeClient`
td_client = TdAmeritradeClient(
    credentials=td_credentials,
    config=config
)
