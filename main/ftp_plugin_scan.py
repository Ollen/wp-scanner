""" Scans the plugin directories """
import requests

def scan_plugin_dir(con):
    """ 
    Reads the plugin directory names and .php file extension
    located in `wp-content/plugins`
    """
    dir_path = './wp-content/plugins'
    # Check if plugin_dir exists
    if con.path.exists(dir_path):
        print 'SCANNING `wp-content/plugins`...'
    else:
        print '[ERROR] Could not find `wp-content/plugins`'
        quit()
    
    plugin_listdir = con.listdir(dir_path)
    plugin_dirs = []
    plugin_files = []
    for names in plugin_listdir:
        if con.path.isdir('{}/{}'.format(dir_path, names)):
            plugin_dirs.append(names)
        elif names.endswith('.php'):
            plugin_files.append(names)

    print '[DONE]: Scanned `wp-content/plugins'
    return {'plugin_dirs': plugin_dirs, 'plugin_files': plugin_files}


def verify_plugins(plugins):
    """
    Verifies the plugin by checking if it exists in the WordPress plugin SVN
    """
    plugin_url = 'http://plugins.svn.wordpress.org/'
    
    print 'VERIFYING plugins...'
    plugin_res = {'verified': [], 'unverified': []}
    for plugin in plugins:
        r = requests.head('{}{}/'.format(plugin_url, plugin))
        if r.status_code!= 200:
            plugin_res['unverified'].append(plugin)
        else:
            plugin_res['verified'].append(plugin)

    print '[DONE] Verifying plugins'
    return plugin_res