class MultiStateNeuron:
    def __init__(self, states=2):
        self.states = states
        self.memory = {i: [] for i in range(states)}

    def forward(self, x):
        state = self.select_state(x)
        self.memory[state].append(x)
        return f"state_{state}_output"

    def select_state(self, x):
        return hash(str(x)) % self.states