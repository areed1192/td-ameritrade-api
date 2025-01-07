"""Used to access the `Instruments` Services and metadata."""

from enum import Enum
from typing import Union
from schwab.session import CharlesSchwabSession


class Instruments():

    """
    ## Overview
    ----
    Allows the user to query and search for financial instruments
    inside of the Charles Schwab database. The endpoint allows multiple
    methods for searching including regex.
    """

    def __init__(self, session: CharlesSchwabSession) -> None:
        """Initializes the `Instruments` services.

        ### Parameters
        ----
        session : CharlesSchwabSession
            An authenticated `CharlesSchwabSession
            object.
        """

        self.session = session

    def search_instruments(self, symbol: str, projection: Union[str, Enum]) -> dict:
        """Search or retrieve instrument data, including fundamental data.

        ### Parameters
        ----
        symbol: str
            The symbol of the financial instrument you would
            like to search.

        projection: Union[str, Enum]
            The type of request, default is "symbol-search". The type of request
            include the following: `symbol-search`, `symbol-regex`, `desc-search`,
            `desc-regex` ,`fundamental`. For more info on these search types, please
            refer to the documentation link provided above.

        ### Usage
        ----
            >>> from schwab.enums import Instruments
            >>> instruments_service = client.instruments()
            >>> instruments_service.search_instruments(
                symbol='MSFT',
                projection='symbol-search'
            )
        """

        if isinstance(projection, Enum):
            projection = projection.value

        params = {
            'symbol': symbol,
            'projection': projection
        }

        content = self.session.make_request(
            method='get',
            endpoint='instruments',
            params=params
        )

        return content

    def get_instrument(self, cusip: str) -> dict:
        """Get an instrument by CUSIP.

        ### Parameters
        ----
        cusip: str
            The CUSIP Id.

        ### Usage
        ----
            >>> from schwab.enums import Instruments
            >>> instruments_service = client.instruments()
            >>> instruments_service.get_instrument(
                cusip='617446448'
            )
        """

        content = self.session.make_request(
            method='get',
            endpoint=f'instruments/{cusip}'
        )

        return content
