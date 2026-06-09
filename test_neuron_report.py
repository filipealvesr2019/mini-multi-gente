# test_neuron_report.py
from collections import Counter

# --- Definição do neurônio multiestado ---
class MultiStateNeuron:
    def __init__(self, states=5):
        self.states = states
        self.state_counter = Counter()

    def select_state(self, x):
        # Hash simples para escolher estado
        return hash(str(x)) % self.states

    def forward(self, x):
        state = self.select_state(x)
        self.state_counter[state] += 1
        return f"state_{state}_output"

    def report(self):
        total = sum(self.state_counter.values())
        print("\n=== RELATÓRIO DE ESTADOS ===")
        for state, count in sorted(self.state_counter.items()):
            pct = count / total * 100
            print(f"Estado {state}: {count} usos ({pct:.2f}%)")


# --- Teste com 1000 inputs ---
if __name__ == "__main__":
    neuron = MultiStateNeuron(states=5)
    for i in range(1000):
        neuron.forward(f"Tarefa {i}")

    # Mostra relatório
    neuron.report()