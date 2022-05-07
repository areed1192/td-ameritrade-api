import configparser
import os

path_current_directory = os.path.dirname(__file__)
path_config_file = os.path.join(path_current_directory, 'config.ini')
config = configparser.ConfigParser()
config.read(path_config_file)
