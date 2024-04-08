import threading
import time
import requests
# i/o bounded and different between thread and sqeuntial: threading is better
def request_github():
    response = requests.get('https://github.com/rezaghfi')
    time.sleep(1)
    response.raise_for_status()

thread1 = threading.Thread(target = request_github)
thread2 = threading.Thread(target = request_github)

start_time_threaded = time.time()
thread1.start()
thread2.start()
thread2.join()
thread1.join()
end_time_threaded = time.time()
print(f'execution time with thread: {end_time_threaded - start_time_threaded}')

start_time_sqentail = time.time()
request_github()
request_github()
end_time_sqentail = time.time()
print(f'execution time without thread: {end_time_sqentail - start_time_sqentail}')