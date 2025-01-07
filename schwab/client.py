"""This module contains the main client for the Charles Schwab API."""

from schwab.session import CharlesSchwabSession
from schwab.credentials import CharlesSchwabCredentials
from schwab.rest.quotes import Quotes
from schwab.rest.movers import Movers
from schwab.rest.accounts import Accounts
from schwab.rest.market_hours import MarketHours
from schwab.rest.instruments import Instruments
from schwab.rest.user_info import UserInfo
from schwab.rest.price_history import PriceHistory
from schwab.rest.options_chain import OptionsChain
from schwab.rest.watchlists import Watchlists
from schwab.rest.orders import Orders
from schwab.rest.saved_orders import SavedOrders
from schwab.streaming.client import StreamingApiClient


class CharlesSchwabClient():

    """
    ### Overview
    ----
    Handles initializing all the different API Services and ensures
    that your session is authenticated.
    """

    def __init__(self, credentials: CharlesSchwabCredentials) -> None:
        """Initializes the `CharlesSchwabClient` object.

        ### Parameters
        ----
        credentials : `CharlesSchwabCredentials`
            The `CharlesSchwabCredentials` object that contains
            the credentials needed to authenticate the session.
        """

        self.credentials = credentials
        self.session = CharlesSchwabSession(client=self)

    def __repr__(self):
        pass

    def quotes(self) -> Quotes:
        """Used to access the `Quotes` Services and metadata.

        ### Returns
        ---
        `Quotes`:
            The `Quotes` services Object.

        ### Usage
        ----
            >>> client = ChralesSchwabClient()
            >>> quotes_service = client.quotes()
        """

        return Quotes(session=self.session)

    def movers(self) -> Movers:
        """Used to access the `Movers` Services and metadata.

        ### Returns
        ---
        `Movers`:
            The `Movers` services Object.

        ### Usage
        ----
            >>> client = ChralesSchwabClient()
            >>> movers_service = client.movers()
        """

        return Movers(session=self.session)

    def accounts(self) -> Accounts:
        """Used to access the `Accounts` Services and metadata.

        ### Returns
        ---
        `Accounts`:
            The `Accounts` services Object.

        ### Usage
        ----
            >>> client = ChralesSchwabClient()
            >>> accounts_service = client.accounts()
        """

        return Accounts(session=self.session)

    def market_hours(self) -> MarketHours:
        """Used to access the `MarketHours` Services and metadata.

        ### Returns
        ---
        `MarketHours`:
            The `MarketHours` services Object.

        ### Usage
        ----
            >>> client = ChralesSchwabClient()
            >>> market_hours_service = client.market_hours()
        """

        return MarketHours(session=self.session)

    def instruments(self) -> Instruments:
        """Used to access the `Instruments` Services and metadata.

        ### Returns
        ---
        `Instruments`:
            The `Instruments` services Object.

        ### Usage
        ----
            >>> client = ChralesSchwabClient()
            >>> instruments_service = client.instruments()
        """

        return Instruments(session=self.session)

    def user_info(self) -> UserInfo:
        """Used to access the `UserInfo` Services and metadata.

        ### Returns
        ---
        `UserInfo`:
            The `UserInfo` services Object.

        ### Usage
        ----
            >>> client = ChralesSchwabClient()
            >>> user_info_service = client.user_info()
        """

        return UserInfo(session=self.session)

    def price_history(self) -> PriceHistory:
        """Used to access the `PriceHistory` Services and metadata.

        ### Returns
        ---
        `PriceHistory`:
            The `PriceHistory` services Object.

        ### Usage
        ----
            >>> client = ChralesSchwabClient()
            >>> price_history_service = client.price_history()
        """

        return PriceHistory(session=self.session)

    def options_chain(self) -> OptionsChain:
        """Used to access the `OptionsChain` Services and metadata.

        ### Returns
        ---
        `OptionsChain`:
            The `OptionsChain` services Object.

        ### Usage
        ----
            >>> client = ChralesSchwabClient()
            >>> options_chain_service = client.options_chain()
        """

        return OptionsChain(session=self.session)

    def watchlists(self) -> Watchlists:
        """Used to access the `Watchlists` Services and metadata.

        ### Returns
        ---
        `Watchlists`:
            The `Watchlists` services Object.

        ### Usage
        ----
            >>> client = ChralesSchwabClient()
            >>> watchlists_service = client.watchlists()
        """

        return Watchlists(session=self.session)

    def orders(self) -> Orders:
        """Used to access the `Orders` Services and metadata.

        ### Returns
        ---
        `Orders`:
            The `Orders` services Object.

        ### Usage
        ----
            >>> client = ChralesSchwabClient()
            >>> orders_service = client.orders()
        """

        return Orders(session=self.session)

    def saved_orders(self) -> SavedOrders:
        """Used to access the `SavedOrders` Services and metadata.

        ### Returns
        ---
        `SavedOrders`:
            The `SavedOrders` services Object.

        ### Usage
        ----
            >>> client = ChralesSchwabClient()
            >>> saved_orders_service = client.saved_orders()
        """

        return SavedOrders(session=self.session)

    def streaming_api_client(self) -> StreamingApiClient:
        """Used to access the `StreamingApiClient` Services and metadata.

        ### Returns
        ---
        `StreamingApiClient`:
            The `StreamingApiClient` services Object.

        ### Usage
        ----
            >>> client = ChralesSchwabClient()
            >>> streaming_api_service = client.streaming_api_client()
        """

        return StreamingApiClient(session=self.session)
