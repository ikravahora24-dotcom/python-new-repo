# Outer function
def update_status():

    status = "pending"

    # Inner function
    def change_status():
        nonlocal status
        status = "completed"

    # Calling inner function
    change_status()

    # Printing final status
    print("Final Status:", status)


# Function calling
update_status()