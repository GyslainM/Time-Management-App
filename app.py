from tasks.task import TaskManager 

def main():
    print("Welcome to the Time Management App")
    task_manager = TaskManager()

    while True:
        print("\\Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Tasks")
        print("4. Delete Tasks")
        print("5. Mark Task as Completed")
        print("6. Exit")
        
        choice = input("Choose an option: ") 

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            deadline = input("Enter task deadline (YYYY-MM-DD): ")
            task_manager.add_task(title, description, deadline)

        elif choice == '2':
            task_manager.view_tasks()

        elif choice == '3':
            task_manager.view_tasks()
            task_index = int(input("Enter the task number to edit: "))
            title = input("Enter new task title (or press Enter to keep current): ")
            description = input("Enter new task description (or press Enter to keep current): ")
            deadline = input("Enter new task deadline (or press Enter to keep current): ")
            task_manager.edit_task(task_index,title, description, deadline)

        elif choice == '4':
            task_manager.view_tasks()
            try:
                task_index = int(input("Enter the task number to delete: "))
                task_manager.delete_task(task_index)
            except ValueError:
                print("Invalid input! Please enter valid task number.")

        elif choice == '5':
            task_manager.view_tasks()
            task_index = int(input("Enter the task number to mark complete: "))
            task_manager.mark_task_complete(task_index)

        elif choice == '6':
            print("Exiting the program. !")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
