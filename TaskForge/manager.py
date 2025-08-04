import json
import os

from datetime import datetime, timedelta
from task import Task
from utils import validate_date, validate_priority, validate_status


class TaskManager:
    def __init__(self):
        self.task_list = []

    def add_task(self, title, priority, due_date):
        if not validate_date(due_date):
            print("❌ Invalid date format. Use DD-MM-YYYY.")
            return

        t = Task(title, priority.capitalize(), due_date)
        self.task_list.append(t)
        print("✅ Task Added.")

    def view_tasks(self, filter_by=None):
        if not self.task_list:
            print("No Tasks available.")
            return
        filtered = self.task_list
        today = datetime.today().date()

        if filter_by == 'Pending' or filter_by == 'Completed':
            filtered = [t for t in self.task_list if t.status == filter_by.upper()]
        elif filter_by == 'Today':
            filtered = [t for t in self.task_list if datetime.strptime(t.due_date, "%d-%m-%Y").date() == today]
        elif filter_by == 'Week':
            weekend = today + timedelta(days=7)
            filtered = [t for t in self.task_list if today
                        <= datetime.strptime(t.due_date, "%d-%m-%Y").date()
                        <= weekend]
        print("\n📝 Tasks:")
        print("ID       | Title                | Priority | Due Date   | Status")
        print("-" * 65)
        if len(filtered) > 0:
            for task in filtered:
                print(task)
        else:
            print("No Tasks Found")

    def update_task(self, task_id):
        for task in self.task_list:
            if task.task_id.startswith(task_id):
                new_title = input("New title (leave blank to keep current): ")
                new_priority = input("New priority (Low/Medium/High): ")
                new_due_date = input("New due date (DD-MM-YYYY): ")
                new_status = input("New Status (Pending/Completed): ")

                if new_title:
                    task.title = new_title
                if new_priority and validate_priority(new_priority.capitalize()):
                    task.priority = new_priority
                if new_due_date and validate_date(new_due_date):
                    task.due_date = new_due_date
                if new_status and validate_status(new_status.capitalize()):
                    task.status = new_status

                print("✅ Task updated.")
                return
        print("❌ Task not found.")

    def mark_complete(self, task_id):
        for t in self.task_list:
            if t.task_id.startswith(task_id):
                t.status = 'COMPLETED'
                print("Task Marked as Completed")
                return
        print("Task Not Found.")

    def delete_task(self, task_id):
        self.task_list = [t for t in self.task_list if not t.task_id.startswith(task_id)]
        print("Task Deleted.")

    def save_to_file(self, filename='tasks.json'):
        with open(filename, 'w') as f:
            json.dump([t.to_dict() for t in self.task_list], f)
        print("Tasks Saved")

    def load_from_file(self, filename="tasks.json"):
        if not os.path.exists(filename):
            self.task_list = []
            return

        with open(filename, "r") as f:
            content = f.read().strip()
            if not content:
                self.task_list = []
            else:
                self.task_list = [Task.from_dict(d) for d in json.loads(content)]
