""" Download WordPress files and hashes """
import requests
import zipfile, StringIO
import os

dir_path = os.path.dirname(os.path.realpath(__file__)) + '\\wp-files'

def download(ver):
    url = "https://wordpress.org/wordpress-{}.zip".format(ver)
    zip_filename = url.split('/')[-1]
    extract_path = dir_path + '\\{}'.format(ver)

    # Create wp-files if it doesn't exist
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    # Download version
    r = requests.get(url, stream=True)
    with open('{}\\{}'.format(dir_path, zip_filename), 'wb') as code:
        code.write(r.content)
    
    # Create extract dir.
    os.makedirs(extract_path)

    # Extract zip version
    z = zipfile.ZipFile(StringIO.StringIO(r.content))
    z.extractall(extract_path)

download('4.7.5')






