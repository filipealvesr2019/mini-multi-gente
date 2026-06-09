import random
from collections import defaultdict

class MultiStateNeuron:
    def __init__(self, states=5, categories=None):
        self.states = states
        self.categories = categories or ["texto", "codigo", "matematica", "planejamento"]
        self.usage_count = {i:0 for i in range(states)}
        # afinidades por estado e categoria
        self.affinities = {i:{cat:1.0 for cat in self.categories} for i in range(states)}

    def forward(self, x, category):
        # Seleciona o estado com maior afinidade
        affinities = [self.affinities[s][category] for s in range(self.states)]
        state = affinities.index(max(affinities))
        # conta uso
        self.usage_count[state] += 1
        return state

    def update_affinity(self, state, category, delta=0.05):
        self.affinities[state][category] += delta
        # manter valores razoáveis
        if self.affinities[state][category] > 1000:
            self.affinities[state][category] = 1000