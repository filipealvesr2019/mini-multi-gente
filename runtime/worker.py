from runtime.sandbox import Sandbox
from runtime.diff_engine import generate_diff
import time
import random

class Worker:

    def __init__(self, name, persona, skills):
        self.name = name
        self.persona = persona
        self.skills = skills

    def run_task(self, skill, task_title, content):
        print(f"[{self.name}] recebeu: {task_title}")

        # simula execução em etapas
        for p in [20, 40, 60, 80, 100]:
            time.sleep(random.uniform(0.2, 0.6))
            print(f"[{self.name}] {task_title} {p}%")

        filename = task_title.replace(" ", "_") + ".txt"
        path = Sandbox.save_file(self.name, filename, content)

        # diff simples
        diff = generate_diff(path)
        print(f"[{self.name}] DIFF +{diff['added']} -{diff['removed']}")
        print(f"[{self.name}] ENTREGUE {task_title} em {round(random.uniform(1,3),2)}s")

        return {"worker": self.name, "file": path, "task": task_title, "diff": diff}