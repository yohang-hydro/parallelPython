import logging  # Import the logging module for capturing log messages.
import threading  # Import the threading module for threading operations.
import time  # Import the time module to handle time-related tasks.
from concurrent.futures import ThreadPoolExecutor  # Import ThreadPoolExecutor for managing a pool of threads efficiently.

def thread_kernel(thread_index):
    """
    Function to be run by a thread, logs the start and end of its process, and returns a string message.

    Args:
    thread_index (int): Identifier for the thread, used in logging and returned string.

    Returns:
    str: Message indicating which thread has completed.
    """
    logging.info("I am thread %s", thread_index)  # Log the start of the thread's task.
    time.sleep(2)  # Simulate doing work by sleeping for 2 seconds.
    logging.info("I am thread %s, and I am done", thread_index)  # Log the completion of the thread's task.
    return "I am thread " + str(thread_index)  # Return a string indicating the thread's completion.

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")  # Setup the logging configuration.

    # Create an instance of ThreadPoolExecutor with up to 8 worker threads.
    pool = ThreadPoolExecutor(max_workers=8)

    # Submit a single task to the thread pool and get a Future object.
    future = pool.submit(thread_kernel, 1)  # Submitting the thread_kernel function with argument 1. This call is non-blocking.

    # Block and wait for the future's result, effectively waiting for the thread to complete.
    result = future.result()  # Retrieving the result of the thread, this will block until the thread completes.

    print(result)  # Print the result received from the thread.

    pool.shutdown()  # Properly shutdown the ThreadPoolExecutor, freeing up resources.
