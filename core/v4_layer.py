from core.neuron_multistate import MultiStateNeuron

class V4Layer:
    def __init__(self, num_neurons=8, states=5):
        self.num_neurons = num_neurons  # adicionar isso
        self.neurons = [MultiStateNeuron(states) for _ in range(num_neurons)]

    def forward(self, x):
        outputs = []
        for i, neuron in enumerate(self.neurons):
            input_i = f"{x}_{i}"
            outputs.append(neuron.forward(input_i))
        return outputs  # retorna todos os neurônios