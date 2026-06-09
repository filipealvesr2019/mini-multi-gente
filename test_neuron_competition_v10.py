from core.neuron_multistate import MultiStateNeuron
import random


neuron = MultiStateNeuron(states=5)

categorias = [
    "texto",
    "codigo",
    "matematica",
    "planejamento"
]

wins = {
    i: 0
    for i in range(5)
}

specialization = {
    i: {
        cat: 0
        for cat in categorias
    }
    for i in range(5)
}

TOTAL = 10000

for _ in range(TOTAL):

    categoria = random.choice(
        categorias
    )

    entrada = f"{categoria}_{random.randint(0,100000)}"

    estado = neuron.forward(
        entrada,
        categoria
    )

    wins[estado] += 1

    specialization[estado][categoria] += 1


print()
print("=== RELATÓRIO V10 ===")
print()

print("=== DISTRIBUIÇÃO GLOBAL ===")
print()

for state in range(5):

    pct = wins[state] / TOTAL * 100

    print(
        f"Estado {state}: "
        f"{wins[state]} vitórias "
        f"({pct:.2f}%)"
    )

print()
print("=== ESPECIALIZAÇÃO ===")
print()

for state in range(5):

    print()
    print(f"Estado {state}")

    total_state = wins[state]

    if total_state == 0:
        continue

    for cat in categorias:

        value = specialization[state][cat]

        pct = value / total_state * 100

        print(
            f"  {cat}: "
            f"{value} "
            f"({pct:.2f}%)"
        )

print()
print("=== AFINIDADES FINAIS ===")
print()

for state in range(5):

    print()
    print(f"Estado {state}")

    for cat in categorias:

        affinity = neuron.affinity[state][cat]

        print(
            f"  {cat}: "
            f"{affinity:.2f}"
        )