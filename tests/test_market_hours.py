import unittest
from datetime import datetime
from unittest import TestCase

from td.utils.enums import Markets
from td.credentials import TdCredentials
from td.client import TdAmeritradeClient
from td.config import TdConfiguration
from td.rest.market_hours import MarketHours


class TestMarketHourService(TestCase):

    """Will perform a unit test for the `TdAmeritradeClient` object."""

    def setUp(self) -> None:
        """Set up the `TdAmeritradeClient` Client."""

        # Initialize our `Credentials` object.
        self.td_credentials = TdCredentials.authentication_default()

        self.config = TdConfiguration("config/config.ini")

        # Initialize the `TdAmeritradeClient`
        self.td_client = TdAmeritradeClient(
            credentials=self.td_credentials,
            config=self.config
        )

        self.service = self.td_client.market_hours()

    def test_creates_instance_of_client(self):
        """Create an instance and make sure it's a `TdAmeritradeClient` object."""

        self.assertIsInstance(self.td_client, TdAmeritradeClient)
        self.assertIsInstance(self.td_credentials, TdCredentials)

    def test_creates_instance_of_market_hours(self):
        """Create an instance and make sure it's a `MarketHours` object."""

        self.assertIsInstance(self.service, MarketHours)

    def test_get_single_market_hours(self):
        """Test grabbing market hours for a single market."""

        # Grab the market hours for the equity Markets.
        response = self.service.get_market_hours(
            market='EQUITY',
            date_time=datetime.now()
        )

        self.assertEqual('equity', list(response.keys())[0])

        # Grab the market hours for the equity Markets, using Enums.
        response = self.service.get_market_hours(
            market=Markets.Equity,
            date_time=datetime.now()
        )

        self.assertEqual('equity', list(response.keys())[0])

    def test_get_multiple_market_hours(self):
        """Test grabbing market hours for a multiple markets."""

        # Grab the market hours for the equity Markets.
        response = self.service.get_multiple_market_hours(
            markets=['EQUITY', 'BOND'],
            date_time=datetime.now()
        )

        self.assertEqual('bond', list(response.keys())[0])

        # Grab the market hours for the equity Markets, using Enums.
        response = self.service.get_multiple_market_hours(
            markets=[Markets.Equity, Markets.Bond],
            date_time=datetime.now()
        )

        self.assertEqual('equity', list(response.keys())[1])

    def tearDown(self) -> None:
        """Teardown the `TdAmeritradeClient` Client."""

        del self.td_client
        del self.td_credentials


if __name__ == '__main__':
    unittest.main()
