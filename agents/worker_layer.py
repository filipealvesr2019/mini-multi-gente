from core.v4_layer import V4Layer

class WorkerAgent:
    def __init__(self):
        self.layer = V4Layer(num_neurons=8, states=5)

    def forward(self, instruction):
        return self.layer.forward(instruction)