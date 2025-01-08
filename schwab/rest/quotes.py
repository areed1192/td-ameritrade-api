"""Used to access the `Quotes` Services and metadata."""

from enum import Enum
from typing import List
from schwab.session import CharlesSchwabSession


class Quotes:

    """
    ## Overview
    ----
    Allows the user to query real-time quote.
    """

    def __init__(self, session: CharlesSchwabSession) -> None:
        """Initializes the `Quotes` services.

        ### Parameters
        ----
        session : CharlesSchwabSession
            An authenticated `CharlesSchwabSession
            object.
        """

        self.session = session

    def get_quote(self, symbol_id=str, fields: List[str] | Enum = None) -> dict:
        """Get quote by a single symbol.

        ### Parameters
        ----
        symbol_id: str
            A list of different financial instruments.

        fields: List[str] | Enum, (optional, default=None)
            Request for subset of data by passing coma separated list of
            root nodes, possible root nodes are quote, fundamental, extended,
            reference, regular. Sending quote, fundamental in request
            will return quote and fundamental data in response.
            Dont send this attribute for full response.

        ### Usage
        ----
            >>> quote_service = client.quotes()
            >>> quote_service.get_quote(
                instrument='AAPL',
                fields=['quote', 'fundamental']
            )
        """

        params = {}

        # If fields are provided, join them with a comma.
        if fields:
            if isinstance(fields, Enum):
                fields = fields.value
                if isinstance(fields, str):
                    fields = [fields]
            params["fields"] = ",".join(fields)

        content = self.session.make_request(
            method="get", endpoint=f"{symbol_id}/quotes", params=params
        )

        return content

    def get_quotes(
        self,
        instruments=List[str],
        fields: List[str] | Enum = None,
        indicative: bool = False,
    ) -> dict:
        """Get quote by a list of symbols.

        ### Parameters
        ----
        instruments: List[str]
            A list of different financial instruments.

        fields: List[str] | Enum, (optional, default=None)
            Request for subset of data by passing coma separated list of
            root nodes, possible root nodes are quote, fundamental, extended,
            reference, regular. Sending quote, fundamental in request
            will return quote and fundamental data in response.
            Dont send this attribute for full response.

        indicative: bool, (optional, default=False)
            Include indicative symbol quotes for all ETF symbols in request.
            If ETF symbol ABC is in request and indicative=true API will
            return quotes for ABC and its corresponding indicative quote
            for $ABC.IV

        ### Usage
        ----
            >>> quote_service = client.quotes()
            >>> quote_service.get_quotes(
                instruments=['AAPL','SQ']
            )
        """

        params = {
            "symbol": ",".join(instruments),
            "indicative": indicative,
        }

        # If fields are provided, join them with a comma.
        if fields:
            if isinstance(fields, Enum):
                fields = fields.value
                if isinstance(fields, str):
                    fields = [fields]
            params["fields"] = ",".join(fields)

        content = self.session.make_request(
            method="get", endpoint="quotes", params=params
        )

        return content
