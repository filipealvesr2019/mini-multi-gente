from runtime.workspace_manager import WorkspaceManager

class ProjectScanner:

    @staticmethod
    def scan(project):

        files = WorkspaceManager.list_files(project)

        result = {}

        for file in files:

            folder = file.split("/")[0]

            if folder not in result:
                result[folder] = []

            result[folder].append(file)

        return result