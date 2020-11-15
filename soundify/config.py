'''
helper functions related to configuration file
'''

from yaml import safe_load
from pathlib import Path
from os import path


# TODO: platform independant
CONFIG_FILE = str(Path.home()) + '/.soundify.yml'


def config_exist():
    '''check config file is available'''
    global CONFIG_FILE

    if not path.exists(CONFIG_FILE):
        return False
    return True


def read_config():
    '''read config file'''
    global CONFIG_FILE

    if not config_exist():
        print('config not exist', CONFIG_FILE)
        return {}

    with open(CONFIG_FILE, 'r') as config_file:
        config_dict = safe_load(config_file)

    return config_dict

