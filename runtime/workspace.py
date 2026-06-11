from pathlib import Path


class Workspace:

    def __init__(self, root="workspace"):
        self.root = Path(root)

    def scan(self):
        files = []

        for path in self.root.rglob("*"):
            if path.is_file():
                files.append({
                    "name": path.name,
                    "path": str(path),
                    "suffix": path.suffix,
                    "size": path.stat().st_size
                })

        return files