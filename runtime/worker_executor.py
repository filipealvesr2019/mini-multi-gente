# runtime/worker_executor.py

import traceback
import time


class WorkerExecutor:

    @staticmethod
    def execute(worker, operation):
        """
        Executa qualquer operação.

        O formato da operação não é definido aqui.
        O executor apenas encaminha.
        """

        started_at = time.time()

        try:

            print(
                f"[EXECUTOR] "
                f"worker={worker.name}"
            )

            result = worker.run_task(operation)

            elapsed = round(
                time.time() - started_at,
                2
            )

            return {
                "success": True,
                "worker": worker.name,
                "execution_time": elapsed,
                "result": result
            }

        except Exception as e:

            traceback.print_exc()

            return {
                "success": False,
                "worker": worker.name,
                "error": str(e)
            }