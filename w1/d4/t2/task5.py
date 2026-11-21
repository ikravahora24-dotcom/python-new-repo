
mode = "Global Mode"  # Global variable


def outer_function():
    mode = "Enclosing Mode"  # Enclosing variable

    def inner_function():
        mode = "Local Mode"  # Local variable

        print("Inside inner function:", mode)

    print("Inside outer function:", mode)

    inner_function()


print("Outside functions:", mode)

outer_function()

print("After function calls:", mode)
