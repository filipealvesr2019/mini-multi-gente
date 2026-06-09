import time
import random
from runtime.sandbox import Sandbox

class WorkerExecutor:

    @staticmethod
    def execute(worker, subtask):
        start_time = time.time()
        print()
        print(f"[{worker.name}] recebeu: {subtask}")

        # Simula progresso
        for p in [20, 40, 60, 80, 100]:
            time.sleep(random.uniform(0.3, 1.0))
            print(f"[{worker.name}] {subtask} {p}%")

        # Salva na sandbox
        filename = subtask.replace(" ", "_") + ".txt"
        Sandbox.create_file(f"{worker.name}/{filename}", f"{subtask} realizado por {worker.name}")

        end_time = time.time()
        elapsed = end_time - start_time
        print(f"[{worker.name}] ENTREGOU {subtask} em {elapsed:.2f}s -> {Sandbox.BASE_DIR}\\{worker.name}\\{filename}")