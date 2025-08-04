from manager import TaskManager


def main():
    manager = TaskManager()
    manager.load_from_file()

    while True:
        print("\n TaskForge Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Complete")
        print("5. Delete Task")
        print("6. Save Tasks")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == '1':
            title = input("Title: ").strip()
            priority = input("Priority (Low/Medium/High): ").strip()
            due_date = input("Due Date (DD-MM-YYYY): ")
            manager.add_task(title, priority, due_date)
        elif choice == '2':
            print("View Options: All, Pending, Completed, Today, Week")
            filter_by = input("Filter by: ").strip()
            manager.view_tasks(filter_by if filter_by != 'All' else None)
        elif choice == '3':
            task_id = input("Enter Task Id to update: ").strip()
            manager.update_task(task_id)
        elif choice == '4':
            task_id = input("Enter Task Id to Mark as Complete: ").strip()
            manager.mark_complete(task_id)
        elif choice == '5':
            task_id = input("Enter Task Id to delete: ").strip()
            manager.delete_task(task_id)
        elif choice == '6':
            manager.save_to_file()
        elif choice == '7':
            manager.save_to_file()
            print("Good Bye")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()