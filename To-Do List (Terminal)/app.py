
tasks = []
tasks_done = []


def add_task():
    task = input("Enter a new task: ")
    if task.isdigit() or not task.strip():  # Check if the task is empty or just digits
        print("Invalid task. Please enter a valid task description.")
    else:
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
    # [a.insert(4, b.pop(idx)) for idx in [b.index(10)]] - Move One List Element to Another List
    index_input = input(
        "Enter the index of the task to mark as done (0 to {}): ".format(len(tasks) - 1))
    if not index_input.isdigit() or int(index_input) < 0 or int(index_input) >= len(tasks):
        print("Invalid index. Please enter a valid index.")
        return
    else:
        idx = int(index_input)
        [tasks_done.insert(0, tasks.pop(idx))
         for idx in [0]] if tasks else None
        print("Marked as done.")
    print("Tasks done: ", tasks_done)


def mark_as_done_list():
    print("Tasks done: ")
    for task in tasks_done:
        print(f"- {task}")


while True:
    print("===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete a task")
    print("4. Delete all items")
    print("5. Mark as done")
    print("6. View completed tasks")
    print("7. Exit")
    user_prompt = input("Enter your choice: ")
    if user_prompt == "1":
        add_task()
    elif user_prompt == "2":
        view_task()
    elif user_prompt == "3":
        delete_task()
    elif user_prompt == "4":
        clear_tasks()
    elif user_prompt == "5":
        mark_as_done()
    elif user_prompt == "6":
        mark_as_done_list()
    elif user_prompt == "7":
        print("Program Terminated.")
        break
    else:
        print("Invalid choice. Please try again.")
    print()  # Print a new line for better readability
