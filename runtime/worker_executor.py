import os

class WorkerExecutor:

    @staticmethod
    def execute(worker, task):

        if worker.name == "João":
            os.makedirs("workspace/frontend", exist_ok=True)
            with open("workspace/frontend/App.jsx", "w", encoding="utf8") as f:
                f.write("// React App\n")

        elif worker.name == "Ana":
            os.makedirs("workspace/frontend", exist_ok=True)
            with open("workspace/frontend/style.css", "w", encoding="utf8") as f:
                f.write("body{}")

        elif worker.name == "Marina":
            os.makedirs("workspace/docs", exist_ok=True)
            with open("workspace/docs/README.md", "w", encoding="utf8") as f:
                f.write("# Projeto\n")

        print(f"{worker.name} entregou artefato")