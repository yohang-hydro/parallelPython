import logging  # Import the logging module to enable logging of debug and runtime information.
import threading  # The threading module is used to run multiple threads (tasks, function calls) in a single process.
import time  # Import time module to use sleep function for simulating delay.
from concurrent.futures import ThreadPoolExecutor  # Import ThreadPoolExecutor for managing a pool of threads.

def thread_kernel(thread_index):
    """
    Function to be executed by each thread, logging its start and completion.

    Args:
    thread_index (int): Index identifying the current thread.

    Returns:
    str: A message stating which thread has completed.
    """
    logging.info("I am thread %s", thread_index)  # Log message indicating which thread is starting.
    time.sleep(2)  # Simulate a task with a sleep/delay of 2 seconds.
    logging.info("I am thread %s, and I am done", thread_index)  # Log message when thread completes its task.
    return "I am thread " + str(thread_index)  # Return a string message that this thread is complete.

if __name__ == "__main__":
    # Define the format for logging, including timestamp and message content.
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")  # Configure basic settings for logging system.

    thread_indices = [1, 2, 3]  # List of thread indices to be passed to threads.

    # Create an instance of ThreadPoolExecutor with a specified number of worker threads.
    with ThreadPoolExecutor(max_workers=8) as pool:
        # Submit tasks to the pool; this is non-blocking and immediately returns control to the main thread.
        results = pool.map(thread_kernel, thread_indices)

        # Print results as they become available. This operation will block until all threads have completed.
        for res in results:
            print(res)  # Print the result returned from each thread.
    # The ThreadPoolExecutor is automatically shut down when exiting the 'with' block.
    # This ensures all threads are joined before exiting the main script.

# All threads enqueued to ThreadPoolExecutor will be joined before the interpreter can exit.
