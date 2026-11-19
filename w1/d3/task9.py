tasks=[]
def add_task(task):
    tasks.append(task)
    print(task,"added successfully!")
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(task,"removed successfully!")
    else:
        print(task,"not found!")
def show_tasks():
    print("\n current to-do list:")
    if tasks:
            for task in tasks:
                print("-",task)
    else:
                print("no tasks available.")
                
add_task("complete project")
add_task("learrn python")
add_task("practice coding")
add_task("read a book")
show_tasks()
remove_task("learn python")
remove_task("complete project")
show_tasks()
