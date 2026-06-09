import os
import shutil

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
    def save_file(worker_name, filename, content):
        worker_dir = os.path.join(SANDBOX_DIR, worker_name)
        os.makedirs(worker_dir, exist_ok=True)
        path = os.path.join(worker_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[{worker_name}] CRIADO {path}")
        return path