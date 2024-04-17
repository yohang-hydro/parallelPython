import logging  # Import the logging module for outputting debug and runtime information.
import threading  # Import threading for creating and managing threads.
import time
from time import sleep  # Import sleep to simulate processing delays.

sum = 0  # A global variable to hold the sum modified by multiple threads.

def thread_kernel_add(thread_index, repeat, value):
    """
    Function that increments the global sum variable in a thread-safe manner using a lock.

    Args:
    thread_index (int): The identifier for the thread, for logging.
    repeat (int): The number of iterations to perform the addition.
    value (int): The value to add to the global sum in each iteration.
    """
    logging.info("I am thread %s", thread_index)
    global sum  # Access to the global variable 'sum'
    global lock  # Access to the global lock object
    logging.info("Initial sum in thread %s: %d", thread_index, sum)
   
    lock.acquire()  # Acquire the lock before modifying the shared resource
    for i in range(repeat):
        tmp = sum
        sleep(0)  # Simulate processing delay
        tmp = tmp + value
        sleep(0)  # Simulate processing delay
        sum = tmp
    lock.release()  # Release the lock after modifying the shared resource

    logging.info("Final sum in thread %s: %d", thread_index, sum)
    logging.info("I am thread %s, and I am done", thread_index)

def thread_kernel_sub(thread_index, repeat, value):
    """
    Function that decrements the global sum variable in a thread-safe manner using a lock.

    Args:
    thread_index (int): The identifier for the thread, for logging.
    repeat (int): The number of iterations to perform the subtraction.
    value (int): The value to subtract from the global sum in each iteration.
    """
    logging.info("I am thread %s", thread_index)
    global sum  # Access to the global variable 'sum'
    global lock  # Access to the global lock object
    logging.info("Initial sum in thread %s: %d", thread_index, sum)
    
    lock.acquire()  # Acquire the lock before modifying the shared resource
    for i in range(repeat):
        tmp = sum
        sleep(0)  # Simulate processing delay
        tmp = tmp - value
        sleep(0)  # Simulate processing delay
        sum = tmp
    lock.release()  # Release the lock after modifying the shared resource

    logging.info("Final sum in thread %s: %d", thread_index, sum)
    logging.info("I am thread %s, and I am done", thread_index)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")  # Set up basic configuration for logging.
    
    lock = threading.Lock()  # Create a lock object to synchronize thread access to the shared 'sum' variable.
    
    # Create and start threads for adding to and subtracting from the sum.
    adder = threading.Thread(target=thread_kernel_add, args=(1, 1000000, 100))  # Thread for adding to the sum.
    subtractor = threading.Thread(target=thread_kernel_sub, args=(2, 1000000, 100))  # Thread for subtracting from the sum.
    
    adder.start()  # Start the adder thread.
    subtractor.start()  # Start the subtractor thread.
    
    adder.join()  # Wait for the adder thread to complete.
    subtractor.join()  # Wait for the subtractor thread to complete.
    
    print("Sum = " + str(sum))  # Print the final value of the sum after both threads have completed.
