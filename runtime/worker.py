# runtime/worker.py
import time
from runtime.sandbox import Sandbox

class Worker:
    def __init__(self, name, skills=None):
        self.name = name
        self.skills = skills or []

    def run_task(self, skill, task_description):
        """
        Executa a tarefa: chama a LLM para gerar conteúdo,
        escreve no sandbox e retorna caminho do arquivo.
        """
        print(f"[{self.name}] recebeu: {task_description}")

        # 1. Geração de conteúdo via LLM
        content = self.generate_content(skill, task_description)

        # 2. Criação do arquivo na sandbox
        file_path = Sandbox.create_file(self.name, task_description, content)

        # 3. Calcula diff (simula linhas adicionadas/removidas)
        diff_plus, diff_minus = Sandbox.diff_file(file_path)

        print(f"[{self.name}] CRIADO {file_path}")
        print(f"[{self.name}] DIFF +{diff_plus} -{diff_minus}")

        # 4. Retorna resultado
        return f"[{self.name}] ENTREGOU {task_description} -> {file_path}"

    def generate_content(self, skill, task_description):
        """
        Aqui é onde você chamaria a LLM de verdade.
        Por enquanto, exemplo de placeholder:
        """
        # Simula delay de processamento
        time.sleep(0.5)

        # Retorna texto baseado na skill
        return f"# {skill.upper()} - {task_description}\n\nConteúdo gerado dinamicamente.\n"