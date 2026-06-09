# test_neuron_competition_v15.py
import random
import numpy as np

# =====================================================
# CONFIGURAÇÃO
# =====================================================
NUM_ESTADOS = 5
CATEGORIAS = ["texto", "codigo", "matematica", "planejamento"]
SEEDS = [42, 123, 999]

SIMULACOES = 5000

RUÍDO = 0.05          # evita colapso
RECOMPENSA = 0.1      # incremento por vitória
ESQUECIMENTO = 0.999  # decaimento da afinidade
PENALIDADE_CARGA = 0.05  # penaliza estados com excesso de uso

# =====================================================
# FUNÇÕES AUXILIARES
# =====================================================
def softmax(x):
    x = np.array(x, dtype=np.float64)
    x = x - np.max(x)
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x)

# =====================================================
# CLASSE MULTI-ESTADO
# =====================================================
class MultiEstado:
    def __init__(self):
        # afinidade inicial igual para todos
        self.afinidade = np.ones((NUM_ESTADOS, len(CATEGORIAS)), dtype=np.float64)
        # histórico de uso por estado (para penalidade de carga)
        self.uso_estado = np.zeros(NUM_ESTADOS, dtype=np.float64)

    def step(self, categoria):
        cat_idx = CATEGORIAS.index(categoria)
        # score = afinidade + ruído - penalidade por excesso de carga
        score = (
            self.afinidade[:, cat_idx]
            + np.random.random(NUM_ESTADOS) * RUÍDO
            - PENALIDADE_CARGA * (self.uso_estado / max(1, np.sum(self.uso_estado)))
        )
        probs = softmax(score)
        estado = np.random.choice(NUM_ESTADOS, p=probs)
        # atualizar afinidade e histórico de uso
        self.afinidade[estado, cat_idx] += RECOMPENSA
        self.afinidade *= ESQUECIMENTO  # decaimento
        self.uso_estado[estado] += 1
        return estado

# =====================================================
# SIMULAÇÃO
# =====================================================
def simular(seed):
    random.seed(seed)
    np.random.seed(seed)

    sistema = MultiEstado()
    estado_counts = np.zeros(NUM_ESTADOS, dtype=int)
    categoria_counts = np.zeros((NUM_ESTADOS, len(CATEGORIAS)), dtype=int)

    for _ in range(SIMULACOES):
        categoria = random.choice(CATEGORIAS)
        estado = sistema.step(categoria)
        estado_counts[estado] += 1
        categoria_counts[estado, CATEGORIAS.index(categoria)] += 1

    return estado_counts, categoria_counts, sistema.afinidade

# =====================================================
# RELATÓRIO
# =====================================================
def imprimir_relatorio(estado_counts, categoria_counts, afinidade):
    total = np.sum(estado_counts)

    print("\n=== DISTRIBUIÇÃO GLOBAL ===\n")
    for i, count in enumerate(estado_counts):
        pct = count / total * 100
        print(f"Estado {i}: {count} vitórias ({pct:.2f}%)")

    print("\n=== ESPECIALIZAÇÃO POR CATEGORIA ===\n")
    for i in range(NUM_ESTADOS):
        print(f"Estado {i}")
        total_estado = np.sum(categoria_counts[i])
        if total_estado == 0:
            total_estado = 1
        for j, cat in enumerate(CATEGORIAS):
            valor = categoria_counts[i, j]
            pct = valor / total_estado * 100
            print(f"  {cat}: {valor} ({pct:.2f}%)")
        print()

    print("=== AFINIDADES FINAIS ===\n")
    for i in range(NUM_ESTADOS):
        print(f"Estado {i}")
        for j, cat in enumerate(CATEGORIAS):
            print(f"  {cat}: {afinidade[i,j]:.2f}")
        print()

# =====================================================
# EXECUÇÃO PRINCIPAL
# =====================================================
if __name__ == "__main__":
    for seed in SEEDS:
        print(f"\n--- SEED {seed} ---")
        estado_counts, categoria_counts, afinidade = simular(seed)
        imprimir_relatorio(estado_counts, categoria_counts, afinidade)
    print("Fim do relatório.")