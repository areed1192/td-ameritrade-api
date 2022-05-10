import configparser
import inspect
from os import path


class TdConfiguration():
    """ ### Overview
        ----
        Handles client configuration data,
        such as account number, consumer key, etc.
    """

    def __init__(self, config_path: str) -> None:
        """Initializes the Configuration object.

        ### Parameters
        config_path: str
            The relative path to your config.ini file. An example is located
            in `td/config/config-example.ini`

            Note: This path is relative to the file calling this class,
            an absolute path will not work correctly
        """

        # This is kinda funky, but it grabs the full path to the file which called this class
        # Then it grabs the directory that its in, and then uses that to find the config file
        self._caller_filename = inspect.stack()[1].filename
        self._caller_directory = path.basename(self._caller_filename)
        self._config_path = path.join(self._caller_directory, config_path)
        self._config = configparser.ConfigParser()
        self._config.read(self._config_path)

        # This section grabs all the information from the config file
        self.app_name = self._config.get('app_info', 'app_name')
        self.client_id = self._config.get('app_info', 'client_id')
        self.redirect_uri = self._config.get('app_info', 'redirect_uri')

        self.username = self._config.get('credentials', 'username')
        self.account_password = self._config.get('credentials', 'account_password')
        self.secretquestion0 = self._config.get('credentials', 'secretquestion0')
        self.secretanswer0 = self._config.get('credentials', 'secretanswer0')
        self.secretquestion1 = self._config.get('credentials', 'secretquestion1')
        self.secretanswer1 = self._config.get('credentials', 'secretanswer1')
        self.secretquestion2 = self._config.get('credentials', 'secretquestion2')
        self.secretanswer2 = self._config.get('credentials', 'secretanswer2')
        self.secretquestion3 = self._config.get('credentials', 'secretquestion3')
        self.secretanswer3 = self._config.get('credentials', 'secretanswer3')

        self.default = self._config.get('accounts', 'default')
        self.TD_IRA_ROTH_ACCOUNT = self._config.get('accounts', 'TD_IRA_ROTH_ACCOUNT')
        self.TD_CASH_ACCOUNT = self._config.get('accounts', 'TD_CASH_ACCOUNT')
        self.TD_MARGIN_ACCOUNT = self._config.get('accounts', 'TD_MARGIN_ACCOUNT')

        self.logs_directory_path = self._config.get('logging', 'logs_directory_path')

        self.config_directory_path = self._config.get('config', 'config_directory_path')

        self.browser_directory_path = self._config.get('scraping', 'browser_directory_path')
        self.browser_type = self._config.get('scraping', 'browser_type')

        self.app_info = {
            "app_name" : self.app_name,
            "client_id" : self.client_id,
            "redirect_uri" : self.redirect_uri
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
            "default" : self.default,
            "TD_IRA_ROTH_ACCOUNT" : self.TD_IRA_ROTH_ACCOUNT,
            "TD_CASH_ACCOUNT" : self.TD_CASH_ACCOUNT,
            "TD_MARGIN_ACCOUNT" : self.TD_MARGIN_ACCOUNT
        }

        # Even though the next two only have 1 entry currenty,
        # I am still putting it in a dictionary for consistency
        # And it will make life easier if we decide to add more in the future

        self.logging = {
            "logs_directory_path" : self.logs_directory_path
        }

        self.config_information = {
            "config_directory_path" : self.config_directory_path
        }

        self.scraping_information = {
            "browser_directory_path" : self.browser_directory_path,
            "browser_type" : self.browser_type
        }

    def get(self, section: str = None, variable: str = None):
        """
        Returns the value of the user config variable requested.
        Added as a drop in replacement for the old config.get() method.
        ----
        ### Usage
            >>> config = Configuration("path/to/config")
            >>> config.get("app_info", "app_name")
        """

        # Dictionairy to look up the section requested by the user
        sectDict = {
            "app_info" : self.app_info,
            "credentials" : self.login_credentials,
            "accounts" : self.accounts,
            "logging" : self.logging,
            "config" : self.config_information,
            "scraping" : self.scraping_information
        }

        #Which dictionairy to look in
        userSection = sectDict[section]

        #The actual value the user is looking for
        userVariable = userSection[variable]

        return userVariable

    def get_app_info(self) -> dict:
        """Returns the app_info for the `Credentials` object"""

        return self.app_info

    def get_login_credentials(self) -> dict:
        """Returns the login_credentials for the `Credentials` object"""

        return self.login_credentials

    def get_accounts(self) -> dict:
        """Returns the accounts for the `Credentials` object"""

        return self.accounts

    def get_logging(self) -> dict:
        """Returns the logging information for the `Credentials` object"""

        return self.logging

    def get_config_information(self) -> dict:
        """Returns the config information for the `Credentials` object"""

        return self.config_information

    def get_scraping_info(self) -> dict:
        """Returns the web scraping information for the `Credentials` object"""

        return self.scraping_information
