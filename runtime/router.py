class Router:
    def choose_worker(self, workers, categoria):
        for w in workers:
            if w.especialidade == categoria:
                return w
        return workers[0]