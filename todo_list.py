class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        tasks = []
        for idx, task in enumerate(self.tasks, start=1):
            status = "Done" if task["completed"] else "Pending"
            tasks.append({"id": idx, "status": status, "task": task["task"]})
        return tasks

    def mark_completed(self, task_idx):
        if 1 <= task_idx <= len(self.tasks):
            self.tasks[task_idx - 1]["completed"] = True
        else:
            print("Invalid task number.")
