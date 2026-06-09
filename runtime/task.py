class Task:
    def __init__(self, title):
        self.title = title
        self.status = "pending"

    def __str__(self):
        return f"{self.title} [{self.status}]"