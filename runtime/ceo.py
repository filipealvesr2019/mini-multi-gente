from .manager import Manager
from .revisor import Revisor

class CEO:
    def __init__(self):
        self.manager = Manager()
        self.revisor = Revisor()

    def handle_task(self, tarefa):
        # Envia para manager
        subtarefas = self.manager.divide_task(tarefa)
        
        # Recebe respostas dos workers
        resultados = self.manager.execute_subtasks(subtarefas)
        
        # Revisa resultados
        final = self.revisor.revisar(resultados)
        return final

if __name__ == "__main__":
    ceo = CEO()
    resposta = ceo.handle_task("Crie uma calculadora React")
    print(resposta)