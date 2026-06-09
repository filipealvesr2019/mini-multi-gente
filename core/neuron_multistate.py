import random


class MultiStateNeuron:
    def __init__(self, states=5):

        self.states = states

        self.categories = [
            "texto",
            "codigo",
            "matematica",
            "planejamento"
        ]

        self.memory = {
            i: [] for i in range(states)
        }

        self.usage = {
            i: 0 for i in range(states)
        }

        self.affinity = {
            i: {
                cat: 1.0
                for cat in self.categories
            }
            for i in range(states)
        }

    def compete(self, category):

        scores = {}

        for state in range(self.states):

            affinity = self.affinity[state][category]

            fatigue = self.usage[state] * 0.0005

            exploration = random.uniform(
                0,
                0.3
            )

            scores[state] = (
                affinity
                + exploration
                - fatigue
            )

        winner = max(
            scores,
            key=scores.get
        )

        return winner

    def normalize_category(self, category):

        total = sum(
            self.affinity[s][category]
            for s in range(self.states)
        )

        if total == 0:
            return

        target_total = self.states

        for state in range(self.states):

            self.affinity[state][category] = (
                self.affinity[state][category]
                / total
            ) * target_total

    def learn(
        self,
        winner,
        category
    ):

        self.affinity[winner][category] += 0.10

        for state in range(self.states):

            if state != winner:

                self.affinity[state][category] -= 0.02

                if self.affinity[state][category] < 0.10:

                    self.affinity[state][category] = 0.10

        self.normalize_category(category)

        self.usage[winner] += 1

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