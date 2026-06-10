# runtime/department.py

import threading
from runtime.worker_executor import WorkerExecutor
from runtime.router import feedback_task, escolher_worker_inteligente


class Department:
    def __init__(self, name, manager=None):
        self.name = name
        self.manager = manager
        self.workers = []

    def add_worker(self, worker):
        """Adiciona um worker ao departamento"""
        self.workers.append(worker)

    def assign_operations(self, operations):
        """
        Recebe operações planejadas pelo Planner e distribui para workers
        Cada operação deve ter o formato:
        {
            "task": "Descrição da operação",
            "required_skills": ["skill1", "skill2"]
        }
        """
        print(f"\n[{self.name}] distribuindo operações")

        threads = []

        for op in operations:
            worker = self.find_best_worker(op)

            if not worker:
                print(f"[{self.name}] nenhum worker disponível para operação '{op.get('task')}' com skills {op.get('required_skills')}")
                continue

            # Cria thread para execução
            t = threading.Thread(
                target=WorkerExecutor.execute,
                args=(worker, op)
            )
            t.start()
            threads.append(t)

            # Feedback para router aprender
            feedback_task(worker.id, op, success=True)

        # Espera todas as threads terminarem
        for t in threads:
            t.join()

        print(f"[{self.name}] operações concluídas")

    def find_best_worker(self, operation):
        """
        Seleciona o melhor worker do departamento baseado nas skills requeridas
        """
        required_skills = operation.get("required_skills", [])

        candidates = []

        for worker in self.workers:
            # Conta quantas skills do worker batem com as skills requeridas
            score = len(set(worker.skills) & set(required_skills))
            if score > 0:
                candidates.append((worker, score))

        if not candidates:
            return None

        # Ordena pelo score mais alto
        candidates.sort(key=lambda x: x[1], reverse=True)

        # Pode usar escolher_worker_inteligente para roteamento esparso, se quiser
        top_worker, _ = escolher_worker_inteligente([c[0] for c in candidates], required_skills[0] if required_skills else None)

        return top_worker