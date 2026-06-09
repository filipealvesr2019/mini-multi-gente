# runtime/manager.py

from concurrent.futures import ThreadPoolExecutor
import threading
import time
from .worker import Worker

class Manager:
    def __init__(self):
        self.workers = [
            Worker("Ana", skills=["texto"], forbidden=["matematica"]),
            Worker("João", skills=["codigo"], forbidden=["texto"]),
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

    def choose_worker(self, skill):
        # filtra por skill e não forbidden
        candidates = [w for w in self.workers if skill in w.skills and skill not in w.forbidden]
        if not candidates:
            return None
        # escolhe o worker mais rápido naquela skill
        from .performance_tracker import tracker
        return min(candidates, key=lambda w: tracker.average_time(w.name, skill))

    def dashboard_loop(self):
        while True:
            print("\n" * 2)
            print("=" * 60)
            print("CEO DASHBOARD")
            print("=" * 60)
            concluidos = 0
            for w in self.workers:
                print(f"{w.name:<12}{','.join(w.skills):<20}{w.status:<20}{w.progress}%")
                if w.status == "concluído":
                    concluidos += 1
            if concluidos == len(self.workers):
                break
            time.sleep(1)

    def execute_subtasks(self, subtasks):
        # dependências simples
        dep_map = {
            "planejamento": [],
            "codigo": ["planejamento"],
            "texto": ["codigo"],
            "matematica": ["texto"]
        }

        name_map = {w.skills[0]: w for w in self.workers}  # simplificado

        for key, deps in dep_map.items():
            for dep in deps:
                if dep in name_map:
                    name_map[key].dependency_done = False

        dashboard = threading.Thread(target=self.dashboard_loop)
        dashboard.start()

        def executar(sub):
            worker = self.choose_worker(sub["skill"])
            if not worker:
                return f"Nenhum worker disponível para skill {sub['skill']}"
            worker.dependency_done = all(
                name_map[d].status == "concluído" for d in dep_map[sub["skill"]]
            )
            res = worker.run_task(sub["skill"], sub["task"])
            for k, deps in dep_map.items():
                if sub["skill"] in deps:
                    name_map[k].dependency_done = True
            return res

        resultados = []
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(executar, s) for s in subtasks]
            for f in futures:
                resultados.append(f.result())

        dashboard.join()
        return resultados