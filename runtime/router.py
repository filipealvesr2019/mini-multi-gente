# runtime/router.py
from core.neuron_multistate import SistemaMultiEstado
from runtime.company_config import COMPANY_CONFIG
import numpy as np

# Inicializa o Sistema Multi-Estado do router
router_brain = SistemaMultiEstado()

# Categorias possíveis (skills principais)
CATEGORIAS = ["texto", "codigo", "matematica", "planejamento", "react", "css", "prompts"]

def escolher_worker_inteligente(workers, categoria):
    """
    Escolhe um worker baseado na afinidade do router.
    Retorna: (worker, estado)
    """
    if categoria not in CATEGORIAS:
        raise ValueError(f"Categoria '{categoria}' não está registrada no router.")

    idx = CATEGORIAS.index(categoria)
    # Cria pesos baseados na afinidade do router
    pesos = router_brain.affinity[:len(workers), idx] + 0.1
    prob = pesos / pesos.sum()
    estado_escolhido = np.random.choice(range(len(workers)), p=prob)
    return workers[estado_escolhido], estado_escolhido

def feedback_task(categoria):
    """
    Envia feedback para o router aprender com a execução da skill.
    """
    if categoria in CATEGORIAS:
        router_brain.step(categoria)