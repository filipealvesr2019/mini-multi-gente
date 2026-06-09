# runtime/worker.py
import time

class Worker:
    def __init__(self, especialidade):
        self.especialidade = especialidade
        self.status = "aguardando"
        self.current_task = None

    def execute(self, tarefa):
        self.status = "executando"
        self.current_task = tarefa
        time.sleep(0.5)  # simula processamento
        self.status = "concluído"
        self.current_task = None
        return f"[{self.especialidade.upper()}] Processado: {tarefa}"