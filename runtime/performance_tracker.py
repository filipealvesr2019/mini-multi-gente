# runtime/performance_tracker.py

import threading
import time

class PerformanceTracker:
    def __init__(self):
        # dados por worker e skill
        self.data = {}
        self.lock = threading.Lock()

    def log_task(self, worker_name, skill, duration):
        with self.lock:
            if worker_name not in self.data:
                self.data[worker_name] = {}
            if skill not in self.data[worker_name]:
                self.data[worker_name][skill] = {"tasks": 0, "total_time": 0.0}
            self.data[worker_name][skill]["tasks"] += 1
            self.data[worker_name][skill]["total_time"] += duration

    def average_time(self, worker_name, skill):
        with self.lock:
            if worker_name in self.data and skill in self.data[worker_name]:
                info = self.data[worker_name][skill]
                return info["total_time"] / info["tasks"]
        return float('inf')

    def report(self):
        with self.lock:
            report = {}
            for worker, skills in self.data.items():
                report[worker] = {}
                for skill, info in skills.items():
                    avg = info["total_time"] / info["tasks"]
                    report[worker][skill] = {"tasks": info["tasks"], "average_time": avg}
            return report

# Tracker global
tracker = PerformanceTracker()