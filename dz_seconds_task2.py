import time
import datetime
from concurrent.futures import ThreadPoolExecutor


def create_file(filename, data):
    time.sleep(1)
    with open(filename, 'w') as file:
        file.write(data)
    print(filename)
 
start_time = time.time()

with ThreadPoolExecutor() as executor:
    for i in range(100):
        executor.submit(create_file, f"file_{i}.txt", f" File's data {i}")

end_time = time.time()
execution_time = end_time - start_time

execution_time