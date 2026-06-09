from runtime.company import Company
from runtime.sandbox import Sandbox

def main():
    # Limpa e inicializa sandbox
    Sandbox.clear()
    Sandbox.init()

    empresa = Company()
    empresa.show_structure()

    tarefas = [
        "Projeto IDE Multi-Agente"
    ]

    for tarefa in tarefas:
        print(f"\n🚀 Nova tarefa: {tarefa}")
        empresa.create_task(tarefa)

if __name__ == "__main__":
    main()