from datetime import datetime  # Importing datetime module

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.created_at = datetime.now()  # Using datetime.now() to get the current time
        self.completed = False # Initially, the task is not complete

    def __str__(self):
        return f"Task: {self.title}\nDescription: {self.description}\nDeadline: {self.deadline}\nCreated At: {self.created_at}\nCompleted: {'yes' if self.completed else 'No'}"

    def edit_task(self, title=None, description=None, deadline=None):
       
        """Method to edit task details"""
        
        if title:
            self.title = title
        if description:
            self.description = description
        if deadline:
            self.deadline = deadline
        print(f"Task '{self.title}' has been updated!")

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
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def edit_task(self, task_index, title=None, description=None, deadline=None):
        """Allow editing an existing task by index"""
        if task_index < 1 or task_index > len(self.tasks):
            print("Invalid task number!")
        else:
            task = self.tasks[task_index - 1]
            task.edit_task(title, description, deadline)

    def delete_task(self, task_index):
        """Delete a task by index"""
        if task_index < 1 or task_index > len(self.tasks):
            print("Invalid task number!")
        else:
            task = self.tasks.pop(task_index - 1)
            print(f"Task '{task.title}' has been deleted!")
