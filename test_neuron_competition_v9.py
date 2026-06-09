# test_neuron_competition_v9.py
import random
from core.neuron_multistate import MultiStateNeuron

# Configurações
num_states = 5
categories = ["texto", "codigo", "matematica", "planejamento"]
num_inputs_per_category = 1000
exploration_noise = 0.1  # ruído para exploração
fatigue_penalty = 0.05   # penalidade para estados já usados muito

# Inicializa neurônio multiestado
neuron = MultiStateNeuron(states=num_states)

# Inicializa afinidades
affinities = {state: {cat: 1.0 for cat in categories} for state in range(num_states)}

# Inicializa contadores de vitórias
wins = {state: 0 for state in range(num_states)}
wins_per_category = {state: {cat: 0 for cat in categories} for state in range(num_states)}

# Simula inputs
inputs = []
for cat in categories:
    for i in range(num_inputs_per_category):
        inputs.append((cat, f"{cat}_input_{i}"))

# Executa competição
for cat, inp in inputs:
    scores = {}
    for state in range(num_states):
        # Score = afinidade + ruído - penalidade por uso
        score = affinities[state][cat] + random.uniform(0, exploration_noise) - len(neuron.memory[state]) * fatigue_penalty
        scores[state] = score

    # Escolhe vencedor
    winner = max(scores, key=scores.get)

    # Atualiza memória e afinidades
    neuron.forward(inp)  # memoriza input
    affinities[winner][cat] += 1.0  # reforço positivo

    # Contadores
    wins[winner] += 1
    wins_per_category[winner][cat] += 1

# Calcula afinidades finais
final_affinities = {state: {} for state in range(num_states)}
for state in range(num_states):
    for cat in categories:
        final_affinities[state][cat] = affinities[state][cat]

# Relatório
print("\n=== RELATÓRIO V9 ===\n")
print("=== DISTRIBUIÇÃO GLOBAL ===\n")
for state in range(num_states):
    print(f"Estado {state}: {wins[state]} vitórias ({wins[state]/len(inputs)*100:.2f}%)")
print("\n=== ESPECIALIZAÇÃO POR CATEGORIA ===\n")
for state in range(num_states):
    print(f"Estado {state}")
    for cat in categories:
        print(f"  {cat}: {wins_per_category[state][cat]} ({wins_per_category[state][cat]/num_inputs_per_category*100:.2f}%)")
print("\n=== AFINIDADES FINAIS ===\n")
for state in range(num_states):
    print(f"Estado {state}")
    for cat in categories:
        print(f"  {cat}: {final_affinities[state][cat]:.2f}")
print("\nFim do relatório.")