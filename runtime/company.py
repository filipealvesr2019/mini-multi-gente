from runtime.agent import Agent
from runtime.department import Department
from runtime.task import Task
from runtime.company_config import COMPANY_CONFIG

class Company:

    def __init__(self):
        self.ceos = []
        self.departments = []
        self.load_config()

    def load_config(self):
        for ceo_data in COMPANY_CONFIG["ceos"]:
            ceo = Agent(
                name=ceo_data["name"],
                role="CEO",
                persona=ceo_data["persona"],
                skills=ceo_data["skills"],
                authority=100
            )
            self.ceos.append(ceo)

        for dep_data in COMPANY_CONFIG["departments"]:
            manager = Agent(
                name=dep_data["manager"]["name"],
                role="Manager",
                persona=dep_data["manager"]["persona"],
                skills=dep_data["manager"]["skills"],
                authority=50
            )
            department = Department(dep_data["name"], manager)
            for worker_data in dep_data["workers"]:
                worker = Agent(
                    name=worker_data["name"],
                    role="Worker",
                    persona=worker_data["persona"],
                    skills=worker_data["skills"],
                    authority=10
                )
                department.add_worker(worker)
            self.departments.append(department)

    def show_structure(self):
        print("\nEMPRESA\n")
        print("CEOs:")
        for ceo in self.ceos:
            print(f"  {ceo.name}")
        print()
        for dep in self.departments:
            print(f"Departamento: {dep.name}")
            print(f"  Manager: {dep.manager.name}")
            for worker in dep.workers:
                print(f"  Worker: {worker.name}")
            print()

    def create_task(self, task_title):
        task = Task(task_title)
        print("\nCEO criou tarefa:")
        print(f"  {task.title}")
        for department in self.departments:
            department.assign_task(task)