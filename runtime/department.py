import threading
from pathlib import Path
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
        """
        Divide uma task em subtasks por skill do departamento
        e envia para execução paralela pelos workers.
        """
        print()
        print(f"[{self.name}] planejando tarefa")

        subtasks = []

        # Definição de subtasks por departamento
        if self.name == "Frontend":
            subtasks.append(("Criar App.jsx", "react"))
            subtasks.append(("Criar style.css", "css"))
        elif self.name == "AI":
            subtasks.append(("Criar prompts", "prompts"))
        else:
            # Fallback para departamentos sem regras
            subtasks.append((task.title, None))

        threads = []

        for subtask_title, required_skill in subtasks:

            selected_worker = None
            estado = None

            # Escolha inteligente usando router
            if required_skill:
                # Filtra apenas workers que têm a skill
                eligible_workers = [w for w in self.workers if required_skill in w.skills]
                if eligible_workers:
                    selected_worker, estado = escolher_worker_inteligente(
                        eligible_workers, required_skill
                    )
                else:
                    print(f"Nenhum worker encontrado para skill: {required_skill}")
                    continue
            else:
                # Se não há skill, pega o primeiro worker disponível
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

                # Feedback para router aprender
                if required_skill:
                    feedback_task(required_skill)

        # Espera todas as threads terminarem
        for t in threads:
            t.join()