import time
import random

class WorkerExecutor:

    @staticmethod
    def execute(worker, task):

        task.status = "running"

        for p in [10, 30, 50, 70, 90, 100]:

            time.sleep(random.uniform(0.5, 1.2))

            task.update(p)

            print(
                f"[{worker.name}] "
                f"{worker.persona} "
                f"{p}%"
            )

        print(
            f"[{worker.name}] FINALIZOU"
        )