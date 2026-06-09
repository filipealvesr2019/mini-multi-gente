import random

def escolher_worker_inteligente(workers, required_skill):
    filtered = [w for w in workers if required_skill in w.skills]
    if not filtered:
        filtered = workers
    worker = random.choice(filtered)
    return worker, 0

def feedback_task(skill):
    # futuramente aprende com execução
    pass