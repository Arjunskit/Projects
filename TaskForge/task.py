import uuid


class Task:
    def __init__(self, title, priority, due_date, status='PENDING', task_id=None):
        self.task_id = task_id or str(uuid.uuid4())
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id[:8]} | {self.title:<20} | {self.priority:<6} | {self.due_date} | {self.status}"

    def to_dict(self):
        return {
            'task_id': self.task_id,
            'title': self.title,
            'priority': self.priority,
            'due_date': self.due_date,
            'status': self.status,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            task_id=data['task_id'],
            title=data['title'],
            priority=data['priority'],
            due_date=data['due_date'],
            status=data['status']
        )



