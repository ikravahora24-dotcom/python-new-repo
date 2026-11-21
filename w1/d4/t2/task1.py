# Global variable
count = 0

# Function to count how many times it is called
def my_function():
    global count

    count += 1
    print("Function called:", count, "times")


# Calling the function 4 times
my_function()
my_function()
my_function()
my_function()

# Print final count
print("Total Function Calls:", count)