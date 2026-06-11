# runtime/ide.py
import os
from runtime.agent import Agent

class IDE:
    def __init__(self):
        self.current_project = None
        self.agents = []

    def open_project(self, path):
        """Define o projeto que será manipulado"""
        if not os.path.isdir(path):
            raise ValueError(f"Projeto não encontrado: {path}")
        self.current_project = path
        print(f"[IDE] Projeto aberto: {self.current_project}")

    def scan_project(self):
        """Lista todos os arquivos do projeto"""
        if not self.current_project:
            raise ValueError("Nenhum projeto aberto")
        
        all_files = []
        for root, dirs, files in os.walk(self.current_project):
            for f in files:
                filepath = os.path.join(root, f)
                all_files.append({
                    "name": f,
                    "path": filepath,
                    "size": os.path.getsize(filepath),
                    "suffix": os.path.splitext(f)[1]
                })
        return all_files

    def add_agent(self, agent: Agent):
        self.agents.append(agent)
        print(f"[IDE] Agente {agent.name} adicionado")

    def run_agents(self):
        """Executa todos os agentes no projeto aberto"""
        if not self.current_project:
            raise ValueError("Nenhum projeto aberto")
        for agent in self.agents:
            print(f"[{agent.name}] executando...")
            agent.execute(self.current_project)