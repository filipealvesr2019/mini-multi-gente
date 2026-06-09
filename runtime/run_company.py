# runtime/run_company.py
from runtime.sandbox import Sandbox
from runtime.manager import Manager

def main():
    Sandbox.clear()
    Sandbox.init()

    ceo_manager = Manager()

    tasks = ["Projeto IDE Multi-Agente"]

    for task_name in tasks:
        print(f"\n🚀 Nova tarefa: {task_name}")
        subtasks = ceo_manager.divide_task(task_name)
        resultados = ceo_manager.execute_subtasks(subtasks)
        print("\n📊 RESULTADOS:")
        for r in resultados:
            print(r)

if __name__ == "__main__":
    main()