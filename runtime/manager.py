# runtime/manager.py

from concurrent.futures import ThreadPoolExecutor

from runtime.worker import Worker
from runtime.router import escolher_worker_inteligente


class Manager:

    def __init__(self):

        self.departments = []

    def load_company(self, company_data):

        self.departments.clear()

        for dep_data in company_data.get("departments", []):

            workers = []

            for w in dep_data.get("workers", []):

                worker = Worker(
                    name=w["name"],
                    persona=w["persona"],
                    skills=w["skills"]
                )

                workers.append(worker)

            self.departments.append({
                "name": dep_data["name"],
                "workers": workers
            })

    def get_department(self, department_name):

        for dep in self.departments:

            if dep["name"] == department_name:
                return dep

        return None

    def execute_operations(
        self,
        operations,
        content_generator
    ):

        results = []

        def run_operation(op):

            department = self.get_department(
                op["department"]
            )

            if not department:

                raise Exception(
                    f"Departamento não encontrado: "
                    f"{op['department']}"
                )

            worker, estado = escolher_worker_inteligente(
                department["workers"],
                op["skill"]
            )

            content = content_generator(
                worker,
                op
            )

            return worker.run_task(
                skill=op["skill"],
                task_title=op["task_title"],
                content=content
            )

        max_workers = max(
            1,
            len(operations)
        )

        with ThreadPoolExecutor(
            max_workers=max_workers
        ) as executor:

            futures = [
                executor.submit(
                    run_operation,
                    op
                )
                for op in operations
            ]

            for future in futures:

                results.append(
                    future.result()
                )

        return results