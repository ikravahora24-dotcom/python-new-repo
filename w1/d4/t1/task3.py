# List of temperatures in Celsius
celsius = [0, 10, 20, 30, 40, 50]

# Convert Celsius to Fahrenheit using map() and lambda
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

# Print the results
print("Celsius Temperatures:", celsius)
print("Fahrenheit Temperatures:", fahrenheit)