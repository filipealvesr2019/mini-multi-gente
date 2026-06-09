from runtime.department import Department
from runtime.agent import Agent
from runtime.company_config import COMPANY

class Company:

    def __init__(self):

        self.departments = []

        for dep_cfg in COMPANY["departments"]:

            dep = Department(dep_cfg["name"])

            manager_cfg = dep_cfg["manager"]

            manager = Agent(
                name=manager_cfg["name"],
                persona=manager_cfg["persona"],
                skills=manager_cfg["skills"],
                authority=50,
                tipo="manager",
                bus=None
            )

            dep.add_manager(manager)

            for worker_cfg in dep_cfg["workers"]:

                worker = Agent(
                    name=worker_cfg["name"],
                    persona=worker_cfg["persona"],
                    skills=worker_cfg["skills"],
                    authority=10,
                    tipo="worker",
                    bus=None
                )

                dep.add_worker(worker)

            self.departments.append(dep)

    def show_structure(self):

        print("\nEMPRESA\n")

        for dep in self.departments:

            print(f"Departamento: {dep.name}")

            for m in dep.managers:
                print(f"  Manager: {m.name}")

            for w in dep.workers:
                print(f"  Worker: {w.name}")

            print()