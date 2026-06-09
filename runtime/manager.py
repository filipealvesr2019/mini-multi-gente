# runtime/manager.py
from .worker import Worker
from .router import Router

class Manager:
    def __init__(self):
        self.router = Router()
        self.workers = [
            Worker("texto"),
            Worker("codigo"),
            Worker("matematica"),
            Worker("planejamento")
        ]

    def divide_task(self, tarefa):
        # Divide tarefa em partes específicas
        return [
            {"categoria": "texto", "conteudo": f"Gerar interface e descrição: {tarefa}"},
            {"categoria": "codigo", "conteudo": f"Gerar código base: {tarefa}"},
            {"categoria": "matematica", "conteudo": f"Gerar cálculos: {tarefa}"},
            {"categoria": "planejamento", "conteudo": f"Planejar etapas e componentes: {tarefa}"}
        ]

    def execute_subtasks(self, subtarefas):
        resultados = []
        for sub in subtarefas:
            worker = self.router.choose_worker(self.workers, sub["categoria"])
            resultado = worker.execute(sub["conteudo"])
            resultados.append(resultado)
            # Mostrar status para feedback humano
            self.report_status()
        return resultados

    def report_status(self):
        print("\nStatus dos Workers:")
        for w in self.workers:
            print(f"{w.especialidade}: {w.status} - {w.current_task}")