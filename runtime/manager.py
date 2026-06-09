from concurrent.futures import ThreadPoolExecutor
import threading
import time
from runtime.worker import Worker, tracker
from runtime.router import Router
from runtime.command_bus import CommandBus


class Manager:
    def __init__(self):
        self.bus = CommandBus()
        self.router = Router()
        self.workers = [
            Worker("Ana", "texto", self.bus),
            Worker("João", "codigo", self.bus),
            Worker("Pedro", "matematica", self.bus),
            Worker("Marina", "planejamento", self.bus)
        ]

    def divide_task(self, tarefa):
        return [
            {"categoria": "planejamento", "conteudo": f"Planejar projeto: {tarefa}"},
            {"categoria": "codigo", "conteudo": f"Criar código React: {tarefa}"},
            {"categoria": "texto", "conteudo": f"Documentar interface: {tarefa}"},
            {"categoria": "matematica", "conteudo": f"Implementar cálculos: {tarefa}"}
        ]

    def dashboard_loop(self):
        while True:
            print("\n" * 2)
            print("=" * 60)
            print("CEO DASHBOARD")
            print("=" * 60)
            concluidos = 0
            for w in self.workers:
                print(f"{w.nome:<12}{w.especialidade:<15}{w.status:<20}{w.progress}% | avg {tracker.average_time(w.nome):.2f}s")
                if w.status == "concluído":
                    concluidos += 1
            if concluidos == len(self.workers):
                break
            time.sleep(1)

    def execute_subtasks(self, subtasks):
        dep_map = {
            "planejamento": [],
            "codigo": ["planejamento"],
            "texto": ["codigo"],
            "matematica": ["texto"]
        }

        name_map = {w.especialidade: w for w in self.workers}

        for key, deps in dep_map.items():
            for dep in deps:
                if dep in name_map:
                    name_map[key].dependency_done = False

        dashboard = threading.Thread(target=self.dashboard_loop)
        dashboard.start()

        def executar(sub):
            # escolhe worker com melhor performance
            candidates = [w for w in self.workers if w.especialidade == sub["categoria"]]
            if not candidates:
                worker = self.workers[0]
            else:
                worker = min(candidates, key=lambda w: tracker.average_time(w.nome))

            worker.dependency_done = all(
                name_map[d].status == "concluído" for d in dep_map[sub["categoria"]]
            )
            res = worker.run_task(sub["conteudo"])

            for k, deps in dep_map.items():
                if sub["categoria"] in deps:
                    name_map[k].dependency_done = True
            return res

        resultados = []
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(executar, s) for s in subtasks]
            for f in futures:
                resultados.append(f.result())

        dashboard.join()
        return resultados

    # comandos humanos
    def command(self, cmd):
        tokens = cmd.strip().split()
        if not tokens:
            return
        if tokens[0].lower() == "status":
            for w in self.workers:
                print(f"{w.nome:<12}{w.especialidade:<15}{w.status:<20}{w.progress}% | avg {tracker.average_time(w.nome):.2f}s")
        elif tokens[0].lower() == "tarefas":
            for w in self.workers:
                print(f"{w.nome:<12}{w.current_task}")
        elif tokens[0].lower() == "parar" and len(tokens) == 2:
            for w in self.workers:
                if w.nome.lower() == tokens[1].lower():
                    w.paused = True
                    print(f"{w.nome} pausado")
        elif tokens[0].lower() == "reiniciar" and len(tokens) == 2:
            for w in self.workers:
                if w.nome.lower() == tokens[1].lower():
                    w.paused = False
                    print(f"{w.nome} reiniciado")
        elif tokens[0].lower() == "msg" and len(tokens) >= 3:
            target = tokens[1]
            message = " ".join(tokens[2:])
            self.bus.send(target, message)
            print(f"Mensagem enviada para {target}")
        else:
            print("Comando desconhecido")