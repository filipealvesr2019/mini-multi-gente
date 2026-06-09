from pathlib import Path

class FileSystem:

    ROOT = Path("workspace/sandbox")

    @classmethod
    def init(cls):
        cls.ROOT.mkdir(parents=True, exist_ok=True)

    @classmethod
    def create_file(cls, path, content=""):

        full = cls.ROOT / path

        full.parent.mkdir(parents=True, exist_ok=True)

        full.write_text(content, encoding="utf-8")

        return str(full)

    @classmethod
    def read_file(cls, path):

        full = cls.ROOT / path

        if not full.exists():
            return None

        return full.read_text(encoding="utf-8")

    @classmethod
    def edit_file(cls, path, new_content):

        full = cls.ROOT / path

        if not full.exists():
            return False

        full.write_text(new_content, encoding="utf-8")

        return True

    @classmethod
    def create_folder(cls, path):

        full = cls.ROOT / path

        full.mkdir(parents=True, exist_ok=True)

    @classmethod
    def list_tree(cls):

        for p in cls.ROOT.rglob("*"):
            print(p)