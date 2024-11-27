import time

def run_function_at_frequency(func, frequency, duration):
    interval = 1.0 / frequency  # Time interval between function calls in seconds
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        start_cycle = time.time()
        func()
        end_cycle = time.time()
        delta_time = end_cycle - start_cycle
        #print(f"Delta time: {delta_time:.6f} seconds")
        time_to_sleep = interval - delta_time
        if time_to_sleep > 0:
            time.sleep(time_to_sleep)


#frequency = 5  # Run the function 5 times per second
#duration = 10  # Run for 10 seconds
#run_function_at_frequency(example_function, frequency, duration)
