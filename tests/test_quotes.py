"""Unit tests for the `Quotes` service."""

import unittest
from unittest import TestCase
from configparser import ConfigParser

from schwab.client import CharlesSchwabClient
from schwab.credentials import CharlesSchwabCredentials

from schwab.rest.quotes import Quotes


class TestQuotesService(TestCase):
    """Will perform a unit test for the `Quotes` service object."""

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

        self.service = self.client.quotes()

    def test_creates_instance_of_client(self):
        """Create an instance and make sure it's a `CharlesSchwabClient` object."""

        self.assertIsInstance(self.client, CharlesSchwabClient)
        self.assertIsInstance(self.credentials, CharlesSchwabCredentials)

    def test_creates_instance_of_quote(self):
        """Create an instance and make sure it's a `Quotes` object."""

        self.assertIsInstance(self.service, Quotes)

    def test_get_quote(self):
        """Test grabbing a single quote."""

        response = self.service.get_quote(symbol_id="AAPL")
        self.assertEqual("AAPL", list(response.keys())[0])

    def test_get_quotes(self):
        """Test grabbing multiple quotes."""

        response = self.service.get_quotes(symbol_ids=["AAPL", "SQ"])
        self.assertListEqual(["AAPL", "SQ"], list(response.keys()))

    def tearDown(self) -> None:
        """Teardown the `CharlesSchwabClient` Client."""

        del self.client
        del self.credentials


if __name__ == "__main__":
    unittest.main()
