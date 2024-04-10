class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        if self.tasks:
            print("Todo List:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{idx}. [{status}] {task['task']}")
        else:
            print("Todo List is empty.")

    def mark_completed(self, task_idx):
        if 1 <= task_idx <= len(self.tasks):
            self.tasks[task_idx - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_idx = int(input("Enter task number to mark as completed: "))
            todo_list.mark_completed(task_idx)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
