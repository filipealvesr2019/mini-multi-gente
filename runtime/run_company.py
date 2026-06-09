# runtime/run_company.py

from runtime.manager import Manager
from runtime.performance_tracker import tracker

if __name__ == "__main__":
    manager = Manager()
    tarefas = ["Criar sistema React completo"]

    subtasks = []
    for t in tarefas:
        subtasks.extend(manager.divide_task(t))

    resultados = manager.execute_subtasks(subtasks)

    print("\n📊 RESULTADOS FINAIS:")
    for r in resultados:
        print(r)

    print("\n📊 RELATÓRIO DE PERFORMANCE:")
    for worker, skills in tracker.report().items():
        for skill, stats in skills.items():
            print(f"{worker} ({skill}): {stats['tasks']} tarefas, média {stats['average_time']:.2f}s")