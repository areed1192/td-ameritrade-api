"""Used to access the `MarketHours` Services and metadata."""

from enum import Enum
from typing import List
from typing import Union
from datetime import date as date_type
from datetime import datetime
from schwab.session import CharlesSchwabSession


class MarketHours():

    """
    ## Overview
    ----
    Allows the user query the different market hours for
    the different financial markets.
    """

    def __init__(self, session: CharlesSchwabSession) -> None:
        """Initializes the `MarketHours` services.

        ### Parameters
        ----
        session : CharlesSchwabSession
            An authenticated `CharlesSchwabSession
            object.
        """

        self.session = session

    def get_multiple_market_hours(
        self,
        markets: List[str] | List[Enum],
        date: Union[str, datetime, date_type]
    ) -> dict:
        """Returns the market hours for all the markets.

        ### Parameters
        ----
        markets: List[str] | List[Enum]
            A list of market IDs you want to return hours for.
            Possible values are: `equity`, `option`, `future`,
            `bond`, or `forex`.

        date: Union[str, datetime, date]
            The date you wish to recieve market hours for.
            Valid ISO-8601 formats are: yyyy-MM-dd and
            yyyy-MM-dd'T'HH:mm:ssz

        ### Usage
        ----
            >>> from schwab.enums import Markets
            >>> market_hours_service = client.market_hours()
            >>> market_hours_service.get_multiple_market_hours(
                markets=['equity', Markets.BOND],
                date='2021-12-31'
            )
        """

        for index, market in enumerate(markets):
            if isinstance(market, Enum):
                markets[index] = market.value

        if isinstance(date, (date_type, datetime)):
            date = date.isoformat()

        params = {
            'markets': ','.join(markets),
            'date': date
        }

        content = self.session.make_request(
            method='get',
            endpoint='markets',
            params=params
        )

        return content

    def get_market_hours(
        self,
        market: Union[str, Enum],
        date: Union[str, datetime, date_type]
    ) -> dict:
        """Returns the market hours for the specified market.

        ### Parameters
        ----
        market: Union[str, Enum]
            A list of market IDs you want to return hours for.
            Possible values are: `equity`, `option`, `future`,
            `bond`, or `forex`.

        date: Union[str, datetime, date]
            The date you wish to recieve market hours for.
            Valid ISO-8601 formats are: yyyy-MM-dd and
            yyyy-MM-dd'T'HH:mm:ssz

        ### Usage
        ----
            >>> from schwab.enums import Markets
            >>> market_hours_service = client.market_hours()
            >>> market_hours_service.get_market_hours(
                markets='equity',
                date='2021-12-31'
            )
        """

        if isinstance(market, Enum):
            market = market.value

        if isinstance(date, (date_type, datetime)):
            date = date.isoformat()

        params = {
            'date': date
        }

        content = self.session.make_request(
            method='get',
            endpoint=f'markets/{market}',
            params=params
        )

        return content
