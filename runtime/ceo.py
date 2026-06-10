# runtime/ceo.py

from runtime.manager import Manager


class CEO:

    def __init__(
        self,
        name,
        persona,
        skills,
        llm=None
    ):
        self.name = name
        self.persona = persona
        self.skills = skills
        self.llm = llm

        self.manager = Manager()

    def think(self, objective):
        """
        CEO analisa objetivo.
        Não executa nada.
        Apenas produz um plano.
        """

        if not self.llm:
            raise Exception("CEO sem LLM configurada")

        prompt = f"""
Você é o CEO.

Nome: {self.name}

Persona:
{self.persona}

Skills:
{", ".join(self.skills)}

Objetivo:
{objective}

Crie um plano operacional para atingir esse objetivo.

Retorne JSON.
"""

        return self.llm.generate(prompt)

    def execute(self, objective):

        print(f"\n[CEO {self.name}] analisando objetivo")

        plan = self.think(objective)

        print(f"\n[CEO {self.name}] plano criado")

        return self.manager.execute_plan(plan)

    def command(self, text):

        return self.manager.command(text)