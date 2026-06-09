from runtime.sandbox import Sandbox
from runtime.manager import Manager

def prompt_func(worker, op):
    # gera conteúdo baseado em skill dinamicamente
    return f"Executando tarefa '{op['task_title']}' com skill '{op['skill']}' por {worker.name}\n"

def main():
    Sandbox.clear()
    Sandbox.init()

    manager = Manager()

    # gerar operações baseadas no company_config
    operations = []
    task_name = "Projeto IDE Multi-Agente"
    for dep in manager.departments:
        for worker in dep["workers"]:
            for skill in worker.skills:
                task_title = f"{skill} - {task_name}"
                operations.append({
                    "department": dep["name"],
                    "skill": skill,
                    "worker_name": worker.name,
                    "task_title": task_title
                })

    results = manager.execute_operations(operations, prompt_func)

    print("\n📊 RESULTADOS:")
    for r in results:
        print(f"[{r['worker']}] ENTREGUE {r['task']} -> {r['file']}")

if __name__ == "__main__":
    main()