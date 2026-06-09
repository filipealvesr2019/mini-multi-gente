# runtime/router.py
class Router:
    def choose_worker(self, workers, categoria):
        # Escolhe o worker com a mesma especialidade
        for w in workers:
            if w.especialidade == categoria:
                return w
        # fallback aleatório
        import random
        return random.choice(workers)