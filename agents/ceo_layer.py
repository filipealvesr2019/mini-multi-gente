from core.v4_layer import V4Layer

class CEOAgent:
    def __init__(self):
        self.layer = V4Layer(num_neurons=4, states=3)

    def forward(self, task):
        return self.layer.forward(task)