from runtime.worker_executor import WorkerExecutor

class Department:
    def __init__(self, name, manager=None):
        self.name = name
        self.manager = manager
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def assign_task(self, task):
        print(f"\n[{self.name}] recebendo tarefa:")
        print(f"  Tarefa: {task.title}")
        for worker in self.workers:
            print(f"  -> {worker.name} ({worker.persona}) executando")
            WorkerExecutor.execute(worker, task)