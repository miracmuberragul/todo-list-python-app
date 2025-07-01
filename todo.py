import json
import os
from datetime import datetime

def load_tasks():
    if os.path.exists("tasks.json"):
        try:
            with open("tasks.json") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Warning: tasks.json is empty or corrupted. Starting with an empty task list.")
            return []
    return []



def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
def get_valid_date():
    while True:
        date_input=input("enter the date input date (dd.mm.yyyy) ").strip()
        if not date_input:
            return "No date"
        try:
            datetime.strptime(date_input, "%d.%m.%Y" )
            return date_input
        except ValueError:
            print("Invalid date format! Please use dd.mm.yyyy (Example: 05.07.2025)")






def add_tasks(tasks):
    title = input("Enter title: ").strip()
    due_date = get_valid_date()
    task = {
        "title": title,
        "completed": False,
        "due_date": due_date if due_date else "No date"
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def list_tasks(tasks):
    if not tasks:
        print("No tasks added!")
        return
    print("Task list:")
    for idx, task in enumerate(tasks):
        status = "yes" if task['completed'] else "no"
        print(f"{idx + 1}. {task['title']} (Due: {task['due_date']}) - [{status}]")

def complete_tasks(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter index to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks(tasks)
            print("Task completed successfully!")
        else:
            print("Invalid index")
    except ValueError:
        print("Please enter a valid number.")

def delete_tasks(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter index to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid index")
    except ValueError:
        print("Please enter a valid number.")

def show_completion_percentage(tasks):
    if not tasks:
        print("No tasks to evaluate.")
        return
    completed = sum(1 for task in tasks if task["completed"])
    total = len(tasks)
    percent = (completed / total) * 100
    print(f"Completion: {completed}/{total} tasks done ({percent:.1f}%)")

def main():
    tasks = load_tasks()
    while True:
        print("\nTO DO LIST")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete a Task")
        print("4. Delete a Task")
        print("5. Show Completion Percentage")
        print("6. Exit")

        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                add_tasks(tasks)
            elif choice == 2:
                list_tasks(tasks)
            elif choice == 3:
                complete_tasks(tasks)
            elif choice == 4:
                delete_tasks(tasks)
            elif choice == 5:
                show_completion_percentage(tasks)
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()