import threading


class CommandBus:
    def __init__(self):
        self.commands = []
        self.lock = threading.Lock()

    def send(self, target, message):
        with self.lock:
            self.commands.append((target, message))

    def get(self, target):
        msgs = []
        remaining = []

        with self.lock:
            for t, m in self.commands:
                if t == target:
                    msgs.append(m)
                else:
                    remaining.append((t, m))

            self.commands = remaining

        return msgs