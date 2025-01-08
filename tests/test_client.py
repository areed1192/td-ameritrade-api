"""Unit tests for the `CharlesSchwabClient` object."""

import unittest
from unittest import TestCase
from configparser import ConfigParser

from schwab.client import CharlesSchwabClient
from schwab.credentials import CharlesSchwabCredentials

from schwab.rest.quotes import Quotes
from schwab.rest.movers import Movers
from schwab.rest.accounts import Accounts
from schwab.rest.market_hours import MarketHours
from schwab.rest.instruments import Instruments
from schwab.rest.user_info import UserInfo
from schwab.rest.price_history import PriceHistory
from schwab.rest.options_chain import OptionsChain
from schwab.rest.orders import Orders


class TestClient(TestCase):
    """Will perform a unit test for the `CharlesSchwabClient` object."""

    def setUp(self) -> None:
        """Set up the `CharlesSchwabClient` Client."""

        # Initialize the Parser.
        config = ConfigParser()

        # Read the file.
        config.read("config/config.ini")

        # Get the specified credentials.
        client_id = config.get("main", "client_id")
        client_secret = config.get("main", "client_secret")
        redirect_uri = config.get("main", "redirect_uri")

        # Intialize our `CharlesSchwabCredentials` object.
        self.credentials = CharlesSchwabCredentials(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            credential_file="config/credentials.json",
        )

        # Initalize the `CharlesSchwabClient`
        self.client = CharlesSchwabClient(credentials=self.credentials)

    def test_creates_instance_of_client(self):
        """Create an instance and make sure it's a `CharlesSchwabClient` object."""

        self.assertIsInstance(self.client, CharlesSchwabClient)
        self.assertIsInstance(self.credentials, CharlesSchwabCredentials)

    def test_creates_instance_of_quote(self):
        """Create an instance and make sure it's a `Quotes` object."""

        self.assertIsInstance(self.client.quotes(), Quotes)

    def test_creates_instance_of_mover(self):
        """Create an instance and make sure it's a `Movers` object."""

        self.assertIsInstance(self.client.movers(), Movers)

    def test_creates_instance_of_accounts(self):
        """Create an instance and make sure it's a `Accounts` object."""

        self.assertIsInstance(self.client.accounts(), Accounts)

    def test_creates_instance_of_market_hours(self):
        """Create an instance and make sure it's a `MarketHours` object."""

        self.assertIsInstance(self.client.market_hours(), MarketHours)

    def test_creates_instance_of_instruments(self):
        """Create an instance and make sure it's a `Instruments` object."""

        self.assertIsInstance(self.client.instruments(), Instruments)

    def test_creates_instance_of_user_info(self):
        """Create an instance and make sure it's a `UserInfo` object."""

        self.assertIsInstance(self.client.user_info(), UserInfo)

    def test_creates_instance_of_price_history(self):
        """Create an instance and make sure it's a `PriceHistory` object."""

        self.assertIsInstance(self.client.price_history(), PriceHistory)

    def test_creates_instance_of_options_chain(self):
        """Create an instance and make sure it's a `OptionsChain` object."""

        self.assertIsInstance(self.client.options_chain(), OptionsChain)

    def test_creates_instance_of_orders(self):
        """Create an instance and make sure it's a `Orders` object."""

        self.assertIsInstance(self.client.orders(), Orders)

    def tearDown(self) -> None:
        """Teardown the `CharlesSchwabClient` Client."""

        del self.client
        del self.credentials


if __name__ == "__main__":
    unittest.main()
