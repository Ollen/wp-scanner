""" Returns the database config data located in 'db_config.json' """
import json
import os

def read_config():
    """ Returns the decoded config data in 'db_config.json'
    Will return the decoded config file if 'db_config.json' exists and is a valid JSON format.
    Otherwise, it will return a False.
    """
    # Check if file exists
    if not os.path.isfile('db_config.json'):
        return False

    # Check if file is a valid JSON format.
    try:
        with open('db_config.json') as json_data:
            config = json.load(json_data)
    except ValueError:
        print '[WARN] Error Decoding config.json'
        return False
    return config


def check_config_keys(config):
    """ Checks if the dictionary keys are valid.
    Returns a True boolean if all the required keys are present,
    Otherwise returns a False boolean.

    Keywork Arguments:
    config -- <Dictionary> Decoded JSON config dictionary 
    """

    db_config = config
    db_keys = ['user', 'password', 'host', 'database']
    if not all(key in db_config for key in db_keys):
        return False

    return True

def create_default_config():
    """ Creats a 'db_config.json' file if it doesn't exist or is an invalid JSON format. """
    print 'Creating default DB config'
    default_config = {
        'user': 'user',
        'password': '',
        'host': '127.0.0.1',
        'database': 'wp_scan'
    }

    with open('db_config.json', 'w') as jsonfile:
        json_output = json.dumps(default_config , ensure_ascii=False, sort_keys=True ,indent=4, separators=(',', ': '))
        jsonfile.write(json_output)

    return default_config

def get_config():
    """ Main database config module fetcher.
    Returns the config data in the 'db_config.json' file.
    """
    config = read_config()
    if config:
        if check_config_keys(config):
            return config

        else: 
            return create_default_config()

    else:
        return create_default_config()