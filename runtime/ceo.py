from .manager import Manager
import threading

class CEO:
    def __init__(self):
        self.manager = Manager()

    def run(self, tarefa):
        print("Iniciando tarefa do CEO...")

        subtasks = self.manager.divide_task(tarefa)

        # thread para ler comandos humanos
        def input_loop():
            while True:
                cmd = input("CEO> ")
                if cmd.lower() in ["exit", "sair", "fim"]:
                    break
                self.manager.command(cmd)

        threading.Thread(target=input_loop, daemon=True).start()

        resultados = self.manager.execute_subtasks(subtasks)

        print("\n=== Resultado final ===")
        for r in resultados:
            print(r)


if __name__ == "__main__":
    ceo = CEO()
    ceo.run("Crie uma calculadora React")