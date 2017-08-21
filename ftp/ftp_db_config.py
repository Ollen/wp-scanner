import json, os

def read_config():
    if not os.path.isfile('db_config.json'):
        return False

    try:
        with open('db_config.json') as json_data:
            config = json.load(json_data)
    except ValueError:
        print('[WARN] Error Decoding config.json')
        return False
    
    return config

def check_config_keys(config):
    if ('DB_CONFIG' not in config):
        return False

    db_config = config['DB_CONFIG']
    db_keys = ['user', 'password', 'host', 'database']
    if not all(key in db_config for key in db_keys):
        return False

    return True

def create_default_config():
    print ('Creating default DB config')
    default_config = {
        "DB_CONFIG": {
            'user': 'user',
            'password': '',
            'host': '127.0.0.1',
            'database': 'wp_scan'
        }
    }

    with open('db_config.json', 'w') as jsonfile:
        json_output = json.dumps(default_config , ensure_ascii=False, sort_keys=True ,indent=4, separators=(',', ': '))
        jsonfile.write(json_output)
    
    return default_config
    

def get_config():
    config = read_config()
    if config:
        if check_config_keys(config):
            return config

        else: 
            return create_default_config()

    else:
        return create_default_config()

if __name__ == '__main__':
    get_config()

