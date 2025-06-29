import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


class Counter:
    def __init__(self):
        self.count = 0  # Shared counter
        self.lock = threading.Lock()

    def inc(self):
        with self.lock:
            temp = self.count
            time.sleep(0.0001)  # Small delay to allow context switch (race condition exposure)
            self.count = temp + 1  # Write
        return self.count


if __name__ == '__main__':
    counter = Counter()

    with ThreadPoolExecutor(max_workers=5) as executor:
        n = 1000
        for _ in range(n):  # Smaller number for demo; increase for stronger effect
            executor.submit(counter.inc)

    print(f"Expected count: {n}")
    print(f"Actual count: {counter.count}")
