from runtime.companies_config import COMPANIES_CONFIG
from runtime.manager import Manager
from runtime.sandbox import Sandbox

def prompt_func(worker, op):
    return f"{worker.name} executando {op['task_title']}"

def main():

    Sandbox.clear()
    Sandbox.init()

    print("\nTemplates disponíveis:\n")

    names = list(COMPANIES_CONFIG.keys())

    for i, name in enumerate(names, start=1):
        print(f"{i} - {name}")

    choice = int(input("\nEscolha: "))

    company_name = names[choice - 1]
    company_data = COMPANIES_CONFIG[company_name]

    manager = Manager()
    manager.load_company(company_data)

    task = input("\nTarefa: ")

    operations = []

    for dep in company_data["departments"]:

        for worker in dep["workers"]:

            for skill in worker["skills"]:

                operations.append({
                    "department": dep["name"],
                    "skill": skill,
                    "task_title": f"{skill} - {task}"
                })

    results = manager.execute_operations(
        operations,
        prompt_func
    )

    print("\nRESULTADOS\n")

    for r in results:
        print(r)

if __name__ == "__main__":
    main()