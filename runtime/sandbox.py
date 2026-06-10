import os
import shutil


class Sandbox:

    BASE_PATH = os.path.join("workspace", "sandbox")

    @classmethod
    def init(cls):
        os.makedirs(cls.BASE_PATH, exist_ok=True)
        print(f"[SANDBOX] Inicializada em {cls.BASE_PATH}")

    @classmethod
    def clear(cls):
        if os.path.exists(cls.BASE_PATH):
            shutil.rmtree(cls.BASE_PATH)

        os.makedirs(cls.BASE_PATH)
        print("[SANDBOX] Limpada")

    @classmethod
    def path(cls, relative_path):

        full_path = os.path.abspath(
            os.path.join(cls.BASE_PATH, relative_path)
        )

        base = os.path.abspath(cls.BASE_PATH)

        if not full_path.startswith(base):
            raise PermissionError(
                "Acesso fora da sandbox bloqueado"
            )

        return full_path

    @classmethod
    def create_file(cls, relative_path, content):

        file_path = cls.path(relative_path)

        os.makedirs(
            os.path.dirname(file_path),
            exist_ok=True
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as f:
            f.write(content)

        print(f"[SANDBOX] Arquivo criado: {file_path}")

        return file_path

    @classmethod
    def read_file(cls, relative_path):

        file_path = cls.path(relative_path)

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            return f.read()

    @classmethod
    def exists(cls, relative_path):

        return os.path.exists(
            cls.path(relative_path)
        )