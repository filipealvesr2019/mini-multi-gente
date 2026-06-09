import json
import re

print("Carregando workspace_docs.json...")

with open("workspace_docs.json", "r", encoding="utf-8") as f:
    documents = json.load(f)

symbols = []

class_pattern = re.compile(r'class\s+([A-Za-z_][A-Za-z0-9_]*)')
function_pattern = re.compile(
    r'([A-Za-z_][A-Za-z0-9_:<>]*)\s+([A-Za-z_][A-Za-z0-9_]*)\s*\('
)

for doc in documents:

    path = doc["path"]
    content = doc["content"]

    classes = class_pattern.findall(content)

    for cls in classes:
        symbols.append({
            "symbol": cls,
            "type": "class",
            "file": path
        })

    functions = function_pattern.findall(content)

    for return_type, func in functions:
        symbols.append({
            "symbol": func,
            "type": "function",
            "file": path
        })

print(f"Símbolos encontrados: {len(symbols)}")

with open("symbols.json", "w", encoding="utf-8") as f:
    json.dump(symbols, f, indent=2)

print("symbols.json salvo!")