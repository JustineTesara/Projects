
tasks = []


def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")


def view_task():
    print("\nLists of task")
    for task in tasks:
        print(f"- {task}")


def delete_task():
    print("Removed task.")
    tasks.pop()


def clear_tasks():
    print("Removed all tasks")
    tasks.clear()


def mark_as_done():
    if not tasks:
        print("No tasks to mark as done.")
        return
    task_index = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_index < len(tasks):
        print(f"Task '{tasks[task_index]}' marked as done.")
        tasks.pop(task_index)
    else:
        print("Invalid task number.")


while True:
    print("===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete a task")
    print("4. Delete all items")
    print("5. Mark as done")
    print("6. Exit")
    user_prompt = input("Enter your choice: ")
    if user_prompt == "1":
        add_task()
        print(f"Current tasks: {tasks}")
    elif user_prompt == "2":
        view_task()
    elif user_prompt == "3":
        delete_task()
    elif user_prompt == "4":
        clear_tasks()
    elif user_prompt == "5":
        mark_as_done()
    elif user_prompt == "6":
        print("Program Terminated.")
        break
