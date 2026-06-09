import numpy as np

MAX_AFFINITY = 10.0
DECAY = 0.01


class SistemaMultiEstado:

    def __init__(self, num_estados=5, categorias=None):

        if categorias is None:
            categorias = [
                "react",
                "javascript",
                "css",
                "figma",
                "prompts",
                "reasoning",
                "llm",
                "agents"
            ]

        self.categorias = categorias
        self.num_estados = num_estados

        self.score = np.zeros(
            (num_estados, len(categorias))
        )

        self.affinity = np.ones(
            (num_estados, len(categorias))
        )

    def step(self, categoria):

        if categoria not in self.categorias:
            return 0

        idx = self.categorias.index(categoria)

        affinity = self.affinity[:, idx] + 0.1

        prob = affinity / np.sum(affinity)

        winner = np.random.choice(
            range(self.num_estados),
            p=prob
        )

        self.score[winner, idx] += 1

        self.affinity[winner, idx] += 1

        if self.affinity[winner, idx] > MAX_AFFINITY:
            self.affinity[winner, idx] = MAX_AFFINITY

        self.affinity = np.maximum(
            self.affinity - DECAY,
            0
        )

        return winner