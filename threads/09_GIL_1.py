""" 
This script defines a simple countdown function that decrements a counter from a given number down to zero, 
measuring the time it takes to complete this operation in a single-threaded context.
"""

import time  # Import time module to measure the performance of the code.
from threading import Thread  # Import Thread for possible threading implementation.

COUNT = 50000000  # Set the number of decrements.

def countdown(n):
    """
    Decrements an integer from n to 0.

    Args:
    n (int): The starting integer value from which to countdown.
    """
    while n > 0:
        n -= 1  # Decrement n until it reaches zero.

start = time.time()  # Record the start time before the countdown.
countdown(COUNT)  # Call the countdown function with the initial count.
end = time.time()  # Record the end time after the countdown finishes.

print('Time taken in seconds -', end - start)  # Print the time taken to perform the countdown.



""" 
Multithreading Implementation
If your goal is to explore how threading might impact this type of operation, 
you should be aware that for CPU-bound tasks like this countdown, 
Python's Global Interpreter Lock (GIL) may prevent threads from executing in true parallel, 
potentially leading to no performance gain or even a slowdown. 
However, for educational purposes, you can modify the script to use threads and compare performance. 

Here's an example of how you might implement threading:
"""

import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n > 0:
        n -= 1

def threaded_countdown():
    t1 = Thread(target=countdown, args=(COUNT//2,))  # Create first thread to handle half of the count.
    t2 = Thread(target=countdown, args=(COUNT//2,))  # Create second thread to handle the other half.

    start = time.time()  # Start timing before threads start.
    t1.start()  # Start first thread.
    t2.start()  # Start second thread.

    t1.join()  # Wait for the first thread to finish.
    t2.join()  # Wait for the second thread to finish.
    end = time.time()  # Stop timing after all threads have finished.

    print('Time taken in seconds with multithreading -', end - start)

start = time.time()  # Record the start time before the single-threaded countdown.
countdown(COUNT)  # Single-threaded countdown.
end = time.time()  # Record the end time after the countdown finishes.
print('Time taken in seconds -', end - start)  # Output the time for single-threaded countdown.

threaded_countdown()  # Run the multithreaded countdown and print its time.
