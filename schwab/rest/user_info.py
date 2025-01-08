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

    def get_preferences(self, account_id: str) -> dict:
        """Get's User Preferences for a specific account.

        ### Parameters
        ----
        account_id: str
            The User's TD Ameritrade account ID.

        ### Usage
        ----
            >>> user_info_service = client.user_service()
            >>> user_info_service.get_preferences(
                account_id='123456789'
            )
        """

        content = self.session.make_request(
            method="get",
            endpoint=f"accounts/{account_id}/preferences",
        )

        return content

    def get_streamer_subscription_keys(self, account_ids: List[str]) -> dict:
        """SubscriptionKey for provided accounts or default accounts.

        ### Parameters
        ----
        account_ids: List[str]
            A list of account IDs.

        ### Usage
        ----
            >>> user_info_service = client.user_service()
            >>> user_info_service.get_streamer_subscription_keys(
                account_ids=['123456789']
            )
        """

        params = {"accountIds": ",".join(account_ids)}

        content = self.session.make_request(
            method="get",
            endpoint="userprincipals/streamersubscriptionkeys",
            params=params,
        )

        return content

    def get_user_principals(self) -> dict:
        """Get's User principals details.

        ### Usage
        ----
            >>> user_info_service = client.user_service()
            >>> user_info_service.get_user_principals()
        """

        params = {
            "fields": "streamerSubscriptionKeys,streamerConnectionInfo,preferences,surrogateIds"
        }

        content = self.session.make_request(
            method="get", endpoint="userprincipals", params=params
        )

        return content
