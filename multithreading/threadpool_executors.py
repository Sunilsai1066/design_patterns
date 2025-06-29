import threading
from concurrent.futures import ThreadPoolExecutor
import time


# Using Manual Threads
def greet(name):
    print(f"Hello, {name}")
    time.sleep(1)
    print(f"Goodbye, {name}")


# Create and start threads manually
t1 = threading.Thread(target=greet, args=("Alice",))
t2 = threading.Thread(target=greet, args=("Bob",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads finished.")
print()


# Using Threadpool Executor
def greet(name):
    print(f"Hello, {name}")
    time.sleep(1)
    print(f"Goodbye, {name}")
    return f"{name} done"


# Use ThreadPoolExecutor to handle threading
with ThreadPoolExecutor(max_workers=2) as executor:
    future1 = executor.submit(greet, "Alice")
    future2 = executor.submit(greet, "Bob")
    future3 = executor.submit(greet, "Carol")
    future4 = executor.submit(greet, "Dave")
    future5 = executor.submit(greet, "Eve")
    future6 = executor.submit(greet, "Fred")

    # Get return values
    print(future1.result())
    print(future2.result())
    print(future3.result())
    print(future4.result())
    print(future5.result())
    print(future6.result())

print("All threads finished.")
