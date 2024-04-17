import logging  # Importing the logging module for logging messages.
import threading  # Importing the threading module to utilize multiple threads.
import time  # Importing the time module for time-related tasks.

def thread_kernel(thread_thread_index):
    """
    Executes a task on a separate thread.
    
    Logs a message when the thread starts and after a simulated task delay, logs another message
    indicating completion.

    Args:
    thread_thread_index (int): The index of the thread, used for identification in logs.
    """
    logging.info("I am thread %s", thread_thread_index)  # Log entry for the start of the thread.
    time.sleep(2)  # Simulate a task delay of 2 seconds.
    logging.info("I am thread %s, and I am done", thread_thread_index)  # Log entry for the end of the thread.

# This conditional statement checks if the script is the main program and is not being imported as a module.
if __name__ == "__main__":
    # Define the format for logging messages, including a timestamp.
    format = "%(asctime)s: %(message)s"
    # Configure the logging system to display information level messages with the specified format and time format.
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    list_threads = list()  # Initialize a list to store threads.
    for thread_index in range(3):  # Loop to create three threads.
        logging.info("Create thread %d", thread_index)  # Log the creation of a thread.
        thread_x = threading.Thread(target=thread_kernel, args=(thread_index,))  # Initialize a Thread object.
        list_threads.append(thread_x)  # Append the new thread to the list of threads.
        thread_x.start()  # Start the thread.

    for thread_index, thread_x in enumerate(list_threads):  # Iterate over the list of threads.
        thread_x.join()  # Wait for the thread to finish.
        logging.info("Join thread %d", thread_index)  # Log the completion of thread joining.
