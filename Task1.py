import json
from datetime import datetime


class Task:
    def __init__(self, title, priority, due_date):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True


class TaskManager:
    def __init__(self, tasks_file):
        self.tasks_file = tasks_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.tasks_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.tasks_file, 'w') as file:
            json.dump(self.tasks, file, default=lambda o: o.__dict__, indent=4)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_title):
        self.tasks = [task for task in self.tasks if task.title != task_title]
        self.save_tasks()

    def mark_task_completed(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.mark_as_completed()
        self.save_tasks()

    def list_tasks(self):
        for task in self.tasks:
            completed = 'Completed' if task.completed else 'Not Completed'
            print(f"{task.title} - Priority: {task.priority}, Due: {task.due_date}, Status: {completed}")


if __name__ == "__main__":
    task_manager = TaskManager('tasks.json')

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task Completed")
        print("4. List Tasks")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            priority = input("Enter task priority (high, medium, low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task_manager.add_task(Task(title, priority, due_date))
        elif choice == '2':
            title = input("Enter task title to remove: ")
            task_manager.remove_task(title)
        elif choice == '3':
            title = input("Enter task title to mark as completed: ")
            task_manager.mark_task_completed(title)
        elif choice == '4':
            task_manager.list_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
