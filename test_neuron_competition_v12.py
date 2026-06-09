# test_neuron_competition_v12.py
import random
from core.neuron_multistate import MultiStateNeuron

# Configurações iniciais
NUM_NEURONS = 5
CATEGORIES = ['texto', 'codigo', 'matematica', 'planejamento']
NUM_INPUTS = 5000

# Cria neurônios MultiState
neurons = [MultiStateNeuron(states=5) for _ in range(NUM_NEURONS)]

# Armazena contadores
state_wins = {i: 0 for i in range(5)}
specialization = {i: {cat: 0 for cat in CATEGORIES} for i in range(5)}
affinities = {i: {cat: 1.0 for cat in CATEGORIES} for i in range(5)}

# Simula competição
for _ in range(NUM_INPUTS):
    cat = random.choice(CATEGORIES)
    outputs = [neurons[i].forward(cat, cat) for i in range(NUM_NEURONS)]
    
    # Escolhe vencedor (maior hash)
    winner_idx = max(range(NUM_NEURONS), key=lambda i: hash(outputs[i]))
    state_wins[winner_idx] += 1
    specialization[winner_idx][cat] += 1
    affinities[winner_idx][cat] += random.uniform(0.05, 0.2)

# Imprime relatório
print("\n=== RELATÓRIO V12 ===\n")
print("=== DISTRIBUIÇÃO GLOBAL ===\n")
for state, wins in state_wins.items():
    perc = wins / NUM_INPUTS * 100
    print(f"Estado {state}: {wins} vitórias ({perc:.2f}%)")

print("\n=== ESPECIALIZAÇÃO POR CATEGORIA ===\n")
for state, cats in specialization.items():
    print(f"Estado {state}")
    for cat, count in cats.items():
        perc = count / max(1, sum(cats.values())) * 100
        print(f"  {cat}: {count} ({perc:.2f}%)")
    print()

print("=== AFINIDADES FINAIS ===\n")
for state, cats in affinities.items():
    print(f"Estado {state}")
    for cat, value in cats.items():
        print(f"  {cat}: {value:.2f}")
    print()

print("Fim do relatório.")