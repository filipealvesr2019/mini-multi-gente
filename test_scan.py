from runtime.workspace import Workspace

# Cria instância do scanner
ws = Workspace("workspace")

# Varre todos os arquivos
files = ws.scan()

# Mostra os arquivos
for file in files:
    print(file)