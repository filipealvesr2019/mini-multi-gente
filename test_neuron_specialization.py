# test_neuron_specialization.py
from collections import Counter

# --- Definição do neurônio multiestado ---
class MultiStateNeuron:
    def __init__(self, states=5):
        self.states = states
        self.state_counter = Counter()
        self.category_counter = {i: Counter() for i in range(states)}

    def select_state(self, x):
        # Hash simples para roteamento
        return hash(str(x)) % self.states

    def forward(self, x, category):
        state = self.select_state(x)
        self.state_counter[state] += 1
        self.category_counter[state][category] += 1
        return f"state_{state}_output"

    def report(self):
        total = sum(self.state_counter.values())
        print("\n=== RELATÓRIO DE ESTADOS ===")
        for state, count in sorted(self.state_counter.items()):
            pct = count / total * 100
            print(f"Estado {state}: {count} usos ({pct:.2f}%)")
        print("\n=== ESPECIALIZAÇÃO POR CATEGORIA ===")
        for state, cat_counts in self.category_counter.items():
            print(f"\nEstado {state}:")
            total_state = sum(cat_counts.values())
            for cat, count in cat_counts.items():
                pct = count / total_state * 100 if total_state > 0 else 0
                print(f"  Categoria '{cat}': {count} usos ({pct:.2f}%)")

# --- Inputs categorizados ---
categories = ["texto", "codigo", "matematica", "planejamento"]
inputs_per_category = 250  # total 1000 inputs

# --- Inicializa neurônio ---
neuron = MultiStateNeuron(states=5)

# --- Envia inputs ---
for cat in categories:
    for i in range(inputs_per_category):
        neuron.forward(f"{cat}_input_{i}", category=cat)

# --- Gera relatório ---
neuron.report()