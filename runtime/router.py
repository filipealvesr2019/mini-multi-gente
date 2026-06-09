import numpy as np

from runtime.company_config import COMPANY_CONFIG
from core.neuron_multistate import SistemaMultiEstado

CATEGORIAS = []

for dep in COMPANY_CONFIG["departments"]:

    for skill in dep["manager"]["skills"]:

        if skill not in CATEGORIAS:
            CATEGORIAS.append(skill)

    for worker in dep["workers"]:

        for skill in worker["skills"]:

            if skill not in CATEGORIAS:
                CATEGORIAS.append(skill)

MAX_WORKERS = max(
    len(dep["workers"])
    for dep in COMPANY_CONFIG["departments"]
)

router_brain = SistemaMultiEstado(
    num_estados=MAX_WORKERS,
    categorias=CATEGORIAS
)


def escolher_worker_inteligente(
    workers,
    categoria
):

    if len(workers) == 1:
        return workers[0], 0

    if categoria not in CATEGORIAS:

        idx = np.random.randint(
            0,
            len(workers)
        )

        return workers[idx], idx

    cat_idx = CATEGORIAS.index(categoria)

    pesos = (
        router_brain.affinity[
            :len(workers),
            cat_idx
        ]
        + 0.1
    )

    prob = pesos / pesos.sum()

    estado_escolhido = np.random.choice(
        range(len(workers)),
        p=prob
    )

    return (
        workers[estado_escolhido],
        estado_escolhido
    )


def feedback_task(categoria):

    if categoria in CATEGORIAS:
        router_brain.step(categoria)