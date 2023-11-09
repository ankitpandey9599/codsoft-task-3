# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added: " + task)

# Function to remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed: " + task)
    else:
        print("Task not found: " + task)

# Function to display the list of tasks
def display_tasks():
    if tasks:
        print("To-Do List:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")
    else:
        print("Your to-do list is empty.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        print("Goodbye!")
        break
