import os
import shutil

class Sandbox:
    BASE_PATH = os.path.join("workspace", "sandbox")

    @classmethod
    def init(cls):
        """Cria a sandbox limpa se não existir"""
        os.makedirs(cls.BASE_PATH, exist_ok=True)
        print(f"[SANDBOX] Inicializada em {cls.BASE_PATH}")

    @classmethod
    def clear(cls):
        """Apaga tudo dentro da sandbox"""
        if os.path.exists(cls.BASE_PATH):
            shutil.rmtree(cls.BASE_PATH)
        os.makedirs(cls.BASE_PATH)
        print("[SANDBOX] Limpada")

    @classmethod
    def path(cls, *subpaths):
        """Retorna o caminho seguro dentro da sandbox"""
        final_path = os.path.join(cls.BASE_PATH, *subpaths)
        final_path = os.path.abspath(final_path)

        if not final_path.startswith(os.path.abspath(cls.BASE_PATH)):
            raise PermissionError("Acesso fora da sandbox proibido!")

        # Garante que a pasta existe
        os.makedirs(os.path.dirname(final_path), exist_ok=True)
        return final_path

    @classmethod
    def create_file(cls, relative_path, content):
        """Cria ou sobrescreve um arquivo dentro da sandbox"""
        filepath = cls.path(relative_path)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[SANDBOX] Arquivo criado: {filepath}")

    @classmethod
    def read_file(cls, relative_path):
        """Lê um arquivo da sandbox"""
        filepath = cls.path(relative_path)
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()