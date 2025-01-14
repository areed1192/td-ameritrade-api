"""Used to access the `Accounts` Services and metadata."""

from enum import Enum
from typing import Union
from datetime import datetime
from datetime import timezone
from schwab.session import CharlesSchwabSession


class Accounts:
    """
    ## Overview
    ----
    Allows the user to retrieve account information.
    """

    def __init__(self, session: CharlesSchwabSession) -> None:
        """Initializes the `Accounts` services.

        ### Parameters
        ----
        session : CharlesSchwabSession
            An authenticated `CharlesSchwabSession
            object.
        """

        self.session = session

    def get_account_numbers(self) -> list:
        """Gets a list of account numbers and their encrypted
        values for a user.

        ### Returns
        ----
        list :
            A list of account numbers and their encrypted values
            for a user.

        ### Usage
        ----
            >>> account_services = client.accounts()
            >>> account_services.get_account_numbers()
        """

        content = self.session.make_request(
            method="get", endpoint="accounts/accountNumbers"
        )

        return content

    def get_accounts(
        self, account_id: str = None, include_positions: bool = True
    ) -> dict:
        """Get linked account(s) balances and positions for the
        logged in user.

        ### Overview
        ----
        Serves as the mechanism to make a request to the
        "Get Accounts" and "Get Account" Endpoint. If one
        account is provided a "Get Account" request will
        be made and if more than one account is provided
        then a "Get Accounts" request will be made.

        ### Parameters
        ----
        account_id: str (optional, default=None)
            The account number you wish to recieve data on.
            If no account ID is provided then all accounts will
            be queried.

        include_positions: bool (optional, default=True)
            If set to `True` then account positions will be returned
            from the API. If set to `False` no positions will be
            returned.

        ### Usage
        ----
            >>> account_services = client.accounts()
            >>> account_services.get_accounts(
                account_id='123456789',
                include_positions=True
            )
        """

        fields = []

        if account_id is None:
            endpoint = "accounts"
        else:
            endpoint = f"accounts/{account_id}"

        if include_positions is True:
            fields.append("positions")
            params = {
                "fields": ",".join(fields),
            }
        else:
            params = None

        content = self.session.make_request(
            method="get", endpoint=endpoint, params=params
        )

        return content

    def get_transactions(
        self,
        account_id: str,
        start_date: Union[str, datetime] = None,
        end_date: Union[str, datetime] = None,
        symbol: str = None,
        transaction_type: Union[str, Enum] = None,
    ) -> dict:
        """Queries the transactions for an account.

        ### Parameters
        ----
        account_id: str
            The encrypted ID of the account.

        start_date: Union[str, datetime] (optional, default=None)
            Only transactions after the start date will be returned.
            Note: The maximum date range is one year. Valid ISO-8601
            formats are: yyyy-MM-dd.

        end_date: Union[str, datetime] (optional, default=None)
            Only transactions before the end date will be returned.
            Note: The maximum date range is one year. Valid ISO-8601
            formats are: yyyy-MM-dd.

        symbol: str (optional, default=None)
            Filters the transaction to the ones that only include
            the symbol provided. If there is any special character
            in the symbol, please send th encoded value.

        transaction_type: Union[str, Enum] (optional, default=None)
            The type of transaction you want to query. For more info,
            review the documentation for a full list of transaction
            types, or review the `schwab.enums` file.

        ### Usage
        ----
            >>> account_services = client.accounts()
            >>> account_services.get_transactions(
                account_id='123456789',
                transaction_type='ALL'
            )
        """

        if isinstance(transaction_type, Enum):
            transaction_type = transaction_type.value

        if isinstance(start_date, datetime):
            # Check if the datetime object is timezone-aware
            if start_date.tzinfo is None:
                # Optionally assign a default timezone (e.g., UTC or local time)
                start_date = start_date.replace(tzinfo=timezone.utc)

            # Format to ISO 8601 with milliseconds and 'Z' if UTC
            start_date = (
                start_date.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[
                    :-3
                ]
                + "Z"
            )

        if isinstance(end_date, datetime):
            # Check if the datetime object is timezone-aware
            if end_date.tzinfo is None:
                # Optionally assign a default timezone (e.g., UTC or local time)
                end_date = end_date.replace(tzinfo=timezone.utc)
            # Format to ISO 8601 with milliseconds and 'Z' if UTC
            end_date = end_date.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


        # Check if symbol has special characters and encode them.
        if symbol is not None:
            symbol = symbol.encode("utf-8").decode("unicode_escape")

        params = {
            "types": transaction_type,
            "startDate": start_date,
            "endDate": end_date,
            "symbol": symbol,
        }

        content = self.session.make_request(
            method="get", endpoint=f"accounts/{account_id}/transactions", params=params
        )

        return content

    def get_transaction(self, account_id: str, transaction_id: str) -> dict:
        """Queries a transaction for a specific account.

        ### Overview
        ----
        Serves as the mechanism to make a request to the "Get Transaction"
        Endpoint. The transaction ID will be queried for the specific account
        passed through.

        ### Parameters
        ----
        account_id: str
            The encrypted ID of the account.

        transaction_id: str
            If set to `True` then account orders will be returned
            from the API. If set to `False` no orders will be
            returned.

        ### Usage
        ----
            >>> account_services = client.accounts()
            >>> account_services.get_transaction(
                account_id='123456789',
                transaction_id='123456789'
            )
        """

        content = self.session.make_request(
            method="get",
            endpoint=f"accounts/{account_id}/transactions/{transaction_id}",
        )

        return content
