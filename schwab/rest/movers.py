"""Used to access the `Movers` Services and metadata."""

from enum import Enum

from typing import Union
from schwab.session import CharlesSchwabSession

class Movers():

    """
    ## Overview
    ----
    Allows the user to query the top movers for the
    different indexes based on the type of move.
    """

    def __init__(self, session: CharlesSchwabSession) -> None:
        """Initializes the `Movers` services.

        ### Parameters
        ----
        session : CharlesSchwabSession
            An authenticated `CharlesSchwabSession
            object.
        """

        self.session = session

    def get_movers(
        self,
        symbol_id=Union[str, Enum],
        sort: Union[str, Enum] = None,
        frequency: Union[int, Enum] = 0
    ) -> dict:
        """Gets Active movers for a specific Index.

        ### Overview
        ----
        Top 10 (up or down) movers by value or percent for
        a particular market.

        ### Parameters
        ----
        symbol_id: Union[str, Enum]
            The index symbol to get movers for, can be
            `$DJI`, `$COMPX`, or `$SPX`.

        sort: Union[str, Enum] (optional, default=None)
            Sort by a particular attribute. Available values:
            `VOLUME`, `TRADES`, `PERCENT_CHANGE_UP`,
            `PERCENT_CHANGE_DOWN`.

        frequency: Union[int, Enum] (optional, default=0)
            To return movers with the specified directions of
            up or down. Available values: 0, 1, 5, 10, 30, 60.

        ### Usage
        ----
            >>> movers_service = client.movers()
            >>> movers_service.get_movers(
                symbol_id='$DJI',
                sort='VOLUME',
                frequency=10
            )
        """

        if isinstance(sort, Enum):
            sort = sort.value

        if isinstance(frequency, Enum):
            frequency = frequency.value

        params = {
            'sort': sort,
            'frequency': frequency
        }

        content = self.session.make_request(
            method='get',
            endpoint=f'movers/{symbol_id}',
            params=params
        )

        return content
