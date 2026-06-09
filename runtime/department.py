class Department:
    def __init__(self, name):
        self.name = name
        self.managers = []
        self.workers = []

    def add_manager(self, manager):
        self.managers.append(manager)

    def add_worker(self, worker):
        self.workers.append(worker)

    def info(self):
        return {
            "name": self.name,
            "managers": len(self.managers),
            "workers": len(self.workers)
        }