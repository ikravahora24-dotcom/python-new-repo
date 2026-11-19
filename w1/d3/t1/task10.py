
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(task, "added successfully!")

# Function to remove a task
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(task, "removed successfully!")
    else:
        print(task, "not found!")

# Function to display tasks
def show_tasks():
    print("\nCurrent To-Do List:")
    if tasks:
        for task in tasks:
            print("-", task)
    else:
        print("No tasks available.")

# Adding 5 tasks
add_task("Complete project")
add_task("Learn Python")
add_task("Practice coding")
add_task("Read a book")
add_task("Complete homework")

# Display all tasks
show_tasks()

# Removing 2 tasks
remove_task("Learn Python")
remove_task("Complete project")

# Display remaining tasks
show_tasks()
