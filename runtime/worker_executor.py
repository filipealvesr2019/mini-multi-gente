import time
import random

class WorkerExecutor:

    @staticmethod
    def execute(worker, subtask):

        start_time = time.time()  # Início do timer

        print()
        print(f"[{worker.name}] recebeu: {subtask}")

        for p in [20, 40, 60, 80, 100]:
            time.sleep(random.uniform(0.3, 1.0))  # simula tempo de trabalho
            print(f"[{worker.name}] {subtask} {p}%")

        end_time = time.time()  # Fim do timer
        elapsed = end_time - start_time

        print(f"[{worker.name}] ENTREGOU {subtask} em {elapsed:.2f}s")