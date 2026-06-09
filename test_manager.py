from agents.manager_layer import ManagerAgent

manager = ManagerAgent()

print(manager.forward("planejamento inicial"))
print(manager.forward("otimizar banco de dados"))
print(manager.forward("gerar interface UI"))