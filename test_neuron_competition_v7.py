from core.neuron_multistate import MultiStateNeuron
import random

# Categorias de teste
categories = ["texto", "codigo", "matematica", "planejamento"]

# Configurações do neurônio
num_states = 5
num_inputs = 5000

# Inicializa neurônio
neuron = MultiStateNeuron(states=num_states)

# Contadores globais
state_wins = {i: 0 for i in range(num_states)}
state_category = {i: {cat: 0 for cat in categories} for i in range(num_states)}

# Simula inputs
for _ in range(num_inputs):
    category = random.choice(categories)
    output = neuron.forward(category)  # usa forward
    state_idx = int(output.split("_")[1])

    # Conta vitória global
    state_wins[state_idx] += 1

    # Conta especialização por categoria
    state_category[state_idx][category] += 1

# Calcula afinidades finais
state_affinity = {}
for s in range(num_states):
    state_affinity[s] = {}
    for cat in categories:
        state_affinity[s][cat] = state_category[s][cat] / max(1, state_wins[s]) * 50  # escala

# === Relatório ===
print("\n=== RELATÓRIO V7 ===\n")
print("=== DISTRIBUIÇÃO GLOBAL ===\n")
for s, count in state_wins.items():
    perc = count / num_inputs * 100
    print(f"Estado {s}: {count} vitórias ({perc:.2f}%)")

print("\n=== ESPECIALIZAÇÃO POR CATEGORIA ===\n")
for s, cats in state_category.items():
    print(f"Estado {s}")
    for cat, c in cats.items():
        perc = c / max(1, state_wins[s]) * 100
        print(f"  {cat}: {c} ({perc:.2f}%)")
    print()

print("=== AFINIDADES FINAIS ===\n")
for s, cats in state_affinity.items():
    print(f"Estado {s}")
    for cat, aff in cats.items():
        print(f"  {cat}: {aff:.2f}")
    print()