import json
import os
from pathlib import Path
import re

# -------- CONFIGURAÇÃO --------
WORKSPACE_DOCS = "workspace_docs.json"
SYMBOLS_FILE = "symbols.json"
OUTPUT_DIR = Path("memory")

# Cria pastas principais
FILES_DIR = OUTPUT_DIR / "files"
SUMMARIES_DIR = OUTPUT_DIR / "summaries"
DEPENDENCIES_DIR = OUTPUT_DIR / "dependencies"

FILES_DIR.mkdir(parents=True, exist_ok=True)
SUMMARIES_DIR.mkdir(parents=True, exist_ok=True)
DEPENDENCIES_DIR.mkdir(parents=True, exist_ok=True)

# -------- CARREGA WORKSPACE DOCS --------
print("Carregando workspace_docs.json...")
with open(WORKSPACE_DOCS, "r", encoding="utf-8") as f:
    workspace_docs = json.load(f)

print(f"Arquivos no workspace: {len(workspace_docs)}")

# -------- CARREGA SÍMBOLOS --------
print("Carregando symbols.json...")
with open(SYMBOLS_FILE, "r", encoding="utf-8") as f:
    symbols = json.load(f)

# -------- EXTRAI ARQUIVOS E RESUMOS --------
summaries = []
dependencies = {}

for doc in workspace_docs:
    path = Path(doc["path"])
    content = doc["content"]
    
    # 1️⃣ Salva arquivo no memory/files
    safe_name = "_".join(path.parts).replace(" ", "_")
    file_out_path = FILES_DIR / f"{safe_name}.txt"
    with open(file_out_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    # 2️⃣ Extrai classes e funções simples
    classes = re.findall(r'class\s+(\w+)', content)
    functions = re.findall(r'(?:def|void|float|int|bool|std::\w+)\s+(\w+)\s*\(', content)
    
    summary = {
        "file": str(file_out_path),
        "classes": classes,
        "functions": functions
    }
    summaries.append(summary)
    
    # 3️⃣ Extrai dependências simples baseado nos símbolos
    file_deps = set()
    for sym in symbols:
        sym_name = sym.get("symbol")
        sym_file = Path(sym.get("file"))
        if sym_name and sym_name in content and sym_file != path:
            file_deps.add(str(sym_file))
    dependencies[str(file_out_path)] = list(file_deps)

# -------- SALVA SUMMARIES E DEPENDENCIES --------
with open(SUMMARIES_DIR / "file_summaries.json", "w", encoding="utf-8") as f:
    json.dump(summaries, f, indent=2)

with open(DEPENDENCIES_DIR / "dependency_graph.json", "w", encoding="utf-8") as f:
    json.dump(dependencies, f, indent=2)

print("=== BASE DE CONHECIMENTO CONCLUÍDA ===")
print(f"Arquivos extraídos: {len(workspace_docs)}")
print(f"Summaries salvos em: {SUMMARIES_DIR}")
print(f"Dependencies salvos em: {DEPENDENCIES_DIR}")