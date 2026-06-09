import time
import random
from runtime.workspace_manager import WorkspaceManager

class WorkerExecutor:

    @staticmethod
    def execute(worker, subtask, project_name="IDE_Multi_Agente"):

        start_time = time.time()
        print(f"\n[{worker.name}] recebeu: {subtask}")

        # Simulação de progresso
        for p in [20, 40, 60, 80, 100]:
            time.sleep(random.uniform(0.3, 1.0))
            print(f"[{worker.name}] {subtask} {p}%")

        # Conteúdo simulado do arquivo
        content = f"{worker.name} executou: {subtask}"

        # Salva no projeto final
        project_path = subtask_to_path(subtask)
        WorkspaceManager.save_project_file(project_name, project_path, content)

        # Salva no log do worker
        WorkspaceManager.save_worker_log(worker.name, subtask, content)

        elapsed = time.time() - start_time
        print(f"[{worker.name}] ENTREGOU {subtask} em {elapsed:.2f}s -> {project_path}")


def subtask_to_path(subtask):
    """
    Define onde cada subtask deve ir dentro do projeto final
    """
    if subtask == "Criar App.jsx":
        return "frontend/App.jsx"
    elif subtask == "Criar style.css":
        return "frontend/style.css"
    elif subtask == "Criar prompts":
        return "prompts/system_prompt.md"
    else:
        return f"misc/{subtask.replace(' ', '_')}.txt"