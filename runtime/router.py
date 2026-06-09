import random


class Router:

    def choose_worker(
        self,
        workers,
        categoria
    ):

        for worker in workers:

            if (
                worker.especialidade
                == categoria
            ):
                return worker

        return random.choice(
            workers
        )