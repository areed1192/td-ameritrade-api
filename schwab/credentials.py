"""This module contains the `CharlesSchwabCredentials` class."""

import json
import urllib
import pathlib
import webbrowser

from typing import Union
from datetime import datetime
from urllib.parse import parse_qs
from urllib.parse import urlparse
from base64 import b64encode

import requests


class CharlesSchwabCredentials:
    """
    ### Overview
    ----
    Charles Schwab's OAuth 2.0 workflow allows your application
    to obtain access and refresh tokens that let you call Schwab APIs
    on behalf of a user. This object helps manage and refresh those tokens.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        credential_dict: dict = None,
        credential_file: Union[str, pathlib.Path] = None,
    ) -> None:
        """
        Initializes the `CharlesSchwabCredentials` object.

        Parameters
        ----------
        client_id : str
            The Client ID (also called Consumer Key) assigned by Schwab.

        client_secret : str
            The Client Secret assigned by Schwab.

        redirect_uri : str
            The redirect (callback) URL where the user is sent after
            authorizing access in Schwab's LMS.

        credential_dict : dict
            Optional. A dictionary containing saved tokens you want to load.

        credential_file : Union[str, pathlib.Path]
            Optional. A path to a JSON file containing saved tokens.
        """

        self._access_token = ""
        self._refresh_token = ""
        self._scope = []
        self._token_type = ""
        self._expires_in = 0
        self._refresh_token_expires_in = 0
        self._is_expired = True
        self._client_id = client_id
        self._client_secret = client_secret
        self._redirect_uri = redirect_uri

        self._refresh_token_expiration_time = 0
        self._access_token_expiration_time = 0

        # Schwab OAuth Endpoints
        self._authorization_endpoint = "https://api.schwabapi.com/v1/oauth/authorize"
        self._token_endpoint = "https://api.schwabapi.com/v1/oauth/token"

        self.authorization_code = ""
        self._loaded_from_file = False
        self._file_path = ""

        # Check if the credential file exists.
        if credential_file and not isinstance(credential_file, pathlib.Path):
            credential_file = pathlib.Path(credential_file).resolve()

        # Decide how to load credentials.
        if credential_file and credential_file.exists():
            self._loaded_from_file = True
            self._file_path = credential_file
            self.from_credential_file(file_path=credential_file)
            self.to_credential_file(file_path=credential_file)
        elif credential_dict:
            self.from_credential_dict(token_dict=credential_dict)
        # If a file path is provided but the file doesn't exist.
        elif credential_file and not credential_file.exists():
            self.from_workflow()
            self._loaded_from_file = True
            self._file_path = credential_file
            self.to_credential_file(file_path=credential_file)
        # If no credentials supplied, run the OAuth 2 flow.
        else:
            self.from_workflow()

    @property
    def redirect_uri(self) -> str:
        """Returns the user's redirect URI."""
        return self._redirect_uri

    @property
    def client_id(self) -> str:
        """Returns the Client ID."""
        return self._client_id

    @property
    def client_secret(self) -> str:
        """Returns the Client Secret."""
        return self._client_secret

    @property
    def access_token(self) -> str:
        """Returns the current access token."""
        return self._access_token

    @property
    def refresh_token(self) -> str:
        """Returns the current refresh token."""
        return self._refresh_token

    @property
    def refresh_token_expiration_time(self) -> datetime:
        """Returns when the Refresh Token will expire."""
        return self._refresh_token_expiration_time

    @property
    def is_refresh_token_expired(self) -> bool:
        """Checks if the refresh token has expired."""
        exp_time = self.refresh_token_expiration_time - 20
        now = datetime.now().timestamp()
        return bool(exp_time < now)

    @property
    def access_token_expiration_time(self) -> datetime:
        """Returns when the Access Token will expire."""
        return self._access_token_expiration_time

    @property
    def is_access_token_expired(self) -> bool:
        """Checks if the access token has expired."""
        exp_time = self.access_token_expiration_time - 20
        now = datetime.now().timestamp()
        return bool(exp_time < now)

    def from_token_dict(self, token_dict: dict) -> None:
        """Loads token information from a dictionary."""

        self._access_token = token_dict.get("access_token", "")
        self._refresh_token = token_dict.get("refresh_token", "")
        self._scope = token_dict.get("scope", [])

        self._token_type = token_dict.get("token_type", "")
        self._expires_in = token_dict.get("expires_in", 0)

        if "refresh_token_expiration_time" in token_dict:
            self._refresh_token_expiration_time = datetime.fromisoformat(
                token_dict["refresh_token_expiration_time"]
            ).timestamp()
        else:
            # If the refresh token expiration time is not in the dictionary.
            self._refresh_token_expiration_time = datetime.now().timestamp() + 604800

        if "access_token_expiration_time" in token_dict:
            self._access_token_expiration_time = datetime.fromisoformat(
                token_dict["access_token_expiration_time"]
            ).timestamp()
        else:
            # If the access token expiration time is not in the dictionary.
            self._access_token_expiration_time = (
                datetime.now().timestamp() + self._expires_in
            )

        self.validate_token()

    def to_token_dict(self) -> dict:
        """Converts the credential data to a dictionary."""
        token_dict = {
            "access_token": self._access_token,
            "refresh_token": self._refresh_token,
            "scope": self._scope,
            "expires_in": self._expires_in,
            "refresh_token_expires_in": self._refresh_token_expires_in,
            "token_type": self._token_type,
            "refresh_token_expiration_time": datetime.fromtimestamp(
                self.refresh_token_expiration_time
            ).isoformat(),
            "access_token_expiration_time": datetime.fromtimestamp(
                self.access_token_expiration_time
            ).isoformat(),
        }
        return token_dict

    def from_workflow(self) -> None:
        """
        Executes the full OAuth flow:
        1. Directs the user to Schwab's LMS for Consent & Grant.
        2. Exchanges the Authorization Code for Access & Refresh tokens.
        """
        self.grab_authorization_code()
        token_dict = self.exchange_code_for_token()
        self.from_token_dict(token_dict=token_dict)

    def from_credential_file(self, file_path: str) -> None:
        """Loads credentials from a JSON file."""

        with open(file=file_path, mode="r", encoding="utf-8") as token_file:
            token_dict = json.load(fp=token_file)
            self.from_token_dict(token_dict=token_dict)

    def to_credential_file(self, file_path: Union[str, pathlib.Path]) -> None:
        """Saves the current tokens to a JSON file."""
        if isinstance(file_path, pathlib.Path):
            file_path = file_path.resolve()
        with open(file=file_path, mode="w+", encoding="utf-8") as token_file:
            json.dump(obj=self.to_token_dict(), fp=token_file, indent=2)

    def from_credential_dict(self, token_dict: dict) -> None:
        """Loads the credentials from a token dictionary."""
        self.from_token_dict(token_dict=token_dict)
        self.validate_token()

    def grab_authorization_code(self) -> None:
        """
        Step 1: Obtain the authorization code.

        This builds a URL with your 'client_id' and 'redirect_uri'
        and opens it in the user’s browser. The user signs in,
        grants access, and is redirected back to your redirect_uri
        with a '?code=' parameter in the URL.

        You copy-paste that URL (or code) back here to continue.
        """
        # Build the URL parameters.
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
        }
        url_params = urllib.parse.urlencode(params)
        auth_url = f"{self._authorization_endpoint}?{url_params}"

        # Open browser for user to log in.
        try:
            print(f"Open the URL (if it doesn't open automatically):\n{auth_url}\n")
            webbrowser.open(url=auth_url)

            # Ask the user to paste back the final URL which contains '?code=...'
            code_url = input("Paste the full callback URL here: ")

            # Parse out the 'code' from the callback URL.
            parsed_url = urlparse(code_url)

            # Typically, the code is in the query string as "code=<value>"
            query_data = parse_qs(parsed_url.query)
            self.authorization_code = query_data["code"][0]

        except KeyError as e:
            raise ValueError(
                "Error: Could not find 'code' in the URL. Please try again."
            ) from e

        except Exception as e:  # pylint: disable=broad-exception-caught
            print(f"Error parsing the URL: {e}")

    def exchange_code_for_token(self) -> dict:
        """
        Step 2: Exchange the Authorization Code for tokens.

        Sends a POST to Schwab's /oauth/token endpoint to get:
        - access_token (valid ~30 minutes)
        - refresh_token (valid ~7 days)
        """
        # Schwab requires Basic Auth (client_id:client_secret).
        client_creds = f"{self.client_id}:{self.client_secret}"
        b64_creds = b64encode(client_creds.encode("utf-8")).decode("utf-8")
        headers = {
            "Authorization": f"Basic {b64_creds}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        # The body parameters:
        data = {
            "grant_type": "authorization_code",
            "code": self.authorization_code,
            "redirect_uri": self.redirect_uri,
        }

        # Make the token request.
        response = requests.post(
            url=self._token_endpoint, headers=headers, data=data, timeout=10
        )

        if response.ok:
            return response.json()

        raise requests.HTTPError(
            f"Token request failed with status {response.status_code}: {response.text}"
        )

    def grab_access_token(self) -> dict:
        """Step 4 (Refresh step): Use your existing refresh token to
        get a new access token.

        Sends a POST to Schwab's /oauth/token with grant_type=refresh_token
        and your existing refresh token.
        """
        # Schwab requires Basic Auth again.
        client_creds = f"{self.client_id}:{self.client_secret}"
        b64_creds = b64encode(client_creds.encode("utf-8")).decode("utf-8")
        headers = {
            "Authorization": f"Basic {b64_creds}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        data = {"grant_type": "refresh_token", "refresh_token": self.refresh_token}

        response = requests.post(
            url=self._token_endpoint, headers=headers, data=data, timeout=10
        )

        if response.ok:
            return response.json()

        raise requests.HTTPError(
            f"Refresh request failed with status {response.status_code}: {response.text}"
        )

    def validate_token(self) -> None:
        """
        Checks if the tokens are expired and refreshes if needed.
        If refresh token is also expired, restarts the OAuth flow.
        """

        # If the refresh token is expired, we must do the full OAuth flow again.
        if self.is_refresh_token_expired:
            print("Refresh Token Expired or invalid. Initiating full OAuth workflow...")
            self.from_workflow()
            return

        # If only the access token is expired, refresh it.
        if self.is_access_token_expired:
            print("Access Token expired, attempting to refresh...")
            token_dict = self.grab_access_token()
            self.from_token_dict(token_dict=token_dict)

            if self._loaded_from_file:
                self.to_credential_file(file_path=self._file_path)
