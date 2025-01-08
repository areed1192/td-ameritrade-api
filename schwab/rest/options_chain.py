"""Used to access the `OptionsChain` Services and metadata."""

from schwab.session import CharlesSchwabSession
from schwab.utils.option_chain import OptionChainQuery


class OptionsChain:
    """
    ## Overview
    ----
    Allows the user to query options chain data.
    """

    def __init__(self, session: CharlesSchwabSession) -> None:
        """Initializes the `OptionsChain` services.

        ### Parameters
        ----
        session : CharlesSchwabSession
            An authenticated `CharlesSchwabSession
            object.
        """

        self.session = session

    def get_option_chain(
        self,
        option_chain_query: OptionChainQuery = None,
        option_chain_dict: dict = None,
        raise_validation_errors: bool = True,
    ) -> dict:
        """Get Option Chain including information on options
        contracts associated with each expiration.

        ### Parameters
        ----
        option_chain_query: OptionChainQuery (optional, Default=None)
            Represents a query object that can be constructed from
            the `schwab.utils` file. This is the preferred method of querying
            of data because additional checks are put in place.

        option_chain_dict: dict (optional, Default=None)
            Represents a query constructed from an ordinary python
            dictionary object. No additional checks will be made on the
            inputs to validate them.

        raise_validation_errors: bool (optional, Default=True)
            Applies only to the `option_chain_query` argument. If set to `True`
            any validation errors will be raise to the user regardless if the
            library can fix them or not. If set to `False` the library will remove
            invalid arguments or replace them with valid ones when approriate.

        ### Usage
        ----
            >>> options_chain_service = client.options_chain()
            >>> # Method 1: Using the `OptionChainQuery` object.
            >>> option_chain_query = OptionChainQuery(
                    symbol='MSFT',
                    contract_type=ContractType.Call,
                    expiration_month=ExpirationMonth.June,
                    option_type=OptionType.StandardContracts,
                    option_range=OptionaRange.InTheMoney,
                    include_quotes=True
                )
            >>> options_chain_service.get_option_chain(
                    option_chain_query=option_chain_query
                )
            >>> # Method 2: Using a `Dictionary` object.
            >>> option_chain_dict = {
                    'symbol': 'MSFT',
                    'contractType': 'CALL',
                    'expirationMonth': 'JUN',
                    'optionType': 'SC',
                    'range': 'ITM',
                    'includeQuotes': True
                }
            >>> options_chain_service.get_option_chain(
                    option_chain_dict=option_chain_dict
                )
        """

        if option_chain_query:
            params = option_chain_query.to_dict(raise_errors=raise_validation_errors)
        else:
            params = option_chain_dict

        content = self.session.make_request(
            method="get", endpoint="chains", params=params
        )

        return content

    def get_option_expiration_chain(self, symbol: str) -> dict:
        """Get Option Expiration (Series) information for an optionable symbol.
        Does not include individual options contracts for the underlying.

        ### Parameters
        ----
        symbol: str
            A valid symbol for the underlying security.

        ### Usage
        ----
            >>> options_chain_service = client.options_chain()
            >>> options_chain_service.get_option_expiration_chain(
                    symbol='MSFT'
                )
        """

        content = self.session.make_request(
            method="get", endpoint="expirationchain", params={"symbol": symbol}
        )

        return content
