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
        print(f"[{self.name}] planejando tarefa")

        subtasks = []

        # Frontend
        if self.name == "Frontend":

            subtasks.append(
                ("Criar App.jsx", "react")
            )

            subtasks.append(
                ("Criar style.css", "css")
            )

        # AI
        elif self.name == "AI":

            subtasks.append(
                ("Criar prompts", "prompts")
            )

        # Fallback para departamentos sem regras
        else:

            subtasks.append(
                (task.title, None)
            )

        threads = []

        for subtask_title, required_skill in subtasks:

            selected_worker = None

            for worker in self.workers:

                if (
                    required_skill is None
                    or required_skill in worker.skills
                ):
                    selected_worker = worker
                    break

            if selected_worker:

                t = threading.Thread(
                    target=WorkerExecutor.execute,
                    args=(
                        selected_worker,
                        subtask_title
                    )
                )

                t.start()

                threads.append(t)

            else:

                print(
                    f"Nenhum worker encontrado para skill: "
                    f"{required_skill}"
                )

        for t in threads:
            t.join()