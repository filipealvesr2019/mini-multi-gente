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
        Recebe operações e distribui para workers.
        Cada operação deve ter o formato:
        {
            "task_title": "Descrição da operação",
            "skill": "skill principal da operação",
            "metadata": {...} # Qualquer dado extra
        }
        """
        print(f"\n[{self.name}] distribuindo operações")

        threads = []

        for op in operations:
            worker = self.find_best_worker(op)

            if not worker:
                print(f"[{self.name}] nenhum worker disponível para operação '{op.get('task_title')}' com skill '{op.get('skill')}'")
                continue

            # Cria thread para execução da operação
            t = threading.Thread(
                target=WorkerExecutor.execute,
                args=(worker, op)
            )
            t.start()
            threads.append(t)

            # Feedback para roteamento inteligente
            feedback_task(worker.name, op, success=True)

        # Aguarda todas threads terminarem
        for t in threads:
            t.join()

        print(f"[{self.name}] todas operações concluídas")

    def find_best_worker(self, operation):
        """
        Seleciona o melhor worker baseado na skill necessária
        """
        required_skill = operation.get("skill")
        if not required_skill:
            return None

        candidates = []

        for worker in self.workers:
            score = 1 if required_skill in worker.skills else 0
            if score > 0:
                candidates.append((worker, score))

        if not candidates:
            return None

        # Ordena candidatos pelo score mais alto
        candidates.sort(key=lambda x: x[1], reverse=True)

        # Roteamento inteligente (pode usar algoritmo avançado)
        top_worker, _ = escolher_worker_inteligente([c[0] for c in candidates], required_skill)
        return top_worker