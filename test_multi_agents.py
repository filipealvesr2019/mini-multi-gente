from runtime.pipeline import MultiOrgSystem
from collections import Counter

# Instancia sistema
system = MultiOrgSystem()

# Quantidade de testes
tasks = [f"Tarefa {i}" for i in range(1000)]

# Armazenar outputs
all_outputs = {
    "CEO": [],
    "Manager": [],
    "Worker": []
}

print("Executando testes...\n")

# Executa pipeline
for task in tasks:

    ceo_out = system.ceo.forward(task)
    all_outputs["CEO"].append(ceo_out)

    manager_out = system.manager.forward(ceo_out)
    all_outputs["Manager"].append(manager_out)

    worker_out = system.worker.forward(manager_out)
    all_outputs["Worker"].append(worker_out)

print("Testes concluídos.")

# Diversidade de estados
print("\n===== DIVERSIDADE =====")

for agent_name, outputs in all_outputs.items():

    print(f"\n--- {agent_name} ---")

    for neuron_idx in range(len(outputs[0])):

        neuron_states = [task[neuron_idx] for task in outputs]

        unique_states = set(neuron_states)

        print(
            f"Neuron {neuron_idx}: "
            f"{len(unique_states)} estados diferentes"
        )

# Distribuição detalhada
print("\n\n===== DISTRIBUICAO =====")

for agent_name, outputs in all_outputs.items():

    print(f"\n======================")
    print(f"AGENTE: {agent_name}")
    print(f"======================")

    for neuron_idx in range(len(outputs[0])):

        neuron_states = [task[neuron_idx] for task in outputs]

        counts = Counter(neuron_states)

        print(f"\nNeuron {neuron_idx}")

        total = len(neuron_states)

        for state, count in sorted(counts.items()):

            pct = (count / total) * 100

            print(
                f"{state}: {count} ({pct:.2f}%)"
            )

print("\nFim da análise.")