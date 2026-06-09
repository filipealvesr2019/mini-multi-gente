import os
import json

print("Iniciando escaneamento...")

workspace_dir = "workspace_test"
all_files = []

allowed_exts = [".html", ".py", ".cpp", ".h", ".js", ".ts", ".tsx"]

for root, dirs, files in os.walk(workspace_dir):
    for file in files:
        if any(file.endswith(ext) for ext in allowed_exts):

            path = os.path.join(root, file)

            print(f"Escaneando: {path}")

            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            all_files.append({
                "path": path,
                "content": content
            })

print(f"\nArquivos encontrados: {len(all_files)}")

with open("workspace_docs.json", "w", encoding="utf-8") as f:
    json.dump(all_files, f, indent=2)

print("workspace_docs.json salvo com sucesso!")
print("Escaneamento concluído!")