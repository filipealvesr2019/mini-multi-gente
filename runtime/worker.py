# runtime/worker.py

import threading
import time
import random
from .performance_tracker import tracker

class Worker:
    def __init__(self, name, skills, forbidden=None):
        self.name = name
        self.skills = skills
        self.forbidden = forbidden or []
        self.status = "aguardando"
        self.current_task = None
        self.progress = 0
        self.dependency_done = True
        self.paused = False
        self.lock = threading.Lock()
        self.thread = None

    def run_task(self, skill, task):
        if skill in self.forbidden:
            return f"[{self.name}] Skill '{skill}' proibida!"

        if not self.dependency_done:
            self.status = "aguardando dependência"
            while not self.dependency_done:
                time.sleep(0.2)

        self.status = "executando"
        self.current_task = task
        self.progress = 0

        start_time = time.time()

        for i in range(10):
            time.sleep(random.uniform(0.2, 0.5))
            while self.paused:
                time.sleep(0.1)
            with self.lock:
                self.progress = (i + 1) * 10

        self.status = "concluído"
        self.progress = 100
        self.current_task = None

        duration = time.time() - start_time
        tracker.log_task(self.name, skill, duration)
        return f"[{self.name}] Processado ({skill}): {task} em {duration:.2f}s"

    def start_task(self, skill, task):
        self.thread = threading.Thread(target=self.run_task, args=(skill, task))
        self.thread.start()