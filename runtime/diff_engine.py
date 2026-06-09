# diff_engine.py
import os  # ESSENCIAL

def generate_diff(file_path):
    if not os.path.exists(file_path):
        return {"added": 0, "removed": 0}
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    added = len(lines)
    removed = 0  # futuramente você pode comparar versões anteriores
    return {"added": added, "removed": removed}