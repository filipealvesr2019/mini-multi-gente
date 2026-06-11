# runtime/agent.py
import os

class Agent:
    def __init__(self, name, skills=None):
        self.name = name
        self.skills = skills or []

    def execute(self, project_path):
        """
        Lógica do agente. 
        Aqui ele lista os arquivos com caminho relativo,
        mantendo a hierarquia.
        """
        print(f"[{self.name}] analisando projeto: {project_path}")

        for root, dirs, files in os.walk(project_path):
            for f in files:
                filepath = os.path.join(root, f)
                # caminho relativo em relação à raiz do projeto
                relative_path = os.path.relpath(filepath, project_path)
                print(f"[{self.name}] arquivo encontrado: {relative_path}")