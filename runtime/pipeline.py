from agents.ceo_layer import CEOAgent
from agents.manager_layer import ManagerAgent
from agents.worker_layer import WorkerAgent

class MultiOrgSystem:
    def __init__(self):
        self.ceo = CEOAgent()
        self.manager = ManagerAgent()
        self.worker = WorkerAgent()

    def run(self, project_input):
        print("\nINPUT:")
        print(project_input)

        plan = self.ceo.forward(project_input)
        print("\nCEO outputs:")
        print(plan)

        refined = self.manager.forward(plan)
        print("\nManager outputs:")
        print(refined)

        result = self.worker.forward(refined)
        print("\nWorker outputs:")
        print(result)

        return result