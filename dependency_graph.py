import json
import re

print("Construindo grafo...")

with open("workspace_docs.json", "r", encoding="utf-8") as f:
    documents = json.load(f)

graph = {}

include_pattern = re.compile(
    r'#include\s+[<"]([^">]+)[">]'
)

for doc in documents:

    path = doc["path"]
    content = doc["content"]

    includes = include_pattern.findall(content)

    graph[path] = includes

with open(
    "dependency_graph.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(graph, f, indent=2)

print("dependency_graph.json salvo!")