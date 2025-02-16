import json
import os

TASKS_FILE = "tasks.json"

# Load tasks from JSON file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("\nNo tasks found!\n")
        return
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "❌"
        print(f"{idx}. {task['task']} [{status}]")
    print()

# Add a new task
def add_task():
    task_name = input("Enter the task: ")
    tasks = load_tasks()
    tasks.append({"task": task_name, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

# Mark task as completed
def complete_task():
    view_tasks()
    tasks = load_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task():
    view_tasks()
    tasks = load_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            deleted_task = tasks.pop(task_number)
            save_tasks(tasks)
            print(f"Deleted task: {deleted_task['task']}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# Main menu loop
def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
