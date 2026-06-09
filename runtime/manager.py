from concurrent.futures import ThreadPoolExecutor
import threading
import time

from .worker import Worker
from .router import Router


class Manager:

    def __init__(self):

        self.router = Router()

        self.workers = [
            Worker("texto"),
            Worker("codigo"),
            Worker("matematica"),
            Worker("planejamento")
        ]

    def divide_task(self, tarefa):

        return [
            {
                "categoria": "texto",
                "conteudo": f"Gerar interface e descrição: {tarefa}"
            },
            {
                "categoria": "codigo",
                "conteudo": f"Gerar código base: {tarefa}"
            },
            {
                "categoria": "matematica",
                "conteudo": f"Gerar cálculos: {tarefa}"
            },
            {
                "categoria": "planejamento",
                "conteudo": f"Planejar etapas e componentes: {tarefa}"
            }
        ]

    def dashboard_loop(self):

        while True:

            print("\n" * 2)
            print("=" * 50)
            print("CEO DASHBOARD")
            print("=" * 50)

            concluidos = 0

            for worker in self.workers:

                print(
                    f"{worker.especialidade:<15}"
                    f"{worker.status:<15}"
                    f"{worker.progress}%"
                )

                if worker.status == "concluído":
                    concluidos += 1

            if concluidos == len(self.workers):
                break

            time.sleep(1)

    def execute_subtasks(self, subtarefas):

        resultados = []

        dashboard = threading.Thread(
            target=self.dashboard_loop
        )

        dashboard.start()

        def executar(sub):

            worker = self.router.choose_worker(
                self.workers,
                sub["categoria"]
            )

            print(
                f"\n[{worker.especialidade.upper()}] INICIOU"
            )

            resultado = worker.execute(
                sub["conteudo"]
            )

            print(
                f"[{worker.especialidade.upper()}] TERMINOU"
            )

            return resultado

        with ThreadPoolExecutor(max_workers=4) as executor:

            futures = [
                executor.submit(
                    executar,
                    sub
                )
                for sub in subtarefas
            ]

            for future in futures:
                resultados.append(
                    future.result()
                )

        dashboard.join()

        return resultados