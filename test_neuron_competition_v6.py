import random
import math
from collections import defaultdict

# Configurações
ESTADOS = 5
CATEGORIAS = ["texto", "codigo", "matematica", "planejamento"]
EPSILON = 0.05  # chance de exploração
PASSOS = 5000    # número de competições

class Estado:
    def __init__(self):
        self.afinidade = {cat: 1.0 for cat in CATEGORIAS}
        self.experiencia = {cat: 0 for cat in CATEGORIAS}

    def score(self, categoria):
        # Log da experiência para crescimento controlado
        return self.afinidade[categoria] + math.log1p(self.experiencia[categoria])

    def aprender(self, categoria):
        self.experiencia[categoria] += 1
        self.afinidade[categoria] += 0.01
        # Esquecimento leve para as outras categorias
        for cat in self.afinidade:
            if cat != categoria:
                self.afinidade[cat] *= 0.999

# Inicializa estados
estados = [Estado() for _ in range(ESTADOS)]

# Contadores de vitórias
vitorias = [0 for _ in range(ESTADOS)]

# Contadores por categoria
vitorias_categoria = [defaultdict(int) for _ in range(ESTADOS)]

# Softmax helper
def softmax(scores):
    max_score = max(scores)
    exp_scores = [math.exp(s - max_score) for s in scores]
    s = sum(exp_scores)
    return [e/s for e in exp_scores]

# Simulação
for _ in range(PASSOS):
    categoria = random.choice(CATEGORIAS)
    scores = [estado.score(categoria) for estado in estados]

    # Exploração: epsilon-greedy
    if random.random() < EPSILON:
        vencedor_idx = random.randint(0, ESTADOS-1)
    else:
        probs = softmax(scores)
        r = random.random()
        cumul = 0
        for i, p in enumerate(probs):
            cumul += p
            if r <= cumul:
                vencedor_idx = i
                break

    vitorias[vencedor_idx] += 1
    vitorias_categoria[vencedor_idx][categoria] += 1
    estados[vencedor_idx].aprender(categoria)

# Relatório final
print("\n=== RELATÓRIO V6 ===\n")
print("=== DISTRIBUIÇÃO GLOBAL ===\n")
for i, v in enumerate(vitorias):
    print(f"Estado {i}: {v} vitórias ({v/PASSOS*100:.2f}%)")

print("\n=== ESPECIALIZAÇÃO POR CATEGORIA ===\n")
for i, vc in enumerate(vitorias_categoria):
    print(f"Estado {i}")
    for cat in CATEGORIAS:
        print(f"  {cat}: {vc[cat]} ({vc[cat]/sum(vc.values())*100:.2f}%)")
    print("")

print("=== AFINIDADES FINAIS ===\n")
for i, e in enumerate(estados):
    print(f"Estado {i}")
    for cat in CATEGORIAS:
        print(f"  {cat}: {e.afinidade[cat]:.2f}")
    print("")