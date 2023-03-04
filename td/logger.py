from pathlib import Path
import logging
from logging.handlers import TimedRotatingFileHandler
from td.config import TdConfiguration


class TdLogger:
    """
    ### Overview

    Handles logging for the api
    """

    def __init__(self, log_name: str = None) -> None:
        """
        Initializes the TdLogger object

        ### Parameters
        config: TdConfiguration
            The config object of your program
        
        log_name: str = None
            The name of the log you want to use. 
            Defaults to the log named after your application.
        """
        self._config = TdConfiguration()
        self._log_root_path = self._config.logs_directory_path

        if log_name:
            self._log_name = log_name
        else:
            self._log_name = self._config.app_name

        self._log_module_path = Path.joinpath(Path(self._log_root_path), self._log_name)
        self._log_path = Path.joinpath(self._log_module_path, self._log_name)

        if not Path.exists(Path(self._log_root_path)):
            Path.mkdir(Path(self._log_root_path))

        if not Path.exists(self._log_module_path):
            Path.mkdir(self._log_module_path)

        self._log_handler = TimedRotatingFileHandler(
            self._log_path, when='M', interval=5, encoding='utf-8'
        )

        self._log = logging.getLogger(self._log_name)
        self._log.setLevel(logging.INFO)

        self._log_handler.setLevel(logging.INFO)

        self._log_handler.suffix = '%Y-%m-%d_%H-%M-%S'

        self._formatter = logging.Formatter(
            '%(levelname)s: %(asctime)-15s|%(filename)s|%(message)s'
        )

        self._log_handler.setFormatter(self._formatter)

        self._log.addHandler(self._log_handler)


    def info(self, msg, *args) -> None:
        """
        Intended as a drop in replacement for the old log object

        ----
        ### Usage
            >>> log = TdLogger(config)
            >>> log.info("There was a noteworthy event!")
        """

        self._log.info(msg, *args)
    
    def error(self, msg, *args) -> None:
        """
        Intended as a drop in replacement for the old error object

        ----
        ### Usage
            >>> log = TdLogger(config)
            >>> log.error("There was an error!")
        """

        self._log.error(msg, *args)
