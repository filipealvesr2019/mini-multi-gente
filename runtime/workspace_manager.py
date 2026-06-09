# runtime/workspace_manager.py
from runtime.sandbox import Sandbox
from pathlib import Path

class WorkspaceManager:

    @classmethod
    def create_file(cls, path, content=""):
        full_path = Sandbox.path(path)
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(content, encoding="utf-8")
        return full_path

    @classmethod
    def read_file(cls, path):
        full_path = Sandbox.path(path)
        if not full_path.exists():
            return None
        return full_path.read_text(encoding="utf-8")

    @classmethod
    def update_file(cls, path, content):
        full_path = Sandbox.path(path)
        if not full_path.exists():
            raise FileNotFoundError(full_path)
        full_path.write_text(content, encoding="utf-8")

    @classmethod
    def append_file(cls, path, content):
        full_path = Sandbox.path(path)
        if not full_path.exists():
            raise FileNotFoundError(full_path)
        with open(full_path, "a", encoding="utf-8") as f:
            f.write(content)

    @classmethod
    def delete_file(cls, path):
        full_path = Sandbox.path(path)
        if full_path.exists():
            full_path.unlink()

    @classmethod
    def list_files(cls):
        return [str(f.relative_to(Sandbox.ROOT)) 
                for f in Sandbox.ROOT.rglob("*") if f.is_file()]