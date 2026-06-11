# runtime/agent.py
import os
from pathlib import Path

class Agent:
    def __init__(self, name, skills=None):
        self.name = name
        self.skills = skills or []

    def execute(self, project_path):
        """
        Analisa o projeto inteiro.
        Mostra todas as pastas e arquivos com caminho completo.
        """
        print(f"[{self.name}] analisando projeto: {project_path}")

        project_data = {
            "folders": [],
            "files": []
        }

        project_path = os.path.abspath(project_path)

        for root, dirs, files in os.walk(project_path):
            # Mostra todas as pastas com caminho completo
            for d in dirs:
                folder_path = os.path.join(root, d)
                project_data["folders"].append(folder_path)
                print(f"[{self.name}] pasta encontrada: {folder_path}")

            # Mostra todos os arquivos com caminho completo
            for f in files:
                file_path = os.path.join(root, f)
                size = os.path.getsize(file_path)
                project_data["files"].append({
                    "name": f,
                    "path": file_path,  # caminho completo
                    "size": size,
                    "suffix": Path(f).suffix
                })
                print(f"[{self.name}] arquivo encontrado: {file_path}")

        print(f"[{self.name}] {len(project_data['folders'])} pastas | {len(project_data['files'])} arquivos")
        return project_data