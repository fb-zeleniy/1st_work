import time
import datetime
def create_file(filename, data):
    time.sleep(1)
    with open(filename, 'w') as file:
        file.write(data)
    print(filename)
 
  