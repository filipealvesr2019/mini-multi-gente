import difflib

class DiffEngine:

    @staticmethod
    def compare(old_text, new_text):

        diff = difflib.unified_diff(
            old_text.splitlines(),
            new_text.splitlines(),
            lineterm=""
        )

        return "\n".join(diff)

    @staticmethod
    def stats(old_text, new_text):

        old_lines = old_text.splitlines()
        new_lines = new_text.splitlines()

        added = max(0, len(new_lines) - len(old_lines))
        removed = max(0, len(old_lines) - len(new_lines))

        return added, removed