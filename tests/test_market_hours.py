"""Unit tests for the `MarketHours` service."""

import unittest
from datetime import datetime
from unittest import TestCase
from configparser import ConfigParser

from schwab.client import CharlesSchwabClient
from schwab.credentials import CharlesSchwabCredentials

from schwab.utils.enums import Markets
from schwab.rest.market_hours import MarketHours


class TestMarketHourService(TestCase):
    """Will perform a unit test for the `CharlesSchwabClient` object."""

    def setUp(self) -> None:
        """Set up the `TdAmeritradeClient` Client."""

        # Initialize the Parser.
        config = ConfigParser()

        # Read the file.
        config.read("config/config.ini")

        # Get the specified credentials.
        client_id = config.get("main", "client_id")
        redirect_uri = config.get("main", "redirect_uri")

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

        self.service = self.client.market_hours()

    def test_creates_instance_of_client(self):
        """Create an instance and make sure it's a `CharlesSchwabClient` object."""

        self.assertIsInstance(self.client, CharlesSchwabClient)
        self.assertIsInstance(self.credentials, CharlesSchwabCredentials)

    def test_creates_instance_of_market_hours(self):
        """Create an instance and make sure it's a `MarketHours` object."""

        self.assertIsInstance(self.service, MarketHours)

    def test_get_single_market_hours(self):
        """Test grabbing market hours for a single market."""

        # Grab the market hours for the equity Markets.
        response = self.service.get_market_hours(market="equity", date=datetime.now())

        self.assertEqual("equity", list(response.keys())[0])

        # Grab the market hours for the equity Markets, using Enums.
        response = self.service.get_market_hours(
            market=Markets.EQUITY, date=datetime.now()
        )

        self.assertEqual("equity", list(response.keys())[0])

    def test_get_multiple_market_hours(self):
        """Test grabbing market hours for a multiple markets."""

        # Grab the market hours for the equity Markets.
        response = self.service.get_multiple_market_hours(
            markets=["equity", "bond"], date=datetime.now()
        )

        self.assertEqual("equity", list(response.keys())[0])

        # Grab the market hours for the equity Markets, using Enums.
        response = self.service.get_multiple_market_hours(
            markets=[Markets.EQUITY, Markets.BOND], date=datetime.now()
        )

        self.assertEqual("equity", list(response.keys())[0])

    def tearDown(self) -> None:
        """Teardown the `CharlesSchwabClient` Client."""

        del self.client
        del self.credentials


if __name__ == "__main__":
    unittest.main()
