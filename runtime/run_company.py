from runtime.auto_company_builder import AutoCompanyBuilder
from runtime.company_registry import CompanyRegistry
from runtime.manager import Manager
from runtime.sandbox import Sandbox

def prompt_func(worker, op):
    return f"{worker.name} executando {op['task_title']}"

def main():
    Sandbox.clear()
    Sandbox.init()

    registry = CompanyRegistry()
    builder = AutoCompanyBuilder(registry)

    # Prompt da tarefa
    task = input("Descreva a tarefa a ser realizada: ")

    # Cria ou usa empresa existente automaticamente
    company_name, company_data = builder.create_or_use_company(task)

    print(f"[AUTO] Empresa selecionada: {company_name}")

    manager = Manager()
    manager.load_company(company_data)

    # Gerar operações para todos os workers
    operations = []
    for dep in company_data["departments"]:
        for worker in dep["workers"]:
            for skill in worker["skills"]:
                operations.append({
                    "department": dep["name"],
                    "skill": skill,
                    "task_title": f"{skill} - {task}"
                })

    results = manager.execute_operations(operations, prompt_func)

    print("\n📊 RESULTADOS:")
    for r in results:
        print(r)

if __name__ == "__main__":
    main()