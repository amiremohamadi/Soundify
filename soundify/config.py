'''
helper functions related to configuration file
'''

from yaml import safe_load
from appdirs import user_config_dir
from os import path


CONFIG_DIR = user_config_dir() + '/soundify'
CONFIG_FILE = CONFIG_DIR + '/config.yml'


def config_exist():
    '''check config file/dir is available'''
    global CONFIG_DIR
    global CONFIG_FILE

    if not path.exists(CONFIG_DIR):
        return False

    if not path.exists(CONFIG_FILE):
        return False

    return True


def read_config():
    '''read config file'''
    global CONFIG_FILE

    if not config_exist():
        return {}

    with open(CONFIG_FILE, 'r') as config_file:
        config_dict = safe_load(config_file)

    return config_dict

