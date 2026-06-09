# runtime/worker.py
class Worker:
    def __init__(self, especialidade):
        self.especialidade = especialidade

    def execute(self, tarefa):
        # Aqui você pode chamar o modelo Qwen 1.5B
        # Por enquanto, apenas simula a resposta
        return f"[{self.especialidade.upper()}] Processado: {tarefa}"