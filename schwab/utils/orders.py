"""Utility functions for orders."""

from dataclasses import field
from dataclasses import fields
from dataclasses import dataclass
from dataclasses import is_dataclass

from enum import Enum

from typing import Any
from typing import Union
from typing import List


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
class Instrument:
    """Represents instrument data based on the schema."""

    cusip: str = None
    symbol: str = None
    description: str = None
    instrument_id: int = 0
    net_change: float = 0.0
    type: Union[str, Enum] = None  # or just str if you prefer

    def to_dict(self) -> dict:
        """Converts the Instrument object to a dictionary.

        ### Returns
        ----
        dict :
            The Instrument object as a dictionary.

        ### Usage
        ----
            >>> my_instrument = {
                'cusip': '123456789',
                'symbol': 'SQ',
                'description': 'Square Inc.',
                'instrument_id': 123456,
                'net_change': 0.0,
                'type': 'EQUITY'
            }
            >>> my_instrument = Instrument(**my_instrument)
            >>> my_instrument.to_dict()
        """

        return _convert_to_dict(self)


@dataclass
class ExecutionLeg:
    """Represents each execution leg within an order activity."""

    leg_id: int = 0
    price: float = 0.0
    quantity: int = 0
    mismarked_quantity: int = 0
    instrument_id: int = 0
    time: str = None  # or datetime if you plan to parse it

    def to_dict(self) -> dict:
        """Converts the ExecutionLeg object to a dictionary.

        ### Returns
        ----
        dict :
            The ExecutionLeg object as a dictionary.

        ### Usage
        ----
            >>> my_execution_leg = {
                'leg_id': 1,
                'price': 0.0,
                'quantity': 1,
                'mismarked_quantity': 0,
                'instrument_id': 123456,
                'time': '2021-01-01T00:00:00Z'
            }
            >>> my_execution_leg = ExecutionLeg(**my_execution_leg)
            >>> my_execution_leg.to_dict()

        """
        return _convert_to_dict(self)


@dataclass
class OrderActivity:
    """Represents each item in the 'orderActivityCollection' array."""

    activity_type: Union[str, Enum] = None
    execution_type: Union[str, Enum] = None
    quantity: int = 0
    order_remaining_quantity: int = 0
    execution_legs: List[ExecutionLeg] = field(default_factory=list)

    def to_dict(self) -> dict:
        """Converts the OrderActivity object to a dictionary.

        ### Returns
        ----
        dict :
            The OrderActivity object as a dictionary.

        ### Usage
        ----
            >>> my_order_activity = {
                activity_type: 'EXECUTION',
                execution_type: 'FILL',
                quantity: 1,
                order_remaining_quantity: 0,
                execution_legs: [{
                    'leg_id': 1,
                    'price': 0.0,
                    'quantity': 1,
                    'mismarked_quantity': 0,
                    'instrument_id': 123456,
                    'time': '2021-01-01T00:00:00Z'
                }]
            }
            >>> my_order_activity = Emy_order_activityxecutionLeg(**my_order_activity)
            >>> my_order_activity.to_dict()

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

    session: Union[str, Enum] = None
    duration: Union[str, Enum] = None
    order_type: Union[str, Enum] = None

    cancel_time: str = None

    complex_order_strategy_type: Union[str, Enum] = None
    quantity: int = 0

    requested_destination: Union[str, Enum] = None

    stop_price: float = 0.0
    stop_price_link_basis: Union[str, Enum] = None
    stop_price_link_type: Union[str, Enum] = None
    stop_price_offset: float = 0.0
    stop_type: Union[str, Enum] = None

    price: float = 0.00
    price_link_basis: Union[str, Enum] = None
    price_link_type: Union[str, Enum] = None

    tax_lot_method: Union[str, Enum] = None

    activation_price: float = 0.0
    special_instruction: Union[str, Enum] = None
    order_strategy_type: Union[str, Enum] = None

    order_id: int = 0
    cancelable: bool = False
    editable: bool = False
    status: Union[str, Enum] = None
    entered_time: str = None  # or datetime
    close_time: str = None  # or datetime
    account_number: int = 0

    # Contains a list of OrderActivity objects
    order_activity_collection: List[OrderActivity] = field(default_factory=list)

    # Replacing orders (strings)
    replacing_order_collection: List[str] = field(default_factory=list)

    # Child order strategies (strings or entire nested orders—depends on your use case)
    child_order_strategies: List[str] = field(default_factory=list)

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
