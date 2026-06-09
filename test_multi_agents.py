from runtime.pipeline import MultiOrgSystem

# instanciando o sistema
system = MultiOrgSystem()

# criar 50 inputs diferentes
tasks = [f"Tarefa {i}" for i in range(50)]

# armazenar todos os outputs
all_outputs = {"CEO": [], "Manager": [], "Worker": []}

for task in tasks:
    ceo_out = system.ceo.forward(task)
    all_outputs["CEO"].append(ceo_out)

    manager_out = system.manager.forward(ceo_out)
    all_outputs["Manager"].append(manager_out)

    worker_out = system.worker.forward(manager_out)
    all_outputs["Worker"].append(worker_out)

# análise simples: quantos estados diferentes cada neurônio ativou
def analyze(outputs, agent_name):
    print(f"\n--- {agent_name} ---")
    for neuron_idx in range(len(outputs[0])):
        neuron_states = [task[neuron_idx] for task in outputs]
        unique_states = set(neuron_states)
        print(f"Neuron {neuron_idx}: {len(unique_states)} estados diferentes")

# rodar análise
analyze(all_outputs["CEO"], "CEO")
analyze(all_outputs["Manager"], "Manager")
analyze(all_outputs["Worker"], "Worker")