#Python Project: "Personal To-Do List Application"

import json
import os

# file to save tasks
FILENAME = "tasks.json"

# Task class to hold task details
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

# save tasks to file
def save_tasks(task_list):
    with open(FILENAME, "w") as f:
        json.dump([t.__dict__ for t in task_list], f, indent=4)

# load tasks from file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            data = json.load(f)
            return [Task(**t) for t in data]
    else:
        return []

# add new task
def add_task(task_list):
    title = input("Enter task title: ")
    desc = input("Enter task description: ")
    cat = input("Enter category (Work, Personal, Urgent, etc): ")
    task = Task(title, desc, cat)
    task_list.append(task)
    save_tasks(task_list)
    print("Task added!\n")

# view all tasks
def view_tasks(task_list):
    if not task_list:
        print("No tasks available.\n")
        return
    print("\n=== Your Tasks ===")
    for i, t in enumerate(task_list, 1):
        status = "Done" if t.completed else "Pending"
        print(f"{i}. {t.title} ({t.category}) - {status}")
        print("   Description:", t.description)
    print()

# mark a task as completed
def complete_task(task_list):
    view_tasks(task_list)
    try:
        choice = int(input("Enter task number to mark complete: "))
        if 1 <= choice <= len(task_list):
            task_list[choice - 1].mark_completed()
            save_tasks(task_list)
            print("Task marked as completed!\n")
        else:
            print("Invalid task number.\n")
    except:
        print("Please enter a valid number.\n")

# delete a task
def delete_task(task_list):
    view_tasks(task_list)
    try:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(task_list):
            removed = task_list.pop(choice - 1)
            save_tasks(task_list)
            print(f"Task '{removed.title}' deleted!\n")
        else:
            print("Invalid task number.\n")
    except:
        print("Please enter a valid number.\n")

# main menu
def main():
    tasks = load_tasks()
    while True:
        print("=== Personal To-Do List ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
    
#Submitted By - Tejasvi Munjal
    #Mobile No. - +91 7982602495
    #Email Address - tejasvimunjal17@gmail.com
                                                #Submitted To - Vault of Code
