# test_neuron_competition_v14.py

import random
import numpy as np

# =====================================================
# CONFIG
# =====================================================

NUM_ESTADOS = 5

CATEGORIAS = [
    "texto",
    "codigo",
    "matematica",
    "planejamento"
]

SEEDS = [42, 123, 999]

SIMULACOES = 5000

PENALTY_OVERLAP = 0.05
BOOST_ESPECIALIZACAO = 0.50

# especialista artificial por categoria
ESPECIALIZACAO = {
    "texto": 0,
    "codigo": 1,
    "matematica": 2,
    "planejamento": 3
}


# =====================================================
# UTIL
# =====================================================

def softmax(x):
    x = np.array(x, dtype=np.float64)

    x = x - np.max(x)

    exp_x = np.exp(x)

    return exp_x / np.sum(exp_x)


# =====================================================
# MULTI ESTADO
# =====================================================

class MultiEstado:

    def __init__(self):

        self.score = np.random.rand(
            NUM_ESTADOS,
            len(CATEGORIAS)
        )

    def selecionar_estado(self, categoria):

        cat_idx = CATEGORIAS.index(categoria)

        scores = self.score[:, cat_idx].copy()

        # ruído anti-colapso
        scores += np.random.random(NUM_ESTADOS) * 0.1

        # especialista artificial
        dominante = ESPECIALIZACAO[categoria]
        scores[dominante] += BOOST_ESPECIALIZACAO

        probs = softmax(scores)

        estado = np.random.choice(
            NUM_ESTADOS,
            p=probs
        )

        return estado

    def atualizar(self, estado, categoria):

        cat_idx = CATEGORIAS.index(categoria)

        # recompensa
        self.score[estado, cat_idx] += 0.1

        # overlap somente da categoria atual
        overlap = np.mean(
            self.score[:, cat_idx]
        )

        self.score[:, cat_idx] -= (
            PENALTY_OVERLAP * overlap
        )

        self.score = np.clip(
            self.score,
            0.0,
            None
        )

    def step(self, categoria):

        estado = self.selecionar_estado(
            categoria
        )

        self.atualizar(
            estado,
            categoria
        )

        return estado


# =====================================================
# SIMULACAO
# =====================================================

def simular(seed):

    random.seed(seed)
    np.random.seed(seed)

    sistema = MultiEstado()

    estado_counts = np.zeros(
        NUM_ESTADOS,
        dtype=int
    )

    categoria_counts = np.zeros(
        (
            NUM_ESTADOS,
            len(CATEGORIAS)
        ),
        dtype=int
    )

    for _ in range(SIMULACOES):

        categoria = random.choice(
            CATEGORIAS
        )

        estado = sistema.step(
            categoria
        )

        estado_counts[estado] += 1

        categoria_counts[
            estado,
            CATEGORIAS.index(categoria)
        ] += 1

    return (
        estado_counts,
        categoria_counts,
        sistema.score
    )


# =====================================================
# RELATORIO
# =====================================================

def imprimir_relatorio(
    estado_counts,
    categoria_counts,
    score
):

    total = np.sum(
        estado_counts
    )

    print()
    print("=== DISTRIBUIÇÃO GLOBAL ===")
    print()

    for i, count in enumerate(
        estado_counts
    ):

        pct = (
            count /
            total *
            100
        )

        print(
            f"Estado {i}: "
            f"{count} vitórias "
            f"({pct:.2f}%)"
        )

    print()
    print("=== ESPECIALIZAÇÃO POR CATEGORIA ===")
    print()

    for estado in range(
        NUM_ESTADOS
    ):

        print(
            f"Estado {estado}"
        )

        total_estado = np.sum(
            categoria_counts[
                estado
            ]
        )

        if total_estado == 0:
            total_estado = 1

        for cat_idx, cat in enumerate(
            CATEGORIAS
        ):

            valor = categoria_counts[
                estado,
                cat_idx
            ]

            pct = (
                valor /
                total_estado *
                100
            )

            print(
                f"  {cat}: "
                f"{valor} "
                f"({pct:.2f}%)"
            )

        print()

    print("=== AFINIDADES FINAIS ===")
    print()

    for estado in range(
        NUM_ESTADOS
    ):

        print(
            f"Estado {estado}"
        )

        for cat_idx, cat in enumerate(
            CATEGORIAS
        ):

            print(
                f"  {cat}: "
                f"{score[estado, cat_idx]:.2f}"
            )

        print()


# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    for seed in SEEDS:

        print()
        print(
            f"--- SEED {seed} ---"
        )

        (
            estado_counts,
            categoria_counts,
            score
        ) = simular(seed)

        imprimir_relatorio(
            estado_counts,
            categoria_counts,
            score
        )

    print("Fim do relatório.")