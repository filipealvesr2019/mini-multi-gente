# runtime/file_diff.py
import difflib
from runtime.workspace_manager import WorkspaceManager

def generate_diff(path, new_content):
    old_content = WorkspaceManager.read_file(path) or ""
    diff = difflib.unified_diff(
        old_content.splitlines(),
        new_content.splitlines(),
        fromfile="old",
        tofile="new",
        lineterm=""
    )
    return "\n".join(diff)