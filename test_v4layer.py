from core.v4_layer import V4Layer

layer = V4Layer(num_neurons=4, states=3)

print(layer.forward("teste 1"))
print(layer.forward("teste 2"))
print(layer.forward("teste 3"))