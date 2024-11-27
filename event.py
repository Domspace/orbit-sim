import time

def run_function_at_frequency(func, frequency, duration):
    """
    Run the given function at the specified frequency for a certain duration.

    :param func: The function to run.
    :param frequency: The desired frequency in Hz (times per second).
    :param duration: The duration in seconds for which to run the function.
    """
    interval = 1.0 / frequency  # Time interval between function calls in seconds
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        start_cycle = time.time()
        
        # Call the function
        func()
        
        end_cycle = time.time()
        delta_time = end_cycle - start_cycle
        print(f"Delta time: {delta_time:.6f} seconds")
        
        # Calculate the time to sleep to maintain the desired frequency
        time_to_sleep = interval - delta_time
        if time_to_sleep > 0:
            time.sleep(time_to_sleep)


# Example usage
#frequency = 5  # Run the function 5 times per second
#duration = 10  # Run for 10 seconds
#run_function_at_frequency(example_function, frequency, duration)
