import threading
import time

# global interpreter lock - GIL
# یک قفل است که دستوراتی که محدود به پردازنده است باعث می شود که نخ های مختلف هم بصورت که فقط یک نخ اچرا در یک زمان می شود و شبیه حالت پشت سر هم می شود.
#باید برویم سر چند پردازه ای استفاده کنیم.
#cpu bound : dont diffrent bettween threading and sqeuntial
def calculate_fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)

fibonacci_thread1 = threading.Thread(target=calculate_fibonacci, args=(38,))
fibonacci_thread2 = threading.Thread(target=calculate_fibonacci, args=(38,))

start_time_threaded = time.time()
fibonacci_thread1.start()
fibonacci_thread2.start()
fibonacci_thread2.join()
fibonacci_thread1.join()
end_time_threaded = time.time()
print(f"execution time with threading : {end_time_threaded - start_time_threaded}")

start_time_sequentially = time.time()
calculate_fibonacci(38)
calculate_fibonacci(38)
end_time_sequentially = time.time()
print(f"execution time without threading : {end_time_sequentially - start_time_sequentially}")