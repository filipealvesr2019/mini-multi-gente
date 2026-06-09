# runtime/worker_executor.py
import threading

class WorkerExecutor:

    @staticmethod
    def execute(worker, task_description):
        """
        Executa a tarefa do worker em uma thread segura.
        """
        t = threading.Thread(target=worker.run_task, args=(None, task_description))
        t.start()
        t.join()