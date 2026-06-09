from concurrent.futures import ThreadPoolExecutor
import threading
import time

from .worker import Worker
from .router import Router


class Manager:

    def __init__(self):
        self.router = Router()
        self.workers = [
            Worker("Ana", "texto"),
            Worker("João", "codigo"),
            Worker("Pedro", "matematica"),
            Worker("Marina", "planejamento")
        ]

    def divide_task(self, tarefa):
        return [
            {"categoria": "planejamento", "conteudo": f"Planejar projeto: {tarefa}"},
            {"categoria": "codigo", "conteudo": f"Criar código React: {tarefa}"},
            {"categoria": "texto", "conteudo": f"Documentar interface: {tarefa}"},
            {"categoria": "matematica", "conteudo": f"Implementar cálculos: {tarefa}"}
        ]

    def dashboard_loop(self):
        while True:
            print("\n" * 2)
            print("=" * 50)
            print("CEO DASHBOARD")
            print("=" * 50)
            concluidos = 0
            for w in self.workers:
                print(f"{w.nome:<12}{w.especialidade:<15}{w.status:<20}{w.progress}%")
                if w.status == "concluído":
                    concluidos += 1
            if concluidos == len(self.workers):
                break
            time.sleep(1)

    def execute_subtasks(self, subtasks):
        # Configurar dependências simples
        dep_map = {
            "planejamento": [],
            "codigo": ["planejamento"],
            "texto": ["codigo"],
            "matematica": ["texto"]
        }
        name_map = {w.especialidade: w for w in self.workers}
        for key, deps in dep_map.items():
            for dep in deps:
                if dep in name_map:
                    name_map[key].dependency_done = False

        dashboard = threading.Thread(target=self.dashboard_loop)
        dashboard.start()

        def executar(sub):
            worker = self.router.choose_worker(self.workers, sub["categoria"])
            # marcar dependências como feitas antes de começar
            worker.dependency_done = all(
                name_map[d].status == "concluído" for d in dep_map[sub["categoria"]]
            )
            res = worker.execute(sub["conteudo"])
            # liberar dependentes
            for k, deps in dep_map.items():
                if sub["categoria"] in deps:
                    name_map[k].dependency_done = True
            return res

        resultados = []
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(executar, s) for s in subtasks]
            for f in futures:
                resultados.append(f.result())

        dashboard.join()
        return resultados