"""Unit tests for the `OptionsChain` service."""

import unittest
from unittest import TestCase
from configparser import ConfigParser

from schwab.client import CharlesSchwabClient
from schwab.credentials import CharlesSchwabCredentials

from schwab.utils.enums import OptionaRange
from schwab.utils.enums import OptionType
from schwab.utils.enums import ContractType
from schwab.utils.enums import ExpirationMonth

from schwab.rest.options_chain import OptionsChain
from schwab.rest.options_chain import OptionChainQuery


class TestOptionsChainService(TestCase):
    """Will perform a unit test for the `OptionsChain` object."""

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

        self.service = self.client.options_chain()

    def test_creates_instance_of_client(self):
        """Create an instance and make sure it's a `CharlesSchwabClient` object."""

        self.assertIsInstance(self.client, CharlesSchwabClient)
        self.assertIsInstance(self.credentials, CharlesSchwabCredentials)

    def test_creates_instance_of_service(self):
        """Create an instance and make sure it's a `OptionsChain` object."""

        self.assertIsInstance(self.service, OptionsChain)

    def test_creates_instance_of_options_chain_query(self):
        """Create an instance and make sure it's a `OptionsChainQuery` object."""

        # Build a Query.
        option_chain_query = OptionChainQuery(
            symbol="MSFT",
            contract_type=ContractType.Call,
            expiration_month=ExpirationMonth.June,
            option_type=OptionType.StandardContracts,
            option_range=OptionaRange.InTheMoney,
            include_quotes=True,
        )

        self.assertIsInstance(option_chain_query, OptionChainQuery)

    def test_get_option_chains_through_query_object(self):
        """Test grabbing option chains data using the `Query` object."""

        # Build a Query.
        option_chain_query = OptionChainQuery(
            symbol="MSFT",
            contract_type=ContractType.Call,
            expiration_month=ExpirationMonth.June,
            option_type=OptionType.StandardContracts,
            option_range=OptionaRange.InTheMoney,
            include_quotes=True,
        )

        # Query the Options Data.
        options_data = self.service.get_option_chain(
            option_chain_query=option_chain_query
        )

        self.assertIn("numberOfContracts", list(options_data.keys()))

    def test_get_option_chains(self):
        """Test grabbing option chains data using a dictionary object."""

        # Build a Query.
        option_chain_dict = {
            "symbol": "MSFT",
            "contractType": "CALL",
            "expirationMonth": "JUN",
            "optionType": "SC",
            "range": "ITM",
            "includeQuotes": True,
        }

        # Query the Options Data.
        options_data = self.service.get_option_chain(
            option_chain_dict=option_chain_dict
        )

        self.assertIn("numberOfContracts", list(options_data.keys()))

    def tearDown(self) -> None:
        """Teardown the `CharlesSchwabClient` Client."""

        del self.client
        del self.credentials


if __name__ == "__main__":
    unittest.main()
