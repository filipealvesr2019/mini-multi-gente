# test_neuron_competition.py - V5.1
import random
from collections import defaultdict

class Estado:
    def __init__(self, id_estado, categorias):
        self.id = id_estado
        self.categorias = categorias

        # Afinidade inicial neutra
        self.afinidade = {c: 1.0 for c in categorias}

        # Experiência acumulada por categoria
        self.experiencia = {c: 0 for c in categorias}

        # Contador de vitórias totais
        self.vitorias = 0

        # Últimas vitórias para penalização de dominância
        self.recentes = 0

    def score(self, categoria):
        # score = afinidade + experiencia + aleatoriedade - penalização dominância
        return (
            self.afinidade[categoria]
            + 0.05 * self.experiencia[categoria]
            + random.uniform(0, 0.2)
            - 0.02 * self.recentes
        )

    def aprender(self, categoria):
        self.experiencia[categoria] += 1
        self.afinidade[categoria] += 0.02
        self.vitorias += 1
        self.recentes += 1

    def reset_recentes(self):
        self.recentes = 0


def escolher_estado(estados, categoria):
    return max(estados, key=lambda e: e.score(categoria))


def executar_treinamento():
    categorias = ["texto", "codigo", "matematica", "planejamento"]

    estados = [Estado(i, categorias) for i in range(5)]

    # Bônus inicial para forçar diversidade
    estados[0].afinidade['texto'] = 2.0
    estados[1].afinidade['codigo'] = 2.0
    estados[2].afinidade['matematica'] = 2.0
    estados[3].afinidade['planejamento'] = 2.0
    # Estado 4 neutro

    total_tarefas = 10000

    for _ in range(total_tarefas):
        categoria = random.choice(categorias)

        vencedor = escolher_estado(estados, categoria)
        vencedor.aprender(categoria)

        # Reset recente de todos a cada 50 tarefas
        if _ % 50 == 0:
            for e in estados:
                e.reset_recentes()

    return estados


def imprimir_relatorio(estados):
    print("\n=== RELATÓRIO V5.1 ===\n")

    total_vitorias = sum(e.vitorias for e in estados)

    print("=== DISTRIBUIÇÃO GLOBAL ===\n")
    for estado in estados:
        pct = (estado.vitorias / total_vitorias * 100) if total_vitorias > 0 else 0
        print(f"Estado {estado.id}: {estado.vitorias} vitórias ({pct:.2f}%)")

    print("\n=== ESPECIALIZAÇÃO POR CATEGORIA ===\n")
    for estado in estados:
        print(f"Estado {estado.id}")
        total = sum(estado.experiencia.values())
        for categoria, valor in estado.experiencia.items():
            pct = (valor / total * 100) if total > 0 else 0
            print(f"  {categoria}: {valor} ({pct:.2f}%)")

    print("\n=== AFINIDADES FINAIS ===\n")
    for estado in estados:
        print(f"Estado {estado.id}")
        for categoria, valor in estado.afinidade.items():
            print(f"  {categoria}: {valor:.2f}")


if __name__ == "__main__":
    estados = executar_treinamento()
    imprimir_relatorio(estados)