import logging
from logging.handlers import TimedRotatingFileHandler
import pathlib
from td.config.get_config import config


def get_logger(log_name: str = ''):
    if len(log_name):
        logger_name = log_name
    else:
        # Get the specified credentials.
        logger_name = config.get('credentials', 'client_name')

    log = logging.getLogger(logger_name)
    log.setLevel(logging.INFO)

    logging_root_path = config.get('logging', 'logs_directory_path')
    if not pathlib.Path(logging_root_path).exists():
        pathlib.Path(logging_root_path).mkdir()

    logging_app_path = pathlib.Path(logging_root_path + "/" + logger_name)
    if not pathlib.Path(logging_app_path).exists():
        pathlib.Path(logging_app_path).mkdir()

    logger_path = pathlib.Path.joinpath(
        logging_app_path, logger_name + "_log_")

    logHandler = TimedRotatingFileHandler(
        logger_path, when="M", interval=5, encoding="utf-8")

    logHandler.setLevel(logging.INFO)

    logHandler.suffix = "%Y-%m-%d_%H-%M-%S"

    # create formatter and add it to the handlers
    # add colors to the info part
    formatter = logging.Formatter(
        '%(levelname)s: %(asctime)-15s|%(filename)s|%(message)s'
    )

    logHandler.setFormatter(formatter)

    log.addHandler(logHandler)

    return log
