from datetime import datetime

class ChangeLog:

    history = []

    @classmethod
    def add(
        cls,
        worker,
        file,
        added,
        removed
    ):

        cls.history.append({
            "worker": worker,
            "file": file,
            "added": added,
            "removed": removed,
            "time": datetime.now().isoformat()
        })

    @classmethod
    def show(cls):

        print("\n=== CHANGE LOG ===\n")

        for item in cls.history:

            print(
                f"[{item['worker']}] "
                f"{item['file']} "
                f"+{item['added']} "
                f"-{item['removed']}"
            )