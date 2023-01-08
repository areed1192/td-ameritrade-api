import inspect
from os import path, environ, getenv
from pathlib import Path
import configparser


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

        self._config_parser = configparser.ConfigParser()
        self._config_parser.read(self._config_directory_path)

        for section in self._config_parser.sections():
            for item in self._config_parser.items(section):
                item_name = str(item[0])
                setattr(self, item_name, item[1])

        self.login_credentials = {
            "username": self.username, # pylint: disable=E1101:no-member
            "account_password": self.account_password,  # pylint: disable=E1101:no-member
            "secretquestion0": self.secretquestion0,  # pylint: disable=E1101:no-member
            "secretanswer0": self.secretanswer0,  # pylint: disable=E1101:no-member
            "secretquestion1": self.secretquestion1,  # pylint: disable=E1101:no-member
            "secretanswer1": self.secretanswer1,  # pylint: disable=E1101:no-member
            "secretquestion2": self.secretquestion2,  # pylint: disable=E1101:no-member
            "secretanswer2": self.secretanswer2, # pylint: disable=E1101:no-member
            "secretquestion3": self.secretquestion3,  # pylint: disable=E1101:no-member
            "secretanswer3": self.secretanswer3,  # pylint: disable=E1101:no-member
        }

    def get_login_credentials(self) -> dict:
        """Returns the login_credentials for the `Credentials` object"""

        return self.login_credentials
