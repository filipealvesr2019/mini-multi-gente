# run_ide_test.py
from runtime.ide import IDE
from runtime.agent import Agent

# Cria IDE
ide = IDE()

# Abre projeto em qualquer lugar do disco
ide.open_project(r"C:\Users\filipe\Documents\themes it html\byteforge")  # coloque seu caminho real

# Cria agentes
agente1 = Agent("João", skills=["react"])
agente2 = Agent("Ana", skills=["css"])

# Adiciona agentes
ide.add_agent(agente1)
ide.add_agent(agente2)

# Roda agentes
ide.run_agents()