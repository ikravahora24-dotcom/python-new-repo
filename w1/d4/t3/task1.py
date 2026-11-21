
def safe_division(a, b):
    try:
        result = a / b
        return result

    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"

    except TypeError:
        return "Error: Please enter numeric values!"


print(safe_division(20, 4))
print(safe_division(20, 0))
print(safe_division(20, "hello"))
