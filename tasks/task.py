from datetime import datetime  # Importing datetime module

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.created_at = datetime.now()  # Using datetime.now() to get the current time

    def __str__(self):
        return f"Task: {self.title}\nDescription: {self.description}\nDeadline: {self.deadline}\nCreated At: {self.created_at}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, deadline):
        task = Task(title, description, deadline)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)
