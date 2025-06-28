import threading
import time
from concurrent.futures import ThreadPoolExecutor  # Used to manage thread pool


# Class to simulate sending an SMS
class SendSms:
    def __init__(self):
        pass

    @staticmethod
    def process():
        print("Sending SMS")
        time.sleep(2)  # Simulate delay (I/O-bound task)
        print("Sent SMS")


# Class to simulate sending an Email
class SendEmail:
    def __init__(self):
        pass

    @staticmethod
    def process():
        print("Sending Email")
        time.sleep(3)  # Simulate delay (I/O-bound task)
        print("Sent Email")


# Class to simulate calculating ETA (Estimated Time of Arrival)
class SendETA:
    def __init__(self):
        pass

    @staticmethod
    def process():
        print("Sending ETA")
        time.sleep(5)  # Simulate longer delay
        print("Sent ETA")
        return 20  # Return some result (e.g., minutes)


# Main program starts here
if __name__ == "__main__":
    # Create a thread pool executor (default max_workers = number of processors * 5 or so)
    with ThreadPoolExecutor() as executor:
        # Submit ETA task to the thread pool (runs in background thread)
        # Using ThreadPoolExecutor here, so we can get a return value using `eta.result()`
        eta = executor.submit(SendETA.process)

        # Create separate threads manually for SMS and Email tasks
        t1 = threading.Thread(target=SendSms.process)
        t2 = threading.Thread(target=SendEmail.process)

        # Start both threads
        t1.start()
        t2.start()

        # Wait until both threads (SMS and Email) finish
        t1.join()
        t2.join()

        # Wait for ETA thread to complete and get the return value
        print(f"ETA {eta.result()}")  # Blocks until ETA task finishes

        print("All threads finished execution.")  # Final confirmation
