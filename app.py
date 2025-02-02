from tasks.task import TaskManager 

def main():
    print("Welcome to the Time Management App")
    task_manager = TaskManager()

    while True:
        print("\\Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        
        choice = input("Choose an option: ") 

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            deadline = input("Enter task deadline (YYYY-MM-DD): ")
            task_manager.add_task(title, description, deadline)

        elif choice == '2':
            task_manager.view_tasks()

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
