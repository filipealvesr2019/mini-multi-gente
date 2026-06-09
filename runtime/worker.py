import random
import time


class Worker:

    def __init__(self, especialidade):

        self.especialidade = especialidade

        self.status = "aguardando"

        self.current_task = None

        self.progress = 0

    def execute(self, tarefa):

        self.status = "executando"

        self.current_task = tarefa

        for i in range(10):

            time.sleep(
                random.uniform(
                    0.2,
                    0.5
                )
            )

            self.progress = (
                (i + 1) * 10
            )

        resultado = (
            f"[{self.especialidade.upper()}] "
            f"Processado: {tarefa}"
        )

        self.status = "concluído"

        self.current_task = None

        self.progress = 100

        return resultado