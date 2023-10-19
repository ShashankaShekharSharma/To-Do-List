'''
Simple To-Do List Application: Create a basic to-do list application that allows users to add, delete, and update tasks using command-line input.
'''

import csv
import os

FILE_NAME = "tasks.csv"

def create_csv_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Task', 'Deadline'])
print("Welcome to the to do list")
def save_tasks_to_csv():
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Task', 'Deadline'])
        for task in tasks:
            if 'deadline' in task:
                writer.writerow([task['name'], task['deadline']])
            else:
                writer.writerow([task, ""])
def load_tasks_from_csv():
    create_csv_file()
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row[1] != "":
                tasks.append({'name': row[0], 'deadline': row[1]})
            else:
                tasks.append(row[0])
print("Welcome to the to-do list")
tasks = []
load_tasks_from_csv()

def show_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("Tasks:")
        sorted_tasks = sorted(tasks, key=lambda x: x.get('deadline', ''))
        for i, task in enumerate(sorted_tasks, start=1):
            print(f"{i}. {task['name']}", end="")
            if 'deadline' in task:
                print(f" - Deadline: {task['deadline']}")
            else:
                print()

def add_task(task):
    has_deadline = input("Does the task have a deadline? (yes/no): ").lower()
    if has_deadline == 'yes':
        deadline = input("Enter the deadline for the task: ")
        tasks.append({'name': task, 'deadline': deadline})
    else:
        tasks.append({'name': task})
    print(f"Task '{task}' added.")

def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print(f"Task '{deleted_task}' deleted.")
    else:
        print("Invalid task index.")

def update_task(task_index):
    if 1 <= task_index <= len(tasks):
        print("1. Edit Task\n2. Edit Deadline")
        sub_choice = input("Enter your sub-choice: ")
        if sub_choice == '1':
            updated_task = input("Enter the updated task: ")
            tasks[task_index - 1]['name'] = updated_task
            print(f"Task {task_index} updated to '{updated_task}'.")
        elif sub_choice == '2':
            updated_deadline = input("Enter the updated deadline: ")
            tasks[task_index - 1]['deadline'] = updated_deadline
            print(f"Task {task_index} deadline updated to '{updated_deadline}'.")
        else:
            print("Invalid sub-choice.")
        save_tasks_to_csv()
    else:
        print("Invalid task index.")

while True:
    print("\nMain Menu\n1. Show Tasks\n2. Add Task\n3. Delete Task\n4. Update Task\n5. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter the task to add: ")
        add_task(task)
        save_tasks_to_csv()
    elif choice == '3':
        show_tasks()
        task_index = int(input("Enter the index of the task to delete: "))
        delete_task(task_index)
        save_tasks_to_csv()
    elif choice == '4':
        show_tasks()
        task_index = int(input("Enter the index of the task to update: "))
        update_task(task_index)
    elif choice == '5':
        save_tasks_to_csv()
        break
    else:
        print("Invalid choice. Please try again.")







