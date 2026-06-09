from agents.ceo_layer import CEOAgent
from agents.manager_layer import ManagerAgent
from agents.worker_layer import WorkerAgent

class MultiOrgSystem:
    def __init__(self):
        self.ceo = CEOAgent()
        self.manager = ManagerAgent()
        self.worker = WorkerAgent()

    def run(self, project_input):
        plan = self.ceo.forward(project_input)
        refined = self.manager.forward(plan)
        result = self.worker.forward(refined)
        return result