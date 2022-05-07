import json
import pathlib

from typing import Union
from datetime import datetime

import multiprocessing as mp
from time import sleep
from urllib.parse import unquote
import requests

from splinter import Browser
from td.config.get_config import config
from td.logging.create_logger import get_logger


class TdCredentials:

    """
    ### Overview
    ----
    TD Ameritrade uses an oAuth protocol
    to authenticate it's users. The `TdCredential`
    object helps the user manage the credentials to ensure
    the are properly authenticated.
    """

    # allows for multiple clients and  concurrency lock to refresh/access expiration times
    __consumer_apps = {}

    def __init__(
        self, 
        client_id: str, 
        redirect_uri: str, 
        token_dict: dict = None,
        token_file: Union[str, pathlib.Path] = None, 
        client_name: str = "td-ameritrade-api", 
        login_credentials_dict: dict = None) -> None:
        """Initializes the `TdCredential` object."""

        TdCredentials.__consumer_apps[client_name] = {
            "multiprocessing_lock": mp.Lock(),
            "refresh_token_expiration_time": 0,
            "access_token_expiration_time": 0
        }

        self._access_token = ''
        self._refresh_token = ''
        self._scope = []
        self._token_type = ''
        self._expires_in = 0
        self._refresh_token_expires_in = 0
        self._client_name = client_name
        self._client_id = client_id
        self._redirect_uri = redirect_uri
        self.__login_credentials_dict = login_credentials_dict

        self.resource_url = 'https://api.tdameritrade.com/'
        self.version = 'v1/'
        self.token_endpoint = 'oauth2/token'
        self.authorization_url = 'https://auth.tdameritrade.com/auth?'
        self.authorization_code = ""
        self._file_path = pathlib.Path.joinpath(pathlib.Path(config.get('config', 'config_directory_path')),
                                                client_name + "/td_credentials.json")
        self._file_path_base = pathlib.Path.joinpath(pathlib.Path(config.get('config', 'config_directory_path')),
                                                     client_name)
        self._first_pass = True

        self.log = get_logger()

        if token_file:
            if isinstance(token_file, pathlib.Path):
                token_file = token_file.resolve()

            self._file_path = token_file
            self.from_token_file(file_path=token_file)

        elif token_dict:
            self.from_token_dict_helper(token_dict=token_dict)
        elif pathlib.Path.exists(pathlib.Path(self._file_path)):
            self.from_token_file(file_path=self._file_path)
        else:
            self.from_workflow()

        self.log.info("credentials init complete")

    @property
    def redirect_uri(self) -> str:
        """Returns the user's redirect URI.

        ### Returns
        ----
        str
            The User's redirect URI.

        ### Usage
        ----
            >>> td_credential = TdCredentials()
            >>> td_credential.redirect_uri
        """

        return self._redirect_uri

    @property
    def client_name(self) -> str:
        """Returns the Client Name.

        ### Returns
        ----
        str
            The app Client Name.

        ### Usage
        ----
            >>> td_credential = TdCredentials()
            >>> td_credential.client_name
        """
        return self._client_name

    @property
    def client_id(self) -> str:
        """Returns the Consumer Key.

        ### Returns
        ----
        str
            The apps Consumer Key.

        ### Usage
        ----
            >>> td_credential = TdCredentials()
            >>> td_credential.client_id
        """
        
        return self._client_id

    @property
    def access_token(self) -> str:
        """Returns the Access token.

        ### Returns
        ----
        str
            A valid Access Token.

        ### Usage
        ----
            >>> td_credential = TdCredentials()
            >>> td_credential.access_token
        """

        return self._access_token

    @property
    def refresh_token(self) -> str:
        """Returns the Refresh token.

        ### Returns
        ----
        str
            A valid Refresh Token.

        ### Usage
        ----
            >>> td_credential = TdCredentials()
            >>> td_credential.refresh_token
        """

        return self._refresh_token

    @property
    def access_token_expiration_time(self):
        """Returns when the Access Token will expire.

        ### Returns
        ----
        datetime
            The date and time of the access token
            expiration.

        ### Usage
        ----
            >>> td_credential = TdCredentials()
            >>> td_credential.refresh_token_expiration_time
        """
        return TdCredentials.__consumer_apps[self._client_name]["access_token_expiration_time"]

    @property
    def refresh_token_expiration_time(self):
        """Returns when the Refresh Token will expire.

        ### Returns
        ----
        datetime
            The date and time of the refresh token
            expiration.

        ### Usage
        ----
            >>> td_credential = TdCredentials()
            >>> td_credential.refresh_token_expiration_time
        """
        return TdCredentials.__consumer_apps[self._client_name]["refresh_token_expiration_time"]

    @property
    def is_access_token_expired(self) -> bool:
        """Specifies whether the current Access Token is expired
        or not.

        ### Returns
        ----
        bool
            `True` if the Access Token is expired,
            `False` otherwise.

        ### Usage
        ----
            >>> td_credential = TdCredentials()
            >>> td_credential.is_refresh_token_expired
        """

        if (self.access_token_expiration_time.timestamp() - 20) < datetime.now().timestamp():
            return True
        else:
            return False

    @property
    def is_refresh_token_expired(self) -> bool:
        """Specifies whether the current Refresh Token is expired
        or not.

        ### Returns
        ----
        bool
            `True` if the Refresh Token is expired,
            `False` otherwise.

        ### Usage
        ----
            >>> td_credential = TdCredentials()
            >>> td_credential.is_refresh_token_expired
        """

        if (self.refresh_token_expiration_time.timestamp() - 20) < datetime.now().timestamp():
            return True
        else:
            return False

    def from_token_dict(self, token_dict: dict) -> None:
        """Converts a token dictionary to a `TdCredential`
        object.

        ### Parameters
        ----
        token_dict : dict
            A dictionary containing all the
            original token details.

        ### Usage
        ----
            >>> td_credential = TdCredentials()
            >>> td_credential.from_dict(
                token_dict={
                    'access_token': '',
                    'refresh_token': ',
                    'scope': '',
                    'expires_in': 0,
                    'refresh_token_expires_in': 0,
                    'token_type': ''
                }
            )
        """
        self._access_token = token_dict.get('access_token', '')
        self._refresh_token = token_dict.get('refresh_token', '')
        self._scope = token_dict.get('scope', [])
        self._token_type = token_dict.get('token_type', '')
        self._expires_in = token_dict.get('expires_in', 0)

        self._refresh_token_expires_in = token_dict.get(
            'refresh_token_expires_in',
            0
        )
        TdCredentials.__consumer_apps[self._client_name]["refresh_token_expiration_time"] = token_dict.get(
            'refresh_token_expiration_time', 0
        )

        TdCredentials.__consumer_apps[self._client_name]["access_token_expiration_time"] = token_dict.get(
            'access_token_expiration_time', 0
        )

        # Calculate the Refresh Token expiration time.
        if isinstance(TdCredentials.__consumer_apps[self._client_name]["refresh_token_expiration_time"], str):
            TdCredentials.__consumer_apps[self._client_name][
                "refresh_token_expiration_time"] = datetime.fromisoformat(
                TdCredentials.__consumer_apps[self._client_name]["refresh_token_expiration_time"]
            )
        elif isinstance(TdCredentials.__consumer_apps[self._client_name]["refresh_token_expiration_time"], float):
            TdCredentials.__consumer_apps[self._client_name][
                "refresh_token_expiration_time"] = datetime.fromtimestamp(
                TdCredentials.__consumer_apps[self._client_name]["refresh_token_expiration_time"]
            )
        else:
            self._calculate_refresh_token_expiration(
                expiration_secs=self._refresh_token_expires_in
            )

        # Calculate the Access Token Expiration Time.
        if isinstance(TdCredentials.__consumer_apps[self._client_name]["access_token_expiration_time"], str):
            TdCredentials.__consumer_apps[self._client_name]["access_token_expiration_time"] = datetime.fromisoformat(
                TdCredentials.__consumer_apps[self._client_name]["access_token_expiration_time"]
            )
        elif isinstance(TdCredentials.__consumer_apps[self._client_name]["access_token_expiration_time"], float):
            TdCredentials.__consumer_apps[self._client_name]["access_token_expiration_time"] = datetime.fromtimestamp(
                TdCredentials.__consumer_apps[self._client_name]["access_token_expiration_time"]
            )
        else:
            self._calculate_access_token_expiration(
                expiration_secs=self._expires_in,
            )

        self.validate_token()

    def to_token_dict(self) -> dict:
        """Converts the TdCredential object
        to a dictionary object.

        ### Returns
        ----
        dict
            A dictionary containing all the
            original token details.

        ### Usage
        ----
            >>> td_credential = TdCredentials()
            >>> td_credential.to_dict()
        """

        token_dict = {
            'access_token': self._access_token,
            'refresh_token': self._refresh_token,
            'scope': self._scope,
            'expires_in': self._expires_in,
            'refresh_token_expires_in': self._refresh_token_expires_in,
            'token_type': self._token_type,
            'refresh_token_expiration_time': self.refresh_token_expiration_time.isoformat(),
            'access_token_expiration_time': self.access_token_expiration_time.isoformat(),
        }

        return token_dict

    def _calculate_refresh_token_expiration(self, expiration_secs: int) -> None:
        """Calculates the number of seconds until the refresh token
        expires.

        ### Parameters
        ----
        expiration_secs : int
            The number of seconds until expiration.
        """

        expiration_time = datetime.now().timestamp() + expiration_secs
        TdCredentials.__consumer_apps[self._client_name]["refresh_token_expiration_time"] = datetime.fromtimestamp(
            expiration_time
        )

    def _calculate_access_token_expiration(self, expiration_secs: int) -> None:
        """Calculates the number of seconds until the access token
        expires.

        ### Parameters
        ----
        expiration_secs : int
            The number of seconds until expiration.
        """

        expiration_time = datetime.now().timestamp() + expiration_secs
        TdCredentials.__consumer_apps[self._client_name]["access_token_expiration_time"] = datetime.fromtimestamp(
            expiration_time
        )

    def from_workflow(self) -> None:
        """Grabs an Access toke and refresh token using
        the oAuth workflow.

        ### Usage
        ----
            >>> td_credentials = TdCredentials()
                client_id=client_id,
                redirect_uri=redirect_uri,
                token_file='config/td_credentials.jsonc'
            )
            >>> td_credentials.from_workflow()
        """

        self.grab_authorization_code()
        token_dict = self.exchange_code_for_token(return_refresh_token=True)
        self.from_token_dict(token_dict=token_dict)

    def from_token_file(self, file_path: Union[str, pathlib.Path]) -> None:

        with open(file=file_path, mode='r') as token_file:
            token_dict = json.load(fp=token_file)
            self.from_token_dict(token_dict=token_dict)

    def to_token_file(self, file_path: Union[str, pathlib.Path]) -> None:
        """Takes the token dictionary and saves it to a JSON file.

        ### Parameters
        ----
        file_path : Union[str, pathlib.Path]
            The file path to the credentials file.

        ### Usage
        ----
            >>> td_credentials.to_token_file(
                    file_path='config/td_credentials.json'
                )
        """

        if not pathlib.Path(self._file_path_base).exists():
            pathlib.Path(self._file_path_base).mkdir()

        if isinstance(file_path, pathlib.Path):
            file_path = file_path.resolve()

        with open(file=file_path, mode='w+') as token_file:
            json.dump(obj=self.to_token_dict(), fp=token_file, indent=2)

    def from_token_dict_helper(self, token_dict: dict) -> None:
        """Loads the credentials from a token dictionary.

        ### Parameters
        ----
        token_dict : dict
            The token dictionary with the required
            authentication tokens.

        ### Usage
        ----

        ### Example 1
        ----
        You don't necessairly need the `refresh_token_expiration_time` or the
        `access_token_expiration_time` because they can be calculated using the
        `access_token` key and `refresh_token`.

            >>> td_credentials.from_token_dict_helper(
                    token_dict={
                        "access_token": "YOUR_ACCESS_TOKEN",
                        "refresh_token": "YOUR_REFRESH_TOKEN"
                        "scope": "PlaceTrades AccountAccess MoveMoney",
                        "expires_in": 1800,
                        "refresh_token_expires_in": 7776000,
                        "token_type": "Bearer",
                        "refresh_token_expiration_time": "2021-07-08T17:38:07.973982",
                        "access_token_expiration_time": "2021-04-09T18:08:07.973982"
                    }
                )

        ### Example 2
        ----
        You don't necessairly need the `refresh_token_expiration_time` or the
        `access_token_expiration_time` because they can be calculated using the
        `access_token` key and `refresh_token`.

            >>> # This just is another way of sending it through.
            >>> td_credentials.from_token_dict_helper(
                    token_dict={
                        "access_token": "YOUR_ACCESS_TOKEN",
                        "refresh_token": "YOUR_REFRESH_TOKEN"
                        "scope": "PlaceTrades AccountAccess MoveMoney",
                        "expires_in": 1800,
                        "refresh_token_expires_in": 7776000,
                        "token_type": "Bearer"
                    }
                )
        """

        self.from_token_dict(token_dict=token_dict)
        self.validate_token()

    def grab_authorization_code(self) -> None:
        """Generates the URL to grab the authorization code."""

        # define the location of the Chrome Driver - CHANGE THIS!!!!!
        executable_path = {
            'executable_path': config.get('scraping', 'browser_directory_path')
        }

        # Create a new instance of the browser, make sure we can see it (Headless = False)
        browser = Browser(config.get('scraping', 'browser_type'), **executable_path, headless=False)

        data = {
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
            "client_id": self.client_id + "@AMER.OAUTHAP"
        }
        method = 'GET'
        url = 'https://auth.tdameritrade.com/auth?'

        # build the URL and store it in a new variable
        p = requests.Request(method, url, params=data).prepare()
        auth_url = p.url

        # go to the URL
        browser.visit(auth_url)

        sleep(2)

        # define items to fillout form
        payload = {'username': self.__login_credentials_dict["username"],
                   'password': self.__login_credentials_dict["account_password"]}

        # fill out each part of the form and click submit
        browser.find_by_id("username0").first.fill(payload['username'])
        browser.find_by_id("password1").first.fill(payload['password'])
        browser.find_by_id("accept").first.click()

        sleep(2)

        browser.find_by_text('Can\'t get the text message?').first.click()

        # Get the Answer Box
        browser.find_by_value("Answer a security question").first.click()

        sleep(2)

        # Answer the Security Questions.
        if browser.is_text_present(self.__login_credentials_dict["secretquestion0"]):
            browser.find_by_id("secretquestion0").first.click()
            browser.find_by_id('secretquestion0').first.fill(
                self.__login_credentials_dict["secretanswer0"])
        elif browser.is_text_present(self.__login_credentials_dict["secretquestion1"]):
            browser.find_by_id("secretquestion0").first.click()
            browser.find_by_id('secretquestion0').first.fill(
                self.__login_credentials_dict["secretanswer1"])
        elif browser.is_text_present(self.__login_credentials_dict["secretquestion2"]):
            browser.find_by_id("secretquestion0").first.click()
            browser.find_by_id('secretquestion0').first.fill(
                self.__login_credentials_dict["secretanswer2"])
        elif browser.is_text_present(self.__login_credentials_dict["secretquestion3"]):
            browser.find_by_id("secretquestion0").first.click()
            browser.find_by_id('secretquestion0').first.fill(
                self.__login_credentials_dict["secretanswer3"])

        browser.find_by_id('accept').first.click()

        sleep(2)

        browser.find_by_text('No, do not trust this device').first.click()
        # Submit results
        browser.find_by_id('accept').first.click()

        sleep(2)

        browser.find_by_id('accept').first.click()

        sleep(2)

        new_url = browser.url
        browser.quit()
        self.authorization_code = unquote(
            new_url.split("code=")[1])

    def exchange_code_for_token(self, return_refresh_token: bool) -> dict:
        """Access token handler for AuthCode Workflow.

        ### Overview
        ----
        This takes the authorization code parsed from
        the auth endpoint to call the token endpoint
        and obtain an access token.

        ### Parameters
        ----
        return_refresh_token: bool
            If set to `True`, will request a refresh token in
            the request. Otherwise, will only request an access
            token along.

        ### Returns
        ----
        dict :
            The token dictionary with the content.
        """

        # Define the parameters of our access token post.
        data = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id + '@AMER.OAUTHAP',
            'code': self.authorization_code,
            'redirect_uri': self.redirect_uri
        }

        if return_refresh_token:
            data['access_type'] = 'offline'

        # Make the request.
        response = requests.post(
            url="https://api.tdameritrade.com/v1/oauth2/token",
            headers={
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            data=data
        )

        if response.ok:
            return response.json()
        else:
            raise requests.HTTPError()

    def grab_access_token(self) -> dict:
        """Refreshes the current access token.

        This takes a valid refresh token and refreshes
        an expired access token. This is different from
        exchanging a code for an access token.

        ### Returns
        ----
        dict:
            The dictionary contain all the token
            info.
        """

        # build the parameters of our request
        data = {
            'client_id': self.client_id,
            'grant_type': 'refresh_token',
            'access_type': 'offline',
            'refresh_token': self.refresh_token
        }

        # Make the request.
        response = requests.post(
            url="https://api.tdameritrade.com/v1/oauth2/token",
            headers={
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            data=data
        )

        if response.ok:
            return response.json()
        else:
            raise requests.HTTPError()

    def validate_token(self) -> None:
        """Validates the access token and refresh token.

        ### Overview
        ----
        A TD Ameritrade Access token is only valid for 30 minutes,
        and a TD Ameritrade Refresh token is only valid for 90 days.
        When an access token expires, a new one is retrieved using the
        refresh token. If the refresh token is expired the oAuth workflow
        starts again.
        """

        if self.is_refresh_token_expired:
            with TdCredentials.__consumer_apps[self._client_name]["multiprocessing_lock"]:
                if self.is_refresh_token_expired:
                    print("Refresh Token Expired, initiating oAuth workflow.")
                    self.from_workflow()
                    self.to_token_file(file_path=self._file_path)

        if self.is_access_token_expired:
            with TdCredentials.__consumer_apps[self._client_name]["multiprocessing_lock"]:
                if self.is_access_token_expired:
                    print("Access Token Expired, refreshing access token.")
                    token_dict = self.grab_access_token()
                    self.from_token_dict(token_dict=token_dict)
                    self.to_token_file(file_path=self._file_path)

        if self._first_pass:
            self._first_pass = False
            self.to_token_file(file_path=self._file_path)

    @staticmethod
    def authentication_default():
        # Get the specified credentials.
        client_name = config.get('credentials', 'client_name')
        client_id = config.get('credentials', 'client_id')
        redirect_uri = config.get('credentials', 'redirect_uri')
        username = config.get('credentials', 'username')
        account_password = config.get('credentials', 'account_password')

        secretquestion0 = config.get('credentials', 'secretquestion0')
        secretanswer0 = config.get('credentials', 'secretanswer0')
        secretquestion1 = config.get('credentials', 'secretquestion1')
        secretanswer1 = config.get('credentials', 'secretanswer1')
        secretquestion2 = config.get('credentials', 'secretquestion2')
        secretanswer2 = config.get('credentials', 'secretanswer2')
        secretquestion3 = config.get('credentials', 'secretquestion3')
        secretanswer3 = config.get('credentials', 'secretanswer3')

        login_credentials = {
            "username": username,
            "account_password": account_password,
            "secretquestion0": secretquestion0,
            "secretanswer0": secretanswer0,
            "secretquestion1": secretquestion1,
            "secretanswer1": secretanswer1,
            "secretquestion2": secretquestion2,
            "secretanswer2": secretanswer2,
            "secretquestion3": secretquestion3,
            "secretanswer3": secretanswer3,
        }

        # Initialize our `Credentials` object.
        return TdCredentials(
            client_name=client_name,
            client_id=client_id,
            redirect_uri=redirect_uri,
            login_credentials_dict=login_credentials
        )
