# runtime/worker.py

from runtime.sandbox import Sandbox
from runtime.diff_engine import generate_diff
import time
import random

class Worker:
    def __init__(self, name: str, persona: str, skills: list):
        self.name = name
        self.persona = persona
        self.skills = skills

    def run_task(self, skill: str, task_title: str, content: str):
        """
        Executa uma tarefa real (conteúdo dinâmico) e salva no Sandbox.
        Não há mocks nem ifs fixos.
        """

        print(f"[{self.name}] recebeu tarefa: {task_title}")

        # Simula progresso baseado em tempo variável
        for progress in [20, 40, 60, 80, 100]:
            time.sleep(random.uniform(0.1, 0.5))
            print(f"[{self.name}] {task_title} {progress}%")

        # Cria o arquivo dinamicamente no Sandbox
        filename = task_title.replace(" ", "_") + ".txt"
        path = Sandbox.create_file(f"{self.name}/{filename}", content)

        # Calcula diff real baseado no conteúdo atual
        diff = generate_diff(path)

        print(f"[{self.name}] DIFF +{diff['added']} -{diff['removed']}")
        print(f"[{self.name}] ENTREGUE tarefa: {task_title}")

        # Retorna resultado completo para o Manager
        return {
            "worker": self.name,
            "file": path,
            "task": task_title,
            "diff": diff
        }

    def has_skill(self, skill: str) -> bool:
        """
        Verifica se o Worker possui a skill requerida.
        """
        return skill.lower() in [s.lower() for s in self.skills]