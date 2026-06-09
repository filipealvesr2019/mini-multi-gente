from .manager import Manager


class CEO:

    def __init__(self):

        self.manager = Manager()

    def run(self, tarefa):

        print(
            "Iniciando tarefa do CEO..."
        )

        subtasks = (
            self.manager.divide_task(
                tarefa
            )
        )

        resultados = (
            self.manager.execute_subtasks(
                subtasks
            )
        )

        print("\n=== Resultado final ===")

        for resultado in resultados:

            print(resultado)


if __name__ == "__main__":

    ceo = CEO()

    ceo.run(
        "Crie uma calculadora React"
    )