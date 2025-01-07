"""This is an example of how to use OAuth2 to authenticate with Schwab"""

from pprint import pprint
from configparser import ConfigParser

from schwab.client import CharlesSchwabClient
from schwab.credentials import CharlesSchwabCredentials

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('config/config.ini')

# Get the specified credentials.
client_id = config.get('main', 'client_id')
client_secret = config.get('main', 'client_secret')
redirect_uri = config.get('main', 'redirect_uri')

# Intialize our `CharlesSchwabCredentials` object.
credentials = CharlesSchwabCredentials(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    credential_file='config/credentials.json'
)

print(credentials.client_id)
print(credentials.client_secret)
print(credentials.redirect_uri)
