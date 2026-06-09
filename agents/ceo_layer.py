from core.v4_layer import V4Layer

class CEOAgent:
    def __init__(self):
        self.layer = V4Layer(num_neurons=4, states=3)

    def forward(self, task):
        # Gera um plano de texto para cada neurônio
        plan = [f"{task} - passo {i}" for i in range(self.layer.num_neurons)]
        return plan