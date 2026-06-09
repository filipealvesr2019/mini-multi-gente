import random
import time
import threading


class Worker:
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade
        self.status = "aguardando"
        self.current_task = None
        self.progress = 0
        self.dependency_done = True
        self.paused = False
        self.lock = threading.Lock()

    def execute(self, tarefa):
        # espera dependência
        if not self.dependency_done:
            self.status = "aguardando dependência"
            while not self.dependency_done:
                time.sleep(0.2)

        self.status = "executando"
        self.current_task = tarefa

        for i in range(10):
            time.sleep(random.uniform(0.2, 0.5))

            # espera se pausado
            while self.paused:
                time.sleep(0.1)

            with self.lock:
                self.progress = (i + 1) * 10

        self.status = "concluído"
        self.progress = 100
        self.current_task = None
        return f"[{self.nome}] Processado: {tarefa}"