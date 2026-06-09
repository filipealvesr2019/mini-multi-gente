from core.neuron_multistate import MultiStateNeuron

n = MultiStateNeuron(states=3)

print(n.forward("hello"))
print(n.forward("world"))
print(n.forward("hello again"))