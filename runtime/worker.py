import time
import random
import threading

class Worker:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
        self.status = "aguardando"
        self.current_task = None
        self.progress = 0
        self.lock = threading.Lock()

    def run_task(self, skill, task):
        self.status = "executando"
        self.current_task = task
        self.progress = 0
        for i in range(10):
            time.sleep(random.uniform(0.1, 0.3))
            with self.lock:
                self.progress = (i+1)*10
        self.status = "concluído"
        self.progress = 100
        self.current_task = None
        return f"[{self.name}] Executou ({skill}): {task}"