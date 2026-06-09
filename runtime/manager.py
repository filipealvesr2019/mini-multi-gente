from concurrent.futures import ThreadPoolExecutor
import threading
import time

from .worker import Worker
from .router import Router


class Manager:

    def __init__(self):

        self.router = Router()

        self.workers = [

            Worker(
                "Ana",
                "texto"
            ),

            Worker(
                "João",
                "codigo"
            ),

            Worker(
                "Pedro",
                "matematica"
            ),

            Worker(
                "Marina",
                "planejamento"
            )

        ]

    def divide_task(self, tarefa):

        return [

            {
                "categoria": "texto",
                "conteudo": (
                    "Criar interface e descrição"
                )
            },

            {
                "categoria": "codigo",
                "conteudo": (
                    "Criar código React"
                )
            },

            {
                "categoria": "matematica",
                "conteudo": (
                    "Implementar operações"
                )
            },

            {
                "categoria": "planejamento",
                "conteudo": (
                    "Planejar arquitetura"
                )
            }

        ]

    def dashboard_loop(self):

        while True:

            print("\n")
            print("=" * 60)
            print("CEO DASHBOARD")
            print("=" * 60)

            concluidos = 0

            for worker in self.workers:

                print(
                    f"{worker.nome:<12}"
                    f"{worker.especialidade:<15}"
                    f"{worker.status:<15}"
                    f"{worker.progress}%"
                )

                if worker.status == "concluído":
                    concluidos += 1

            if concluidos == len(self.workers):
                break

            time.sleep(1)

    def execute_subtasks(self, subtasks):

        resultados = []

        dashboard = threading.Thread(
            target=self.dashboard_loop
        )

        dashboard.start()

        def executar(subtask):

            worker = self.router.choose_worker(
                self.workers,
                subtask["categoria"]
            )

            return worker.execute(
                subtask["conteudo"]
            )

        with ThreadPoolExecutor(
            max_workers=4
        ) as executor:

            futures = [

                executor.submit(
                    executar,
                    subtask
                )

                for subtask in subtasks

            ]

            for future in futures:

                resultados.append(
                    future.result()
                )

        dashboard.join()

        return resultados