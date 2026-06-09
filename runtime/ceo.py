# runtime/ceo.py
from .manager import Manager
from .revisor import Revisor

class CEO:
    def __init__(self):
        self.manager = Manager()
        self.revisor = Revisor()

    def handle_task(self, tarefa):
        subtarefas = self.manager.divide_task(tarefa)
        resultados = self.manager.execute_subtasks(subtarefas)
        final = self.revisor.revisar(resultados)
        return final

if __name__ == "__main__":
    ceo = CEO()
    tarefa = "Crie uma calculadora React"
    print("Iniciando tarefa do CEO...")
    resposta = ceo.handle_task(tarefa)
    print("\n=== Resultado final ===")
    print(resposta)