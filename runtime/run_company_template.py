from runtime.companies_config import COMPANIES_CONFIG
from runtime.manager import Manager
from runtime.sandbox import Sandbox

def prompt_func(worker, op):
    return f"{worker.name} executando {op['task_title']}"

def main():
    Sandbox.clear()
    Sandbox.init()

    # Lista todos os templates disponíveis com identificador
    templates = list(COMPANIES_CONFIG.keys())
    print("=== Templates disponíveis ===")
    for i, name in enumerate(templates, start=1):
        # Mostra ID + nome
        display_name = COMPANIES_CONFIG[name].get("type", name).capitalize()
        print(f"[{i}] {name} - {display_name}")

    # Escolha do usuário
    while True:
        try:
            choice = int(input("Escolha a empresa/template (ID): "))
            if 1 <= choice <= len(templates):
                break
            print("ID inválido! Escolha um número da lista.")
        except ValueError:
            print("Digite um número válido!")

    company_name = templates[choice-1]
    company_data = COMPANIES_CONFIG[company_name]

    print(f"\n[INFO] Você escolheu: {company_name}")

    # Prompt da tarefa
    task = input("Descreva a tarefa a ser realizada: ")

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