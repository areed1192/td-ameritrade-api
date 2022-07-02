import json
import logging
import pathlib

import requests


def build_error_dict(response):
    response.request.headers['Authorization'] = 'Bearer XXXXXXX'
    response_data = '' if len(response.content) == 0 else response.json()
    return {
        'error_code': response.status_code,
        'response_url': response.url,
        'response_body': response_data,
        'response_request': dict(response.request.headers),
        'response_method': response.request.method,
    }


class TdAmeritradeSession:

    """Serves as the Session for TD Ameritrade API."""

    def __init__(self, td_client: object) -> None:
        """Initializes the `TdAmeritradeSession` client.

        ### Overview
        ----
        The `TdAmeritradeSession` object handles all the requests made
        for the different endpoints on the TD Ameritrade API.

        ### Parameters
        ----
        client : object
            The `TdAmeritradeClient` Python Client.

        ### Usage:
        ----
            >>> td_session = TdAmeritradeSession()
        """

        from td.client import TdAmeritradeClient

        # We can also add custom formatting to our log messages.
        log_format = '%(asctime)-15s|%(filename)s|%(message)s'

        self.client: TdAmeritradeClient = td_client
        self.resource_url = 'https://api.tdameritrade.com/'
        self.version = 'v1/'

        if not pathlib.Path('logs').exists():
            pathlib.Path('logs').mkdir()
            pathlib.Path('logs/log_file_custom.log').touch()

        logging.basicConfig(
            filename="logs/log_file_custom.log",
            level=logging.INFO,
            format=log_format,
        )

    def build_headers(self) -> dict:
        """Used to build the headers needed to make the request.

        ### Parameters
        ----
        mode: str, optional
            The content mode the headers is being built for, by default `json`.

        ### Returns
        ----
        Dict:
            A dictionary containing all the components.
        """

        return {
            "Authorization": f"Bearer {self.client.td_credentials.access_token}",
            "Content-Type": "application/json",
        }

    def build_url(self, endpoint: str) -> str:
        """Build the URL used the make string.

        ### Parameters
        ----
        endpoint : str
            The endpoint used to make the full URL.

        ### Returns
        ----
        str:
            The full URL with the endpoint needed.
        """

        return self.resource_url + self.version + endpoint

    def make_request(
        self,
        method: str,
        endpoint: str,
        params: dict = None,
        data: dict = None,
        json_payload: dict = None
    ) -> dict:
        """Handles all the requests in the library.

        ### Overview
        ---
        A central function used to handle all the requests made in the library,
        this function handles building the URL, defining Content-Type, passing
        through payloads, and handling any errors that may arise during the
        request.

        ### Parameters
        ----
        method : str
            The Request method, can be one of the following:
            ['get','post','put','delete','patch']

        endpoint : str
            The API URL endpoint, example is 'quotes'

        params : dict (optional, Default={})
            The URL params for the request.

        data : dict (optional, Default={})
        A data payload for a request.

        json_payload : dict (optional, Default={})
            A json data payload for a request

        ### Returns
        ----
        Dict:
            A Dictionary object containing the
            JSON values.
        """

        self.client.td_credentials.validate_token()

        url = self.build_url(endpoint=endpoint)
        headers = self.build_headers()

        logging.info("Request URL: %s", url)

        session = requests.Session()

        req = requests.Request(
            method=method.upper(),
            headers=headers,
            url=url,
            params=params,
            data=data,
            json=json_payload
        )

        response: requests.Response = session.send(
            request=req.prepare()
        )
        session.close()

        if response.ok and len(response.content):
            return response.json()

        logging.error(
            msg=json.dumps(obj=build_error_dict(response), indent=4)
        )

        raise requests.HTTPError()
