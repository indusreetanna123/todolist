# ==============================
# To-Do List Application
# CodSoft Python Internship - Task 1
# ==============================

tasks = []

def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        if len(tasks) == 0:
            print("\nNo tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "✓" if task["completed"] else "✗"
                print(f"{i}. [{status}] {task['title']}")

    elif choice == "2":
        title = input("Enter task: ")
        tasks.append({"title": title, "completed": False})
        print("Task added successfully!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to update.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "✓" if task["completed"] else "✗"
                print(f"{i}. [{status}] {task['title']}")

            try:
                task_no = int(input("Enter task number to mark as completed: "))
                if 1 <= task_no <= len(tasks):
                    tasks[task_no - 1]["completed"] = True
                    print("Task marked as completed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "✓" if task["completed"] else "✗"
                print(f"{i}. [{status}] {task['title']}")

            try:
                task_no = int(input("Enter task number to delete: "))
                if 1 <= task_no <= len(tasks):
                    removed = tasks.pop(task_no - 1)
                    print(f"'{removed['title']}' deleted successfully.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("\nThank you for using the To-Do List Application!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")