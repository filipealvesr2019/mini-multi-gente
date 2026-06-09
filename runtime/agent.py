class Agent:
    def __init__(self, name, role, persona, skills=None, authority=0):
        self.name = name
        self.role = role
        self.persona = persona
        self.skills = skills or []
        self.authority = authority

    def __str__(self):
        return f"{self.role}: {self.name} ({self.persona}) skills={self.skills}"