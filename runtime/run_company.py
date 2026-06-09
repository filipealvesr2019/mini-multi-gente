from runtime.company import Company

def main():
    # Inicializa a empresa com departamentos, managers e workers
    empresa = Company()

    # Mostra a estrutura da empresa
    empresa.show_structure()

    # Cria tarefas
    tarefas = ["Projeto IDE Multi-Agente"]

    for tarefa in tarefas:
        print(f"\n🚀 Nova tarefa: {tarefa}")
        empresa.create_task(tarefa)

if __name__ == "__main__":
    main()