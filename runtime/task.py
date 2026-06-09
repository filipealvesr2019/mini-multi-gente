class Task:

    def __init__(self, title):
        self.title = title
        self.progress = 0
        self.status = "pending"

    def update(self, progress):
        self.progress = progress

        if progress >= 100:
            self.status = "completed"
        else:
            self.status = "running"