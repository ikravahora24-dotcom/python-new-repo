# Closure function
def make_counter():

    count = 0

    def counter():
        nonlocal count

        count += 1
        return count

    return counter


# Create two independent counters
counter1 = make_counter()
counter2 = make_counter()


# Call first counter 4 times
print("Counter 1:")
print(counter1())
print(counter1())
print(counter1())
print(counter1())

print("--------------------")

# Call second counter 2 times
print("Counter 2:")
print(counter2())
print(counter2())

print("--------------------")

# Print final results
print("Final Counter 1:", counter1())
print("Final Counter 2:", counter2())