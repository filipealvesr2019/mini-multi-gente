# test_neuron_competition_v18.py
import numpy as np

# Configurações
ESTADOS = 5
CATEGORIAS = ["texto", "codigo", "matematica", "planejamento"]
MAX_AFFINITY = 10.0
DECAY = 0.01
ITERACOES = 2500

class SistemaMultiEstado:
    def __init__(self):
        # Score e afinidade para cada estado x categoria
        self.score = np.zeros((ESTADOS, len(CATEGORIAS)))
        self.affinity = np.ones((ESTADOS, len(CATEGORIAS)))  # Começa com 1 para todos
     
    def step(self, categoria):
        idx = CATEGORIAS.index(categoria)
        
        # Probabilidade proporcional à afinidade + chance mínima
        affinity = self.affinity[:, idx] + 0.1  # evita zeros
        prob = affinity / np.sum(affinity)
        
        # Escolhe o vencedor com base em probabilidade
        winner = np.random.choice(range(ESTADOS), p=prob)
        
        # Atualiza score e afinidade
        self.score[winner, idx] += 1
        self.affinity[winner, idx] += 1
        if self.affinity[winner, idx] > MAX_AFFINITY:
            self.affinity[winner, idx] = MAX_AFFINITY
        
        # Decaimento suave de afinidade
        self.affinity = np.maximum(self.affinity - DECAY, 0)
        
        return winner

def simular(seed):
    np.random.seed(seed)
    sistema = SistemaMultiEstado()
    
    estado_counts = np.zeros(ESTADOS, dtype=int)
    categoria_counts = np.zeros((ESTADOS, len(CATEGORIAS)), dtype=int)
    
    for _ in range(ITERACOES):
        categoria = np.random.choice(CATEGORIAS)
        estado = sistema.step(categoria)
        estado_counts[estado] += 1
        categoria_counts[estado, CATEGORIAS.index(categoria)] += 1
    
    return estado_counts, categoria_counts, sistema.affinity

def relatorio(estado_counts, categoria_counts, affinities, seed):
    print(f"\n--- SEED {seed} ---\n")
    
    print("=== DISTRIBUIÇÃO GLOBAL ===\n")
    for i, count in enumerate(estado_counts):
        pct = count / np.sum(estado_counts) * 100
        print(f"Estado {i}: {count} vitórias ({pct:.2f}%)")
    
    print("\n=== ESPECIALIZAÇÃO POR CATEGORIA ===\n")
    for i in range(ESTADOS):
        print(f"Estado {i}")
        for j, cat in enumerate(CATEGORIAS):
            cat_count = categoria_counts[i, j]
            cat_pct = cat_count / np.sum(categoria_counts[i]) * 100 if np.sum(categoria_counts[i]) > 0 else 0
            print(f"  {cat}: {cat_count} ({cat_pct:.2f}%)")
        print()
    
    print("=== AFINIDADES FINAIS ===\n")
    for i in range(ESTADOS):
        print(f"Estado {i}")
        for j, cat in enumerate(CATEGORIAS):
            print(f"  {cat}: {affinities[i,j]:.2f}")
        print()

if __name__ == "__main__":
    seeds = [42, 123, 999]
    for s in seeds:
        estado_counts, categoria_counts, affinities = simular(s)
        relatorio(estado_counts, categoria_counts, affinities, s)
    
    print("Fim do relatório.")