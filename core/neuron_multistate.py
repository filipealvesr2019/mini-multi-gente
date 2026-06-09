import os

class MultiStateNeuron:
    def __init__(self, states=3):
        self.states = states
        self.memory = {i: [] for i in range(states)}

    def forward(self, x):
        state = self.select_state(x)
        self.memory[state].append(x)
        return f"state_{state}_output"

    def select_state(self, x):
        # Usa hash para distribuir inputs nos estados
        return hash(str(x)) % self.states

        import json

def log_neuron(agent_name, neuron_idx, input_value, output_value):
    os.makedirs("logs", exist_ok=True)
    log_file = f"logs/{agent_name}_neuron_{neuron_idx}.json"
    with open(log_file, "a") as f:
        json.dump({"input": input_value, "output": output_value}, f)
        f.write("\n")