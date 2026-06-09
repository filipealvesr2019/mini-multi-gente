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

    def assign_task(self, task):

        print()
        print(f"[{self.name}] planejando tarefa")

        subtasks = []

        # Frontend
        if self.name == "Frontend":
            subtasks.append(("Criar App.jsx", "react"))
            subtasks.append(("Criar style.css", "css"))

        # AI
        elif self.name == "AI":
            subtasks.append(("Criar prompts", "prompts"))

        # Fallback para departamentos sem regras
        else:
            subtasks.append((task.title, None))

        threads = []

        for subtask_title, required_skill in subtasks:

            selected_worker = None
            estado = None

            # Escolha inteligente com router
            if required_skill:
                selected_worker, estado = escolher_worker_inteligente(
                    self.workers, required_skill
                )
            else:
                # Se não tem skill específica, pega o primeiro
                if self.workers:
                    selected_worker = self.workers[0]

            if selected_worker:

                # Executa a subtask em thread
                t = threading.Thread(
                    target=WorkerExecutor.execute,
                    args=(selected_worker, subtask_title)
                )
                t.start()
                threads.append(t)

                # Feedback para o router (aprender com a execução)
                if required_skill:
                    feedback_task(required_skill)

            else:
                print(f"Nenhum worker encontrado para skill: {required_skill}")

        # Espera todas as threads terminarem
        for t in threads:
            t.join()