# runtime/planner.py

from runtime.llm_engine import LLMEngine
import json

class Planner:

    def __init__(self):
        self.llm = LLMEngine()

    def analyze(self, task_description):

        prompt = f"""
Analise a tarefa:

{task_description}

Retorne apenas JSON:

{{
    "company_type": "...",
    "departments": [
        {{
            "name": "...",
            "skills": [...]
        }}
    ]
}}
"""

        response = self.llm.generate(prompt)

        return json.loads(response)