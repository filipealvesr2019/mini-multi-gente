# runtime/router.py
import random

class Router:
    def choose_worker(self, workers, categoria):
        # Seleciona worker pela especialidade
        for w in workers:
            if w.especialidade == categoria:
                return w
        # fallback aleatório
        return random.choice(workers)