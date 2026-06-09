import os

class WorkspaceManager:
    base_dir = "workspace"

    @staticmethod
    def save_project_file(project_name, relative_path, content):
        """
        Salva o arquivo no projeto final.
        Exemplo: workspace/projects/IDE_Multi_Agente/frontend/App.jsx
        """
        project_file = os.path.join(
            WorkspaceManager.base_dir,
            "projects",
            project_name,
            relative_path
        )
        os.makedirs(os.path.dirname(project_file), exist_ok=True)
        with open(project_file, "w", encoding="utf-8") as f:
            f.write(content)
        return project_file

    @staticmethod
    def save_worker_log(worker_name, subtask_name, content):
        """
        Salva o arquivo no log de cada worker.
        Exemplo: workspace/logs/João/Criar_App.jsx.txt
        """
        log_file = os.path.join(
            WorkspaceManager.base_dir,
            "logs",
            worker_name,
            f"{subtask_name.replace(' ', '_')}.txt"
        )
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(content)
        return log_file

    @staticmethod
    def list_workspace():
        """
        Lista todos os arquivos em workspace
        """
        all_files = []
        for root, dirs, files in os.walk(WorkspaceManager.base_dir):
            for file in files:
                all_files.append(os.path.join(root, file))
        return all_files