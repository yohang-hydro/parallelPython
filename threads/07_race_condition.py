import logging
import threading
import time
from time import sleep

sum = 0  # Global variable to keep track of the sum

def thread_kernel_add(thread_index, repeat, value):
    """
    Function to increment a global sum variable in a threaded environment.

    Args:
    thread_index (int): Identifier for the thread for logging purposes.
    repeat (int): Number of times to repeat the addition.
    value (int): Value to add to the global sum.
    """
    logging.info("I am thread %s", thread_index)
    global sum  # Declare that this function intends to use the global 'sum' variable
    logging.info("Initial sum in thread %s: %d", thread_index, sum)
   
    for i in range(repeat):
        tmp = sum  # Local snapshot of sum
        sleep(0)  # Simulate some processing time
        tmp = tmp + value  # Increment local snapshot
        sleep(0)  # More processing time simulation
        sum = tmp  # Update global sum

    logging.info("Final sum in thread %s: %d", thread_index, sum)
    logging.info("I am thread %s, and I am done", thread_index)

def thread_kernel_sub(thread_index, repeat, value):
    """
    Function to decrement a global sum variable in a threaded environment.

    Args:
    thread_index (int): Identifier for the thread for logging purposes.
    repeat (int): Number of times to repeat the subtraction.
    value (int): Value to subtract from the global sum.
    """
    logging.info("I am thread %s", thread_index)
    global sum  # Declare that this function intends to use the global 'sum' variable
    logging.info("Initial sum in thread %s: %d", thread_index, sum)
    
    for i in range(repeat):
        tmp = sum  # Local snapshot of sum
        sleep(0)  # Simulate some processing time
        tmp = tmp - value  # Decrement local snapshot
        sleep(0)  # More processing time simulation
        sum = tmp  # Update global sum

    logging.info("Final sum in thread %s: %d", thread_index, sum)
    logging.info("I am thread %s, and I am done", thread_index)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")  
    
    # Launch threads to modify the global sum concurrently
    adder = threading.Thread(target=thread_kernel_add, args=(1, 1000000, 100))  # Thread for adding to sum
    subtractor = threading.Thread(target=thread_kernel_sub, args=(2, 1000000, 100))  # Thread for subtracting from sum
    
    adder.start()
    subtractor.start()
    
    adder.join()  # Wait for the adder thread to complete
    subtractor.join()  # Wait for the subtractor thread to complete
    
    print("Sum = " + str(sum))  # Output the final value of sum

