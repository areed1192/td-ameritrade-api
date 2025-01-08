"""This module contains the different streaming services that you can pull data from."""

from enum import Enum
from typing import List
from typing import Union

from datetime import datetime

from schwab.utils.enums import StreamingServices as Services


class StreamingServices:
    """
    ## Overview
    ----
    Represents the different streaming services that you can pull
    data from.
    """

    def __init__(self, streaming_api_client: object) -> None:
        """Initializes the `StreamingServices` object.

        ### Parameters
        ----
        streaming_api_client : StreamingApiClient
            The streaming API client that handles sending requests.
        """

        from schwab.streaming.client import (  # pylint: disable=import-outside-toplevel
            StreamingApiClient,
        )

        self.streaming_api_client: StreamingApiClient = streaming_api_client

    def _new_request_template(self) -> dict:
        """Serves as a template to build new service requests.

        ### Overview
        ----
        This takes the Request template and populates the required fields
        for a subscription request.

        ### Returns
        ----
        dict:
            The service request with the standard fields
            filled out.
        """

        # Grab the current count of the services.
        service_count = len(self.streaming_api_client.data_requests["requests"]) + 1

        request = {
            "service": None,
            "command": None,
            "requestid": service_count,
            "SchwabClientCustomerId": self.streaming_api_client.customer_id,
            "SchwabClientCorrelId": self.streaming_api_client.correl_id,
            "parameters": {"keys": None, "fields": None},
        }

        return request

    def level_one_quotes(
        self, symbols: List[str], fields: Union[List[Enum], List[str], List[int]]
    ) -> None:
        """Provides access to level one streaming quotes.

        ### Parameters
        ----
        symbols: List[str]
            A List of symbols you wish to stream quotes for.

        fields: Union[List[Enum], List[str], List[int]]
            The fields you want returned from the Endpoint, can either
            be the numeric representation or the key value representation.
            For more info on fields, refer to the documentation.

        ### Usage
        ----
            >>> streaming_api_service = client.streaming_api_client()
            >>> streaming_services = streaming_api_service.services()
            >>> streaming_services.level_one_quotes(
                symbols=['AAPL','SQ'],
                fields=LevelOneQuotes.ALL
            )
        """

        if isinstance(fields, list):
            new_fields = []
            for field in fields:
                if isinstance(field, int):
                    field = str(int)
                elif isinstance(field, Enum):
                    field = str(field.value)
                new_fields.append(field)

        if isinstance(fields, Enum):
            new_fields = fields.value

        # Build the request
        request = self._new_request_template()
        request["service"] = Services.LEVELONE_EQUITIES.value
        request["command"] = "SUBS"
        request["parameters"]["keys"] = ",".join(symbols)
        request["parameters"]["fields"] = ",".join(new_fields)

        self.streaming_api_client.data_requests["requests"].append(request)

    def level_one_options(
        self, symbols: List[str], fields: Union[List[Enum], List[str], List[int]]
    ) -> None:
        """Provides access to level one streaming options quotes.

        ### Parameters
        ----
        symbols: List[str]
            A List of symbols you wish to stream quotes for.

        fields: Union[List[Enum], List[str], List[int]]
            The fields you want returned from the Endpoint, can either
            be the numeric representation or the key value representation.
            For more info on fields, refer to the documentation.

        ### Usage
        ----
            >>> streaming_api_service = client.streaming_api_client()
            >>> streaming_services = streaming_api_service.services()
            >>> streaming_services.level_one_options(
                symbols=['MSFT_043021C120'],
                fields=LevelOneOptions.ALL
            )
        """

        if isinstance(fields, list):
            new_fields = []
            for field in fields:
                if isinstance(field, int):
                    field = str(int)
                elif isinstance(field, Enum):
                    field = str(field.value)
                new_fields.append(field)

        if isinstance(fields, Enum):
            new_fields = fields.value

        # Build the request
        request = self._new_request_template()
        request["service"] = Services.LEVELONE_OPTIONS.value
        request["command"] = "SUBS"
        request["parameters"]["keys"] = ",".join(symbols)
        request["parameters"]["fields"] = ",".join(new_fields)

        self.streaming_api_client.data_requests["requests"].append(request)

    def level_one_futures(
        self, symbols: List[str], fields: Union[List[Enum], List[str], List[int]]
    ) -> None:
        """Provides access to level one streaming futures quotes.

        ### Parameters
        ----
        symbols: List[str]
            A List of symbols you wish to stream quotes for.

        fields: Union[List[Enum], List[str], List[int]]
            The fields you want returned from the Endpoint, can either
            be the numeric representation or the key value representation.
            For more info on fields, refer to the documentation.

        ### Usage
        ----
            >>> streaming_api_service = client.streaming_api_client()
            >>> streaming_services = streaming_api_service.services()
            >>> streaming_services.level_one_futures(
                symbols=['/ES'],
                fields=LevelOneFutures.ALL
            )
        """

        if isinstance(fields, list):
            new_fields = []
            for field in fields:
                if isinstance(field, int):
                    field = str(int)
                elif isinstance(field, Enum):
                    field = str(field.value)
                new_fields.append(field)

        if isinstance(fields, Enum):
            new_fields = fields.value

        # Build the request
        request = self._new_request_template()
        request["service"] = Services.LEVELONE_FUTURES.value
        request["command"] = "SUBS"
        request["parameters"]["keys"] = ",".join(symbols)
        request["parameters"]["fields"] = ",".join(new_fields)

        self.streaming_api_client.data_requests["requests"].append(request)

    def level_one_futures_options(
        self, symbols: List[str], fields: Union[List[Enum], List[str], Enum]
    ) -> None:
        """Provides access to level one streaming futures options quotes.

        ### Parameters
        ----
        symbols: List[str]
            A List of symbols you wish to stream quotes for.

        fields: Union[List[Enum], List[str]]
            The fields you want returned from the Endpoint, can either
            be the numeric representation or the key value representation.
            For more info on fields, refer to the documentation.

        ### Usage
        ----
            >>> streaming_api_service = client.streaming_api_client()
            >>> streaming_services = streaming_api_service.services()
            >>> streaming_services.level_one_futures(
                symbols=['./EW2J20C2675'],
                fields=LevelOneFutures.ALL
            )
        """

        if isinstance(fields, list):
            new_fields = []
            for field in fields:
                if isinstance(field, int):
                    field = str(int)
                elif isinstance(field, Enum):
                    field = str(field.value)
                new_fields.append(field)

        if isinstance(fields, Enum):
            new_fields = fields.value

        # Build the request
        request = self._new_request_template()
        request["service"] = Services.LEVELONE_FUTURES_OPTIONS.value
        request["command"] = "SUBS"
        request["parameters"]["keys"] = ",".join(symbols)
        request["parameters"]["fields"] = ",".join(new_fields)

        self.streaming_api_client.data_requests["requests"].append(request)

    def level_one_forex(
        self, symbols: List[str], fields: Union[List[str], List[int]]
    ) -> None:
        """Provides access to level one streaming forex quotes.

        ### Parameters
        ----
        symbols: List[str]
            A List of symbols you wish to stream quotes for.

        fields: Union[List[Enum], List[str], List[int]]
            The fields you want returned from the Endpoint, can either
            be the numeric representation or the key value representation.
            For more info on fields, refer to the documentation.

        ### Usage
        ----
            >>> streaming_api_service = client.streaming_api_client()
            >>> streaming_services = streaming_api_service.services()
            >>> streaming_services.level_one_forex(
                symbols=['EUR/USD'],
                fields=LevelOneForex.ALL
            )
        """

        if isinstance(fields, list):
            new_fields = []
            for field in fields:
                if isinstance(field, int):
                    field = str(int)
                elif isinstance(field, Enum):
                    field = str(field.value)
                new_fields.append(field)

        if isinstance(fields, Enum):
            new_fields = fields.value

        # Build the request
        request = self._new_request_template()
        request["service"] = Services.LEVELONE_FOREX.value
        request["command"] = "SUBS"
        request["parameters"]["keys"] = ",".join(symbols)
        request["parameters"]["fields"] = ",".join(new_fields)

        self.streaming_api_client.data_requests["requests"].append(request)

    def account_activity(self) -> None:
        """
        ### Overview
        ----
        Represents the ACCOUNT_ACTIVITY endpoint of the Charles Schwab
        Streaming API. This service is used to request streaming
        updates for one or more accounts associated with
        the logged in User ID. Common usage would involve issuing
        the OrderStatus API request to get all transactions for an
        account, and subscribing to ACCT_ACTIVITY to get any updates.
        """

        # Build the request
        request = self._new_request_template()
        request["service"] = Services.ACCT_ACTIVITY.value
        request["command"] = "SUBS"
        request["parameters"]["keys"] = "Account Activity"
        request["parameters"]["fields"] = "0,1,2,3"

        self.streaming_api_client.data_requests["requests"].append(request)

    def chart(
        self,
        service: Union[str, Enum],
        symbols: List[str],
        fields: Union[List[str], List[int]],
    ) -> None:
        """Subscribes to the Chart Service.

        ### Overview
        ----
        Represents the CHART_EQUITY, CHART_FUTRUES, and CHART_OPTIONS endpoint that can
        be used to stream info needed to recreate charts.

        ### Parameters
        ---
        service: Union[str, Enum]
            The type of Chart Service you wish to recieve. Can be either
            `CHART_EQUITY`, `CHART_FUTURES` or `CHART_OPTIONS`

        symbols: List[str]
            A List of symbols you wish to stream quotes for.

        fields: Union[List[Enum], List[str], List[int]]
            The fields you want returned from the Endpoint, can either
            be the numeric representation or the key value representation.
            For more info on fields, refer to the documentation.

        ### Usage
        ----
            >>> streaming_api_service = client.streaming_api_client()
            >>> streaming_services = streaming_api_service.services()
            >>> streaming_services.chart(
                service=ChartServices.ChartEquity,
                symbols=['MSFT', 'GOOG', 'AAPL'],
                fields=ChartEquity.ALL
            )
        """

        if isinstance(service, Enum):
            service = service.value

        if isinstance(fields, list):
            new_fields = []
            for field in fields:
                if isinstance(field, int):
                    field = str(int)
                elif isinstance(field, Enum):
                    field = str(field.value)
                new_fields.append(field)

        if isinstance(fields, Enum):
            new_fields = fields.value

        # Build the request
        request = request = self._new_request_template()
        request["service"] = service
        request["command"] = "SUBS"
        request["parameters"]["keys"] = ",".join(symbols)
        request["parameters"]["fields"] = ",".join(new_fields)
        self.streaming_api_client.data_requests["requests"].append(request)

    def chart_history_futures(
        self,
        symbols: List[str],
        frequency: Union[str, Enum],
        period: Union[str, Enum] = None,
        start_time: Union[str, datetime] = None,
        end_time: Union[str, datetime] = None,
    ) -> None:
        """Stream historical futures prices for charting. For normal equity charts, please use the
        the `get_historical_prices` method.

        ### Parameters
        ---
        symbols: List[str]
            A List of symbols you wish to stream quotes for.

        frequency: Union[str, Enum]
            The frequency at which you want the data to appear.

        period: Union[str, Enum] (optional, Default=None)
            The period you wish to return historical data for. Not
            required if `start_time` or `end_time` is set.

        start_time: Union[str, datetime] (optional, Default=None)
            Start time of chart in milliseconds since Epoch.

        end_time: Union[str, datetime] (optional, Default=None)
            End time of chart in milliseconds since Epoch.

        ### Usage
        ----
            >>> streaming_api_service = client.streaming_api_client()
            >>> streaming_services = streaming_api_service.services()
            >>> streaming_services.chart_history_futures(
                symbols=['/ES', '/CL'],
                frequency=ChartFuturesFrequencies.ONE_MINUTE,
                period=ChartFuturesPeriods.ONE_DAY
            )
        """

        # Handle datetimes.
        if isinstance(start_time, datetime):
            start_time = int(start_time.timestamp() * 1000)

        if isinstance(end_time, datetime):
            end_time = int(end_time.timestamp() * 1000)

        if isinstance(frequency, Enum):
            frequency = frequency.value

        if isinstance(period, Enum):
            period = period.value

        # define the valid inputs.
        valid_frequencies = ["m1", "m5", "m10", "m30", "h1", "d1", "w1", "n1"]
        valid_periods = ["d1", "d5", "w4", "n10", "y1", "y10"]

        # validate the frequency input.
        if frequency not in valid_frequencies:
            raise ValueError(
                "FREQUENCY is incorrect choose a valid option:['m1','m5','m10','m30','h1','d1','w1','n1']"
            )

        # validate the period input.
        if period not in valid_periods and start_time is None and end_time is None:
            raise ValueError(
                "PERIOD is incorrect choose a valid option:['d5','w4','n10','y1','y10']"
            )

        # Build the request
        request = self._new_request_template()
        request["service"] = Services.CHART_FUTURES.value
        request["command"] = "GET"
        request["parameters"]["symbol"] = ",".join(symbols)
        request["parameters"]["frequency"] = frequency

        # handle the case where we get a start time or end time. DO FURTHER VALIDATION.
        if start_time is not None or end_time is not None:
            request["parameters"]["END_TIME"] = end_time
            request["parameters"]["START_TIME"] = start_time
        else:
            request["parameters"]["period"] = period

        del request["parameters"]["keys"]
        del request["parameters"]["fields"]

        request["requestid"] = str(request["requestid"])
        self.streaming_api_client.data_requests["requests"].append(request)

    def level_two_quotes(
        self, symbols: List[str], fields: Union[Enum, List[str], List[int]]
    ) -> None:
        """Stream Level Two Equity Quotes.

        ### Parameters
        ---
        symbols: List[str]
            A List of symbols you wish to stream quotes for.

        fields: Union[List[Enum], List[str], List[int]]
            The fields you want returned from the Endpoint, can either
            be the numeric representation or the key value representation.
            For more info on fields, refer to the documentation.

        ### Usage
        ----
            >>> streaming_api_service = client.streaming_api_client()
            >>> streaming_services = streaming_api_service.services()
            >>> streaming_services.level_two_quotes(
                symbols=['MSFT', 'PINS'],
                fields=LevelTwoQuotes.ALL
            )
        """

        if isinstance(fields, list):
            new_fields = []
            for field in fields:
                if isinstance(field, int):
                    field = str(int)
                elif isinstance(field, Enum):
                    field = str(field.value)
                new_fields.append(field)

        if isinstance(fields, Enum):
            new_fields = fields.value

        # Build the request
        request = self._new_request_template()
        request["service"] = "LISTED_BOOK"
        request["command"] = "SUBS"
        request["parameters"]["keys"] = ",".join(symbols)
        request["parameters"]["fields"] = ",".join(new_fields)

        self.streaming_api_client.data_requests["requests"].append(request)

    def level_two_options(
        self, symbols: List[str], fields: Union[Enum, List[str], List[int]]
    ) -> None:
        """Stream Level Two Options Quotes.

        ### Parameters
        ---
        symbols: List[str]
            A List of symbols you wish to stream quotes for.

        fields: Union[List[Enum], List[str], List[int]]
            The fields you want returned from the Endpoint, can either
            be the numeric representation or the key value representation.
            For more info on fields, refer to the documentation.

        ### Usage
        ----
            >>> streaming_api_service = client.streaming_api_client()
            >>> streaming_services = streaming_api_service.services()
            >>> streaming_services.level_two_options(
                symbols=['MSFT_043021C120'],
                fields=LevelTwoOptions.ALL
            )
        """

        if isinstance(fields, list):
            new_fields = []
            for field in fields:
                if isinstance(field, int):
                    field = str(int)
                elif isinstance(field, Enum):
                    field = str(field.value)
                new_fields.append(field)

        if isinstance(fields, Enum):
            new_fields = fields.value

        # Build the request
        request = self._new_request_template()
        request["service"] = "OPTIONS_BOOK"
        request["command"] = "SUBS"
        request["parameters"]["keys"] = ",".join(symbols)
        request["parameters"]["fields"] = ",".join(new_fields)

        self.streaming_api_client.data_requests["requests"].append(request)
