class SubTask:

    def __init__(self, title, skill):

        self.title = title
        self.skill = skill
        self.status = "pending"

    def __str__(self):
        return self.title