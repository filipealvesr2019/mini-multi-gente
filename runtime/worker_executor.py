# runtime/worker_executor.py

import time
import random

from runtime.file_system import FileSystem
from runtime.diff_engine import DiffEngine
from runtime.change_log import ChangeLog


class WorkerExecutor:

    @staticmethod
    def execute(worker, subtask):

        start_time = time.time()

        print()
        print(f"[{worker.name}] recebeu: {subtask}")

        for p in [20, 40, 60, 80, 100]:

            time.sleep(random.uniform(0.3, 0.8))

            print(
                f"[{worker.name}] "
                f"{subtask} "
                f"{p}%"
            )

        # -----------------------------
        # Decide arquivo alvo
        # -----------------------------

        if "App.jsx" in subtask:

            path = "frontend/App.jsx"

            new_content = """
export default function App() {
    return (
        <div>
            <h1>Projeto Multi Agente</h1>
        </div>
    );
}
"""

        elif "style.css" in subtask:

            path = "frontend/style.css"

            new_content = """
body {
    font-family: Arial;
}

h1 {
    color: blue;
}
"""

        elif "prompts" in subtask:

            path = "ai/prompts.md"

            new_content = """
# Prompt Base

Você é um assistente especializado.
"""

        else:

            safe_name = (
                subtask
                .replace(" ", "_")
                .replace("/", "_")
                .replace("\\", "_")
            )

            path = f"misc/{safe_name}.txt"

            new_content = f"Tarefa executada: {subtask}"

        # -----------------------------
        # Lê conteúdo antigo
        # -----------------------------

        old_content = FileSystem.read_file(path)

        if old_content is None:
            old_content = ""

        # -----------------------------
        # Cria ou edita
        # -----------------------------

        if old_content == "":

            FileSystem.create_file(
                path,
                new_content
            )

            action = "CRIADO"

        else:

            FileSystem.edit_file(
                path,
                new_content
            )

            action = "EDITADO"

        # -----------------------------
        # Diff
        # -----------------------------

        diff = DiffEngine.compare(
            old_content,
            new_content
        )

        added, removed = DiffEngine.stats(
            old_content,
            new_content
        )

        ChangeLog.add(
            worker.name,
            path,
            added,
            removed
        )

        # -----------------------------
        # Relatório
        # -----------------------------

        elapsed = (
            time.time()
            - start_time
        )

        print()
        print(
            f"[{worker.name}] "
            f"{action} "
            f"{path}"
        )

        print(
            f"[{worker.name}] "
            f"DIFF +{added} -{removed}"
        )

        if diff.strip():

            print("\n--- DIFF ---")
            print(diff)
            print("------------\n")

        print(
            f"[{worker.name}] "
            f"ENTREGOU "
            f"{subtask} "
            f"em {elapsed:.2f}s"
        )