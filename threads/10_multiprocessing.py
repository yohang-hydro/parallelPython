""" 
Python's multiprocessing to parallelize a countdown task, 
which circumvents the limitations imposed by the Global Interpreter Lock (GIL). 
This allows for true parallel execution of CPU-bound tasks like your countdown 
on systems with multiple cores.
"""

from multiprocessing import Pool  # Import Pool from multiprocessing to manage a pool of worker processes.
import time  # Import time to track the execution duration.

COUNT = 50000000  # Define the total number of decrements.

def countdown(n):
    """
    Decrements an integer from n to 0.

    Args:
    n (int): The starting integer value from which to countdown.
    """
    while n > 0:
        n -= 1  # Decrement n until it reaches zero.

if __name__ == '__main__':
    pool = Pool(processes=2)  # Create a pool of 2 worker processes.

    start = time.time()  # Record the start time of the countdown.

    # Launch asynchronous tasks within the process pool.
    # Each process receives its own Python interpreter and memory space, hence bypassing the GIL.
    r1 = pool.apply_async(countdown, [COUNT//2])  # Start an asynchronous task for half the count.
    r2 = pool.apply_async(countdown, [COUNT//2])  # Start another asynchronous task for the other half.

    pool.close()  # Prevent any more tasks from being submitted to the pool.
    pool.join()  # Wait for the worker processes to complete their tasks.

    end = time.time()  # Record the end time after all processes have finished.

    # Processes involve higher overhead compared to threads, but they are not restricted by the GIL.
    print('Time taken in seconds -', end - start)  # Output the total time taken for the tasks to complete.

