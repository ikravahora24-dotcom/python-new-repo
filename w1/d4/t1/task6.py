# Recursive function to calculate sum from 1 to n
def calculate_sum(n):

    # Base condition
    if n == 1:
        return 1

    # Recursive call
    else:
        return n + calculate_sum(n - 1)


# Function calling
num = 5
result = calculate_sum(num)

print("Number:", num)
print("Sum of numbers from 1 to", num, "is:", result)