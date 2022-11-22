import configparser
import inspect
from os import path, environ, getenv
from pathlib import Path
from pprint import pprint


class TdConfiguration():
    """ ### Overview
        ----
        Handles client configuration data,
        such as account number, consumer key, etc.
    """

    def __init__(self, config_path: str = "config/config.ini") -> None:
        """Initializes the Configuration object.

        ### Parameters
        config_path: str
            The relative path to your config.ini file. An example is located
            in `td/z-config-example.ini`

            Note: This path is relative to the file calling this class,
            an absolute path will not work correctly. Or you can set the path
            explicitly by setting the TD_API_CONFIG_PATH environment variable.
        """

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

        self._config = configparser.ConfigParser()
        self._config.read(self._config_directory_path)

        # This section grabs all the from the config file
        self.app_name = self._config.get('app_info', 'app_name')
        self.client_id = self._config.get('app_info', 'client_id')
        self.redirect_uri = self._config.get('app_info', 'redirect_uri')

        self.username = self._config.get('credentials', 'username')
        self.account_password = self._config.get(
            'credentials', 'account_password')
        self.secretquestion0 = self._config.get(
            'credentials', 'secretquestion0')
        self.secretanswer0 = self._config.get('credentials', 'secretanswer0')
        self.secretquestion1 = self._config.get(
            'credentials', 'secretquestion1')
        self.secretanswer1 = self._config.get('credentials', 'secretanswer1')
        self.secretquestion2 = self._config.get(
            'credentials', 'secretquestion2')
        self.secretanswer2 = self._config.get('credentials', 'secretanswer2')
        self.secretquestion3 = self._config.get(
            'credentials', 'secretquestion3')
        self.secretanswer3 = self._config.get('credentials', 'secretanswer3')

        self.default = self._config.get('accounts', 'default')
        self.ROTH_IRA = self._config.get('accounts', 'ROTH_IRA')
        self.TRADITIONAL_IRA = self._config.get('accounts', 'TRADITIONAL_IRA')
        self.CASH = self._config.get('accounts', 'CASH')
        self.MARGIN = self._config.get('accounts', 'MARGIN')

        self.logs_directory_path = Path(
            self._config.get('logging', 'logs_directory_path'))

        self.browser_directory_path = Path(
            self._config.get('scraping', 'browser_directory_path'))
        self.browser_type = self._config.get('scraping', 'browser_type')

        self.app_info = {
            "app_name": self.app_name,
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri
        }

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
            "secretanswer3": self.secretanswer3,
        }

        self.accounts = {
            "default": self.default,
            "ROTH_IRA": self.ROTH_IRA,
            "TRADITIONAL_IRA": self.TRADITIONAL_IRA,
            "CASH": self.CASH,
            "MARGIN": self.MARGIN
        }

        # Still use a dictionary for consistency
        # And it will make life easier if we decide to add more in the future

        self.logging = {
            "logs_directory_path": self.logs_directory_path
        }

        self.config = {
            "config_directory_path": self._config_directory_path,
            "config_directory_parent_path": self._config_directory_parent_path
        }

        self.scraping = {
            "browser_directory_path": self.browser_directory_path,
            "browser_type": self.browser_type
        }

    def get(self, section: str = None, variable: str = None):
        """
        Returns the value of the user config variable requested.
        Added as a drop in replacement for the old config.get() method.
        ----
        ### Usage
            >>> config = Configuration("path/to/config")
            >>> config.get("app", "app_name")
        """

        # Dictionairy to look up the section requested by the user
        sectDict = {
            "app_info": self.app_info,
            "credentials": self.login_credentials,
            "accounts": self.accounts,
            "logging": self.logging,
            "config": self.config,
            "scraping": self.scraping
        }

        # Which dictionairy to look in
        userSection = sectDict[section]

        # The actual value the user is looking for
        userVariable = userSection[variable]

        return userVariable

    def get_app_info(self) -> dict:
        """Returns the app info for the `Credentials` object"""

        return self.app_info

    def get_login_credentials(self) -> dict:
        """Returns the login_credentials for the `Credentials` object"""

        return self.login_credentials

    def get_accounts(self) -> dict:
        """Returns the accounts for the `Credentials` object"""

        return self.accounts

    def get_logging_info(self) -> dict:
        """Returns the logging info  for the `Credentials` object"""

        return self.logging

    def get_config_info(self) -> dict:
        """Returns the config info for the `Credentials` object"""

        return self.config

    def get_scraping_info(self) -> dict:
        """Returns the web scraping info  for the `Credentials` object"""

        return self.scraping