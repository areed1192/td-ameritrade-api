"""Used to access the `Orders` Services and metadata."""

from enum import Enum
from typing import Union
from datetime import date
from datetime import datetime

from schwab.session import CharlesSchwabSession
from schwab.utils.orders import Order


class Orders:
    """
    ## Overview
    ----
    Allows the user to query, update, delete, and place
    orders with the Charles Schwab API.
    """

    def __init__(self, session: CharlesSchwabSession) -> None:
        """Initializes the `Orders` services.

        ### Parameters
        ----
        session : CharlesSchwabSession
            An authenticated `CharlesSchwabSession
            object.
        """

        self.session = session
        self.service = "trader"

    def get_orders(
        self,
        max_results: int = 3000,
        from_entered_time: Union[datetime, str] = None,
        to_entered_time: Union[datetime, str] = None,
        order_status: Union[Enum, str] = None,
    ) -> dict:
        """Get all orders for all accounts

        ### Parameters
        ----
        max_results: int (optional, Default=3000)
            The max number of orders to retrieve. Default is 3000.

        from_entered_time: Union[datetime, str] (optional, Default=None)
            Specifies that no orders entered before this time should be
            returned. Valid ISO-8601 format yyyy-MM-dd Date must be within
            60 days from today's date. If argument set then 'to_entered_time'
            must also be set.

        to_entered_time: Union[datetime, str] (optional, Default=None)
            Specifies that no orders entered after this time should be
            returned. Valid ISO-8601 format yyyy-MM-dd Date must be within
            60 days from today's date. If argument set then 'from_entered_time'
            must also be set.

        status: Union[datetime, Enum] (optional, Default=None)
            Specifies that only orders of this status should be returned.

        ### Usage
        ----
            >>> orders_service = client.orders()
            >>> orders_service.get_orders(
                order_status=OrderStatus.FILLED
            )
        """

        # Grab the From Entered Time.
        if isinstance(from_entered_time, datetime):
            from_entered_time = from_entered_time.date().isoformat()
        elif isinstance(from_entered_time, date):
            from_entered_time = from_entered_time.isoformat()

        # Grab the To Entered Time.
        if isinstance(to_entered_time, datetime):
            to_entered_time = to_entered_time.date().isoformat()
        elif isinstance(to_entered_time, date):
            to_entered_time = to_entered_time.isoformat()

        # Grab the Order Status.
        if isinstance(order_status, Enum):
            order_status = order_status.value

        # Define the payload.
        params = {
            "maxResults": max_results,
            "fromEnteredTime": from_entered_time,
            "toEnteredTime": to_entered_time,
            "status": order_status,
        }

        # Define the endpoint.
        endpoint = "orders"

        content = self.session.make_request(
            method="get", service=self.service, endpoint=endpoint, params=params
        )

        return content

    def get_orders_by_account(
        self,
        account_id: str,
        max_results: int = 3000,
        from_entered_time: Union[datetime, str] = None,
        to_entered_time: Union[datetime, str] = None,
        order_status: Union[Enum, str] = None,
    ) -> dict:
        """Returns the orders for a specific account.

        ### Parameters
        ----
        account_id: str
            The encrypted ID of the account.

        max_results: int (optional, Default=3000)
            The max number of orders to retrieve. Default is 3000.

        from_entered_time: Union[datetime, str] (optional, Default=None)
            Specifies that no orders entered before this time should be
            returned. Valid ISO-8601 format yyyy-MM-dd Date must be within
            60 days from today's date. If argument set then 'to_entered_time'
            must also be set.

        to_entered_time: Union[datetime, str] (optional, Default=None)
            Specifies that no orders entered after this time should be
            returned. Valid ISO-8601 format yyyy-MM-dd Date must be within
            60 days from today's date. If argument set then 'from_entered_time'
            must also be set.

        status: Union[datetime, Enum] (optional, Default=None)
            Specifies that only orders of this status should be returned.

        ### Usage
        ----
            >>> orders_service = client.orders()
            >>> orders_service.get_orders_by_path(
                account_id=account_number,
                order_status=OrderStatus.FILLED
            )
        """

        # Grab the From Entered Time.
        if isinstance(from_entered_time, datetime):
            from_entered_time = from_entered_time.date().isoformat()
        elif isinstance(from_entered_time, date):
            from_entered_time = from_entered_time.isoformat()

        # Grab the To Entered Time.
        if isinstance(to_entered_time, datetime):
            to_entered_time = to_entered_time.date().isoformat()
        elif isinstance(to_entered_time, date):
            to_entered_time = to_entered_time.isoformat()

        # Grab the Order Status.
        if isinstance(order_status, Enum):
            order_status = order_status.value

        # Define the payload.
        params = {
            "maxResults": max_results,
            "fromEnteredTime": from_entered_time,
            "toEnteredTime": to_entered_time,
            "status": order_status,
        }

        # Define the endpoint.
        endpoint = f"accounts/{account_id}/orders"

        content = self.session.make_request(
            method="get", service=self.service, endpoint=endpoint, params=params
        )

        return content

    def get_order(self, account_id: str, order_id: str) -> dict:
        """Get a specific order by it's id, for a specific account.

        ### Parameters
        ----
        account_id: str
            The encrypted ID of the account.

        order_id: str
            The order ID you want to query.

        ### Usage
        ----
            >>> orders_service = client.orders()
            >>> orders_service.get_order(
                account_id='123456789',
                order_id='12345678;
            )
        """

        # Define the endpoint.
        endpoint = f"accounts/{account_id}/orders/{order_id}"

        content = self.session.make_request(
            method="get", service=self.service, endpoint=endpoint
        )

        return content

    def place_order(
        self, account_id: str, order_object: Order = None, order_dict: dict = None
    ) -> dict:
        """Place an order for a specific account.

        ### Parameters
        ----
        account_id: str
            The encrypted ID of the account.

        order_object: Order (optional, Default=None)
            Represents an `Order` object that can be used to
            submit a new order to the Charles Schwab API. This
            is the preferred method as additional checks are
            done to make sure the order is valid.

        order_dict: dict (optional, Default=None)
            Represents an Order constructed from an ordinary python
            dictionary object. No additional checks will be made on the
            inputs to validate them.

        ### Usage
        ----
            >>> orders_service = client.orders()
            >>> orders_service.place_order(
                account_id='123456789',
                order_dict={}
            )
        """

        if not order_object and not order_dict:
            raise ValueError(
                "You must provide either an Order object or dictionary to place orders."
            )

        if order_object:
            order = order_object.save_order_to_json()
        else:
            order = order_dict

        # Define the endpoint.
        endpoint = f"accounts/{account_id}/orders"

        content = self.session.make_request(
            method="post", service=self.service, endpoint=endpoint, json_payload=order
        )

        return content

    def replace_order(
        self,
        account_id: str,
        order_id: str,
        order_object: Order = None,
        order_dict: dict = None,
    ) -> dict:
        """Replace an existing order for an account.

        ### Overview
        ----
        The existing order will be replaced by the new order. Once
        replaced, the old order will be canceled and a new order
        will be created.

        ### Parameters
        ----
        account_id: str
            The encrypted ID of the account

        order_id: str
            The ID of the order being replaced.

        order_object: Order (optional, Default=None)
            Represents an `Order` object that can be used to
            submit a replacing order to the Charles Schwab API.
            This is the preferred method as additional checks
            are done to make sure the order is valid.

        order_dict: dict (optional, Default=None)
            Represents an Order constructed from an ordinary python
            dictionary object. No additional checks will be made on the
            inputs to validate them.

        ### Usage
        ----
            >>> orders_service = client.orders()
            >>> orders_service.replace_order(
                account_id='123456789',
                order_id='12345678',
                order_dict={}
            )
        """

        if not order_object and not order_dict:
            raise ValueError(
                "You must provide either an Order object or dictionary to replace orders."
            )

        if order_object:
            order = order_object.save_order_to_json()
        else:
            order = order_dict

        # Define the endpoint.
        endpoint = f"accounts/{account_id}/orders/{order_id}"

        content = self.session.make_request(
            method="put", service=self.service, endpoint=endpoint, json_payload=order
        )

        return content

    def cancel_order(self, account_id: str, order_id: str) -> dict:
        """Cancels a specific order for a specific account.

        ### Parameters
        ----
        account_id: str
            The encrypted ID of the account.

        order_id: str
            The ID of the order being cancelled.

        ### Usage
        ----
            >>> orders_service = client.orders()
            >>> orders_service.cancel_order(
                account_id='123456789',
                order_id='12345678'
            )
        """

        # Define the endpoint.
        endpoint = f"accounts/{account_id}/orders/{order_id}"

        content = self.session.make_request(
            method="delete", service=self.service, endpoint=endpoint
        )

        return content
