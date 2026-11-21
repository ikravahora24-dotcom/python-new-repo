from functools import reduce

# Create a list of numbers
numbers = [25, 78, 12, 95, 43, 67]

# Find the largest number using reduce()
largest = reduce(lambda a, b: a if a > b else b, numbers)

# Print the result
print("Numbers:", numbers)
print("Largest Number:", largest)