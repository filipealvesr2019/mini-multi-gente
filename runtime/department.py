import threading
from runtime.worker_executor import WorkerExecutor
from runtime.router import escolher_worker_inteligente, feedback_task


class Department:

    def __init__(self, name, manager=None):
        self.name = name
        self.manager = manager
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def assign_operations(self, operations):
        """
        Recebe operações planejadas pelo Planner e distribui para workers
        """
        print(f"\n[{self.name}] distribuindo operações")

        threads = []

        for op in operations:
            skill = op.get("skill")
            eligible_workers = [w for w in self.workers if skill in w.skills]

            if not eligible_workers:
                print(f"[{self.name}] nenhum worker para skill {skill}")
                continue

            worker, estado = escolher_worker_inteligente(eligible_workers, skill)

            t = threading.Thread(
                target=WorkerExecutor.execute,
                args=(worker, op)
            )
            t.start()
            threads.append(t)

            feedback_task(skill)

        for t in threads:
            t.join()

        print(f"[{self.name}] operações concluídas")