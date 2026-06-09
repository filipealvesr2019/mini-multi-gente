from .worker import Worker
from .router import Router

class Manager:
    def __init__(self):
        self.router = Router()
        self.workers = [Worker("texto"), Worker("codigo"), Worker("matematica"), Worker("planejamento")]

    def divide_task(self, tarefa):
        # Divisão simples por categoria
        return [
            {"categoria": "texto", "conteudo": tarefa},
            {"categoria": "codigo", "conteudo": tarefa},
            {"categoria": "matematica", "conteudo": tarefa},
            {"categoria": "planejamento", "conteudo": tarefa}
        ]

    def execute_subtasks(self, subtarefas):
        resultados = []
        for sub in subtarefas:
            worker = self.router.choose_worker(self.workers, sub["categoria"])
            resultados.append(worker.execute(sub["conteudo"]))
        return resultados