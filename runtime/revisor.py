# runtime/revisor.py
class Revisor:
    def revisar(self, outputs):
        revisado = []
        for o in outputs:
            if not o.strip():
                revisado.append("[ERRO DETECTADO]")
            else:
                revisado.append(o)
        return "\n".join(revisado)