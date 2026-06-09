import json

query = input("Arquivo: ")

with open(
    "dependency_graph.json",
    "r",
    encoding="utf-8"
) as f:
    graph = json.load(f)

for file, deps in graph.items():

    if query.lower() in file.lower():

        print("\nArquivo:")
        print(file)

        print("\nDependências:")

        for dep in deps:
            print("  ", dep)