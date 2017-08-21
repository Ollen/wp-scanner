import json, os

def read_config():
    if not os.path.isfile('config.json'):
        return False

    try:
        with open('config.json') as json_data:
            config = json.load(json_data)
    except ValueError:
        print('[WARN] Error Decoding config.json')
        return False
    
    return config

def check_config_keys(config):
    if ('FTP_CONFIG' not in config) and ('DB_CONFIG' not in config):
        return False

    return True

def get_config():
    config = read_config()
    if config:
        print 'yay'
    else:
        print 'nay' 

if __name__ == '__main__':
    get_config()

