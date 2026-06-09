import time
import random
from pathlib import Path

class WorkerExecutor:

    @staticmethod
    def execute(worker, subtask):
        start_time = time.time()
        print(f"\n[{worker.name}] recebeu: {subtask}")

        # Definir pasta do workspace
        workspace = Path("workspace")
        workspace.mkdir(exist_ok=True)

        # Criar pastas por departamento ou worker (opcional)
        worker_dir = workspace / worker.name
        worker_dir.mkdir(exist_ok=True)

        # Nome do arquivo baseado na subtask
        filename = worker_dir / f"{subtask.replace(' ', '_')}.txt"

        # Simular progresso e criar conteúdo inicial
        content = f"Executando subtask: {subtask}\nResponsável: {worker.name}\n\n"
        for p in [20, 40, 60, 80, 100]:
            time.sleep(random.uniform(0.1, 0.5))  # tempo de execução
            content += f"Progresso: {p}%\n"
            print(f"[{worker.name}] {subtask} {p}%")

        # Escrever arquivo
        filename.write_text(content, encoding="utf-8")

        end_time = time.time()
        elapsed = end_time - start_time
        print(f"[{worker.name}] ENTREGOU {subtask} em {elapsed:.2f}s -> {filename}")