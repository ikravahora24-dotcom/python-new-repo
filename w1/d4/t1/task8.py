import time

# Creating a decorator
def timer(func):

    def wrapper():
        start_time = time.time()

        # Calling the original function
        func()

        end_time = time.time()

        # Calculate execution time
        total_time = end_time - start_time

        print("Execution Time:", total_time, "seconds")

    return wrapper


# Applying decorator
@timer
def calculate_sum():

    total = sum(range(1, 1000001))

    print("Sum of numbers:", total)


# Function calling
calculate_sum()