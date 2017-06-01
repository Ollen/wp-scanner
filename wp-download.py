""" Download WordPress files and hashes """
import requests, zipfile, os

dir_path = os.path.dirname(os.path.realpath(__file__)) + '\\wp-files'

def extract(ver):
    """Extract a WordPress version in \\wp"""
    extract_path = dir_path + '\\{}'.format(ver)
    zip_filename = "wordpress-{}.zip".format(ver)
    zip_filepath = dir_path + '\\' + zip_filename

    # Check if zip exists
    if not os.path.exists(zip_filepath):
        print '[ERROR] wordpress-{}.zip not found'.format(ver)
        quit()

    # Create extract dir.
    if not os.path.exists(extract_path):
        print 'Creating {} directory'.format(extract_path)
        os.makedirs(extract_path)
    
    try:
        # Extract zip version
        print 'EXTRACTING ' + zip_filename
        z = zipfile.ZipFile(zip_filepath)
        z.extractall(extract_path)
    except (zipfile.BadZipfile, zipfile.LargeZipFile) as e:
        print '[ERROR] Bad/Large zip file'
    else:
        print '[DONE] Extract finish'
    

def download(ver):
    url = "https://wordpress.org/wordpress-{}.zip".format(ver)
    zip_filename = url.split('/')[-1]

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
        print '[ERROR]: Conenction error'
        quit()
    except requests.Timeout:
        print '[ERROR]: Connection timeout'
        quit()

    print '[DONE] Download finished'

    extract(ver)

download('4.7.5')






