from concurrent.futures import ThreadPoolExecutor
from .worker import Worker
from .router import escolher_worker_inteligente, feedback_task

class Manager:
    def __init__(self):
        self.workers = [
            Worker("Ana", skills=["texto"]),
            Worker("João", skills=["codigo"]),
            Worker("Pedro", skills=["matematica"]),
            Worker("Marina", skills=["planejamento"])
        ]

    def divide_task(self, task_name):
        return [
            {"skill": "planejamento", "task": f"Planejar projeto: {task_name}"},
            {"skill": "codigo", "task": f"Criar código React: {task_name}"},
            {"skill": "texto", "task": f"Documentar interface: {task_name}"},
            {"skill": "matematica", "task": f"Implementar cálculos: {task_name}"}
        ]

    def execute_subtasks(self, subtasks):
        resultados = []

        def executar(sub):
            worker, estado = escolher_worker_inteligente(self.workers, sub["skill"])
            res = worker.run_task(sub["skill"], sub["task"])
            feedback_task(sub["skill"])
            return res

        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(executar, s) for s in subtasks]
            for f in futures:
                resultados.append(f.result())

        return resultados