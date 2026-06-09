# runtime/run_company.py
from runtime.manager import Manager

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

    # mostrar relatório de performance
    from runtime.performance_tracker import tracker
    print("\n📊 RELATÓRIO DE PERFORMANCE:")
    for worker, stats in tracker.report().items():
        print(f"{worker}: {stats['tasks']} tarefas, média {stats['average_time']:.2f}s")