import random
import time


class Worker:

    def __init__(self, nome, especialidade):

        self.nome = nome
        self.especialidade = especialidade

        self.status = "aguardando"
        self.current_task = None
        self.progress = 0

    def execute(self, tarefa):

        self.status = "executando"
        self.current_task = tarefa

        print(
            f"\n[{self.nome} - {self.especialidade.upper()}] INICIOU"
        )

        for i in range(10):

            time.sleep(
                random.uniform(0.2, 0.5)
            )

            self.progress = (i + 1) * 10

        self.status = "concluído"
        self.progress = 100

        print(
            f"[{self.nome} - {self.especialidade.upper()}] TERMINOU"
        )

        return (
            f"[{self.nome}] "
            f"Processado: {tarefa}"
        )