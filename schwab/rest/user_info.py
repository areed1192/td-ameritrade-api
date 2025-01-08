"""Used to access the `UserInfo` Services and metadata."""

from typing import List
from schwab.session import CharlesSchwabSession


class UserInfo:
    """
    ## Overview
    ----
    Allows the user to query information about their profile,
    modify settings that are related to the API and retrieve
    streaming keys that can be used with the Streaming API
    client.
    """

    def __init__(self, session: CharlesSchwabSession) -> None:
        """Initializes the `UserInfo` services.

        ### Parameters
        ----
        session : CharlesSchwabSession
            An authenticated `CharlesSchwabSession
            object.

        ### Usage
        ----
            >>> user_info_service = client.user_service()
        """

        self.session = session

    def get_preferences(self) -> dict:
        """Get user preference information for the logged in user.

        ### Usage
        ----
            >>> user_info_service = client.user_service()
            >>> user_info_service.get_preferences()
        """

        content = self.session.make_request(
            method="get",
            endpoint="userPreference",
        )

        return content
