# runtime/sandbox.py
import os
import shutil
import difflib

SANDBOX_DIR = "workspace/sandbox"

class Sandbox:

    @staticmethod
    def clear():
        if os.path.exists(SANDBOX_DIR):
            shutil.rmtree(SANDBOX_DIR)
        print("[SANDBOX] Limpada")

    @staticmethod
    def init():
        os.makedirs(SANDBOX_DIR, exist_ok=True)
        print(f"[SANDBOX] Inicializada em {SANDBOX_DIR}")

    @staticmethod
    def create_file(worker_name, task_description, content):
        worker_dir = os.path.join(SANDBOX_DIR, worker_name)
        os.makedirs(worker_dir, exist_ok=True)
        # Nome do arquivo baseado na task
        filename = task_description.replace(" ", "_").replace(":", "") + ".txt"
        path = os.path.join(worker_dir, filename)
        # Salva conteúdo
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path

    @staticmethod
    def diff_file(file_path):
        """
        Calcula um diff básico para simular linhas adicionadas/removidas.
        Retorna +linhas -linhas
        """
        # Se o arquivo já existia antes, calcula diff
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                new_content = f.readlines()
            # Como ainda não temos histórico antigo, simulamos:
            plus = len(new_content)
            minus = 0
            return plus, minus
        else:
            with open(file_path, "r", encoding="utf-8") as f:
                plus = len(f.readlines())
            return plus, 0