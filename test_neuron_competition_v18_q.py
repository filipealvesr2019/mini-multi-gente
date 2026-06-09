import numpy as np

# =========================
# CONFIGURAÇÕES
# =========================
ESTADOS = 5
CATEGORIAS = ["texto", "codigo", "matematica", "planejamento"]

DECAY = 0.02
ITERACOES = 2500


# =========================
# UTIL QUÂNTICO-CLÁSSICO
# =========================
def born_normalize(x):
    x = np.power(x, 2)  # regra de Born (amplitude^2)
    total = np.sum(x)
    if total == 0:
        return np.ones_like(x) / len(x)
    return x / total


# =========================
# SISTEMA MULTI-ESTADO (Q-LIKE)
# =========================
class SistemaMultiEstadoQ:

    def __init__(self):
        # "amplitudes" dos estados
        self.state = np.random.rand(ESTADOS, len(CATEGORIAS))

        # memória estatística
        self.score = np.zeros((ESTADOS, len(CATEGORIAS)))

    # =========================
    # PASSO PRINCIPAL
    # =========================
    def step(self, categoria):
        idx = CATEGORIAS.index(categoria)

        # 1. pega amplitudes do "mundo"
        amplitudes = self.state[:, idx] + 0.01

        # 2. converte em probabilidade (Born rule)
        prob = born_normalize(amplitudes)

        # 3. colapso (escolha do estado vencedor)
        winner = np.random.choice(range(ESTADOS), p=prob)

        # 4. aprendizado + interferência simples
        for i in range(ESTADOS):
            if i == winner:
                self.state[i, idx] += 0.25  # reforço construtivo
            else:
                self.state[i, idx] *= (1 - DECAY)  # decaimento (descoerência)

        # 5. registro
        self.score[winner, idx] += 1

        return winner


# =========================
# SIMULAÇÃO
# =========================
def simular(seed):
    np.random.seed(seed)

    sistema = SistemaMultiEstadoQ()

    estado_counts = np.zeros(ESTADOS, dtype=int)
    categoria_counts = np.zeros((ESTADOS, len(CATEGORIAS)), dtype=int)

    for _ in range(ITERACOES):
        categoria = np.random.choice(CATEGORIAS)
        estado = sistema.step(categoria)

        estado_counts[estado] += 1
        categoria_counts[estado, CATEGORIAS.index(categoria)] += 1

    return estado_counts, categoria_counts, sistema.state


# =========================
# RELATÓRIO
# =========================
def relatorio(estado_counts, categoria_counts, state, seed):
    print(f"\n--- SEED {seed} (v18-Q) ---\n")

    print("=== DISTRIBUIÇÃO GLOBAL ===\n")
    for i, c in enumerate(estado_counts):
        print(f"Estado {i}: {c} ({c/np.sum(estado_counts)*100:.2f}%)")

    print("\n=== ESPECIALIZAÇÃO ===\n")
    for i in range(ESTADOS):
        print(f"Estado {i}")
        for j, cat in enumerate(CATEGORIAS):
            total = np.sum(categoria_counts[i])
            pct = (categoria_counts[i, j] / total * 100) if total > 0 else 0
            print(f"  {cat}: {categoria_counts[i, j]} ({pct:.2f}%)")
        print()

    print("=== ESTADO FINAL (AMPLITUDES) ===\n")
    for i in range(ESTADOS):
        print(f"Estado {i}: {np.round(state[i], 3)}")


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    seeds = [42, 123, 999]

    for s in seeds:
        estado_counts, categoria_counts, state = simular(s)
        relatorio(estado_counts, categoria_counts, state, s)

    print("\nFim do relatório v18-Q.")