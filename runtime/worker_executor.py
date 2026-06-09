import os
import difflib
import time
from runtime.sandbox import Sandbox

class WorkerExecutor:
    @staticmethod
    def execute(worker, file_path, content):
        path = Sandbox.get_path(file_path)
        os.makedirs(os.path.dirname(path), exist_ok=True)

        old_content = ""
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                old_content = f.read()
            action = "EDITADO"
        else:
            action = "CRIADO"

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        # calcula diff
        old_lines = old_content.splitlines()
        new_lines = content.splitlines()
        diff = list(difflib.unified_diff(old_lines, new_lines, lineterm=""))

        # simula progresso
        for p in [20,40,60,80,100]:
            time.sleep(0.3)
            print(f"[{worker.name}] {task_title} {p}%")

        # logs
        print(f"[{worker.name}] {action} {file_path}")
        added = sum(1 for l in diff if l.startswith("+") and not l.startswith("+++"))
        removed = sum(1 for l in diff if l.startswith("-") and not l.startswith("---"))
        print(f"[{worker.name}] DIFF +{added} -{removed}")
        if diff:
            print("--- DIFF ---")
            print("\n".join(diff))
            print("------------")