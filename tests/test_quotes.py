import unittest
from unittest import TestCase

from td.rest.quotes import Quotes
from td.client import TdAmeritradeClient
from td.config import TdConfiguration
from td.credentials import TdCredentials


class TestQuotesService(TestCase):

    """Will perform a unit test for the `Quotes` service object."""

    def setUp(self) -> None:
        """Set up the `TdAmeritradeClient` Client."""

        # Initialize our `Credentials` object.
        self.td_credentials = TdCredentials.authentication_default()

        self.config = TdConfiguration()

        # Initialize the `TdAmeritradeClient`
        self.td_client = TdAmeritradeClient(
            credentials=self.td_credentials,
            config=self.config
        )

        self.service = self.td_client.quotes()

    def test_creates_instance_of_client(self):
        """Create an instance and make sure it's a `TdAmeritradeClient` object."""

        self.assertIsInstance(self.td_client, TdAmeritradeClient)
        self.assertIsInstance(self.td_credentials, TdCredentials)

    def test_creates_instance_of_quote(self):
        """Create an instance and make sure it's a `Quotes` object."""

        self.assertIsInstance(self.service, Quotes)

    def test_get_quote(self):
        """Test grabbing a single quote."""

        response = self.service.get_quote(instrument='AAPL')
        self.assertEqual('AAPL', list(response.keys())[0])

    def test_get_quotes(self):
        """Test grabbing multiple quotes."""

        response = self.service.get_quotes(instruments=['AAPL', 'SQ'])
        self.assertListEqual(['AAPL', 'SQ'], list(response.keys()))

    def tearDown(self) -> None:
        """Teardown the `TdAmeritradeClient` Client."""

        del self.td_client
        del self.td_credentials


if __name__ == '__main__':
    unittest.main()
