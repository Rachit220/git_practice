import os
import json
import datetime
from tabulate import tabulate  

TASK_FILE = "tasks.json"

def load_tasks():
    """Load tasks from file, return empty list if file doesn't exist."""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to file."""
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(title, description, due_date):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "due_date": due_date,
        "status": "Pending",
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    table = [[t["id"], t["title"], t["description"], t["due_date"], t["status"], t["created_at"]] for t in tasks]
    headers = ["ID", "Title", "Description", "Due Date", "Status", "Created At"]
    print(tabulate(table, headers=headers, tablefmt="grid"))

def update_task(task_id, status):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = status
            save_tasks(tasks)
            print(f" Task {task_id} updated to '{status}'")
            return
    print("Task not found.")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    print(f" Task {task_id} deleted.")
def menu():
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Task Title: ")
            description = input("Task Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            add_task(title, description, due_date)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            task_id = int(input("Enter Task ID: "))
            status = input("Enter new status (Pending/Completed): ")
            update_task(task_id, status)

        elif choice == "4":
            task_id = int(input("Enter Task ID: "))
            delete_task(task_id)

        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    menu()