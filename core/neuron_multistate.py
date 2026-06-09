import random


class MultiStateNeuron:
    def __init__(self, states=5):
        self.states = states

        self.memory = {
            i: [] for i in range(states)
        }

        self.usage = {
            i: 0 for i in range(states)
        }

        self.affinity = {
            i: {
                "texto": 1.0,
                "codigo": 1.0,
                "matematica": 1.0,
                "planejamento": 1.0
            }
            for i in range(states)
        }

    def compete(self, category):

        scores = {}

        for state in range(self.states):

            affinity = self.affinity[state][category]

            fatigue = self.usage[state] * 0.002

            exploration = random.uniform(
                0,
                0.5
            )

            score = affinity + exploration - fatigue

            scores[state] = score

        winner = max(
            scores,
            key=scores.get
        )

        return winner

    def learn(
        self,
        state,
        category
    ):

        self.affinity[state][category] += 0.1

        self.usage[state] += 1

    def forward(
        self,
        x,
        category
    ):

        winner = self.compete(category)

        self.memory[winner].append(x)

        self.learn(
            winner,
            category
        )

        return winner