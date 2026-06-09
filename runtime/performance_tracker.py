# runtime/performance_tracker.py

class PerformanceTracker:
    def __init__(self):
        # dados por worker
        # { "João": {"tasks": 0, "total_time": 0.0} }
        self.data = {}

    def record(self, worker_name, duration):
        if worker_name not in self.data:
            self.data[worker_name] = {"tasks": 0, "total_time": 0.0}
        self.data[worker_name]["tasks"] += 1
        self.data[worker_name]["total_time"] += duration

    def average_time(self, worker_name):
        worker = self.data.get(worker_name)
        if worker and worker["tasks"] > 0:
            return worker["total_time"] / worker["tasks"]
        return 1.0  # default 1s para quem ainda não executou

    def report(self):
        return {
            worker: {
                "tasks": stats["tasks"],
                "average_time": stats["total_time"] / stats["tasks"]
            }
            for worker, stats in self.data.items()
        }

# tracker global
tracker = PerformanceTracker()