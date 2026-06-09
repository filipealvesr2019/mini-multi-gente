import os
import shutil

class Sandbox:
    BASE_DIR = os.path.join("workspace", "sandbox")

    @staticmethod
    def clear():
        """Apaga toda a sandbox."""
        if os.path.exists(Sandbox.BASE_DIR):
            shutil.rmtree(Sandbox.BASE_DIR)
            print("[SANDBOX] Limpada")

    @staticmethod
    def init():
        """Cria a pasta sandbox vazia."""
        os.makedirs(Sandbox.BASE_DIR, exist_ok=True)
        print(f"[SANDBOX] Inicializada em {Sandbox.BASE_DIR}")

    @staticmethod
    def create_file(path, content=""):
        """Cria arquivo dentro da sandbox, criando pastas se necessário."""
        full_path = os.path.join(Sandbox.BASE_DIR, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[SANDBOX] Criado arquivo: {full_path}")

    @staticmethod
    def read_file(path):
        """Lê conteúdo de arquivo dentro da sandbox."""
        full_path = os.path.join(Sandbox.BASE_DIR, path)
        if not os.path.exists(full_path):
            return None
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def list_files():
        """Lista arquivos e pastas dentro da sandbox."""
        for root, dirs, files in os.walk(Sandbox.BASE_DIR):
            level = root.replace(Sandbox.BASE_DIR, "").count(os.sep)
            indent = " " * 4 * level
            print(f"{indent}{os.path.basename(root)}/")
            sub_indent = " " * 4 * (level + 1)
            for f in files:
                print(f"{sub_indent}{f}")