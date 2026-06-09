import random
from collections import defaultdict

# Categorias de teste
categories = ["texto", "codigo", "matematica", "planejamento"]

# Classe de neurônio multiestado competitivo
class CompetitiveMultiStateNeuron:
    def __init__(self, states=5):
        self.states = states
        # Afinidade inicial igual para todos
        self.affinity = [{cat: 1.0 for cat in categories} for _ in range(states)]
        self.memory = {i: [] for i in range(states)}

    def forward(self, category):
        # Cada estado tem chance proporcional à afinidade
        scores = [self.affinity[s][category] for s in range(self.states)]
        winner = scores.index(max(scores))
        # Registra o input
        self.memory[winner].append(category)
        # Reforço do estado vencedor para essa categoria
        self.affinity[winner][category] += 1.0
        return winner

# Simulação de múltiplos inputs
def simulate(neuron, num_trials=5000):
    global_counts = [0] * neuron.states
    category_counts = [defaultdict(int) for _ in range(neuron.states)]

    for _ in range(num_trials):
        cat = random.choice(categories)
        winner = neuron.forward(cat)
        global_counts[winner] += 1
        category_counts[winner][cat] += 1

    return global_counts, category_counts, neuron.affinity

# Função de relatório
def print_report(global_counts, category_counts, affinities):
    print("=== RELATÓRIO V8 ===\n")
    total = sum(global_counts)
    print("=== DISTRIBUIÇÃO GLOBAL ===\n")
    for s, count in enumerate(global_counts):
        print(f"Estado {s}: {count} vitórias ({count/total*100:.2f}%)")
    print("\n=== ESPECIALIZAÇÃO POR CATEGORIA ===\n")
    for s, cat_counts in enumerate(category_counts):
        print(f"Estado {s}")
        for cat in categories:
            print(f"  {cat}: {cat_counts[cat]} ({cat_counts[cat]/sum(cat_counts.values())*100 if sum(cat_counts.values())>0 else 0:.2f}%)")
    print("\n=== AFINIDADES FINAIS ===\n")
    for s, aff in enumerate(affinities):
        print(f"Estado {s}")
        for cat in categories:
            print(f"  {cat}: {aff[cat]:.2f}")
    print("\nFim do relatório.")

# Execução do teste
if __name__ == "__main__":
    neuron = CompetitiveMultiStateNeuron(states=5)
    global_counts, category_counts, affinities = simulate(neuron, num_trials=5000)
    print_report(global_counts, category_counts, affinities)