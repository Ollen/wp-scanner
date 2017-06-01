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
        print 'Creating /wp-files directory.'
        os.makedirs(dir_path)
    
    # Download version
    print 'DOWNLOADING {}...'.format(zip_filename)
    try:
        r = requests.get(url, stream=True, timeout=60)
        with open('{}\\{}'.format(dir_path, zip_filename), 'wb') as code:
            code.write(r.content)
    except requests.ConnectionError:
        print '[ERROR]: Conenction Error'
        quit()
    except requests.Timeout:
        print '[ERROR]: Connection timeout'
        quit()

    print '[DONE] Download finished'

    # Create extract dir.
    if not os.path.exists(extract_path):
        print 'Creating {} directory'.format(extract_path)
        os.makedirs(extract_path)

    # Extract zip version
    print 'EXTRACTING ' + zip_filename
    z = zipfile.ZipFile(StringIO.StringIO(r.content))
    z.extractall(extract_path)
    print '[DONE] Extract finish'

download('4.7.5')






