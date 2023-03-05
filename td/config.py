import inspect
from os import path, environ, getenv
from pathlib import Path
import configparser


class TdConfiguration:
    """
    Handles client configuration data such as account number, consumer key, etc.

    ...

    Attributes
    ----------
    app_info : AppInfoConfiguration
        The application information configuration object.
    credentials : CredentialsConfiguration
        The login credentials configuration object.
    accounts : AccountsConfiguration
        The accounts configuration object.
    logging : LoggingConfiguration
        The logging configuration object.

    Methods
    -------
    get_login_credentials() -> dict:
        Returns the login credentials for the `Credentials` object.

    """

    def __init__(self, config_path: str = "config/config.ini") -> None:
        """
        Initializes the Configuration object.

        Parameters
        ----------
        config_path: str
            The relative path to your config.ini file. An example is located
            in `td/z-config-example.ini`.

            Note: This path is relative to the file calling this class,
            an absolute path will not work correctly. Or you can set the path
            explicitly by setting the TD_API_CONFIG_PATH environment variable.
        """

        class AppInfoConfiguration:
            """
            Handles application information configuration data.

            ...

            Attributes
            ----------
            app_name : str
                The name of the application.
            client_id : str
                The client ID of the application.
            redirect_uri : str
                The redirect URI of the application.

            """

            def __init__(self, config_parser):
                self.app_name = config_parser.get("app_info", "app_name")
                self.client_id = config_parser.get("app_info", "client_id")
                self.redirect_uri = config_parser.get(
                    "app_info", "redirect_uri")

        if "TD_API_CONFIG_PATH" not in environ:
            # This is kinda funky, but it grabs the full path to the file which called this class
            # Then it grabs the directory that its in, and then uses that to find the config file
            self._caller_directory = Path(
                Path(inspect.stack()[-1].filename).parents[0])
            self._config_directory_path = Path(
                path.join(self._caller_directory, config_path))
        else:
            self._config_directory_path = Path(getenv("TD_API_CONFIG_PATH"))
        self._config_directory_parent_path = Path(
            self._config_directory_path.parents[0])

        self._config_parser = configparser.ConfigParser()
        self._config_parser.read(self._config_directory_path)

        self.app_info = AppInfoConfiguration(self._config_parser)
        self.credentials = CredentialsConfiguration(self._config_parser)
        self.accounts = AccountsConfiguration(self._config_parser)
        self.logging = LoggingConfiguration(self._config_parser)

    def get_login_credentials(self) -> dict:
        """
        Returns the login_credentials for the `Credentials` object.

        Returns
        -------
        dict
            The login credentials.
        """

        return self.credentials.login_credentials


class CredentialsConfiguration:
    """
    Handles login credentials configuration data.

    ...

    Attributes
    ----------
    login_credentials : dict
        The login credentials.

    Methods
    -------
    None

    """

    def __init__(self, config_parser):
        """
        Initializes the CredentialsConfiguration object.

        Parameters
        ----------
        config_parser : ConfigParser
            The configuration parser object.
        """
        self.config_present = False
        if config_parser.has_section("accounts"):
            self.config_present = True
            self.username = config_parser.get("credentials", "username")
            self.account_password = config_parser.get(
                "credentials", "account_password")
            self.secretquestion0 = config_parser.get(
                "credentials", "secretquestion0")
            self.secretanswer0 = config_parser.get(
                "credentials", "secretanswer0")
            self.secretquestion1 = config_parser.get(
                "credentials", "secretquestion1")
            self.secretanswer1 = config_parser.get(
                "credentials", "secretanswer1")
            self.secretquestion2 = config_parser.get(
                "credentials", "secretquestion2")
            self.secretanswer2 = config_parser.get(
                "credentials", "secretanswer2")
            self.secretquestion3 = config_parser.get(
                "credentials", "secretquestion3")
            self.secretanswer3 = config_parser.get(
                "credentials", "secretanswer3")

            self.login_credentials = {
                "username": self.username,
                "account_password": self.account_password,
                "secretquestion0": self.secretquestion0,
                "secretanswer0": self.secretanswer0,
                "secretquestion1": self.secretquestion1,
                "secretanswer1": self.secretanswer1,
                "secretquestion2": self.secretquestion2,
                "secretanswer2": self.secretanswer2,
                "secretquestion3": self.secretquestion3,
                "secretanswer3": self.secretanswer3
            }
        else:
            self.login_credentials = None


class AccountsConfiguration:
    """
    Handles accounts configuration data.

    ...

    Attributes
    ----------
    default_account : str
        The default account.
    roth_ira : str
        The Roth IRA account.
    traditional_ira : str
        The Traditional IRA account.
    cash_account : str
        The cash account.
    margin_account : str
        The margin account.

    Methods
    -------
    None

    """

    def __init__(self, config_parser):
        """
        Initializes the AccountsConfiguration object.

        Parameters
        ----------
        config_parser : ConfigParser
            The configuration parser object.
        """

        self.config_present = False
        if config_parser.has_section("accounts"):
            self.config_present = True
            self.default_account = config_parser.get(
                "accounts", "default_account")
            self.roth_ira = config_parser.get("accounts", "roth_ira")
            self.traditional_ira = config_parser.get(
                "accounts", "traditional_ira")
            self.cash_account = config_parser.get("accounts", "cash_account")
            self.margin_account = config_parser.get(
                "accounts", "margin_account")


class LoggingConfiguration:
    """
    Handles logging configuration data.

    ...

    Attributes
    ----------
    logs_directory_path : str
        The directory path for the logs.

    Methods
    -------
    None

    """

    def __init__(self, config_parser):
        """
        Initializes the LoggingConfiguration object.

        Parameters
        ----------
        config_parser : ConfigParser
            The configuration parser object.
        """

        self.config_present = False
        if config_parser.has_section("logging"):
            self.config_present = True
            self.logs_directory_path = config_parser.get(
                "logging", "logs_directory_path")
