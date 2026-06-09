from concurrent.futures import ThreadPoolExecutor
from runtime.worker import Worker
from runtime.router import escolher_worker_inteligente, feedback_task
from runtime.company_config import COMPANY_CONFIG

class Manager:

    def __init__(self):
        self.departments = []
        self._load_workers()

    def _load_workers(self):
        for dep in COMPANY_CONFIG["departments"]:
            workers = []
            for w in dep["workers"]:
                workers.append(Worker(w["name"], w["persona"], w["skills"]))
            self.departments.append({
                "name": dep["name"],
                "workers": workers
            })

    def execute_operations(self, operations, prompt_func):
        resultados = []

        def run(op):
            dept = next(d for d in self.departments if d["name"] == op["department"])
            worker, estado = escolher_worker_inteligente(dept["workers"], op["skill"])
            content = prompt_func(worker, op)
            return worker.run_task(op["skill"], op["task_title"], content)

        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(run, op) for op in operations]
            for f in futures:
                resultados.append(f.result())

        return resultados