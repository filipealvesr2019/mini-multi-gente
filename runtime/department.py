import threading
from runtime.worker_executor import WorkerExecutor

class Department:

    def __init__(self, name, manager=None):
        self.name = name
        self.manager = manager
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def assign_task(self, task):

        print()
        print(f"[{self.name}] recebendo tarefa:")
        print(f"  Tarefa: {task.title}")

        threads = []

        for worker in self.workers:

            t = threading.Thread(
                target=WorkerExecutor.execute,
                args=(worker, task)
            )

            t.start()

            threads.append(t)

        for t in threads:
            t.join()