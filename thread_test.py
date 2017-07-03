import time
from threading import Thread
from wp_diff import wp_diff, status

file_path = 'C:\\xampp\\htdocs\\wordpress-1'
t = Thread(target=wp_diff, args=(file_path,))
t.start()

count = 0
while count != 60:
    time.sleep(1)
    count += 1            
    print("This program has now been running for {} seconds - {}".format(str(count), status))
