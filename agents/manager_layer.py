from core.v4_layer import V4Layer

class ManagerAgent:
    def __init__(self):
        self.layer = V4Layer(num_neurons=6, states=4)

    def forward(self, plan):
        return self.layer.forward(plan)