from runtime.sandbox import Sandbox
from runtime.manager import Manager
from runtime.auto_company_builder import AutoCompanyBuilder
from runtime.company_registry import CompanyRegistry

def prompt_func(worker, op):
    return f"Executando '{op['task_title']}' com skill '{op['skill']}' por {worker.name}\n"

def main():
    Sandbox.clear()
    Sandbox.init()

    registry = CompanyRegistry()
    builder = AutoCompanyBuilder(registry)

    task_description = input("Descreva a tarefa a ser realizada: ")
    company_name, company_data = builder.create_or_use_company(task_description)

    manager = Manager()
    manager.load_company(company_data)

    operations = []
    for dep in company_data.get("departments", []):
        for worker in dep["workers"]:
            for skill in worker["skills"]:
                task_title = f"{skill} - {task_description}"
                operations.append({
                    "department": dep["name"],
                    "skill": skill,
                    "worker_name": worker["name"],
                    "task_title": task_title
                })

    results = manager.execute_operations(operations, prompt_func)

    print("\n📊 RESULTADOS:")
    for r in results:
        print(f"[{r['worker']}] ENTREGUE {r['task']} -> {r['file']}")

if __name__ == "__main__":
    main()