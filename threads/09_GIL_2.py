""" 
This script uses Python's threading to parallelize a countdown task, 
and it also demonstrates how reference counting works in Python. 

Add explanations to clarify what each section of the code does 
and the implications of the Global Interpreter Lock (GIL) in this context:
"""

import time
from threading import Thread
import sys  # Import the sys module to access system-specific parameters and functions.

COUNT = 50000000  # Define the number of times the countdown will loop.

def countdown(n):
    """
    Function that counts down from `n` to 0, decreasing by 1 in each iteration.

    Args:
    n (int): The starting number for the countdown.
    """
    while n > 0:
        n -= 1  # Decrement n until it reaches zero.

# Create two threads, each will handle half of the total count.
t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()  # Record the start time of the threads.
t1.start()  # Start the first thread.
t2.start()  # Start the second thread.
t1.join()  # Wait for the first thread to finish.
t2.join()  # Wait for the second thread to finish.
end = time.time()  # Record the end time after both threads have finished.

print('Time taken in seconds -', end - start)  # Output the total time taken for both threads to complete.

# Example to show how Python manages memory using reference counting:
a = []  # Create an empty list.
b = a  # Assign 'b' to refer to the same list 'a' does.
print('Refcount = ', sys.getrefcount(a))  # Print the reference count for the list 'a'.

# Commentary about Python's GIL and its effects:
# The GIL (Global Interpreter Lock) is a mutex that protects access to Python objects,
# preventing multiple native threads from executing Python bytecodes at once. This lock is necessary
# because Python's memory management is not thread-safe. The GIL can be a bottleneck in CPU-bound
# and multithreaded code as it forces threads to execute in series rather than in parallel.


""" Key Notes

Threading and GIL: 
    The threading module allows for concurrent programming, 
    but due to the GIL in the standard CPython interpreter, 
    you may not see a speedup in CPU-bound tasks like the countdown function. 
    The GIL ensures that only one thread executes Python bytecode at a time even 
    on multi-core processors. This can make threading appear ineffective for CPU-bound tasks.

Reference Counting: 
    Python uses reference counting as part of its memory management. 
    In your example, sys.getrefcount(a) returns the number of references 
    to the object referenced by a (including the reference by getrefcount itself).

Multi-threading Use Case: 
    For I/O-bound tasks, Python's threading can still be beneficial, 
    as the GIL is released during I/O operations, allowing other threads to run Python code.

"""
