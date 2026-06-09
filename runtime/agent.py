# runtime/agent.py

class Agent:
    def __init__(
        self,
        name,
        persona,
        skills,
        authority,
        tipo,
        bus,
        likes=None,
        dislikes=None,
        goals=None,
        rules=None
    ):
        self.name = name
        self.persona = persona
        self.skills = skills
        self.authority = authority
        self.tipo = tipo
        self.bus = bus

        self.likes = likes or []
        self.dislikes = dislikes or []
        self.goals = goals or []
        self.rules = rules or []

        self.status = "idle"
        self.progress = 0
        self.current_task = None
        self.paused = False
        self.memory = []

    def log(self, msg):
        self.memory.append(msg)

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False