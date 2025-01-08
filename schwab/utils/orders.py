"""Utility functions for orders."""

from dataclasses import fields
from dataclasses import dataclass
from dataclasses import is_dataclass

from typing import Any
from typing import Union
from typing import List
from enum import Enum


def _snake_to_camel(snake_str: str) -> str:
    """Convert a snake_case string to camelCase."""

    parts = snake_str.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])


def _convert_to_dict(obj: Any) -> Any:
    """
    ### Overview
    ----
    Recursively convert a dataclass or dictionary (which can contain
    more dataclasses, dictionaries, lists, or Enums) into a dictionary
    with camelCase keys and primitive values.

    ### Parameters
    ----
    obj : Any
        The object to convert. Can be a dataclass, dictionary
        list, or Enum.
    """
    # If it's an Enum, return its value (e.g., the string or int it holds).
    if isinstance(obj, Enum):
        return obj.value

    # If it's a dataclass, convert its fields into a dict.
    if is_dataclass(obj):
        result = {}
        for f in fields(obj):
            value = getattr(obj, f.name)
            if value is not None:  # Skip fields that are None
                result[_snake_to_camel(f.name)] = _convert_to_dict(value)
        return result

    # If it's a dictionary, convert each key and value.
    if isinstance(obj, dict):
        result = {}
        for key, value in obj.items():
            if value is not None:  # Skip keys with None values
                result[_snake_to_camel(key)] = _convert_to_dict(value)
        return result

    # If it's a list, convert each element in the list.
    if isinstance(obj, list):
        return [_convert_to_dict(item) for item in obj]

    # Otherwise, return it as-is (e.g., string, int, float).
    return obj


@dataclass
class OrderLegInstrument:
    """
    ## Overview
    ----
    Represents the Instrument object that is part of an order leg.
    The instrument is one of the financial objects that TD Ameritrade
    allows you to trade.
    """

    asset_type: Union[str, Enum]
    symbol: str

    def to_dict(self) -> dict:
        """Generates a dictionary containing all the field
        names and values.

        ### Returns
        ----
        dict
            The Field Name and Values.

        ### Usage
        ----
            >>> my_order_leg_instrument = {
                'asset_type': 'EQUITY',
                'symbol': 'SQ',
            }
            >>> my_order_leg_instrument = OrderLegInstrument(**my_order_leg_instrument)
            >>> my_order_leg_instrument.to_dict()
        """

        return _convert_to_dict(self)


@dataclass
class OrderLeg:
    """
    ## Overview
    ----
    Represents an OrderLeg object that is used to specify
    instructions about the order.
    """

    order_leg_type: Union[str, Enum] = None
    leg_id: int = 0
    instrument: Union[dict, OrderLegInstrument] = None
    instruction: Union[str, Enum] = None
    position_effect: Union[str, Enum] = None
    quantity: int = None
    quantity_type: str = None

    def to_dict(self) -> dict:
        """Generates a dictionary containing all the field
        names and values.

        ### Returns
        ----
        dict
            The Field Name and Values.

        ### Usage
        ----
            >>> my_order_leg = {
                'instruction': 'BUY',
                'instrument':{
                    'asset_type': 'EQUITY',
                    'symbol': 'SQ'
                },
                'quantity': 2
            }
            >>> my_order_leg = OrderLeg(**my_order_leg)
            >>> my_order_leg.to_dict()
        """

        return _convert_to_dict(self)


@dataclass
class Order:
    """
    ## Overview
    ----
    Represents the order object that you want to submit to
    Charles Schwab.
    """

    order_leg_collection: List
    child_order_strategies: List

    price: float = 0.00
    session: Union[str, Enum] = None
    duration: Union[str, Enum] = None
    requested_destination: Union[str, Enum] = None
    complex_order_strategy_type: Union[str, Enum] = None
    stop_price_link_basis: Union[str, Enum] = None
    stop_price_link_type: Union[str, Enum] = None
    stop_type: Union[str, Enum] = None
    price_link_basis: Union[str, Enum] = None
    price_link_type: Union[str, Enum] = None
    order_type: Union[str, Enum] = None
    order_strategy_type: Union[str, Enum] = None

    def to_dict(self) -> dict:
        """Generates a dictionary containing all the field
        names and values.

        ### Returns
        ----
        dict
            The Field Name and Values.

        ### Usage
        ----
            >>> my_order_leg = {
                'instruction': 'BUY',
                'instrument':{
                    'asset_type': 'EQUITY',
                    'symbol': 'SQ'
                },
                'quantity': 2
            }
            >>> my_order_leg = OrderLeg(**my_order_leg)
            >>> my_order_leg.to_dict()
        """

        return _convert_to_dict(self)
