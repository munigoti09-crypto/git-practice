tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    print("Your tasks: ", tasks)

add_task("Learn git")
show_tasks()